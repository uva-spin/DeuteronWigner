# C22Q/M3Q Codex Work Package

## Title

**Authoritative M3 capability reconciliation, process-eligibility qualification, and C23 prerequisite closure**

## Starting baseline

Start from the local prerequisite-audit commit:

```text
dbd003bbd26c954a67ca0f534081ff1a99ab5307
```

This commit must contain:

```text
docs/next_level/c23_p0_codex_prompt.md
docs/next_level/c23_prerequisite_audit.json
```

and must retain the scientific C22 completion commit in its ancestry:

```text
12e1850d101b0d64de27ae0daaf4ae42772e2a22
```

Do not use `origin/main` as the scientific baseline if the local branch is ahead of the remote.

Do not push the completion commit.

---

# 1. Why this package exists

The preserved C23/P0 prompt cannot be executed against the authoritative post-Volume-XVIII capability state.

The conflict is:

```text
C23 prompt assumption:
    438 M3-qualified
    54 evolution-only
    48 unavailable

authoritative post-Volume-XVIII state:
    0 M3-qualified
    54 evolution-only
    486 unavailable
```

The value `438` came from the inherited C21/M2 count of identities that were fully evolvable at M2 scope. It is not, by itself, proof that those identities satisfy the stricter C22/M3 small-b, collinear, source, scheme, boundary, and process-consumption gates.

C22Q/M3Q must reconcile these layers without weakening any gate, inventing metadata, or declaring an analytic validation oracle to be a physical TMD.

The original C23 prompt must remain preserved byte-for-byte as the historical blocked prompt. A corrected process prompt may be generated separately only after this package produces the authoritative process-eligibility contract.

---

# 2. Primary objective

Implement the exact unblocking work recorded in:

```text
docs/next_level/c23_prerequisite_audit.json
```

The required chain is:

```text
C20 reference matching capability
    + C21 M2 evolution capability
    + C22 small-b/OPE/collinear capability
    + nonperturbative-boundary and scheme status
    + nuclear-operator status
    -> authoritative M3 qualification tier
    -> process-consumption eligibility
    -> corrected C23/P0 prerequisite contract
```

The output must distinguish at least three levels:

```text
M3_VALIDATION_QUALIFIED
    Complete for an explicitly synthetic/analytic validation plan.
    May support analytic process-compiler and W+Y oracles.
    Cannot support a physical process claim.

M3_SOURCE_QUALIFIED
    Complete declared-order operator route with source-audited perturbative
    ingredients and a source-qualified boundary/kernel plan, but not necessarily
    a physical extraction or global covariance-bearing result.

M3_PHYSICAL_INPUT_QUALIFIED
    Includes every physical external/nonperturbative input, covariance, scheme,
    domain, and source requirement needed for a physical-input process plan.

M3_EVOLUTION_ONLY
M3_COEFFICIENT_ONLY
M3_COLLINEAR_ONLY
M3_HIGHER_TWIST_REQUIRED
M3_SOURCE_DISAGREEMENT
M3_MISSING_OPERATOR
M3_UNAVAILABLE
```

Do not collapse these levels into one Boolean flag.

The exact status vocabulary may follow the existing code if equivalent distinctions already exist.

---

# 3. Autonomous execution and honesty

Completeness is the objective. Do not optimize for quickness.

Read the complete prerequisite audit, C19-C22 reports, APIs, capability matrices, source manifests, tests, ADRs, roadmap, and Volume V/XVI/XVIII formal sources before changing code.

Continue autonomously until every audit item and acceptance criterion is resolved.

Do not stop for approval to:

- inspect repository files;
- run tests, builders, evidence, atlas, and validators;
- install routine local dependencies when permitted;
- regenerate deterministic manifests;
- build crosswalk and diagnostic tools;
- preserve primary sources already identified by C20-C22;
- add independent analytic checks.

If a physical source or covariance bundle remains unavailable, retain that limitation and qualify only the lower validation/source tier that is actually supported.

Do not solve the conflict by:

- relabeling the C21 `438` count;
- weakening `M3_FULLY_QUALIFIED`;
- treating an analytic Collins-Soper kernel as physical;
- ignoring the large-b boundary;
- copying a nucleon operator block into a distinct many-body operator;
- declaring process eligibility from a TMD name;
- making unavailable identities zero;
- changing the C23 prompt in place;
- creating a process, W, Y, likelihood, or production route.

---

# 4. Normative sources

Read completely and hash-audit at least:

```text
docs/next_level/c23_prerequisite_audit.json
docs/next_level/c23_p0_codex_prompt.md

docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c19_matching_basis.json
docs/next_level/c19_matching_fit_manifest.json

docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_matching_fit_manifest.json

docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_evolution_capability_matrix.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_uncertainty_manifest.json

docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_collinear_evolution_manifest.json
docs/next_level/c22_accuracy_manifest.json
docs/next_level/c22_uncertainty_manifest.json
docs/next_level/c22_unresolved_physics_gaps.md
docs/next_level/c22_regression_report.json

references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c22q_normative_source_integration.json
```

containing source hashes, roles, and any missing-file status.

---

# 5. Immutable baseline reproduction

Before editing, reproduce and record:

```text
1,071 C22 tests
all C22 builders and validators
36/36 evidence rows
162/162 atlas pages
980 C22 requirements
720 C22 negative injections
15 C22 primary papers preserved

C20 historical split:
    492 matching-executable
    48 matching-unavailable

C21 historical split:
    438 fully evolvable at M2 scope
    102 incomplete at M2 scope

authoritative post-C22/M3 split:
    0 M3-qualified
    54 evolution-only
    486 unavailable

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C22 manifests byte-identical
deterministic C22 manifest rebuild
18 focused prerequisite-audit tests
C22 validator
clean working tree
```

Do not proceed if the authoritative `0/54/486` split cannot be reproduced.

Do not overwrite the authoritative C22 matrix merely to match an older narrative summary.

---

# 6. Root-cause reconciliation

Produce an exact, machine-readable explanation of how each historical count was obtained.

For all 540 identities, record:

```text
operator_id
C20 reference-matching status
C21 M2 TMD-evolution status
C22 twist classification
C22 coefficient status
C22 collinear-operator status
C22 collinear-evolution status
gamma5/scheme status
threshold status
rank-transform status
route-A/route-B status
nonperturbative CS-kernel tier
large-b boundary tier
nuclear-operator tier
missing-operator status
M3 qualification tier
process-eligibility tier
blocking reasons
source provenance
```

Create:

```text
docs/next_level/c22q_capability_reconciliation.json
docs/next_level/c22q_count_reconciliation_report.md
```

The report must explain explicitly:

1. why `438 M2 fully evolvable` did not imply `438 M3 qualified`;
2. why the earlier C22 narrative summary reported `438/54/48`;
3. why the authoritative matrix reports `0/54/486`;
4. whether the discrepancy was:
   - a summary-generation bug;
   - a status-semantic mismatch;
   - a manifest-construction bug;
   - missing operator metadata;
   - a genuinely unfulfilled scientific gate;
   - or a combination;
5. which count is authoritative for each layer.

Do not change scientific statuses until the cause is identified.

---

# 7. Qualification contract

Implement a single authoritative qualification evaluator.

A validation-qualified M3 identity requires, at minimum:

```text
complete operator identity
C20 reference matching executable
C21 TMD evolution available
C22 twist classification complete
declared-order coefficient executable
correct collinear operator identified
collinear evolution executable
gamma5 conversion when applicable
threshold path supported
rank transform supported
route-A/route-B consistency within declared remainder
complete validation CS-kernel plan
complete validation large-b boundary plan
nuclear operator block available or explicitly not required
all scheme identities compatible
all missing-operator terms explicit
accuracy and uncertainty manifests complete
```

A source-qualified identity additionally requires:

```text
source-audited nonperturbative/kernel or boundary plan
source-valid domain
source covariance or an explicitly source-qualified uncertainty model
no synthetic-only input in the qualifying chain
```

A physical-input-qualified identity additionally requires every physical-input and covariance condition specified by the prerequisite audit.

If the audit uses stricter definitions, follow the audit.

The evaluator must return every failed gate, not only the first failure.

---

# 8. Validation versus physical process eligibility

Create separate process-consumption gates:

```text
ANALYTIC_PROCESS_ORACLE_ELIGIBLE
    May be used only by an analytic/synthetic process validation plan.

SOURCE_PROCESS_VALIDATION_ELIGIBLE
    May be used by a source-qualified but validation-only process plan.

PHYSICAL_PROCESS_INPUT_ELIGIBLE
    May be used by a physical-input process plan.

NOT_PROCESS_ELIGIBLE
```

These gates must not be inferred from a TMD name or array shape.

The corrected C23 process package must later enforce:

```text
analytic W/Y oracle
    -> ANALYTIC_PROCESS_ORACLE_ELIGIBLE or stronger

source-qualified W term
    -> SOURCE_PROCESS_VALIDATION_ELIGIBLE or stronger

physical-input process claim
    -> PHYSICAL_PROCESS_INPUT_ELIGIBLE
```

This tiering must not permit the 54 evolution-only or 48 C20 matching-unavailable identities to enter a W term.

---

# 9. Execute the prerequisite audit's unblocking work

Treat every item in:

```text
docs/next_level/c23_prerequisite_audit.json
```

as a mandatory requirement.

Build a coverage map:

```text
audit_item_id
description
affected identities
required code change
required source/manifest change
tests
negative injections
completion status
remaining limitation
```

Create:

```text
docs/next_level/c22q_prerequisite_audit_coverage.json
```

Do not omit an audit item because it is difficult.

Where the audit identifies missing metadata rather than missing physics, add the exact typed metadata and reconstruct the capability matrix.

Where it identifies missing physics, implement only source-supported or clearly validation-only routes, preserving the status tier.

Where it identifies an unavailable physical input, leave the physical tier unavailable and document the exact unblocking source requirement.

---

# 10. Minimal process-relevant qualification targets

Do not preselect a total qualified count.

However, explicitly audit the minimal T-even process-relevant families needed for later P0 architecture:

```text
rank-zero unpolarized quark and antiquark U
rank-zero spin-1 LL quark and antiquark where same-local-operator universality is proven
rank-zero quark helicity where the full gamma5 route is available
quark transversity where the complete route is available
rank-zero unpolarized gluon
rank-two linearly polarized gluon
inclusive collinear b1 inputs
tagged-DIS collinear/GTMD inputs
```

For each family, report separately:

```text
validation qualification
source qualification
physical-input qualification
process eligibility
blocking reasons
```

Do not force any family to qualify.

T-odd and multiparton families remain unavailable unless their exact C22 prerequisites are added through a separate source-audited package.

---

# 11. Collins-Soper and large-b semantics

The audit must determine whether the lack of a physical covariance-qualified quark/gluon CS-kernel bundle blocks:

```text
validation qualification
source qualification
physical-input qualification
```

These must be distinct decisions.

An analytic large-b completion may qualify a synthetic validation route only when:

- it is explicitly marked synthetic/model;
- its parameters and domain are recorded;
- it is not called a physical kernel;
- its uncertainty is retained separately;
- it is not used to qualify a physical process input.

A source-recorded but covariance-incomplete kernel may receive only the tier permitted by the audit.

A physical-input tier must remain unavailable when the required covariance/domain/scheme bundle is absent.

---

# 12. Nuclear and many-body operator semantics

Do not declare the full nuclear matched total M3-qualified merely because the nucleon impulse block qualifies.

Retain separate status for:

```text
NN impulse
NNPI pion-active
DeltaDelta
six-quark cluster
six-quark hidden color
transition/interference
coherent pilot
matched total
```

For each block, distinguish:

```text
same local operator and universal coefficient proven
independent coefficient/evolution block implemented
validation-only model block
operator-specific unavailable
```

The complete matched total may qualify only when every selected component is qualified at the same requested tier or is excluded by the assumption plan.

Hidden-color complete observables must remain basis covariant.

---

# 13. Corrected C23 prerequisite contract

Do not modify:

```text
docs/next_level/c23_p0_codex_prompt.md
```

Create:

```text
docs/next_level/c23_p0_prerequisite_contract.json
docs/next_level/c23_p0_codex_prompt_v2.md
```

The corrected prompt must:

1. use the final authoritative qualification counts;
2. distinguish analytic, source-qualified, and physical-input process plans;
3. allow analytic W/Y oracles only from the analytic-eligible tier;
4. allow source-qualified W terms only from the source-eligible tier;
5. forbid physical claims without physical-input eligibility;
6. preserve all T-odd and multiparton gates;
7. preserve the original C23 scientific scope and process/factorization safeguards;
8. retain the original prompt as an immutable historical artifact;
9. begin from the final C22Q completion commit, not from the old C22 commit;
10. fail closed when its minimum process-eligible set is empty.

Do not execute the corrected C23 prompt in this package.

---

# 14. Tests and negative injections

Add at least **160 ordered C22Q negative injections** with stable IDs.

Include:

## Count and semantic failures

- C21 M2 `438` copied into M3-qualified count;
- old narrative `438/54/48` treated as authoritative;
- authoritative `0/54/486` ignored;
- one Boolean availability flag replacing tiered capability;
- process eligibility inferred from matching only;
- process eligibility inferred from evolution only.

## Qualification-gate failures

- missing coefficient;
- missing collinear operator;
- missing collinear evolution;
- missing gamma5 conversion;
- missing threshold;
- wrong rank transform;
- failed route-A/route-B test;
- synthetic CS kernel labeled physical;
- large-b boundary omitted;
- missing nuclear operator block;
- unresolved missing operator silently set to zero;
- incompatible scheme accepted.

## Process-tier failures

- analytic-only identity used in source-qualified plan;
- source-qualified identity used in physical-input claim;
- evolution-only identity used in any W term;
- matching-unavailable identity used in any W term;
- T-odd microscopic boundary used without multiparton matching;
- process eligibility inferred from TMD name.

## Nuclear failures

- impulse qualification copied to pion/DeltaDelta/6q/coherent blocks;
- matched total qualified with unavailable selected component;
- hidden-color basis covariance lost;
- cluster/compact double counting.

## Integrity failures

- original C23 prompt modified;
- C22 scientific manifests mutated;
- production registry mutation;
- authoritative artifact mutation;
- process/W/Y route created;
- inference route created;
- nondeterministic manifest.

---

# 15. Deliverables

Create at least:

```text
docs/next_level/c22q_implementation_report.md
docs/next_level/c22q_api.md
docs/next_level/c22q_requirement_coverage.json
docs/next_level/c22q_normative_source_integration.json
docs/next_level/c22q_capability_reconciliation.json
docs/next_level/c22q_count_reconciliation_report.md
docs/next_level/c22q_qualification_contract.json
docs/next_level/c22q_process_eligibility_matrix.json
docs/next_level/c22q_prerequisite_audit_coverage.json
docs/next_level/c22q_minimal_process_family_audit.json
docs/next_level/c22q_cs_largeb_tier_manifest.json
docs/next_level/c22q_nuclear_operator_qualification.json
docs/next_level/c23_p0_prerequisite_contract.json
docs/next_level/c23_p0_codex_prompt_v2.md
docs/next_level/c22q_injection_manifest.json
docs/next_level/c22q_regression_report.json
docs/next_level/c22q_unresolved_physics_gaps.md
```

Add ADRs for:

- M2 versus M3 capability semantics;
- validation/source/physical qualification tiers;
- process-consumption eligibility;
- CS-kernel and large-b qualification tiers;
- nuclear-component qualification;
- preservation of the blocked C23 prompt.

Update:

```text
handoff/ROADMAP.md
```

All generated JSON and the corrected prompt must reproduce byte-for-byte.

---

# 16. Acceptance criteria

C22Q/M3Q is complete only when:

1. The exact baseline commit and C22 ancestor are verified.
2. The C22 baseline and audit tests reproduce.
3. The `0/54/486` authoritative split reproduces before changes.
4. The historical `438`, `438/102`, `492/48`, and old narrative `438/54/48` counts are explained without conflation.
5. Every one of 540 identities has a complete gate-by-gate reconciliation record.
6. A single authoritative qualification evaluator exists.
7. Validation, source-qualified, and physical-input tiers are distinct.
8. Process-eligibility tiers are distinct and fail closed.
9. Every prerequisite-audit item is covered.
10. No audit item is silently waived.
11. Minimal process-relevant families are audited individually.
12. T-odd and multiparton identities remain fail-closed.
13. CS-kernel and large-b limitations receive the correct tiered effect.
14. Nuclear components are qualified separately.
15. Hidden-color covariance remains closed.
16. The original C23 prompt remains byte-identical.
17. A corrected C23 v2 prompt and prerequisite contract are generated.
18. The corrected prompt uses the actual final counts.
19. No process, W, Y, inference, or production route is executed.
20. Every new negative injection produces the expected diagnostic.
21. All previous tests and validators remain passing.
22. The production registry remains 216.
23. All eight authoritative artifacts remain byte-identical.
24. All prior pinned manifests remain byte-identical.
25. All new manifests reproduce byte-for-byte.
26. The working tree is clean.
27. A local completion commit is created and not pushed.

If the final process-eligible count remains zero, C22Q may still complete the reconciliation and corrected contract, but its final report must state that C23 remains blocked and identify the exact remaining scientific inputs. It may not declare C23 unblocked.

---

# 17. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- reproduced pre-change `0/54/486` split;
- exact root cause of the count conflict;
- historical count reconciliation;
- final counts by M3 qualification tier;
- final counts by process-eligibility tier;
- minimal process-family audit results;
- CS-kernel and large-b tier statuses;
- nuclear-component qualification counts;
- all remaining blockers;
- whether C23 is now unblocked;
- corrected C23 prompt path and hash;
- confirmation that the original C23 prompt is byte-identical;
- deterministic manifest status;
- files created;
- local commit;
- confirmation that nothing was pushed.

Do not claim that C23 is executable unless at least one process plan has a nonempty, correctly tiered eligible operator set and every prerequisite contract gate for that plan passes.
