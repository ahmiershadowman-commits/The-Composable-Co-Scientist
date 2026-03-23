"""Score model for candidate evaluation."""
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Score:
    """Represents an evaluation score for a candidate.

    Attributes:
        candidate_id: ID of the candidate being scored.
        evaluator_model: Name/ID of the model that produced this score.
        score: The numeric score value (typically 0.0 to 1.0).
        rubric: Dictionary of rubric criteria and their scores.
        calibration: Calibration factor for the score (default 1.0).
        created_at: Timestamp when the score was created (UTC).
    """

    candidate_id: str
    evaluator_model: str
    score: float
    rubric: dict = field(default_factory=dict)
    calibration: float = 1.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
