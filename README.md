# The Compositional Co-Scientist

**Version:** 0.2.0 - Research Prototype

Evidence-anchored agentic scaffolding for scientific reasoning.

## Status

**Implemented & Enforced:**
- ✅ C1: EVALUATE ≠ GENERATE (different models)
- ✅ C2: GENERATE → EVALUATE → SELECT (temporal order)
- ✅ C3: Diversity quota at SELECT (with auto-regenerate)
- ✅ C4: LOG all EVALUATE operations (audit interceptor)
- ✅ C5: MEMORY decay policy (cleanup + auto-cron scheduler)
- ✅ C6: ACT sandbox enforcement

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
| C3 | DIVERSITY quota at SELECT | ✅ Enforced + auto-regenerate |
| C4 | LOG all EVALUATE operations | ✅ Enforced (audit interceptor) |
| C5 | MEMORY decay policy | ✅ Cleanup + auto-cron scheduler |
| C6 | ACT sandbox enforcement | ✅ Enforced |

## Testing

```bash
pytest --cov=compositional_co_scientist --cov-branch --cov-fail-under=80
```

**Current Metrics:**
- **80 tests** (77 passed, 3 skipped)
- **87.61% branch coverage** (exceeds 80% target)

## Documentation

- **Getting Started**: [`docs/user-guide/getting-started.md`](docs/user-guide/getting-started.md)
- **API Reference**: [`docs/user-guide/api-reference.md`](docs/user-guide/api-reference.md)
- **Tutorials**: [`docs/tutorials/`](docs/tutorials/)
  - Tutorial 1: Basic Hypothesis Generation Workflow
  - Tutorial 2: Retrieval-Augmented Generation

## License

MIT - see LICENSE file.
