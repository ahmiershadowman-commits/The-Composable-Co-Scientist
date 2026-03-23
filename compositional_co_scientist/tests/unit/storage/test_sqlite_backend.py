"""Unit tests for SQLite backend initialization."""
import pytest
import tempfile
import sqlite3
from pathlib import Path

from compositional_co_scientist.storage.sqlite_backend import DatabaseInitializer


def test_database_initialization():
    """Test that database is properly initialized with schema."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        initializer = DatabaseInitializer(db_path)
        initializer.initialize()
        
        # Check database file was created
        assert db_path.exists()
        
        # Check tables were created
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        assert "candidates" in tables, "candidates table should exist"
        assert "scores" in tables, "scores table should exist"
        conn.close()


def test_database_indexes_created():
    """Test that database indexes are properly created."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        initializer = DatabaseInitializer(db_path)
        initializer.initialize()
        
        # Check indexes were created
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='index'")
        indexes = [row[0] for row in cursor.fetchall()]
        
        assert "idx_goal" in indexes, "idx_goal index should exist"
        assert "idx_scores" in indexes, "idx_scores index should exist"
        conn.close()


def test_database_directory_creation():
    """Test that database directory is created if it doesn't exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "subdir" / "nested" / "test.db"
        initializer = DatabaseInitializer(db_path)
        initializer.initialize()
        
        assert db_path.exists()
        assert db_path.parent.exists()
