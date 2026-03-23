"""Tests for TTL manager."""
import sqlite3
import tempfile
from pathlib import Path
from datetime import datetime, timezone, timedelta
from compositional_co_scientist.storage.ttl_manager import TTLManager


def test_ttl_manager_cleanup():
    """Test TTL manager cleanup of expired entries."""
    # Create a mock connection
    class MockConn:
        def __init__(self):
            self.executed = []
        
        def execute(self, sql):
            self.executed.append(sql)
            return self
        
        def fetchone(self):
            return (0,)
        
        def commit(self):
            pass
    
    conn = MockConn()
    manager = TTLManager(conn)
    manager.cleanup_expired()
    # First query is COUNT, second is DELETE
    assert "SELECT COUNT(*) FROM memory WHERE expires_at < CURRENT_TIMESTAMP" in conn.executed[0]
    assert "DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP" in conn.executed[1]


def test_ttl_manager_with_real_database():
    """Test TTL manager with a real SQLite database."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        conn = sqlite3.connect(db_path)
        
        # Create schema
        conn.execute("""
            CREATE TABLE memory (
                key TEXT PRIMARY KEY,
                value JSON NOT NULL,
                ttl INTEGER,
                expires_at TIMESTAMP,
                utility_score REAL DEFAULT 1.0,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        
        # Insert an expired entry
        expired_time = datetime.now(timezone.utc) - timedelta(hours=1)
        conn.execute(
            "INSERT INTO memory (key, value, ttl, expires_at) VALUES (?, ?, ?, ?)",
            ("expired-key", '{"data": "test"}', 3600, expired_time)
        )
        
        # Insert a valid entry
        valid_time = datetime.now(timezone.utc) + timedelta(hours=1)
        conn.execute(
            "INSERT INTO memory (key, value, ttl, expires_at) VALUES (?, ?, ?, ?)",
            ("valid-key", '{"data": "test"}', 3600, valid_time)
        )
        conn.commit()
        
        # Run cleanup
        manager = TTLManager(conn)
        deleted_count = manager.cleanup_expired()
        
        assert deleted_count == 1
        
        # Verify only valid entry remains
        cursor = conn.execute("SELECT key FROM memory")
        keys = [row[0] for row in cursor.fetchall()]
        assert "valid-key" in keys
        assert "expired-key" not in keys
        
        conn.close()


def test_ttl_manager_decay_low_utility():
    """Test TTL manager decay of low utility entries."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        conn = sqlite3.connect(db_path)
        
        # Create schema
        conn.execute("""
            CREATE TABLE memory (
                key TEXT PRIMARY KEY,
                value JSON NOT NULL,
                ttl INTEGER,
                expires_at TIMESTAMP,
                utility_score REAL DEFAULT 1.0,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        
        # Insert low utility entries
        conn.execute(
            "INSERT INTO memory (key, value, utility_score) VALUES (?, ?, ?)",
            ("low-util-1", '{"data": "test"}', 0.2)
        )
        conn.execute(
            "INSERT INTO memory (key, value, utility_score) VALUES (?, ?, ?)",
            ("low-util-2", '{"data": "test"}', 0.1)
        )
        
        # Insert high utility entry
        conn.execute(
            "INSERT INTO memory (key, value, utility_score) VALUES (?, ?, ?)",
            ("high-util", '{"data": "test"}', 0.8)
        )
        conn.commit()
        
        # Run decay
        manager = TTLManager(conn)
        decayed_count = manager.decay_low_utility(threshold=0.3)
        
        assert decayed_count == 2
        
        conn.close()
