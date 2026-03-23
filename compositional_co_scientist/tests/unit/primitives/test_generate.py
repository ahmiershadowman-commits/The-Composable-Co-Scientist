"""Tests for the GENERATE primitive."""
from compositional_co_scientist.core.primitives.generate import generate


def test_generate_produces_candidates():
    """Test that generate produces candidate hypotheses with diversity scoring."""
    candidates = generate(
        goal="What causes superconductivity?",
        constraints={"max_candidates": 5},
        temperature=0.7
    )
    assert len(candidates["candidates"]) >= 3
    assert "diversity_score" in candidates
    assert candidates["diversity_score"] > 0
