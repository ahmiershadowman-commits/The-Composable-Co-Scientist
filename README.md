# The Compositional Co-Scientist

Evidence-anchored agentic scaffolding for scientific reasoning.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from compositional_co_scientist.core.primitives import generate, evaluate, select

# Generate candidate hypotheses
candidates = generate(
    goal="What causes superconductivity?",
    constraints={"max_candidates": 5},
    temperature=0.7
)

# Evaluate candidates
scored = evaluate(
    candidates=candidates,
    rubric={"coherence": 0.5, "novelty": 0.5},
    evaluator_model="claude-3"  # Must differ from generator
)

# Select survivors with diversity quota
survivors = select(scored, diversity_quota=0.4)
```

## Primitives

| Primitive | Function |
|-----------|----------|
| GENERATE | Generate candidate hypotheses |
| EVALUATE | Score candidates against rubric |
| CRITIQUE | Identify defects |
| SELECT | Choose survivors with diversity quota |
| RETRIEVE | Fetch external context |
| ACT | Invoke tools with sandbox |
| SYNTHESIZE | Combine into coherent output |
| MEMORY | Persist/recall state |
| LOG | Record provenance |

## Constraints

| Constraint | Description |
|------------|-------------|
| C1 | EVALUATE ≠ GENERATE (different models) |
| C2 | GENERATE → EVALUATE → SELECT (temporal order) |
| C3 | DIVERSITY quota at SELECT |
| C4 | LOG all EVALUATE operations |
| C5 | MEMORY decay policy |
| C6 | ACT sandbox enforcement |

## Documentation

See `docs/` for API reference, user guide, and tutorials.

## License

MIT
