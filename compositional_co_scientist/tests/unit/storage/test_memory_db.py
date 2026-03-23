"""Unit tests for MemoryDatabase operations."""
import pytest
import tempfile
import time
from pathlib import Path
from datetime import datetime, timezone, timedelta

from compositional_co_scientist.storage.memory_db import MemoryDatabase


def test_memory_persist_and_recall():
    """Test basic persist and recall operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist
        artifact_id = db.persist("test-key", {"data": "value"}, ttl=3600)
        assert artifact_id == "test-key"
        
        # Recall
        value = db.recall("test-key")
        assert value == {"data": "value"}
        
        db.close()


def test_memory_ttl_expiration():
    """Test that TTL expiration works correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist with very short TTL
        db.persist("expiring-key", {"data": "value"}, ttl=1)  # 1 second
        
        # Wait for expiration
        time.sleep(2)
        
        # Clean up expired
        db.cleanup_expired()
        
        # Should raise KeyError
        with pytest.raises(KeyError):
            db.recall("expiring-key")
        
        db.close()


def test_memory_no_ttl():
    """Test persist without TTL (no expiration)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist without TTL
        db.persist("permanent-key", {"data": "permanent_value"})
        
        # Should still exist after cleanup
        db.cleanup_expired()
        value = db.recall("permanent-key")
        assert value == {"data": "permanent_value"}
        
        db.close()


def test_memory_key_not_found():
    """Test that recalling non-existent key raises KeyError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        with pytest.raises(KeyError, match="Memory key not found"):
            db.recall("non-existent-key")
        
        db.close()


def test_memory_overwrite():
    """Test that persisting same key overwrites value."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist initial value
        db.persist("overwrite-key", {"data": "initial"})
        
        # Overwrite
        db.persist("overwrite-key", {"data": "updated"}, ttl=7200)
        
        # Recall should return updated value
        value = db.recall("overwrite-key")
        assert value == {"data": "updated"}
        
        db.close()


def test_memory_complex_value():
    """Test persisting and recalling complex nested data."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        complex_data = {
            "nested": {"key": "value"},
            "list": [1, 2, 3],
            "mixed": {"a": 1, "b": [4, 5, 6]}
        }
        
        db.persist("complex-key", complex_data)
        value = db.recall("complex-key")
        assert value == complex_data
        
        db.close()
