"""Command handlers for compositional co-scientist slash commands.

Provides handlers for /generate, /evaluate, and /synthesize commands.
"""
from typing import Dict, Any, Optional

from compositional_co_scientist.api.skills.generate_skill import generate as generate_skill
from compositional_co_scientist.api.skills.evaluate_skill import evaluate as evaluate_skill
from compositional_co_scientist.api.skills.synthesize_skill import synthesize as synthesize_skill
from compositional_co_scientist.api.skills.log_skill import log as log_skill


async def handle_generate(goal: str, max_candidates: int = 5, temperature: float = 0.7) -> Dict[str, Any]:
    """Handle the /generate command.

    Args:
        goal: The research goal or question to generate hypotheses for.
        max_candidates: Maximum number of candidates to generate.
        temperature: Temperature parameter for generation diversity.

    Returns:
        Dictionary containing generated candidates and diversity score.
    """
    constraints = {"max_candidates": max_candidates}

    result = generate_skill(goal, constraints, temperature)

    # Log the operation
    log_skill("GENERATE", {
        "goal": goal,
        "max_candidates": max_candidates,
        "temperature": temperature,
        "num_candidates": len(result["candidates"])
    })

    return result


async def handle_evaluate(
    candidates: list,
    rubric: Dict[str, float],
    evaluator_model: str
) -> Dict[str, Any]:
    """Handle the /evaluate command.

    Args:
        candidates: List of candidate dictionaries to evaluate.
        rubric: Dictionary of evaluation criteria and their weights.
        evaluator_model: Name/ID of the model used for evaluation.

    Returns:
        Dictionary containing scores and calibration factor.
    """
    result = evaluate_skill(candidates, rubric, evaluator_model)

    # Log the operation (C4 constraint: all EVALUATE operations must be logged)
    log_skill("EVALUATE", {
        "num_candidates": len(candidates),
        "rubric": rubric,
        "evaluator_model": evaluator_model,
        "scores": [s["score"] for s in result["scores"]]
    }, severity="INFO")

    return result


async def handle_synthesize(
    survivors: Dict[str, Any],
    context: Optional[Dict[str, Any]] = None,
    preserve_tensions: bool = True
) -> Dict[str, Any]:
    """Handle the /synthesize command.

    Args:
        survivors: SurvivorSet from SELECT primitive.
        context: ContextSet from RETRIEVE primitive (optional).
        preserve_tensions: Whether to preserve disagreements between candidates.

    Returns:
        Dictionary containing synthesized output, tension map, and confidence.
    """
    result = synthesize_skill(survivors, context, preserve_tensions)

    # Log the operation
    log_skill("SYNTHESIZE", {
        "num_survivors": len(survivors.get("survivors", [])),
        "preserve_tensions": preserve_tensions,
        "confidence": result["confidence"]
    })

    return result
