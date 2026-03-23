"""Memory skill wrapper for the MEMORY primitive.

Use when persisting or recalling information from the memory substrate.
Triggers the MEMORY primitive (P8) with constraint C5 (decay policy).
"""
from typing import Dict, Any, Optional
from pathlib import Path
import os

from compositional_co_scientist.storage.memory_db import MemoryDatabase
from compositional_co_scientist.core.constraints.c5_memory_decay import (
    run_decay_cleanup,
    check_memory_health,
    get_memory_stats,
)


_memory_db: Optional[MemoryDatabase] = None


def _get_memory_db() -> MemoryDatabase:
    """Get or create the memory database instance."""
    global _memory_db
    if _memory_db is None:
        # Use data directory in user's home or package directory
        data_dir = Path(os.environ.get("CO_SCIENTIST_DATA", Path.home() / ".composable_co_scientist"))
        db_path = data_dir / "memory.db"
        _memory_db = MemoryDatabase(db_path)
        _memory_db.initialize()
    return _memory_db


def memory(operation: str, key: str, value: Any = None, ttl: int = None) -> Dict[str, Any]:
    """Persist or recall information from the memory substrate.

    Args:
        operation: Operation type ('persist' or 'recall').
        key: Memory key for retrieval.
        value: Value to persist (for 'persist' operation, must be JSON-serializable).
        ttl: Time-to-live in seconds (for decay policy).

    Returns:
        Dictionary containing operation results:
            - For 'persist': success (boolean), key (string)
            - For 'recall': value (any or None), utility_score (float)

    Raises:
        ValueError: If operation is invalid or required parameters are missing.
        KeyError: If recalling a non-existent key.
    """
    db = _get_memory_db()

    if operation == "persist":
        if value is None:
            raise ValueError("Value required for persist operation")
        db.persist(key, value, ttl)
        return {"success": True, "key": key}

    elif operation == "recall":
        try:
            result = db.recall(key)
            return {
                "value": result,
                "utility_score": 1.0  # Updated by _update_utility internally
            }
        except KeyError:
            return {"value": None, "utility_score": 0.0}

    else:
        raise ValueError(f"Invalid operation: {operation}. Must be 'persist' or 'recall'")


def memory_cleanup(
    utility_threshold: float = 0.3,
    decay_factor: float = 0.5
) -> Dict[str, Any]:
    """Run C5 memory decay cleanup.

    Args:
        utility_threshold: Utility score below which entries are decayed.
        decay_factor: Factor to multiply utility by when decaying.

    Returns:
        Dictionary containing cleanup statistics.
    """
    db = _get_memory_db()
    return run_decay_cleanup(db.db_path, utility_threshold, decay_factor)


def memory_health_check(
    max_entries: int = 1000,
    max_avg_age_days: float = 30.0
) -> Dict[str, Any]:
    """Check C5 memory health metrics.

    Args:
        max_entries: Maximum acceptable number of entries.
        max_avg_age_days: Maximum acceptable average age in days.

    Returns:
        Dictionary containing health metrics.
    """
    db = _get_memory_db()
    return check_memory_health(db.db_path, max_entries, max_avg_age_days)


def memory_statistics() -> Dict[str, Any]:
    """Get memory database statistics.

    Returns:
        Dictionary with memory statistics.
    """
    db = _get_memory_db()
    return get_memory_stats(db.db_path)
