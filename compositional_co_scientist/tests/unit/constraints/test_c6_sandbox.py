"""Tests for C6 Sandbox Enforcement."""

import pytest
from compositional_co_scientist.core.constraints.c6_sandbox_enforcement import check_sandbox_permission
from compositional_co_scientist.core.errors import SandboxViolationError


def test_c6_allows_permitted_tool():
    check_sandbox_permission("search", {}, {"allowed_tools": ["search"]})


def test_c6_blocks_unpermitted_tool():
    with pytest.raises(SandboxViolationError):
        check_sandbox_permission("exec", {}, {"allowed_tools": ["search"]})


def test_c6_empty_allowlist():
    with pytest.raises(SandboxViolationError):
        check_sandbox_permission("any", {}, {"allowed_tools": []})
