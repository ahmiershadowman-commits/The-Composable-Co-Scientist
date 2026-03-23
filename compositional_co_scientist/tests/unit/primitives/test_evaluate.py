"""Tests for the EVALUATE primitive."""
from compositional_co_scientist.core.primitives.evaluate import evaluate


def test_evaluate_scores_candidates():
    """Test that evaluate produces scores for candidates."""
    candidates = {"candidates": []}  # Mock
    scored = evaluate(candidates, rubric={"coherence": 0.5}, evaluator_model="gpt-4")
    assert "scores" in scored
