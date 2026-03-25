# API Reference

This document provides detailed API reference for all primitives and constraints.

## Primitives

### GENERATE

Generate candidate hypotheses for a research goal.

**Function:** `compositional_co_scientist.api.skills.generate_skill.generate`

**Signature:**
```python
def generate(
    goal: str,
    constraints: Dict[str, Any] = None,
    temperature: float = 0.7,
    llm_response: str = None
) -> Dict[str, Any]
```

**Parameters:**
- `goal` (str): The research goal or question
- `constraints` (dict, optional): Generation constraints
  - `max_candidates` (int): Maximum candidates to generate (default: 5)
- `temperature` (float): Temperature for generation diversity (0.0-1.0, default: 0.7)
- `llm_response` (str, optional): Pre-computed LLM response for host integration

**Returns:**
```python
{
    "candidates": List[Dict],  # Generated candidates
    "diversity_score": float,  # Diversity score (0.0-1.0)
    "prompt_used": str         # Prompt template used
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import generate

result = generate(
    goal="What are the mechanisms of aging?",
    constraints={"max_candidates": 3},
    temperature=0.8
)

for candidate in result["candidates"]:
    print(f"ID: {candidate['id']}")
    print(f"Content: {candidate['content']}")
    print(f"Rationale: {candidate['metadata']['rationale']}")
```

---

### EVALUATE

Evaluate candidates against a rubric. Enforces **C1** (evaluator independence).

**Function:** `compositional_co_scientist.api.skills.evaluate_skill.evaluate`

**Signature:**
```python
def evaluate(
    candidates: List[Dict],
    rubric: Dict[str, float],
    evaluator_model: str,
    generator_model: str = None
) -> Dict[str, Any]
```

**Parameters:**
- `candidates` (List[Dict]): Candidates to evaluate
- `rubric` (Dict[str, float]): Scoring rubric with weights
- `evaluator_model` (str): Model ID for evaluation
- `generator_model` (str, optional): Model ID used for generation (for C1 check)

**Returns:**
```python
{
    "scored_candidates": List[Dict],  # Candidates with scores
    "c1_passed": bool,                # C1 constraint check
    "evaluation_log_id": str          # Audit log ID (C4)
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import evaluate

result = evaluate(
    candidates=candidates,
    rubric={"coherence": 0.5, "novelty": 0.5},
    evaluator_model="claude-3",
    generator_model="gpt-4"  # Must be different for C1
)

if not result["c1_passed"]:
    raise ValueError("C1 violation: evaluator must differ from generator")
```

**Constraints Enforced:**
- **C1**: Evaluator model must differ from generator model
- **C4**: All evaluations are logged for auditability

---

### CRITIQUE

Identify defects in candidates.

**Function:** `compositional_co_scientist.api.skills.critique_skill.critique`

**Signature:**
```python
def critique(
    candidate: Dict,
    critique_mode: str = "comprehensive"
) -> Dict[str, Any]
```

**Parameters:**
- `candidate` (Dict): Candidate to critique
- `critique_mode` (str): Critique mode
  - `"comprehensive"`: Full defect analysis
  - `"targeted"`: Focus on specific aspects

**Returns:**
```python
{
    "defects": List[Dict],      # Identified defects
    "severity_scores": Dict,    # Severity per defect
    "critique_log_id": str      # Audit log ID
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import critique

result = critique(candidate, critique_mode="comprehensive")

for defect in result["defects"]:
    print(f"Defect: {defect['description']}")
    print(f"Severity: {defect['severity']}")
```

---

### SELECT

Select survivors with diversity quota enforcement (**C3**).

**Function:** `compositional_co_scientist.api.skills.select_skill.select`

**Signature:**
```python
def select(
    scored_candidates: List[Dict],
    diversity_quota: float = 0.4,
    max_survivors: int = None
) -> Dict[str, Any]
```

**Parameters:**
- `scored_candidates` (List[Dict]): Scored candidates from EVALUATE
- `diversity_quota` (float): Minimum novelty score (0.0-1.0, default: 0.4)
- `max_survivors` (int, optional): Maximum survivors to select

**Returns:**
```python
{
    "survivors": List[Dict],       # Selected candidates
    "rejected": List[Dict],        # Rejected candidates
    "c3_passed": bool,             # Diversity quota check
    "similarity_matrix": List[List[float]]  # Pairwise similarity
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import select

result = select(
    scored_candidates,
    diversity_quota=0.4,
    max_survivors=3
)

if not result["c3_passed"]:
    # Auto-regenerate if diversity quota not met
    print("Diversity quota not met, regenerating...")
```

**Constraints Enforced:**
- **C3**: Diversity quota enforcement with auto-regenerate

---

### RETRIEVE

Fetch external context for grounding.

**Function:** `compositional_co_scientist.api.skills.retrieve_skill.retrieve`

**Signature:**
```python
def retrieve(
    query: str,
    sources: List[str] = None,
    max_results: int = 5
) -> Dict[str, Any]
```

**Parameters:**
- `query` (str): Search query
- `sources` (List[str], optional): Sources to search
- `max_results` (int): Maximum results to return

**Returns:**
```python
{
    "documents": List[Dict],   # Retrieved documents
    "relevance_scores": List[float],
    "sources_used": List[str]
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import retrieve

result = retrieve(
    query="high-temperature superconductivity mechanisms",
    sources=["arxiv", "pubmed"],
    max_results=10
)
```

---

### ACT

Invoke tools with sandbox enforcement (**C6**).

**Function:** `compositional_co_scientist.api.skills.act_skill.act`

**Signature:**
```python
def act(
    tool_name: str,
    arguments: Dict[str, Any],
    allowed_tools: List[str] = None
) -> Dict[str, Any]
```

**Parameters:**
- `tool_name` (str): Tool to invoke
- `arguments` (Dict): Tool arguments
- `allowed_tools` (List[str], optional): Sandbox allowlist

**Returns:**
```python
{
    "result": Any,           # Tool output
    "c6_passed": bool,       # Sandbox check
    "tool_log_id": str       # Audit log ID
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import act

# Permitted tool
result = act(
    tool_name="web_search",
    arguments={"query": "superconductivity"},
    allowed_tools=["web_search", "calculator"]
)

# Blocked tool (C6 violation)
try:
    result = act(
        tool_name="shell_exec",  # Not in allowlist
        arguments={"command": "ls"},
        allowed_tools=["web_search"]
    )
except SandboxViolationError:
    print("Tool blocked by C6 sandbox")
```

**Constraints Enforced:**
- **C6**: Sandbox enforcement for all tool invocations

---

### SYNTHESIZE

Combine candidates into coherent output.

**Function:** `compositional_co_scientist.api.skills.synthesize_skill.synthesize`

**Signature:**
```python
def synthesize(
    candidates: List[Dict],
    synthesis_mode: str = "tension_preserving"
) -> Dict[str, Any]
```

**Parameters:**
- `candidates` (List[Dict]): Candidates to synthesize
- `synthesis_mode` (str): Synthesis strategy
  - `"tension_preserving"`: Maintain conflicting views
  - `"consensus"`: Find common ground
  - `"integrative"`: Merge into unified theory

**Returns:**
```python
{
    "output": str,              # Synthesized output
    "tensions_preserved": List, # Unresolved tensions
    "synthesis_log_id": str     # Audit log ID
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import synthesize

result = synthesize(
    survivors,
    synthesis_mode="tension_preserving"
)

print(f"Synthesis: {result['output']}")
print(f"Unresolved tensions: {result['tensions_preserved']}")
```

---

### MEMORY

Persist and recall state with TTL enforcement (**C5**).

**Function:** `compositional_co_scientist.api.skills.memory_skill.memory`

**Signature:**
```python
def memory(
    operation: str,
    key: str = None,
    value: Any = None,
    ttl_seconds: int = None
) -> Dict[str, Any]
```

**Parameters:**
- `operation` (str): Operation type
  - `"persist"`: Store value
  - `"recall"`: Retrieve value
  - `"delete"`: Remove value
  - `"stats"`: Get memory statistics
- `key` (str, optional): Memory key
- `value` (Any, optional): Value to store
- `ttl_seconds` (int, optional): Time-to-live in seconds

**Returns:**
```python
# For persist
{"success": bool, "key": str}

# For recall
{"value": Any, "ttl_remaining": int}

# For stats
{
    "total_entries": int,
    "expired_entries": int,
    "utilization": float
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import memory

# Persist with TTL
memory("persist", key="hypothesis_1", value={"content": "..."}, ttl_seconds=3600)

# Recall
result = memory("recall", key="hypothesis_1")
print(f"Value: {result['value']}")
print(f"TTL remaining: {result['ttl_remaining']}s")

# Stats
stats = memory("stats")
print(f"Memory utilization: {stats['utilization']:.2%}")
```

**Constraints Enforced:**
- **C5**: TTL-based decay to prevent path dependence

---

### LOG

Record provenance for auditability (**C4**, **C9**).

**Function:** `compositional_co_scientist.api.skills.log_skill.log`

**Signature:**
```python
def log(
    event_type: str,
    details: Dict[str, Any],
    severity: str = "INFO"
) -> Dict[str, Any]
```

**Parameters:**
- `event_type` (str): Type of event
- `details` (Dict): Event details
- `severity` (str): Severity level
  - `"DEBUG"`, `"INFO"`, `"WARNING"`, `"ERROR"`, `"CRITICAL"`

**Returns:**
```python
{
    "log_id": str,           # Unique log entry ID
    "timestamp": str,        # ISO 8601 timestamp
    "appended": bool         # True if successfully logged
}
```

**Example:**
```python
from compositional_co_scientist.api.skills import log

# Log evaluation event
log_result = log(
    event_type="EVALUATE",
    details={
        "candidate_ids": ["abc123"],
        "evaluator_model": "claude-3",
        "scores": {"coherence": 0.8, "novelty": 0.6}
    },
    severity="INFO"
)

print(f"Logged with ID: {log_result['log_id']}")
```

**Constraints Enforced:**
- **C4**: All EVALUATE operations must be logged
- **C9**: Provenance logging for reproducibility

---

## Constraints

### C1: Evaluator Independence

**Module:** `compositional_co_scientist.core.constraints.c1_evaluator_independence`

**Function:** `check_c1_evaluator_independence`

```python
def check_c1_evaluator_independence(
    generator_model: str,
    evaluator_model: str
) -> bool
```

**Returns:** `True` if models are different, `False` otherwise.

---

### C2: Temporal Order

**Module:** `compositional_co_scientist.core.constraints.c2_temporal_order`

**Function:** `validate_c2_transition`

```python
def validate_c2_transition(
    from_stage: str,
    to_stage: str
) -> Dict[str, Any]
```

**Valid Stages:** `FRAME`, `EXPLORE`, `GENERATE`, `EVALUATE`, `SELECT`, `SYNTHESIZE`, `COMPLETE`, `ERROR`

---

### C3: Diversity Quota

**Module:** `compositional_co_scientist.core.constraints.c3_diversity_quota`

**Functions:**
- `check_diversity_quota(candidates, threshold=0.4)` → `bool`
- `generate_anti_canon_prompt(goal)` → `str`

---

### C4: Log Completeness

**Module:** `compositional_co_scientist.core.constraints.c4_log_completeness`

**Functions:**
- `log_evaluate_start(...)` → `str` (returns log ID)
- `log_evaluate_end(log_id, ...)` → `bool`
- `check_log_completeness(log_id)` → `bool`

---

### C5: Memory Decay

**Module:** `compositional_co_scientist.core.constraints.c5_memory_decay`

**Functions:**
- `run_decay_cleanup(db_path, utility_threshold=0.3)` → `Dict`
- `get_memory_stats(db_path)` → `Dict`
- `check_memory_health(db_path)` → `Dict`

---

### C6: Sandbox Enforcement

**Module:** `compositional_co_scientist.core.constraints.c6_sandbox_enforcement`

**Function:** `check_c6_sandbox`

```python
def check_c6_sandbox(
    tool_name: str,
    allowed_tools: List[str]
) -> bool
```

**Returns:** `True` if tool is allowed, `False` otherwise.

---

## Error Handling

All primitives and constraints raise typed exceptions:

| Exception | When Raised |
|-----------|-------------|
| `PrimitiveError` | Base exception for all primitive errors |
| `ConstraintViolationError` | Constraint check failed |
| `SandboxViolationError` | C6: Unauthorized tool access |
| `StageTransitionError` | C2: Invalid stage transition |
| `DiversityQuotaError` | C3: Diversity threshold not met |
| `LogCompletenessError` | C4: Missing log entries |
| `MemoryDecayError` | C5: Memory cleanup failed |

**Example:**
```python
from compositional_co_scientist.core.errors import ConstraintViolationError

try:
    result = evaluate(
        candidates,
        rubric,
        evaluator_model="gpt-4",  # Same as generator!
        generator_model="gpt-4"
    )
except ConstraintViolationError as e:
    print(f"C1 violation: {e}")
```
