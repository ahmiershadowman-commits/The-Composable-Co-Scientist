"""Decay policy for memory utility scores.

This module provides utility score computation and decay threshold logic
for memory entries in the Compositional Co-Scientist storage system.

The utility score is computed as:
    utility_score = 1.0 / (1.0 + days_since_last_accessed)

Entries with utility scores below the threshold (default 0.3) are marked
for decay or consolidation.
"""


def compute_utility_score_from_days(days_since_accessed: float) -> float:
    """Compute utility score based on days since last access.

    The utility score follows a decay curve where:
    - Freshly accessed items (0 days) have score 1.0
    - Items accessed 1 day ago have score 0.5
    - Items accessed 9 days ago have score 0.1
    - Score approaches 0 as days increase

    Args:
        days_since_accessed: Number of days since the memory was last accessed.

    Returns:
        Utility score between 0 and 1.
    """
    return 1.0 / (1.0 + days_since_accessed)


def should_decay(utility_score: float, threshold: float = 0.3) -> bool:
    """Determine if a memory entry should be decayed.

    Memory entries with utility scores below the threshold are candidates
    for decay or consolidation.

    Args:
        utility_score: The current utility score of the memory entry.
        threshold: The decay threshold (default 0.3).

    Returns:
        True if the entry should be decayed (score < threshold), False otherwise.
    """
    return utility_score < threshold
