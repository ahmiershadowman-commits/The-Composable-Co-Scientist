"""Tests for SYNTHESIZE primitive."""

from compositional_co_scientist.core.primitives.synthesize import synthesize


def test_synthesize_produces_output():
    output = synthesize({"survivors": []}, {"results": []}, preserve_tensions=True)
    assert "output" in output
    assert "tension_map" in output
    assert "confidence" in output


def test_synthesize_with_data():
    survivors = {"survivors": ["a", "b"]}
    context = {"results": ["doc1"]}
    output = synthesize(survivors, context, preserve_tensions=False)
    assert output["confidence"] == 0.8
