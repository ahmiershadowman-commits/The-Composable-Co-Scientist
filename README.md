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
