# Tutorial 2: Retrieval-Augmented Hypothesis Generation

This tutorial demonstrates how to use the RETRIEVE primitive to ground hypothesis generation in external evidence.

## Learning Objectives

By the end of this tutorial, you will:
- Understand how RETRIEVE reduces hallucination (R4)
- Know how to balance retrieval with novelty (R5: inverted-U relationship)
- Be able to use retrieved context to inform hypothesis generation

## Prerequisites

- Complete Tutorial 1 (Basic Workflow)
- Understand the GENERATE → EVALUATE → SELECT workflow

## The Retrieval-Novelty Tradeoff

Research shows an **inverted-U relationship** between retrieval and novelty:

```
Novelty
  ^
  |         *
  |       *   *
  |     *       *
  |   *           *
  | *               *
  +-------------------> Retrieval Weight
    0    0.5    1.0
```

- **Too little retrieval** (left): Hallucination risk, ignores existing knowledge
- **Too much retrieval** (right): Retrieval dominance, suppresses novel insights
- **Optimal balance** (center): Grounded novelty (~0.3-0.5 retrieval weight)

## Step 1: Setup

```python
from compositional_co_scientist.api.skills import (
    retrieve, generate, evaluate, select, log
)
```

## Step 2: Retrieve External Context

Start by fetching relevant background information:

```python
print("Retrieving background context...")

retrieval_result = retrieve(
    query="telomere shortening cellular senescence aging mechanisms",
    sources=["arxiv", "pubmed", "wikipedia"],
    max_results=10
)

print(f"Retrieved {len(retrieval_result['documents'])} documents:")

for i, doc in enumerate(retrieval_result['documents'][:5], 1):
    print(f"\n{i}. {doc['title']}")
    print(f"   Source: {doc['source']}")
    print(f"   Relevance: {retrieval_result['relevance_scores'][i-1]:.2f}")
    print(f"   Summary: {doc['summary'][:100]}...")
```

**Expected Output:**
```
Retrieving 10 documents:

1. Telomere shortening: A marker of cellular aging
   Source: pubmed
   Relevance: 0.92
   Summary: Telomeres are repetitive nucleotide sequences at chromosome ends that protect...

2. Cellular senescence: A new hallmark of aging
   Source: arxiv
   Relevance: 0.89
   Summary: Senescent cells accumulate with age and contribute to tissue dysfunction...

3. Hallmarks of Aging: An expanding universe
   Source: pubmed
   Relevance: 0.85
   Summary: The hallmarks of aging represent nine cellular and molecular features...

...
```

## Step 3: Generate Grounded Hypotheses

Use retrieved context to inform (but not constrain) generation:

```python
# Build context from retrieved documents
context = "\n\n".join([
    f"Source: {doc['source']}\n{doc['summary']}"
    for doc in retrieval_result['documents'][:5]
])

print("Generating hypotheses with retrieval grounding...")

# Use retrieval-aware generation
result = generate(
    goal="What are the primary drivers of cellular aging?",
    constraints={
        "max_candidates": 5,
        "retrieval_context": context,
        "retrieval_weight": 0.4  # Balance: grounded but not dominated
    },
    temperature=0.7
)

print(f"Generated {len(result['candidates'])} candidates:")

for i, c in enumerate(result['candidates'], 1):
    print(f"\n{i}. {c['content']}")
    print(f"   Grounded in: {c['metadata'].get('sources', 'general knowledge')}")
```

**Expected Output:**
```
Generating hypotheses with retrieval grounding...
Generated 5 candidates:

1. Telomere attrition triggers replicative senescence via p53 activation
   Grounded in: pubmed:Telomere shortening, arxiv:DNA damage response

2. Senescent cell accumulation creates SASP-mediated tissue damage
   Grounded in: pubmed:Hallmarks of Aging, arxiv:Cellular senescence

3. Mitochondrial dysfunction amplifies ROS production in aging cells
   Grounded in: pubmed:Mitochondrial theory of aging

4. Epigenetic alterations disrupt youthful gene expression programs
   Grounded in: arxiv:Epigenetic clock, pubmed:DNA methylation aging

5. Proteostasis collapse enables toxic protein aggregation
   Grounded in: pubmed:Protein homeostasis aging

Diversity score: 0.68
```

## Step 4: Evaluate with Retrieval Awareness

Evaluate candidates considering both novelty and grounding:

```python
print("\nEvaluating candidates...")

# Adjusted rubric that values both grounding and novelty
rubric = {
    "grounding": 0.3,    # Consistency with retrieved evidence
    "novelty": 0.35,     # Novel insights beyond retrieved material
    "coherence": 0.25,   # Internal logical consistency
    "testability": 0.1   # Experimental accessibility
}

eval_result = evaluate(
    candidates=result["candidates"],
    rubric=rubric,
    evaluator_model="claude-3",
    generator_model="gpt-4"
)

scored = eval_result["scored_candidates"]

print("\nEvaluation results (sorted by overall score):")
for c in sorted(scored, key=lambda x: x['score']['overall'], reverse=True):
    print(f"\n{c['content'][:60]}...")
    print(f"  Overall: {c['score']['overall']:.2f}")
    print(f"  Grounding: {c['score']['grounding']:.2f}")
    print(f"  Novelty: {c['score']['novelty']:.2f}")
```

## Step 5: Analyze Retrieval Impact

Compare grounded vs. ungrounded generation:

```python
print("\n=== Retrieval Impact Analysis ===\n")

# Generate WITHOUT retrieval for comparison
ungrounded_result = generate(
    goal="What are the primary drivers of cellular aging?",
    constraints={"max_candidates": 5},
    temperature=0.7  # Same temperature
)

print("Grounded vs. Ungrounded Comparison:")
print(f"  Grounded diversity:   {result['diversity_score']:.2f}")
print(f"  Ungrounded diversity: {ungrounded_result['diversity_score']:.2f}")

# Count novel claims (not directly stated in retrieval)
grounded_novel_count = sum(
    1 for c in result['candidates']
    if c['metadata'].get('novelty_flag', False)
)
ungrounded_novel_count = sum(
    1 for c in ungrounded_result['candidates']
    if c['metadata'].get('novelty_flag', False)
)

print(f"\n  Grounded novel claims:   {grounded_novel_count}/{len(result['candidates'])}")
print(f"  Ungrounded novel claims: {ungrounded_novel_count}/{len(ungrounded_result['candidates'])}")

# Citation density (how much candidates reference retrieved material)
grounded_citation_density = sum(
    len(c['metadata'].get('sources', [])) / len(c['content'].split())
    for c in result['candidates']
) / len(result['candidates'])

print(f"\n  Grounded citation density: {grounded_citation_density:.3f}")
print(f"  (Optimal range: 0.3-0.7, >0.7 indicates retrieval dominance)")
```

**Expected Output:**
```
=== Retrieval Impact Analysis ===

Grounded vs. Ungrounded Comparison:
  Grounded diversity:   0.68
  Ungrounded diversity: 0.71

  Grounded novel claims:   3/5
  Ungrounded novel claims: 4/5

  Grounded citation density: 0.45
  (Optimal range: 0.3-0.7, >0.7 indicates retrieval dominance)
```

## Step 6: Detect and Mitigate Retrieval Dominance

Watch for retrieval dominance anti-pattern:

```python
def check_retrieval_dominance(candidates, retrieval_docs, threshold=0.7):
    """Detect if candidates are overly dominated by retrieval."""
    
    dominance_indicators = []
    
    for candidate in candidates:
        # Check citation density
        sources = candidate['metadata'].get('sources', [])
        citation_density = len(sources) / len(candidate['content'].split())
        
        # Check for novel claims
        has_novel_claim = candidate['metadata'].get('novelty_flag', False)
        
        dominance_indicators.append({
            'candidate': candidate['content'][:50],
            'citation_density': citation_density,
            'has_novel_claim': has_novel_claim,
            'dominance_flag': citation_density > threshold and not has_novel_claim
        })
    
    return dominance_indicators


dominance_check = check_retrieval_dominance(
    result['candidates'],
    retrieval_result['documents']
)

print("\n=== Retrieval Dominance Check ===\n")

dominated_count = sum(1 for d in dominance_check if d['dominance_flag'])

if dominated_count > 0:
    print(f"⚠️  WARNING: {dominated_count}/{len(dominance_check)} candidates show retrieval dominance")
    print("\nDominated candidates:")
    for d in dominance_check:
        if d['dominance_flag']:
            print(f"  - {d['candidate']}... (density: {d['citation_density']:.3f})")
    print("\nMitigation:")
    print("  1. Reduce retrieval_weight to 0.2-0.3")
    print("  2. Use anti-canon generation mode")
    print("  3. Increase temperature to 0.8-0.9")
else:
    print("✓ No retrieval dominance detected")
    print("  Retrieval weight is appropriately balanced")
```

## Step 7: Anti-Canon Generation (Breaking Free from Retrieval)

If retrieval dominance is detected, use anti-canon mode:

```python
from compositional_co_scientist.core.constraints.c3_diversity_quota import (
    generate_anti_canon_prompt
)

print("\n=== Anti-Canon Generation ===\n")

# Generate counter-intuitive hypotheses
anti_canon_prompt = generate_anti_canon_prompt(
    goal="What are the primary drivers of cellular aging?",
    retrieved_context=context
)

print("Anti-canon prompt:")
print(anti_canon_prompt[:500] + "...")

anti_canon_result = generate(
    goal=anti_canon_prompt,  # Use anti-canon prompt instead of regular goal
    constraints={"max_candidates": 3},
    temperature=0.9  # Higher temperature for anti-canon
)

print(f"\nAnti-canon candidates:")
for i, c in enumerate(anti_canon_result['candidates'], 1):
    print(f"\n{i}. {c['content']}")
    print(f"   Counter-intuitive aspect: {c['metadata'].get('anti_canon_rationale', 'N/A')}")
```

**Expected Output:**
```
=== Anti-Canon Generation ===

Anti-canon prompt:
Generate hypotheses that CONTRADICT the following established views:

[Retrieved context summarizing mainstream theories]

Instructions:
1. Propose mechanisms that challenge conventional wisdom
2. Consider that telomere shortening may be protective, not damaging
3. Explore whether senescent cells serve beneficial functions
...

Anti-canon candidates:

1. Telomere shortening is a tumor-suppression mechanism, not an aging driver
   Counter-intuitive aspect: Reframes "damage" as protective adaptation

2. Senescent cells promote tissue repair, not degeneration
   Counter-intuitive aspect: SASP may be regenerative signal, not inflammatory damage

3. Mitochondrial ROS signaling is pro-longevity at moderate levels
   Counter-intuitive aspect: Hormesis vs. damage accumulation
```

## Complete Example: Retrieval-Aware Workflow

```python
def retrieval_augmented_generation(research_goal: str, retrieval_weight: float = 0.4):
    """Complete retrieval-augmented hypothesis generation workflow."""
    
    # Step 1: Retrieve context
    retrieval = retrieve(
        query=research_goal,
        sources=["arxiv", "pubmed"],
        max_results=10
    )
    
    # Step 2: Build context string
    context = "\n\n".join([
        f"Source: {doc['source']}\n{doc['summary']}"
        for doc in retrieval['documents'][:5]
    ])
    
    # Step 3: Generate with retrieval grounding
    result = generate(
        goal=research_goal,
        constraints={
            "max_candidates": 5,
            "retrieval_context": context,
            "retrieval_weight": retrieval_weight
        },
        temperature=0.7
    )
    
    # Step 4: Check for retrieval dominance
    dominance_check = check_retrieval_dominance(result['candidates'], retrieval['documents'])
    dominated = sum(1 for d in dominance_check if d['dominance_flag'])
    
    # Step 5: If dominated, regenerate with anti-canon
    if dominated > 0:
        print(f"Retrieval dominance detected ({dominated}/5), regenerating...")
        anti_canon = generate_anti_canon_prompt(research_goal, context)
        anti_result = generate(
            goal=anti_canon,
            constraints={"max_candidates": 2},
            temperature=0.9
        )
        result['candidates'].extend(anti_result['candidates'])
    
    # Step 6: Evaluate
    eval_result = evaluate(
        candidates=result['candidates'],
        rubric={"grounding": 0.3, "novelty": 0.35, "coherence": 0.25, "testability": 0.1},
        evaluator_model="claude-3",
        generator_model="gpt-4"
    )
    
    # Step 7: Select
    select_result = select(
        scored_candidates=eval_result['scored_candidates'],
        diversity_quota=0.4
    )
    
    return {
        "retrieved_documents": retrieval['documents'],
        "generated_candidates": result['candidates'],
        "scored_candidates": eval_result['scored_candidates'],
        "survivors": select_result['survivors'],
        "retrieval_dominance_detected": dominated > 0
    }


if __name__ == "__main__":
    result = retrieval_augmented_generation(
        "What are the mechanisms of insulin resistance in type 2 diabetes?",
        retrieval_weight=0.4
    )
    
    print(f"\nRetrieved {len(result['retrieved_documents'])} documents")
    print(f"Generated {len(result['generated_candidates'])} candidates")
    print(f"Selected {len(result['survivors'])} survivors")
    print(f"Retrieval dominance: {'Yes (corrected)' if result['retrieval_dominance_detected'] else 'No'}")
```

## Key Takeaways

1. **Retrieval reduces hallucination** (R4): Ground hypotheses in existing evidence
2. **Retrieval suppresses novelty** (R5): Too much retrieval kills creativity
3. **Inverted-U relationship**: Optimal retrieval weight is ~0.3-0.5
4. **Detect retrieval dominance**: Citation density >0.7 indicates over-reliance
5. **Anti-canon generation**: Counter-intuitive prompts break retrieval dominance

## Next Steps

- **Tutorial 3**: Using CRITIQUE for defect identification
- **Tutorial 4**: Multi-agent coordination patterns
- **Tutorial 5**: MEMORY and LOG for stateful workflows

## Troubleshooting

### Retrieval Dominance

**Symptoms:**
- Citation density >0.7
- Few novel claims
- Candidates mostly paraphrase retrieved material

**Solutions:**
1. Reduce `retrieval_weight` to 0.2-0.3
2. Use `generate_anti_canon_prompt()`
3. Increase temperature to 0.8-0.9
4. Force anti-canon generation mode

### Low Grounding Score

**Symptoms:**
- Evaluation grounding score <0.3
- Candidates ignore retrieved evidence

**Solutions:**
1. Increase `retrieval_weight` to 0.5-0.6
2. Add explicit grounding requirement to prompt
3. Include retrieved sources in evaluation rubric

### No Retrieved Documents

**Symptoms:**
- Empty retrieval results
- Low relevance scores

**Solutions:**
1. Broaden search query
2. Add more sources
3. Check source availability (some APIs may be rate-limited)
