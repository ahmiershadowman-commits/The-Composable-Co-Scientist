"""Tests for audit database."""
import tempfile
from pathlib import Path
from compositional_co_scientist.storage.audit_db import AuditDatabase


def test_audit_append():
    """Test audit event logging."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        log_id = db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        assert log_id >= 1
        db.close()


def test_audit_query_by_event_type():
    """Test querying audit log by event type."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        
        db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        db.log_event("GENERATE", {"goal_id": "test-2"}, "INFO")
        db.log_event("EVALUATE", {"candidate_id": "test-3"}, "WARNING")
        
        events = db.query_by_event_type("EVALUATE")
        assert len(events) == 2
        db.close()


def test_audit_query_by_severity():
    """Test querying audit log by severity."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        
        db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        db.log_event("GENERATE", {"goal_id": "test-2"}, "WARNING")
        db.log_event("ACT", {"tool_name": "test"}, "ERROR")
        
        events = db.query_by_severity("WARNING")
        assert len(events) == 1
        db.close()


def test_audit_append_only():
    """Test that audit log is append-only (no delete)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        
        log_id = db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        
        # Verify no delete method exists or it raises an error
        assert not hasattr(db, 'delete_event')
        db.close()
