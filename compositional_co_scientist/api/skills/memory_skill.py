"""Memory skill wrapper for the MEMORY primitive.

Use when persisting or recalling information from the memory substrate.
Triggers the MEMORY primitive (P8) with constraint C5 (decay policy).
"""
from typing import Dict, Any, Optional
from pathlib import Path
import os

from compositional_co_scientist.storage.memory_db import MemoryDatabase


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
