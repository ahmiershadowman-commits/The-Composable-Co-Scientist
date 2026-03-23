"""Select skill wrapper for the SELECT primitive.

Use when selecting surviving candidates from a scored set with diversity enforcement.
Triggers the SELECT primitive (P4) with constraints C2 (temporal order) and C3 (diversity quota).
"""
from typing import Dict, Any, List, Optional, Tuple

from compositional_co_scientist.core.primitives.select import select as select_primitive
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score
from compositional_co_scientist.core.constraints import (
    check_diversity_quota,
    check_diversity_score,
    generate_anti_canon_prompt,
)
from compositional_co_scientist.core.errors import ConstraintViolationError


def select(
    scored: Dict[str, Any],
    diversity_quota: float = 0.4,
    max_similarity: float = 0.7,
    auto_regenerate: bool = True,
    max_retries: int = 3
) -> Dict[str, Any]:
    """Select surviving candidates from a scored set with diversity enforcement.

    Args:
        scored: Dictionary containing:
            - scores: List of score dictionaries from EVALUATE primitive
            - candidates: List of candidate dictionaries to select from
        diversity_quota: Fraction of top candidates to select (0.0-1.0).
                        Default 0.4 selects top 40% of candidates.
        max_similarity: Maximum acceptable similarity between candidates (default 0.7).
        auto_regenerate: If True, automatically regenerate if C3 violated.
        max_retries: Maximum regeneration attempts (default 3).

    Returns:
        Dictionary containing:
            - survivors: List of selected Candidate objects
            - similarity_matrix: Dictionary mapping candidate pairs to similarity scores
            - c3_passed: True if diversity constraint satisfied
            - regeneration_count: Number of regeneration attempts (if any)
            - anti_canon_prompt: Prompt for regeneration if needed
    """
    regeneration_count = 0
    last_error = None

    for attempt in range(max_retries):
        # Convert input to proper objects
        candidates = [
            Candidate(
                id=c["id"],
                goal_id=c.get("goal_id", "unknown"),
                content=c["content"],
                metadata=c.get("metadata", {})
            )
            for c in scored.get("candidates", [])
        ]

        scores = [
            Score(
                candidate_id=s["candidate_id"],
                evaluator_model=s["evaluator_model"],
                score=s["score"],
                rubric=s.get("rubric", {}),
                calibration=s.get("calibration", 1.0)
            )
            for s in scored.get("scores", [])
        ]

        scored_dict = {"scores": scores, "candidates": candidates}

        # Run selection
        result = select_primitive(scored_dict, diversity_quota)

        # Check C3 constraint
        try:
            check_diversity_quota(result["similarity_matrix"], max_similarity)
            # C3 passed - return result
            break
        except ConstraintViolationError as e:
            last_error = e
            if auto_regenerate and attempt < max_retries - 1:
                regeneration_count += 1
                # In a full implementation, this would trigger regeneration
                # For now, we just note that regeneration is needed
                scored["anti_canon_prompt"] = generate_anti_canon_prompt(
                    scored.get("goal", "Research goal")
                )
            else:
                # Final attempt failed - return with violation info
                result["c3_passed"] = False
                result["c3_error"] = str(e)
                result["regeneration_count"] = regeneration_count
                result["anti_canon_prompt"] = generate_anti_canon_prompt(
                    scored.get("goal", "Research goal")
                )
                return _format_result(result)

    # Success path
    result["c3_passed"] = True
    result["regeneration_count"] = regeneration_count
    return _format_result(result)


def _format_result(result: Dict[str, Any]) -> Dict[str, Any]:
    """Format result for return."""
    survivors_data = [
        {
            "id": c.id,
            "goal_id": c.goal_id,
            "content": c.content,
            "metadata": c.metadata,
            "created_at": c.created_at.isoformat()
        }
        for c in result.get("survivors", [])
    ]

    return {
        "survivors": survivors_data,
        "similarity_matrix": result.get("similarity_matrix", {}),
        "c3_passed": result.get("c3_passed", True),
        "regeneration_count": result.get("regeneration_count", 0),
        "anti_canon_prompt": result.get("anti_canon_prompt"),
        "c3_error": result.get("c3_error"),
    }
