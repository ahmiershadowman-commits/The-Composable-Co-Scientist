"""Tests for the SELECT primitive."""
import pytest
from compositional_co_scientist.core.primitives.select import select
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score


def test_select_chooses_survivors():
    """Test that SELECT chooses survivors based on diversity quota."""
    # Create mock scored candidates
    candidates = [
        Candidate(id=f"cand-{i}", goal_id="goal-1", content=f"Candidate {i}")
        for i in range(5)
    ]
    scores = [
        Score(candidate_id=f"cand-{i}", evaluator_model="eval-model", score=0.9 - i * 0.1)
        for i in range(5)
    ]
    
    scored = {"scores": scores, "candidates": candidates}
    
    # Select with 40% diversity quota (should select 2 out of 5)
    result = select(scored, diversity_quota=0.4)
    
    assert "survivors" in result
    assert "similarity_matrix" in result
    assert len(result["survivors"]) == 2  # 40% of 5 = 2


def test_select_handles_empty_input():
    """Test that SELECT handles empty input gracefully."""
    scored = {"scores": [], "candidates": []}
    result = select(scored, diversity_quota=0.4)
    
    assert "survivors" in result
    assert len(result["survivors"]) == 0


def test_select_computes_similarity_matrix():
    """Test that SELECT computes a similarity matrix for survivors."""
    candidates = [
        Candidate(id=f"cand-{i}", goal_id="goal-1", content=f"Candidate {i}")
        for i in range(3)
    ]
    scores = [
        Score(candidate_id=f"cand-{i}", evaluator_model="eval-model", score=0.9 - i * 0.1)
        for i in range(3)
    ]
    
    scored = {"scores": scores, "candidates": candidates}
    result = select(scored, diversity_quota=1.0)  # Select all
    
    assert "similarity_matrix" in result
    assert isinstance(result["similarity_matrix"], dict)
