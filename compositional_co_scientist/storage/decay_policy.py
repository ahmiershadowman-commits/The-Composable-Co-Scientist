"""Decay policy for memory utility scores.

This module provides utility score computation for memory entries.
Full implementation in Task 1.6.
"""
import sqlite3
from datetime import datetime, timezone


def compute_utility_score(key: str, conn: sqlite3.Connection) -> float:
    """Compute utility score based on recency.
    
    Stub implementation - returns default score of 1.0.
    Full implementation in Task 1.6.
    
    Args:
        key: Memory key
        conn: SQLite connection
        
    Returns:
        Utility score (default 1.0 for stub)
    """
    # Stub: return default utility score
    # Full implementation: utility_score = 1.0 / (1.0 + days_since_last_accessed)
    return 1.0
