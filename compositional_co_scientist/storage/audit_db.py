"""Audit database for The Compositional Co-Scientist.

Provides append-only event logging for audit and compliance purposes.
"""
import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Optional


class AuditDatabase:
    """SQLite-backed append-only audit database.

    This class provides event logging for audit and compliance with:
    - Append-only semantics (no UPDATE, no DELETE)
    - Event type indexing for efficient queries
    - Severity level tracking
    - Timestamp tracking (UTC)

    Schema:
        id: Auto-increment primary key (INTEGER)
        event_type: Type of event (TEXT)
        event_data: JSON-encoded event data (JSON)
        severity: Event severity level (TEXT)
        timestamp: Event timestamp (TIMESTAMP)
    """

    SCHEMA_SQL = """
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        event_data JSON NOT NULL,
        severity TEXT DEFAULT 'INFO',
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX IF NOT EXISTS idx_event_type ON audit_log(event_type);
    CREATE INDEX IF NOT EXISTS idx_timestamp ON audit_log(timestamp);
    CREATE INDEX IF NOT EXISTS idx_severity ON audit_log(severity);
    """

    def __init__(self, db_path: Path):
        """Initialize the audit database.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

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

    def log_event(self, event_type: str, event_data: dict, severity: str = "INFO") -> int:
        """Log an event to the audit database.

        Args:
            event_type: Type of event (e.g., "EVALUATE", "GENERATE", "ACT")
            event_data: Dictionary containing event data (must be JSON-serializable)
            severity: Severity level ("INFO", "WARNING", "ERROR", "CRITICAL")

        Returns:
            The ID of the logged event.
        """
        cursor = self.conn.execute(
            """INSERT INTO audit_log (event_type, event_data, severity, timestamp)
               VALUES (?, ?, ?, ?)""",
            (event_type, json.dumps(event_data), severity, datetime.now(timezone.utc))
        )
        self.conn.commit()
        return cursor.lastrowid

    def query_by_event_type(self, event_type: str) -> list[dict]:
        """Query audit log by event type.

        Args:
            event_type: The event type to filter by.

        Returns:
            List of matching audit log entries as dictionaries.
        """
        cursor = self.conn.execute(
            "SELECT id, event_type, event_data, severity, timestamp FROM audit_log WHERE event_type = ?",
            (event_type,)
        )
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "event_type": row[1],
                "event_data": json.loads(row[2]),
                "severity": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]

    def query_by_severity(self, severity: str) -> list[dict]:
        """Query audit log by severity level.

        Args:
            severity: The severity level to filter by.

        Returns:
            List of matching audit log entries as dictionaries.
        """
        cursor = self.conn.execute(
            "SELECT id, event_type, event_data, severity, timestamp FROM audit_log WHERE severity = ?",
            (severity,)
        )
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "event_type": row[1],
                "event_data": json.loads(row[2]),
                "severity": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]

    def query_all(self, limit: Optional[int] = None) -> list[dict]:
        """Query all audit log entries.

        Args:
            limit: Optional limit on the number of results.

        Returns:
            List of all audit log entries as dictionaries.
        """
        query = "SELECT id, event_type, event_data, severity, timestamp FROM audit_log ORDER BY timestamp DESC"
        if limit:
            query += f" LIMIT {limit}"
        
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "event_type": row[1],
                "event_data": json.loads(row[2]),
                "severity": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
