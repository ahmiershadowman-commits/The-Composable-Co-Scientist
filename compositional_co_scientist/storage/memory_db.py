"""Memory database for The Compositional Co-Scientist.

Provides persistent key-value storage with TTL support and utility scoring.
"""
import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Any, Optional


class MemoryDatabase:
    """SQLite-backed memory database with TTL and utility scoring.
    
    This class provides persistent storage for memory artifacts with:
    - Time-to-live (TTL) based expiration
    - Utility scoring for memory importance
    - Automatic cleanup of expired entries
    
    Schema:
        key: Primary key (TEXT)
        value: JSON-encoded data (JSON)
        ttl: Time-to-live in seconds (INTEGER)
        expires_at: Expiration timestamp (TIMESTAMP)
        utility_score: Importance score (REAL)
        last_accessed: Last access timestamp (TIMESTAMP)
        created_at: Creation timestamp (TIMESTAMP)
    """
    
    SCHEMA_SQL = """
    CREATE TABLE IF NOT EXISTS memory (
        key TEXT PRIMARY KEY,
        value JSON NOT NULL,
        ttl INTEGER,
        expires_at TIMESTAMP,
        utility_score REAL DEFAULT 1.0,
        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX IF NOT EXISTS idx_expires ON memory(expires_at);
    CREATE INDEX IF NOT EXISTS idx_utility ON memory(utility_score);
    """
    
    def __init__(self, db_path: Path):
        """Initialize the memory database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
    
    def initialize(self) -> None:
        """Initialize the database with schema.
        
        Creates the database file and parent directories if they don't exist,
        then executes the schema SQL to create tables and indexes.
        """
        # Ensure parent directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create database connection and execute schema
        self.conn = sqlite3.connect(self.db_path)
        self.conn.executescript(self.SCHEMA_SQL)
        self.conn.commit()
    
    def persist(self, key: str, value: Any, ttl: Optional[int] = None) -> str:
        """Persist a value to the database.
        
        Args:
            key: Unique identifier for the value
            value: Any JSON-serializable value
            ttl: Time-to-live in seconds (optional, None = no expiration)
            
        Returns:
            The key that was persisted
        """
        expires_at = None
        if ttl:
            expires_at = datetime.now(timezone.utc) + timedelta(seconds=ttl)
        
        self.conn.execute(
            """INSERT OR REPLACE INTO memory 
               (key, value, ttl, expires_at, utility_score) 
               VALUES (?, ?, ?, ?, 1.0)""",
            (key, json.dumps(value), ttl, expires_at)
        )
        self.conn.commit()
        return key
    
    def recall(self, key: str) -> Any:
        """Recall a value from the database.
        
        Args:
            key: The key to look up
            
        Returns:
            The stored value (JSON-decoded)
            
        Raises:
            KeyError: If the key does not exist
        """
        cursor = self.conn.execute(
            "SELECT value, utility_score FROM memory WHERE key = ?",
            (key,)
        )
        row = cursor.fetchone()
        if row is None:
            raise KeyError(f"Memory key not found: {key}")
        
        # Update last_accessed and utility score
        self._update_utility(key)
        
        return json.loads(row[0])
    
    def _update_utility(self, key: str) -> None:
        """Update utility score based on recency.
        
        Args:
            key: The key to update
        """
        from .decay_policy import compute_utility_score
        utility = compute_utility_score(key, self.conn)
        self.conn.execute(
            "UPDATE memory SET utility_score = ?, last_accessed = CURRENT_TIMESTAMP WHERE key = ?",
            (utility, key)
        )
        self.conn.commit()
    
    def cleanup_expired(self) -> int:
        """Delete expired entries from the database.
        
        Returns:
            Number of entries deleted
        """
        cursor = self.conn.execute(
            "SELECT COUNT(*) FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        count = cursor.fetchone()[0]
        
        self.conn.execute("DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP")
        self.conn.commit()
        return count
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
