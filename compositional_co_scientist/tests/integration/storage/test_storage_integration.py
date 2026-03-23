"""Integration tests for storage subsystem."""
import tempfile
from pathlib import Path
from compositional_co_scientist.storage.memory_db import MemoryDatabase
from compositional_co_scientist.storage.audit_db import AuditDatabase
from compositional_co_scientist.storage.ttl_manager import TTLManager


def test_full_storage_workflow():
    """Test full storage workflow with memory and audit databases."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Initialize databases
        memory_db = MemoryDatabase(tmpdir / "memory.db")
        memory_db.initialize()
        
        audit_db = AuditDatabase(tmpdir / "audit.db")
        audit_db.initialize()
        
        try:
            # Test memory persist/recall
            memory_db.persist("test-key", {"data": "value"}, ttl=3600)
            value = memory_db.recall("test-key")
            assert value == {"data": "value"}
            
            # Test audit logging
            log_id = audit_db.log_event("MEMORY_TEST", {"key": "test-key"}, "INFO")
            assert log_id >= 1
            
            # Verify audit log entry
            events = audit_db.query_by_event_type("MEMORY_TEST")
            assert len(events) == 1
            assert events[0]["event_data"] == {"key": "test-key"}
        finally:
            memory_db.close()
            audit_db.close()


def test_memory_with_ttl_expiration():
    """Test memory database TTL expiration."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        memory_db = MemoryDatabase(tmpdir / "memory.db")
        memory_db.initialize()
        
        try:
            # Persist with short TTL
            memory_db.persist("expiring-key", {"data": "test"}, ttl=1)
            memory_db.persist("persistent-key", {"data": "test"}, ttl=None)
            
            # Both should exist initially
            assert memory_db.recall("expiring-key") == {"data": "test"}
            assert memory_db.recall("persistent-key") == {"data": "test"}
            
            # Cleanup expired (none yet)
            deleted = memory_db.cleanup_expired()
            assert deleted == 0
        finally:
            memory_db.close()


def test_ttl_manager_integration():
    """Test TTL manager with memory database."""
    import sqlite3
    from datetime import datetime, timezone, timedelta
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        memory_db = MemoryDatabase(tmpdir / "memory.db")
        memory_db.initialize()
        
        # Manually insert an expired entry for testing
        expired_time = datetime.now(timezone.utc) - timedelta(hours=1)
        memory_db.conn.execute(
            "INSERT INTO memory (key, value, ttl, expires_at) VALUES (?, ?, ?, ?)",
            ("expired-key", '{"data": "test"}', 3600, expired_time)
        )
        memory_db.conn.commit()
        
        # Run TTL manager cleanup
        ttl_manager = TTLManager(memory_db.conn)
        deleted = ttl_manager.cleanup_expired()
        assert deleted == 1
        
        # Verify expired entry was deleted
        try:
            memory_db.recall("expired-key")
            assert False, "Should have raised KeyError"
        except KeyError:
            pass  # Expected
        
        memory_db.close()


def test_audit_log_completeness():
    """Test audit log captures all operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        audit_db = AuditDatabase(tmpdir / "audit.db")
        audit_db.initialize()
        
        # Log multiple events
        audit_db.log_event("GENERATE", {"goal_id": "g1"}, "INFO")
        audit_db.log_event("EVALUATE", {"candidate_id": "c1"}, "INFO")
        audit_db.log_event("SELECT", {"survivor_id": "s1"}, "WARNING")
        
        # Verify all events are logged
        all_events = audit_db.query_all()
        assert len(all_events) == 3
        
        event_types = [e["event_type"] for e in all_events]
        assert "GENERATE" in event_types
        assert "EVALUATE" in event_types
        assert "SELECT" in event_types
        
        audit_db.close()
