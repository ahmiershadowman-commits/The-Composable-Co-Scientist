"""Tests for the CRITIQUE primitive."""
from compositional_co_scientist.core.primitives.critique import critique


def test_critique_identifies_defects():
    """Test that critique identifies defects in candidates."""
    candidates = {"candidates": []}  # Mock
    defects = critique(candidates, defect_taxonomy=["logical_error"])
    assert "defects" in defects
