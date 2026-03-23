"""C6 sandbox enforcement constraint for tool execution.

This constraint enforces sandbox permissions by validating that tool
executions are within an allowed allowlist, preventing unauthorized
tool usage as specified in OWASP LLM Top 10.
"""
from typing import Dict, Any
from compositional_co_scientist.core.errors import SandboxViolationError


def check_sandbox_permission(tool_name: str, params: Dict[str, Any], 
                              sandbox_spec: Dict[str, Any]) -> None:
    """Check if a tool execution is permitted by the sandbox.

    Args:
        tool_name: Name of the tool to execute.
        params: Parameters to pass to the tool.
        sandbox_spec: Sandbox specification containing:
            - allowed_tools: List of tool names permitted in the sandbox

    Raises:
        SandboxViolationError: If the tool is not in the allowlist.
    """
    allowed_tools = sandbox_spec.get("allowed_tools", [])
    
    if tool_name not in allowed_tools:
        raise SandboxViolationError(
            f"C6 violated: '{tool_name}' not in allowlist"
        )
