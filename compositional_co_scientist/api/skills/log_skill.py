"""Log skill wrapper for the LOG primitive.

Use when logging operations for auditability.
Triggers the LOG primitive (P9) with constraint C4 (audit all EVALUATE operations).
"""
from typing import Dict, Any, Optional
from pathlib import Path
import os

from compositional_co_scientist.storage.audit_db import AuditDatabase


_audit_db: Optional[AuditDatabase] = None


def _get_audit_db() -> AuditDatabase:
    """Get or create the audit database instance."""
    global _audit_db
    if _audit_db is None:
        # Use data directory in user's home or package directory
        data_dir = Path(os.environ.get("CO_SCIENTIST_DATA", Path.home() / ".composable_co_scientist"))
        db_path = data_dir / "audit.db"
        _audit_db = AuditDatabase(db_path)
        _audit_db.initialize()
    return _audit_db


def log(event_type: str, event_data: Dict[str, Any], severity: str = "INFO") -> Dict[str, Any]:
    """Log an operation for auditability.

    Args:
        event_type: Type of event being logged (e.g., 'EVALUATE', 'SELECT', 'GENERATE').
        event_data: Dictionary containing event details (must be JSON-serializable).
        severity: Severity level ('INFO', 'WARNING', 'ERROR', 'CRITICAL'). Default: 'INFO'.

    Returns:
        Dictionary containing:
            - event_id: Unique identifier for the log entry
            - timestamp: Timestamp when the log was created (ISO format)

    Raises:
        ValueError: If event_type or event_data is missing.
    """
    if not event_type:
        raise ValueError("event_type is required")
    if not event_data:
        raise ValueError("event_data is required")

    db = _get_audit_db()
    event_id = db.log_event(event_type, event_data, severity)

    from datetime import datetime, timezone
    timestamp = datetime.now(timezone.utc).isoformat()

    return {
        "event_id": event_id,
        "timestamp": timestamp
    }
