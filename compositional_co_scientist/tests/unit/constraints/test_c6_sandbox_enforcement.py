"""Tests for C6 sandbox enforcement constraint."""
import pytest
from compositional_co_scientist.core.constraints.c6_sandbox_enforcement import check_sandbox_permission
from compositional_co_scientist.core.errors import SandboxViolationError


def test_c6_allows_permitted_tool():
    """Test that C6 allows tools in the allowlist."""
    # Should not raise any exception
    check_sandbox_permission("search", {}, {"allowed_tools": ["search"]})


def test_c6_blocks_unpermitted_tool():
    """Test that C6 blocks tools not in the allowlist."""
    with pytest.raises(SandboxViolationError):
        check_sandbox_permission("exec", {}, {"allowed_tools": ["search"]})


def test_c6_handles_empty_allowlist():
    """Test that C6 blocks all tools when allowlist is empty."""
    with pytest.raises(SandboxViolationError):
        check_sandbox_permission("search", {}, {"allowed_tools": []})
