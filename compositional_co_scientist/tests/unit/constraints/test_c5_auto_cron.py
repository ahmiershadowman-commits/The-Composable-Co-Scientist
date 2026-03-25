"""Tests for C5 auto-cron module."""
import pytest
import sqlite3
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
from unittest.mock import patch, MagicMock


@pytest.fixture
def temp_memory_db(tmp_path):
    """Create a temporary memory database for testing."""
    db_path = tmp_path / "test_memory.db"
    
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE memory (
            key TEXT PRIMARY KEY,
            value TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP,
            ttl INTEGER,
            utility_score REAL DEFAULT 1.0
        )
    """)
    
    # Expired entries (use past timestamp)
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("expired_1", "data1", "2020-01-01 00:00:00", 0.8)
    )
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("expired_2", "data2", "2020-01-01 00:00:00", 0.5)
    )
    
    # Low utility entries
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("low_util_1", "data3", "2099-12-31 23:59:59", 0.2)
    )
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("low_util_2", "data4", "2099-12-31 23:59:59", 0.1)
    )
    
    # Healthy entries
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("healthy_1", "data5", "2099-12-31 23:59:59", 0.9)
    )
    conn.execute(
        "INSERT INTO memory (key, value, expires_at, utility_score) VALUES (?, ?, ?, ?)",
        ("healthy_2", "data6", "2099-12-31 23:59:59", 0.7)
    )
    
    conn.commit()
    conn.close()
    
    return db_path


class TestC5AutoCron:
    """Tests for C5 auto-cron functionality."""
    
    def test_run_c5_maintenance(self, temp_memory_db):
        """Test C5 maintenance routine."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            run_c5_maintenance
        )
        
        result = run_c5_maintenance(db_path=temp_memory_db)
        
        # Check cleanup results
        assert "expired_deleted" in result
        assert "decayed_count" in result
        assert "remaining_count" in result
        assert "c5_passed" in result
        
        # Should have deleted 2 expired entries
        assert result["expired_deleted"] == 2
        
        # Should have decayed 2 low-utility entries
        assert result["decayed_count"] == 2
        
        # Should have 4 remaining entries
        assert result["remaining_count"] == 4
        
        # C5 should pass
        assert result["c5_passed"] is True
    
    def test_create_apscheduler_callback(self, temp_memory_db):
        """Test APScheduler callback creation."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            create_apscheduler_callback
        )
        
        callback = create_apscheduler_callback(
            db_path=temp_memory_db,
            utility_threshold=0.3
        )
        
        # Callback should be callable
        assert callable(callback)
        
        # Callback should run maintenance
        result = callback()
        assert result is not None
        assert "expired_deleted" in result
    
    @pytest.mark.skip(reason="Requires APScheduler installation")
    @patch('apscheduler.schedulers.background.BackgroundScheduler')
    def test_start_c5_scheduler(self, mock_scheduler_class, temp_memory_db):
        """Test starting C5 scheduler."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            start_c5_scheduler
        )
        
        # Mock scheduler instance
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        # Start scheduler (disable immediate run to avoid actual maintenance)
        scheduler = start_c5_scheduler(
            run_interval_hours=24,
            db_path=temp_memory_db,
            start_immediately=False
        )
        
        # Should return scheduler instance
        assert scheduler is not None
        
        # Should have added job
        mock_scheduler.add_job.assert_called_once()
        
        # Should have started scheduler
        mock_scheduler.start.assert_called_once()
    
    def test_stop_c5_scheduler(self):
        """Test stopping C5 scheduler."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            stop_c5_scheduler
        )
        
        # Mock scheduler
        mock_scheduler = MagicMock()
        
        # Stop scheduler
        stop_c5_scheduler(mock_scheduler)
        
        # Should have shutdown scheduler
        mock_scheduler.shutdown.assert_called_once_with(wait=True)
    
    def test_create_cron_script(self):
        """Test cron script generation."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            create_cron_script
        )
        
        script = create_cron_script()
        
        # Script should be valid Python
        assert script.startswith('#!/usr/bin/env python3')
        assert 'run_c5_maintenance' in script
        assert 'if __name__ == "__main__"' in script
        
        # Script should be compilable
        compile(script, '<string>', 'exec')  # Should not raise
    
    def test_get_default_db_path(self, tmp_path):
        """Test default database path resolution."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            get_default_db_path
        )
        
        # Test with custom environment variable
        custom_dir = tmp_path / "custom_data"
        custom_dir.mkdir()
        
        with patch.dict(os.environ, {"CO_SCIENTIST_DATA": str(custom_dir)}):
            path = get_default_db_path()
            assert path == custom_dir / "memory.db"
        
        # Test default path (using tmp_path to avoid home directory issues)
        with patch.dict(os.environ, {}, clear=True):
            with patch('pathlib.Path.home', return_value=tmp_path / "home"):
                path = get_default_db_path()
                assert path.name == "memory.db"
                assert ".composable_co_scientist" in str(path)
    
    def test_maintenance_with_no_database(self, tmp_path):
        """Test maintenance when database doesn't exist."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            run_c5_maintenance
        )
        
        non_existent_path = tmp_path / "non_existent.db"
        
        result = run_c5_maintenance(db_path=non_existent_path)
        
        # Should handle gracefully
        assert result["c5_passed"] is True
        assert result["expired_deleted"] == 0
        assert result["decayed_count"] == 0
        assert "note" in result or "Database does not exist" in str(result)
    
    def test_maintenance_decay_verification(self, temp_memory_db):
        """Test that decay actually reduces utility scores."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            run_c5_maintenance
        )
        import sqlite3
        
        # Get initial utility scores
        conn = sqlite3.connect(temp_memory_db)
        before_cursor = conn.execute(
            "SELECT key, utility_score FROM memory WHERE key LIKE 'low_util_%'"
        )
        before_scores = {row[0]: row[1] for row in before_cursor.fetchall()}
        conn.close()
        
        # Verify initial scores are low
        assert before_scores["low_util_1"] == 0.2
        assert before_scores["low_util_2"] == 0.1
        
        # Run maintenance
        run_c5_maintenance(db_path=temp_memory_db)
        
        # Get post-maintenance scores
        conn = sqlite3.connect(temp_memory_db)
        after_cursor = conn.execute(
            "SELECT key, utility_score FROM memory WHERE key LIKE 'low_util_%'"
        )
        after_scores = {row[0]: row[1] for row in after_cursor.fetchall()}
        conn.close()
        
        # Verify scores were decayed (multiplied by 0.5)
        assert after_scores["low_util_1"] == pytest.approx(0.1, rel=0.01)
        assert after_scores["low_util_2"] == pytest.approx(0.05, rel=0.01)


class TestC5SchedulerIntegration:
    """Integration tests for C5 scheduler (requires APScheduler)."""
    
    @pytest.fixture
    def scheduler_with_cleanup(self, temp_memory_db):
        """Create scheduler that cleans up after tests."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            start_c5_scheduler, stop_c5_scheduler
        )
        
        scheduler = None
        try:
            scheduler = start_c5_scheduler(
                run_interval_hours=24,
                db_path=temp_memory_db,
                start_immediately=False
            )
            yield scheduler
        finally:
            if scheduler:
                stop_c5_scheduler(scheduler)
    
    @pytest.mark.skip(reason="Requires APScheduler installation")
    def test_scheduler_creation(self, scheduler_with_cleanup):
        """Test that scheduler can be created and started."""
        # If APScheduler is installed, scheduler should be created
        assert scheduler_with_cleanup is not None
    
    @pytest.mark.skip(reason="Requires APScheduler installation")
    def test_scheduler_job_execution(self, temp_memory_db):
        """Test that scheduled job executes maintenance."""
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            start_c5_scheduler, stop_c5_scheduler, run_c5_maintenance
        )
        
        # Run maintenance once to clear expired entries
        initial_result = run_c5_maintenance(db_path=temp_memory_db)
        
        # Scheduler would run periodic maintenance
        # (Testing actual scheduling requires time passage)
        assert initial_result["c5_passed"] is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
