# C27/P1C Codex Work Package

## Title

**Author-supplied `MSHT20_REP` closure, frozen ART25 output validation, and complete 642-member ARTEMIDE v3.01 process reproduction**

## Do not submit before the external inputs are staged

This work package is intentionally conditional.

Do not begin C27 merely to repeat the C26 source search. Begin only after the requested author/source payload has been placed in the repository working environment under a declared incoming-source directory, for example:

```text
data/incoming/c27_art25/
```

The incoming directory must contain one of the admissible `MSHT20_REP` source forms defined below and, preferably, the source-owned frozen-output bundle.

When the required files are absent, stop at preflight with a deterministic blocked report. Do not modify scientific capability matrices, do not create process outputs, and do not claim C27 completion.

## Authoritative baseline

Start from the local C26/P1B completion commit:

```text
8c2ed28abadf73663e2c816ac49b13541fae6a3b
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C26 baseline reproduces before any scientific changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

Do not push the completion commit.

---

# 1. Scientific starting point

C26 established all of the following:

```text
exact ARTEMIDE v3.01 engine available
exact official ART25 model payload available
642 stochastic ART25 Lambda_i rows available
2 technical ART25 records available
MAPFF10NNLOPIp DataVersion 1 hash locked
MAPFF10NNLOKAp DataVersion 1 hash locked
all 1,284 pion/kaon member resolutions exact
all 402 MAPFF member files hash locked
```

C26 also established the exact remaining source blocker:

```text
MSHT20_REP unavailable
```

The ART25 stochastic rows require PDF indices over:

```text
0 through 999
```

The public `MSHT20nnlo_as118` object contains only 65 Hessian members and is not the requested source object. It was correctly not renamed, wrapped, converted, or substituted.

Consequently:

```text
exact ART25 initialization unavailable
complete TMDPDF/TMDFF/CS convolution unavailable
central DY unavailable
central SIDIS unavailable
full 642-member process execution unavailable
serial/parallel/restart validation unavailable
DY-SIDIS joint covariance unavailable
source W unavailable
source W+Y unavailable
```

The immutable qualification state remains:

```text
438 analytic-process-oracle eligible
102 not process eligible
0 external ART25 source-process eligible
0 microscopic-project source-process eligible
0 physical-input eligible
```

C27 must close only those gates supported by the actual author/source payload.

---

# 2. Primary objective

Execute the chain:

```text
author/source-supplied MSHT20_REP archive or exact generator state
    -> provenance, license, checksum, and member-order validation
    -> exact ART25 PDF-index resolution for all 642 Lambda_i rows
    -> immutable ARTEMIDE v3.01 initialization
    -> distribution-level central and member execution
    -> frozen central DY and SIDIS reproduction
    -> all 642 stochastic joint-member executions
    -> joint TMDPDF/TMDFF/CS/PDF/FF/process covariance
    -> source W and possible source W+Y decision
    -> unchanged source and physical-input gate rerun
```

C27 must preserve two disjoint provenance roots:

```text
ART25_EXTERNAL_SOURCE_REPRODUCTION
PROJECT_MICROSCOPIC_TMD_PROCESS_PLAN
```

Successful ART25 reproduction does not automatically qualify the microscopic deuteron model.

---

# 3. Admissible incoming source forms

## 3.1 Preferred: exact `MSHT20_REP` archive

The preferred payload contains:

```text
MSHT20_REP.info
all member files
archive or directory checksum
member count
member numbering
ErrorType and source semantics
input/source provenance
generation provenance
license or redistribution permission
ART25 compatibility statement
```

The archive must support every ART25 PDF index used by the 642 stochastic rows.

## 3.2 Admissible alternative: exact deterministic generator state

A generator bundle is admissible only when it contains all of:

```text
exact input Hessian/source set name
exact input DataVersion and hashes
conversion formalism
source code and exact commit
all patches
random or quasi-random matrix
all seeds
normalization convention
eigenvector ordering
replica count
output-member ordering
clipping and positivity rules
output .info template
generation command
environment
official checksum or frozen numerical validation
license/permission
```

A generic Hessian-to-Monte-Carlo script is not sufficient.

The generator must reproduce the author/source `MSHT20_REP` members, not merely a statistically similar ensemble.

## 3.3 Frozen-output bundle

The preferred frozen-output bundle contains:

```text
central distribution-level values
selected stochastic-member distribution values
central fixed-target DY outputs
central collider/rapidity/fiducial DY outputs
central HERMES-like pion SIDIS outputs
central COMPASS-like kaon SIDIS outputs
selected stochastic-member DY/SIDIS outputs
dataset-component or chi2 values where available
commands and configurations
measurement definitions
integration mode
tolerances
software and data commits
checksums
```

Every file must carry source provenance and hash.

Do not digitize figures when frozen numerical outputs remain absent.

---

# 4. Completeness and autonomy

Completeness is the objective. Do not optimize for quickness.

Read all C24-C26 reports, APIs, manifests, requests, source locks, frozen grids, tests, ADRs, and roadmap entries before modifying code.

Continue autonomously until every applicable C27 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect the incoming files;
- validate archives, git bundles, checksums, signatures, and metadata;
- build source-locked isolated environments;
- install routine ARTEMIDE, LHAPDF, Fortran, Python, BLAS/LAPACK, and analysis dependencies;
- execute the immutable v3.01 engine;
- run all 642 members;
- construct deterministic restart and parallel-execution systems;
- generate source-level numerical and covariance reports;
- rebuild deterministic manifests.

Do not fabricate missing members, outputs, checksums, or permissions.

---

# 5. Normative repository sources

Read completely and hash-audit at least:

```text
docs/next_level/c25_implementation_report.md
docs/next_level/c25_art25_reproduction_source_plan.json
docs/next_level/c25_art25_member_schema.json
docs/next_level/c25_art25_member_validation.json
docs/next_level/c25_art25_parameter_reproduction.json
docs/next_level/c25_artemide_v301_build_manifest.json
docs/next_level/c25_v301_payload_compatibility.json
docs/next_level/c25_dataprocessor_source_manifest.json
docs/next_level/c25_frozen_benchmark_grid.json
docs/next_level/c25_art25_author_request.md

docs/next_level/c26_implementation_report.md
docs/next_level/c26_api.md
docs/next_level/c26_requirement_coverage.json
docs/next_level/c26_normative_source_integration.json
docs/next_level/c26_collinear_source_manifest.json
docs/next_level/c26_mapff_pion_source_lock.json
docs/next_level/c26_mapff_kaon_source_lock.json
docs/next_level/c26_msht20_rep_source_lock.json
docs/next_level/c26_collinear_set_inventory.json
docs/next_level/c26_art25_collinear_index_map.json
docs/next_level/c26_joint_member_validation.json
docs/next_level/c26_artemide_runtime_manifest.json
docs/next_level/c26_frozen_output_source_manifest.json
docs/next_level/c26_distribution_reproduction_manifest.json
docs/next_level/c26_source_process_eligibility_matrix.json
docs/next_level/c26_physical_input_eligibility_matrix.json
docs/next_level/c26_gate_delta_report.json
docs/next_level/c26_art25_request_delta.md
docs/next_level/c26_requested_file_schema.json
docs/next_level/c26_source_gap_manifest.json
docs/next_level/c26_unresolved_physics_gaps.md

references/volume_xix_source_qualified_process_inputs.tex
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c27_normative_source_integration.json
```

---

# 6. Immutable C26 baseline

Before ingesting incoming files, reproduce and record:

```text
1,120 tests
26 builders
36/36 evidence rows
162/162 atlas pages
1,080 C26 requirements
1,040/1,040 C26 negative injections

642 stochastic ART25 members
2 technical records
644 total stored rows
1,284 exact MAPFF member resolutions
zero MAPFF wrapping/clipping/missing/duplicate residuals

exact ARTEMIDE v3.01 build/import
642 direct NP-function executions
zero complete source-member executions

438 analytic eligible
102 not process eligible
0 external ART25 source eligible
0 microscopic-project source eligible
0 physical-input eligible

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C26 manifests byte-identical
deterministic C19-C26 manifest reconstruction
```

C27 must not modify:

- ARTEMIDE v3.01;
- ART25 constants;
- the official ART25 payload;
- the 642 stochastic rows;
- MAPFF tarballs or member files;
- C25/C26 frozen benchmark grid;
- C24-C26 gate definitions;
- historical capability matrices;
- C23 analytic process plans;
- microscopic/nuclear model identities;
- production registry or authoritative artifacts.

---

# 7. Incoming-source preflight

Implement a deterministic `C27IncomingSourcePreflight`.

The preflight must report every required file and gate:

```text
incoming directory exists
MSHT20_REP source form
archive/generator integrity
source identity
checksum
license/permission
member count
member numbering
ART25 index coverage
frozen-output bundle status
commands/configuration status
source contact/authorization status
```

When the MSHT source form is absent or incomplete:

```text
C27_BLOCKED_MISSING_EXACT_MSHT20_REP
```

must be issued.

When frozen outputs are absent but exact source execution is otherwise possible, C27 may continue with source-regenerated validation while preserving:

```text
AUTHOR_FROZEN_OUTPUT_UNAVAILABLE
```

The absence of author-frozen outputs must never be hidden.

---

# 8. Source provenance and integrity

For each incoming file record:

```text
original filename
source/author
transfer date
transfer channel
license/permission
original checksum
local checksum
size
MIME type
archive members
source role
immutability status
```

Preserve original incoming bytes under:

```text
data/raw/c27_sources/
```

Do not edit original source files in place.

Every normalized or generated derivative must point back to its source hash.

Create:

```text
docs/next_level/c27_incoming_source_manifest.json
docs/next_level/c27_msht20_rep_source_lock.json
docs/next_level/c27_frozen_output_source_lock.json
```

---

# 9. Exact PDF ensemble validation

Implement immutable objects equivalent to:

```text
MSHT20RepSourceId
MSHT20RepGenerationId
MSHT20RepMemberId
MSHT20RepEnsemble
MSHT20RepIndexMap
MSHT20RepValidationReport
```

Validate:

```text
source member count
central/member semantics
index range
all ART25 PDF indices in range
unique content identities
member ordering
source metadata
alpha_s and heavy-flavor metadata
x and Q domains
deterministic evaluation
source checksum
```

Required negative controls:

```text
MSHT20nnlo_as118 substitution
generic Hessian-to-MC substitution
renamed source set
modulo member mapping
nearest-member mapping
central-member replication
member clipping
member reordering without explicit source IDs
```

All must fail before ARTEMIDE initialization.

---

# 10. Generator-state reproduction

When the incoming source is a generator state:

1. reproduce the exact output in an isolated environment;
2. hash every generated member;
3. compare against any provided official checksums;
4. preserve generator inputs and outputs separately;
5. test repeated generation;
6. test execution on an independent clean environment;
7. record bitwise or numerical reproducibility status;
8. retain generator uncertainty or platform dependence.

If the generated set cannot be proven to match the ART25 source ensemble, qualification remains closed.

---

# 11. ART25 joint-member map

For every stochastic row \(i=1,\ldots,642\), resolve exactly:

```text
Lambda_i
MSHT20_REP[pdf_index_i]
MAPFF10NNLOPIp[pion_index_i]
MAPFF10NNLOKAp[kaon_index_i]
```

Retain one indivisible `ART25JointMemberId`.

Validate:

- all 642 PDF indices;
- all 1,284 FF indices;
- no wrapping, clipping, defaulting, or substitution;
- repeated indices preserved;
- central and technical records treated by source semantics;
- deterministic map hash;
- exact source-file references.

Create:

```text
docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_joint_member_validation.json
```

---

# 12. Immutable v3.01 runtime initialization

Initialize with:

```text
exact ARTEMIDE v3.01 engine
exact ART25 constants
exact ART25 model payload
exact MSHT20_REP
exact MAPFF10NNLOPIp
exact MAPFF10NNLOKAp
source-locked DataProcessor
```

Record:

```text
compiler
flags
Python
NumPy/f2py
LHAPDF
BLAS/LAPACK
OpenMP
integration mode
precompiled-kernel mode
thread count
floating-point environment
data paths
set hashes
initialization logs
```

No physics patch is permitted.

Path aliases are permitted only when byte content and metadata remain unchanged and the alias is explicitly recorded.

Create:

```text
docs/next_level/c27_artemide_v301_runtime_manifest.json
```

---

# 13. Distribution-level execution

Execute the immutable C25/C26 distribution grid for:

```text
CS kernel
unpolarized TMDPDF
pion TMDFF
kaon TMDFF
```

Run:

```text
central/mean record
frozen diagnostic members
all 642 stochastic members
```

For each value retain:

```text
joint member ID
x or z
b
Q
scheme
source domain
value
integration/numerical error
runtime identity
```

Validate:

- direct independent NP-function evaluation;
- ARTEMIDE output;
- collinear-member dependence;
- small-b behavior;
- large-b source domain;
- Q dependence;
- central-versus-mean distinction;
- empirical intervals;
- covariance and cross-covariance;
- member-order invariance.

---

# 14. Central DY reproduction

Execute every immutable frozen DY point.

Retain:

```text
fixed-target
collider/Z
rapidity/fiducial
```

For every comparison record:

```text
source-output evidence tier
measurement definition
cuts/binning
electroweak current
units and normalization
central/mean identity
source value if supplied
reproduced value
absolute residual
relative residual
numerical uncertainty
```

Do not compare unlike observables or bin definitions.

---

# 15. Central SIDIS reproduction

Execute every immutable frozen SIDIS point:

```text
HERMES-like pion
COMPASS-like kaon
charge-resolved channels
```

Retain:

```text
x
z
Q
P_hT
hadron charge
multiplicity/cross-section convention
normalization
binning
PDF/FF member identity
```

No negative-charge or charge-sum substitution is allowed.

---

# 16. Full 642-member execution

Execute all 642 stochastic members.

The execution system must support:

```text
deterministic serial run
deterministic parallel run
checkpoint/restart
per-member failure record
retry policy that does not alter physics
content-addressed outputs
```

Validate:

```text
642 attempted
642 completed when all source inputs are valid
0 missing
0 duplicate
serial == parallel
restart == uninterrupted
stable member order
no cross-process member shuffle
```

Do not impute failed members.

Create:

```text
docs/next_level/c27_full_member_execution_manifest.json
docs/next_level/c27_execution_failure_manifest.json
```

---

# 17. Joint covariance reconstruction

Construct the empirical joint covariance across:

```text
CS kernel
TMDPDF
pion TMDFF
kaon TMDFF
PDF members
FF members
DY observables
SIDIS observables
```

Retain source member identity.

Validate:

- covariance symmetry;
- PSD within numerical tolerance;
- cross-process blocks;
- distribution/process cross-covariance;
- central-versus-ensemble semantics;
- serial/parallel/restart equality;
- member permutation covariance when IDs are retained;
- failure under independent marginal reshuffling.

Create:

```text
docs/next_level/c27_joint_covariance_manifest.json
```

---

# 18. Frozen-output validation

Classify every comparison as:

```text
AUTHOR_PROVIDED_FROZEN_OUTPUT
OFFICIAL_REPOSITORY_FROZEN_OUTPUT
SOURCE_REGENERATED_OUTPUT
PUBLISHED_NUMERICAL_ANCHOR
NO_SOURCE_NUMERICAL_ANCHOR
```

Author-provided outputs receive exact checksum and command validation.

Source-regenerated outputs must not be relabeled author-provided.

When no official numerical anchor exists, report deterministic source execution without inventing a residual to a paper figure.

---

# 19. Independent oracles

Require at least three independent checks:

1. direct NP model-function evaluation;
2. independent LHAPDF evaluation at exact PDF/FF member indices;
3. independent ensemble statistics and covariance;
4. controlled Born/normalization limit;
5. DataProcessor-independent controlled-bin computation.

At least one oracle must depend on the exact `MSHT20_REP` member content.

---

# 20. Source W and W+Y decision

A reproduced low-\(q_T\) ART25 process object may receive:

```text
SOURCE_TMD_W_TERM_REPRODUCED
```

only when the exact source chain is complete.

A source-qualified \(W+Y\) record additionally requires exact fixed-order and asymptotic source inputs with identical:

```text
process
measurement
cuts
scheme
hard factor
masses
scales
thresholds
rank
order
```

The prohibited combination remains:

```text
ART25 source W + C23 analytic Y
```

When fixed-order inputs remain incomplete, issue:

```text
SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE
```

---

# 21. Gate rerun and capability separation

Rerun unchanged C24-C26 source and physical-input evaluators for the external ART25 plan.

Report separately:

```text
external ART25 source-process eligibility
external ART25 physical-input eligibility
microscopic-project source-process eligibility
microscopic-project physical-input eligibility
```

Successful ART25 proton process reproduction cannot directly qualify:

```text
spin-1 process
deuteron process
microscopic model
non-NN nuclear component
matched nuclear total
```

Create:

```text
docs/next_level/c27_source_process_eligibility_matrix.json
docs/next_level/c27_physical_input_eligibility_matrix.json
docs/next_level/c27_gate_delta_report.json
```

---

# 22. Holdouts

Freeze holdouts before adapter or tolerance changes.

Reserve at least:

- one MSHT member value;
- one ART25 PDF index;
- one MAPFF pion member;
- one MAPFF kaon member;
- one CS point;
- one TMDPDF point;
- one pion-TMDFF point;
- one kaon-TMDFF point;
- one fixed-target DY point;
- one collider/fiducial DY point;
- one HERMES SIDIS point;
- one COMPASS SIDIS point;
- one stochastic-member frozen output;
- one DY-SIDIS covariance element;
- one serial/parallel equality point;
- one external-versus-microscopic provenance control.

Do not move failed holdouts into tuning without a new version and new independent holdouts.

---

# 23. Required benchmark families

Implement at least:

```text
P1C-A incoming-source integrity
P1C-B MSHT20_REP exact identity
P1C-C generator-state reproduction when applicable
P1C-D all-index joint member resolution
P1C-E immutable v3.01 initialization
P1C-F distribution central reproduction
P1C-G distribution 642-member reproduction
P1C-H central DY reproduction
P1C-I central SIDIS reproduction
P1C-J complete 642-member process execution
P1C-K serial/parallel/restart equality
P1C-L joint covariance
P1C-M frozen-output evidence tiers
P1C-N source W/W+Y decision
P1C-O external versus microscopic capability
P1C-P deterministic isolation
```

---

# 24. Negative injections

Create at least **1,120 ordered C27 negative injections**.

Include:

## Source provenance

- missing permission;
- missing checksum;
- altered archive;
- wrong author/source;
- wrong transfer version;
- incomplete archive;
- unofficial reconstruction.

## MSHT identity

- public 65-member Hessian substitution;
- generic Hessian-to-MC conversion;
- missing generator seed/matrix;
- wrong input DataVersion;
- wrong output ordering;
- member count mismatch;
- central member replicated;
- renamed set;
- modulo mapping;
- clipping;
- nearest-member substitution.

## Joint members

- PDF index shuffle;
- pion FF index shuffle;
- kaon FF index shuffle;
- TMDPDF/TMDFF/CS independent sampling;
- technical record in stochastic ensemble;
- dropped member;
- duplicate member;
- one process uses a different member identity.

## Runtime

- v3.02/v3.03/current engine;
- changed ART25 constants;
- physics patch;
- wrong integration mode;
- nondeterministic threading;
- wrong data path content;
- incomplete initialization hidden.

## Reproduction

- changed frozen point;
- figure digitization;
- central/mean confusion;
- wrong binning;
- wrong units;
- wrong current;
- wrong hadron charge;
- wrong z convention;
- source-regenerated output labeled author provided;
- residual omitted.

## Covariance

- marginal bands sampled independently;
- cross-process covariance dropped;
- failed members imputed;
- member weights changed;
- covariance mixed with synthetic C23 uncertainty.

## Qualification and integrity

- external ART25 promoted to microscopic qualification;
- proton result called deuteron prediction;
- source W mixed with analytic Y;
- T-odd process promoted;
- historical matrices overwritten;
- production registry changed;
- authoritative artifact changed;
- likelihood/posterior created;
- nondeterministic manifest.

---

# 25. Deliverables

Create at least:

```text
docs/next_level/c27_implementation_report.md
docs/next_level/c27_api.md
docs/next_level/c27_requirement_coverage.json
docs/next_level/c27_normative_source_integration.json
docs/next_level/c27_incoming_source_manifest.json
docs/next_level/c27_msht20_rep_source_lock.json
docs/next_level/c27_frozen_output_source_lock.json
docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_joint_member_validation.json
docs/next_level/c27_artemide_v301_runtime_manifest.json
docs/next_level/c27_distribution_reproduction_manifest.json
docs/next_level/c27_dy_central_reproduction.json
docs/next_level/c27_sidis_central_reproduction.json
docs/next_level/c27_full_member_execution_manifest.json
docs/next_level/c27_execution_failure_manifest.json
docs/next_level/c27_joint_covariance_manifest.json
docs/next_level/c27_frozen_output_validation.json
docs/next_level/c27_independent_oracle_report.json
docs/next_level/c27_source_wy_status.json
docs/next_level/c27_source_process_eligibility_matrix.json
docs/next_level/c27_physical_input_eligibility_matrix.json
docs/next_level/c27_gate_delta_report.json
docs/next_level/c27_holdout_report.json
docs/next_level/c27_injection_manifest.json
docs/next_level/c27_regression_report.json
docs/next_level/c27_unresolved_physics_gaps.md
```

Preserve incoming source bytes under:

```text
data/raw/c27_sources/
```

Add ADRs for:

- author-supplied source provenance;
- exact `MSHT20_REP` versus generated equivalents;
- frozen-output evidence tiers;
- all-member execution and restart;
- joint covariance;
- external ART25 versus microscopic provenance;
- source W versus W+Y status.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C27/P1C is complete only when:

1. The exact C26 baseline reproduces.
2. The required incoming source is present and hash locked.
3. Source permission/license is recorded.
4. `MSHT20_REP` is exact or its exact generator state is reproduced.
5. The public 65-member Hessian set is never substituted.
6. All ART25 PDF indices resolve exactly.
7. All MAPFF indices remain exact.
8. All 642 stochastic joint members retain indivisible identity.
9. ARTEMIDE v3.01 and ART25 constants remain unchanged.
10. Exact runtime initialization completes.
11. The frozen benchmark grid remains unchanged.
12. Distribution central execution completes.
13. Distribution stochastic execution completes for all 642 members.
14. Central DY execution completes.
15. Central SIDIS execution completes.
16. All 642 process members execute or every source-supported process limitation is explicit.
17. No failed member is imputed.
18. Serial, parallel, and restart paths agree.
19. Joint covariance and cross-process covariance are reconstructed.
20. At least three independent oracles pass.
21. Frozen-output evidence tiers are truthful.
22. No paper figure is digitized as source data.
23. Source W status is decided.
24. Source W+Y is issued only with exact fixed-order/asymptotic identity.
25. External ART25 and microscopic capability remain distinct.
26. No ART25 proton result is called a deuteron prediction.
27. Every failed gate remains visible.
28. All prior tests, builders, requirements, injections, and manifests pass.
29. The production registry remains 216.
30. All eight authoritative artifacts remain byte-identical.
31. No likelihood, posterior, inference, or production route is created.
32. Every C27 injection yields its expected diagnostic.
33. All C27 manifests reproduce byte-for-byte.
34. The working tree is clean.
35. A local completion commit is created and not pushed.

When the incoming payload is incomplete, C27 is not scientifically complete. Produce a blocked preflight report rather than a completion claim.

---

# 27. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- incoming files, provenance, permissions, and hashes;
- exact MSHT source form;
- exact member count and index range;
- generator reproduction status when applicable;
- all joint-index residuals;
- v3.01 initialization status;
- distribution central and ensemble residuals;
- central DY residuals;
- central SIDIS residuals;
- members attempted/completed/failed/retried;
- serial/parallel/restart residuals;
- joint covariance residuals;
- frozen-output evidence tiers;
- source W and W+Y status;
- external ART25 source/physical eligibility counts;
- microscopic-project source/physical eligibility counts;
- all remaining gates;
- deterministic manifest status;
- files created;
- local commit;
- confirmation that nothing was pushed.

Do not claim C27 completion when the exact incoming source contract is not satisfied.
