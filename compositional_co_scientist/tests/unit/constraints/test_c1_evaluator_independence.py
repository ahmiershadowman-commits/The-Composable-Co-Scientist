"""Tests for the C1 evaluator independence constraint."""
import pytest
from compositional_co_scientist.core.constraints.c1_evaluator_independence import check_evaluator_independence
from compositional_co_scientist.core.errors import ConstraintViolationError


def test_c1_allows_different_models():
    """Test that C1 allows different generator and evaluator models."""
    assert check_evaluator_independence("gpt-4", "claude-3") is True


def test_c1_blocks_same_model():
    """Test that C1 blocks using the same model for generator and evaluator."""
    with pytest.raises(ConstraintViolationError):
        check_evaluator_independence("gpt-4", "gpt-4")
