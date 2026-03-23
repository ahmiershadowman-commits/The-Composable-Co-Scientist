"""Document model for source materials."""
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Document:
    """Represents a source document in the knowledge base.

    Attributes:
        id: Unique identifier for the document.
        source: Source reference (e.g., arxiv ID, DOI, URL).
        content: The document content.
        metadata: Additional metadata about the document.
        relevance_score: Relevance score for current context (default 1.0).
        created_at: Timestamp when the document was added (UTC).
    """

    id: str
    source: str
    content: str
    metadata: dict = field(default_factory=dict)
    relevance_score: float = 1.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
