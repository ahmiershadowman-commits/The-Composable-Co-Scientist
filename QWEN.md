# QWEN.md — The Composable Co-Scientist Project Context

**Directory:** `C:\Users\Ashbi\OneDrive\Documents\GitHub\The Composable Co-Scientist\`

**Profile:** Research repository for agentic AI scaffolding frameworks and plugin architectures for scientific hypothesis generation.

**Last Updated:** 2026-03-23 (Evidence-Anchored Dependency Graph)

---

## Overview

This repository contains theoretical frameworks, design documents, and a skills package for building **agentic scaffolding systems** — AI architectures that support scientific reasoning through structured multi-agent workflows, ontological engineering, and abductive hypothesis generation.

The project translates research on AI co-scientist architectures into implementable plugin systems for LLM hosts (Claude Code, Qwen Code, Gemini, Codex, OpenCode).

**Current Status:** Completed evidence-anchored dependency graph with explicit uncertainty quantification. Ready for Phase 1 implementation (MEMORY + LOG substrate).

---

## Repository Structure

| Directory/File | Purpose |
|----------------|---------|
| `docs/research/` | Core research papers and design documents (12 files: 7 Markdown, 4 TXT, 1 PDF, 1 DOCX) |
| `docs/superpowers/specs/` | Approved design specifications (evidence-anchored dependency graph) |
| `skills/universal-plugin-skill/` | Plugin architecture specification with `SKILL.md` |
| `.gitattributes` | Git LFS/binary configuration |

---

## Key Research Documents

### Core Framework Papers

| Document | Focus | Key Contributions |
|----------|-------|-------------------|
| **The Composable Co-Scientist** (244 lines) | Plugin-first blueprint for dialectical ontology engineering | Mechanism taxonomy (5 families), implementation feasibility classification (Class A/B/C), architectural recommendations for modular theory-forging engines |
| **Deconstructing Agentic Science** (181 lines) | Dependency graph of primitives, stages, and ontologies | 12 ontological families, evidence stratification (Recurrent/Emerging/Speculative), primitive operation families with failure mode analysis |
| **Architecting Abduction** (73 lines) | Comparative analysis of hypothesis generation frameworks | Symbolic vs neuro-symbolic paradigms, single-agent vs multi-agent tradeoffs, domain-specific benchmarks (scientific/medical/narrative) |
| **Agentic Scaffolding Skills Package** | Complete `/skills` repository skeleton | 6 Python agent modules, 6 slash-commands, I/O schemas, marketplace manifest (YAML), dependency graph (Mermaid) |

### Supporting Documents

| Document | Type | Content |
|----------|------|---------|
| `Agentic Scaffolding → /Skills Plugin Mapping` | Technical specification | 8 Class A / 6 Class B / 5 Class C ontological family mappings, 7 irreducible primitives, 8-stage gated workflow |
| `GPT-Agentic-Scientists.md` | Literature review | Survey of existing agentic scientist systems |
| `Scaffolding-for-Science-Agent.md` | Design notes | Scaffolding patterns for scientific reasoning |
| `Abduction Scaffolding.txt` | Notes | Abductive reasoning frameworks |
| `Science Agent Scaffolding.txt` | Notes | Stage-based agent design |
| `Gem-Thought-Trace-AI-Scientist.txt` | Notes | Thought tracing for scientific agents |
| `Agentic_Scaffolding_Research_Map.pdf` | Visual map | Dependency graph visualization |
| `Build Propositon.docx` | Business document | Value proposition (binary format) |

---

## Key Concepts (Updated 2026-03-23)

### Ontological Families (8 Evidence-Anchored)

| Family | Primitives | Evidence Status | Confidence |
|--------|------------|-----------------|------------|
| **Generation** | GENERATE | Validated by QD literature | HIGH |
| **Evaluation** | EVALUATE | Validated by Huang et al. (ICLR 2024) | HIGH |
| **Critique** | CRITIQUE | Inferred (distinct failure mode) | MEDIUM-HIGH |
| **Selection** | SELECT | Validated by Tree-of-Thoughts | HIGH |
| **Retrieval** | RETRIEVE | Validated by RAG literature | HIGH |
| **Action** | ACT | Validated by OWASP LLM Top 10 | HIGH |
| **Integration** | SYNTHESIZE | Inferred (dialectical ontology) | MEDIUM |
| **Substrate** | MEMORY, LOG | Validated by MemGPT, W3C PROV | MEDIUM-HIGH |

**Note:** Prior corpus taxonomies (19 families, 4 meta-families) were re-evaluated from first principles. 8 families is the evidence-anchored count—4 loses implementation-relevant distinctions; 19 over-specifies.

### Primitive Operations (9 Irreducible)

| ID | Primitive | Function | Failure Mode | Confidence |
|----|-----------|----------|--------------|------------|
| **P1** | **GENERATE** | Produce candidates | Mode collapse | HIGH |
| **P2** | **EVALUATE** | Assign quality scores | Evaluator collapse (calibration) | HIGH |
| **P3** | **CRITIQUE** | Identify defects | Coverage error | MEDIUM-HIGH |
| **P4** | **SELECT** | Choose survivors | Premature convergence | HIGH |
| **P5** | **RETRIEVE** | Fetch external context | Retrieval dominance | HIGH |
| **P6** | **ACT** | Invoke tools | Tool-output credulity | HIGH |
| **P7** | **SYNTHESIZE** | Combine into coherence | Averaging to mediocrity | MEDIUM |
| **P8** | **MEMORY** | Persist/recall state | Path dependence, bloat | HIGH |
| **P9** | **LOG** | Record provenance | Invisible failures | MEDIUM |

**Test for primitiveness:** Each has (1) distinct failure mode, (2) distinct constraints, (3) distinct optimization target.

**Composite operations (not primitives):** branch=GENERATE×N, diversify=GENERATE+novelty_constraint, persist/recall=MEMORY read/write, halt=SELECT(stop), aggregate=SYNTHESIZE, formalize=SYNTHESIZE+constraints, checkpoint=MEMORY+LOG.

### Validated Relationships (Non-Negotiable Constraints)

| ID | Relationship | Evidence | Effect Size |
|----|--------------|----------|-------------|
| **R1** | EVALUATE ≠ GENERATE (different models) | Huang et al., Kambhampati et al. | 10-25% score inflation if violated |
| **R2** | GENERATE → EVALUATE → SELECT (order) | Tree-of-Thoughts, FunSearch | 74% vs 4% on Game of 24 |
| **R4** | RETRIEVE reduces hallucination | RAG literature, GraphRAG | 3-5× reduction |
| **R5** | RETRIEVE suppresses novelty | Retrieval dominance pattern | Inverted-U relationship |
| **R6** | Independent multi-agent amplifies errors | Google DeepMind (arXiv:2512.08296) | 17.2× amplification |
| **R7** | Centralized coordination reduces error | Same study | 4.4× (vs. 17.2× independent) |
| **R8** | Compound reliability: 95%^N degrades | Mathematical derivation | 10 steps=60%; 50 steps=7.7% |
| **R9** | Provenance logging enables reproducibility | W3C PROV standard | N/A (standards compliance) |
| **R10** | Tool use expands attack surface | OWASP LLM Top 10 | N/A (security standard) |

### Open Questions (Require Empirical Study)

| ID | Question | Status |
|----|----------|--------|
| **Q1** | Does multi-agent debate improve truth-tracking? | CONTESTED (Du et al. yes; Wynn et al. no) |
| **Q2** | Is developmental staging necessary? | UNTESTED in scientific agents |
| **Q3** | What are operational stage-transition criteria? | UNSPECIFIED (0/9 docs provide thresholds) |
| **Q4** | Can novelty be reliably assessed? | FAILED (AI Scientist v1 failed) |
| **Q5** | Is 8-stage workflow optimal? | UNTESTED (no ablation studies) |
| **Q6** | Does graph structure improve reasoning? | UNPROVEN (correlational only) |
| **Q7** | What is "different enough" for cross-family verification? | UNSPECIFIED |

```
STAGE 0: FRAME      → Goal decomposition, ambiguity check
STAGE 1: EXPLORE    → Divergent generation, diversity quotas
STAGE 2: INCUBATE   → Protected development, external feedback
STAGE 3: EVALUATE   → Critical filtering, cross-verification
STAGE 4: SYNTHESIZE → Integration of surviving candidates
STAGE 5: FORMALIZE  → Crystallization (optional formal proof)
STAGE 6: BOUNDARY   → Consequence tracing, risk assessment
STAGE 7: HANDOFF    → Provenance logging, human escalation
```

### Anti-Patterns (10 Identified)

| Anti-Pattern | Detection | Mitigation |
|--------------|-----------|------------|
| Premature convergence | <3 candidates at Stage 3, diversity <0.4 | Loop to Stage 1 with diversity quota |
| Retrieval dominance | Citation density >0.7, novel claims <0.2 | Force anti-canon generation mode |
| Evaluator collapse | Generator/evaluator same model family | Require cross-family verification |
| Stage collapse | Gate criteria skipped, wrong primitives | Block transition, enforce gate |
| Hidden memory path dependence | Early influence score >0.7 | Force consolidation and decay |
| Premature formalization | Formalization before Stage 5 | Block, flag as premature |
| Invisible failure accumulation | Missing failure log entries | Require compound reliability calculation |
| Cargo-cult multi-agentism | Multiple agents, same model, no diversity | Collapse to single agent with role prompts |
| Verification theater | Verification without external source | Downgrade confidence, flag unverified |
| Untracked uncertainty | Missing confidence annotations | Require calibration before handoff |

---

## Plugin Architecture (Evidence-Anchored)

### Build Order (Dependency-Driven)

```
Phase 1: MEMORY + LOG (substrate)
  └─ Test: persist/recall, append-only log, TTL enforcement

Phase 2: GENERATE + RETRIEVE (input layer)
  └─ Test: diversity metrics, retrieval relevance

Phase 3: EVALUATE + CRITIQUE (judgment layer)
  └─ Test: cross-family verification, calibration

Phase 4: SELECT (decision layer)
  └─ Test: diversity quota enforcement

Phase 5: SYNTHESIZE (output layer)
  └─ Test: tension preservation vs. smoothing

Phase 6: ACT (tool layer)
  └─ Test: sandbox enforcement, error handling
```

### Non-Negotiable Constraints (Must Enforce)

| Constraint | Enforcement | Consequence of Violation |
|------------|-------------|-------------------------|
| EVALUATE ≠ GENERATE (different models) | Architecture-level separation | 10-25% score inflation → garbage selection |
| GENERATE → EVALUATE → SELECT (temporal order) | Workflow engine | Premature convergence → local optima |
| DIVERSITY quota at SELECT | Minimum novelty score | Loss of novel candidates |
| LOG all EVALUATE operations | Append-only log, required field | Can't debug calibration |
| MEMORY decay policy | TTL, utility scoring | Path dependence → early states dominate |
| ACT sandbox enforcement | Permission manifest, allowlist | Security vulnerabilities |

---

## Usage Patterns

### When to Reference This Repository

- Designing multi-agent systems for scientific reasoning
- Implementing plugin architectures for LLM hosts
- Evaluating agentic scaffolding mechanisms (evidence-anchored vs. inferred)
- Building hypothesis generation frameworks with uncertainty quantification

### Key Design Principles (Evidence-Anchored)

1. **Evaluator independence** — GENERATE and EVALUATE must use different models (R1, 10-25% inflation if violated)
2. **Temporal ordering** — GENERATE → EVALUATE → SELECT (R2, 74% vs 4% on Game of 24)
3. **Diversity preservation** — Quota at SELECT prevents premature convergence (R15, ~85% confident)
4. **Provenance logging** — All EVALUATE operations logged (R9, W3C PROV)
5. **Dynamic grounding** — RETRIEVE weight calibrated by phase (R5, inverted-U relationship)
6. **Sandbox enforcement** — All ACT operations bounded (R17, OWASP)
7. **Uncertainty quantification** — All claims marked HIGH/MEDIUM/LOW confidence

---

## Related Projects

This repository is conceptually related to the user's **Open Sky** project (recursive recomposition substrate search) but focuses on **agentic scaffolding** rather than evolutionary search. Both share:
- Stage-gated development workflows
- Viability/evaluation gates
- Deformation robustness testing
- Motif/candidate preservation mechanisms

---

## Development Practices

### Methodological Principles

1. **Evidence > Reasoning > Assertion** — Validated relationships constrain design; inferred relationships guide it; assertions are hypotheses
2. **Uncertainty quantification** — All claims marked with confidence level (HIGH/MEDIUM/LOW)
3. **First principles reasoning** — Taxonomies evaluated by failure modes, constraints, optimization targets—not by authority
4. **Bias audit** — Document authority bias, deference bias, extraction bias; correct explicitly
5. **Dependency graphs reveal constraints** — Encode what breaks if violated, not what categories exist

### Specification Workflow

1. **Brainstorming** — Use `brainstorming` skill for design exploration
2. **Design doc** — Write to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
3. **Spec review** — Dispatch spec-document-reviewer subagent
4. **User review** — Human approves spec before implementation
5. **Implementation plan** — Invoke `writing-plans` skill (only after spec approved)

### Confidence Levels

| Level | Meaning | Action |
|-------|---------|--------|
| **HIGH** | Empirically validated across multiple studies | Enforce at architecture level |
| **MEDIUM-HIGH** | Strong inference, distinct failure modes | Implement with monitoring |
| **MEDIUM** | Logically sound, not yet validated | Implement, plan ablation study |
| **LOW** | Contested or untested | Flag as open question, don't enforce |

---

## Commands Reference

### Key Documents

| Document | Purpose |
|----------|---------|
| `docs/superpowers/specs/2026-03-23-dependency-graph-design.md` | Evidence-anchored dependency graph (approved spec) |
| `skills/universal-plugin-skill/SKILL.md` — Plugin architecture patterns |
| `docs/research/Agentic Scaffolding Skills Package - GPT.md` — Complete implementation skeleton |

### Skill Usage

| Skill | When to Use |
|-------|-------------|
| `brainstorming` | Design exploration, before any implementation |
| `writing-plans` | After spec approved, before coding |
| `critical-analysis` | Evaluating claims, identifying logical fallacies |
| `using-superpowers` | Check for applicable skills before any task |

---

## Recent Activity

**2026-03-23: Evidence-Anchored Dependency Graph Completed**

- Re-evaluated corpus taxonomies from first principles (not authority)
- Identified **9 primitives** (not 29, not 7) by distinct failure modes test
- Identified **8 families** (not 19, not 4) by implementation-relevance test
- Documented **10 validated relationships** (empirically confirmed)
- Documented **8 inferred relationships** (logically sound, not validated)
- Documented **7 open questions** (genuinely unresolved, need empirical study)
- Spec approved and committed to `docs/superpowers/specs/`

**Key Methodological Insight:** Dependency graphs should encode **what breaks if violated**, not **what categories exist**.

**Next Phase:** Phase 1 implementation (MEMORY + LOG substrate).

---

## Appendix: Bias Audit (2026-03-23)

This spec was produced after explicit bias correction:

| Pass | Bias Type | Correction Applied |
|------|-----------|-------------------|
| 1st | Authority bias (accepted corpus's 19 families) | Re-evaluated from first principles |
| 2nd | Deference bias (accepted partner's 9 primitives) | Applied irreducibility test rigorously |
| 3rd | First principles | Distinguished validated vs. inferred vs. uncertain |

**Lesson:** The dependency graph's purpose is **structural revelation**, not taxonomic completeness.
