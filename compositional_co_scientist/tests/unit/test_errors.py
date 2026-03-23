import pytest
from compositional_co_scientist.core.errors import (
    CompositionalCoScientistError,
    ConstraintViolationError,
    PrimitiveFailureError,
    StorageError,
    InvalidTransitionError,
    LogCompletenessError,
    SandboxViolationError
)

def test_error_inheritance():
    assert issubclass(ConstraintViolationError, CompositionalCoScientistError)
    assert issubclass(PrimitiveFailureError, CompositionalCoScientistError)
    assert issubclass(InvalidTransitionError, ConstraintViolationError)

def test_user_message_format():
    try:
        raise ConstraintViolationError("C1 violated")
    except ConstraintViolationError as e:
        assert "safety constraint was violated" in e.user_message
        assert e.severity == "CRITICAL"
