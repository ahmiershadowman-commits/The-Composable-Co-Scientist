# The Compositional Co-Scientist

**Version:** 0.1.0 - Research Prototype

Evidence-anchored agentic scaffolding for scientific reasoning.

## Status

**Implemented & Enforced:**
- ✅ C1: EVALUATE ≠ GENERATE (different models)
- ✅ C2: GENERATE → EVALUATE → SELECT (temporal order)
- ✅ C6: ACT sandbox enforcement

**Partial Implementation:**
- 🟡 C3: Diversity quota at SELECT (quota enforced, auto-regenerate pending)
- 🟡 C4: LOG all EVALUATE operations (logging works, auto-enforcement pending)
- 🟡 C5: MEMORY decay policy (TTL exists, cleanup cron pending)

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from compositional_co_scientist.api.skills import generate, evaluate, select

# Generate candidate hypotheses
candidates = generate(
    goal="What causes superconductivity?",
    constraints={"max_candidates": 5},
    temperature=0.7
)

# Evaluate candidates (C1: must use different model than generator)
scored = evaluate(
    candidates=candidates,
    rubric={"coherence": 0.5, "novelty": 0.5},
    evaluator_model="claude-3"  # Must differ from generator
)

# Select survivors with diversity quota
survivors = select(scored, diversity_quota=0.4)
```

## Primitives

| Primitive | Function | Status |
|-----------|----------|--------|
| GENERATE | Generate candidate hypotheses | ✅ Implemented |
| EVALUATE | Score candidates against rubric | ✅ Implemented |
| CRITIQUE | Identify defects | ✅ Implemented |
| SELECT | Choose survivors with diversity quota | ✅ Implemented |
| RETRIEVE | Fetch external context | ✅ Implemented |
| ACT | Invoke tools with sandbox | ✅ Implemented |
| SYNTHESIZE | Combine into coherent output | ✅ Implemented |
| MEMORY | Persist/recall state | ✅ Implemented |
| LOG | Record provenance | ✅ Implemented |

## Constraints

| Constraint | Description | Status |
|------------|-------------|--------|
| C1 | EVALUATE ≠ GENERATE (different models) | ✅ Enforced |
| C2 | GENERATE → EVALUATE → SELECT (temporal order) | ✅ Enforced |
| C3 | DIVERSITY quota at SELECT | 🟡 Partial |
| C4 | LOG all EVALUATE operations | 🟡 Partial |
| C5 | MEMORY decay policy | 🟡 Partial |
| C6 | ACT sandbox enforcement | ✅ Enforced |

## Testing

```bash
pytest --cov=compositional_co_scientist --cov-branch --cov-fail-under=80
```

Current: 57 tests passing, 91%+ coverage

## License

MIT - see LICENSE file.
