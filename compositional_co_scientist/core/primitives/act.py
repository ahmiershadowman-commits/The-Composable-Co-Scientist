"""ACT primitive for tool execution with sandbox enforcement.

This primitive executes tool operations while enforcing C6 sandbox
constraints to prevent unauthorized tool usage.
"""
from typing import Dict, Any
from compositional_co_scientist.core.constraints.c6_sandbox_enforcement import (
    check_sandbox_permission,
)
from compositional_co_scientist.core.errors import SandboxViolationError


def act(tool_name: str, params: Dict[str, Any], 
        sandbox_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a tool operation with sandbox enforcement.

    Args:
        tool_name: Name of the tool to execute.
        params: Parameters to pass to the tool.
        sandbox_spec: Sandbox specification containing:
            - allowed_tools: List of tool names permitted in the sandbox

    Returns:
        Dictionary containing:
            - result: Tool execution result (None if validation failed)
            - validation: Boolean indicating if the tool passed sandbox validation
            - error: Error message if validation failed (None otherwise)
    """
    try:
        # Enforce C6 sandbox constraint
        check_sandbox_permission(tool_name, params, sandbox_spec)
    except SandboxViolationError as e:
        return {
            "result": None,
            "validation": False,
            "error": str(e)
        }
    
    # Tool is permitted - in production, this would invoke the actual tool
    # For now, return a placeholder result
    return {
        "result": "Tool result",
        "validation": True,
        "error": None
    }
