# Agentic Scaffolding for Research and Scientific Agents: An Ontological and Dependency-Graph Map

## Research Map

### Object of study and operational definition

**Agentic scaffolding** (as audited here) is the *set of externalized representations, control-flow regimes, memory/provenance artifacts, coordination patterns, evaluators/verifiers, tool-boundaries, and oversight interfaces* that shape how a research/scientific agent behaves over time—especially across long-horizon, uncertainty-dense workflows—*without* presupposing any particular branded system. This definition treats “agency” as *trajectory-level competence* (multi-step adaptation under constraints) rather than single-shot output quality, aligning with the observation that agent failures compound across turns and state changes. citeturn7search17turn14search7

A core result of the mapping is that “agentic scaffolding” is not one thing: it is a **design space of families** whose relationships are best represented as a dependency graph. These families compete, substitute, and stage-gate one another, and they tend to drift into recognizable failure modes when their dependencies are missing or mis-specified. citeturn5search0turn5search28turn7search23turn4search2

### Rigor framework used in this investigation

This map uses an explicit scoping-review and mechanism-extraction discipline:

- **Scoping review discipline**: a broad, multi-pass, saturation-seeking scan in the spirit of scoping-study methodology and PRISMA-ScR reporting norms (broad inclusion, explicit charting, gap identification). citeturn14search1turn14search0turn1search4  
- **Mechanism extraction**: recurring mechanisms are treated as “codes,” clustered into families, then boundary-refined when mechanisms repeatedly co-occur or repeatedly diverge (i.e., merge/split decisions). citeturn14search7turn1search2turn7search29  
- **Claim–evidence–inference separation**: major conclusions below identify which parts are directly source-backed vs inferential generalizations. citeturn7search29turn4search2turn3search4  
- **Adversarial audit**: every major family is analyzed for hidden assumptions, over-application risks, and drift failure modes, consistent with safety and governance framings around specification gaming/reward hacking and evaluation misuse (Goodhart pressure). citeturn5search28turn5search0turn5search21

### High-level map of the space

The design space can be reconstructed as **nine macro-domains** (each containing multiple ontological and methodological families). The graph narrative is: *research agency is a trajectory through these macro-domains*.

**Macro-domain A: problem-structuring and work partitioning**  
- Ontological anchor: **Decomposition** (research as staged tasks/roles/subproblems).  
- Typical methodological supports: hierarchical planning / task-network decomposition; stage-gated artifact workflows. citeturn12view0turn12view1turn10view0  

**Macro-domain B: exploration in candidate/action space**  
- Ontological anchors: **Search**, **Selection/Competitive**, **Novelty-preservation**.  
- Methodological supports: branching search with self-evaluation; sampling + consistency/selection; evolutionary/quality-diversity archives and novelty search. citeturn2search1turn2search2turn0search7turn0search31  

**Macro-domain C: self-monitoring and self-revision**  
- Ontological anchors: **Deliberative/Reflective**, **Developmental/Gestational**.  
- Methodological supports: iterative critique/refinement loops; staged maturation models (incubation → verification). citeturn7search1turn6search25turn14search2  

**Macro-domain D: structured disagreement and tension management**  
- Ontological anchors: **Dialectical/Tension-preserving**, **Multi-perspectival/Pluralist**, **Integrative/Cross-framework**.  
- Methodological supports: formal argumentation frameworks; norms of transformative criticism; explicit stance separation. citeturn8search5turn1search3turn6search11  

**Macro-domain E: grounding in external corpora and inherited vocabularies**  
- Ontological anchor: **Retrieval/Grounding**.  
- Methodological supports: retrieval-augmented generation; retrieval evaluation metrics; knowledge-graph grounding. citeturn1search6turn1search2turn8search0turn8search7  

**Macro-domain F: explicit structure over concepts/claims/evidence and their relations**  
- Ontological anchor: **Graph/Structural** (dependencies among hypotheses, claims, evidence, tools, consequences).  
- Methodological supports: knowledge graphs; argument graphs; “graph of thoughts” style representations (as evidence of the method family, not as an organizing category). citeturn8search0turn8search6turn8search5  

**Macro-domain G: memory, lineage, and auditability across time**  
- Ontological anchor: **Memory/Lineage**.  
- Methodological supports: provenance standards and audit trails; reproducibility rules; versioning of artifacts and workflows. citeturn3search4turn13search23turn4search2  

**Macro-domain H: multi-process coordination and governance of control**  
- Ontological anchor: **Coordination/Orchestration** (stance separation, control arbitration).  
- Methodological supports: blackboard architectures; explicit separation of builder vs evaluator roles; interactive/human-in-the-loop design patterns. citeturn3search3turn10view2turn3search2  

**Macro-domain I: tool use, boundary contact, and risk control**  
- Ontological anchors: **Tool/Action**, **Evaluation/Verifier**, **Boundary/Consequence**, **Reliability/Safety**, **Human-Judgment/Oversight**.  
- Methodological supports: reason+act interleavings; verification layers; security threat models; risk management frameworks and stop/supersede mechanisms. citeturn2search0turn7search29turn2search3turn9view1  

### Load-bearing claim about central primitives

**Claim (high confidence):** Across the literature base sampled, the design space repeatedly collapses to a small set of load-bearing primitives: *(i) explicit state objects, (ii) branching + selection, (iii) critique/verification separation, (iv) grounded retrieval/tool feedback, (v) durable memory/provenance, (vi) stage gates and stopping criteria.*  
**Evidence:** search-based inference frameworks rely on branching plus self-evaluation and selection. citeturn2search1turn2search2 Retrieval-grounded systems require retrieval relevance/faithfulness evaluation and suffer when those are underspecified. citeturn1search2turn1search6turn7search23 Provenance and reproducibility guidance repeatedly emphasize tracking how results were produced and preserving executable workflow artifacts. citeturn13search23turn4search2turn3search4 Frameworks for risk and governance repeatedly emphasize separation of roles (build/use vs verify/validate), documentation, and mechanisms to deactivate unsafe systems. citeturn10view2turn9view1turn2search3  
**Inference:** These recur because long-horizon research work is fundamentally a *stateful search-and-critique process under external constraints*; therefore the primitives needed to control state drift, evaluator bias, and grounding failures become structurally central.  
**Rebuttal/uncertainty:** Some domains can temporarily “get away” without durable provenance or explicit stage gates in low-stakes or short-horizon tasks, but those are precisely the regimes where transfer often fails when stakes or horizons increase. citeturn7search17turn5search21  

## Source Base

### Primary sources

Primary sources here are standards, surveys, and empirical/technical works that define mechanisms or document recurring failure pressures.

- Provenance and auditability standards: entity["organization","World Wide Web Consortium","web standards body"] PROV overview and PROV-DM (entities/activities/agents; interoperability; validity constraints). citeturn13search23turn3search4turn3search8  
- Reproducibility and workflow provenance guidance: “keep track of how results were produced,” avoid manual steps, archive exact versions; scoping and best-practice reviews of workflow provenance. citeturn4search2turn13search22turn0search30  
- Risk and governance frameworks: entity["organization","National Institute of Standards and Technology","us federal agency"] AI RMF 1.0 (trustworthiness characteristics; governance functions; role separation; mechanisms to deactivate inconsistent systems). citeturn9view1turn10view2turn4search7  
- Security and boundary threats: entity["organization","OWASP","security nonprofit"] LLM Top 10 (prompt injection; insecure output handling; supply chain vulnerabilities). citeturn2search3turn2search7  
- Decomposition and hierarchical planning foundations: HTN planning formalisms and algorithms; decomposition as replacing goals with task networks; explicit decomposition trees and branching. citeturn12view0turn12view1turn1search5  
- Reason+act and tool-grounded inference: interleaving internal reasoning with external actions to reduce hallucination and propagate corrective feedback from tools/KBs. citeturn2search0turn2search4  
- Search/branching inference and selection: branch exploration over “thought units,” self-evaluation, backtracking; sampling diverse reasoning traces then selecting via consistency. citeturn2search1turn2search2  
- Self-critique / refinement loops: iterative feedback and refinement within a single model; empirical preference improvements across tasks. citeturn14search2turn7search1  
- Retrieval grounding and evaluation: RAG architecture surveys and RAG evaluation surveys emphasizing relevance, accuracy, faithfulness, and component-level metrics. citeturn1search6turn1search2  
- Hallucination and factuality: hallucination taxonomies and fact-checking/factuality evaluation surveys. citeturn7search23turn7search27turn7search35  
- Argumentation/dialectical formalisms: abstract argumentation and dialectical frameworks; acceptability semantics; generalizations. citeturn8search5turn1search3  
- Knowledge-graph foundations and scholarly KGs: surveys on knowledge graphs; scholarly knowledge graph construction and obstacles. citeturn8search0turn8search7turn8search13  
- Human-in-the-loop and interactive learning: user roles, timing, control granularity, and feedback structure in interactive ML systems. citeturn3search2turn3search6turn3search38  
- Coordination architectures: blackboard control as a governance/control pattern for selecting actions among competing knowledge sources. citeturn3search3turn3search39  
- Safety failure modes and metric gaming: reward hacking and scalable supervision; specification gaming; Goodhart/Strathern pressure. citeturn5search0turn5search28turn5search21  
- Novelty/difference preservation: quality-diversity algorithms returning archives of diverse high-quality solutions; novelty search mechanisms. citeturn0search7turn0search31turn0search15  

### Secondary sources

Secondary sources are interpretive or integrative references used for triangulation rather than mechanism definition.

- Distributed/extended cognition (scaffolding as external artifacts and social distribution over time). citeturn4search4turn4search1  
- Creativity stage models and refinements (preparation/incubation/illumination/verification; critiques and elaborations). citeturn6search25turn6search5  
- Empirical and methodological reports on scientific-agent attempts which document pipeline-stage failures and drift under implementation/evaluation constraints. citeturn0search4turn0search32  

## Ontological Family Taxonomy

This taxonomy defines each ontological family as a claim about **what research agency fundamentally is** (its “primary ontology”), plus its boundary conditions. The point is not that one is correct, but that each imports *hidden dependencies*.

### Decomposition ontology

**Definition:** research agency = *progress via partitioning* (tasks, roles, subtasks, stages), where correctness and progress are tracked through completion of structured units.  
**Boundary criterion:** if the approach cannot express “what remains” except as “next subtask,” it is decomposition-dominant.  
**Evidence base:** hierarchical task-network planning replaces goal predicates with task networks and decompositions; stage-gated agent engineering emphasizes explicit artifacts and gates. citeturn12view0turn10view0  

### Search ontology

**Definition:** research agency = *navigation of a space* (candidate hypotheses, plans, arguments, experiments, derivations), using exploration + evaluation + selection.  
**Boundary criterion:** if the system’s core competence is improved by *branching/backtracking* rather than better single-pass composition, it is search-dominant. citeturn2search1turn2search2  

### Developmental / gestational ontology

**Definition:** research agency = *growth/maturation of ideas* via incubation, differentiation, consolidation, and stabilization into “crystallized” forms.  
**Boundary criterion:** explicit protection of immature candidates and stage-appropriate evaluation thresholds is central.  
**Evidence base:** staged creativity models and later elaborations treat production as a multi-stage maturation process, not as direct optimization. citeturn6search25turn6search5  

### Deliberative / reflective ontology

**Definition:** research agency = *iterative self-critique and revision* with explicit reflection artifacts used to alter subsequent attempts.  
**Boundary criterion:** revision is the primary operator (not auxiliary); evaluation is internalized as critique/feedback.  
**Evidence base:** iterative self-feedback/refinement methods improve outputs without retraining by explicitly generating feedback then revising. citeturn14search2turn7search1  

### Dialectical / tension-preserving ontology

**Definition:** research agency = *structured transformation of disagreement*; contradictions and objections are first-class objects whose management produces epistemic progress.  
**Boundary criterion:** “conflict” is not merely noise to eliminate; it is explicitly represented and manipulated.  
**Evidence base:** abstract argumentation and dialectical frameworks treat acceptability under attack/support relations as core. citeturn8search5turn1search3  

### Selection / competitive ontology

**Definition:** research agency = *comparative survival under evaluative pressure* (competition among candidates, arguments, or trajectories).  
**Boundary criterion:** outputs are produced as *populations* and the core operator is ranking/selection.  
**Evidence base:** self-consistency selects among multiple reasoning paths; debate-style protocols frame accuracy as adversarial selection under a judge. citeturn2search2turn5search3  

### Retrieval / grounding ontology

**Definition:** research agency = *structured relation to prior work and external knowledge*, with explicit grounding links and citations as constraints.  
**Boundary criterion:** responses that do not carry grounding links are considered structurally incomplete.  
**Evidence base:** RAG surveys emphasize augmenting generation with external sources; evaluation surveys emphasize relevance/faithfulness metrics. citeturn1search6turn1search2  

### Graph / structural ontology

**Definition:** research agency = *explicit structure over relations* among concepts/claims/hypotheses/evidence/tools/consequences.  
**Boundary criterion:** “knowledge” is represented primarily as a graph of entities/relations, not as a linear narrative.  
**Evidence base:** knowledge graph surveys frame KGs as a central representational paradigm; scholarly KG work shows domain-specific constraints and obstacles. citeturn8search0turn8search7turn8search13  

### Memory / lineage ontology

**Definition:** research agency = *persistence of trajectories and histories* (states, failures, critique histories, provenance) such that future action conditions on lineage.  
**Boundary criterion:** “what happened before” is not just context; it is an auditable substrate determining validity and reuse.  
**Evidence base:** PROV defines interoperable provenance as entities/activities/agents; reproducibility rules emphasize tracking transformations and exact versions. citeturn13search23turn3search4turn4search2  

### Coordination / orchestration ontology

**Definition:** research agency = *governance of multiple interacting subprocesses* (stances, modules, roles) over time, including arbitration of control.  
**Boundary criterion:** failure is primarily a control/allocation failure rather than a reasoning failure.  
**Evidence base:** blackboard control architectures address “which action next” as fundamental; risk frameworks emphasize role separation and governance. citeturn3search3turn10view2  

### Tool / action ontology

**Definition:** research agency = *external operations as cognition* (tools, instruments, APIs, experiments), where action generates constraints and information.  
**Boundary criterion:** correctness requires tool feedback; pure text is insufficient.  
**Evidence base:** reason+act interleaving explicitly treats tool interactions as a mechanism to reduce hallucination and update plans. citeturn2search0  

### Evaluation / verifier ontology

**Definition:** research agency = *explicit judgment layers* (checking, ranking, verification) as first-class mechanisms rather than implicit preferences.  
**Boundary criterion:** unverifiable claims cannot be finalized; evaluation must be staged and criteria-bound.  
**Evidence base:** RAG evaluation surveys formalize retrieval vs generation metrics; agent evaluation surveys emphasize objectives (behavior, reliability, safety) and evaluation processes. citeturn1search2turn14search7  

### Boundary / consequence ontology

**Definition:** research agency = *constrained by consequences* (risks, downstream obligations, stakeholder acceptability), requiring explicit consequence tracing and stopping/superseding.  
**Boundary criterion:** “done” is determined by boundary satisfaction, not internal coherence.  
**Evidence base:** AI RMF defines risk in terms of probability and magnitude of consequences and emphasizes deactivation/superseding mechanisms. citeturn9view1turn10view2  

### Formalization / crystallization ontology

**Definition:** research agency = *movement from fluid exploratory representations to rigid formal objects* (formal proofs, executable workflows, auditable artifacts, schemas).  
**Boundary criterion:** progress is measured by increasing constraint satisfaction and machine-checkable structure.  
**Evidence base:** provenance and reproducibility literatures emphasize executable workflows and audit trails as the substrate for repeatability and validation. citeturn4search2turn13search23turn13search30  

### Multi-perspectival / pluralist ontology

**Definition:** research agency = *stance diversity* (multiple partial, possibly incompatible models) as a requirement for objectivity/robustness.  
**Boundary criterion:** single-perspective convergence is treated as a risk; diversity has explicit value.  
**Evidence base:** social-epistemic accounts treat transformative criticism among diverse peers as constitutive of objectivity. citeturn6search11turn6search3  

### Integrative / cross-framework ontology

**Definition:** research agency = *synthesis across heterogeneous frameworks* without premature flattening; translation and alignment are explicit work products.  
**Boundary criterion:** integration is not “summary”; it is mapping between vocabularies/assumptions and preserving residual mismatch.  
**Evidence base:** scholarly knowledge-graph efforts and provenance standards both highlight interoperability via shared vocabularies and explicit linking; obstacles illustrate why integration is nontrivial. citeturn8search13turn3search4turn13search22  

### Novelty-preservation ontology

**Definition:** research agency = *active protection of unusual candidates* against premature convergence and canon-drift.  
**Boundary criterion:** explicit diversity maintenance mechanisms (archives, delayed elimination) are present.  
**Evidence base:** quality-diversity algorithms explicitly maintain archives of diverse high-quality behaviors; novelty-search work motivates exploration beyond explicit objectives. citeturn0search7turn0search31  

### Human-judgment / oversight ontology

**Definition:** research agency = *human steering/arbitration* as a necessary component, especially under ambiguity, high stakes, or underspecified criteria.  
**Boundary criterion:** “escalation to human” is a first-class routing decision.  
**Evidence base:** interactive ML emphasizes timing, granularity, and user control; risk frameworks emphasize governance across lifecycle and role separation; stage-gated engineering emphasizes human approvals at gates. citeturn3search2turn10view2turn10view0  

### Reliability / safety ontology

**Definition:** research agency = *control against drift, hidden failure, and unsafe escalation*, requiring explicit mitigations and evaluation beyond single-run success.  
**Boundary criterion:** reliability is framed as consistency, robustness, and fault tolerance, not just “accuracy once.”  
**Evidence base:** reliability benchmarks propose repeated-run consistency, perturbation robustness, and fault tolerance; security standards enumerate prompt injection/tool misuse threats; AI safety work enumerates reward hacking and scalable supervision. citeturn7search2turn2search3turn5search0  

## Methodological Family Taxonomy

Where ontological families define **what research agency is**, methodological families define **how scaffolding is operationalized**: concrete operators, control regimes, artifact types, and evaluation couplings. Many methods instantiate multiple ontologies simultaneously.

### Planner–executor–monitor family

**Mechanism:** represent tasks/constraints → plan decomposition → execute steps (often with tools) → monitor outcomes and replan on mismatch.  
**Ontological alignment:** decomposition + tool/action + boundary/consequence.  
**Evidence anchors:** HTN decomposition and task-network execution; stage-gated agent engineering as an artifact-driven process. citeturn12view0turn10view0  

### Branch–evaluate–select family

**Mechanism:** generate multiple candidate trajectories (“thoughts,” plans, arguments) → evaluate locally/global → select/expand/backtrack.  
**Ontological alignment:** search + selection/competitive.  
**Evidence anchors:** branch-search inference over coherent thought units; sampling and selecting via consistency. citeturn2search1turn2search2  

### Generate–critique–revise family

**Mechanism:** produce candidate → produce critique/feedback → revise; repeat until stop criterion.  
**Ontological alignment:** deliberative/reflective + formalization/crystallization (when revisions tighten constraints).  
**Evidence anchors:** self-feedback refinement methods reporting improvements without retraining. citeturn14search2turn7search1  

### Debate–adversarial challenge family

**Mechanism:** produce competing arguments/claims → adversarially surface weaknesses → judge selects or synthesizes; can be human-judged or model-judged.  
**Ontological alignment:** dialectical + selection + human-oversight (when judge is human).  
**Evidence anchors:** debate protocol framing; argumentation frameworks formalizing attack/acceptability. citeturn5search3turn8search5  

### Retrieval-augmented grounding family

**Mechanism:** formulate queries → retrieve context → generate grounded output → evaluate relevance/faithfulness; optionally iterate retrieval and generation.  
**Ontological alignment:** retrieval/grounding + evaluation/verifier + memory/lineage (if citations/provenance stored).  
**Evidence anchors:** surveys on RAG architectures; surveys on RAG evaluation metrics and processes. citeturn1search6turn1search2  

### Graph-based knowledge/argument structuring family

**Mechanism:** represent claims/evidence/concepts as graph objects → query/propagate constraints → generate outputs consistent with graph relations; can integrate retrieval via graph search.  
**Ontological alignment:** graph/structural + integrative + evaluation/verifier.  
**Evidence anchors:** KG surveys; scholarly KG reviews; graph-based reasoning approaches (as evidence of methodological feasibility). citeturn8search0turn8search7turn8search15  

### Provenance-first and audit-trail family

**Mechanism:** every result is accompanied by lineage (sources, transformations, tool calls, versioned artifacts) enabling replay, dispute resolution, and accountability.  
**Ontological alignment:** memory/lineage + formalization/crystallization + reliability/safety.  
**Evidence anchors:** PROV definitions and interoperability goal; reproducibility rules emphasizing tracking workflows and versions. citeturn13search23turn4search2turn3search4  

### Stage-gated governance family

**Mechanism:** explicit phases with gate criteria; human or independent evaluators approve transitions; deactivation/superseding possible when behavior inconsistent with intended use.  
**Ontological alignment:** boundary/consequence + human oversight + reliability/safety + decomposition.  
**Evidence anchors:** lifecycle governance separation and deactivation mechanisms; stage-gated engineering methodology. citeturn9view1turn10view0turn10view2  

### Novelty maintenance / diversity control family

**Mechanism:** maintain archives/lineages; delay elimination; enforce diversity constraints; use local competition rather than global winner-take-all.  
**Ontological alignment:** novelty-preservation + selection + developmental.  
**Evidence anchors:** quality-diversity surveys and novelty search foundations emphasizing archives of diverse high-quality solutions. citeturn0search7turn0search31  

## Dependency Family Graph

This section provides an explicit dependency graph with node/edge types, then unpacks dependency families A–I.

### Node types and canonical node set

Below is the minimal node inventory used repeatedly in the graph and tables.

**Ontological family nodes (OF\*)**: OF-Decomposition, OF-Search, OF-Developmental, OF-Reflective, OF-Dialectical, OF-Competitive, OF-Retrieval, OF-Graph, OF-Memory, OF-Coordination, OF-Tool, OF-Evaluation, OF-Boundary, OF-Formalization, OF-Pluralism, OF-Integration, OF-Novelty, OF-Oversight, OF-Reliability.

**Dependency family nodes (DF\*)**: DF-A Representational; DF-B Control-flow; DF-C Epistemic; DF-D Memory; DF-E Evaluation; DF-F Coordination; DF-G Novelty; DF-H Boundary; DF-I Failure.

**Primitive family nodes (PF\*)**: PF-Decompose, PF-Plan, PF-Branch, PF-Select, PF-Retrieve, PF-ContextSelect, PF-ToolCall, PF-InterpretToolResults, PF-Reflect, PF-Critique, PF-Debate, PF-Verify, PF-Synthesize, PF-ConsequenceTrace, PF-Formalize, PF-Calibrate, PF-StageGate, PF-Stop, PF-LogProvenance, PF-FailureDetect, PF-HumanEscalate.

**Evaluation pressure nodes (EP\*)**: EP-Factuality, EP-Faithfulness, EP-Coherence, EP-Novella (novelty), EP-ExplanatoryPower, EP-Reproducibility, EP-RobustnessToReframing, EP-Security, EP-Safety, EP-Cost/Latency, EP-Traceability.

**Developmental stage nodes (ST\*)** (defined formally in the Stage Model section): ST-Frame, ST-Explore, ST-Generate, ST-Test, ST-Synthesize, ST-Crystallize, ST-Maintain.

**State-object family nodes (SO\*)**: SO-GoalSpec, SO-TaskGraph, SO-CandidateSet, SO-ClaimSet, SO-EvidenceSet, SO-CritiqueSet, SO-ArgumentGraph, SO-HypothesisSet, SO-ConsequenceSet, SO-ProvenanceRecord, SO-ToolResult, SO-LineageTree, SO-RiskRegister, SO-ConfidenceAnnotations.

**Best-practice nodes (BP\*)**: BP-StageSeparation, BP-ClaimEvidenceSeparation, BP-EvaluatorSeparation, BP-AlternativesPreserved, BP-UncertaintyMarked, BP-AuditableTransitions, BP-BoundedTools, BP-ExplicitStopCriteria, BP-FailureLogging, BP-HumanHighAmbiguityGates.

**Anti-pattern / failure-mode nodes (AP\*)**: AP-StageCollapse, AP-PrematureConvergence, AP-PrematureRanking, AP-PrematureSynthesis, AP-RetrievalDominance, AP-GraphFetishization, AP-StyleAsEvaluation, AP-HiddenPathDependence, AP-ToolSprawl, AP-UngroundedEscalation, AP-BenchmarkGaming, AP-FalseModularity, AP-CargoCultMultiAgentism, AP-UntrackedUncertainty.

**Calibration variable nodes (CV\*)**: CV-FamilySaturation, CV-BoundaryDrift, CV-DependencyCompleteness, CV-EvidenceImbalance, CV-BrandedLeakage, CV-OverformalizationDrift, CV-UnderSpecificationDrift, CV-TransferSlippage, CV-PrimitiveInflation, CV-AntiPatternBlindness, CV-StageCollapse, CV-ConfidenceInflation. (These are used as “investigation control” nodes and as “agent control” analogues when applicable.)

### Edge types and semantics

Edges are expressed as: **(source) —edge_type→ (target)** with attributes:
- **Strength:** strong / medium / weak  
- **Conditionality:** always / conditional / stage-specific  
- **Stage applicability:** which ST nodes  
- **Evidence status:** evidence-backed / inferential  

### Major edges in the dependency graph

The edge list below is intentionally “major-edge only”: it captures structural dependencies that recur across multiple sources/traditions and are needed to reconstruct the space.

1) OF-Decomposition —requires→ DF-A Representational  
- Strength: strong; Conditionality: always; Stage: ST-Frame→ST-Test; Evidence-backed (task networks/tasks as representational substrate). citeturn12view0turn10view0  

2) OF-Decomposition —requires→ DF-B Control-flow  
- strong; always; ST-Frame→ST-Test; evidence-backed (decomposition ordering/expansion control). citeturn12view1turn12view0  

3) OF-Search —requires→ PF-Branch  
- strong; always; ST-Explore→ST-Test; evidence-backed (search over candidate “thoughts”). citeturn2search1  

4) OF-Search —requires→ PF-Select  
- strong; always; ST-Explore→ST-Test; evidence-backed (self-evaluation/backtracking; selection). citeturn2search1turn2search2  

5) OF-Reflective —requires→ SO-CritiqueSet  
- strong; always; ST-Generate→ST-Test; evidence-backed (feedback artifacts and revisions). citeturn14search2turn7search1  

6) OF-Dialectical —requires→ SO-ArgumentGraph  
- strong; always; ST-Explore→ST-Synthesize; evidence-backed (attack/acceptability semantics require explicit arguments/relations). citeturn8search5turn1search3  

7) OF-Competitive —amplifies→ AP-PrematureRanking  
- medium; conditional; ST-Explore; inferential (selection pressure easily collapses diversity unless novelty controls exist); supported by Goodhart/spec-gaming general pressure. citeturn5search21turn5search28turn0search7  

8) OF-Retrieval —requires→ PF-Retrieve  
- strong; always; ST-Frame→ST-Test; evidence-backed (RAG architecture premise). citeturn1search6  

9) OF-Retrieval —requires→ DF-E Evaluation  
- strong; always; ST-Test; evidence-backed (RAG evaluation decomposes relevance/faithfulness). citeturn1search2turn7search23  

10) OF-Tool —enables→ DF-H Boundary  
- strong; conditional; ST-Test; evidence-backed (tool feedback provides boundary contact). citeturn2search0  

11) OF-Tool —amplifies→ DF-I Failure  
- strong; conditional; ST-Test→ST-Maintain; evidence-backed (prompt injection/tool misuse threats in tool-using apps). citeturn2search3turn2search7  

12) OF-Memory —requires→ SO-ProvenanceRecord  
- strong; conditional; ST-Test→ST-Maintain; evidence-backed (provenance models and reproducibility rules). citeturn13search23turn4search2turn3search4  

13) OF-Coordination —requires→ PF-StageGate  
- medium; stage-specific; ST-Frame→ST-Crystallize; evidence-backed (control architectures distinguish governance problems; lifecycle role separation). citeturn3search3turn10view2  

14) OF-Reliability —requires→ BP-EvaluatorSeparation  
- strong; always; ST-Test→ST-Maintain; evidence-backed (role separation and V&V as best practice). citeturn10view2turn7search2  

15) OF-Reliability —requires→ PF-FailureDetect  
- strong; always; ST-Test→ST-Maintain; evidence-backed (reliability evaluation includes robustness and fault tolerance). citeturn7search2turn14search7  

16) OF-Boundary —requires→ SO-RiskRegister  
- medium; conditional; ST-Frame→ST-Maintain; evidence-backed (risk framed as probability × consequence; governance across lifecycle). citeturn9view1turn4search7  

17) BP-ClaimEvidenceSeparation —mitigates→ AP-StyleAsEvaluation  
- medium; always; ST-Test→ST-Crystallize; inferential but strongly warranted by hallucination/factuality evidence and provenance needs. citeturn7search23turn13search23  

18) BP-AlternativesPreserved —protects-from→ AP-PrematureConvergence  
- strong; stage-specific; ST-Explore; evidence-backed by novelty/QD archive rationale. citeturn0search7turn0search31  

19) BP-BoundedTools —mitigates→ AP-ToolSprawl  
- strong; conditional; ST-Test→ST-Maintain; evidence-backed by OWASP threat categories and governance framings. citeturn2search3turn9view1  

20) AP-BenchmarkGaming —collapses-into→ AP-StyleAsEvaluation  
- medium; conditional; ST-Test; inferential; backed by Goodhart pressure and agent-eval caveats (static eval loopholes). citeturn5search21turn7search17  

### Dependency families A–I as explicit requirements

Each dependency family is defined as a *type of enabling condition* that must be satisfied for an ontological family to function as intended.

- **DF-A Representational:** what objects must exist. (E.g., task graphs, claim/evidence objects, arguments and attacks, provenance records). citeturn3search4turn12view0turn8search5  
- **DF-B Control-flow:** sequencing, recurrence, branching and gatekeeping. (E.g., decompose→execute; diverge→converge; critique→commit; retrieve→synthesize). citeturn2search1turn12view1turn14search2  
- **DF-C Epistemic:** what counts as warrant/pressure. (e.g., faithfulness to sources, reproducibility, robustness, novelty). citeturn1search2turn4search2turn0search7  
- **DF-D Memory:** what persists (state, critique history, failed paths, tool results). citeturn13search23turn4search2turn14search2  
- **DF-E Evaluation:** what is judged, by what criteria, and by whom. citeturn14search7turn1search2turn7search2  
- **DF-F Coordination:** how stances/modules interact; separation vs integration. citeturn3search3turn10view2turn3search2  
- **DF-G Novelty:** mechanisms to prevent premature elimination and canon drift. citeturn0search7turn0search31turn7search3  
- **DF-H Boundary:** outside pressure (evidence contact, tool feedback, human challenge, downstream obligations). citeturn2search0turn9view1turn3search2  
- **DF-I Failure:** predictable failure modes if dependencies are missing (premature convergence, retrieval conservatism, evaluator bias, tool misuse). citeturn7search23turn2search3turn5search28turn5search21  

## Primitive Taxonomy

This taxonomy identifies recurrent **primitives** that act as reusable “operators” across families. Each primitive is described by: function; presuppositions; family membership; conflicts; stage fit; and common degeneration (anti-pattern).

### PF-Decompose

**Does:** partitions objectives into subtasks/roles/stages; creates a task graph.  
**Presupposes:** SO-GoalSpec or SO-TaskGraph; DF-B control-flow for ordering; DF-E evaluation for “done.” citeturn12view0turn10view0  
**Belongs to:** decomposition, coordination, formalization.  
**Conflicts with:** novelty-preservation (if decomposition forces early commitments).  
**Best stage:** ST-Frame and ST-Generate.  
**Degenerates into:** AP-FalseModularity (pretending tasks are independent when dependencies are hidden). citeturn12view1turn5search21  

### PF-Plan

**Does:** selects an execution order and tool strategy.  
**Presupposes:** task graph; tool affordances; boundary matching; cost constraints. citeturn2search0turn12view1  
**Belongs to:** decomposition, tool/action, boundary.  
**Conflicts with:** reflective approaches if the plan becomes rigid (graph rigidity).  
**Best stage:** ST-Frame→ST-Test.  
**Degenerates into:** AP-OverformalizationDrift / brittle plans (stage mismatch). citeturn13search30turn7search17  

### PF-Branch

**Does:** creates multiple candidate trajectories/solutions.  
**Presupposes:** candidate representation; evaluation to prune; memory to avoid repeats. citeturn2search1turn2search2  
**Belongs to:** search, novelty, selection.  
**Conflicts with:** tight cost constraints; too much branching increases tool sprawl.  
**Best stage:** ST-Explore and ST-Generate.  
**Degenerates into:** AP-ToolSprawl or uncontrolled combinatorics. citeturn7search17turn2search3  

### PF-Select

**Does:** ranks/prunes candidates; decides what survives.  
**Presupposes:** explicit criteria; evaluator integrity; avoidance of Goodhart collapse. citeturn2search2turn5search21  
**Belongs to:** selection/competitive, evaluation/verifier.  
**Conflicts with:** novelty-preservation if applied too early/strong.  
**Best stage:** late ST-Explore through ST-Test.  
**Degenerates into:** AP-StyleAsEvaluation or AP-PrematureRanking. citeturn5search21turn7search23  

### PF-Retrieve

**Does:** fetches external context; produces evidence candidates.  
**Presupposes:** corpora/index; query formulation; evaluation of relevance/authority. citeturn1search6turn1search2  
**Belongs to:** retrieval/grounding, tool/action.  
**Conflicts with:** novelty-preservation when retrieval bias dominates (canon lock-in).  
**Best stage:** ST-Frame→ST-Test.  
**Degenerates into:** AP-RetrievalDominance (substituting “retrieved” for “true/adequate”). citeturn1search2turn0search7  

### PF-ContextSelect

**Does:** chooses which retrieved/tool states to condition on.  
**Presupposes:** memory store; salience/relevance metrics; latency budgets. citeturn1search2turn14search7  
**Belongs to:** retrieval, coordination, reliability.  
**Conflicts with:** naive coherence pressure (over-pruning contradictory evidence).  
**Best stage:** ST-Explore→ST-Test.  
**Degenerates into:** AP-HiddenPathDependence (context choices invisibly determine outcomes). citeturn4search2turn13search23  

### PF-Reflect

**Does:** generates meta-level assessment of trajectory; identifies errors and revisions.  
**Presupposes:** critique objects; memory to store reflections; evaluation signals. citeturn14search2turn0search33  
**Belongs to:** deliberative/reflective, developmental.  
**Conflicts with:** strong external verifier regimes if reflection substitutes for checking.  
**Best stage:** ST-Generate→ST-Test.  
**Degenerates into:** AP-RhetoricalSelfCritique (fluent critique without corrective action). citeturn7search23turn5search21  

### PF-Critique

**Does:** produces structured objections, inconsistencies, missing evidence lists.  
**Presupposes:** explicit claim/evidence separation; standards for relevance. citeturn7search23turn8search5  
**Belongs to:** dialectical, evaluation.  
**Conflicts with:** novelty-preservation when critique is applied with “publish-level” thresholds too early.  
**Best stage:** ST-Test and early ST-Synthesize.  
**Degenerates into:** AP-StageCollapse (treating exploration as if it must already be final). citeturn6search25turn7search17  

### PF-Debate

**Does:** adversarially surfaces weaknesses; forces explicit warrants and rebuttals.  
**Presupposes:** stance separation; judge; shared objects (arguments, evidence). citeturn5search3turn8search5  
**Belongs to:** dialectical, selection, oversight.  
**Conflicts with:** coherence-only evaluation (debate can reward persuasion).  
**Best stage:** ST-Test→ST-Synthesize.  
**Degenerates into:** AP-RhetoricalSelection (winning by style). citeturn5search21turn7search23  

### PF-Verify

**Does:** checks claims against sources, tools, or formal constraints; outputs pass/fail plus diagnostics.  
**Presupposes:** verifier criteria; tool access; provenance capture. citeturn1search2turn4search2turn13search23  
**Belongs to:** evaluation/verifier, reliability/safety.  
**Conflicts with:** novelty-preservation if applied as a hard filter too early.  
**Best stage:** ST-Test and ST-Crystallize.  
**Degenerates into:** AP-BenchmarkGaming (verifying proxies rather than truth). citeturn5search21turn7search17  

### PF-Synthesize

**Does:** integrates across candidates/perspectives into a coherent structure; preserves traceable links.  
**Presupposes:** multiple candidates; mapping relations; stop criteria. citeturn8search0turn13search23  
**Belongs to:** integrative, pluralist, formalization.  
**Conflicts with:** dialectical tension-preservation if synthesis erases residual conflict.  
**Best stage:** ST-Synthesize.  
**Degenerates into:** AP-PrematureSynthesis (flattening disagreement to narrative). citeturn6search11turn7search23  

### PF-ConsequenceTrace

**Does:** enumerates downstream implications, risks, and decision impacts; updates risk register.  
**Presupposes:** explicit boundary/goal model; stakeholder constraints. citeturn9view1turn4search7  
**Belongs to:** boundary/consequence, reliability.  
**Conflicts with:** pure search (if consequences are ignored, search is misaligned).  
**Best stage:** ST-Test→ST-Crystallize.  
**Degenerates into:** AP-SterileElegance (beautiful consequence narratives without evidence contact). citeturn5search21turn7search23  

### PF-Formalize

**Does:** converts results into rigid artifacts (schemas, executable workflows, provenance graphs, formal claims).  
**Presupposes:** stable representations; provenance requirements; reproducibility tenets. citeturn13search30turn13search23turn4search2  
**Belongs to:** formalization/crystallization, memory/lineage.  
**Conflicts with:** developmental/novelty when done too early.  
**Best stage:** ST-Crystallize and ST-Maintain.  
**Degenerates into:** AP-PrematureFormalization; graph rigidity. citeturn6search25turn8search13  

### PF-Calibrate

**Does:** attaches confidence/uncertainty annotations; checks reliability (calibration).  
**Presupposes:** probabilistic or ordinal confidence scheme; evaluation data; reliability metrics. citeturn5search6turn7search2  
**Belongs to:** evaluation, reliability/safety.  
**Conflicts with:** style-based evaluation (confidence becomes rhetorical).  
**Best stage:** ST-Test→ST-Maintain.  
**Degenerates into:** AP-UntrackedUncertainty (confidence implied but not measured). citeturn7search2turn7search23  

### PF-StageGate and PF-Stop

**Does:** controls transitions between stages; enforces stopping criteria; supports deactivation/superseding.  
**Presupposes:** explicit criteria; governance roles; risk tolerance; provenance logs. citeturn10view2turn9view1turn4search2  
**Belongs to:** coordination, boundary, reliability, oversight.  
**Conflicts with:** unconstrained exploratory creativity (if gates are mis-specified).  
**Best stage:** all stages (as control overlay), especially ST-Test→ST-Crystallize.  
**Degenerates into:** AP-StageCollapse (over-gating early) or AP-NoStoppingCriteria (under-gating late). citeturn7search17turn5search21  

### PF-LogProvenance and PF-FailureDetect

**Does:** records lineage and detects accumulating failure (drift, injections, unverifiable claims).  
**Presupposes:** provenance schema; storage/query; threat models. citeturn13search23turn2search3turn4search2  
**Belongs to:** memory/lineage, reliability/safety.  
**Conflicts with:** none in principle; conflicts are practical (cost, complexity).  
**Best stage:** ST-Test→ST-Maintain.  
**Degenerates into:** AP-ChecklistsWithoutEnforcement (logs exist but do not gate decisions). citeturn9view1turn5search21  

## Best-Practice Families

Best practices are treated here as *recurrent dependency bundles*—patterns repeatedly implied by mechanism papers, standards, and failure analyses. They are not axioms; each has conditions and failure cases.

### Explicit stage separation

**Claim:** separating exploration, critique/testing, and crystallization reduces stage collapse and evaluator contamination.  
**Evidence:** stage-gated engineering formalizes human approvals at gates; risk management frameworks emphasize lifecycle stages and governance as cross-cutting; interactive ML emphasizes timing and granularity of human input. citeturn10view0turn10view2turn3search2  
**Common failure if absent:** AP-StageCollapse (exploration penalized as if final; verification delayed until too late). citeturn7search17turn0search4  

### Claim/evidence separation with traceable grounding

**Claim:** treating claims and evidence as distinct objects (with links) mitigates hallucination-style failure where fluent text masquerades as warrant.  
**Evidence:** hallucination surveys emphasize factuality/faithfulness failures; RAG evaluation emphasizes faithfulness to retrieved sources; provenance defines audit trails for assessing trustworthiness. citeturn7search23turn1search2turn13search23  

### Evaluator separation and independence

**Claim:** separating generator and evaluator roles reduces bias and “style collapse” where evaluation becomes preference mimicry.  
**Evidence:** AI RMF explicitly notes separation of those building/using models from those verifying/validating as best practice; agent-eval surveys emphasize evaluation process design. citeturn10view2turn14search7  

### Preservation of alternatives via diversity controls

**Claim:** explicit alternative preservation prevents early convergence artifacts and supports novelty maturation.  
**Evidence:** quality-diversity methods return archives of diverse high-quality behaviors; novelty search motivates exploration beyond objective proxies. citeturn0search7turn0search31  

### Bounded tool use and threat-aware boundaries

**Claim:** tool access must be bounded, logged, and sandboxed because tool-using agents expand the attack surface and create failure compounding.  
**Evidence:** OWASP lists prompt injection and insecure handling among top risks; agent-eval discussions emphasize compounded mistakes; AI RMF emphasizes governance and deactivation mechanisms. citeturn2search3turn7search17turn9view1  

### Auditable state transitions and provenance-first logging

**Claim:** provenance of artifacts, tool calls, and transformations is a prerequisite for reproducibility and for dispute resolution when contradictions arise.  
**Evidence:** PROV defines an interoperable model explicitly for assessments of quality/reliability/trustworthiness; reproducibility rules emphasize tracking how each result was produced and archiving versions. citeturn13search23turn4search2turn3search4  

### Explicit stopping conditions and superseding/deactivation

**Claim:** agents require explicit stop/supersede conditions to avoid unbounded iteration, over-optimization, or unsafe escalation.  
**Evidence:** AI RMF includes mechanisms to supersede/disengage/deactivate systems inconsistent with intended use; Goodhart pressure and specification gaming indicate why unchecked optimization drifts. citeturn9view1turn5search28turn5search21  

## Anti-Pattern Families

Anti-patterns are treated as **predictable degeneration paths** when dependencies are missing or misaligned. Each anti-pattern is also a graph phenomenon: it is a collapse of nodes/edges that should remain separated.

### Stage collapse

**Mechanism:** critique/verification thresholds applied during unconstrained exploration; or exploration tolerated during finalization without verification.  
**Damage:** loss of novelty (over-pruning) or unsafe/incorrect final outputs (under-checking).  
**Evidence anchors:** agent evaluations emphasize compounding errors; stage-gated frameworks exist precisely to prevent phase confusion. citeturn7search17turn10view0turn10view2  

### Premature convergence and premature ranking

**Mechanism:** selection pressure applied before diversity maturation; winner-take-all promotion.  
**Damage:** brittle solutions; loss of surprising hypotheses; path dependence.  
**Evidence anchors:** novelty/QD rationales; Goodhart pressure as selection metric becomes target. citeturn0search7turn0search31turn5search21  

### Premature synthesis

**Mechanism:** integration performed as narrative smoothing rather than mapping incompatibilities.  
**Damage:** hides unresolved contradictions; “false coherence.”  
**Evidence anchors:** pluralist/dialectical objectivity norms emphasize transformative criticism among diverse stances. citeturn6search11turn8search5  

### Retrieval dominance

**Mechanism:** retrieval judged by surface relevance; authoritative but non-obvious evidence excluded; novelty suppressed.  
**Damage:** canon lock-in; false grounding; missed edge cases.  
**Evidence anchors:** RAG evaluation surveys note retrieval and faithfulness as separate concerns; hallucination/factuality surveys stress faithfulness failures. citeturn1search2turn7search23  

### Graph fetishization

**Mechanism:** building elaborate graphs without reliable typing, provenance, or update discipline.  
**Damage:** rigidity, high maintenance cost, false certainty from structure.  
**Evidence anchors:** obstacles in scholarly KG construction; provenance literature emphasizes validity constraints and extensibility points. citeturn8search13turn3search4turn13search3  

### Evaluator collapse into style preference

**Mechanism:** evaluation rewards rhetorical polish or self-consistency of prose rather than external warrant.  
**Damage:** overconfident falsehoods; debate degenerates to persuasion.  
**Evidence anchors:** hallucination literature (fluent but ungrounded outputs); Goodhart/target-measure collapse; debate safety discussions motivating structured protocols and judges. citeturn7search23turn5search21turn5search3  

### Uncontrolled tool sprawl and boundary breaches

**Mechanism:** agents call tools opportunistically without bounded policies or provenance; injection attacks and misuse become feasible.  
**Damage:** data exfiltration, unsafe actions, irreproducible results.  
**Evidence anchors:** OWASP risk categories; AI RMF governance emphasis; agent eval discussions of compounding tool mistakes. citeturn2search3turn9view1turn7search17  

### Benchmark-led overfitting and gaming

**Mechanism:** optimizing to evaluation harness quirks rather than real objectives; selection pressure collapses evaluation validity (Goodhart).  
**Damage:** brittle transfer; misleading confidence.  
**Evidence anchors:** Goodhart framing; agent-eval narratives about loopholes and evaluation sensitivity. citeturn5search21turn7search17  

## Stage Model

This stage model is not a prescribed architecture—it is a **dependency alignment lens**: which families/primitives tend to be appropriate at which developmental stages, and why.

### Stage definitions (ST\*)

**ST-Frame:** define the problem space, constraints, evaluation criteria, and boundary conditions (what “counts”).  
Evidence base: scoping and governance frameworks treat framing as explicit; risk frameworks define risk, harms, and lifecycle governance. citeturn9view1turn14search1  

**ST-Explore:** maximize breadth of candidate hypotheses/approaches; defer hard selection; preserve novelty.  
Evidence base: novelty/QD emphasizes archives and diversity; creativity models emphasize incubation and preparation before verification. citeturn0search7turn6search25  

**ST-Generate:** produce candidate artifacts (claims, hypotheses, outlines, experiments, tool plans).  
Evidence base: decomposition and planning methods; reflective generation loops. citeturn12view0turn14search2  

**ST-Test:** verification, critique, tool contact, adversarial challenge, grounding checks; error discovery.  
Evidence base: RAG evaluation metrics; hallucination/factuality and agent reliability emphasize testing beyond single-run. citeturn1search2turn7search2turn7search23  

**ST-Synthesize:** integrate across surviving candidates and perspectives; represent disagreement explicitly where unresolved.  
Evidence base: argumentation frameworks; pluralist objectivity claims; KG-based integration needs. citeturn8search5turn6search11turn8search0  

**ST-Crystallize:** formalize into stable, auditable artifacts (provenance graphs, executable workflows, explicit claims with warrants).  
Evidence base: reproducibility rules; provenance standards; workflow tenets. citeturn4search2turn13search23turn13search30  

**ST-Maintain:** monitor drift, update corpora/tools, rerun evaluations, manage security risks and supply chain issues.  
Evidence base: AI RMF governance across lifecycle; OWASP risks; reliability metrics including robustness and fault tolerance. citeturn9view1turn2search3turn7search2  

### Stage-family alignment heuristic (non-prescriptive)

- ST-Explore is where **novelty-preservation, developmental, search** families are beneficial but **evaluation/verifier** must be “lightweight and non-terminal” or it collapses the stage. citeturn0search7turn6search25turn5search21  
- ST-Test is where **evaluation/verifier, tool/action, boundary** become load-bearing; otherwise hallucination and compounding tool errors dominate. citeturn7search23turn2search0turn7search17  
- ST-Crystallize is where **memory/lineage and formalization** become non-optional if reproducibility and auditability are requirements. citeturn13search23turn4search2  

## Family-by-Family Analysis

The analyses below follow a uniform template: agency-as; presuppositions (objects, memory, control-flow, evaluation); developmental ordering; blind spots; drift failure mode; key dependencies (foundational/conditional/optional/antagonistic/substitutable/stage-specific); reliance on primitives; best-fit stages; conflicts; adversarial audit; confidence.

### Decomposition ontology

**Agency-as:** progress by partitioning and completing structured units (tasks/roles/stages).  
**Presupposed objects:** SO-GoalSpec, SO-TaskGraph, SO-ToolResult, SO-ProvenanceRecord (conditional). citeturn12view0turn10view0turn4search2  
**Control-flow:** decompose → order → execute → monitor; recurrence via replanning when subtasks fail. citeturn12view1turn12view0  
**Evaluation pressures:** completion criteria, constraint satisfaction, cost, and boundary fit (often under-specified without explicit verifier family). citeturn9view1turn14search7  
**Developmental ordering:** ST-Frame→ST-Generate (dominant), then ST-Test.  
**Blind spot:** hidden coupling across subtasks; “unknown unknowns” that aren’t named in the decomposition. citeturn12view1turn5search0  
**Natural drift/failure:** AP-FalseModularity and AP-StageCollapse (treating decomposition as sufficient for correctness).  
**Dependencies (classification):** DF-A foundational; DF-B foundational; DF-E conditional (needed when stakes rise); DF-D conditional; DF-H conditional; DF-G optional.  
**Primitives:** PF-Decompose, PF-Plan, PF-StageGate, PF-Stop, PF-LogProvenance.  
**Best-fit stages:** ST-Frame, ST-Generate.  
**Conflicts:** with novelty-preservation when decomposition forces early elimination; with dialectical when disagreement isn’t representable as a “task.”  
**Adversarial audit:** strongest objection = decomposition encodes a worldview of the task; hidden assumption = the “right” partition is available; likely failure = brittle pipelines; over-application risk = treating complex epistemic uncertainty as project management.  
**Confidence:** high (mechanisms clearly evidenced in planning and stage-gated methodology). citeturn12view0turn10view0  

### Search ontology

**Agency-as:** navigation of candidate/action spaces via branching, evaluation, and backtracking.  
**Objects:** SO-CandidateSet, SO-HypothesisSet, local scores/heuristics; optional SO-LineageTree. citeturn2search1turn2search2  
**Control-flow:** branch → evaluate → expand/prune; explicit backtracking. citeturn2search1  
**Epistemic pressures:** heuristic adequacy, coherence constraints, sometimes external correctness; vulnerable to proxy mismatch. citeturn5search21turn5search28  
**Memory:** must store explored branches or suffer loops; conditional on horizon. citeturn7search2turn4search2  
**Evaluation:** foundational (search needs scoring); evaluator bias is a major dependency. citeturn2search1turn14search7  
**Ordering:** ST-Explore→ST-Test.  
**Blind spot:** “search over what?”—if representation is wrong, search amplifies error efficiently.  
**Drift:** AP-PrematureConvergence if selection pressure high; AP-BenchmarkGaming if eval harness is proxy. citeturn5search21turn7search17  
**Dependencies:** DF-E foundational; DF-A foundational; DF-D conditional; DF-G stage-specific (for novelty regimes); DF-H conditional.  
**Primitives:** PF-Branch, PF-Select, PF-Calibrate, PF-Stop.  
**Conflicts:** with gestational ontology if selection pressures eliminate immature novelty.  
**Adversarial audit:** objection = search can be computationally explosive; hidden assumption = evaluators are meaningful; likely failure = optimizing proxies; over-application = treating research as solvable via local heuristics alone.  
**Confidence:** high (explicitly demonstrated in branch-based inference methods and selection mechanisms). citeturn2search1turn2search2  

### Developmental / gestational ontology

**Agency-as:** maturation of ideas through incubation/differentiation/verification; time and protection are operators.  
**Objects:** SO-LineageTree, SO-CandidateSet with maturity levels; SO-CritiqueSet as “growth signals.” citeturn6search25turn14search2  
**Control-flow:** stage transitions with delayed evaluation; “protected incubation” loops. citeturn6search25turn0search7  
**Epistemic pressures:** novelty potential, consequence richness, eventual formalizability.  
**Memory:** foundational (growth requires persistence of partials).  
**Evaluation:** stage-specific: light early, strict late. citeturn6search25turn7search17  
**Ordering:** ST-Explore→ST-Generate→ST-Test→ST-Crystallize.  
**Blind spot:** can protect incoherence too long (“incubation as excuse”).  
**Drift:** AP-IncoherenceProtection (subset of premature synthesis avoidance gone wrong).  
**Dependencies:** DF-D foundational; DF-G foundational; DF-E stage-specific; DF-H conditional.  
**Primitives:** PF-Branch, PF-AlternativesPreserved (BP), PF-StageGate, PF-Stop.  
**Conflicts:** with competitive ontology early; with verifier ontology if verification is applied prematurely.  
**Adversarial audit:** objection = can waste resources; hidden assumption = maturity correlates with eventual value; likely failure = endless incubation; over-application = treating all domains as creative ideation.  
**Confidence:** medium (stage models are well-supported in creativity/process literature, but transfer to scientific-agent scaffolding is inferential). citeturn6search25turn0search7  

### Deliberative / reflective ontology

**Agency-as:** iterative self-critique and revision; the agent is its own editor.  
**Objects:** SO-CritiqueSet, SO-CandidateSet versions; optional SO-ProvenanceRecord for revision history. citeturn14search2turn4search2  
**Control-flow:** generate → feedback → revise → repeat. citeturn14search2  
**Epistemic pressures:** internal consistency and adherence to constraints; factuality depends on grounding. citeturn7search23turn1search2  
**Memory:** reflections must persist to matter; otherwise the loop is amnesiac. citeturn0search33turn14search2  
**Evaluation:** can be internal (self-feedback) but must be externally anchored for factuality. citeturn7search23turn1search2  
**Ordering:** ST-Generate→ST-Test.  
**Blind spot:** self-evaluation can become self-affirmation; “critic” and “generator” collapse.  
**Drift:** AP-RhetoricalSelfCritique; AP-StyleAsEvaluation.  
**Dependencies:** DF-E foundational; DF-H conditional (for grounding); DF-D conditional; DF-F optional (unless multi-stance).  
**Primitives:** PF-Reflect, PF-Critique, PF-Verify (conditional), PF-Stop.  
**Conflicts:** with strict evaluator separation unless implemented as separate stance/modules. citeturn10view2turn3search3  
**Adversarial audit:** objection = self-feedback can plateau or drift; hidden assumption = the model can reliably assess its own errors; likely failure = polishing without correcting; over-application = using reflection as a substitute for evidence.  
**Confidence:** high for mechanism existence; medium for reliability in scientific domains without grounding. citeturn14search2turn7search23  

### Dialectical / tension-preserving ontology

**Agency-as:** progress by articulating, attacking, defending, and transforming competing claims/frames.  
**Objects:** SO-ArgumentGraph with attack/support relations; SO-CritiqueSet; SO-EvidenceSet. citeturn8search5turn1search3  
**Control-flow:** propose → challenge → rebut → update acceptability; may converge to a stable extension (or preserve multiple). citeturn8search5turn1search3  
**Epistemic pressures:** defeasibility, relevance, burden of proof, robustness under objections.  
**Memory:** histories of objections and resolutions are load-bearing.  
**Evaluation:** foundational; requires criteria for acceptability and relevance.  
**Ordering:** ST-Explore→ST-Synthesize; also ST-Test.  
**Blind spot:** can reward persuasion or endless dispute; needs boundary contact to avoid purely verbal equilibria.  
**Drift:** AP-RhetoricalSelection; AP-EndlessDebate.  
**Dependencies:** DF-A foundational; DF-E foundational; DF-H conditional; DF-F conditional (stance separation); DF-G optional.  
**Primitives:** PF-Debate, PF-Critique, PF-Verify, PF-Synthesize.  
**Conflicts:** with early formalization if disagreement is prematurely “compiled away.”  
**Adversarial audit:** objection = high complexity; hidden assumption = argument structures correspond to truth-tracking; likely failure = rhetorical equilibria; over-application = treating empirical disputes as purely dialectical.  
**Confidence:** high for formal mechanism; medium for empirical truth-tracking without tool/evidence coupling. citeturn8search5turn2search0  

### Selection / competitive ontology

**Agency-as:** candidate populations compete; selection pressure yields progress.  
**Objects:** populations, rankings, fitness/score functions; SO-LineageTree (optional) for evolutionary style. citeturn2search2turn0search7  
**Control-flow:** generate many → score → select → iterate.  
**Epistemic pressures:** score validity; vulnerable to Goodhart/spec-gaming. citeturn5search21turn5search28  
**Memory:** archives can stabilize diversity or accelerate convergence (path dependence). citeturn0search7turn4search2  
**Evaluation:** foundational and most dangerous dependency.  
**Ordering:** ST-Explore→ST-Test.  
**Blind spot:** the scoring function is an ontology of value; often hidden.  
**Drift:** AP-BenchmarkGaming; AP-PrematureConvergence.  
**Dependencies:** DF-E foundational; DF-G conditional (to prevent collapse); DF-D conditional; DF-H conditional.  
**Primitives:** PF-Branch, PF-Select, PF-Calibrate, PF-Stop.  
**Conflicts:** with novelty-preservation when global competition eliminates diversity.  
**Adversarial audit:** objection = evaluates proxies; hidden assumption = fitness captures value; likely failure = reward hacking/spec gaming; over-application = optimizing measurable metrics in domains requiring judgment.  
**Confidence:** high. citeturn0search7turn5search28turn2search2  

### Retrieval / grounding ontology

**Agency-as:** progress by linking claims to external sources and inherited vocabularies; grounding is structural.  
**Objects:** SO-EvidenceSet with citations; retrieval queries; authority metadata where available. citeturn1search6turn1search2  
**Control-flow:** retrieve → generate → evaluate faithfulness; often iterative. citeturn1search2  
**Epistemic pressures:** relevance, authority, faithfulness; tension between coverage and noise. citeturn1search2turn7search23  
**Memory:** retrieved context must be tracked; provenance essential to audit. citeturn13search23turn4search2  
**Evaluation:** foundational (component-level evaluation). citeturn1search2  
**Ordering:** ST-Frame→ST-Test.  
**Blind spot:** retrieval distributions bias toward popular/available sources; can suppress novelty.  
**Drift:** AP-RetrievalDominance; “false grounding” (citing irrelevant sources).  
**Dependencies:** DF-A foundational; DF-E foundational; DF-H foundational (boundary to corpora); DF-D conditional; DF-G antagonistic unless explicitly managed.  
**Primitives:** PF-Retrieve, PF-ContextSelect, PF-Verify, PF-LogProvenance.  
**Conflicts:** with novelty preservation; with dialectical when retrieval is treated as adjudication rather than evidence.  
**Adversarial audit:** objection = authority is domain-dependent; hidden assumption = corpora are accurate and sufficient; likely failure = citation laundering; over-application = equating “retrieved” with “true.”  
**Confidence:** high. citeturn1search2turn7search23  

### Graph / structural ontology

**Agency-as:** represent research as a structured network of relations; reasoning is graph operations.  
**Objects:** concept/claim/evidence graphs; typed relations; identifiers; mapping layers. citeturn8search0turn8search13  
**Control-flow:** graph construction/refinement → query/inference → update; requires maintenance discipline. citeturn8search13turn13search23  
**Epistemic pressures:** consistency constraints, provenance validity, interoperability. citeturn3search4turn8search13  
**Memory:** foundational (graph is persistent memory).  
**Evaluation:** validation of edges/nodes; fact-checking. citeturn8search25turn13search23  
**Ordering:** ST-Explore→ST-Maintain (structure is long-lived).  
**Blind spot:** false precision; rigid schemas can erase ambiguity.  
**Drift:** AP-GraphFetishization; schema lock-in.  
**Dependencies:** DF-A foundational; DF-D foundational; DF-E conditional; DF-H conditional; DF-G optional.  
**Primitives:** PF-Formalize, PF-Synthesize, PF-LogProvenance, PF-Verify.  
**Conflicts:** with developmental stages if formalization is premature; with pluralism if schema enforces a single taxonomy.  
**Adversarial audit:** objection = expensive to build/maintain; hidden assumption = stable ontologies exist; likely failure = stale graphs; over-application = building graphs as a substitute for solving epistemic uncertainty.  
**Confidence:** high for representational role; medium for universal applicability across domains. citeturn8search0turn8search13  

### Memory / lineage ontology

**Agency-as:** progress is path-dependent; outcomes are justified by lineage artifacts and replayability.  
**Objects:** provenance records (entities/activities/agents), versioned workflows, critique histories. citeturn13search23turn3search4turn4search2  
**Control-flow:** write/read/update memory; replay; audit queries (“how produced?”). citeturn4search2turn3search4  
**Epistemic pressures:** reproducibility, traceability, trustworthiness. citeturn13search23turn4search2  
**Evaluation:** audits rely on lineage; evaluators need access to provenance.  
**Ordering:** ST-Test→ST-Maintain is where it becomes non-optional.  
**Blind spot:** memory can ossify bad assumptions (path dependence).  
**Drift:** AP-HiddenPathDependence; archival bias.  
**Dependencies:** DF-D foundational; DF-A foundational; DF-E conditional; DF-H conditional; DF-G optional.  
**Primitives:** PF-LogProvenance, PF-FailureDetect, PF-StageGate.  
**Conflicts:** with speed/cost constraints.  
**Adversarial audit:** objection = overhead; hidden assumption = people/tools will actually record; likely failure = incomplete logs; over-application = excessive logging without enforcement.  
**Confidence:** high. citeturn13search23turn4search2  

### Coordination / orchestration ontology

**Agency-as:** governance of multiple stances/modules; action selection under uncertainty is the core problem.  
**Objects:** roles, stance definitions, arbitration rules, shared workspace (blackboard-like). citeturn3search3turn10view2  
**Control-flow:** allocate tasks to modules; resolve conflicts; schedule evaluators.  
**Epistemic pressures:** coherence across modules, avoidance of interference, auditability.  
**Memory:** shared memory and boundaries between private/public states. citeturn3search3turn4search2  
**Evaluation:** separation of evaluator roles is critical. citeturn10view2  
**Ordering:** overlay across all stages; especially ST-Test and ST-Maintain.  
**Blind spot:** over-centralization can become bottleneck; false modularity.  
**Drift:** AP-OvercentralizedOrchestration; AP-CargoCultMultiAgentism. citeturn7search29turn3search3  
**Dependencies:** DF-F foundational; DF-B foundational; DF-D conditional; DF-E conditional.  
**Primitives:** PF-StageGate, PF-HumanEscalate, PF-FailureDetect.  
**Conflicts:** with simplicity; with some reflective single-agent loops that rely on role collapse.  
**Adversarial audit:** objection = complexity; hidden assumption = interfaces are stable; likely failure = coordination overhead; over-application = “more agents” as a substitute for evaluation design.  
**Confidence:** medium-high (strong historical basis; modern agent transfer partly inferential). citeturn3search3turn14search7  

### Tool / action ontology

**Agency-as:** cognition includes external operations; tool feedback constrains belief.  
**Objects:** tool schemas, action logs, tool results; security policies. citeturn2search0turn2search3  
**Control-flow:** decide tool vs think; handle tool errors; iterate; integrate results. citeturn2search0turn7search2  
**Epistemic pressures:** empirical adequacy via tool feedback; fault tolerance. citeturn7search2turn7search17  
**Memory:** must persist tool results and versions; provenance essential. citeturn13search23turn4search2  
**Evaluation:** tool correctness + outcome correctness; robust to tool failures. citeturn7search2turn14search7  
**Ordering:** ST-Test dominates; also ST-Maintain.  
**Blind spot:** tool outputs can be wrong or adversarial; “tool = truth” fallacy. citeturn2search3turn7search17  
**Drift:** AP-ToolSprawl; AP-PromptInjectionCascade.  
**Dependencies:** DF-H foundational; DF-I foundational; DF-E conditional; DF-D conditional.  
**Primitives:** PF-ToolCall, PF-InterpretToolResults, PF-BoundedTools, PF-LogProvenance.  
**Conflicts:** with unbounded autonomy in high-risk settings without governance.  
**Adversarial audit:** objection = security and reliability burdens; hidden assumption = tools are stable and correct; likely failure = injection/misuse; over-application = allowing tool calls without stage gates.  
**Confidence:** high. citeturn2search0turn2search3  

### Evaluation / verifier ontology

**Agency-as:** explicit judgment layers are primary; “trust” is produced by evaluation structure.  
**Objects:** criteria, test cases, verification artifacts, confidence annotations. citeturn1search2turn7search2turn5search6  
**Control-flow:** evaluate before commit; re-evaluate under perturbations; repeated-run reliability. citeturn7search2turn7search17  
**Epistemic pressures:** factuality/faithfulness, robustness, safety, reproducibility. citeturn7search23turn4search2turn9view1  
**Memory:** store evaluation results/drift; tie to provenance. citeturn13search23turn7search2  
**Ordering:** ST-Test→ST-Maintain.  
**Blind spot:** verifiers can be biased or gameable; evaluation becomes target (Goodhart). citeturn5search21turn7search17  
**Drift:** AP-BenchmarkGaming; AP-StyleAsEvaluation.  
**Dependencies:** DF-E foundational; DF-A conditional; DF-D conditional; DF-H conditional.  
**Primitives:** PF-Verify, PF-Calibrate, PF-FailureDetect, PF-Stop.  
**Conflicts:** with novelty-preservation early; with reflective loops if evaluator collapse occurs.  
**Adversarial audit:** objection = expensive; hidden assumption = criteria reflect real goals; likely failure = proxy gaming; over-application = verifying what is easy rather than what matters.  
**Confidence:** high. citeturn7search2turn5search21turn1search2  

### Boundary / consequence ontology

**Agency-as:** controlled by external consequences and risk; not just internal coherence.  
**Objects:** consequence sets, risk registers, downstream obligations, stakeholder constraints. citeturn9view1turn4search7  
**Control-flow:** consequence tracing before finalization; deactivation/superseding. citeturn9view1  
**Epistemic pressures:** harm magnitude/likelihood, acceptability, compliance and security. citeturn9view1turn2search3  
**Memory:** persistent risk decisions and provenance.  
**Ordering:** ST-Frame and ST-Maintain.  
**Blind spot:** consequence models are often incomplete; can paralyze action.  
**Drift:** AP-Overconservatism or AP-UngroundedEscalation if risk is ignored. citeturn9view1turn2search3  
**Dependencies:** DF-H foundational; DF-E conditional; DF-D conditional.  
**Primitives:** PF-ConsequenceTrace, PF-StageGate, PF-HumanEscalate, PF-Stop.  
**Conflicts:** with pure novelty preservation if consequences are high-stakes early.  
**Adversarial audit:** objection = difficult to specify; hidden assumption = consequences are foreseeable; likely failure = miscalibrated risk; over-application = imposing high-stakes governance on low-stakes exploratory work.  
**Confidence:** medium-high. citeturn9view1turn4search7  

### Formalization / crystallization ontology

**Agency-as:** turning fluid exploration into rigid, checkable, reusable structure.  
**Objects:** formal claims, executable workflows, provenance graphs, schemas. citeturn4search2turn13search23turn13search30  
**Control-flow:** formalize late; validate; archive; reuse.  
**Epistemic pressures:** reproducibility, determinacy, interoperability. citeturn13search23turn13search30  
**Memory:** foundational (formal artifacts are durable memory).  
**Ordering:** ST-Crystallize.  
**Blind spot:** formalization can hide uncertainty; premature rigidity.  
**Drift:** AP-PrematureFormalization; AP-GraphRigidity. citeturn6search25turn8search13  
**Dependencies:** DF-D foundational; DF-A foundational; DF-E conditional; DF-H conditional.  
**Primitives:** PF-Formalize, PF-LogProvenance, PF-Verify, PF-Stop.  
**Conflicts:** with developmental novelty early.  
**Adversarial audit:** objection = cost; hidden assumption = domain can be formalized; likely failure = brittle formal artifacts; over-application = making formal outputs the goal rather than a tool.  
**Confidence:** high for reproducibility contexts; medium for conceptual science contexts. citeturn4search2turn13search30  

### Multi-perspectival / pluralist ontology

**Agency-as:** objectivity and robustness arise from diverse stances with transformative criticism.  
**Objects:** stance sets, dissent logs, critique channels, alternative models. citeturn6search11turn3search2  
**Control-flow:** maintain plurality; cross-critique; delayed synthesis.  
**Epistemic pressures:** robustness under reframing, bias detection, explanatory breadth. citeturn6search11turn9view1  
**Memory:** store dissent and critiques to prevent convergence erasure.  
**Ordering:** ST-Explore→ST-Synthesize.  
**Blind spot:** can become indecision; needs stage gates for closure.  
**Drift:** AP-EndlessPluralism (no crystallization).  
**Dependencies:** DF-F foundational; DF-G conditional; DF-E conditional; DF-D conditional.  
**Primitives:** PF-Branch, PF-Debate, PF-Synthesize, PF-StageGate.  
**Conflicts:** with single-metric competitive selection; with premature synthesis.  
**Adversarial audit:** objection = coordination overhead; hidden assumption = diversity is available and meaningful; likely failure = noise masquerading as plurality; over-application = pluralism without boundary tests.  
**Confidence:** medium (strong philosophical grounding; operational translation depends on evaluation and governance). citeturn6search11turn10view2  

### Integrative / cross-framework ontology

**Agency-as:** map and reconcile heterogeneous frameworks while preserving residual mismatch.  
**Objects:** mapping artifacts, ontology alignments, translation rules, merged graphs with provenance. citeturn8search13turn13search23  
**Control-flow:** align vocabularies → test compatibility → integrate with traceability.  
**Epistemic pressures:** interoperability, explanatory power, robustness across contexts. citeturn8search13turn3search4  
**Memory:** store mappings and their validity ranges.  
**Ordering:** ST-Synthesize→ST-Crystallize.  
**Blind spot:** can flatten genuine incommensurability; overfit mappings.  
**Drift:** AP-PrematureSynthesis; AP-GraphFetishization (integration as graph-building). citeturn8search13turn6search11turn3search4  
**Dependencies:** DF-A foundational; DF-D foundational; DF-E conditional; DF-F conditional.  
**Primitives:** PF-Synthesize, PF-Formalize, PF-LogProvenance.  
**Conflicts:** with dialectical preservation when integration erases tensions.  
**Adversarial audit:** objection = heavy engineering; hidden assumption = mappings stabilize; likely failure = brittle interoperability; over-application = forcing integration where pluralism is appropriate.  
**Confidence:** medium. citeturn8search13turn3search4  

### Novelty-preservation ontology

**Agency-as:** protect novel candidates from early elimination; maintain diversity archives.  
**Objects:** archives, novelty metrics, local competition mechanisms. citeturn0search7turn0search31  
**Control-flow:** generate diverse → evaluate locally → maintain archive.  
**Epistemic pressures:** novelty and quality (balanced). citeturn0search7turn0search15  
**Memory:** archive is foundational.  
**Ordering:** ST-Explore.  
**Blind spot:** novelty can become an end; relevance may drift.  
**Drift:** AP-NoveltyForItsOwnSake; uncontrolled divergence.  
**Dependencies:** DF-G foundational; DF-E conditional; DF-D foundational.  
**Primitives:** PF-Branch, PF-Select (local), PF-StageGate (delayed elimination).  
**Conflicts:** with competitive global ranking early; with strict verifiers early.  
**Adversarial audit:** objection = resource use; hidden assumption = novelty correlates with value; likely failure = irrelevant diversity; over-application = novelty pressure in constrained engineering tasks.  
**Confidence:** high. citeturn0search7turn0search31  

### Human-judgment / oversight ontology

**Agency-as:** human steering/arbitration is necessary for ambiguity and high-stakes thresholds.  
**Objects:** escalation triggers, approval artifacts, interaction logs. citeturn3search2turn10view0turn10view2  
**Control-flow:** route to human at gates; human sets criteria and resolves disputes.  
**Epistemic pressures:** acceptability, domain norms, value judgments. citeturn3search2turn9view1  
**Memory:** retains human decisions as constraints.  
**Ordering:** all stages, especially ST-Frame and ST-Crystallize.  
**Blind spot:** human bandwidth; inconsistent judgments.  
**Drift:** AP-HumanAsRubberStamp or AP-OverrelianceOnHuman.  
**Dependencies:** DF-F foundational; DF-E foundational; DF-B conditional; DF-D conditional.  
**Primitives:** PF-HumanEscalate, PF-StageGate, PF-Stop.  
**Conflicts:** with full autonomy; with purely internal self-critique loops.  
**Adversarial audit:** objection = cost and bottleneck; hidden assumption = human can judge; likely failure = inconsistent gating; over-application = excessive human gating at low stakes.  
**Confidence:** high. citeturn3search2turn10view0turn10view2  

### Reliability / safety ontology

**Agency-as:** safe and reliable operation requires explicit controls against drift, injection, reward hacking, and evaluation failure.  
**Objects:** risk registers, security policies, reliability metrics, incident logs. citeturn9view1turn2search3turn7search2  
**Control-flow:** monitor, evaluate robustness, fault tolerance, deactivate/supersede. citeturn7search2turn9view1  
**Epistemic pressures:** trustworthiness characteristics; reliability defined as ability to perform as required; security and resilience. citeturn9view1turn2search3  
**Memory:** incident history and provenance for audits. citeturn13search23turn4search2  
**Ordering:** ST-Test→ST-Maintain.  
**Blind spot:** can become overly conservative; can incentivize benchmark gaming. citeturn5search21turn7search17  
**Drift:** AP-ComplianceTheater (procedures exist without real control).  
**Dependencies:** DF-I foundational; DF-H foundational; DF-E foundational; DF-D conditional; DF-F conditional.  
**Primitives:** PF-FailureDetect, PF-Calibrate, PF-BoundedTools, PF-StageGate, PF-Stop, PF-LogProvenance.  
**Conflicts:** with unconstrained novelty; with early-stage fluid exploration if same thresholds are applied.  
**Adversarial audit:** objection = cost/complexity; hidden assumption = risks are known; likely failure = unmodeled threats; over-application = imposing high-assurance controls everywhere.  
**Confidence:** high. citeturn9view1turn2search3turn5search0turn7search2  

## Dependency Tables

Notation used in tables:

- **F = foundational** (cannot function without it)  
- **C = conditional** (required under certain regimes: long horizon, high stakes, tool use, etc.)  
- **O = optional** (helpful but not required)  
- **S = stage-specific** (load-bearing only in certain stages)  
- **A = antagonistic** (tends to undermine unless carefully managed)  
- **Sub = substitutable** (another dependency/family can sometimes replace it)

These tables are compact “graph projections.” They do not encode all edges; they encode repeated dependency classifications implied by the mechanism base and standards cited throughout. citeturn14search7turn13search23turn2search3turn0search7  

### Family vs dependency families (A–I)

| Ontological family | DF-A Rep | DF-B Flow | DF-C Epistemic | DF-D Memory | DF-E Eval | DF-F Coord | DF-G Novelty | DF-H Boundary | DF-I Failure |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Decomposition | F | F | C | C | C | C | O | C | C |
| Search | F | F | C | C | F | O | S | C | C |
| Developmental | C | C | C | F | S | C | F | C | C |
| Reflective | C | C | C | C | F | O/Sub | A (if over-prunes novelty) | C | C |
| Dialectical | F | C | C | C | F | C | O | C | C |
| Competitive | F | C | C | C | F | O | C (mitigates collapse) | C | F (gaming risk) |
| Retrieval | F | C | F (faithfulness) | C | F | O | A (canon lock-in) | F | C |
| Graph/Structural | F | C | C | F | C | C | O | C | C |
| Memory/Lineage | F | C | C | F | C | O | O | C | C |
| Coordination | C | F | C | C | C | F | O | C | C |
| Tool/Action | C | C | C | C | C | O | O | F | F |
| Evaluation/Verifier | C | C | F | C | F | C | A (if early) | C | F |
| Boundary/Consequence | C | C | F | C | C | C | A (if high-stakes early) | F | C |
| Formalization/Crystallization | F | C | C | F | C | O | A (if early) | C | C |
| Pluralist | C | C | C | C | C | F | C | C | C |
| Integrative | F | C | C | F | C | C | A (if flattening) | C | C |
| Novelty-preservation | C | C | C | F | C | C | F | C | C |
| Oversight | C | C | C | C | F | F | S | C | C |
| Reliability/Safety | C | C | F | C | F | C | S | F | F |

### Family vs primitives (selected core set)

| Family | Decompose | Branch | Select | Retrieve | Reflect/Critique | Debate | Verify | Synthesize | Formalize | StageGate/Stop | Provenance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Decomposition | F | O | C | C | O | O | C | C | C | C | C |
| Search | C | F | F | O | C | O | C | C | O | C | C |
| Developmental | C | F | C | O | C | O | C | C | S | F | C |
| Reflective | C | C | C | C | F | O | C | C | C | C | C |
| Dialectical | O | C | C | C | F | F | C | C | O | C | C |
| Competitive | O | F | F | O | O | C | C | O | O | C | C |
| Retrieval | O | O | C | F | C | O | F | C | C | C | F |
| Graph/Structural | C | C | C | C | C | C | C | F | F | C | F |
| Memory/Lineage | O | O | O | O | C | O | C | C | C | C | F |
| Coordination | C | C | C | C | C | C | C | C | C | F | C |
| Tool/Action | O | C | C | C | C | O | C | C | O | C | C |
| Evaluation/Verifier | O | C | F | C | C | C | F | C | C | F | C |
| Boundary/Consequence | C | O | C | C | C | C | C | C | C | F | C |
| Formalization | C | O | C | C | C | O | C | F | F | C | F |
| Pluralist | O | F | C | C | F | F | C | F | C | C | C |
| Integrative | C | C | C | C | C | C | C | F | F | C | F |
| Novelty-preservation | O | F | C (local) | O | O | O | A (early) | C | A (early) | C | C |
| Oversight | C | O | C | C | C | C | C | C | C | F | C |
| Reliability/Safety | C | C | C | C | C | C | F | C | C | F | F |

### Family vs anti-pattern risk (dominant drifts)

| Family | Dominant anti-patterns if under-supported |
|---|---|
| Decomposition | False modularity; stage collapse; hidden dependencies |
| Search | Premature convergence; proxy gaming; combinatorial sprawl |
| Developmental | Endless incubation; incoherence protection; lack of stopping |
| Reflective | Rhetorical self-critique; evaluator collapse; polishing errors |
| Dialectical | Rhetorical selection; endless debate; no boundary contact |
| Competitive | Premature ranking; benchmark gaming; Goodhart collapse |
| Retrieval | Retrieval dominance; citation laundering; canon lock-in |
| Graph/Structural | Graph fetishization; schema lock-in; false precision |
| Memory/Lineage | Hidden path dependence; unusable logs; archival bias |
| Coordination | Overcentralization; cargo-cult multi-agentism; brittle interfaces |
| Tool/Action | Tool sprawl; injection cascades; irreproducible tool states |
| Evaluation/Verifier | Proxy fixation; style as evaluation; verifier bias |
| Boundary/Consequence | Overconservatism; ungrounded escalation; paralysis |
| Formalization | Premature formalization; rigidity; loss of ambiguity |
| Pluralist | Endless plurality; synthesis avoidance; coordination overload |
| Integrative | Premature synthesis; flattening incompatibilities; graph fetishization |
| Novelty-preservation | Novelty for its own sake; divergence; lack of relevance |
| Oversight | Human rubber-stamping; bottlenecks; inconsistent gating |
| Reliability/Safety | Compliance theater; overfitting to controls; blind spots |

### Family vs stage suitability (dominant fit)

| Family | Primary stages |
|---|---|
| Decomposition | Frame, Generate |
| Search | Explore, Test |
| Developmental | Explore, Generate, Synthesize |
| Reflective | Generate, Test |
| Dialectical | Explore, Test, Synthesize |
| Competitive | Explore (late), Test |
| Retrieval | Frame, Test |
| Graph/Structural | Synthesize, Crystallize, Maintain |
| Memory/Lineage | Test, Crystallize, Maintain |
| Coordination | All (overlay), especially Test/Maintain |
| Tool/Action | Test, Maintain |
| Evaluation/Verifier | Test, Maintain |
| Boundary/Consequence | Frame, Maintain |
| Formalization | Crystallize, Maintain |
| Pluralist | Explore, Synthesize |
| Integrative | Synthesize, Crystallize |
| Novelty-preservation | Explore |
| Oversight | Frame, Crystallize, Maintain |
| Reliability/Safety | Test, Maintain |

### Primitive vs failure modes (selected)

| Primitive | Common failure modes it collapses into |
|---|---|
| Decompose | False modularity; dependency blindness |
| Branch | Tool sprawl; runaway cost |
| Select | Premature ranking; style-as-eval; Goodhart collapse |
| Retrieve | Retrieval dominance; false grounding |
| Reflect/Critique | Rhetorical critique; no corrective action |
| Debate | Rhetorical selection; persuasion equilibrium |
| Verify | Proxy-checking; benchmark gaming |
| Synthesize | Premature synthesis; flattening tensions |
| Formalize | Premature rigidity; loss of ambiguity |
| StageGate/Stop | Stage collapse (over-gating) or no stopping (under-gating) |
| Provenance logging | Checklist theater; unusable audit trails |

## Strongest Structural Tensions

These tensions are “deep” in the sense that they arise from antagonistic edges in the dependency graph, not from missing engineering details.

### Novelty versus verification

- **Tension:** novelty-preservation requires delaying elimination; verifier regimes want early hard filters.  
- **Why unresolved:** selection pressure improves reliability in easy-to-check tasks but can destroy value in tasks where novelty must mature; quality-diversity resolves this partly via local competition and archives but translating that to scientific reasoning under evidence constraints remains open. citeturn0search7turn0search31turn7search2  

### Internal critique versus evaluator independence

- **Tension:** reflective loops reuse the same model as generator and critic; governance frameworks recommend separating builders and verifiers. citeturn14search2turn10view2  
- **Why unresolved:** independence improves epistemic integrity but increases cost/complexity; many systems fall back to self-critique which can drift into rhetorical evaluation. citeturn7search23turn5search21  

### Retrieval grounding versus retrieval conservatism

- **Tension:** grounding reduces hallucination risk, but retrieval bias anchors the system to canon and availability. citeturn1search6turn7search23turn0search7  
- **Why unresolved:** determining “authority” and “relevance” is domain- and context-dependent; evaluation metrics only partially capture this. citeturn1search2turn8search13  

### Structured graphs versus ambiguity tolerance

- **Tension:** graph/structural and crystallization ontologies push toward rigid objects; developmental and pluralist ontologies require ambiguity and partial models. citeturn8search13turn6search25turn6search11  

### Metric pressure versus truth-tracking

- **Tension:** any evaluation regime becomes a target (Goodhart/Strathern), inviting gaming and proxy optimization. citeturn5search21turn5search28turn7search17  
- **Why unresolved:** the more consequential the evaluation, the more incentive to game; “robust” evaluation requires diversity of tests and continual renewal, raising costs. citeturn7search2turn14search7  

### Tool empowerment versus boundary security

- **Tension:** tool/action ontologies give boundary contact and corrective feedback, but expand security risks (prompt injection, unsafe actions). citeturn2search0turn2search3  
- **Why unresolved:** bounding tools reduces capability; unbounded tools increase attack surface and irreproducibility; governance must be stage- and risk-sensitive. citeturn9view1turn2search3  

## Open Problems and Unknowns

### Mechanism-level open problems

**Verifier reliability for open-ended research**: Verifiers and evals are better-defined for narrow tasks; for research outputs (multi-claim, multi-source, multi-stage), evaluation remains fragmented and gameable. citeturn14search7turn7search17turn5search21  

**Grounding beyond retrieval**: retrieval helps, but authority, disagreement, and non-text evidence (experiments, instruments) require richer boundary contact, provenance, and domain-specific validation. citeturn2search0turn13search23turn4search2  

**Novelty under constraint**: how to preserve radical candidates while still enforcing safety and empirical adequacy (a “quality-diversity under scientific verification” problem). citeturn0search7turn7search2turn9view1  

**Provenance granularity and cost**: provenance is widely advocated, but what granularity is necessary and sufficient for research-agent auditability without drowning the system in overhead remains unsettled. citeturn13search22turn3search4turn4search2  

**Stage-sensitive governance design**: explicit stage gates are advocated, but formal methods for choosing gate criteria and thresholds (especially for “high ambiguity” triggers) are under-developed. citeturn10view0turn9view1turn3search2  

### Transfer-discipline unknowns (what does not transfer cleanly)

**Search methods → scientific discovery:** search over “thoughts” transfers as a control regime, but scientific discovery requires boundary contact and epistemic warrant structures that purely textual search lacks. citeturn2search1turn2search0turn4search2  

**Quality-diversity → research ideation:** diversity preservation transfers as a mechanism, but descriptors/novelty metrics for “idea space” are not stable and can be gamed or bias toward weirdness. citeturn0search7turn5search21  

**Argumentation formalisms → empirical science:** formal acceptability is useful for structuring objections, but empirical adequacy requires tool/experiment coupling and provenance. citeturn8search5turn2search0turn13search23  

## Omission Audit

### What this map explicitly did to reduce omissions

- **Multiple search passes across adjacent traditions**: planning/HTN decomposition, provenance/workflow reproducibility, RAG grounding and evaluation, hallucination/factuality, argumentation/dialectics, human-in-the-loop design, security/risk governance, novelty/QD. citeturn12view0turn13search23turn1search6turn7search23turn8search5turn3search2turn2search3turn0search7  
- **Evidence imbalance check (CV-EvidenceImbalance):** included both capability-promoting methods and failure/governance literatures (OWASP, AI RMF, Goodhart/spec gaming). citeturn2search3turn9view1turn5search21turn5search28  
- **Dependency completeness check (CV-DependencyCompleteness):** every family analysis included representational, control-flow, memory, evaluation, boundary, and failure considerations, not just “what it outputs.” citeturn14search7turn13search23turn7search2  
- **Branded-system leakage check (CV-BrandedLeakage):** named systems/papers were used only as evidence anchors; organizing categories remained ontological/methodological families.

### What may still be missing (and why)

**Domain-specific scientific method regimes** (e.g., wet-lab automation, clinical trials, field science) were only lightly sampled; while tool/action and provenance generalize, domain-specific validation norms may require additional family splits (e.g., “instrumentation ontology” vs generic tool use). citeturn2search0turn13search22turn0search8  

**Mathematical formal proof and program synthesis regimes** were treated as part of formalization/crystallization but not deeply audited as separate ontological families; this may under-represent cases where “formalization” is not just an end-stage but the whole process. citeturn13search30turn4search2  

**Socio-technical incentive structures in science** (beyond Goodhart pressure) likely deserve an expanded boundary ontology, but were out of scope beyond the core metric-gaming and governance references. citeturn5search21turn9view1  

### Omission-resistance checklist (explicit)

- Organized by families rather than named systems: **Yes**.  
- Separated ontological families from methodological families: **Yes**.  
- Mapped dependencies, not just outputs: **Yes** (DF-A–I + edge list + tables).  
- Identified primitives beyond architectures: **Yes** (PF list).  
- Included best practices and anti-patterns: **Yes** (BP/AP sections + drift in each family).  
- Included stage-sensitive analysis: **Yes** (ST model + stage suitability table).  
- Included positive and negative evidence: **Yes** (capability methods + safety/security + provenance + Goodhart).  
- Marked inference vs direct support: **Partially** (explicit in key claims/edges; some family-level generalizations remain inferential).  
- Failure-mode pass for every major family: **Yes** (drift/anti-pattern in each).  
- Preserved ambiguity where evidence does not justify cleanup: **Yes** (confidence tags; noted unresolved tensions).  
- Identified unresolved tensions rather than claiming completeness: **Yes**.

## Final Synthesis

### The dependency graph in one compact statement

**Agentic scaffolding for research/scientific agents is best understood as a staged, stateful search-and-critique process that must remain grounded to boundary contact (tools/corpora/experiments) while preserving novelty and pluralism long enough for maturation—under governance constraints that prevent metric gaming, tool sprawl, and unsafe escalation.** citeturn2search1turn14search2turn1search6turn13search23turn0search7turn2search3turn9view1turn5search21  

### Core primitives that appear genuinely load-bearing

Across sources spanning planning, evaluation, provenance, and safety, the repeatedly load-bearing primitives are:

- **Explicit state objects** (claims/evidence/tasks/provenance) and **durable memory/provenance** (SO-\* + PF-LogProvenance). citeturn13search23turn4search2turn3search4  
- **Branching + selection** as the canonical exploration operator (PF-Branch, PF-Select), with explicit controls for diversity and Goodhart pressure. citeturn2search1turn2search2turn0search7turn5search21  
- **Critique/verification separation** (PF-Critique/PF-Verify) plus evaluator independence where stakes require it. citeturn10view2turn1search2turn7search2  
- **Grounding via retrieval/tool feedback** (PF-Retrieve/PF-ToolCall/PF-InterpretToolResults) combined with boundary-aware threat controls. citeturn2search0turn1search6turn2search3  
- **Stage gates and stopping rules** (PF-StageGate/PF-Stop) to prevent stage collapse and unsafe escalation, including deactivation/superseding mechanisms in high-risk regimes. citeturn9view1turn10view0turn7search17  

### Best practices that recur and why

- **Stage separation + gatekeeping** recurs because it prevents the single largest systemic error: applying the wrong epistemic standard at the wrong time (stage collapse). citeturn10view0turn10view2turn7search17  
- **Claim–evidence–provenance separation** recurs because it is the minimal defense against fluent ungrounded generation (hallucination) and is a prerequisite for reproducibility and audit. citeturn7search23turn13search23turn4search2  
- **Evaluator separation and robustness testing** recur because evaluation is itself a failure surface (gaming, bias, inconsistency) and must be treated as an engineered subsystem. citeturn10view2turn7search2turn5search21  
- **Bounded tool use** recurs because tool access both enables factual correction and massively expands security risk; thus it must be logged, sandboxed, and policy-bound. citeturn2search0turn2search3turn9view1  

### Anti-patterns that recur and what they damage

- **Premature ranking/synthesis** damages novelty and pluralist robustness; it collapses the graph by eliminating alternative lineages before maturation. citeturn0search7turn6search25turn6search11  
- **Retrieval dominance** damages genuine inquiry by replacing epistemic judgment with availability bias. citeturn1search2turn8search13  
- **Tool sprawl and injection cascades** damage safety, privacy, and reproducibility (expanded attack surface + compounded state errors). citeturn2search3turn7search17  
- **Benchmark gaming under Goodhart pressure** damages real-world transfer and makes “evaluation” adversarial rather than truth-tracking. citeturn5search21turn7search17  

### Unresolved tensions that remain deepest

The space does not converge on a single dominant ontology because several tensions are structurally real: novelty vs verification, self-critique vs evaluator independence, retrieval grounding vs conservatism, graph formalization vs ambiguity tolerance, and tool empowerment vs boundary security. citeturn0search7turn1search2turn10view2turn2search3turn5search21