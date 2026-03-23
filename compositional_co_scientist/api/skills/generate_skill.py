"""Generate skill wrapper for the GENERATE primitive.

Use when generating candidate hypotheses or solutions for a research goal or question.
Triggers the GENERATE primitive (P1) to produce diverse candidates.
"""
from typing import Dict, Any

from compositional_co_scientist.core.primitives.generate import generate as generate_primitive
from compositional_co_scientist.core.models.candidate import Candidate


def generate(goal: str, constraints: Dict[str, Any] = None, temperature: float = 0.7) -> Dict[str, Any]:
    """Generate candidate hypotheses for a given goal.

    Args:
        goal: The research goal or question to generate hypotheses for.
        constraints: Constraints for generation (e.g., max_candidates).
        temperature: Temperature parameter for generation diversity (0.0-1.0).

    Returns:
        Dictionary containing:
            - candidates: List of generated Candidate objects
            - diversity_score: Score indicating diversity among candidates (0.0-1.0)
    """
    if constraints is None:
        constraints = {}

    result = generate_primitive(goal, constraints, temperature)

    # Convert candidates to serializable format
    candidates_data = [
        {
            "id": c.id,
            "goal_id": c.goal_id,
            "content": c.content,
            "metadata": c.metadata,
            "created_at": c.created_at.isoformat()
        }
        for c in result["candidates"]
    ]

    return {
        "candidates": candidates_data,
        "diversity_score": result["diversity_score"]
    }
