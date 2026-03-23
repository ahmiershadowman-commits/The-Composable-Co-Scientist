"""Tests for decay policy utility scoring."""
from compositional_co_scientist.storage.decay_policy import (
    compute_utility_score_from_days,
    should_decay
)


def test_utility_score_computation():
    """Test utility score computation based on days since accessed."""
    assert compute_utility_score_from_days(0) == 1.0
    assert compute_utility_score_from_days(1) == 0.5
    assert compute_utility_score_from_days(9) == 0.1


def test_decay_threshold():
    """Test decay threshold logic."""
    assert should_decay(0.2) == True
    assert should_decay(0.4) == False
