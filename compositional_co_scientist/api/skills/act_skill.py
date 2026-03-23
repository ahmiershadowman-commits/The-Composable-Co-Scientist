"""Act skill wrapper for the ACT primitive.

Use when invoking external tools or actions with sandbox enforcement.
Triggers the ACT primitive (P6) with constraint C6 (sandbox enforcement).
"""
from typing import Dict, Any

from compositional_co_scientist.core.primitives.act import act as act_primitive


def act(tool_name: str, params: Dict[str, Any], sandbox_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Invoke tool with sandbox enforcement.

    Args:
        tool_name: Tool to invoke.
        params: Tool parameters.
        sandbox_spec: Permission manifest for sandbox enforcement.

    Returns:
        Dictionary containing:
            - result: Tool result (if successful)
            - validation: Boolean indicating if validation passed
            - error: Error message (if validation failed)
    """
    result = act_primitive(tool_name, params, sandbox_spec)

    return {
        "result": result["result"],
        "validation": result["validation"],
        "error": result["error"]
    }
