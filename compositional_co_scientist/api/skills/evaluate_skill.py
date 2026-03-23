"""Evaluate skill wrapper for the EVALUATE primitive.

Use when evaluating candidate hypotheses against a rubric.
Triggers the EVALUATE primitive (P2) with constraint C1 (evaluator independence).
"""
from typing import Dict, Any, List

from compositional_co_scientist.core.primitives.evaluate import evaluate as evaluate_primitive
from compositional_co_scientist.core.models.candidate import Candidate


def evaluate(candidates: List[Dict[str, Any]], rubric: Dict[str, float], evaluator_model: str) -> Dict[str, Any]:
    """Evaluate candidates against a rubric using an evaluator model.

    Args:
        candidates: List of candidate dictionaries with id and content.
        rubric: Dictionary of evaluation criteria and their weights.
        evaluator_model: Name/ID of the model used for evaluation.

    Returns:
        Dictionary containing:
            - scores: List of Score objects for each candidate
            - calibration: Calibration factor for the scores (default 1.0)

    Raises:
        ValueError: If evaluator_model is not specified (C1 constraint).
    """
    if not evaluator_model:
        raise ValueError("C1 constraint: evaluator_model must be specified (evaluator independence required)")

    # Convert input candidates to Candidate objects
    candidate_objs = [
        Candidate(
            id=c["id"],
            goal_id=c.get("goal_id", "unknown"),
            content=c["content"],
            metadata=c.get("metadata", {})
        )
        for c in candidates
    ]

    candidates_dict = {"candidates": candidate_objs}

    result = evaluate_primitive(candidates_dict, rubric, evaluator_model)

    # Convert scores to serializable format
    scores_data = [
        {
            "candidate_id": s.candidate_id,
            "evaluator_model": s.evaluator_model,
            "score": s.score,
            "rubric": s.rubric,
            "calibration": s.calibration,
            "created_at": s.created_at.isoformat()
        }
        for s in result["scores"]
    ]

    return {
        "scores": scores_data,
        "calibration": result["calibration"]
    }
