"""C6 Sandbox Enforcement - Tool must be in allowlist."""

from compositional_co_scientist.core.errors import SandboxViolationError


def check_sandbox_permission(tool_name: str, params: dict, sandbox_spec: dict):
    """Check C6: Tool must be in allowlist.
    
    Args:
        tool_name: Tool to invoke
        params: Tool parameters
        sandbox_spec: Permission manifest
    
    Raises:
        SandboxViolationError: If tool not allowed
    """
    allowed_tools = sandbox_spec.get("allowed_tools", [])
    if tool_name not in allowed_tools:
        raise SandboxViolationError(f"C6 violated: '{tool_name}' not in allowlist: {allowed_tools}")
