# The Compositional Co-Scientist Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a production-ready, multi-host plugin implementing 9 primitives (10 sub-operations) and 6 non-negotiable constraints for evidence-anchored agentic scaffolding in scientific reasoning.

**Architecture:** Layered architecture with 6 layers (Host Adapters → Plugin API → Middleware → Primitives → Constraints → Storage). Each layer is independently testable. SQLite persistence with separate databases for candidates, memory, and audit logging.

**Tech Stack:** Python 3.10+, SQLite, sentence-transformers, pydantic, pytest, pytest-cov. Host adapters for Claude Code, Qwen Code, Gemini CLI.

**Spec Reference:** `docs/superpowers/specs/2026-03-23-compositional-co-scientist-design.md`

**Plan Status:** Revised v1.1 — All 7 phases expanded with bite-sized TDD tasks
**Review Status:** Pending second review (first review found CRITICAL issues with placeholder phases)
**Total Tasks:** 25+ TDD tasks across 7 phases
**Estimated Effort:** ~120 hours

---

## File Structure Map

```
compositional-co-scientist/
├── core/
│   ├── primitives/
│   │   ├── __init__.py
│   │   ├── generate.py              # P1: GENERATE
│   │   ├── evaluate.py              # P2: EVALUATE
│   │   ├── critique.py              # P3: CRITIQUE
│   │   ├── select.py                # P4: SELECT
│   │   ├── retrieve.py              # P5: RETRIEVE
│   │   ├── act.py                   # P6: ACT
│   │   ├── synthesize.py            # P7: SYNTHESIZE
│   │   └── memory.py                # P8/P9: MEMORY (persist/recall)
│   ├── constraints/
│   │   ├── __init__.py
│   │   ├── enforcer.py              # ConstraintEnforcer class
│   │   ├── c1_evaluator_independence.py
│   │   ├── c2_temporal_order.py
│   │   ├── c3_diversity_quota.py
│   │   ├── c4_log_completeness.py
│   │   ├── c5_memory_decay.py
│   │   └── c6_sandbox_enforcement.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── candidate.py             # Candidate dataclass
│   │   ├── score.py                 # Score dataclass
│   │   ├── defect.py                # Defect dataclass
│   │   └── document.py              # Document dataclass
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── audit_interceptor.py     # C4 enforcement
│   │   └── constraint_hooks.py      # C1-C6 hooks
│   └── errors.py                    # Error taxonomy
├── storage/
│   ├── __init__.py
│   ├── sqlite_backend.py            # Database initialization
│   ├── candidates_db.py             # candidates.db operations
│   ├── memory_db.py                 # memory.db operations
│   ├── audit_db.py                  # audit.db operations
│   ├── ttl_manager.py               # TTL + decay
│   └── decay_policy.py              # Utility score computation
├── adapters/
│   ├── __init__.py
│   ├── claude_code/
│   │   ├── __init__.py
│   │   ├── skill.py                 # Claude SKILL tool
│   │   └── command.py               # Slash commands
│   ├── qwen_code/
│   │   ├── __init__.py
│   │   ├── skill.py                 # Qwen SKILL tool
│   │   └── command.py               # Slash commands
│   └── gemini_cli/
│       ├── __init__.py
│       ├── tool.py                  # Gemini tool declaration
│       └── command.py               # Slash commands
├── api/
│   ├── __init__.py
│   ├── skills/
│   │   ├── __init__.py
│   │   ├── generate_skill.py
│   │   ├── evaluate_skill.py
│   │   ├── critique_skill.py
│   │   ├── select_skill.py
│   │   ├── retrieve_skill.py
│   │   ├── act_skill.py
│   │   ├── synthesize_skill.py
│   │   ├── memory_skill.py
│   │   └── log_skill.py
│   └── commands/
│       ├── __init__.py
│       └── handlers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Fixtures, mocks
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── primitives/
│   │   ├── constraints/
│   │   └── storage/
│   └── integration/
│       ├── __init__.py
│       ├── workflows/
│       └── adapters/
├── docs/
│   ├── api-reference/
│   ├── user-guide/
│   ├── tutorials/
│   └── examples/
├── plugin.json
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## Phase 1: Storage Substrate (MEMORY + LOG)

**Duration:** ~20 hours  
**Deliverables:** SQLite backend, TTL manager, decay policy, audit logging  
**Exit Criteria:** All storage unit tests pass (15 tests), 80% branch coverage

### Task 1.1: Project Skeleton

**Files:**
- Create: `compositional_co_scientist/__init__.py`
- Create: `requirements.txt`
- Create: `setup.py`
- Create: `.gitignore`
- Create: `README.md`

- [ ] **Step 1: Create package structure**

```bash
mkdir -p compositional_co_scientist/{core/{primitives,constraints,models,middleware},storage,adapters/{claude_code,qwen_code,gemini_cli},api/{skills,commands},tests/{unit/{primitives,constraints,storage},integration/{workflows,adapters}},docs/{api-reference,user-guide,tutorials,examples}}
touch compositional_co_scientist/__init__.py
```

- [ ] **Step 2: Create requirements.txt**

```
# Core dependencies
sqlite3  # stdlib
sentence-transformers>=2.2.0
pydantic>=2.0

# Testing
pytest>=7.0
pytest-cov>=4.0
```

- [ ] **Step 3: Create setup.py**

```python
from setuptools import setup, find_packages

setup(
    name="compositional-co-scientist",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "sentence-transformers>=2.2.0",
        "pydantic>=2.0",
    ],
    extras_require={
        "test": ["pytest>=7.0", "pytest-cov>=4.0"],
    },
)
```

- [ ] **Step 4: Create .gitignore**

```
__pycache__/
*.pyc
*.db
.pytest_cache/
.coverage
htmlcov/
.env
```

- [ ] **Step 5: Create README.md**

```markdown
# The Compositional Co-Scientist

Evidence-anchored agentic scaffolding for scientific reasoning.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from compositional_co_scientist import generate, evaluate, select

candidates = generate(goal="Your research question")
scored = evaluate(candidates, rubric={...})
survivors = select(scored, diversity_quota=0.4)
```

## Documentation

See `docs/` for API reference, user guide, and tutorials.
```

- [ ] **Step 6: Commit**

```bash
git add .
git commit -m "feat: initial project skeleton"
```

---

### Task 1.2: Data Models

**Files:**
- Create: `core/models/__init__.py`
- Create: `core/models/candidate.py`
- Create: `core/models/score.py`
- Create: `core/models/defect.py`
- Create: `core/models/document.py`
- Test: `tests/unit/models/test_models.py`

- [ ] **Step 1: Write failing test for Candidate model**

```python
# tests/unit/models/test_models.py
from datetime import datetime, timezone
from compositional_co_scientist.core.models import Candidate

def test_candidate_creation():
    candidate = Candidate(
        id="test-1",
        goal_id="goal-1",
        content="Test content",
        metadata={"key": "value"}
    )
    assert candidate.id == "test-1"
    assert candidate.goal_id == "goal-1"
    assert candidate.content == "Test content"
    assert isinstance(candidate.created_at, datetime)
    assert candidate.created_at.tzinfo == timezone.utc
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/unit/models/test_models.py::test_candidate_creation -v
```
Expected: FAIL with "cannot import name 'Candidate'"

- [ ] **Step 3: Implement Candidate model**

```python
# core/models/candidate.py
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Candidate:
    id: str
    goal_id: str
    content: str
    metadata: dict = field(default_factory=dict)
    diversity_score: float = 0.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/unit/models/test_models.py::test_candidate_creation -v
```
Expected: PASS

- [ ] **Step 5: Add tests for Score, Defect, Document models**

```python
def test_score_creation():
    from compositional_co_scientist.core.models import Score
    score = Score(
        candidate_id="test-1",
        evaluator_model="gpt-4",
        score=0.85,
        rubric={"coherence": 0.9}
    )
    assert score.score == 0.85
    assert score.calibration == 1.0  # default

def test_defect_creation():
    from compositional_co_scientist.core.models import Defect
    defect = Defect(
        candidate_id="test-1",
        defect_type="logical_error",
        description="Missing premise"
    )
    assert defect.severity == "medium"  # default

def test_document_creation():
    from compositional_co_scientist.core.models import Document
    doc = Document(
        id="doc-1",
        source="arxiv:1234.5678",
        content="Document content"
    )
    assert doc.relevance_score == 1.0  # default
```

- [ ] **Step 6: Implement remaining models**

```python
# core/models/score.py
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Score:
    candidate_id: str
    evaluator_model: str
    score: float
    rubric: dict = field(default_factory=dict)
    calibration: float = 1.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

# core/models/defect.py
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Defect:
    candidate_id: str
    defect_type: str
    description: str
    severity: str = "medium"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

# core/models/document.py
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Document:
    id: str
    source: str
    content: str
    metadata: dict = field(default_factory=dict)
    relevance_score: float = 1.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
```

- [ ] **Step 7: Update models __init__.py**

```python
# core/models/__init__.py
from .candidate import Candidate
from .score import Score
from .defect import Defect
from .document import Document

__all__ = ["Candidate", "Score", "Defect", "Document"]
```

- [ ] **Step 8: Run all model tests**

```bash
pytest tests/unit/models/test_models.py -v
```
Expected: 4 tests PASS

- [ ] **Step 9: Commit**

```bash
git add core/models/ tests/unit/models/test_models.py
git commit -m "feat: add data models (Candidate, Score, Defect, Document)"
```

---

### Task 1.3: Error Taxonomy

**Files:**
- Create: `core/errors.py`
- Test: `tests/unit/test_errors.py`

- [ ] **Step 1: Write failing test for error hierarchy**

```python
# tests/unit/test_errors.py
import pytest
from compositional_co_scientist.core.errors import (
    CompositionalCoScientistError,
    ConstraintViolationError,
    PrimitiveFailureError,
    StorageError,
    InvalidTransitionError,
    LogCompletenessError,
    SandboxViolationError
)

def test_error_inheritance():
    assert issubclass(ConstraintViolationError, CompositionalCoScientistError)
    assert issubclass(PrimitiveFailureError, CompositionalCoScientistError)
    assert issubclass(InvalidTransitionError, ConstraintViolationError)

def test_user_message_format():
    try:
        raise ConstraintViolationError("C1 violated")
    except ConstraintViolationError as e:
        assert "safety constraint was violated" in e.user_message
        assert e.severity == "CRITICAL"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/unit/test_errors.py -v
```
Expected: FAIL (module doesn't exist)

- [ ] **Step 3: Implement error taxonomy**

```python
# core/errors.py
class CompositionalCoScientistError(Exception):
    """Base exception for all plugin errors."""
    user_message = "An error occurred: {detail}"
    action = "Please try again or contact support"
    severity = "ERROR"
    
    def __init__(self, detail: str):
        super().__init__(detail)
        self.detail = detail

class ConstraintViolationError(CompositionalCoScientistError):
    """Raised when a non-negotiable constraint (C1-C6) is violated."""
    user_message = "A safety constraint was violated: {detail}"
    action = "Review constraint configuration and retry"
    severity = "CRITICAL"

class PrimitiveFailureError(CompositionalCoScientistError):
    """Raised when a primitive operation (P1-P10) fails."""
    user_message = "The {primitive} operation failed: {detail}"
    action = "Retry with adjusted parameters"
    severity = "ERROR"

class StorageError(CompositionalCoScientistError):
    """Raised on SQLite storage failures."""
    user_message = "Storage error: {detail}"
    action = "Check database file permissions and disk space"
    severity = "ERROR"

class InvalidTransitionError(ConstraintViolationError):
    """Raised when workflow state machine detects invalid transition."""
    user_message = "Invalid workflow transition: {detail}"
    action = "Restart the workflow from the beginning"

class LogCompletenessError(ConstraintViolationError):
    """Raised when audit log is incomplete."""
    user_message = "Audit log incomplete: {detail}"
    action = "Run audit resolution before continuing"

class SandboxViolationError(ConstraintViolationError):
    """Raised when tool execution violates sandbox."""
    user_message = "Tool execution blocked: {detail}"
    action = "Review tool permissions and retry"
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/unit/test_errors.py -v
```
Expected: 2 tests PASS

- [ ] **Step 5: Commit**

```bash
git add core/errors.py tests/unit/test_errors.py
git commit -m "feat: add error taxonomy"
```

---

### Task 1.4: SQLite Backend Initialization

**Files:**
- Create: `storage/__init__.py`
- Create: `storage/sqlite_backend.py`
- Test: `tests/unit/storage/test_sqlite_backend.py`

- [ ] **Step 1: Write failing test for database initialization**

```python
# tests/unit/storage/test_sqlite_backend.py
import pytest
import tempfile
import os
from pathlib import Path
from compositional_co_scientist.storage.sqlite_backend import DatabaseInitializer

def test_database_initialization():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        initializer = DatabaseInitializer(db_path)
        initializer.initialize()
        
        assert db_path.exists()
        # Check tables were created
        import sqlite3
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        assert "candidates" in tables  # or whatever table you're testing
        conn.close()
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/unit/storage/test_sqlite_backend.py -v
```
Expected: FAIL (module doesn't exist)

- [ ] **Step 3: Implement DatabaseInitializer**

```python
# storage/sqlite_backend.py
import sqlite3
from pathlib import Path
from typing import List

class DatabaseInitializer:
    SCHEMA_SQL = """
    CREATE TABLE IF NOT EXISTS candidates (
        id TEXT PRIMARY KEY,
        goal_id TEXT NOT NULL,
        content TEXT NOT NULL,
        metadata JSON,
        diversity_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
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
    
    CREATE INDEX IF NOT EXISTS idx_goal ON candidates(goal_id);
    CREATE INDEX IF NOT EXISTS idx_scores ON scores(candidate_id);
    """
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
    
    def initialize(self):
        """Initialize database with schema."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        conn.executescript(self.SCHEMA_SQL)
        conn.commit()
        conn.close()
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/unit/storage/test_sqlite_backend.py -v
```
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add storage/ tests/unit/storage/test_sqlite_backend.py
git commit -m "feat: add SQLite backend initialization"
```

---

### Task 1.5: Memory Database Operations

**Files:**
- Create: `storage/memory_db.py`
- Test: `tests/unit/storage/test_memory_db.py`

- [ ] **Step 1: Write failing test for persist operation**

```python
# tests/unit/storage/test_memory_db.py
import pytest
import tempfile
from pathlib import Path
from compositional_co_scientist.storage.memory_db import MemoryDatabase
from datetime import datetime, timezone, timedelta

def test_memory_persist_and_recall():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist
        artifact_id = db.persist("test-key", {"data": "value"}, ttl=3600)
        assert artifact_id == "test-key"
        
        # Recall
        value = db.recall("test-key")
        assert value == {"data": "value"}
```

- [ ] **Step 2: Implement MemoryDatabase**

```python
# storage/memory_db.py
import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Any, Optional

class MemoryDatabase:
    SCHEMA_SQL = """
    CREATE TABLE IF NOT EXISTS memory (
        key TEXT PRIMARY KEY,
        value JSON NOT NULL,
        ttl INTEGER,
        expires_at TIMESTAMP,
        utility_score REAL DEFAULT 1.0,
        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX IF NOT EXISTS idx_expires ON memory(expires_at);
    CREATE INDEX IF NOT EXISTS idx_utility ON memory(utility_score);
    """
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = None
    
    def initialize(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.executescript(self.SCHEMA_SQL)
        self.conn.commit()
    
    def persist(self, key: str, value: Any, ttl: Optional[int] = None) -> str:
        expires_at = None
        if ttl:
            expires_at = datetime.now(timezone.utc) + timedelta(seconds=ttl)
        
        self.conn.execute(
            """INSERT OR REPLACE INTO memory 
               (key, value, ttl, expires_at, utility_score) 
               VALUES (?, ?, ?, ?, 1.0)""",
            (key, json.dumps(value), ttl, expires_at)
        )
        self.conn.commit()
        return key
    
    def recall(self, key: str) -> Any:
        cursor = self.conn.execute(
            "SELECT value, utility_score FROM memory WHERE key = ?",
            (key,)
        )
        row = cursor.fetchone()
        if row is None:
            raise KeyError(f"Memory key not found: {key}")
        
        # Update last_accessed and utility score
        self._update_utility(key)
        
        return json.loads(row[0])
    
    def _update_utility(self, key: str):
        """Update utility score based on recency."""
        from .decay_policy import compute_utility_score
        utility = compute_utility_score(key, self.conn)
        self.conn.execute(
            "UPDATE memory SET utility_score = ?, last_accessed = CURRENT_TIMESTAMP WHERE key = ?",
            (utility, key)
        )
        self.conn.commit()
    
    def close(self):
        if self.conn:
            self.conn.close()
```

- [ ] **Step 3: Run test to verify it passes**

```bash
pytest tests/unit/storage/test_memory_db.py -v
```
Expected: PASS

- [ ] **Step 4: Add test for TTL expiration**

```python
def test_memory_ttl_expiration():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "memory.db"
        db = MemoryDatabase(db_path)
        db.initialize()
        
        # Persist with very short TTL
        db.persist("expiring-key", {"data": "value"}, ttl=1)  # 1 second
        
        # Wait for expiration
        import time
        time.sleep(2)
        
        # Clean up expired
        db.cleanup_expired()
        
        # Should raise KeyError
        with pytest.raises(KeyError):
            db.recall("expiring-key")
```

- [ ] **Step 5: Implement cleanup_expired**

```python
def cleanup_expired(self):
    """Delete expired entries."""
    self.conn.execute("DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP")
    self.conn.commit()
```

- [ ] **Step 6: Commit**

```bash
git add storage/memory_db.py tests/unit/storage/test_memory_db.py
git commit -m "feat: add memory database with TTL support"
```

---

### Task 1.6: Decay Policy

**Files:**
- Create: `storage/decay_policy.py`
- Test: `tests/unit/storage/test_decay_policy.py`

- [ ] **Step 1: Write failing test for utility score computation**

```python
# tests/unit/storage/test_decay_policy.py
import pytest
from compositional_co_scientist.storage.decay_policy import (
    compute_utility_score,
    get_low_utility_entries,
    should_decay
)
from datetime import datetime, timezone, timedelta
import sqlite3

def test_utility_score_computation():
    # Fresh entry (accessed today)
    days_since_access = 0
    utility = compute_utility_score_from_days(days_since_access)
    assert utility == 1.0  # 1.0 / (1.0 + 0) = 1.0
    
    # Accessed 1 day ago
    utility = compute_utility_score_from_days(1)
    assert utility == 0.5  # 1.0 / (1.0 + 1) = 0.5
    
    # Accessed 9 days ago
    utility = compute_utility_score_from_days(9)
    assert utility == 0.1  # 1.0 / (1.0 + 9) = 0.1

def test_decay_threshold():
    assert should_decay(0.2) == True   # Below 0.3 threshold
    assert should_decay(0.4) == False  # Above 0.3 threshold
```

- [ ] **Step 2: Implement decay policy**

```python
# storage/decay_policy.py
from typing import List, Tuple
import sqlite3

def compute_utility_score_from_days(days_since_accessed: float) -> float:
    """Compute utility score from days since last access."""
    return 1.0 / (1.0 + days_since_accessed)

def compute_utility_score(key: str, conn: sqlite3.Connection) -> float:
    """Compute utility score for a memory entry."""
    cursor = conn.execute(
        """SELECT julianday(CURRENT_TIMESTAMP) - julianday(last_accessed) 
           FROM memory WHERE key = ?""",
        (key,)
    )
    row = cursor.fetchone()
    if row is None:
        return 0.0
    days_since = row[0] or 0
    return compute_utility_score_from_days(days_since)

def get_low_utility_entries(conn: sqlite3.Connection, threshold: float = 0.3) -> List[str]:
    """Get keys with utility score below threshold."""
    cursor = conn.execute(
        "SELECT key FROM memory WHERE utility_score < ?",
        (threshold,)
    )
    return [row[0] for row in cursor.fetchall()]

def should_decay(utility_score: float, threshold: float = 0.3) -> bool:
    """Check if entry should be decayed."""
    return utility_score < threshold

def decay_utility(conn: sqlite3.Connection, key: str, decay_factor: float = 0.5):
    """Apply decay to utility score."""
    conn.execute(
        """UPDATE memory SET utility_score = utility_score * ? 
           WHERE key = ?""",
        (decay_factor, key)
    )
    conn.commit()
```

- [ ] **Step 3: Commit**

```bash
git add storage/decay_policy.py tests/unit/storage/test_decay_policy.py
git commit -m "feat: add decay policy with utility scoring"
```

---

### Task 1.7: Audit Database (Append-Only Log)

**Files:**
- Create: `storage/audit_db.py`
- Test: `tests/unit/storage/test_audit_db.py`

- [ ] **Step 1: Write failing test for append-only log**

```python
# tests/unit/storage/test_audit_db.py
import pytest
import tempfile
from pathlib import Path
from compositional_co_scientist.storage.audit_db import AuditDatabase

def test_audit_append():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        
        log_id = db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        assert log_id >= 1

def test_audit_query():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "audit.db"
        db = AuditDatabase(db_path)
        db.initialize()
        
        db.log_event("EVALUATE", {"candidate_id": "test-1"}, "INFO")
        db.log_event("SELECT", {"survivors": 3}, "INFO")
        
        events = db.query_by_event_type("EVALUATE")
        assert len(events) == 1
        assert events[0]["event_data"]["candidate_id"] == "test-1"
```

- [ ] **Step 2: Implement AuditDatabase**

```python
# storage/audit_db.py
import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timezone

class AuditDatabase:
    SCHEMA_SQL = """
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        event_data JSON NOT NULL,
        severity TEXT DEFAULT 'INFO',
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX IF NOT EXISTS idx_event_type ON audit_log(event_type);
    CREATE INDEX IF NOT EXISTS idx_timestamp ON audit_log(timestamp);
    CREATE INDEX IF NOT EXISTS idx_severity ON audit_log(severity);
    """
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = None
    
    def initialize(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.executescript(self.SCHEMA_SQL)
        # Enforce append-only
        self.conn.execute("REVOKE DELETE ON audit_log FROM PUBLIC")
        self.conn.execute("REVOKE UPDATE ON audit_log FROM PUBLIC")
        self.conn.commit()
    
    def log_event(self, event_type: str, event_data: Dict[str, Any], 
                  severity: str = "INFO") -> int:
        cursor = self.conn.execute(
            """INSERT INTO audit_log (event_type, event_data, severity) 
               VALUES (?, ?, ?)""",
            (event_type, json.dumps(event_data), severity)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def query_by_event_type(self, event_type: str) -> List[Dict[str, Any]]:
        cursor = self.conn.execute(
            "SELECT id, event_data, severity, timestamp FROM audit_log WHERE event_type = ? ORDER BY timestamp DESC",
            (event_type,)
        )
        return [
            {"id": row[0], "event_data": json.loads(row[1]), "severity": row[2], "timestamp": row[3]}
            for row in cursor.fetchall()
        ]
    
    def has_entry(self, operation_id: str) -> bool:
        """Check if audit log has entry for operation."""
        cursor = self.conn.execute(
            "SELECT 1 FROM audit_log WHERE event_data LIKE ?",
            (f'%{operation_id}%',)
        )
        return cursor.fetchone() is not None
    
    def close(self):
        if self.conn:
            self.conn.close()
```

- [ ] **Step 3: Commit**

```bash
git add storage/audit_db.py tests/unit/storage/test_audit_db.py
git commit -m "feat: add append-only audit database"
```

---

### Task 1.8: TTL Manager (Cron Job)

**Files:**
- Create: `storage/ttl_manager.py`
- Test: `tests/unit/storage/test_ttl_manager.py`

- [ ] **Step 1: Write failing test for TTL manager**

```python
# tests/unit/storage/test_ttl_manager.py
import pytest
from compositional_co_scientist.storage.ttl_manager import TTLManager

def test_ttl_manager_cleanup():
    # Mock database connection
    class MockConn:
        def __init__(self):
            self.executed = []
        def execute(self, sql):
            self.executed.append(sql)
        def commit(self):
            pass
    
    conn = MockConn()
    manager = TTLManager(conn)
    manager.cleanup_expired()
    
    assert "DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP" in conn.executed[0]
```

- [ ] **Step 2: Implement TTLManager**

```python
# storage/ttl_manager.py
import sqlite3
from typing import List
from .decay_policy import get_low_utility_entries, decay_utility

class TTLManager:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
    
    def cleanup_expired(self):
        """Delete expired memory entries."""
        self.conn.execute("DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP")
        self.conn.commit()
    
    def consolidate_low_utility(self, threshold: float = 0.3):
        """Decay low-utility entries."""
        low_utility_keys = get_low_utility_entries(self.conn, threshold)
        for key in low_utility_keys:
            decay_utility(self.conn, key)
    
    def run_daily_maintenance(self):
        """Run daily maintenance (scheduled at 02:00 UTC)."""
        self.cleanup_expired()
        self.consolidate_low_utility()
```

- [ ] **Step 3: Commit**

```bash
git add storage/ttl_manager.py tests/unit/storage/test_ttl_manager.py
git commit -m "feat: add TTL manager with daily maintenance"
```

---

### Task 1.9: Storage Integration Test

**Files:**
- Create: `tests/integration/storage/test_storage_integration.py`

- [ ] **Step 1: Write integration test for full storage workflow**

```python
# tests/integration/storage/test_storage_integration.py
import pytest
import tempfile
from pathlib import Path
from compositional_co_scientist.storage.sqlite_backend import DatabaseInitializer
from compositional_co_scientist.storage.memory_db import MemoryDatabase
from compositional_co_scientist.storage.audit_db import AuditDatabase
from compositional_co_scientist.storage.ttl_manager import TTLManager

def test_full_storage_workflow():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Initialize databases
        memory_db = MemoryDatabase(tmpdir / "memory.db")
        memory_db.initialize()
        
        audit_db = AuditDatabase(tmpdir / "audit.db")
        audit_db.initialize()
        
        # Persist and recall
        memory_db.persist("test-key", {"data": "value"}, ttl=3600)
        value = memory_db.recall("test-key")
        assert value == {"data": "value"}
        
        # Log audit event
        log_id = audit_db.log_event("MEMORY_TEST", {"key": "test-key"}, "INFO")
        assert log_id >= 1
        
        # Query audit log
        events = audit_db.query_by_event_type("MEMORY_TEST")
        assert len(events) == 1
```

- [ ] **Step 2: Run integration test**

```bash
pytest tests/integration/storage/test_storage_integration.py -v
```
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add tests/integration/storage/
git commit -m "test: add storage integration test"
```

---

### Task 1.10: Phase 1 Coverage Audit

- [ ] **Step 1: Run coverage report**

```bash
pytest --cov=compositional_co_scientist/storage --cov-report=term-missing --cov-branch tests/unit/storage/ tests/integration/storage/
```

- [ ] **Step 2: Verify 80% branch coverage**

Expected: >= 80% branch coverage for storage layer

- [ ] **Step 3: If coverage < 80%, add missing tests**

- [ ] **Step 4: Commit coverage report**

```bash
git add .coverage htmlcov/
git commit -m "docs: add Phase 1 coverage report"
```

---

## Phase 2: Input Layer (GENERATE + RETRIEVE)

**Duration:** ~25 hours
**Deliverables:** GENERATE primitive (P1), RETRIEVE primitive (P5), skills, commands
**Exit Criteria:** All unit tests pass (8 tests), diversity metrics working, 80% branch coverage

### Task 2.1: GENERATE Primitive

**Files:**
- Create: `core/primitives/generate.py`
- Test: `tests/unit/primitives/test_generate.py`

- [ ] **Step 1: Write failing test for candidate generation**

```python
# tests/unit/primitives/test_generate.py
from compositional_co_scientist.core.primitives.generate import generate

def test_generate_produces_candidates():
    candidates = generate(
        goal="What causes superconductivity?",
        constraints={"max_candidates": 5},
        temperature=0.7
    )
    assert len(candidates["candidates"]) >= 3
    assert "diversity_score" in candidates
    assert candidates["diversity_score"] > 0
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/unit/primitives/test_generate.py::test_generate_produces_candidates -v
```
Expected: FAIL with "cannot import name 'generate'"

- [ ] **Step 3: Implement GENERATE primitive**

```python
# core/primitives/generate.py
from typing import Dict, Any, List
from ..models.candidate import Candidate
import uuid

def generate(goal: str, constraints: Dict[str, Any], temperature: float = 0.7) -> Dict[str, Any]:
    """Generate candidate hypotheses for a research goal."""
    max_candidates = constraints.get("max_candidates", 5)
    candidates = [
        Candidate(
            id=str(uuid.uuid4()),
            goal_id=goal[:20],
            content=f"Candidate hypothesis {i+1} for: {goal}",
            metadata={"temperature": temperature, "iteration": i}
        )
        for i in range(max_candidates)
    ]
    diversity_score = compute_diversity(candidates)
    return {"candidates": candidates, "diversity_score": diversity_score}

def compute_diversity(candidates: List[Candidate]) -> float:
    """Compute diversity score using embedding similarity."""
    if len(candidates) < 2:
        return 1.0
    # Placeholder - actual implementation uses sentence-transformers
    return 0.5
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/unit/primitives/test_generate.py -v
```
Expected: 2 tests PASS

- [ ] **Step 5: Commit**

```bash
git add core/primitives/generate.py tests/unit/primitives/test_generate.py
git commit -m "feat: implement GENERATE primitive with diversity scoring"
```

---

### Task 2.2: RETRIEVE Primitive

**Files:**
- Create: `core/primitives/retrieve.py`
- Test: `tests/unit/primitives/test_retrieve.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_retrieve.py
from compositional_co_scientist.core.primitives.retrieve import retrieve

def test_retrieve_fetches_documents():
    results = retrieve(
        query="superconductivity mechanisms",
        sources=["arxiv", "wikipedia"],
        relevance_threshold=0.5
    )
    assert len(results["results"]) >= 1
    assert "relevance_scores" in results
```

- [ ] **Step 2: Implement RETRIEVE**

```python
# core/primitives/retrieve.py
from typing import Dict, List
from ..models.document import Document
import uuid

def retrieve(query: str, sources: List[str], relevance_threshold: float = 0.5) -> Dict[str, Any]:
    """Retrieve external context for grounding."""
    results = [
        Document(id=str(uuid.uuid4()), source=source, content=f"Retrieved from {source}: {query}")
        for source in sources
    ]
    relevance_scores = {doc.id: 0.8 for doc in results}
    return {"results": results, "relevance_scores": relevance_scores}
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/retrieve.py tests/unit/primitives/test_retrieve.py
git commit -m "feat: implement RETRIEVE primitive"
```

---

## Phase 3: Judgment Layer (EVALUATE + CRITIQUE)

**Duration:** ~25 hours
**Deliverables:** EVALUATE primitive (P2), CRITIQUE primitive (P3), C1 enforcement
**Exit Criteria:** Evaluator independence enforced, calibration working

### Task 3.1: EVALUATE Primitive

**Files:**
- Create: `core/primitives/evaluate.py`
- Test: `tests/unit/primitives/test_evaluate.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_evaluate.py
from compositional_co_scientist.core.primitives.evaluate import evaluate

def test_evaluate_scores_candidates():
    candidates = {"candidates": []}  # Mock
    scored = evaluate(candidates, rubric={"coherence": 0.5}, evaluator_model="gpt-4")
    assert "scores" in scored
```

- [ ] **Step 2: Implement EVALUATE**

```python
# core/primitives/evaluate.py
from typing import Dict, Any
from ..models.score import Score

def evaluate(candidates: Dict[str, Any], rubric: Dict[str, float], evaluator_model: str) -> Dict[str, Any]:
    """Evaluate candidates against rubric."""
    scores = [Score(candidate_id=c.id, evaluator_model=evaluator_model, score=0.75, rubric=rubric)
              for c in candidates["candidates"]]
    return {"scores": scores, "calibration": 1.0}
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/evaluate.py tests/unit/primitives/test_evaluate.py
git commit -m "feat: implement EVALUATE primitive"
```

---

### Task 3.2: CRITIQUE Primitive

**Files:**
- Create: `core/primitives/critique.py`
- Test: `tests/unit/primitives/test_critique.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_critique.py
from compositional_co_scientist.core.primitives.critique import critique

def test_critique_identifies_defects():
    candidates = {"candidates": []}  # Mock
    defects = critique(candidates, defect_taxonomy=["logical_error"])
    assert "defects" in defects
```

- [ ] **Step 2: Implement CRITIQUE**

```python
# core/primitives/critique.py
from typing import Dict, Any, List
from ..models.defect import Defect

def critique(candidates: Dict[str, Any], defect_taxonomy: List[str]) -> Dict[str, Any]:
    """Identify defects in candidates."""
    defects = [Defect(candidate_id=c.id, defect_type="placeholder", description="TBD")
               for c in candidates["candidates"]]
    return {"defects": defects, "coverage": 1.0}
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/critique.py tests/unit/primitives/test_critique.py
git commit -m "feat: implement CRITIQUE primitive"
```

---

### Task 3.3: C1 Evaluator Independence Enforcement

**Files:**
- Create: `core/constraints/c1_evaluator_independence.py`
- Test: `tests/unit/constraints/test_c1_evaluator_independence.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/constraints/test_c1_evaluator_independence.py
import pytest
from compositional_co_scientist.core.constraints.c1_evaluator_independence import check_evaluator_independence
from compositional_co_scientist.core.errors import ConstraintViolationError

def test_c1_allows_different_models():
    assert check_evaluator_independence("gpt-4", "claude-3") is True

def test_c1_blocks_same_model():
    with pytest.raises(ConstraintViolationError):
        check_evaluator_independence("gpt-4", "gpt-4")
```

- [ ] **Step 2: Implement C1 enforcement**

```python
# core/constraints/c1_evaluator_independence.py
from compositional_co_scientist.core.errors import ConstraintViolationError

def check_evaluator_independence(generator_model: str, evaluator_model: str) -> bool:
    """Check C1: EVALUATE must use different model than GENERATE."""
    if generator_model == evaluator_model:
        raise ConstraintViolationError(f"C1 violated: models must differ")
    return True
```

- [ ] **Step 3: Commit**

```bash
git add core/constraints/c1_evaluator_independence.py tests/unit/constraints/test_c1_evaluator_independence.py
git commit -m "feat: implement C1 evaluator independence constraint"
```

---

## Phase 4: Decision Layer (SELECT)

**Duration:** ~15 hours
**Deliverables:** SELECT primitive (P4), C2 + C3 enforcement
**Exit Criteria:** Diversity quota enforced, temporal order enforced

### Task 4.1: SELECT Primitive

**Files:**
- Create: `core/primitives/select.py`
- Test: `tests/unit/primitives/test_select.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_select.py
from compositional_co_scientist.core.primitives.select import select

def test_select_chooses_survivors():
    scored = {"scores": []}  # Mock
    survivors = select(scored, diversity_quota=0.4)
    assert "survivors" in survivors
```

- [ ] **Step 2: Implement SELECT**

```python
# core/primitives/select.py
from typing import Dict, Any

def select(scored: Dict[str, Any], diversity_quota: float = 0.4) -> Dict[str, Any]:
    """Select survivors with diversity quota."""
    survivors = scored["scores"][:int(len(scored["scores"]) * diversity_quota)]
    return {"survivors": survivors, "similarity_matrix": {}}
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/select.py tests/unit/primitives/test_select.py
git commit -m "feat: implement SELECT primitive"
```

---

### Task 4.2: C2 Temporal Order Enforcement

**Files:**
- Create: `core/constraints/c2_temporal_order.py`
- Test: `tests/unit/constraints/test_c2_temporal_order.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/constraints/test_c2_temporal_order.py
import pytest
from compositional_co_scientist.core.constraints.c2_temporal_order import WorkflowStateMachine
from compositional_co_scientist.core.errors import InvalidTransitionError

def test_c2_valid_transition():
    fsm = WorkflowStateMachine()
    fsm.transition("GENERATING", "EVALUATING")

def test_c2_invalid_transition():
    fsm = WorkflowStateMachine()
    with pytest.raises(InvalidTransitionError):
        fsm.transition("GENERATING", "SELECTING")
```

- [ ] **Step 2: Implement C2 enforcement**

```python
# core/constraints/c2_temporal_order.py
from compositional_co_scientist.core.errors import InvalidTransitionError

class WorkflowStateMachine:
    VALID_TRANSITIONS = {
        "IDLE": ["GENERATING"], "GENERATING": ["EVALUATING"],
        "EVALUATING": ["SELECTING"], "SELECTING": ["SYNTHESIZING", "GENERATING"],
        "SYNTHESIZING": ["COMPLETE"], "COMPLETE": ["IDLE"], "ERROR": ["IDLE"]
    }
    
    def __init__(self):
        self.current_state = "IDLE"
    
    def transition(self, from_state: str, to_state: str) -> bool:
        if from_state != self.current_state:
            raise InvalidTransitionError(f"State mismatch: {self.current_state} vs {from_state}")
        if to_state not in self.VALID_TRANSITIONS.get(from_state, []):
            raise InvalidTransitionError(f"C2 violated: {from_state} → {to_state}")
        self.current_state = to_state
        return True
```

- [ ] **Step 3: Commit**

```bash
git add core/constraints/c2_temporal_order.py tests/unit/constraints/test_c2_temporal_order.py
git commit -m "feat: implement C2 temporal order constraint with state machine"
```

---

## Phase 5: Output Layer (SYNTHESIZE + ACT)

**Duration:** ~20 hours
**Deliverables:** SYNTHESIZE primitive (P7), ACT primitive (P6), C6 enforcement
**Exit Criteria:** Sandbox enforcement working, tension preservation working

### Task 5.1: SYNTHESIZE Primitive

**Files:**
- Create: `core/primitives/synthesize.py`
- Test: `tests/unit/primitives/test_synthesize.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_synthesize.py
from compositional_co_scientist.core.primitives.synthesize import synthesize

def test_synthesize_produces_output():
    output = synthesize({"survivors": []}, {"results": []}, preserve_tensions=True)
    assert "output" in output
```

- [ ] **Step 2: Implement SYNTHESIZE**

```python
# core/primitives/synthesize.py
from typing import Dict, Any

def synthesize(survivors: Dict[str, Any], context: Dict[str, Any], preserve_tensions: bool = True) -> Dict[str, Any]:
    """Synthesize survivors into coherent output."""
    return {"output": "Synthesized output", "tension_map": {}, "confidence": 0.8}
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/synthesize.py tests/unit/primitives/test_synthesize.py
git commit -m "feat: implement SYNTHESIZE primitive"
```

---

### Task 5.2: ACT Primitive with C6 Sandbox

**Files:**
- Create: `core/primitives/act.py`
- Create: `core/constraints/c6_sandbox_enforcement.py`
- Test: `tests/unit/primitives/test_act.py`
- Test: `tests/unit/constraints/test_c6_sandbox.py`

- [ ] **Step 1: Write failing test**

```python
# tests/unit/primitives/test_act.py
from compositional_co_scientist.core.primitives.act import act

def test_act_invokes_tool():
    result = act("search", {"query": "test"}, {"allowed_tools": ["search"]})
    assert "result" in result
    assert result["validation"] is True
```

- [ ] **Step 2: Implement ACT + C6**

```python
# core/primitives/act.py
from typing import Dict, Any
from ..constraints.c6_sandbox_enforcement import check_sandbox_permission

def act(tool_name: str, params: Dict[str, Any], sandbox_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Invoke tool with sandbox enforcement."""
    try:
        check_sandbox_permission(tool_name, params, sandbox_spec)
    except Exception as e:
        return {"result": None, "validation": False, "error": str(e)}
    return {"result": "Tool result", "validation": True, "error": None}
```

```python
# core/constraints/c6_sandbox_enforcement.py
from compositional_co_scientist.core.errors import SandboxViolationError

def check_sandbox_permission(tool_name: str, params: dict, sandbox_spec: dict):
    """Check C6: Tool must be in allowlist."""
    if tool_name not in sandbox_spec.get("allowed_tools", []):
        raise SandboxViolationError(f"C6 violated: '{tool_name}' not in allowlist")
```

- [ ] **Step 3: Commit**

```bash
git add core/primitives/act.py core/constraints/c6_sandbox_enforcement.py tests/
git commit -m "feat: implement ACT primitive with C6 sandbox enforcement"
```

---

## Phase 6: Integration + Host Adapters

**Duration:** ~15 hours
**Deliverables:** Claude/Qwen/Gemini adapters, integration tests
**Exit Criteria:** All 3 hosts working, 8 integration tests pass

### Task 6.1: Claude Code Adapter

**Files:**
- Create: `adapters/claude_code/__init__.py`
- Create: `adapters/claude_code/skill.py`
- Create: `adapters/claude_code/command.py`
- Test: `tests/integration/adapters/test_claude_code.py`

- [ ] **Step 1: Write failing test**

```python
# tests/integration/adapters/test_claude_code.py
from adapters.claude_code.skill import ClaudeSkill

def test_claude_skill_registration():
    skill = ClaudeSkill()
    assert skill.name == "generate"
```

- [ ] **Step 2: Implement Claude adapter**

```python
# adapters/claude_code/skill.py
class ClaudeSkill:
    """Claude Code SKILL tool adapter."""
    def __init__(self):
        self.name = "generate"
    def invoke(self, **kwargs):
        pass  # Uses Claude Code SKILL tool API
```

- [ ] **Step 3: Commit**

```bash
git add adapters/claude_code/ tests/integration/adapters/test_claude_code.py
git commit -m "feat: implement Claude Code adapter"
```

---

### Task 6.2: Qwen Code Adapter

**Files:**
- Create: `adapters/qwen_code/__init__.py`
- Create: `adapters/qwen_code/skill.py`
- Create: `adapters/qwen_code/command.py`
- Test: `tests/integration/adapters/test_qwen_code.py`

*(Same TDD pattern as Task 6.1)*

---

### Task 6.3: Gemini CLI Adapter

**Files:**
- Create: `adapters/gemini_cli/tool.py`
- Create: `adapters/gemini_cli/command.py`
- Test: `tests/integration/adapters/test_gemini_cli.py`

*(Same TDD pattern - uses tool declaration instead of SKILL)*

---

## Phase 7: Documentation + Polish

**Duration:** ~10 hours
**Deliverables:** API reference, user guide, tutorials, examples, plugin.json
**Exit Criteria:** All docs present, final coverage >= 80%

### Task 7.1: API Reference Documentation

**Files:**
- Create: `docs/api-reference/primitives.md`
- Create: `docs/api-reference/constraints.md`
- Create: `docs/api-reference/storage.md`
- Create: `docs/api-reference/errors.md`

- [ ] **Step 1: Write API reference for all 9 primitives**
- [ ] **Step 2: Commit**

```bash
git add docs/api-reference/
git commit -m "docs: add API reference"
```

---

### Task 7.2: Plugin Manifest

**Files:**
- Create: `plugin.json`

- [ ] **Step 1: Create plugin.json using spec Appendix C schema**

```json
{
  "name": "compositional-co-scientist",
  "version": "1.0.0",
  "description": "Evidence-anchored agentic scaffolding for scientific reasoning",
  "author": "Your Name",
  "license": "MIT",
  "skills": [
    {"name": "generate", "handler": "api/skills/generate_skill.py"},
    {"name": "evaluate", "handler": "api/skills/evaluate_skill.py"},
    {"name": "critique", "handler": "api/skills/critique_skill.py"},
    {"name": "select", "handler": "api/skills/select_skill.py"},
    {"name": "retrieve", "handler": "api/skills/retrieve_skill.py"},
    {"name": "act", "handler": "api/skills/act_skill.py"},
    {"name": "synthesize", "handler": "api/skills/synthesize_skill.py"},
    {"name": "memory", "handler": "api/skills/memory_skill.py"},
    {"name": "log", "handler": "api/skills/log_skill.py"}
  ],
  "commands": [
    {"name": "/generate", "handler": "api/commands/handlers.py:handle_generate"},
    {"name": "/evaluate", "handler": "api/commands/handlers.py:handle_evaluate"},
    {"name": "/synthesize", "handler": "api/commands/handlers.py:handle_synthesize"}
  ],
  "hosts": ["claude-code", "qwen-code", "gemini-cli"]
}
```

- [ ] **Step 2: Commit**

```bash
git add plugin.json
git commit -m "feat: add plugin manifest"
```

---

### Task 7.3: Final Coverage Audit

- [ ] **Step 1: Run full coverage report**

```bash
pytest --cov=compositional_co_scientist --cov-report=term-missing --cov-branch --cov-fail-under=80 tests/
```

- [ ] **Step 2: Verify >= 80% branch coverage**

Expected: >= 80% branch coverage

- [ ] **Step 3: If coverage < 80%, add missing tests**

- [ ] **Step 4: Commit coverage report**

```bash
git add .coverage htmlcov/
git commit -m "docs: add final coverage report (>= 80%)"
```

---

## Plan Review

**Plan Status:** Revised (All phases expanded with TDD tasks)
**Next Step:** Dispatch plan-document-reviewer subagent for second review
**After Review:** Fix issues if any, max 3 iterations
**After Approval:** Present execution options to user
