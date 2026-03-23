"""Synthesize skill wrapper for the SYNTHESIZE primitive.

Use when synthesizing surviving candidates into a coherent output.
Triggers the SYNTHESIZE primitive (P7).
"""
from typing import Dict, Any

from compositional_co_scientist.core.primitives.synthesize import synthesize as synthesize_primitive
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.document import Document


def synthesize(survivors: Dict[str, Any], context: Dict[str, Any] = None, preserve_tensions: bool = True) -> Dict[str, Any]:
    """Synthesize survivors into coherent output.

    Args:
        survivors: SurvivorSet from SELECT primitive containing:
            - survivors: List of selected candidate dictionaries
            - similarity_matrix: Dictionary mapping candidate pairs to similarity scores
        context: ContextSet from RETRIEVE primitive containing:
            - results: List of retrieved document dictionaries
        preserve_tensions: Whether to preserve disagreements between candidates.

    Returns:
        Dictionary containing:
            - output: Synthesized output string
            - tension_map: Dictionary mapping tensions between candidates
            - confidence: Confidence score for the synthesis (0.0-1.0)
    """
    if context is None:
        context = {}

    # Convert survivors to Candidate objects
    survivor_candidates = [
        Candidate(
            id=c["id"],
            goal_id=c.get("goal_id", "unknown"),
            content=c["content"],
            metadata=c.get("metadata", {})
        )
        for c in survivors.get("survivors", [])
    ]

    survivors_obj = {"survivors": survivor_candidates, "similarity_matrix": survivors.get("similarity_matrix", {})}

    # Convert context to Document objects
    context_docs = [
        Document(
            id=d["id"],
            source=d["source"],
            content=d["content"],
            metadata=d.get("metadata", {}),
            relevance_score=d.get("relevance_score", 1.0)
        )
        for d in context.get("results", [])
    ]

    context_obj = {"results": context_docs}

    result = synthesize_primitive(survivors_obj, context_obj, preserve_tensions)

    return {
        "output": result["output"],
        "tension_map": result["tension_map"],
        "confidence": result["confidence"]
    }
