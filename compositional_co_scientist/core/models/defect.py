"""Defect model for candidate quality issues."""
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Defect:
    """Represents a defect or quality issue in a candidate.

    Attributes:
        candidate_id: ID of the candidate with the defect.
        defect_type: Type/category of the defect.
        description: Human-readable description of the defect.
        severity: Severity level (low, medium, high). Default: medium.
        created_at: Timestamp when the defect was recorded (UTC).
    """

    candidate_id: str
    defect_type: str
    description: str
    severity: str = "medium"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
