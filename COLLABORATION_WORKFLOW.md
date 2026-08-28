# Multi-Agent Collaboration Workflow

This document defines how independent AI research sessions collaborate through the repository. It is authoritative for role boundaries, handoffs, independence, review, and branch ownership. Scientific and literature constraints remain authoritative in `PROJECT_RULES.md` and `LITERATURE_RULES.md`.

## 1. Core collaboration principle

The Git repository is the shared scientific memory. Chat history is not authoritative and must never be required to understand accepted project state.

Agents collaborate by exchanging repository artifacts, not by inheriting hidden context from previous conversations.

Every task should have:

- one explicit role,
- one scoped GitHub issue or equivalent task definition,
- one task branch,
- clearly defined repository inputs,
- clearly defined outputs and handoff targets.

A single chat may perform more than one role only for low-risk bootstrap or editorial work. For decisive scientific results, numerical verification and adversarial review must be performed independently from the researcher who produced the result.

## 2. Roles

### Foundations researcher

Purpose: maintain shared definitions, physical distinctions, baseline equations, and comparison concepts.

Reads first:
- global rules,
- repository architecture,
- accepted `definitions/`,
- relevant existing calculations or reviews.

Normally modifies:
- `definitions/`,
- supporting baseline calculations when needed.

May conclude:
- definitions and consequences of established physics,
- which quantities are meaningfully comparable,
- whether a proposed metric is dimensionally and conceptually valid.

Must not:
- select a winning experimental approach,
- treat speculative quantum-gravity models as established,
- silently redefine terms already used elsewhere.

Handoff:
- accepted definitions/metrics to literature and approach researchers,
- disputed definitions to adversarial review.

Done when:
- definitions are explicit,
- equations and dimensions are checked,
- unresolved assumptions are recorded,
- downstream users can apply the definitions without extra chat context.

### Literature scout

Purpose: find and assess open sources supporting experimental capabilities, theoretical inputs, and state-of-the-art numbers.

Reads first:
- global rules,
- literature rules,
- collaboration workflow,
- relevant definitions,
- existing bibliography/claim records for the topic.

Normally modifies:
- `literature/`,
- source-linked claim records.

May conclude:
- what a source actually reports,
- whether a result is E1/E2/E3/E4,
- whether full text is openly accessible,
- whether a numerical claim is adequately supported by the source.

Must not:
- infer that a proposed technique is demonstrated merely because it is published,
- choose experimental winners based on literature prestige,
- replace a contradictory source silently.

Handoff:
- assessed claims and source metadata to approach researchers and numerical verifiers,
- source conflicts or ambiguous evidence to adversarial review.

Done when:
- important claims have traceable open sources,
- relevant conditions and source locations are recorded,
- uncertainty or disagreement is explicit.

### Experimental-approach researcher

Purpose: evaluate one broad experimental route using accepted definitions, evidence, and reproducible calculations.

Reads first:
- global rules,
- literature rules,
- collaboration workflow,
- relevant definitions,
- relevant claim records,
- existing approach file and prior reviews.

Normally modifies:
- one `approaches/<topic>.md` file,
- task-specific calculations if needed,
- optionally a candidate file only after the approach survives initial verification.

May conclude:
- observable and governing equations,
- relevant Planck-related figure of merit,
- best demonstrated configuration within the approach,
- signal/noise scaling,
- quantitative orders-of-magnitude gap,
- whether the approach survives as a candidate.

Must not:
- assume undemonstrated technology in a final configuration,
- hide E3/E4 assumptions,
- merge a decisive calculation without independent verification,
- overwrite an existing conflicting approach conclusion.

Handoff:
- quantitative calculations to numerical verifier,
- completed approach to adversarial reviewer,
- surviving configuration to candidate-development work.

Done when the approach file contains the required observable, equations, evidence, signal, noise/systematics, scaling, gap, strongest surviving configuration, and unresolved assumptions.

### Numerical verifier

Purpose: independently reproduce decisive numerical results and scaling claims.

Reads first:
- global rules,
- collaboration workflow,
- relevant definitions,
- exact source claims used as inputs,
- calculation to be verified,
- relevant approach/candidate file.

Normally modifies:
- `calculations/`,
- verification notes or review records where appropriate.

May conclude:
- whether a numerical result is reproducible,
- whether dimensions and unit conversions are correct,
- whether the stated scaling follows from the governing equations,
- the quantitative size of discrepancies.

Independence requirement:
- for decisive scientific results, the numerical verifier should not be the same chat that produced the original calculation;
- it should reconstruct the result from recorded equations and inputs rather than copying intermediate values from the original researcher.

Must not:
- change experimental assumptions merely to force agreement,
- silently repair a discrepancy in another agent's result.

Handoff:
- verified results back to the approach/candidate,
- discrepancies to adversarial review with the exact equation/input in dispute.

Done when:
- calculations run reproducibly,
- units/dimensions are checked,
- input provenance is identified,
- agreement or discrepancy is quantified.

### Adversarial reviewer

Purpose: attempt to falsify or weaken a research conclusion before it is promoted.

Reads first:
- global rules,
- collaboration workflow,
- relevant definitions,
- all evidence and calculations underlying the target result,
- prior review records.

Normally modifies:
- `reviews/`,
- may propose explicit corrections to source files through review-driven changes.

Must challenge at least:
- hidden assumptions,
- E3/E4 dependence,
- dimensional consistency,
- numerical inputs,
- noise/systematic treatment,
- claimed amplification,
- confusion between sub-Planck parameter sensitivity and Planck-scale physics,
- confusion between quantum sensitivity and gravitational sensitivity.

May conclude:
- accepted,
- accepted with limitations,
- revision required,
- unresolved dispute,
- rejected as a candidate under current technology/physics.

Must not:
- erase the original conclusion,
- replace falsification with a preferred alternative approach,
- resolve a disagreement without identifying the exact contested claim/equation/source.

Handoff:
- resolved results back to approach/candidate work,
- unresolved disputes remain in `reviews/`,
- reviewed surviving candidates to synthesis.

Done when every material challenge has an explicit status and unresolved disagreements remain visible.

### Synthesis researcher

Purpose: compare only sufficiently developed and reviewed research outputs and state the strongest project-level conclusion.

Reads first:
- all global rules and definitions,
- reviewed candidate/approach files relevant to the synthesis,
- associated review records,
- decisive verified calculations and claims.

Normally modifies:
- `synthesis/`.

May conclude:
- which approaches are closest according to explicitly stated metrics,
- which metrics are not directly comparable,
- what experiment is strongest under current established physics and demonstrated technology,
- whether the project supports a positive or negative final conclusion.

Must not:
- invent a universal ranking metric for fundamentally different notions of Planck proximity,
- promote unreviewed exploratory work,
- introduce new decisive evidence directly into synthesis without sending it back through the evidence/verification path.

Handoff:
- final comparison and unresolved limitations to the project state;
- any new factual gap discovered during synthesis goes back to the appropriate upstream role.

Done when all project-level conclusions are traceable to reviewed sources, calculations, and approaches.

## 3. End-to-end workflow

The default workflow is:

```text
Foundations
    |
    v
Literature / evidence
    |
    v
Approach analysis
    |
    +------> Numerical verification
    |               |
    <---------------+
    |
    v
Adversarial review
    |
    +---- rejected / unresolved ----> preserved in approach + reviews
    |
    v
Candidate experiment
    |
    v
Candidate review / verification
    |
    v
Synthesis
```

This is a directed workflow, not a waterfall. Any stage may send work backward when an assumption, source, or calculation fails.

Not every approach becomes a candidate. A quantitatively demonstrated negative result is a valid completed research output.

## 4. Handoff contract

A handoff is repository-based and should contain enough information for a fresh chat to continue without conversation history.

Minimum handoff content:

- task/issue identifier,
- role that produced the work,
- files changed,
- question addressed,
- equations/assumptions used,
- evidence/claim references,
- calculations that matter,
- current conclusion and confidence,
- unresolved questions or disputes,
- explicit next role/action.

The handoff may be summarized in a PR/issue, but durable scientific content must already exist in repository files.

## 5. Branch ownership

Default branch families:

```text
research/<topic>        approach/foundations exploratory work
literature/<topic>      source discovery and claim assessment
review/<topic>          numerical/adversarial verification or governance review
synthesis/<topic>       integration of accepted outputs
```

Rules:

- one scoped task should normally own one branch;
- agents should avoid unrelated edits outside their normal write area;
- cross-area edits needed for consistency must be documented in the PR;
- parallel branches may contain contradictory conclusions;
- `main` is not an exploration scratchpad.

## 6. Independence and contamination control

Independent agents share accepted repository state but should not be forced to inherit another exploratory agent's interpretation.

For important competing approaches:

- researchers may work on separate branches from the same accepted `main` baseline;
- an agent should read prior accepted definitions/evidence but need not read another branch's conclusion before producing its own first-pass analysis;
- reviewers must read the result they are reviewing, but should independently reconstruct decisive calculations;
- synthesis happens only after approach-level work has been reviewed.

For decisive claims, role separation is mandatory where practical:

- original calculation author != numerical verifier;
- original approach author != final adversarial reviewer.

The same human may launch all chats; independence refers to the research context and reconstruction, not human identity.

## 7. Disagreement protocol

Never silently overwrite a conflicting conclusion.

When agents disagree:

1. preserve both claims/results;
2. identify the exact disputed item: source, number, assumption, equation, derivation, metric, or interpretation;
3. open or update a review record;
4. classify the dispute as factual, numerical, conceptual, evidentiary, or interpretive;
5. assign a resolution task to the appropriate independent role;
6. record the resolution or retain the dispute as unresolved.

Unresolved disagreement blocks promotion of the disputed claim into an accepted candidate or synthesis conclusion, but does not block unrelated research.

## 8. Rejection and supersession

Rejected approaches and failed candidate ideas remain scientifically useful.

A rejection should state:

- why the approach fails under current assumptions/technology,
- the quantitative gap,
- the decisive limitation,
- whether the failure is fundamental, current-technology-limited, or evidence-limited,
- what evidence would justify reopening it.

Do not delete rejected reasoning merely to keep the repository clean. Mark it clearly as rejected/superseded and keep it discoverable without presenting it as accepted state.

Exact claim/calculation/review/candidate status and identifier conventions are defined in `PROVENANCE_WORKFLOW.md`. Worker/campaign/decision lifecycle conventions are defined in `ORCHESTRATION_MODEL.md` and `orchestration/README.md`.

## 9. Merge rules by work type

### Foundations/literature
May merge when definitions or claims are explicit, sourced, non-conflicting or conflict-flagged, and do not overstate evidence.

### Approach research
May merge as research state even if the answer is negative, provided important claims are sourced, calculations are reproducible, uncertainties are explicit, and decisive numerical claims have verification or are clearly marked pending verification.

### Candidate experiments
Must not be treated as accepted final designs until decisive numerical claims are independently verified and adversarial review is resolved.

### Synthesis
May use only research state whose relevant disputes and verification requirements are resolved or explicitly represented as limitations. Unverified claims cannot support a decisive final ranking or design.

## 10. Bootstrap boundary

The collaboration model is implemented together with the six role files in `agents/`, the provenance workflow in `PROVENANCE_WORKFLOW.md`, and the process orchestration layer in `ORCHESTRATION_MODEL.md` plus `orchestration/`.

The remaining research-start gate is the fresh-system readiness audit in issue #6. Until that audit returns GO on the accepted `main` state, substantive Planck-gravity research remains NO-GO.
