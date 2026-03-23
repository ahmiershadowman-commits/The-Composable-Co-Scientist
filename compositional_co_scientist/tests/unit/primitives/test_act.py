"""Tests for ACT primitive."""

from compositional_co_scientist.core.primitives.act import act


def test_act_invokes_tool():
    result = act("search", {"query": "test"}, {"allowed_tools": ["search"]})
    assert "result" in result
    assert result["validation"] is True


def test_act_blocks_unauthorized_tool():
    result = act("exec", {"cmd": "rm -rf"}, {"allowed_tools": ["search"]})
    assert result["validation"] is False
    assert "error" in result
