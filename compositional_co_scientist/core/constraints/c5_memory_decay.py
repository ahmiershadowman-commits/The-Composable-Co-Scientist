"""C5 constraint: Memory Decay enforcement.

This constraint enforces TTL-based decay on memory entries to prevent
path dependence and memory bloat.
"""
from typing import Dict, Any, Optional, List
from pathlib import Path
import os


def run_decay_cleanup(
    db_path: Optional[Path] = None,
    utility_threshold: float = 0.3,
    decay_factor: float = 0.5
) -> Dict[str, Any]:
    """Run C5: Memory decay cleanup.

    This function:
    1. Deletes expired entries (TTL exceeded)
    2. Decays low-utility entries
    3. Returns cleanup statistics

    Args:
        db_path: Path to memory database. If None, uses default location.
        utility_threshold: Utility score below which entries are decayed.
        decay_factor: Factor to multiply utility by when decaying.

    Returns:
        Dictionary containing:
            - expired_deleted: Number of expired entries deleted
            - decayed_count: Number of entries decayed
            - remaining_count: Number of entries remaining
            - c5_passed: True if cleanup completed
    """
    import sqlite3
    from datetime import datetime, timezone

    # Default path
    if db_path is None:
        data_dir = Path(os.environ.get(
            "CO_SCIENTIST_DATA",
            Path.home() / ".composable_co_scientist"
        ))
        db_path = data_dir / "memory.db"

    if not db_path.exists():
        return {
            "expired_deleted": 0,
            "decayed_count": 0,
            "remaining_count": 0,
            "c5_passed": True,
            "note": "Database does not exist yet"
        }

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        # Step 1: Delete expired entries
        expired_cursor = conn.execute(
            "SELECT key FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        expired_keys = [row["key"] for row in expired_cursor.fetchall()]

        conn.execute(
            "DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        expired_deleted = conn.total_changes

        # Step 2: Find low-utility entries for decay
        low_utility_cursor = conn.execute(
            "SELECT key, utility_score FROM memory WHERE utility_score < ?",
            (utility_threshold,)
        )
        low_utility_keys = [row["key"] for row in low_utility_cursor.fetchall()]

        # Step 3: Decay low-utility entries
        decayed_count = 0
        for key in low_utility_keys:
            conn.execute(
                "UPDATE memory SET utility_score = utility_score * ? WHERE key = ?",
                (decay_factor, key)
            )
            decayed_count += 1

        conn.commit()

        # Step 4: Count remaining entries
        remaining_cursor = conn.execute("SELECT COUNT(*) as count FROM memory")
        remaining_count = remaining_cursor.fetchone()["count"]

        return {
            "expired_deleted": expired_deleted,
            "decayed_count": decayed_count,
            "remaining_count": remaining_count,
            "c5_passed": True,
            "cleanup_timestamp": datetime.now(timezone.utc).isoformat()
        }

    finally:
        conn.close()


def check_memory_health(
    db_path: Optional[Path] = None,
    max_entries: int = 1000,
    max_avg_age_days: float = 30.0
) -> Dict[str, Any]:
    """Check C5: Memory health metrics.

    Args:
        db_path: Path to memory database.
        max_entries: Maximum acceptable number of entries.
        max_avg_age_days: Maximum acceptable average age in days.

    Returns:
        Dictionary containing:
            - passed: True if health metrics within bounds
            - entry_count: Current number of entries
            - avg_age_days: Average age of entries
            - expired_count: Number of expired entries
            - low_utility_count: Number of low-utility entries
    """
    import sqlite3
    from compositional_co_scientist.core.errors import ConstraintViolationError

    if db_path is None:
        data_dir = Path(os.environ.get(
            "CO_SCIENTIST_DATA",
            Path.home() / ".composable_co_scientist"
        ))
        db_path = data_dir / "memory.db"

    if not db_path.exists():
        return {
            "passed": True,
            "entry_count": 0,
            "avg_age_days": 0,
            "expired_count": 0,
            "low_utility_count": 0,
            "note": "Database does not exist yet"
        }

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        # Entry count
        count_cursor = conn.execute("SELECT COUNT(*) as count FROM memory")
        entry_count = count_cursor.fetchone()["count"]

        # Average age in days
        age_cursor = conn.execute(
            """SELECT AVG(julianday(CURRENT_TIMESTAMP) - julianday(created_at)) as avg_age
               FROM memory"""
        )
        avg_age_days = age_cursor.fetchone()["avg_age"] or 0

        # Expired count
        expired_cursor = conn.execute(
            "SELECT COUNT(*) as count FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        expired_count = expired_cursor.fetchone()["count"]

        # Low utility count
        low_utility_cursor = conn.execute(
            "SELECT COUNT(*) as count FROM memory WHERE utility_score < 0.3"
        )
        low_utility_count = low_utility_cursor.fetchone()["count"]

        # Check constraints
        violations = []
        if entry_count > max_entries:
            violations.append(f"Entry count {entry_count} exceeds max {max_entries}")
        if avg_age_days > max_avg_age_days:
            violations.append(f"Average age {avg_age_days:.1f} days exceeds max {max_avg_age_days}")

        if violations:
            raise ConstraintViolationError(
                f"C5 violated: {'; '.join(violations)}. Run decay cleanup."
            )

        return {
            "passed": True,
            "entry_count": entry_count,
            "avg_age_days": round(avg_age_days, 2),
            "expired_count": expired_count,
            "low_utility_count": low_utility_count
        }

    finally:
        conn.close()


def get_memory_stats(db_path: Optional[Path] = None) -> Dict[str, Any]:
    """Get memory database statistics.

    Args:
        db_path: Path to memory database.

    Returns:
        Dictionary with memory statistics.
    """
    import sqlite3

    if db_path is None:
        data_dir = Path(os.environ.get(
            "CO_SCIENTIST_DATA",
            Path.home() / ".composable_co_scientist"
        ))
        db_path = data_dir / "memory.db"

    if not db_path.exists():
        return {"error": "Database does not exist"}

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        # Total entries
        count_cursor = conn.execute("SELECT COUNT(*) as count FROM memory")
        total = count_cursor.fetchone()["count"]

        # Entries with TTL
        ttl_cursor = conn.execute(
            "SELECT COUNT(*) as count FROM memory WHERE ttl IS NOT NULL"
        )
        with_ttl = ttl_cursor.fetchone()["count"]

        # Expired but not yet deleted
        expired_cursor = conn.execute(
            "SELECT COUNT(*) as count FROM memory WHERE expires_at < CURRENT_TIMESTAMP"
        )
        expired = expired_cursor.fetchone()["count"]

        # Average utility
        util_cursor = conn.execute(
            "SELECT AVG(utility_score) as avg_util FROM memory"
        )
        avg_util = util_cursor.fetchone()["avg_util"] or 0

        return {
            "total_entries": total,
            "entries_with_ttl": with_ttl,
            "expired_pending_cleanup": expired,
            "average_utility": round(avg_util, 3),
            "database_path": str(db_path)
        }

    finally:
        conn.close()
