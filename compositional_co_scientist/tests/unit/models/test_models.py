"""Unit tests for data models."""
from datetime import datetime, timezone

import pytest


def test_candidate_creation():
    """Test that Candidate model can be created with required fields."""
    from compositional_co_scientist.core.models import Candidate

    candidate = Candidate(
        id="test-1",
        goal_id="goal-1",
        content="Test content",
        metadata={"key": "value"},
    )
    assert candidate.id == "test-1"
    assert candidate.goal_id == "goal-1"
    assert candidate.content == "Test content"
    assert isinstance(candidate.created_at, datetime)
    assert candidate.created_at.tzinfo == timezone.utc


def test_score_creation():
    """Test that Score model can be created with required fields."""
    from compositional_co_scientist.core.models import Score

    score = Score(
        candidate_id="test-1",
        evaluator_model="gpt-4",
        score=0.85,
        rubric={"coherence": 0.9},
    )
    assert score.score == 0.85
    assert score.calibration == 1.0  # default


def test_defect_creation():
    """Test that Defect model can be created with required fields."""
    from compositional_co_scientist.core.models import Defect

    defect = Defect(
        candidate_id="test-1",
        defect_type="logical_error",
        description="Missing premise",
    )
    assert defect.severity == "medium"  # default


def test_document_creation():
    """Test that Document model can be created with required fields."""
    from compositional_co_scientist.core.models import Document

    doc = Document(
        id="doc-1",
        source="arxiv:1234.5678",
        content="Document content",
    )
    assert doc.relevance_score == 1.0  # default
