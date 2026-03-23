"""Candidate model for composable co-scientist."""
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Candidate:
    """Represents a candidate solution in the compositional search space.

    Attributes:
        id: Unique identifier for the candidate.
        goal_id: ID of the goal this candidate addresses.
        content: The actual content/solution of the candidate.
        metadata: Additional metadata about the candidate.
        diversity_score: Score indicating diversity from other candidates.
        created_at: Timestamp when the candidate was created (UTC).
    """

    id: str
    goal_id: str
    content: str
    metadata: dict = field(default_factory=dict)
    diversity_score: float = 0.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
