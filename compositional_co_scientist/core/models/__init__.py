"""Core models for The Compositional Co-Scientist."""
from .candidate import Candidate
from .defect import Defect
from .document import Document
from .score import Score

__all__ = ["Candidate", "Score", "Defect", "Document"]
