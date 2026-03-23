"""ACT primitive (P6) - Invoke tools with sandbox enforcement."""

from typing import Dict, Any
from ..constraints.c6_sandbox_enforcement import check_sandbox_permission


def act(tool_name: str, params: Dict[str, Any], sandbox_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Invoke tool with sandbox enforcement.
    
    Args:
        tool_name: Tool to invoke
        params: Tool parameters
        sandbox_spec: Permission manifest
    
    Returns:
        Dict with result, validation, error
    """
    try:
        check_sandbox_permission(tool_name, params, sandbox_spec)
    except Exception as e:
        return {"result": None, "validation": False, "error": str(e)}
    return {"result": "Tool result", "validation": True, "error": None}
