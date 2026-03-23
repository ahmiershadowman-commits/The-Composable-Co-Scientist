"""Tests for the ACT primitive."""
import pytest
from compositional_co_scientist.core.primitives.act import act


def test_act_invokes_tool():
    """Test that ACT invokes a tool and returns result."""
    result = act("search", {"query": "test"}, {"allowed_tools": ["search"]})
    
    assert "result" in result
    assert result["validation"] is True


def test_act_returns_error_on_validation_failure():
    """Test that ACT returns error when validation fails."""
    result = act("exec", {"command": "test"}, {"allowed_tools": ["search"]})
    
    assert "result" in result
    assert result["validation"] is False
    assert "error" in result


def test_act_handles_empty_sandbox():
    """Test that ACT handles empty sandbox spec gracefully."""
    result = act("search", {"query": "test"}, {})
    
    assert "result" in result
    assert "validation" in result
    assert "error" in result
