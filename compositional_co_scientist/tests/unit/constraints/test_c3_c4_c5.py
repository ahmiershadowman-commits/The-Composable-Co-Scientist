"""Tests for C3, C4, C5 constraints."""
import pytest
import uuid
from compositional_co_scientist.core.constraints.c3_diversity_quota import (
    check_diversity_quota,
    check_diversity_score,
    generate_anti_canon_prompt,
)
from compositional_co_scientist.core.constraints.c4_log_completeness import (
    log_start_evaluation,
    log_end_evaluation,
    check_log_completeness,
    get_pending_count,
    clear_pending,
)
from compositional_co_scientist.core.constraints.c5_memory_decay import (
    run_decay_cleanup,
    check_memory_health,
    get_memory_stats,
)
from compositional_co_scientist.core.errors import ConstraintViolationError


class TestC3DiversityQuota:
    """Tests for C3 diversity quota constraint."""

    def test_check_diversity_quota_passed(self):
        """Test that diverse candidates pass C3."""
        similarity_matrix = {
            "c1": {"c1": 1.0, "c2": 0.3, "c3": 0.2},
            "c2": {"c1": 0.3, "c2": 1.0, "c3": 0.4},
            "c3": {"c1": 0.2, "c2": 0.4, "c3": 1.0},
        }
        result = check_diversity_quota(similarity_matrix, max_similarity=0.7)
        assert result["passed"] is True
        assert result["max_found"] == 0.4

    def test_check_diversity_quota_violated(self):
        """Test that similar candidates fail C3."""
        similarity_matrix = {
            "c1": {"c1": 1.0, "c2": 0.85, "c3": 0.9},
            "c2": {"c1": 0.85, "c2": 1.0, "c3": 0.8},
            "c3": {"c1": 0.9, "c2": 0.8, "c3": 1.0},
        }
        with pytest.raises(ConstraintViolationError) as exc_info:
            check_diversity_quota(similarity_matrix, max_similarity=0.7)
        assert "C3 violated" in str(exc_info.value)

    def test_check_diversity_quota_empty(self):
        """Test that empty matrix passes by default."""
        result = check_diversity_quota({})
        assert result["passed"] is True

    def test_check_diversity_score_passed(self):
        """Test that high diversity score passes."""
        assert check_diversity_score(0.6, min_diversity=0.4) is True

    def test_check_diversity_score_violated(self):
        """Test that low diversity score fails."""
        with pytest.raises(ConstraintViolationError) as exc_info:
            check_diversity_score(0.2, min_diversity=0.4)
        assert "C3 violated" in str(exc_info.value)

    def test_generate_anti_canon_prompt(self):
        """Test anti-canon prompt generation."""
        goal = "What causes X?"
        prompt = generate_anti_canon_prompt(goal)
        assert "ANTI-CANON CONSTRAINT" in prompt
        assert "What causes X?" in prompt
        assert "diverge from obvious" in prompt


class TestC4LogCompleteness:
    """Tests for C4 log completeness constraint."""

    def setup_method(self):
        """Clear pending before each test."""
        clear_pending()

    def teardown_method(self):
        """Clear pending after each test."""
        clear_pending()

    def test_log_start_and_end(self):
        """Test that start/end logging works."""
        eval_id = "test-eval-1"
        log_start_evaluation(
            eval_id,
            [{"id": "c1"}, {"id": "c2"}],
            {"novelty": 0.5},
            "gpt-4"
        )
        assert get_pending_count() == 1

        # Mock log function
        def mock_log(event_type, data, severity):
            return {"logged": True}

        log_end_evaluation(
            eval_id,
            [{"score": 0.8}],
            mock_log
        )
        assert get_pending_count() == 0

    def test_check_log_completeness_passed(self):
        """Test that complete logging passes."""
        clear_pending()
        result = check_log_completeness()
        assert result["passed"] is True
        assert result["incomplete_count"] == 0

    def test_check_log_completeness_violated(self):
        """Test that incomplete logging fails."""
        log_start_evaluation(
            "pending-eval",
            [{"id": "c1"}],
            {"novelty": 0.5},
            "gpt-4"
        )
        with pytest.raises(ConstraintViolationError) as exc_info:
            check_log_completeness()
        assert "C4 violated" in str(exc_info.value)
        assert "pending-eval" in str(exc_info.value)

    def test_end_without_start_raises(self):
        """Test that ending without starting raises error."""
        def mock_log(event_type, data, severity):
            return {"logged": True}

        with pytest.raises(ValueError) as exc_info:
            log_end_evaluation("nonexistent", [], mock_log)
        assert "without start log" in str(exc_info.value)


class TestC5MemoryDecay:
    """Tests for C5 memory decay constraint."""

    def test_run_decay_cleanup_no_db(self):
        """Test cleanup when DB doesn't exist."""
        result = run_decay_cleanup(db_path=None)
        # Should not raise, just return note
        assert result["c5_passed"] is True

    def test_get_memory_stats_no_db(self):
        """Test stats when DB doesn't exist."""
        result = get_memory_stats(db_path=None)
        assert "error" in result

    def test_check_memory_health_no_db(self):
        """Test health check when DB doesn't exist."""
        result = check_memory_health(db_path=None)
        assert result["passed"] is True
        assert result["entry_count"] == 0
