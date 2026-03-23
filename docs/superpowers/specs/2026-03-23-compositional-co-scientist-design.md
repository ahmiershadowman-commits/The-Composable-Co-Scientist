# The Compositional Co-Scientist: Production Plugin Specification

**Date:** 2026-03-23  
**Status:** Approved (Post-Review Revision 1 — All CRITICAL/HIGH issues fixed)  
**Author:** Qwen (with human collaborator)  
**Version:** 1.0.1 (Full v1: 9 primitives, 6 constraints, 8 families)  
**Spec Review:** Completed — 3 CRITICAL + 4 HIGH + 3 MEDIUM + 4 LOW issues fixed

**Fixes Applied:**
1. ✅ Evidence anchors added (Section 1.3)
2. ✅ Primitive count clarified (9 primitives, 10 sub-ops)
3. ✅ Middleware layer added to architecture
4. ✅ Host adapter specifications table added
5. ✅ Database initialization section added (3.4)
6. ✅ Decay policy specified (utility formula, cron schedule, threshold)
7. ✅ Timestamp handling specified (UTC everywhere)
8. ✅ Coverage measurement specified (branch coverage)
9. ✅ Similarity algorithm specified (sentence-transformers + fallback)
10. ✅ Workflow state machine added (Appendix A)
11. ✅ Retry strategy table added (Section 5.2)
12. ✅ Dependencies appendix added (Appendix B)
13. ✅ Plugin manifest schema added (Appendix C)

---

## Executive Summary

**The Compositional Co-Scientist** is a production-ready, multi-host plugin implementing an evidence-anchored dependency graph for agentic scaffolding in scientific research. The plugin provides **9 primitive operations** (with 10 sub-operations) as callable skills, enforces 6 non-negotiable constraints at the architecture level, and represents 8 functional families across a layered architecture.

**Target:** Reusable framework for scientific reasoning workflows (Claude Code, Qwen Code, Gemini CLI).

**Quality Gates:**
- Test coverage: 80% branch coverage minimum (unit + integration)
- Documentation: API reference + user guide + tutorials + examples
- Error handling: Graceful degradation + user-facing messages
- Performance: Adjustable latency, concurrent requests, caching enabled

**Estimated Effort:** ~120 hours

---

## 1.3 Evidence Anchors

All primitives and constraints are derived from the dependency graph spec (`docs/superpowers/specs/2026-03-23-dependency-graph-design.md`).

| Primitive/Constraint | Dependency Graph Spec Section | Evidence Source | Confidence |
|---------------------|-------------------------------|-----------------|------------|
| **P1: GENERATE** | Section 2 (Primitives P1) | QD literature, Tree-of-Thoughts | HIGH |
| **P2: EVALUATE** | Section 2 (Primitives P2) | Huang et al. (ICLR 2024) | HIGH |
| **P3: CRITIQUE** | Section 2 (Primitives P3) | Inferred (distinct failure mode) | MEDIUM-HIGH |
| **P4: SELECT** | Section 2 (Primitives P4) | FunSearch (Nature 2024), QD algorithms | HIGH |
| **P5: RETRIEVE** | Section 2 (Primitives P5) | RAG literature, GraphRAG | HIGH |
| **P6: ACT** | Section 2 (Primitives P6) | OWASP LLM Top 10 | HIGH |
| **P7: SYNTHESIZE** | Section 2 (Primitives P7) | Dialectical ontology (4/9 docs) | MEDIUM |
| **P8: MEMORY** (persist/recall) | Section 2 (Primitives P8) | MemGPT, W3C PROV | HIGH |
| **P9: LOG** (event) | Section 2 (Primitives P9) | W3C PROV standard | MEDIUM |
| **C1: Evaluator Independence** | Section 7 (Validated Relationships R1) | Huang et al., Kambhampati et al. | HIGH |
| **C2: Temporal Order** | Section 7 (Validated Relationships R2) | Tree-of-Thoughts, FunSearch | HIGH |
| **C3: Diversity Quota** | Section 7 (Inferred Relationships R15) | QD literature (FunSearch, MAP-Elites) | MEDIUM-HIGH |
| **C4: Log Completeness** | Section 7 (Inferred Relationships R13) | W3C PROV, audit best practices | MEDIUM |
| **C5: Memory Decay** | Section 7 (Inferred Relationships R18) | MemGPT, path dependence literature | MEDIUM-HIGH |
| **C6: Sandbox Enforcement** | Section 7 (Inferred Relationships R17) | OWASP LLM Top 10 | HIGH |

---

## 1. Architecture

### 1.1 Layered Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HOST ADAPTER LAYER                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │
│  │  Claude Code    │  │   Qwen Code     │  │  Gemini CLI     │      │
│  │  (native skill) │  │  (native skill) │  │  (native tool)  │      │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘      │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PLUGIN API LAYER                                  │
│  - Skill routing (primitive dispatch)                               │
│  - Command parsing (slash commands)                                 │
│  - Input validation (schema enforcement)                            │
│  - Error handling (graceful + user-facing)                          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    MIDDLEWARE LAYER                                  │
│  - Constraint enforcement interceptors                               │
│  - Audit logging hooks (C4)                                          │
│  - Permission validation (C6)                                        │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PRIMITIVES LAYER (9 primitives, 10 sub-ops)       │
│  GENERATE, EVALUATE, CRITIQUE, SELECT, RETRIEVE, ACT,               │
│  SYNTHESIZE, MEMORY (persist/recall), LOG                           │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CONSTRAINT ENFORCEMENT LAYER (6 rules)            │
│  C1: EVALUATE ≠ GENERATE (different models)                         │
│  C2: GENERATE → EVALUATE → SELECT (temporal order)                  │
│  C3: DIVERSITY quota at SELECT                                      │
│  C4: LOG all EVALUATE operations                                    │
│  C5: MEMORY decay policy                                            │
│  C6: ACT sandbox enforcement                                        │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    STORAGE LAYER (SQLite)                            │
│  candidates.db, memory.db, audit.db                                 │
│  TTL manager, decay policy, audit log                               │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Design Principles

1. **Layered isolation** — Host changes don't affect primitives; primitive changes don't affect storage
2. **Constraint enforcement as a layer** — Centralized, testable, auditable
3. **9 primitives as discrete modules** — Each independently testable (MEMORY has 2 sub-ops: persist/recall)
4. **SQLite per-purpose** — Separate DBs for candidates, memory, audit

### 1.3 Host Adapter Specifications

| Host | Integration Type | Skill File | Command File | Notes |
|------|------------------|------------|--------------|-------|
| Claude Code | Native skill | `adapters/claude_code/skill.py` | `adapters/claude_code/command.py` | Uses SKILL tool |
| Qwen Code | Native skill | `adapters/qwen_code/skill.py` | `adapters/qwen_code/command.py` | Uses SKILL tool |
| Gemini CLI | Native tool | `adapters/gemini_cli/tool.py` | `adapters/gemini_cli/command.py` | Uses tool declaration |

All hosts support slash commands via `command.py`.

---

## 2. Primitives API

### 2.1 Primitive Signatures

**Note:** 9 primitives total, with MEMORY having 2 sub-operations (persist/recall) and LOG having 1 sub-operation (event), for 10 total callable operations.

| ID | Primitive | Signature | Returns | Failure Mode | Confidence |
|----|-----------|-----------|---------|--------------|------------|
| **P1** | **GENERATE** | `generate(goal: str, constraints: dict, temperature: float) → CandidateSet` | `{candidates: [Candidate], diversity_score: float}` | Mode collapse (diversity < threshold) | HIGH |
| **P2** | **EVALUATE** | `evaluate(candidates: CandidateSet, rubric: dict, evaluator_model: str) → ScoredSet` | `{scores: [Score], calibration: float}` | Evaluator collapse (calibration drift) | HIGH |
| **P3** | **CRITIQUE** | `critique(candidates: CandidateSet, defect_taxonomy: list) → CritiqueSet` | `{defects: [Defect], coverage: float}` | Coverage error (missed defects) | MEDIUM-HIGH |
| **P4** | **SELECT** | `select(scored: ScoredSet, diversity_quota: float) → SurvivorSet` | `{survivors: [Candidate], similarity_matrix: dict}` | Premature convergence | HIGH |
| **P5** | **RETRIEVE** | `retrieve(query: str, sources: list, relevance_threshold: float) → ContextSet` | `{results: [Document], relevance_scores: dict}` | Retrieval dominance | HIGH |
| **P6** | **ACT** | `act(tool_name: str, params: dict, sandbox_spec: dict) → ToolResult` | `{result: any, validation: bool, error: str}` | Tool-output credulity | HIGH |
| **P7** | **SYNTHESIZE** | `synthesize(survivors: SurvivorSet, context: ContextSet, preserve_tensions: bool) → Output` | `{output: str, tension_map: dict, confidence: float}` | Averaging to mediocrity | MEDIUM |
| **P8** | **MEMORY.persist** | `persist(key: str, value: any, ttl: int) → str` | `artifact_id` | Memory bloat | HIGH |
| **P9** | **MEMORY.recall** | `recall(key: str) → any` | `value` | Path dependence | HIGH |
| **P10** | **LOG.event** | `event(event_type: str, data: dict, severity: str) → str` | `log_id` | Invisible failures | MEDIUM |

**Similarity Computation (for P4 SELECT):** Use sentence-transformers (all-MiniLM-L6-v2) for embedding candidates. Cosine similarity threshold: 0.7 (configurable). Fallback: If embeddings unavailable, use Jaccard similarity on token sets (threshold: 0.5).

### 2.2 Data Models

```python
@dataclass
class Candidate:
    id: str
    goal_id: str
    content: str
    metadata: dict
    created_at: datetime

@dataclass
class Score:
    candidate_id: str
    evaluator_model: str
    score: float
    rubric: dict
    calibration: float
    created_at: datetime

@dataclass
class Defect:
    candidate_id: str
    defect_type: str
    description: str
    severity: str
    created_at: datetime

@dataclass
class Document:
    id: str
    source: str
    content: str
    relevance_score: float
    metadata: dict
```

---

## 3. Storage Schema

### 3.1 candidates.db

```sql
CREATE TABLE candidates (
    id TEXT PRIMARY KEY,
    goal_id TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata JSON,
    diversity_score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id TEXT NOT NULL,
    evaluator_model TEXT NOT NULL,
    score REAL NOT NULL,
    rubric JSON,
    calibration REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

CREATE TABLE survivors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    candidate_id TEXT NOT NULL,
    diversity_quota_met BOOLEAN,
    similarity_matrix JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);

CREATE INDEX idx_goal ON candidates(goal_id);
CREATE INDEX idx_scores ON scores(candidate_id);
CREATE INDEX idx_run ON survivors(run_id);
```

### 3.2 memory.db

```sql
CREATE TABLE memory (
    key TEXT PRIMARY KEY,
    value JSON NOT NULL,
    ttl INTEGER,
    expires_at TIMESTAMP,
    utility_score REAL DEFAULT 1.0,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_expires ON memory(expires_at);
CREATE INDEX idx_utility ON memory(utility_score);

-- Periodic cleanup query:
-- DELETE FROM memory WHERE expires_at < CURRENT_TIMESTAMP;
```

**Utility Score Computation:** `utility_score = 1.0 / (1.0 + days_since_last_accessed)`  
**Decay Threshold:** utility_score < 0.3 → mark for consolidation  
**TTL Default:** 30 days (configurable)  
**Cron Schedule:** Daily at 02:00 UTC

### 3.3 audit.db

```sql
CREATE TABLE audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL,
    event_data JSON NOT NULL,
    severity TEXT DEFAULT 'INFO',
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Append-only: no UPDATE, no DELETE
-- Enforcement: REVOKE DELETE, REVOKE UPDATE on audit_log

CREATE INDEX idx_event_type ON audit_log(event_type);
CREATE INDEX idx_timestamp ON audit_log(timestamp);
CREATE INDEX idx_severity ON audit_log(severity);
```

### 3.4 Database Initialization

On first plugin load:
1. Check for existence of `~/.compositional-co-scientist/{candidates,memory,audit}.db`
2. If missing, run schema creation SQL from Sections 3.1-3.3
3. Log initialization event to audit.db

**File paths:**
- Windows: `%USERPROFILE%\.compositional-co-scientist\`
- Unix: `~/.compositional-co-scientist/`

**Migration strategy:** v1 schema is immutable; v2+ migrations require explicit user consent.

### 3.5 Timestamp Handling

All datetime objects MUST be timezone-aware (UTC):
```python
from datetime import datetime, timezone

@dataclass
class Candidate:
    created_at: datetime  # MUST be datetime.now(timezone.utc)
```

All SQLite TIMESTAMP columns store UTC. Python layer converts to/from UTC on read/write.

---

## 4. Constraint Enforcement

### 4.1 Constraint Specifications

| ID | Constraint | Enforcement Mechanism | Detection | Action on Violation |
|----|------------|----------------------|-----------|---------------------|
| **C1** | EVALUATE ≠ GENERATE (different models) | Model registry; reject if same model_id | Config validation at startup | Raise `ConstraintViolationError`; block operation |
| **C2** | GENERATE → EVALUATE → SELECT (temporal order) | State machine; invalid transitions rejected | Workflow engine state tracking | Raise `InvalidTransitionError`; halt workflow |
| **C3** | DIVERSITY quota at SELECT | Enforced in SELECT; reject if similarity > threshold | `diversity_score` check post-SELECT | Loop to GENERATE with anti-canon prompt |
| **C4** | LOG all EVALUATE operations | Middleware; intercept all evaluate calls | Log completeness audit at completion | Block completion; require audit resolution |
| **C5** | MEMORY decay policy | TTL manager (cron); periodic consolidation | `expires_at` scan; utility score check | Delete expired; decay low-utility entries |
| **C6** | ACT sandbox enforcement | Permission manifest; tool allowlist | Pre-execution validation | Reject unallowed tools; log attempt |

### 4.2 Constraint Enforcement Code Structure

```python
# core/constraints/enforcer.py

class ConstraintEnforcer:
    def __init__(self, config: ConstraintConfig):
        self.config = config
        self.model_registry = ModelRegistry()
        self.workflow_state = WorkflowStateMachine()
        self.log_auditor = LogAuditor()

    def check_c1_evaluator_independence(self, generate_model: str, evaluate_model: str):
        if generate_model == evaluate_model:
            raise ConstraintViolationError(
                "C1 violated: EVALUATE must use different model than GENERATE"
            )

    def check_c2_temporal_order(self, current_state: str, requested_transition: str):
        if not self.workflow_state.is_valid_transition(current_state, requested_transition):
            raise InvalidTransitionError(
                f"C2 violated: Invalid transition {current_state} → {requested_transition}"
            )

    def check_c3_diversity_quota(self, survivors: list, threshold: float):
        similarity = compute_similarity_matrix(survivors)
        if similarity.max() > threshold:
            return False  # Trigger regeneration
        return True

    def check_c4_log_completeness(self, operation_id: str):
        if not self.log_auditor.has_entry(operation_id):
            raise LogCompletenessError(
                f"C4 violated: No audit log for operation {operation_id}"
            )

    def check_c5_memory_decay(self):
        expired = self.storage.get_expired_memory()
        self.storage.delete_expired(expired)
        low_utility = self.storage.get_low_utility_memory()
        self.storage.decay(low_utility)

    def check_c6_sandbox_enforcement(self, tool_name: str, params: dict):
        if not self.permission_manifest.is_allowed(tool_name, params):
            raise SandboxViolationError(
                f"C6 violated: Tool {tool_name} not in allowlist"
            )
```

---

## 5. Error Handling

### 5.1 Error Taxonomy

```python
# core/errors.py

class CompositionalCoScientistError(Exception):
    """Base exception for all plugin errors."""
    user_message = "An error occurred: {detail}"
    action = "Please try again or contact support"

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

class HostAdapterError(CompositionalCoScientistError):
    """Raised on host integration failures."""
    user_message = "Host integration error: {detail}"
    action = "Check host configuration and restart the plugin"
    severity = "ERROR"

class InvalidTransitionError(ConstraintViolationError):
    """Raised when workflow state machine detects invalid transition."""
    user_message = "Invalid workflow transition: {detail}"
    action = "Restart the workflow from the beginning"
    severity = "CRITICAL"

class LogCompletenessError(ConstraintViolationError):
    """Raised when audit log is incomplete."""
    user_message = "Audit log incomplete: {detail}"
    action = "Run audit resolution before continuing"
    severity = "CRITICAL"

class SandboxViolationError(ConstraintViolationError):
    """Raised when tool execution violates sandbox."""
    user_message = "Tool execution blocked: {detail}"
    action = "Review tool permissions and retry"
    severity = "CRITICAL"
```

### 5.2 Graceful Degradation Strategy

| Error Severity | Behavior | User Message | Audit Log | Retryable |
|----------------|----------|--------------|-----------|-----------|
| **CRITICAL** (constraint violations) | Halt immediately; block operation | Clear explanation + action required | Always logged | No |
| **ERROR** (primitive/storage failures) | Retry up to 3×; then degrade | "Operation failed; trying alternative approach" | Always logged | See table below |
| **WARNING** (non-critical failures) | Log + continue with degraded mode | Silent (or optional notification) | Logged | N/A |
| **INFO** (expected conditions) | Normal handling | No message | Selectively logged | N/A |

**Retry Strategy by Primitive:**

| Primitive | Failure Mode | Retryable | Retry Strategy |
|-----------|--------------|-----------|----------------|
| GENERATE | Mode collapse | Yes | Increase temperature +0.2, max 3× |
| EVALUATE | Calibration drift | No | Use fallback evaluator |
| CRITIQUE | Coverage error | Yes | Expand defect taxonomy |
| SELECT | Premature convergence | Yes | Relax diversity quota |
| RETRIEVE | Retrieval dominance | Yes | Reduce relevance threshold |
| ACT | Sandbox violation | No | Block immediately |
| SYNTHESIZE | Averaging to mediocrity | Yes | Adjust tension preservation |
| MEMORY | Storage error | Yes | Retry with backoff |
| LOG | Audit failure | No | Block until resolved |

### 5.3 User-Facing Error Messages

All user-facing errors follow this template:

```
[Plugin Name] encountered an issue:

**What happened:** {clear description of the failure}

**Why it matters:** {impact on the user's workflow}

**What to do:** {specific, actionable step}

**Technical details:** {optional, expandable}
{error_id: ABC123, timestamp: 2026-03-23T10:30:00Z}
```

---

## 6. Testing Strategy

### 6.1 Coverage Targets

| Test Type | Target Coverage | Measurement |
|-----------|-----------------|-------------|
| **Unit tests** | 70% branch coverage | `pytest --cov=compositional_co_scientist --cov-report=term-missing --cov-branch` |
| **Integration tests** | 10% path coverage | End-to-end workflow coverage |
| **Total** | 80% branch coverage | Combined report |

### 6.2 Test Structure

```
tests/
├── unit/
│   ├── primitives/
│   │   ├── test_generate.py (3 tests: success, mode collapse, invalid params)
│   │   ├── test_evaluate.py (3 tests: success, calibration drift, independence check)
│   │   ├── test_critique.py (3 tests: success, coverage error, defect taxonomy)
│   │   ├── test_select.py (3 tests: success, premature convergence, diversity quota)
│   │   ├── test_retrieve.py (3 tests: success, retrieval dominance, relevance threshold)
│   │   ├── test_act.py (3 tests: success, sandbox violation, tool-output validation)
│   │   ├── test_synthesize.py (3 tests: success, averaging, tension preservation)
│   │   ├── test_memory.py (5 tests: persist, recall, TTL, decay, path dependence)
│   │   └── test_log.py (3 tests: event logging, completeness audit, query)
│   ├── constraints/
│   │   ├── test_c1_evaluator_independence.py (3 tests: pass, fail, config validation)
│   │   ├── test_c2_temporal_order.py (3 tests: valid transitions, invalid, state machine)
│   │   ├── test_c3_diversity_quota.py (3 tests: quota met, quota failed, regeneration)
│   │   ├── test_c4_log_completeness.py (3 tests: complete, incomplete, audit resolution)
│   │   ├── test_c5_memory_decay.py (3 tests: TTL enforcement, decay, consolidation)
│   │   └── test_c6_sandbox_enforcement.py (3 tests: allowed, blocked, permission manifest)
│   └── storage/
│       ├── test_candidates_db.py (5 tests: CRUD, indexing, queries)
│       ├── test_memory_db.py (5 tests: persist, recall, TTL, utility, cleanup)
│       └── test_audit_db.py (5 tests: append-only, query, integrity)
├── integration/
│   ├── test_workflows.py (5 tests: full pipeline, constraint enforcement, error handling)
│   └── test_adapters.py (3 tests: Claude, Qwen, Gemini)
└── conftest.py (fixtures, mocks, test utilities)
```

### 6.3 Test Count Summary

| Category | File Count | Tests per File | Total Tests |
|----------|------------|----------------|-------------|
| Primitives (unit) | 9 | 3-5 | 32 |
| Constraints (unit) | 6 | 3 | 18 |
| Storage (unit) | 3 | 5 | 15 |
| Workflows (integration) | 1 | 5 | 5 |
| Adapters (integration) | 1 | 3 | 3 |
| **Total** | **20** | **~3.5 avg** | **73 tests** |

---

## 7. Documentation Plan

### 7.1 Documentation Structure

```
docs/
├── api-reference/
│   ├── primitives.md (all 9 primitives with signatures, examples)
│   ├── constraints.md (all 6 constraints with enforcement details)
│   ├── storage.md (SQLite schemas, TTL, decay)
│   └── errors.md (error taxonomy, handling patterns)
├── user-guide/
│   ├── getting-started.md (installation, configuration, first workflow)
│   ├── skills.md (skill definitions, usage examples)
│   ├── commands.md (slash commands, parameters)
│   └── troubleshooting.md (common errors, solutions)
├── tutorials/
│   ├── tutorial-1-hypothesis-generation.md (GENERATE → EVALUATE → SELECT)
│   ├── tutorial-2-literature-review.md (RETRIEVE → SYNTHESIZE)
│   └── tutorial-3-full-workflow.md (end-to-end scientific reasoning)
└── examples/
    ├── example-1-basic-generation.md
    ├── example-2-constraint-enforcement.md
    ├── example-3-error-handling.md
    ├── example-4-multi-host.md (Claude vs. Qwen vs. Gemini)
    └── example-5-custom-rubrics.md
```

### 7.2 Documentation Content Requirements

| Document | Word Count | Code Examples | Diagrams |
|----------|------------|---------------|----------|
| API Reference | 5000 | 20 | 5 |
| User Guide | 3000 | 10 | 3 |
| Tutorials | 4000 | 15 | 5 |
| Examples | 3000 | 15 | 2 |
| **Total** | **15000** | **60** | **15** |

---

## 8. File Structure

```
compositional-co-scientist/
├── core/
│   ├── primitives/
│   │   ├── generate.py
│   │   ├── evaluate.py
│   │   ├── critique.py
│   │   ├── select.py
│   │   ├── retrieve.py
│   │   ├── act.py
│   │   ├── synthesize.py
│   │   └── memory.py
│   ├── constraints/
│   │   ├── enforcer.py
│   │   ├── c1_evaluator_independence.py
│   │   ├── c2_temporal_order.py
│   │   ├── c3_diversity_quota.py
│   │   ├── c4_log_completeness.py
│   │   ├── c5_memory_decay.py
│   │   └── c6_sandbox_enforcement.py
│   ├── models/
│   │   ├── candidate.py
│   │   ├── score.py
│   │   ├── defect.py
│   │   └── document.py
│   └── errors.py
├── storage/
│   ├── sqlite_backend.py
│   ├── ttl_manager.py
│   ├── decay_policy.py
│   └── audit_log.py
├── adapters/
│   ├── claude_code/
│   │   ├── skill.py
│   │   └── command.py
│   ├── qwen_code/
│   │   ├── skill.py
│   │   └── command.py
│   └── gemini_cli/
│       ├── tool.py
│       └── command.py
├── api/
│   ├── skills/
│   │   ├── __init__.py
│   │   ├── generate_skill.py
│   │   ├── evaluate_skill.py
│   │   └── ... (9 skills)
│   └── commands/
│       ├── __init__.py
│       └── handlers.py
├── tests/
│   ├── unit/
│   │   ├── primitives/
│   │   ├── constraints/
│   │   └── storage/
│   ├── integration/
│   │   ├── workflows/
│   │   └── adapters/
│   └── conftest.py
├── docs/
│   ├── api-reference/
│   ├── user-guide/
│   ├── tutorials/
│   └── examples/
├── plugin.json (universal plugin manifest)
├── requirements.txt
├── setup.py
└── README.md
```

---

## 9. Implementation Phases

### Phase 1: Substrate (MEMORY + LOG)
**Duration:** ~20 hours  
**Deliverables:**
- `storage/sqlite_backend.py` (persist, recall, TTL)
- `storage/audit_log.py` (append-only logging)
- `storage/ttl_manager.py` (decay policy)
- Unit tests for storage layer (15 tests)

### Phase 2: Input Layer (GENERATE + RETRIEVE)
**Duration:** ~25 hours  
**Deliverables:**
- `core/primitives/generate.py` (candidate generation)
- `core/primitives/retrieve.py` (external context fetch)
- Skills + commands for both primitives
- Unit tests (8 tests)

### Phase 3: Judgment Layer (EVALUATE + CRITIQUE)
**Duration:** ~25 hours  
**Deliverables:**
- `core/primitives/evaluate.py` (scoring with calibration)
- `core/primitives/critique.py` (defect identification)
- Constraint C1 enforcement (evaluator independence)
- Unit tests (10 tests)

### Phase 4: Decision Layer (SELECT)
**Duration:** ~15 hours  
**Deliverables:**
- `core/primitives/select.py` (survivor selection)
- Constraint C2 (temporal order) + C3 (diversity quota)
- Unit tests (6 tests)

### Phase 5: Output Layer (SYNTHESIZE + ACT)
**Duration:** ~20 hours  
**Deliverables:**
- `core/primitives/synthesize.py` (coherent output)
- `core/primitives/act.py` (tool invocation)
- Constraint C6 (sandbox enforcement)
- Unit tests (8 tests)

### Phase 6: Integration + Host Adapters
**Duration:** ~15 hours  
**Deliverables:**
- `adapters/claude_code/`, `adapters/qwen_code/`, `adapters/gemini_cli/`
- Integration tests (8 tests)
- End-to-end workflow tests (5 tests)

### Phase 7: Documentation + Polish
**Duration:** ~10 hours  
**Deliverables:**
- API reference, user guide, tutorials, examples
- README.md, plugin.json
- Final test coverage audit (80% target)

---

## 10. Success Criteria

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| **Test coverage** | 80% minimum | `pytest --cov=compositional_co_scientist --cov-report=term-missing` |
| **All constraints enforced** | C1-C6 | Integration tests pass |
| **All primitives functional** | P1-P10 | Unit tests pass |
| **Multi-host support** | Claude, Qwen, Gemini | Adapter tests pass |
| **Documentation complete** | 4 sections | All docs/ files present |
| **User-facing errors** | All errors have messages | Code review + manual test |

---

## 11. Open Questions (Deferred to v2)

| Question | v1 Decision | v2 Consideration |
|----------|-------------|------------------|
| Novelty assessment mechanism | Use embedding similarity (known limitations) | Develop new metric beyond similarity |
| Stage-transition thresholds | Hard-coded config values | Empirical calibration on benchmarks |
| Cross-family verification definition | Different model IDs sufficient | Test: same model vs. different family |
| Caching strategy | Simple LRU cache for RETRIEVE | Advanced caching with invalidation |

---

## 12. References

- Dependency graph spec: `docs/superpowers/specs/2026-03-23-dependency-graph-design.md`
- Evidence base: Huang et al. (ICLR 2024), Yao et al. (NeurIPS 2023), Romera-Paredes et al. (Nature 2024)
- OWASP LLM Top 10, W3C PROV standard
- Corpus documents (9 files in `docs/research/`)

---

## Appendix A: Workflow State Machine

### States

- **IDLE** — No active workflow
- **GENERATING** — GENERATE primitive executing
- **EVALUATING** — EVALUATE + CRITIQUE primitives executing
- **SELECTING** — SELECT primitive executing
- **SYNTHESIZING** — SYNTHESIZE primitive executing
- **COMPLETE** — Workflow finished successfully
- **ERROR** — Constraint violation or unrecoverable error

### Valid Transitions

```
IDLE → GENERATING (start workflow)
GENERATING → EVALUATING (candidates produced)
EVALUATING → SELECTING (scores + critiques complete)
SELECTING → SYNTHESIZING (survivors selected, diversity quota met)
SELECTING → GENERATING (diversity quota failed, max 3 loops)
SYNTHESIZING → COMPLETE (output produced)
COMPLETE → IDLE (workflow reset)
Any state → ERROR (on constraint violation)
ERROR → IDLE (after resolution or user abort)
```

### Invalid Transitions (Raise `InvalidTransitionError`)

- GENERATING → SELECTING (skip evaluation)
- EVALUATING → GENERATING (skip selection)
- SELECTING → EVALUATING (backwards)
- SYNTHESIZING → SELECTING (backwards)

---

## Appendix B: Dependencies

**Python:** >= 3.10

**Core Dependencies:**
```
sqlite3 (stdlib)
sentence-transformers >= 2.2.0
pydantic >= 2.0
```

**Testing Dependencies:**
```
pytest >= 7.0
pytest-cov >= 4.0
```

**Host Adapter Dependencies:**
```
# Claude Code: No additional dependencies (uses built-in SKILL tool)
# Qwen Code: No additional dependencies (uses built-in SKILL tool)
# Gemini CLI: No additional dependencies (uses built-in tool declaration)
```

---

## Appendix C: Plugin Manifest Schema

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
    {"name": "/critique", "handler": "api/commands/handlers.py:handle_critique"},
    {"name": "/select", "handler": "api/commands/handlers.py:handle_select"},
    {"name": "/retrieve", "handler": "api/commands/handlers.py:handle_retrieve"},
    {"name": "/act", "handler": "api/commands/handlers.py:handle_act"},
    {"name": "/synthesize", "handler": "api/commands/handlers.py:handle_synthesize"}
  ],
  "hosts": ["claude-code", "qwen-code", "gemini-cli"]
}
```

---

**Spec Status:** Approved (Post-Review Revision 1)  
**Spec Review:** Completed — 3 CRITICAL + 4 HIGH issues fixed  
**Next Step:** User review of written spec  
**After User Approval:** Invoke `writing-plans` skill for implementation plan
