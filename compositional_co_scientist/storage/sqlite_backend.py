"""SQLite backend initialization for the Compositional Co-Scientist."""
import sqlite3
from pathlib import Path
from typing import List, Optional


class DatabaseInitializer:
    """Initialize and manage SQLite database schema.
    
    This class handles the creation and initialization of the SQLite
    database used for storing candidates, scores, and related data.
    """
    
    SCHEMA_SQL = """
    -- Candidates table: stores generated candidate solutions
    CREATE TABLE IF NOT EXISTS candidates (
        id TEXT PRIMARY KEY,
        goal_id TEXT NOT NULL,
        content TEXT NOT NULL,
        metadata JSON,
        diversity_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    -- Scores table: stores evaluation scores for candidates
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_id TEXT NOT NULL,
        evaluator_model TEXT NOT NULL,
        score REAL NOT NULL,
        rubric JSON,
        calibration REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (candidate_id) REFERENCES candidates(id)
    );
    
    -- Indexes for efficient querying
    CREATE INDEX IF NOT EXISTS idx_goal ON candidates(goal_id);
    CREATE INDEX IF NOT EXISTS idx_scores ON scores(candidate_id);
    """
    
    def __init__(self, db_path: Path):
        """Initialize the database initializer.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
    
    def initialize(self) -> None:
        """Initialize database with schema.
        
        Creates the database file and parent directories if they don't exist,
        then executes the schema SQL to create tables and indexes.
        """
        # Ensure parent directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create database and execute schema
        conn = sqlite3.connect(self.db_path)
        try:
            conn.executescript(self.SCHEMA_SQL)
            conn.commit()
        finally:
            conn.close()
    
    def get_connection(self) -> sqlite3.Connection:
        """Get a connection to the database.
        
        Returns:
            A sqlite3.Connection object for the database.
            
        Raises:
            FileNotFoundError: If the database has not been initialized.
        """
        if not self.db_path.exists():
            raise FileNotFoundError(
                f"Database not initialized at {self.db_path}. "
                "Call initialize() first."
            )
        return sqlite3.connect(self.db_path)
    
    def table_exists(self, table_name: str) -> bool:
        """Check if a table exists in the database.
        
        Args:
            table_name: Name of the table to check.
            
        Returns:
            True if the table exists, False otherwise.
        """
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,)
            )
            return cursor.fetchone() is not None
        finally:
            conn.close()
    
    def get_tables(self) -> List[str]:
        """Get list of all tables in the database.
        
        Returns:
            List of table names.
        """
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            return [row[0] for row in cursor.fetchall()]
        finally:
            conn.close()
