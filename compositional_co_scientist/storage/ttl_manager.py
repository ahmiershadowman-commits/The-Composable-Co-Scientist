"""TTL Manager for The Compositional Co-Scientist.

Provides periodic cleanup and decay operations for memory database entries.
"""
import sqlite3
from datetime import datetime, timezone
from typing import Optional


class TTLManager:
    """Time-to-live manager for memory database.

    This class provides maintenance operations for memory entries:
    - Cleanup of expired entries (based on expires_at timestamp)
    - Decay of low-utility entries (based on utility_score)

    The TTLManager is designed to be run periodically (e.g., daily at 02:00 UTC)
    via cron or scheduled task.

    Usage:
        conn = sqlite3.connect("memory.db")
        manager = TTLManager(conn)
        deleted = manager.cleanup_expired()
        decayed = manager.decay_low_utility(threshold=0.3)
    """

    # SQL query to delete expired entries
    CLEANUP_EXPIRED_SQL = "DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP"

    # SQL query to find low utility entries
    QUERY_LOW_UTILITY_SQL = """
        SELECT key FROM memory 
        WHERE utility_score < ?
    """

    # SQL query to decay low utility entries
    DECAY_ENTRY_SQL = """
        UPDATE memory 
        SET utility_score = utility_score * 0.5 
        WHERE key = ?
    """

    def __init__(self, conn: sqlite3.Connection):
        """Initialize the TTL manager.

        Args:
            conn: SQLite connection to the memory database.
        """
        self.conn = conn

    def cleanup_expired(self) -> int:
        """Delete expired entries from the memory database.

        Entries are considered expired if their expires_at timestamp
        is in the past (before CURRENT_TIMESTAMP).

        Returns:
            Number of entries deleted.
        """
        # Count entries to be deleted
        cursor = self.conn.execute(
            "SELECT COUNT(*) FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        count = cursor.fetchone()[0]

        # Delete expired entries
        self.conn.execute(self.CLEANUP_EXPIRED_SQL)
        self.conn.commit()

        return count

    def decay_low_utility(self, threshold: float = 0.3) -> int:
        """Decay entries with low utility scores.

        Entries with utility scores below the threshold have their
        utility score reduced by 50% (multiplied by 0.5).

        Args:
            threshold: Utility score threshold (default 0.3).

        Returns:
            Number of entries decayed.
        """
        # Find low utility entries
        cursor = self.conn.execute(self.QUERY_LOW_UTILITY_SQL, (threshold,))
        low_utility_keys = [row[0] for row in cursor.fetchall()]

        # Decay each low utility entry
        for key in low_utility_keys:
            self.conn.execute(self.DECAY_ENTRY_SQL, (key,))

        self.conn.commit()
        return len(low_utility_keys)

    def run_maintenance(self, decay_threshold: float = 0.3) -> dict:
        """Run full maintenance routine.

        This method performs both cleanup and decay operations.
        It is designed to be called periodically (e.g., daily).

        Args:
            decay_threshold: Utility score threshold for decay (default 0.3).

        Returns:
            Dictionary with maintenance results:
            - expired_deleted: Number of expired entries deleted
            - low_utility_decayed: Number of low utility entries decayed
        """
        expired_deleted = self.cleanup_expired()
        low_utility_decayed = self.decay_low_utility(decay_threshold)

        return {
            "expired_deleted": expired_deleted,
            "low_utility_decayed": low_utility_decayed,
        }
