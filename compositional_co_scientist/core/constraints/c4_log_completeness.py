"""C4 constraint: Log Completeness enforcement.

This constraint ensures all EVALUATE operations are logged to the audit database
for reproducibility and calibration debugging.
"""
from typing import Dict, Any, Optional, Callable
from functools import wraps
import time


# Global state for tracking pending evaluations
_pending_evaluations: Dict[str, Dict[str, Any]] = {}


def log_start_evaluation(
    evaluation_id: str,
    candidates: list,
    rubric: Dict[str, float],
    evaluator_model: str
) -> str:
    """Log the start of an EVALUATE operation.

    Args:
        evaluation_id: Unique identifier for this evaluation.
        candidates: List of candidates being evaluated.
        rubric: Rubric criteria and weights.
        evaluator_model: Model used for evaluation.

    Returns:
        The evaluation_id for tracking.
    """
    _pending_evaluations[evaluation_id] = {
        "started_at": time.time(),
        "candidates": [c.get("id", str(i)) for i, c in enumerate(candidates)],
        "rubric": rubric,
        "evaluator_model": evaluator_model,
        "status": "in_progress"
    }
    return evaluation_id


def log_end_evaluation(
    evaluation_id: str,
    scores: list,
    log_func: Callable[[str, Dict[str, Any], str], Dict[str, Any]]
) -> Dict[str, Any]:
    """Log the completion of an EVALUATE operation.

    Args:
        evaluation_id: Unique identifier for this evaluation.
        scores: List of scores produced.
        log_func: Function to call for logging (e.g., log_skill.log).

    Returns:
        Log result from log_func.

    Raises:
        ValueError: If evaluation_id not found (start was not logged).
    """
    if evaluation_id not in _pending_evaluations:
        raise ValueError(
            f"C4 violation: Evaluation {evaluation_id} completed without start log. "
            "All EVALUATE operations must be logged."
        )

    start_info = _pending_evaluations[evaluation_id]
    duration = time.time() - start_info["started_at"]

    # Create audit log entry
    log_data = {
        "evaluation_id": evaluation_id,
        "evaluator_model": start_info["evaluator_model"],
        "num_candidates": len(start_info["candidates"]),
        "candidate_ids": start_info["candidates"],
        "rubric": start_info["rubric"],
        "scores": [s.get("score", 0) for s in scores],
        "duration_seconds": duration,
        "status": "completed"
    }

    # Remove from pending
    del _pending_evaluations[evaluation_id]

    # Log to audit database
    return log_func("EVALUATE", log_data, "INFO")


def check_log_completeness(
    log_func: Callable[[str, Dict[str, Any], str], Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Check C4: All EVALUATE operations have been logged.

    Args:
        log_func: Optional log function to record the audit check.

    Returns:
        Dictionary containing:
            - passed: True if all evaluations logged
            - incomplete_count: Number of incomplete evaluations
            - incomplete_ids: List of evaluation IDs not yet logged

    Raises:
        ConstraintViolationError: If incomplete evaluations found.
    """
    from compositional_co_scientist.core.errors import ConstraintViolationError

    incomplete_ids = list(_pending_evaluations.keys())

    if incomplete_ids:
        # Log the violation if log_func provided
        if log_func:
            log_func("C4_AUDIT", {
                "incomplete_count": len(incomplete_ids),
                "incomplete_ids": incomplete_ids
            }, "WARNING")

        raise ConstraintViolationError(
            f"C4 violated: {len(incomplete_ids)} EVALUATE operation(s) not logged. "
            f"Incomplete IDs: {incomplete_ids[:5]}{'...' if len(incomplete_ids) > 5 else ''}"
        )

    return {
        "passed": True,
        "incomplete_count": 0,
        "incomplete_ids": []
    }


def clear_pending():
    """Clear all pending evaluations.

    Use with caution - only for testing or recovery scenarios.
    """
    _pending_evaluations.clear()


def get_pending_count() -> int:
    """Get count of pending (incomplete) evaluations."""
    return len(_pending_evaluations)
