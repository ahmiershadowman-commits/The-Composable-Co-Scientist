# Tutorial 1: Basic Hypothesis Generation Workflow

This tutorial walks you through a complete hypothesis generation workflow using the Compositional Co-Scientist.

## Learning Objectives

By the end of this tutorial, you will:
- Understand the basic GENERATE → EVALUATE → SELECT → SYNTHESIZE workflow
- Know how to enforce constraints C1, C2, and C3
- Be able to generate and evaluate candidate hypotheses

## Prerequisites

- Python 3.10+ installed
- Compositional Co-Scientist package installed (`pip install -e .`)

## Step 1: Setup

```python
from compositional_co_scientist.api.skills import (
    generate, evaluate, select, synthesize, log
)
from compositional_co_scientist.core.errors import ConstraintViolationError
```

## Step 2: Define Your Research Goal

Start with a clear, focused research question:

```python
research_goal = "What are the biological mechanisms that limit human lifespan?"
```

## Step 3: Generate Candidate Hypotheses

Use the GENERATE primitive to produce diverse candidates:

```python
print("Generating candidate hypotheses...")

result = generate(
    goal=research_goal,
    constraints={"max_candidates": 5},
    temperature=0.8  # Higher temperature for more diversity
)

candidates = result["candidates"]
print(f"Generated {len(candidates)} candidates:")

for i, c in enumerate(candidates, 1):
    print(f"\n{i}. {c['content']}")
    print(f"   Rationale: {c['metadata']['rationale']}")

print(f"\nDiversity score: {result['diversity_score']:.2f}")
```

**Expected Output:**
```
Generating candidate hypotheses...
Generated 5 candidates:

1. Telomere shortening limits cellular replication
   Rationale: Telomeres protect chromosome ends; shortening triggers senescence

2. Accumulation of senescent cells drives aging
   Rationale: Senescent cells secrete inflammatory factors damaging tissues

3. Mitochondrial DNA mutations reduce energy production
   Rationale: mtDNA accumulates damage, impairing ATP synthesis

4. Protein homeostasis failure leads to aggregation
   Rationale: Chaperone decline allows misfolded protein accumulation

5. Epigenetic drift alters gene expression patterns
   Rationale: Methylation patterns change with age, disrupting regulation

Diversity score: 0.72
```

## Step 4: Evaluate Candidates (C1 Enforcement)

Evaluate candidates using a **different model** than generation (C1 constraint):

```python
print("\nEvaluating candidates...")

# Define evaluation rubric
rubric = {
    "coherence": 0.4,    # Internal logical consistency
    "novelty": 0.3,      # Novelty relative to existing theories
    "testability": 0.3   # Falsifiability and experimental accessibility
}

try:
    eval_result = evaluate(
        candidates=candidates,
        rubric=rubric,
        evaluator_model="claude-3",      # Must differ from generator!
        generator_model="gpt-4"          # Track for C1 enforcement
    )
    
    print(f"C1 constraint passed: {eval_result['c1_passed']}")
    print(f"Evaluation log ID: {eval_result['evaluation_log_id']}")
    
    scored = eval_result["scored_candidates"]
    
    print("\nEvaluation results:")
    for c in scored:
        print(f"\n{c['content'][:50]}...")
        print(f"  Overall score: {c['score']['overall']:.2f}")
        print(f"  Coherence: {c['score']['coherence']:.2f}")
        print(f"  Novelty: {c['score']['novelty']:.2f}")
        print(f"  Testability: {c['score']['testability']:.2f}")
        
except ConstraintViolationError as e:
    print(f"Constraint violation: {e}")
    print("Make sure evaluator_model differs from generator_model")
```

**Expected Output:**
```
Evaluating candidates...
C1 constraint passed: True
Evaluation log ID: log_abc123

Evaluation results:

Telomere shortening limits cellular replication...
  Overall score: 0.82
  Coherence: 0.90
  Novelty: 0.65
  Testability: 0.90

Accumulation of senescent cells drives aging...
  Overall score: 0.78
  Coherence: 0.85
  Novelty: 0.70
  Testability: 0.80

...
```

## Step 5: Select Survivors (C3 Enforcement)

Select candidates that meet the diversity quota:

```python
print("\nSelecting survivors with diversity quota...")

select_result = select(
    scored_candidates=scored,
    diversity_quota=0.4,  # Minimum novelty score
    max_survivors=3
)

print(f"C3 diversity quota passed: {select_result['c3_passed']}")
print(f"Selected {len(select_result['survivors'])} survivors:")

for i, s in enumerate(select_result['survivors'], 1):
    print(f"  {i}. {s['content'][:60]}...")

if select_result['rejected']:
    print(f"\nRejected {len(select_result['rejected'])} candidates:")
    for r in select_result['rejected']:
        print(f"  - {r['content'][:50]}... (score: {r['score']['overall']:.2f})")
```

**Expected Output:**
```
Selecting survivors with diversity quota...
C3 diversity quota passed: True
Selected 3 survivors:
  1. Telomere shortening limits cellular replication...
  2. Accumulation of senescent cells drives aging...
  3. Mitochondrial DNA mutations reduce energy production...

Rejected 2 candidates:
  - Protein homeostasis failure leads to aggregation... (score: 0.65)
  - Epigenetic drift alters gene expression patterns... (score: 0.61)
```

## Step 6: Synthesize Output

Combine survivors into a coherent synthesis:

```python
print("\nSynthesizing final output...")

synth_result = synthesize(
    candidates=select_result['survivors'],
    synthesis_mode="tension_preserving"  # Keep conflicting views
)

print("\n=== SYNTHESIS ===")
print(synth_result['output'])

if synth_result['tensions_preserved']:
    print("\n=== UNRESOLVED TENSIONS ===")
    for tension in synth_result['tensions_preserved']:
        print(f"  - {tension}")
```

**Expected Output:**
```
Synthesizing final output...

=== SYNTHESIS ===
Three major mechanisms limit human lifespan:

1. **Cellular replication limits** (telomere shortening)
2. **Tissue-level damage** (senescent cell accumulation)  
3. **Metabolic decline** (mitochondrial dysfunction)

These mechanisms may operate in cascade: telomere shortening triggers
senescence, which increases metabolic stress, accelerating mitochondrial
damage. However, the relative contribution of each mechanism remains
debated...

=== UNRESOLVED TENSIONS ===
  - Whether telomere shortening is primary cause or downstream marker
  - Whether senescent cells drive aging or are protective response
```

## Step 7: Log the Workflow (C4 Enforcement)

Record the complete workflow for auditability:

```python
print("\nLogging workflow...")

# Log the complete workflow
workflow_log = log(
    event_type="WORKFLOW_COMPLETE",
    details={
        "goal": research_goal,
        "candidates_generated": len(candidates),
        "candidates_evaluated": len(scored),
        "candidates_selected": len(select_result['survivors']),
        "c1_passed": eval_result['c1_passed'],
        "c3_passed": select_result['c3_passed'],
        "evaluation_log_id": eval_result['evaluation_log_id']
    },
    severity="INFO"
)

print(f"Workflow logged with ID: {workflow_log['log_id']}")
```

## Complete Example

Here's the complete workflow in one script:

```python
from compositional_co_scientist.api.skills import (
    generate, evaluate, select, synthesize, log
)

def run_hypothesis_generation(research_goal: str):
    """Complete hypothesis generation workflow."""
    
    # Step 1: Generate
    gen_result = generate(
        goal=research_goal,
        constraints={"max_candidates": 5},
        temperature=0.8
    )
    
    # Step 2: Evaluate (C1: different model)
    eval_result = evaluate(
        candidates=gen_result["candidates"],
        rubric={"coherence": 0.4, "novelty": 0.3, "testability": 0.3},
        evaluator_model="claude-3",
        generator_model="gpt-4"
    )
    
    # Step 3: Select (C3: diversity quota)
    select_result = select(
        scored_candidates=eval_result["scored_candidates"],
        diversity_quota=0.4,
        max_survivors=3
    )
    
    # Step 4: Synthesize
    synth_result = synthesize(
        candidates=select_result["survivors"],
        synthesis_mode="tension_preserving"
    )
    
    # Step 5: Log (C4: auditability)
    log_result = log(
        event_type="WORKFLOW_COMPLETE",
        details={
            "goal": research_goal,
            "survivors": len(select_result["survivors"]),
            "c1_passed": eval_result["c1_passed"],
            "c3_passed": select_result["c3_passed"]
        }
    )
    
    return {
        "synthesis": synth_result["output"],
        "tensions": synth_result["tensions_preserved"],
        "log_id": log_result["log_id"]
    }


if __name__ == "__main__":
    result = run_hypothesis_generation(
        "What are the biological mechanisms that limit human lifespan?"
    )
    print(f"\nFinal synthesis:\n{result['synthesis']}")
```

## Key Takeaways

1. **GENERATE → EVALUATE → SELECT → SYNTHESIZE** is the core workflow
2. **C1 (Evaluator Independence)**: Always use different models for generation and evaluation
3. **C3 (Diversity Quota)**: Set minimum novelty threshold to prevent premature convergence
4. **C4 (Log Completeness)**: Log all evaluation operations for auditability
5. **Temperature matters**: Higher temperature (0.7-0.9) increases diversity

## Next Steps

- **Tutorial 2**: Using RETRIEVE for external grounding
- **Tutorial 3**: Advanced CRITIQUE workflows
- **Tutorial 4**: Multi-agent coordination patterns

## Troubleshooting

### C1 Constraint Failed

**Error:** `ConstraintViolationError: C1 violation - evaluator must differ from generator`

**Solution:** Ensure `evaluator_model` and `generator_model` are different model families (e.g., Claude vs. GPT).

### C3 Diversity Quota Not Met

**Warning:** `C3 diversity quota not met (0.35 < 0.40)`

**Solutions:**
1. Increase generation temperature
2. Increase `max_candidates` in generation
3. Lower `diversity_quota` threshold (not recommended below 0.3)

### Low Diversity Score

**Issue:** Generated candidates are too similar

**Solutions:**
1. Increase temperature to 0.8-0.9
2. Add explicit diversity constraints
3. Use `generate_anti_canon_prompt()` for counter-intuitive candidates
