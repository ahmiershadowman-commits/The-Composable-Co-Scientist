# The Compositional Co-Scientist - Final Delivery Plan

**Date:** 2026-03-23
**Status:** Phase 1-5 Complete, Phase 6-7 In Progress
**Goal:** Deliver production-ready plugin with working LLM integration

---

## Current State (As Built)

### Completed Components

| Component | Status | Files | Tests | Notes |
|-----------|--------|-------|-------|-------|
| **Core Primitives** | ✅ Complete | 9 files in `core/primitives/` | 14 tests | Placeholder implementations |
| **Constraints C1-C6** | ✅ Complete | 6 files in `core/constraints/` | 18 tests | Enforcement logic |
| **Data Models** | ✅ Complete | 4 files in `core/models/` | 4 tests | Candidate, Score, Defect, Document |
| **Storage Layer** | ✅ Complete | 5 files in `storage/` | 19 tests | SQLite backend, TTL, decay |
| **Skill Wrappers** | ✅ Complete | 9 files in `api/skills/` | 0 tests | Host integration layer |
| **Command Handlers** | ✅ Complete | 1 file in `api/commands/` | 0 tests | `/generate`, `/evaluate`, `/synthesize` |
| **Host Adapters** | 🟡 Partial | 3 files in `adapters/` | 0 tests | Stub implementations |
| **Documentation** | 🟡 Partial | API reference | - | User guide + tutorials pending |

### Metrics
- **57 tests passing** (95% coverage)
- **76 files created**
- **22 commits** on main branch

---

## Remaining Work

### Phase 6: LLM Integration (Priority: HIGH)

**Goal:** Replace placeholder primitive implementations with actual LLM calls via host adapters.

| Task | Files | Description | Priority |
|------|-------|-------------|----------|
| 6.1 | `adapters/base.py` | Create base adapter class with common interface | HIGH |
| 6.2 | `adapters/claude_code/skill.py` | Implement Claude SKILL tool invocation | HIGH |
| 6.3 | `adapters/qwen_code/skill.py` | Implement Qwen SKILL tool invocation | HIGH |
| 6.4 | `adapters/gemini_cli/tool.py` | Implement Gemini tool declaration | MEDIUM |
| 6.5 | `core/primitives/generate.py` | Wire to LLM for hypothesis generation | HIGH |
| 6.6 | `core/primitives/evaluate.py` | Wire to LLM for scoring | HIGH |
| 6.7 | `core/primitives/critique.py` | Wire to LLM for defect detection | MEDIUM |
| 6.8 | `core/primitives/synthesize.py` | Wire to LLM for synthesis | MEDIUM |

### Phase 7: sentence-transformers Integration (Priority: HIGH)

**Goal:** Replace constant similarity scores with actual embedding-based computation.

| Task | Files | Description | Priority |
|------|-------|-------------|----------|
| 7.1 | `requirements.txt` | Add `sentence-transformers>=2.2.0` | HIGH |
| 7.2 | `core/primitives/generate.py` | Compute diversity using embeddings | HIGH |
| 7.3 | `core/primitives/select.py` | Compute similarity matrix using embeddings | HIGH |
| 7.4 | `storage/similarity_cache.py` | Cache embeddings for reuse | MEDIUM |

### Phase 8: Documentation Polish (Priority: MEDIUM)

| Task | Files | Description | Priority |
|------|-------|-------------|----------|
| 8.1 | `docs/user-guide/` | Write user guide | MEDIUM |
| 8.2 | `docs/tutorials/` | Write tutorial workflows | MEDIUM |
| 8.3 | `docs/examples/` | Add example scripts | LOW |

---

## Execution Strategy

### Ralph Loop Protocol

For each phase, execute:

1. **Spec Review** - Verify design matches constraints
2. **Implementation** - TDD: test → fail → implement → pass
3. **Two-Stage Review**:
   - Stage 1: Spec compliance (does it enforce C1-C6?)
   - Stage 2: Code quality (tests, coverage, style)
4. **Commit** - Conventional commits with test proof

### Task Dispatch Order

```
Phase 6 (LLM Integration):
  6.1 → 6.2 → 6.3 → 6.4 → 6.5 → 6.6 → 6.7 → 6.8
  
Phase 7 (sentence-transformers):
  7.1 → 7.2 → 7.3 → 7.4
  
Phase 8 (Documentation):
  8.1 → 8.2 → 8.3
```

---

## Success Criteria

| Criterion | Target | Current | Status |
|-----------|--------|---------|--------|
| Tests passing | 57+ | 57 | ✅ |
| Branch coverage | 80%+ | 95% | ✅ |
| LLM integration | 4 primitives | 0 | 🔴 |
| sentence-transformers | diversity + similarity | constant 0.5 | 🔴 |
| User guide | Complete | Partial | 🔴 |
| Tutorial workflows | 3+ | 0 | 🔴 |

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| OneDrive file locks | git gc fails | Non-critical; skip or run offline |
| LLM API rate limits | Testing blocked | Use mocks; add retry logic |
| sentence-transformers slow | User experience | Add caching; lazy loading |

---

## Timeline Estimate

| Phase | Estimated Time | Dependencies |
|-------|----------------|--------------|
| Phase 6 | 4-6 hours | None |
| Phase 7 | 2-3 hours | Phase 6 |
| Phase 8 | 2-3 hours | None |
| **Total** | **8-12 hours** | |

---

## Next Action

**Dispatch subagent for Phase 6, Task 6.1:** Create base adapter class.
