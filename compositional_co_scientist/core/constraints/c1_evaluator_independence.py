"""C1 constraint: Evaluator Independence enforcement.

This constraint ensures that the evaluator model is different from the generator model
to prevent self-reinforcing bias in hypothesis evaluation.
"""
from compositional_co_scientist.core.errors import ConstraintViolationError


def check_evaluator_independence(generator_model: str, evaluator_model: str) -> bool:
    """Check that the evaluator model is independent from the generator model.

    Args:
        generator_model: Name/ID of the model used for hypothesis generation.
        evaluator_model: Name/ID of the model used for hypothesis evaluation.

    Returns:
        True if models are different (constraint satisfied).

    Raises:
        ConstraintViolationError: If the same model is used for both generation and evaluation.
    """
    if generator_model == evaluator_model:
        raise ConstraintViolationError(f"C1 violated: models must differ")
    return True
