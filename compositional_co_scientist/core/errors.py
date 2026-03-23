"""Error taxonomy for The Compositional Co-Scientist plugin.

This module defines the hierarchy of exceptions used throughout the plugin,
organized by constraint violations, primitive failures, and infrastructure errors.
"""


class CompositionalCoScientistError(Exception):
    """Base exception for all plugin errors."""
    user_message = "An error occurred: {detail}"
    action = "Please try again or contact support"
    severity = "ERROR"
    
    def __init__(self, detail: str):
        super().__init__(detail)
        self.detail = detail


class ConstraintViolationError(CompositionalCoScientistError):
    """Raised when a non-negotiable constraint (C1-C6) is violated."""
    user_message = "A safety constraint was violated: {detail}"
    action = "Review constraint configuration and retry"
    severity = "CRITICAL"


class PrimitiveFailureError(CompositionalCoScientistError):
    """Raised when a primitive operation (P1-P10) fails."""
    user_message = "The {primitive} operation failed: {detail}"
    action = "Retry with adjusted parameters"
    severity = "ERROR"


class StorageError(CompositionalCoScientistError):
    """Raised on SQLite storage failures."""
    user_message = "Storage error: {detail}"
    action = "Check database file permissions and disk space"
    severity = "ERROR"


class InvalidTransitionError(ConstraintViolationError):
    """Raised when workflow state machine detects invalid transition."""
    user_message = "Invalid workflow transition: {detail}"
    action = "Restart the workflow from the beginning"


class LogCompletenessError(ConstraintViolationError):
    """Raised when audit log is incomplete."""
    user_message = "Audit log incomplete: {detail}"
    action = "Run audit resolution before continuing"


class SandboxViolationError(ConstraintViolationError):
    """Raised when tool execution violates sandbox."""
    user_message = "Tool execution blocked: {detail}"
    action = "Review tool permissions and retry"
