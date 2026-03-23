"""Select skill wrapper for the SELECT primitive.

Use when selecting surviving candidates from a scored set with diversity enforcement.
Triggers the SELECT primitive (P4) with constraints C2 (temporal order) and C3 (diversity quota).
"""
from typing import Dict, Any

from compositional_co_scientist.core.primitives.select import select as select_primitive
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score


def select(scored: Dict[str, Any], diversity_quota: float = 0.4) -> Dict[str, Any]:
    """Select surviving candidates from a scored set with diversity enforcement.

    Args:
        scored: Dictionary containing:
            - scores: List of score dictionaries from EVALUATE primitive
            - candidates: List of candidate dictionaries to select from
        diversity_quota: Fraction of top candidates to select (0.0-1.0).
                        Default 0.4 selects top 40% of candidates.

    Returns:
        Dictionary containing:
            - survivors: List of selected Candidate objects
            - similarity_matrix: Dictionary mapping candidate pairs to similarity scores
    """
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

    result = select_primitive(scored_dict, diversity_quota)

    # Convert survivors to serializable format
    survivors_data = [
        {
            "id": c.id,
            "goal_id": c.goal_id,
            "content": c.content,
            "metadata": c.metadata,
            "created_at": c.created_at.isoformat()
        }
        for c in result["survivors"]
    ]

    return {
        "survivors": survivors_data,
        "similarity_matrix": result["similarity_matrix"]
    }
