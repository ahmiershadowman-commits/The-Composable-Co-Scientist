# Getting Started with the Compositional Co-Scientist

This guide will help you get started with the Compositional Co-Scientist plugin for agentic scientific reasoning.

## What is the Compositional Co-Scientist?

The Compositional Co-Scientist is an **evidence-anchored agentic scaffolding system** that implements structured workflows for scientific hypothesis generation and evaluation. It translates research on AI co-scientist architectures into a production-ready plugin for LLM hosts (Claude Code, Qwen Code, Gemini CLI).

## Core Concepts

### 9 Primitive Operations

The system is built on 9 irreducible primitive operations:

| Primitive | Function | When to Use |
|-----------|----------|-------------|
| **GENERATE** | Produce candidate hypotheses | Starting exploration of a research question |
| **EVALUATE** | Assign quality scores | Assessing candidate quality against rubric |
| **CRITIQUE** | Identify defects | Finding weaknesses in candidates |
| **SELECT** | Choose survivors | Deciding which candidates to keep |
| **RETRIEVE** | Fetch external context | Needing background information |
| **ACT** | Invoke tools | Executing external actions |
| **SYNTHESIZE** | Combine into coherence | Merging multiple candidates |
| **MEMORY** | Persist/recall state | Saving or retrieving information |
| **LOG** | Record provenance | Tracking operations for auditability |

### 6 Non-Negotiable Constraints

These constraints are **evidence-anchored** and enforced by the system:

| Constraint | Description | Evidence |
|------------|-------------|----------|
| **C1** | EVALUATE ≠ GENERATE (different models) | Huang et al. (ICLR 2024): 10-25% score inflation if violated |
| **C2** | GENERATE → EVALUATE → SELECT (temporal order) | Tree-of-Thoughts: 74% vs 4% on Game of 24 |
| **C3** | Diversity quota at SELECT | Prevents premature convergence |
| **C4** | LOG all EVALUATE operations | W3C PROV standards compliance |
| **C5** | MEMORY decay policy | Prevents path dependence |
| **C6** | ACT sandbox enforcement | OWASP LLM Top 10 security |

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/the-composable-co-scientist.git
cd "The Composable Co-Scientist"

# Install in editable mode
pip install -e .

# Install with test dependencies (optional)
pip install -e ".[test]"
```

### Verify Installation

```bash
# Run tests to verify installation
pytest --cov=compositional_co_scientist --cov-branch --cov-fail-under=80
```

Expected output: 70+ tests passing, 80%+ coverage.

## Quick Start

### Basic Workflow

Here's a minimal example of the core workflow:

```python
from compositional_co_scientist.api.skills import (
    generate, evaluate, select, synthesize
)

# Step 1: Generate candidate hypotheses
result = generate(
    goal="What causes superconductivity in high-temperature materials?",
    constraints={"max_candidates": 5},
    temperature=0.7
)
candidates = result["candidates"]
print(f"Generated {len(candidates)} candidates")

# Step 2: Evaluate candidates (C1: use different model than generator)
eval_result = evaluate(
    candidates=candidates,
    rubric={"coherence": 0.5, "novelty": 0.5},
    evaluator_model="claude-3"  # Must differ from generator model
)
scored_candidates = eval_result["scored_candidates"]

# Step 3: Select survivors with diversity quota
select_result = select(
    scored_candidates,
    diversity_quota=0.4  # Minimum novelty score
)
survivors = select_result["survivors"]

# Step 4: Synthesize into coherent output
synth_result = synthesize(
    survivors,
    synthesis_mode="tension_preserving"
)
print(f"Synthesized output: {synth_result['output']}")
```

### Using Commands (Claude Code / Qwen Code)

If your host supports slash commands:

```
/generate What causes superconductivity?
/evaluate <candidate-id> --rubric coherence=0.5,novelty=0.5
/synthesize <candidate-id-1> <candidate-id-2>
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `CO_SCIENTIST_DATA` | Data directory for databases | `~/.composable_co_scientist` |
| `CO_SCIENTIST_LOG_LEVEL` | Logging verbosity | `INFO` |

### Database Files

The system creates three SQLite databases:

| Database | Purpose | Location |
|----------|---------|----------|
| `candidates.db` | Candidate storage | `$CO_SCIENTIST_DATA/` |
| `memory.db` | MEMORY primitive state | `$CO_SCIENTIST_DATA/` |
| `audit.db` | LOG primitive audit trail | `$CO_SCIENTIST_DATA/` |

## Next Steps

- **Tutorials**: See [`docs/tutorials/`](../tutorials/) for step-by-step workflows
- **API Reference**: See [`docs/api-reference/`](../api-reference/) for detailed API documentation
- **Research**: See [`docs/research/`](../research/) for evidence backing the design

## Getting Help

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions on GitHub Discussions
- **Documentation**: Browse [`docs/`](../) for guides and references
