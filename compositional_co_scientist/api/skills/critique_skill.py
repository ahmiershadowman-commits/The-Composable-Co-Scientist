"""Critique skill wrapper for the CRITIQUE primitive.

Use when identifying defects or quality issues in candidate hypotheses.
Triggers the CRITIQUE primitive (P3).
"""
from typing import Dict, Any, List

from compositional_co_scientist.core.primitives.critique import critique as critique_primitive
from compositional_co_scientist.core.models.candidate import Candidate


def critique(candidates: List[Dict[str, Any]], defect_taxonomy: List[str] = None) -> Dict[str, Any]:
    """Critique candidates to identify defects using a defect taxonomy.

    Args:
        candidates: List of candidate dictionaries with id and content.
        defect_taxonomy: List of defect types to check for.

    Returns:
        Dictionary containing:
            - defects: List of Defect objects for each candidate
            - coverage: Coverage factor indicating how thoroughly candidates were analyzed (0.0-1.0)
    """
    if defect_taxonomy is None:
        defect_taxonomy = ["logical_fallacy", "unsupported_claim", "methodological_flaw", "bias"]

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

    result = critique_primitive(candidates_dict, defect_taxonomy)

    # Convert defects to serializable format
    defects_data = [
        {
            "candidate_id": d.candidate_id,
            "defect_type": d.defect_type,
            "description": d.description,
            "severity": d.severity,
            "created_at": d.created_at.isoformat()
        }
        for d in result["defects"]
    ]

    return {
        "defects": defects_data,
        "coverage": result["coverage"]
    }
