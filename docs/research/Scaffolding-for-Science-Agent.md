# Agentic scaffolding for LLM-based research agents: a dependency-graph analysis

**The full theoretical space of agentic scaffolding for LLM-based research agents decomposes into 19 ontological families, each encoding a distinct theory of what agency *is*, what representational objects it requires, what failure modes it drifts toward, and what primitives it reuses.** The dependency graph reveals that no single family is self-sufficient: every ontology presupposes primitives from at least two others, and the most dangerous failure modes emerge precisely at family boundaries — where one ontology's assumptions silently violate another's requirements. The deepest structural tension in the space is between convergence pressure (evaluation, selection, formalization) and divergence preservation (novelty, developmental incubation, dialectical tension). Systems that collapse this tension prematurely — by ranking before exploring, formalizing before incubating, or resolving before articulating — account for the majority of documented agent failures.

---

## 1 · Research map: high-level topology of the space

The landscape organizes into four super-clusters of ontological families, connected by dependency edges:

**Generation-side families** (how candidates come into existence): Decomposition, Search, Developmental/Gestational, Novelty-Preservation.

**Evaluation-side families** (how candidates are judged): Evaluation/Verifier, Selection/Competitive, Reliability/Safety, Formalization/Crystallization.

**Coordination-side families** (how multiple stances interact): Coordination/Orchestration, Dialectical/Tension-Preserving, Multi-Perspectival/Pluralist, Integrative/Cross-Framework.

**Grounding-side families** (how the agent contacts reality): Retrieval/Grounding, Graph/Structural, Memory/Lineage, Tool/Action, Boundary/Consequence, Human-Judgment/Oversight.

**Deliberative/Reflective** occupies a bridging position — it connects generation-side to evaluation-side by feeding evaluation output back into generation.

The single most load-bearing dependency in the graph is **Evaluation/Verifier → all generation-side families**. Search is vacuous without scoring. Selection is random without fitness functions. Developmental maturation is directionless without stage-appropriate evaluation. Every generation-side family depends on evaluation; the quality of the evaluator bounds the quality of everything downstream.

---

## 2 · Source base

**Primary mechanism sources (high-confidence, empirically grounded):** Yao et al. 2023 (Tree-of-Thoughts); Besta et al. 2023 (Graph-of-Thoughts); Shinn et al. 2023 (Reflexion); Madaan et al. 2023 (Self-Refine); Wang et al. 2022 (Self-Consistency); Romera-Paredes et al. 2024 (FunSearch, Nature); Guo et al. 2023 (EvoPrompt); Packer et al. 2023 (MemGPT); Sumers et al. 2024 (CoALA, TMLR); Du et al. 2024 (Multi-Agent Debate, ICML); Yao et al. 2023 (ReAct); Schick et al. 2023 (Toolformer, NeurIPS); Microsoft 2024 (GraphRAG); Bai et al. 2022 (Constitutional AI); Wu et al. 2022 (Autoformalization, NeurIPS).

**Primary scientific-agent sources:** Boiko et al. 2023 (Coscientist, Nature); Bran et al. 2024 (ChemCrow, Nature Machine Intelligence); Lu et al. 2024 (AI Scientist v1); Sakana 2025 (AI Scientist v2); Gottweis et al. 2025 (AI Co-Scientist/Google); Ghafarollahi and Buehler 2024 (SciAgents, Advanced Materials); Chen et al. 2025 (ScienceAgentBench, ICLR).

**Critical negative-result sources:** Huang et al. 2024 (LLMs Cannot Self-Correct Reasoning Yet, ICLR); Kamoi et al. 2024 (When Can LLMs Correct Their Own Mistakes, TACL); Wynn et al. 2025 (Talk Isn't Always Cheap); Cemri et al. 2025 (MASFT failure taxonomy, NeurIPS); Beel et al. 2025 (independent AI Scientist evaluation); Kambhampati et al. 2025 (Self-Verification Limitations, ICLR); Kim et al. 2025 (Google DeepMind error amplification study).

**Frameworks and surveys:** CoALA (Sumers et al. 2024); COLA framework (ACL 2025); LATS (Zhou et al. 2024); CA2I (Jafari et al. 2025); Three-Pillar Model (2025); Parasuraman-Sheridan-Wickens automation spectrum; MASFT failure taxonomy (NeurIPS 2025); surveys on LLM scientific discovery (arxiv 2505.13259, 2503.24047).

---

## 3 · Ontological family taxonomy: definitions and boundaries

Each of the 19 families encodes a distinct answer to the question "what is agency?" The families are not mutually exclusive — real systems combine several — but each carries specific representational commitments, control-flow requirements, and characteristic blindspots.

### Families 1–5: Generation and deliberation cluster

**Family 1 · Decomposition.** Agency as recursive partitioning of complex goals into tractable subproblems. Presupposes goals, plans, task DAGs, dependency relations. Control flow is hierarchical (linear chains, DAGs, recursive trees). The canonical vulnerability is **recomposition failure**: systems decompose carefully but reassemble results carelessly, losing cross-task emergent properties. Evidence: removing hierarchy from LLM planning causes a **59.3% success-rate drop**; but cascading errors in least-to-most chains propagate and compound through subsequent steps.

**Family 2 · Search.** Agency as systematic traversal of a reasoning-state space. Presupposes search trees/graphs, branching factors, depth bounds, heuristic/value functions, and frontier management. Control flow centers on the generate-evaluate-select loop. On Game of 24, GPT-4 + Chain-of-Thought solved **4%** while GPT-4 + Tree-of-Thoughts solved **74%**, demonstrating the power of structured search. The canonical vulnerability is **evaluator-search misalignment**: when the heuristic poorly correlates with true quality, search amplifies errors rather than correcting them.

**Family 3 · Developmental/Gestational.** Agency as progressive maturation from embryonic ideas to mature research outputs. Presupposes hypothesis objects with maturity scores, version histories, stage-gated artifacts, and progress trees. AI Scientist v2 operationalizes this as a three-stage progressive agentic tree search. The canonical vulnerability is **degeneration-of-thought**: agents repeat the same flawed reasoning across iterations even when explicit failures are identified.

**Family 4 · Deliberative/Reflective.** Agency as iterative self-critique and convergence toward correctness through successive approximation. Reflexion achieves **97% on AlfWorld** through verbal reinforcement learning with episodic memory. Self-Refine yields **~20% absolute improvement** across tasks through feedback-refine loops. However, the critical negative finding from Huang et al. (ICLR 2024) establishes that **intrinsic self-correction without external feedback degrades performance in reasoning tasks**. The canonical vulnerability is **self-bias**: LLMs systematically favor their own outputs even when flawed.

**Family 5 · Dialectical/Tension-Preserving.** Agency as structured articulation of genuine disagreements. Multi-Agent Debate (Du et al.) shows performance improves with more agents and more debate rounds — but Wynn et al. (2025) found that debate can **decrease accuracy**: models shift from correct to incorrect answers in response to persuasive but wrong peer reasoning. **Moderate disagreement achieves best performance; maximal disagreement polarizes without improving accuracy.** The canonical vulnerability is **sycophantic collapse** — agreement is favored over truth.

### Families 6–10: Evaluation and coordination cluster

**Family 6 · Selection/Competitive.** Agency as differential survival under evaluative pressure. Self-consistency (majority voting) is the foundational method. FunSearch (Nature 2024) synthesizes evolutionary selection with LLM generation, achieving the **first LLM-based mathematical discovery** by evolving programs in isolated island populations with formal evaluation. The canonical vulnerability is **premature convergence**: population diversity collapses before the global optimum is found.

**Family 7 · Retrieval/Grounding.** Agency as structured consultation of prior work. RAG architectures ground LLM generation in external corpora, reducing hallucination. PaperQA benchmarks retrieval-augmented literature review. Microsoft's GraphRAG adds community-level summarization. The canonical vulnerability is **retrieval dominance**: the agent degenerates into a paraphraser of retrieved content, losing capacity for novel synthesis. The grounding-creativity tradeoff follows an inverted U — some grounding enables creativity; excessive grounding kills it.

**Family 8 · Graph/Structural.** Agency as explicit relational reasoning over entities, claims, and evidence. GraphRAG structures knowledge into communities via Leiden clustering and LLM-generated summaries. SciAgents builds knowledge graphs with **>33,000 nodes and ~49,000 edges** for cross-domain hypothesis generation. The canonical vulnerability is **graph fetishization**: building elaborate knowledge graphs that add complexity without proportional reasoning benefit. Construction hallucination — where LLMs generate plausible but incorrect triples — poisons all downstream reasoning.

**Family 9 · Memory/Lineage.** Agency as persistence and developmental inheritance across time. MemGPT introduces virtual context management analogous to OS virtual memory, with tiered storage (core memory, archival, recall). CoALA provides the canonical taxonomy: working, episodic, semantic, and procedural memory. A-MEM implements Zettelkasten-inspired interconnected memory notes. The canonical vulnerability is **hidden memory path dependence**: early memories disproportionately shape all subsequent reasoning, creating invisible biases. Flawed memories compound through **self-degradation spirals**.

**Family 10 · Coordination/Orchestration.** Agency as management of multiple interacting modules. The MASFT taxonomy (NeurIPS 2025) identifies **14 failure modes across 5 multi-agent frameworks**, organized into specification failures, inter-agent misalignment, and verification/termination failures. Google DeepMind found that unstructured multi-agent networks **amplify errors up to 17.2×** versus single-agent baselines. The canonical vulnerability is **cargo-cult multi-agentism**: deploying multi-agent systems for tasks a single agent handles adequately — **40% of agentic AI projects are projected to be canceled by 2027** due to this pattern.

### Families 11–15: Grounding and external-contact cluster

**Family 11 · Tool/Action.** Agency as extending cognition through instruments. The ReAct paradigm interleaves Thought → Action → Observation loops. Toolformer demonstrates LLMs can self-supervisedly learn when and how to call APIs. ChemCrow transforms GPT-4 "from a hyperconfident information source to a reasoning engine" via 18 chemistry tools. The canonical vulnerability is **tool-output credulity**: agents treat tool returns as ground truth, unable to distinguish tool errors from reasoning errors.

**Family 12 · Evaluation/Verifier.** Agency as requiring explicit judgment layers. Process Reward Models (PRMs) score each reasoning step; Outcome Reward Models (ORMs) score final answers only. PRMs measuring "progress" are **8× more compute-efficient** than ORMs for test-time search. Evidence strongly establishes that **self-verification yields smaller gains than cross-family verification**: LLMs show self-enhancement bias, judging solutions resembling their own reasoning as more likely correct. The canonical vulnerability is **evaluator collapse**: when generator and verifier share training biases, verification provides false assurance.

**Family 13 · Boundary/Consequence.** Agency as constrained by downstream effects. The CA2I framework inserts consequence assessment between action generation and execution. AgentSpec uses LTL formulas for runtime safety enforcement, achieving **87–95% detection on unseen risky scenarios**. The canonical vulnerability is **paralysis by analysis**: excessive consequence pre-assessment prevents timely action.

**Family 14 · Formalization/Crystallization.** Agency as movement from fluid exploration toward formal structure. Autoformalization translates informal mathematics to formal proofs (Wu et al. achieved **25.3% perfect translation** of math competition problems to Isabelle/HOL). FunSearch's program-skeleton approach formalizes structure while leaving critical logic open for creative evolution. The canonical vulnerability is **premature formalization**: forcing formal structure on ideas that haven't matured, killing creative possibility.

**Family 15 · Multi-Perspectival/Pluralist.** Agency as requiring genuine stance diversity. Mixture-of-Agents achieves **65.1% on AlpacaEval 2.0** (vs. GPT-4 Omni's 57.5%) using only open-source models, through layered proposer-aggregator architecture. ReConcile demonstrates that **multi-model diversity dramatically outperforms multi-instance same-model** approaches. The canonical vulnerability is **performative diversity**: agents assigned different roles but generating from the same underlying model with shared biases.

### Families 16–19: Meta and safety cluster

**Family 16 · Integrative/Cross-Framework.** Agency as meta-cognitive selection across heterogeneous reasoning strategies. CoALA provides the theoretical foundation, bridging symbolic AI and probabilistic LLMs. LATS unifies reasoning, acting, and planning in a single MCTS-based framework. The canonical vulnerability is **meta-cognitive paralysis**: spending more time choosing strategies than executing them.

**Family 17 · Novelty-Preservation.** Agency as active resistance to convergence on the familiar. Typicality bias in preference data drives **pervasive mode collapse** in post-trained LLMs. Doshi and Hauser (Science Advances 2024) found that while individual LLM-assisted stories are rated more creative, **LLM-enabled stories are more similar to each other** — collective novelty decreases. The most effective preservation mechanisms are quality-diversity algorithms (MAP-Elites, island models), verbalized sampling (1.6–2.1× diversity improvement), and novelty-aware RL rewards. The canonical vulnerability is **novelty theater**: generating superficially different but semantically identical outputs.

**Family 18 · Human-Judgment/Oversight.** Agency as collaborative, with delegated and revocable authority. The Parasuraman-Sheridan-Wickens 10-level automation spectrum frames the design space. Most current agents operate at Levels 3–6. Magentic-UI implements co-planning (human reviews agent plans) and co-tasking (human can intervene during execution). The canonical vulnerability is **rubber-stamping**: humans approving everything without meaningful review, especially because LLMs generate "convincingly wrong" plans that appear plausible.

**Family 19 · Reliability/Safety.** Agency as bounded autonomy with failure containment. Compound reliability math dominates: if each step has 95% reliability, a 10-step pipeline achieves only **~60% end-to-end reliability**. The MASFT taxonomy documents that **79% of multi-agent failures originate from specification and coordination issues**, not technical implementation. Sampling-based confidence estimation achieves best discrimination (AUROC 0.66–0.74) but verbalized confidence is **consistently overconfident**. The canonical vulnerability is **invisible failure accumulation**: each step introduces small errors that compound silently.

---

## 4 · Methodological family taxonomy

Ontological families answer **"what is agency?"** Methodological families answer **"how do you build and evaluate agents under that ontology?"** The distinction matters because the same ontological commitment can be realized through multiple methodological approaches, and methodological choices carry their own dependencies.

**Prompting-based methods** realize ontological commitments through prompt engineering alone (Chain-of-Thought, Tree-of-Thoughts, Self-Consistency, Self-Refine). These are lightweight, require no training, but are bounded by the base model's capabilities and context window.

**Training-based methods** realize commitments through fine-tuning or reinforcement learning (DeepSeek-R1 RL training, process reward model training, EVOL-RL for novelty-aware reasoning). These can shape model behavior more deeply but require data, compute, and risk reward hacking.

**Architecture-based methods** realize commitments through external scaffolding — memory systems, tool registries, multi-agent topologies, graph databases, sandbox environments (MemGPT, GraphRAG, LangGraph state machines, AgentSpec runtime enforcement). These are the most flexible but add infrastructure complexity.

**Hybrid methods** combine approaches — prompting for reasoning, RL for policy learning, architecture for memory and tools (LATS, AI Co-Scientist, FunSearch). The most capable systems are hybrid, but hybridization multiplies integration dependencies.

---

## 5 · Dependency family graph

### 5.1 Representational dependencies

Every ontological family presupposes specific objects that must exist in the system's state:

| Family | Required objects | Object type |
|---|---|---|
| Decomposition | Goals, plans, task DAGs, subtasks, dependency edges | Structural |
| Search | Search trees/graphs, frontier, heuristic values, depth bounds | Navigational |
| Developmental | Hypothesis objects with maturity scores, version histories, stage gates | Temporal |
| Reflective | Reflection summaries, feedback objects, episodic memory buffers | Evaluative |
| Dialectical | Debate transcripts, position statements, tension markers, judge verdicts | Argumentative |
| Selection | Candidate populations, fitness functions, rankings, diversity measures | Population |
| Retrieval | Chunks, embeddings, indices, citations, relevance scores | Corpus |
| Graph | Entities, typed relations, triples, subgraphs, community summaries | Structural |
| Memory | Working memory, episodic/semantic/procedural stores, provenance records | Persistent |
| Coordination | Agent roles, interaction topologies, message protocols, shared state | Social |
| Tool/Action | Tool registry, action schemas, observation buffers | Instrumental |
| Evaluation | Candidates, scores, rubrics, rankings, verification verdicts | Judgmental |
| Boundary | Consequence vectors, permission manifests, sandbox specs, risk constraints | Constraining |
| Formalization | Informal-formal pairs, proof objects, verification signals, skeletons | Formal |
| Pluralist | Agent role definitions, diversity metrics, confidence scores, layered outputs | Collective |
| Integrative | Strategy representations, meta-policies, cognitive modules, decision cycles | Meta-cognitive |
| Novelty | Novelty scores, population archives, diversity budgets, behavioral descriptors | Divergence |
| Human-Judgment | Escalation policies, approval queues, annotation schemas, trust models | Collaborative |
| Reliability | Confidence scores, failure logs, drift indicators, guardrail specs, provenance | Protective |

### 5.2 Control-flow dependencies

| Family | Primary pattern | Recurrence | Branching |
|---|---|---|---|
| Decomposition | Sequential/DAG | Low — execute plan once | Yes — parallel independent subtasks |
| Search | Generate-evaluate-select loop | High — iterate until termination | Yes — multiple candidate expansions |
| Developmental | Multi-stage pipeline with feedback | Medium — iterate within stages | Yes — tree search over experimental paths |
| Reflective | Generate-critique-revise loop | High — 2–5 iterations typical | No — single-path refinement |
| Dialectical | Round-robin debate with judge | Medium — 2–4 rounds typical | No — convergent toward consensus |
| Selection | Generate-score-select | Medium — evolutionary generations | Yes — population maintains multiple candidates |
| Retrieval | Query-retrieve-rank-generate | Low-medium — 1–3 retrieval rounds | Minimal |
| Coordination | Supervisor-worker or peer-to-peer | Varies by topology | Yes — fan-out to multiple agents |
| Tool/Action | Thought-action-observation loop | High — until task complete | Minimal per step |
| Evaluation | Score and filter | Low — applied once per candidate | No |
| Boundary | Pre-execute → assess → gate → execute | Low per action | No |
| Formalization | Translate → verify → retry | Medium — until proof checks | Minimal |

### 5.3 Core dependency graph (major edges)

The following table captures the strongest inter-family dependencies. Strength is rated high/medium/low; conditionality indicates whether the dependency is always present or only in specific configurations.

| Source family | Target family | Edge type | Strength | Conditionality | Stage |
|---|---|---|---|---|---|
| Search | Evaluation/Verifier | **requires** | High | Unconditional | All |
| Selection | Evaluation/Verifier | **requires** | High | Unconditional | All |
| Decomposition | Coordination | **enables** | High | Conditional on multi-agent | Mid |
| Reflective | Tool/Action | **amplified-by** | High | Strongest with external feedback | Mid-late |
| Dialectical | Pluralist | **requires** | Medium | Debate needs genuine diversity | Mid |
| Developmental | Novelty-Preservation | **requires** | Medium | Prevents refinement from killing novelty | Early-mid |
| Developmental | Formalization | **stage-gates** | Medium | Formalization readiness check | Late |
| Novelty-Preservation | Selection | **conflicts-with** | Medium | Selection pressure kills diversity | Early vs. mid |
| Formalization | Evaluation/Verifier | **enables** | High | Formal verification is the gold standard | Late |
| Memory/Lineage | Reflective | **requires** | High | Reflection is meaningless without memory | All |
| Retrieval | Graph/Structural | **enables** | Medium | GraphRAG builds on retrieved text | Mid |
| Tool/Action | Boundary/Consequence | **requires** | High | Tools without boundaries cause harm | All |
| Boundary | Human-Judgment | **depends-on** | Medium | Humans set boundaries and handle edge cases | All |
| Reliability | Evaluation | **depends-on** | High | Reliability needs verification mechanisms | All |
| Coordination | Evaluation | **requires** | High | Multi-agent systems need verification agents | All |
| Integrative | All generation families | **depends-on** | High | Meta-cognitive routing needs strategies to route between | Late |
| Reflective (self-only) | Truth/correctness | **fails-without** | High | Self-correction degrades without external signal | All |

### 5.4 Critical dependency chains

**Chain 1 (Search-Evaluation-Reliability):** Search quality is bounded by evaluator quality. Evaluator quality is bounded by calibration and independence. Calibration quality is bounded by held-out data availability. This chain means that **any search-heavy system is only as good as its least reliable evaluation layer**.

**Chain 2 (Novelty-Development-Formalization):** Novel ideas must be protected → then matured through iteration → then formalized for verification. Breaking this chain — by formalizing before maturing, or by selecting before incubating — produces either premature convergence or specification lock-in.

**Chain 3 (Tool-Boundary-Human-Reliability):** Tool invocation requires boundary constraints, which require human-defined thresholds, which require reliability monitoring. This four-family chain is the **safety backbone** of any deployed research agent.

---

## 6 · Primitive taxonomy

Primitives are the reusable atomic operations that recur across families. Each primitive has presuppositions, family affiliations, and characteristic degenerations.

| Primitive | What it does | Presupposes | Primary families | Degenerates into |
|---|---|---|---|---|
| **decompose** | Partition goal into subproblems | Goal structure, decomposition criteria | Decomposition, Coordination | Decomposition theater (splitting simple tasks) |
| **plan** | Generate ordered sequence of actions | Action space, dependency model | Decomposition, Search | Rigid plans that can't adapt |
| **generate** | Produce candidate outputs | Generative model, sampling strategy | Search, Selection, Developmental | Mode collapse under low temperature |
| **retrieve** | Fetch relevant external information | Index, embedding space, query | Retrieval, Memory | Retrieval dominance (paraphrasing sources) |
| **embed/index** | Create searchable representation | Embedding model, storage | Retrieval, Memory | Embedding monoculture |
| **evaluate/score** | Assign quality assessment | Rubric, scoring function | Evaluation, Selection, Search | Evaluator collapse into style preference |
| **rank** | Order candidates by quality | Scoring, comparison method | Selection, Evaluation | Premature ranking of immature candidates |
| **select** | Choose survivors from candidates | Ranking, selection criterion | Selection, Search | Premature convergence |
| **reflect** | Assess own output quality | Prior output, evaluation criteria | Reflective, Developmental | Infinite reflection loops |
| **critique** | Identify specific deficiencies | Output, criteria, critical capacity | Reflective, Dialectical | Critique collapse into surface suggestions |
| **debate** | Structured argumentative exchange | Multiple stances, judge | Dialectical, Pluralist | Sycophantic collapse |
| **revise** | Improve output based on feedback | Feedback, original output | Reflective, Developmental | Sanding away novel elements |
| **verify** | Check correctness against standard | Standard (formal or heuristic) | Evaluation, Formalization, Reliability | Verification theater |
| **call-tool** | Invoke external instrument | Tool registry, parameters | Tool/Action | Tool-output credulity |
| **sandbox** | Isolate execution environment | Container/permission system | Boundary, Reliability | Over-containment killing utility |
| **persist/store** | Write to long-term memory | Memory store, encoding | Memory/Lineage | Memory bloat |
| **recall** | Retrieve from own history | Memory store, query | Memory/Lineage | Hidden path dependence |
| **forget/decay** | Remove or deweight memory | Decay policy, utility scoring | Memory/Lineage | Amnesia of critical context |
| **formalize** | Translate fluid ideas to formal structure | Target formal language, idea maturity | Formalization | Premature formalization |
| **diversify** | Increase population heterogeneity | Diversity metric, generation capacity | Novelty, Selection | Novelty theater |
| **escalate** | Request human input | Escalation policy, context summary | Human-Judgment | Ungrounded escalation (escalating everything) |
| **checkpoint** | Save state for potential rollback | State serialization, storage | Boundary, Reliability, Memory | Checkpoint overhead without use |
| **aggregate** | Merge multiple outputs into synthesis | Multiple sources, merging criteria | Coordination, Pluralist, Integrative | Averaging to mediocrity |
| **route** | Direct task to appropriate handler | Routing policy, agent registry | Coordination, Integrative | Overcentralized orchestration |
| **trace-consequence** | Simulate downstream effects | Consequence model, historical data | Boundary | Paralysis by analysis |
| **calibrate** | Align confidence with accuracy | Calibration data, uncertainty method | Reliability, Evaluation | False confidence from uncalibrated scores |
| **halt/stop** | Terminate execution | Stopping criteria | Reliability, Boundary | Missing stopping conditions (runaway agent) |
| **log-failure** | Record detected failure | Failure taxonomy, logging infrastructure | Reliability | Invisible failure accumulation |

---

## 7 · Best-practice families

Each practice below is established from evidence across multiple sources, not asserted as axiom.

**Explicit stage separation.** AI Scientist v2's three-stage progressive tree search outperforms undifferentiated refinement. Ablation studies show removing hierarchy causes 59.3% success-rate drops. Separating divergent exploration from convergent evaluation prevents premature convergence (supported by Quality-Diversity literature, Double Diamond creativity framework, and FunSearch's evolutionary architecture).

**Claim-evidence separation.** GraphRAG's entity-relation extraction, SciAgents' hypothesis-evidence graphs, and Chain-of-Verification's decomposition of claims into verifiable sub-questions all demonstrate that separating claims from evidence enables targeted verification and prevents fluency-truth conflation.

**Critique before commitment.** Constitutional AI's critique-revision loops, Reflexion's verbal self-reflection before retry, and AI Co-Scientist's reflection agent acting as internal peer reviewer all show that inserting evaluation before propagation catches errors earlier. However, this practice must use **external feedback** — intrinsic self-critique alone degrades reasoning performance (Huang et al., ICLR 2024).

**Preservation of alternatives.** FunSearch's island-based population maintenance, self-consistency's multiple-sample generation, and AI Co-Scientist's tournament-based hypothesis retention all maintain candidate diversity until evaluation pressure is justified. The strongest evidence: FunSearch's island model with periodic extinction of stagnant populations produced the first LLM-based mathematical discovery.

**Explicit uncertainty marking.** Sampling-based uncertainty quantification achieves AUROC 0.66–0.74 with accurate calibration. Verbalized confidence is consistently overconfident. Best practice: propagate calibrated uncertainty through pipeline stages and present confidence intervals rather than point estimates.

**Evaluator separation.** Cross-family verification (using models from different training lineages) is **significantly more effective** than self-verification. GPT-4 shows 10% self-win-rate inflation; Claude-v1 shows 25%. The recommendation: never use the same model for final generation and final verification.

**Bounded tool use.** The "Theory of Agent as Tool-Use Decision-Maker" formalizes the optimal boundary: tool invocation should occur at the agent's **epistemic boundary** — where internal knowledge is insufficient. Overestimating internal solvability causes hallucination; underestimating it causes wasteful tool proliferation.

**Diversity maintenance.** Genuine model diversity (different training families) dramatically outperforms multi-instance same-model (ReConcile). Mixture-of-Agents outperforms GPT-4 Omni using only open-source models through genuine architectural diversity. Temperature alone is **weakly correlated with novelty** and insufficient for diversity.

**Structured memory hygiene.** MemGPT's treatment of forgetting as an essential feature, not a failure mode, establishes the practice. Active decay policies with utility scoring, periodic consolidation, and separation of episodic from semantic stores prevent memory bloat and self-degradation spirals.

**Consequence tracing before finalization.** CA2I's consequence assessment module, inserted between generation and execution, demonstrates that pre-execution consequence simulation reduces irreversible errors. AgentSpec's LTL-based runtime enforcement achieves 87–95% detection of risky scenarios.

**Compound reliability accounting.** Explicitly computing end-to-end reliability from per-step estimates reveals hidden fragility. A 10-step pipeline at 95% per-step reliability yields only ~60% end-to-end reliability — making the case for redundancy, verification, and circuit breakers at every stage.

---

## 8 · Anti-pattern families

### Ontological anti-patterns

**Branded-system thinking.** Organizing analysis around named systems (AutoGPT, CrewAI, LangChain) rather than mechanisms obscures what actually matters — the primitives and dependencies, not the packaging.

**Architecture-by-analogy.** Mapping cognitive science terminology (episodic memory, working memory) onto LLM systems without functional substance. CoALA provides a principled mapping; most systems adopt the terminology without the mechanism.

**Cargo-cult multi-agentism.** Deploying multi-agent systems for tasks a single agent handles adequately. Microsoft's official guidance: "Use the lowest level of complexity that reliably meets your requirements." Google DeepMind's finding that unstructured multi-agent networks amplify errors 17.2× reinforces this.

### Epistemic anti-patterns

**Conflating fluency with truth.** Human evaluators rate assertive but incorrect outputs **15–20% higher** than accurate but cautiously worded outputs. This creates harmful RLHF feedback loops that reward confident wrongness.

**Conflating contradiction with productive tension.** Not all disagreement is dialectically productive. When agents share training biases, debate reinforces shared errors rather than challenging them. Debate decreases accuracy when weaker models corrupt stronger ones through persuasion.

**Untracked uncertainty.** Failing to propagate or aggregate uncertainty through pipeline stages. The final output lacks meaningful confidence bounds, and users cannot distinguish high-confidence from low-confidence claims.

### Temporal anti-patterns

**Premature formalization.** Forcing formal structure on ideas that haven't matured. "Early-stage formalization typically stifles tech startups by restricting the very creativity needed for innovation" — the same holds for research agents.

**Premature ranking.** Ranking candidates before sufficient evaluation. Scores based on noisy partial information lead to wrong ordering and premature pruning of promising candidates.

**Premature synthesis.** Combining frameworks before understanding each individually, producing incoherent chimeras. Stage collapse — treating all stages identically — is the structural version of this.

### Structural anti-patterns

**Retrieval dominance.** Agent becomes a paraphraser of retrieved content. "Recently observed for a number of commercial generative AI search engines" — the system quotes verbatim rather than reasoning.

**Graph fetishization.** Building elaborate knowledge graphs that add complexity without proportional benefit. "If the task involves highly unstructured text or doesn't require explicit relationships, the added complexity may not be worth it."

**Hidden memory path dependence.** Early memories disproportionately shape subsequent reasoning. Flawed memories → flawed actions → flawed new memories → accelerating self-degradation.

**Evaluator collapse into style preference.** Verifiers trained on human preference data learn to reward fluency, length, and assertiveness rather than correctness. Position bias, verbosity bias, and self-enhancement bias are all documented in LLM-as-judge systems.

**Overcentralized orchestration.** Single supervisor becomes bottleneck and single point of failure. When the orchestrator fails, the entire system halts.

**False modularity.** Agents nominally separate but sharing so much state they are effectively one agent with extra overhead and communication costs.

**Invisible failure accumulation.** Each step introduces small errors that compound silently through the pipeline, producing conclusions built on accumulated errors no single check catches.

---

## 9 · Stage model

### Stage 0 · Problem sensing and question formation
**Primary families:** Retrieval (domain scan), Memory (recall prior research goals), Human-Judgment (goal validation).
**Key primitives:** retrieve, recall, escalate.
**Anti-patterns to avoid:** Premature decomposition, premature formalization.
**Critical requirement:** The question must be well-formed before any downstream stage activates. Reliability ontology's finding that safety mechanisms "assume the task is well-defined" means malformed questions propagate undetected.

### Stage 1 · Divergent exploration and candidate generation
**Primary families:** Search (broad exploration), Novelty-Preservation (diversity maintenance), Pluralist (multiple perspectives), Developmental (initial seeding).
**Key primitives:** generate, diversify, branch, retrieve, explore.
**Anti-patterns to avoid:** Premature ranking, premature convergence, retrieval anchoring.
**Critical requirement:** Novelty budgets must be explicit. Temperature alone is insufficient — quality-diversity algorithms, sequential (not parallel) sampling, and island-based populations are the evidence-backed mechanisms.

### Stage 2 · Protected development and incubation
**Primary families:** Developmental (maturation), Novelty-Preservation (protection from premature selection), Reflective (iterative improvement), Memory (version tracking).
**Key primitives:** incubate, refine, persist, recall, maturity-check.
**Anti-patterns to avoid:** Stage collapse, premature formalization, degeneration of thought.
**Critical requirement:** Ideas must be evaluated by stage-appropriate criteria — embryonic ideas should not face mature-idea standards. External feedback improves refinement; self-critique alone causes degradation.

### Stage 3 · Critical evaluation and filtering
**Primary families:** Evaluation/Verifier (scoring), Selection (filtering), Dialectical (adversarial challenge), Reliability (failure detection).
**Key primitives:** evaluate, rank, select, debate, verify, calibrate.
**Anti-patterns to avoid:** Evaluator collapse, benchmark overfitting, fluency-truth conflation, majority voting on systematic errors.
**Critical requirement:** Evaluator diversity — cross-family verification is essential. Formal verification where available (code, math) is the gold standard because it resists reward hacking.

### Stage 4 · Synthesis and integration
**Primary families:** Coordination (merging outputs), Integrative (cross-framework synthesis), Graph/Structural (mapping relations), Pluralist (aggregating diverse perspectives).
**Key primitives:** aggregate, synthesize, link, route, merge.
**Anti-patterns to avoid:** Premature synthesis, averaging to mediocrity, false modularity.
**Critical requirement:** Synthesis must preserve the strongest elements from each candidate rather than averaging. The graph structure must capture support/contradiction relations between integrated claims.

### Stage 5 · Formalization and crystallization
**Primary families:** Formalization (formal translation), Evaluation/Verifier (proof checking), Reliability (validation).
**Key primitives:** formalize, verify, type-check, proof-search, crystallize.
**Anti-patterns to avoid:** Hallucinated verification, specification drift, formalization-as-goal-displacement.
**Critical requirement:** Formalization readiness checks before engaging this stage. FunSearch's skeleton approach — formalize structure, leave critical logic open — balances formalization with flexibility.

### Stage 6 · Consequence tracing and boundary contact
**Primary families:** Boundary/Consequence (impact assessment), Tool/Action (external execution), Reliability (risk monitoring), Human-Judgment (expert review).
**Key primitives:** trace-consequence, sandbox, assess-risk, checkpoint, escalate.
**Anti-patterns to avoid:** Paralysis by analysis, consequence-blind execution, security theater.
**Critical requirement:** Irreversible actions require pre-execution assessment and human approval. Sandboxed execution is architectural safety; prompt-based guardrails are trivially bypassable.

### Stage 7 · Output, publication, and handoff
**Primary families:** Human-Judgment (final review), Reliability (provenance), Memory (archival), Formalization (final formatting).
**Key primitives:** escalate, log, persist, trace-provenance, present-alternatives.
**Anti-patterns to avoid:** Overclaiming, invisible failure accumulation, missing stopping criteria.
**Critical requirement:** Every claim must carry calibrated confidence and traceable provenance. The demo-deployment gap is severe: best agents solve only **32–42% of realistic scientific tasks** independently.

---

## 10 · Family-by-family analysis summary

| # | Family | Agency IS... | Strongest dependency | Best stage | Worst anti-pattern | Confidence |
|---|---|---|---|---|---|---|
| 1 | Decomposition | Divide-and-conquer | Evaluation (to verify subtasks) | 0–2 | Decomposition theater | High |
| 2 | Search | Pathfinding in state space | Evaluation (heuristic quality bounds search) | 1–3 | Premature pruning | High |
| 3 | Developmental | Progressive maturation | Novelty-Preservation (prevents refinement from killing novelty) | 2–4 | Degeneration of thought | Medium |
| 4 | Reflective | Self-monitoring feedback loop | Tool/Action (external feedback essential) | 2–5 | Self-bias / sycophantic self-correction | High |
| 5 | Dialectical | Structured conflict | Pluralist (genuine diversity required) | 3 | Sycophantic collapse | Medium |
| 6 | Selection | Differential survival | Evaluation (fitness function quality) | 3 | Premature convergence | High |
| 7 | Retrieval | Disciplined corpus consultation | Graph (relational structure over flat passages) | 0–1 | Retrieval dominance | High |
| 8 | Graph | Explicit relational reasoning | Retrieval (raw material for graph construction) | 2–4 | Graph fetishization | Medium |
| 9 | Memory | Persistent developmental inheritance | Reliability (memory quality assurance) | All | Hidden path dependence | Medium |
| 10 | Coordination | Multi-module management | Evaluation (verification agents essential) | 2–5 | Cargo-cult multi-agentism | High |
| 11 | Tool/Action | Cognitive extension via instruments | Boundary (tools without constraints cause harm) | 1–6 | Tool-output credulity | High |
| 12 | Evaluation | Explicit judgment layers | Independence (cross-family verification required) | 3–5 | Evaluator collapse | High |
| 13 | Boundary | Constraint by consequences | Human-Judgment (humans set boundaries) | 6 | Paralysis by analysis | Medium |
| 14 | Formalization | Fluid → formal transition | Developmental (ideas must mature first) | 5 | Premature formalization | Medium |
| 15 | Pluralist | Stance diversity | Genuine architectural/training diversity | 1, 3 | Performative diversity | Medium |
| 16 | Integrative | Meta-cognitive routing | All other families (parasitic) | Late | Strategy thrashing | Low |
| 17 | Novelty-Preservation | Resistance to convergence | Quality-diversity algorithms | 1–2 | Novelty theater | Medium |
| 18 | Human-Judgment | Collaborative authority | Consequential actions to oversee | 0, 6–7 | Rubber-stamping | High |
| 19 | Reliability | Bounded autonomy + failure containment | Evaluation (detection requires verification) | All | Invisible failure accumulation | High |

---

## 11 · Dependency tables

### Table A · Family × dependency type

| Family | Representational | Control-flow | Epistemic | Memory | Evaluation | Coordination | Novelty | Boundary | Failure |
|---|---|---|---|---|---|---|---|---|---|
| Decomposition | Goals, DAGs | Sequential/DAG | Completeness | Plan state | Subtask verification | When multi-agent | Low | Low | Cascading errors |
| Search | Trees, frontiers | Loop + branch | Heuristic quality | Tree state | Node scoring | Low | Low | Low | Search space explosion |
| Developmental | Maturity scores | Staged pipeline | Stage-appropriate | Version histories | Maturity checks | Low | High | Low | Degeneration |
| Reflective | Feedback objects | Refine loop | Verification ease > generation | Episodic buffer | Self/external critique | Low | Medium | Low | Self-bias loops |
| Dialectical | Debate transcripts | Round-robin | Truth-tracking | Debate history | Judge accuracy | High | Medium | Low | Sycophantic collapse |
| Selection | Populations | Evolutionary loop | Fitness fidelity | Population archive | Scoring function | Low | High | Low | Premature convergence |
| Retrieval | Chunks, indices | Query-retrieve-generate | Faithfulness | Vector store | Citation quality | Low | Low (anti-novelty) | Low | Retrieval dominance |
| Graph | Entities, triples | Extract-traverse-reason | Structural coherence | Graph database | Graph completeness | Low | Low | Low | Construction hallucination |
| Memory | Multi-tier stores | Read-write-forget | Recall accuracy | Self-referential | Decay utility | Low | Low | Low | Path dependence |
| Coordination | Roles, topologies | Various (fan-out, debate) | Ensemble quality | Shared state | Inter-agent verification | Self-referential | Medium | Low | Error amplification |
| Tool/Action | Tool registry | ReAct loop | Tool output validity | Tool cache | Task completion | Low | Low | High | Tool sprawl |
| Evaluation | Scores, rubrics | Score-and-filter | Calibration | Score history | Self-referential | Low | Low | Low | Evaluator collapse |
| Boundary | Permissions, risk | Pre-assess-gate | Consequence fidelity | Audit logs | Risk metrics | Low | Low | Self-referential | False safety |
| Formalization | Formal objects | Translate-verify | Proof correctness | Proof database | Verification rate | Low | Low (anti-novelty) | Low | Premature formalization |
| Pluralist | Diversity metrics | Parallel + aggregate | Complementarity | Cross-agent visibility | Ensemble accuracy | High | High | Low | Performative diversity |
| Integrative | Meta-policies | Hierarchical control | Strategy fitness | Strategy records | Meta-cognitive efficiency | High | Medium | Low | Strategy thrashing |
| Novelty | Population archives | QD algorithms | Novelty relative to archive | Novelty history | QD-score, coverage | Low | Self-referential | Low | Novelty theater |
| Human-Judgment | Escalation policies | Interrupt-based | Human reviewer quality | Feedback history | Escalation precision | Low | Low | High | Rubber-stamping |
| Reliability | Failure logs, drift | Guardrails + monitors | Calibration quality | Versioned state | Failure detection rate | Low | Low | High | Invisible accumulation |

### Table B · Family × stage suitability

| Family | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 |
|---|---|---|---|---|---|---|---|---|
| Decomposition | ● | ●● | ●● | ● | ● | ○ | ○ | ○ |
| Search | ○ | ●●● | ●● | ●●● | ○ | ○ | ○ | ○ |
| Developmental | ○ | ● | ●●● | ●● | ●● | ● | ○ | ○ |
| Reflective | ○ | ○ | ●● | ●● | ●● | ●● | ○ | ○ |
| Dialectical | ○ | ○ | ● | ●●● | ● | ○ | ○ | ○ |
| Selection | ○ | ○ | ○ | ●●● | ● | ○ | ○ | ○ |
| Retrieval | ●● | ●●● | ● | ● | ● | ● | ● | ● |
| Graph | ○ | ● | ●● | ●● | ●●● | ● | ● | ○ |
| Memory | ● | ● | ●● | ●● | ●● | ●● | ● | ●● |
| Coordination | ○ | ●● | ●● | ●●● | ●●● | ● | ● | ○ |
| Tool/Action | ○ | ●●● | ●● | ●● | ● | ●● | ●●● | ○ |
| Evaluation | ○ | ○ | ● | ●●● | ●●● | ●●● | ●● | ●● |
| Boundary | ○ | ○ | ○ | ○ | ○ | ● | ●●● | ●● |
| Formalization | ○ | ○ | ○ | ○ | ● | ●●● | ●● | ●● |
| Pluralist | ○ | ●●● | ● | ●●● | ●● | ○ | ○ | ○ |
| Integrative | ○ | ● | ●● | ●● | ●●● | ●● | ● | ○ |
| Novelty | ○ | ●●● | ●●● | ● | ○ | ○ | ○ | ○ |
| Human-Judgment | ●●● | ● | ● | ●● | ● | ●● | ●●● | ●●● |
| Reliability | ● | ● | ● | ●● | ●● | ●●● | ●●● | ●●● |

(●●● = primary stage, ●● = strong secondary, ● = relevant, ○ = low relevance)

### Table C · Primitive × failure mode

| Primitive | Failure mode when misused | Severity |
|---|---|---|
| decompose | Over-decomposition; orphan subtasks; recomposition failure | Medium |
| generate | Mode collapse; temperature-as-creativity fallacy | High |
| retrieve | Retrieval dominance; confirmation retrieval; context pollution | High |
| evaluate | Evaluator collapse; score-as-truth; benchmark overfitting | Critical |
| rank | Premature ranking; noisy scores → wrong ordering | High |
| select | Premature convergence; majority amplifying systematic errors | High |
| reflect | Infinite reflection loops; degeneration of thought; self-bias | Medium |
| debate | Sycophantic collapse; persuasion ≠ truth; weak-agent corruption | Medium |
| verify | Verification theater; hallucinated proofs; false safety | Critical |
| call-tool | Tool sprawl; tool-output credulity; infinite tool loops | High |
| persist | Memory bloat; crystallizing flawed hypotheses | Medium |
| forget | Amnesia of critical context; premature memory decay | Medium |
| formalize | Premature formalization; specification drift; hallucinated proofs | High |
| escalate | Ungrounded escalation; bottleneck paralysis; context-free escalation | Medium |
| aggregate | Averaging to mediocrity; false synthesis; losing minority-correct positions | High |

---

## 12 · Strongest structural tensions

**Tension 1 · Convergence vs. divergence.** The deepest tension in the entire space. Evaluation, Selection, and Formalization all exert convergence pressure. Novelty-Preservation, early-stage Developmental growth, and Dialectical tension-preservation all require divergence protection. These pressures are **necessarily in opposition** and cannot be dissolved — only managed through explicit stage separation, where divergent and convergent phases alternate with clear transitions. The FunSearch paradigm (island-based evolution with formal evaluation) is currently the most successful synthesis.

**Tension 2 · Self-evaluation vs. evaluator independence.** Reflective ontology demands self-critique. Evaluation ontology's evidence base shows self-critique is unreliable without external signal. The resolution is not to abandon reflection but to ensure every reflective loop has access to external verification tools or cross-family judges. Constitutional AI's principle-guided revision is a partial solution; CRITIC's tool-augmented self-verification is a stronger one.

**Tension 3 · Grounding vs. creativity.** Retrieval anchors the agent in existing knowledge, reducing hallucination but suppressing novel synthesis. The relationship follows an inverted U: moderate grounding enables creativity, excessive grounding kills it. No principled method exists for calibrating this tradeoff dynamically — it remains an open problem requiring task-type-specific tuning.

**Tension 4 · Autonomy vs. oversight.** Tool/Action and Decomposition families push toward autonomous execution. Human-Judgment and Boundary families impose oversight requirements. Every human checkpoint adds latency and introduces human error/bias. Every autonomous step compounds agent error. The Parasuraman-Sheridan-Wickens spectrum (Levels 1–10) provides the gradient, but **optimal automation level is task-dependent and changes as agent reliability improves**.

**Tension 5 · Memory fidelity vs. memory hygiene.** Memory/Lineage demands persisting all prior states for developmental inheritance. Reliability demands active forgetting to prevent self-degradation spirals. Preserving everything creates path dependence; forgetting aggressively creates amnesia. MemGPT's tiered architecture with intelligent decay represents the current best compromise.

**Tension 6 · Coordination benefit vs. coordination cost.** Multi-agent coordination can improve quality through diverse perspectives and specialized roles. But Google DeepMind's 17.2× error amplification finding, the MASFT 14-failure-mode taxonomy, and the 40% project cancellation projection all demonstrate that coordination overhead frequently exceeds coordination benefit. The resolution: **start single-agent and add agents only when measured quality improvement exceeds measured coordination cost**.

---

## 13 · Open problems and unknowns

**Reliable novelty assessment.** No system can reliably distinguish genuinely novel hypotheses from well-known ideas rephrased. AI Scientist v1 "incorrectly classified well-established concepts as novel, including micro-batching for SGD." This is arguably the single most important unsolved problem for research agents.

**Principled stage-transition criteria.** When should a research process move from exploration to evaluation, from incubation to formalization? Current systems use ad hoc iteration counts or human judgment. No evidence-backed, task-general criteria exist for stage transitions.

**Scalable evaluator independence.** Cross-family verification works but requires maintaining multiple diverse models. As the field converges on similar training data and techniques, the diversity that makes cross-family verification valuable may erode. Formal verification is the gold standard but applies only to formalized domains.

**Compound error detection.** Each pipeline step introduces small errors that compound silently. No robust mechanism exists for detecting when intermediate results have degraded below a quality threshold. End-to-end reliability accounting helps, but detection of *specific* accumulated errors remains unsolved.

**Dynamic grounding-creativity calibration.** The inverted-U relationship between grounding and creativity is recognized but not operationalized. No system dynamically adjusts retrieval strength based on whether the current phase needs factual anchoring or creative divergence.

**Long-horizon planning under uncertainty.** Multi-step research plans spanning days or weeks accumulate errors, encounter unexpected findings, and require replanning. Current systems are mostly plan-once-execute-sequentially. The few with adaptive replanning (AI Scientist v2's tree search) sacrifice reliability for exploration.

**Hallucination elimination.** Non-zero fabrication rates appear inherent to current LLM architectures. Best models fabricate 1–5% of the time, median ~25%. In multi-step agent pipelines, even 1% per-step fabrication compounds to significant end-to-end error rates. No mitigation is 100% effective.

**The evaluation-of-evaluation problem.** Who evaluates the evaluator? Guardrail systems can themselves fail, hallucinate, or be bypassed. Recursive evaluation creates infinite regress. Formal verification breaks the regress for formalized domains but cannot help with natural-language research claims.

**Cross-domain transfer of agent architectures.** Systems are typically domain-specific (chemistry, ML, biomedicine). Whether architectural patterns transfer across scientific domains remains empirically uncertain.

---

## 14 · Omission audit

**Potentially missing ontological families.** An **Embodiment/Situatedness Ontology** (agency as physically situated interaction with environments) was explicitly excluded per scope constraints but would be relevant for agents controlling laboratory equipment. An **Attention/Salience Ontology** (agency as selective attention to what matters most in a given context) is implicit in several families but never given explicit treatment. An **Aesthetic/Elegance Ontology** (agency as gravitating toward simple, beautiful solutions) is hinted at in formalization literature but not systematically investigated. A **Social/Institutional Ontology** (agency as embedded in social structures, norms, and institutions) would matter for agents operating in collaborative human research environments.

**Potentially under-explored mechanisms.** Counterfactual reasoning in agents (what would have happened if a different path were taken) is under-explored. Analogical reasoning across domains (transferring patterns from one scientific field to another) appears in SciAgents' cross-domain knowledge graph paths but lacks systematic treatment. Meta-learning (learning to learn, or improving the agent's learning process itself) is partially covered under Integrative but deserves deeper investigation.

**Potentially under-explored failure modes.** Distributional shift over time (agent trained/calibrated on one data distribution encountering a different one) is acknowledged but not deeply analyzed. Social dynamics failures in human-agent teams (trust calibration, role confusion, attribution disputes) are emerging concerns. The "model collapse" phenomenon where AI-generated content enters training data and degrades model quality could affect retrieval-grounding systems that index AI-generated text.

**Methodological gaps.** The analysis relies heavily on published research, which has publication bias toward successful methods and toward large-lab results. Failure reports are systematically underrepresented. The dependency graph captures structural relationships but does not quantify edge strengths empirically — most strength assessments are based on qualitative evidence integration rather than controlled experiments.

**Evaluation gaps.** No existing benchmark adequately captures research capability — the ability to formulate good questions, navigate ambiguity, maintain epistemic humility, and recognize knowledge boundaries. The demo-deployment gap remains large: best agents solve 32–42% of realistic scientific tasks. Whether benchmark improvements track real-world research capability improvements is unknown.

---

## 15 · Final synthesis

### The dependency graph reveals five load-bearing insights

**First, evaluation is the universal bottleneck.** Every generation-side family depends on evaluation quality. Search is bounded by heuristic quality. Selection is bounded by fitness function quality. Developmental maturation is bounded by stage-gate criteria quality. This means that **investing in better evaluation yields returns across every other family** — it is the single highest-leverage intervention in any agentic scaffolding design.

**Second, the convergence-divergence tension is structural, not incidental.** It cannot be dissolved by better architecture. It must be managed through explicit temporal separation — divergent phases followed by convergent phases, with stage-gate transitions controlled by maturity-appropriate criteria. The most successful system in the space (FunSearch) manages this tension through island-based evolution (divergence) with formal evaluation (convergence), separated across asynchronous cycles.

**Third, self-evaluation is the field's most dangerous default.** The evidence base is unambiguous: LLMs cannot reliably self-correct reasoning without external feedback. Self-enhancement bias, degeneration-of-thought, and sycophantic collapse are documented across multiple settings. Yet self-critique is the cheapest and most convenient evaluation method, making it the default in most systems. Every agent scaffold should treat self-evaluation as a useful heuristic that must be validated by an independent signal — external tools, formal verification, cross-model checking, or human review.

**Fourth, compound reliability is the hidden constraint.** The 95%-per-step → 60%-end-to-end math is rarely explicitly computed in agent system design. Error amplification in multi-agent systems (17.2× in unstructured networks) and the MASFT finding that 79% of multi-agent failures stem from specification and coordination issues (not technical implementation) both point to the same conclusion: **the coordination layer is where most failures originate**. Simple architectures with strong evaluation layers outperform complex architectures with weak evaluation.

**Fifth, the demo-deployment gap is real and large.** AI Scientist v1 produced papers described as "resembling a rushed undergraduate paper." Best agents solve 32–42% of realistic scientific tasks. Deep Research products cannot access paywalled content. ChemCrow and Coscientist developers explicitly state "it hasn't discovered anything yet." The gap between impressive demonstrations and reliable deployment is measured in years, not months. The primary bottleneck is not any single family but the compound effect of imperfect primitives across multi-step pipelines.

### Core primitives that survive across the full graph

Exactly seven primitives appear as dependencies across more than half of all 19 families: **generate**, **evaluate**, **persist**, **retrieve**, **route**, **halt**, and **log**. These form the irreducible primitive basis for any agentic scaffolding system. Every other primitive can be composed from or added to this basis. A minimal viable agent scaffold implements these seven well; a maximal scaffold adds the remaining 18+ primitives as the application demands.

### The single most important design principle

**Separate evaluation from generation architecturally, not just logically.** Use different models, different training lineages, or different modalities (formal verification vs. informal plausibility) for evaluation versus generation. Run evaluation at every stage transition, not just at the final output. Make evaluation results persistent and auditable. This single principle — evaluator independence — mitigates the largest number of documented failure modes across the largest number of ontological families. It is the closest thing the field has to a universal best practice.