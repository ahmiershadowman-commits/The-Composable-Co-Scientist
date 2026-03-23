"""Tests for the SYNTHESIZE primitive."""
import pytest
from compositional_co_scientist.core.primitives.synthesize import synthesize


def test_synthesize_produces_output():
    """Test that SYNTHESIZE produces output with tension map."""
    output = synthesize({"survivors": []}, {"results": []}, preserve_tensions=True)
    
    assert "output" in output
    assert "tension_map" in output


def test_synthesize_includes_confidence():
    """Test that SYNTHESIZE includes confidence score."""
    output = synthesize({"survivors": []}, {"results": []}, preserve_tensions=True)
    
    assert "confidence" in output
    assert isinstance(output["confidence"], (int, float))


def test_synthesize_handles_empty_input():
    """Test that SYNTHESIZE handles empty input gracefully."""
    output = synthesize({"survivors": []}, {"results": []}, preserve_tensions=False)
    
    assert "output" in output
    assert "tension_map" in output
    assert "confidence" in output
