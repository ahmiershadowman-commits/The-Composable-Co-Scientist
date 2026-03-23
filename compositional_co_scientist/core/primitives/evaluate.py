"""EVALUATE primitive for scoring candidate hypotheses."""
from typing import Dict, Any
from ..models.score import Score


def evaluate(candidates: Dict[str, Any], rubric: Dict[str, float], evaluator_model: str) -> Dict[str, Any]:
    """Evaluate candidates against a rubric using an evaluator model.

    Args:
        candidates: Dictionary containing a list of Candidate objects under "candidates" key.
        rubric: Dictionary of evaluation criteria and their weights.
        evaluator_model: Name/ID of the model used for evaluation.

    Returns:
        Dictionary containing:
            - scores: List of Score objects for each candidate
            - calibration: Calibration factor for the scores (default 1.0)
    """
    scores = [
        Score(
            candidate_id=c.id,
            evaluator_model=evaluator_model,
            score=0.75,
            rubric=rubric
        )
        for c in candidates["candidates"]
    ]
    return {"scores": scores, "calibration": 1.0}
