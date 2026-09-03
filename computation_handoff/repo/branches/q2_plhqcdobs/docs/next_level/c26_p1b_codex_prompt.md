# C26/P1B Codex Work Package

## Title

**Exact ART25 collinear-ensemble ingestion, immutable ARTEMIDE v3.01 execution, full 642-member DY/SIDIS reproduction, and source-gate closure**

## Authoritative baseline

Start from the local C25/P1A completion commit:

```text
c4c71d94af09c00b53a5bd21617e2f26962664e9
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C25 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

Do not push the final completion commit.

---

# 1. Why C26/P1B is the exact next package

C25 recovered and hash-locked:

```text
the complete official ART25 model payload
the 642-member stochastic ART25 ensemble
the initialization record
the central/mean record
the exact 22 fitted-parameter semantics
the exact ARTEMIDE v3.01 engine
the two-component engine/payload provenance identity
the already frozen DY/SIDIS/distribution benchmark grid
```

C25 also established:

```text
642 stochastic members
2 technical records
644 stored rows
28 NP slots per row
22 fitted NP parameters
6 fixed/model-control slots
3 correlated collinear-member indices
```

The exact v3.01 engine compiles and imports without a physics patch, and all nine ART25 model files are byte-identical to the v3.01 model sources.

Runtime process reproduction remains blocked because the ART25 constants require:

```text
MSHT20_REP
MAPFF10NNLOPIp
MAPFF10NNLOKAp
```

and because no official source-owned frozen process-output bundle has yet been ingested.

A current official-source refinement must be incorporated:

1. `MAPFF10NNLOPIp` and `MAPFF10NNLOKAp` are listed in the official LHAPDF archive and must be acquired from that authoritative channel first.
2. The public `MSHT20nnlo_as118` LHAPDF set is a 65-member Hessian set—one central member plus 32 eigenvector pairs. It is not the ART25 custom object named `MSHT20_REP`.
3. Therefore the MAPFF blockers may be directly solvable from the official archive, but `MSHT20_REP` must not be replaced by the standard Hessian set or by an arbitrary Hessian-to-Monte-Carlo conversion.
4. The exact member ordering matters because every ART25 \(\Lambda_i\) record stores explicit PDF, pion-FF, and kaon-FF member indices. Distributional equivalence without member-by-member identity is insufficient.

C26 must acquire, validate, and execute the exact source chain—or fail closed with a precise residual source request.

---

# 2. Primary objective

Implement:

```text
C25 ART25 joint member Lambda_i
    -> exact PDF/FF member-index resolution
    -> source-locked collinear ensembles
    -> exact ARTEMIDE v3.01 initialization
    -> frozen distribution-level benchmark execution
    -> frozen DY/SIDIS central execution
    -> all 642 stochastic joint-member executions
    -> joint TMDPDF/TMDFF/CS/PDF/FF covariance reconstruction
    -> unchanged C24/C25 source and physical gate rerun
    -> exact external-source and microscopic-project capability decisions
```

The scientific objective is not to force a positive qualification result.

C26 is complete when:

- the exact requested collinear sets and source-output contract are ingested and executed; or
- every official acquisition and exact-generation path is exhausted, the remaining missing inputs are identified at file/checksum/member level, and the author request is updated without fabrication.

---

# 3. Scope and nonclaims

C26 is:

```text
source-reproduction focused
version locked
member correlated
process and distribution benchmarked
unpolarized ART25 first
validation only
isolated from inference and production
```

C26 is not:

```text
a refit of ART25
a replacement of the microscopic deuteron boundary by ART25
a conversion of published marginal bands into pseudo-replicas
a generic MSHT Hessian-to-MC exercise
a physical spin-1 or deuteron prediction
a T-odd or multiparton process package
a global likelihood or posterior package
a production promotion
```

Do not use ART25 to source-qualify the project’s microscopic deuteron parent unless a separate explicit, tested, operator-level calibration or matching map is present. An external ART25 reproduction plan and the project microscopic process plan remain distinct provenance roots.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C20-C25 reports, APIs, manifests, source locks, payload records, request documents, tests, ADRs, roadmap entries, and raw source packages before changing the repository.

Continue autonomously until every C26 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect all repository and source files;
- run tests, builders, evidence, atlas, and validators;
- access official LHAPDF, Zenodo, Git, Software Heritage, arXiv, and author-linked repositories;
- download official PDF/FF sets and metadata;
- install routine LHAPDF, Fortran, Python, and numerical dependencies when permitted;
- build source-locked isolated environments;
- execute ARTEMIDE v3.01 and official analysis scripts;
- produce deterministic parsers and adapters;
- execute all 642 joint members;
- generate deterministic manifests and numerical tables.

If the exact custom PDF ensemble or source-output bundle remains unavailable, do not substitute an approximate ensemble. Complete the audit and the delta request package.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c24_implementation_report.md
docs/next_level/c24_api.md
docs/next_level/c24_source_process_eligibility_matrix.json
docs/next_level/c24_physical_input_prerequisite_matrix.json
docs/next_level/c24_source_gate_report.json
docs/next_level/c24_unresolved_physics_gaps.md

docs/next_level/c25_implementation_report.md
docs/next_level/c25_api.md
docs/next_level/c25_requirement_coverage.json
docs/next_level/c25_normative_source_integration.json
docs/next_level/c25_official_source_acquisition_manifest.json
docs/next_level/c25_art25_git_history_manifest.json
docs/next_level/c25_art25_reproduction_source_plan.json
docs/next_level/c25_art25_payload_completeness.json
docs/next_level/c25_art25_member_schema.json
docs/next_level/c25_art25_member_validation.json
docs/next_level/c25_art25_parameter_reproduction.json
docs/next_level/c25_artemide_v301_build_manifest.json
docs/next_level/c25_v301_payload_compatibility.json
docs/next_level/c25_dataprocessor_source_manifest.json
docs/next_level/c25_frozen_benchmark_grid.json
docs/next_level/c25_source_process_eligibility_matrix.json
docs/next_level/c25_physical_input_eligibility_matrix.json
docs/next_level/c25_source_gate_report.json
docs/next_level/c25_holdout_report.json
docs/next_level/c25_regression_report.json
docs/next_level/c25_art25_author_request.md
docs/next_level/c25_art25_requested_file_schema.json
docs/next_level/c25_art25_source_gap_manifest.json
docs/next_level/c25_unresolved_physics_gaps.md

references/volume_xix_source_qualified_process_inputs.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c26_normative_source_integration.json
```

with exact hashes, roles, missing-file statuses, and supersession relations.

---

# 6. Immutable C25 baseline

Before edits, reproduce and record:

```text
1,116 tests
all C25 builders and validators
36/36 evidence rows
162/162 atlas pages
925 C25 requirements
960/960 C25 negative injections

438 analytic eligible
102 not process eligible
0 source-process eligible
0 physical-input eligible

642 stochastic ART25 members
2 technical records
644 stored rows
22 fitted NP parameters
6 fixed/model-control slots
3 collinear-member indices

exact v3.01 engine
exact official ART25 payload
nine byte-identical ART25 model files
complete C25 frozen benchmark grid

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C25 manifests byte-identical
deterministic C19-C25 validators and manifest rebuild
```

C26 must not modify:

- the exact v3.01 engine;
- the official ART25 payload;
- the `.rep` ensemble;
- C25 parameter/member semantics;
- the frozen benchmark grid;
- C24/C25 gate definitions;
- C23 analytic process plans;
- prior source and capability matrices;
- the 438/102 analytic split;
- T-odd and multiparton unavailable statuses;
- production registry, provenance, or composition;
- authoritative artifacts.

Add versioned source records and capability matrices. Do not overwrite historical manifests.

---

# 7. Official collinear-set acquisition hierarchy

## 7.1 MAPFF10NNLOPIp and MAPFF10NNLOKAp

First acquire the exact official LHAPDF sets:

```text
MAPFF10NNLOPIp
MAPFF10NNLOKAp
```

from the official CERN LHAPDF dataset archive.

For each set, preserve:

```text
archive URL
download date
tarball
tarball SHA-256
.info file
.info SHA-256
DataVersion
SetIndex
NumMembers
ErrorType
OrderQCD
flavors
x/z and Q domains
alpha_s metadata
all member files and hashes
license/source citation
archive last-modified metadata
```

The current official archive proves that sets with these exact names exist. It does not by itself prove that the current DataVersion is the exact version used in ART25.

Therefore compare:

```text
set name
DataVersion
member count
member indexing
source paper/version
file dates
ART25 constants
ART25 Lambda_i index ranges
paper/source statements
author-request checksums if supplied
```

Do not substitute:

```text
MAPFF10NNLOPIm
MAPFF10NNLOPIsum
MAPFF10NLOPIp
MAPFF10NNLOKAm
MAPFF10NNLOKAsum
MAPFF10NLOKAp
```

Accept the official current sets for source reproduction only when version compatibility with ART25 is established. Otherwise issue:

```text
OFFICIAL_CURRENT_SET_LOCATED
ART25_EXACT_SET_VERSION_UNRESOLVED
```

and keep source qualification closed.

## 7.2 MSHT20_REP

Treat:

```text
MSHT20_REP
```

as a custom ART25 source object until proven otherwise.

The standard public set:

```text
MSHT20nnlo_as118
```

contains 65 Hessian members and is not a substitute.

Search official sources in this order:

```text
ART25 repository history and deleted files
ART25 setup/constants and scripts
official DataProcessor repository/history
author-linked Zenodo deposits
MSHT repositories and data releases
LHAPDF official archive and issue history
Software Heritage
official ART25 correspondence payload
```

Possible accepted forms are:

### A. Exact official replica tarball

```text
MSHT20_REP archive
.info and member files
source hash
member ordering
generation provenance
license
```

### B. Exact official deterministic generator

A generator is acceptable only when all of the following are source locked:

```text
input MSHT20 Hessian set and exact DataVersion
conversion formalism
conversion software and exact commit
random or quasi-random matrix
seed(s)
replica count
normalization
eigenvector ordering
clipping/positivity rules
output member ordering
output .info metadata
at least one official checksum or frozen-output validation
```

Running a generic Watt–Thorne or `hessian2mc` utility without the exact ART25 conversion state is insufficient.

### C. Author-provided source payload

Accept only after hash, provenance, license, and member semantics are recorded.

No modulo mapping, nearest-member mapping, resampling, or newly generated pseudo-replica set may replace the exact ART25 member identity.

---

# 8. Collinear ensemble types and validation

Implement immutable objects equivalent to:

```text
CollinearSetSourceId
CollinearSetVersionLock
CollinearMemberId
CollinearMemberEnsemble
ART25CollinearIndexMap
ART25JointMemberId
ART25JointMemberBundle
CollinearSetCompatibilityReport
```

Each ART25 stochastic member must resolve exactly to:

```text
one ART25 NP vector
one MSHT20_REP member
one MAPFF10NNLOPIp member
one MAPFF10NNLOKAp member
```

Preserve:

```text
source set
source member number
member role
source hash
Lambda_i row
joint member ID
```

Required checks:

- every index is in range;
- no index is wrapped or clipped;
- central indices follow the source contract;
- repeated indices remain repeated;
- member ordering is deterministic;
- no member is silently replaced by a central set;
- all three collinear indices remain correlated with the same \(\Lambda_i\);
- the initialization record is not treated as a stochastic member;
- the central/mean record is not included in empirical stochastic quantiles unless the source prescription says so.

Create:

```text
docs/next_level/c26_collinear_set_inventory.json
docs/next_level/c26_art25_collinear_index_map.json
docs/next_level/c26_joint_member_validation.json
```

---

# 9. Exact ARTEMIDE v3.01 runtime

Use the immutable C25 engine/payload source plan.

Do not modify the ART25 constants to rename or substitute sets.

Initialize the engine only through one of:

```text
exact source set names available to v3.01
a source-neutral path adapter
an exact byte-identical alias certified by file hashes and source identity
```

A directory symlink or path alias is permitted only when it does not change set content, metadata, or member numbering and is recorded in the runtime manifest.

Record:

```text
LHAPDF version
LHAPDF data path
set content hashes
Fortran/Python environment
integration mode
threading
determinism controls
ARTEMIDE initialization log
DataProcessor initialization log
```

Create:

```text
docs/next_level/c26_artemide_runtime_manifest.json
```

No physics patch is permitted.

---

# 10. Official frozen-output contract

Acquire the exact frozen output bundle requested in C25, including where available:

```text
central DY outputs
central SIDIS outputs
selected stochastic-member outputs
distribution-level CS/TMDPDF/TMDFF values
chi2 or dataset-component outputs
commands/configuration used to generate each output
measurement/bin definitions
integration mode and tolerances
```

Distinguish:

```text
AUTHOR_PROVIDED_FROZEN_OUTPUT
OFFICIAL_REPOSITORY_FROZEN_OUTPUT
SOURCE_REGENERATED_FROZEN_OUTPUT
PUBLISHED_NUMERICAL_ANCHOR
NO_FROZEN_OUTPUT_AVAILABLE
```

A source-regenerated output can validate deterministic execution when all code and inputs are exact. It is not the same evidential object as an author-provided frozen output.

A source process may qualify without an author-provided table only if the unchanged gate contract permits it and there are sufficient independent published/source anchors and independent oracles. Do not weaken the gate to obtain a positive count.

Create:

```text
docs/next_level/c26_frozen_output_source_manifest.json
```

---

# 11. Frozen benchmark grid

Use the immutable C25 grid exactly.

It already covers:

```text
fixed-target DY
collider/rapidity DY
HERMES-like pion SIDIS
COMPASS-like kaon SIDIS
CS-kernel points
TMDPDF points
pion-TMDFF points
kaon-TMDFF points
```

Do not add, remove, or move benchmark points after observing residuals.

Every point retains:

```text
observable definition
process
kinematics
cuts/binning
hadron charge
normalization
member identity
source-output status
tolerance
holdout/calibration role
```

---

# 12. Distribution-level reproduction

Before process execution, reproduce:

```text
CS kernel
unpolarized TMDPDF
pion TMDFF
kaon TMDFF
```

for:

```text
central/mean member
a frozen diagnostic member subset
all 642 stochastic members when feasible
```

Required checks:

- direct model-function oracle;
- ARTEMIDE output;
- exact member-index propagation;
- small-b and large-b limits;
- scale dependence;
- domain enforcement;
- central-versus-ensemble-mean distinction;
- empirical 16/84 intervals;
- full covariance and cross-covariance;
- deterministic member-order invariance.

Report no numerical comparison to a paper figure unless an official numerical table exists.

---

# 13. Central DY reproduction

Execute the immutable frozen DY grid with:

```text
exact v3.01 engine
exact ART25 payload
exact collinear sets
central/mean ART25 member
exact source measurement definitions
exact source DataProcessor configuration
```

At minimum preserve separate results for:

```text
fixed-target DY
collider Z-region DY
rapidity/fiducial DY
```

Every comparison records:

```text
source-output status
source value
reproduced value
absolute residual
relative residual
numerical integration error
version uncertainty
normalization and units
```

Do not compare a bin center to a bin-integrated source number.

---

# 14. Central SIDIS reproduction

Execute the immutable frozen SIDIS grid with:

```text
HERMES-like pion channel
COMPASS-like kaon channel
correct hadron charge
correct z convention
correct multiplicity/cross-section definition
correct PDF/FF member indices
```

Record the same source and residual identity as for DY.

Do not substitute charge sums or negative-hadron sets for the requested positive-hadron sets.

---

# 15. Full 642-member joint execution

Execute every stochastic member in the authoritative resampling distribution.

For each member, preserve one indivisible identity:

```text
ART25 Lambda_i row
22 fitted NP parameters
6 fixed/model-control slots
MSHT20_REP index
MAPFF10NNLOPIp index
MAPFF10NNLOKAp index
CS member
TMDPDF member
pion-TMDFF member
kaon-TMDFF member
DY outputs
SIDIS outputs
distribution outputs
runtime environment
```

Required ensemble checks:

- exactly 642 stochastic members;
- no technical row enters the stochastic distribution;
- deterministic output ordering;
- serial versus parallel equality;
- restart/recovery equality;
- no member shuffle between processes;
- no independent TMDPDF/TMDFF/CS sampling;
- no independent PDF/FF resampling;
- no missing or duplicated output row;
- empirical mean and 16/84 intervals;
- covariance and cross-covariance;
- process-to-process correlations.

Create:

```text
docs/next_level/c26_full_member_execution_manifest.json
docs/next_level/c26_joint_covariance_manifest.json
```

---

# 16. Independent oracle

Provide at least two independent checks that do not simply wrap the same ARTEMIDE call:

1. direct evaluation of the ART25 nonperturbative CS/TMDPDF/TMDFF model functions;
2. independent LHAPDF evaluation of selected PDF/FF member values;
3. independent member statistics/covariance;
4. a controlled Born or normalization limit;
5. a DataProcessor-independent controlled-bin oracle.

At least one oracle must test the exact collinear member indices.

---

# 17. External ART25 plan versus microscopic project plan

Maintain two disjoint provenance roots:

```text
ART25_EXTERNAL_SOURCE_REPRODUCTION
PROJECT_MICROSCOPIC_TMD_PROCESS_PLAN
```

ART25 reproduction may establish:

```text
ART25_SOURCE_BUNDLE_VALIDATED
ART25_EXTERNAL_DY_SOURCE_VALIDATED
ART25_EXTERNAL_SIDIS_SOURCE_VALIDATED
```

It does not automatically establish:

```text
PROJECT_MICROSCOPIC_SOURCE_PROCESS_VALIDATED
PHYSICAL_DEUTERON_PROCESS_READY
```

Any bridge from ART25 to the microscopic project must be a later explicit calibration/matching/inference object with its own covariance and holdouts.

---

# 18. Unchanged gate rerun

Rerun the unchanged C24/C25 source and physical-input evaluators for:

```text
unpolarized quark/antiquark source family
quark CS/large-b source plan
unpolarized TMDPDF bundle
pion TMDFF bundle
kaon TMDFF bundle
DY_UU_UNPOLARIZED_RANK0 external ART25 plan
SIDIS_UU_UNPOLARIZED_D1_RANK0 external ART25 plan
```

Audit without forcing qualification:

```text
spin-1 LL
helicity
transversity
unpolarized gluon
linearly polarized gluon
inclusive b1
tagged DIS
heavy-quark-pair DIS
all non-NN nuclear components
```

Return every failed gate.

Preserve historical matrices and create:

```text
docs/next_level/c26_source_process_eligibility_matrix.json
docs/next_level/c26_physical_input_eligibility_matrix.json
docs/next_level/c26_gate_delta_report.json
```

Report external ART25 and microscopic-project eligibility separately.

---

# 19. Source W and W+Y status

If the exact source chain reproduces the ART25 low-\(q_T\) W terms, record:

```text
SOURCE_TMD_W_TERM_REPRODUCED
```

Construct a source-qualified W+Y record only when the exact fixed-order and asymptotic source inputs are also present and identical in:

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
perturbative order
```

Do not combine:

```text
ART25 source W
C23 analytic Y
```

If fixed-order or frozen-output inputs remain incomplete, retain:

```text
SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE
```

---

# 20. Physical-input qualification

Physical-input eligibility requires all gates defined by C24/C25, including:

```text
complete correlated ART25 members
exact collinear-member ensembles
source-qualified nonperturbative boundary
complete source/process domain
joint covariance semantics
no synthetic process object
measurement/source identity
```

Even if the external ART25 proton DY/SIDIS plan qualifies physically, this does not qualify a deuteron or spin-1 prediction.

The project microscopic physical-input tier remains separate and may stay zero.

---

# 21. Residual request package

If any required file remains absent, update rather than replace:

```text
docs/next_level/c25_art25_author_request.md
```

Create:

```text
docs/next_level/c26_art25_request_delta.md
docs/next_level/c26_requested_file_schema.json
docs/next_level/c26_source_gap_manifest.json
```

The delta request must distinguish:

```text
MAPFF sets now obtainable from official LHAPDF
exact ART25 MAPFF DataVersion/checksum still needed if unresolved
MSHT20_REP exact archive or generator state
official member-order convention
source-owned frozen outputs
exact commands/configuration
checksums
license/redistribution permission
```

Do not send the request.

---

# 22. Holdouts

Freeze holdouts before adapter or tolerance tuning.

Reserve at least:

- one MAPFF pion member and value;
- one MAPFF kaon member and value;
- one MSHT20_REP member and value;
- one ART25 joint-index triplet;
- one CS point;
- one TMDPDF point;
- one pion-TMDFF point;
- one kaon-TMDFF point;
- one fixed-target DY point;
- one collider/rapidity DY point;
- one HERMES-like SIDIS point;
- one COMPASS-like SIDIS point;
- one cross-process covariance element;
- one serial/parallel equality test;
- one exact source-output benchmark;
- one external-versus-microscopic provenance negative control.

Do not move a failed holdout into tuning without a new version and independent replacements.

---

# 23. Required benchmark families

Implement at least:

## P1B-A: official MAPFF acquisition

- exact set names;
- archive hashes;
- DataVersion;
- member counts;
- index ranges;
- ART25 version compatibility;
- wrong-charge/order/sum-set rejection.

## P1B-B: MSHT20_REP provenance

- exact custom set or exact official generator;
- standard Hessian non-substitution;
- generator state and ordering;
- generic conversion rejection.

## P1B-C: collinear index resolution

- all 642 rows;
- central and technical semantics;
- exact range;
- no wrapping or clipping;
- joint identity.

## P1B-D: runtime initialization

- exact v3.01 engine;
- constants unchanged;
- source-neutral path adapters only;
- deterministic initialization.

## P1B-E: distribution reproduction

- CS;
- TMDPDF;
- pion TMDFF;
- kaon TMDFF;
- independent model-function checks.

## P1B-F: DY central reproduction

- fixed target;
- collider;
- rapidity/fiducial;
- normalization and units.

## P1B-G: SIDIS central reproduction

- HERMES pion;
- COMPASS kaon;
- charge and z conventions;
- multiplicity definition.

## P1B-H: 642-member execution

- exact count;
- no technical rows;
- deterministic order;
- restart;
- parallel equality.

## P1B-I: joint covariance

- TMDPDF/TMDFF/CS;
- PDF/FF indices;
- DY/SIDIS cross-covariance;
- no marginal shuffling.

## P1B-J: source-output evidence

- author/repository/regenerated distinction;
- frozen commands;
- exact source anchors;
- no figure digitization.

## P1B-K: C24/C25 gate rerun

- unchanged gate logic;
- every failed gate;
- historical matrices immutable.

## P1B-L: external versus microscopic provenance

- separate roots;
- no external-fit promotion of microscopic predictions.

## P1B-M: source W/W+Y decision

- source W status;
- exact FO/asymptotic identity;
- analytic Y rejection.

## P1B-N: physical-input decision

- external ART25 plan;
- microscopic project plan;
- deuteron/spin-1 negative controls.

## P1B-O: request delta fallback

- exact missing files;
- public MAPFF resolution;
- MSHT/frozen-output residual request.

## P1B-P: deterministic isolation

- prior manifests immutable;
- no likelihood/inference;
- no production route;
- deterministic rebuild.

---

# 24. Negative injections

Create at least **1,040 ordered C26 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## MAPFF source integrity

- wrong set name;
- NLO substituted for NNLO;
- negative charge substituted;
- charge sum substituted;
- wrong DataVersion;
- missing `.info`;
- member count mismatch;
- member index out of range;
- current archive assumed identical to ART25 without proof;
- local set modified after download.

## MSHT20_REP integrity

- standard 65-member Hessian set substituted;
- central member copied 642 times;
- generic random Hessian-to-MC conversion;
- seed missing;
- transformation matrix missing;
- wrong eigenvector order;
- member count mismatch;
- set renamed without content identity;
- modulo member mapping;
- nearest-member mapping;
- pseudo-replicas generated from Hessian errors.

## ART25 joint identity

- PDF index shuffled;
- pion-FF index shuffled;
- kaon-FF index shuffled;
- TMDPDF/TMDFF/CS members independently sampled;
- technical row included;
- central row included in stochastic quantiles;
- member dropped;
- member duplicated;
- row order changed without ID;
- one process uses a different joint member.

## Runtime

- v3.02/v3.03 engine used;
- ART25 constants modified;
- set name changed in physics config;
- integration mode silently changed;
- compiler/runtime identity omitted;
- nondeterministic threading;
- physics patch hidden.

## Benchmarks

- frozen point changed after failure;
- bin center compared to bin integral;
- wrong units;
- wrong normalization;
- wrong electroweak current;
- wrong hadron charge;
- wrong z convention;
- paper figure digitized;
- central compared to mean without label;
- source-regenerated output labeled author provided.

## Covariance

- marginal covariance substituted for joint covariance;
- cross-process correlation dropped;
- PDF/FF indices ignored;
- ensemble member weights changed;
- missing members imputed;
- covariance combined with synthetic C23 bands.

## Qualification

- payload availability treated as process qualification;
- source W mixed with analytic Y;
- external ART25 reproduction treated as microscopic-model qualification;
- proton ART25 fit called deuteron prediction;
- source process called physical without gate closure;
- failed gate omitted;
- historical matrix overwritten.

## Integrity/readiness

- T-odd channel promoted;
- non-NN nuclear total constructed;
- likelihood created;
- posterior sampled;
- production registry mutated;
- authoritative artifact mutated;
- nondeterministic manifest.

---

# 25. Deliverables

Create at least:

```text
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
docs/next_level/c26_dy_central_reproduction.json
docs/next_level/c26_sidis_central_reproduction.json
docs/next_level/c26_full_member_execution_manifest.json
docs/next_level/c26_joint_covariance_manifest.json
docs/next_level/c26_independent_oracle_report.json

docs/next_level/c26_source_process_eligibility_matrix.json
docs/next_level/c26_physical_input_eligibility_matrix.json
docs/next_level/c26_gate_delta_report.json
docs/next_level/c26_source_wy_status.json

docs/next_level/c26_holdout_report.json
docs/next_level/c26_injection_manifest.json
docs/next_level/c26_regression_report.json
docs/next_level/c26_unresolved_physics_gaps.md
```

When residual source gaps remain, also create:

```text
docs/next_level/c26_art25_request_delta.md
docs/next_level/c26_requested_file_schema.json
docs/next_level/c26_source_gap_manifest.json
```

Preserve official raw sources under:

```text
data/raw/c26_sources/
```

Add ADRs for:

- official MAPFF current archive versus exact ART25 version;
- `MSHT20_REP` custom-replica identity;
- prohibition on generic Hessian-to-MC substitution;
- source-neutral set-path aliases;
- ART25 joint member propagation;
- author-provided versus source-regenerated frozen outputs;
- external ART25 versus microscopic project provenance;
- source W versus W+Y readiness.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md  # documentation only if appropriate
```

All generated JSON must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C26/P1B is complete only when:

1. The exact C25 baseline reproduces before edits.
2. The two official MAPFF set names are acquired and hash locked, or exact source failure is documented.
3. MAPFF DataVersion compatibility with ART25 is decided explicitly.
4. No wrong-charge, sum, or lower-order FF set is substituted.
5. `MSHT20_REP` is acquired exactly or remains explicitly unavailable.
6. The 65-member public MSHT20 Hessian set is never treated as the requested replica set.
7. No generic unsourced Hessian-to-MC conversion is accepted.
8. Every collinear member index resolves exactly.
9. All 642 stochastic ART25 members retain joint PDF/FF/TMD identity.
10. The two technical records retain their source-defined roles.
11. The exact v3.01 engine and ART25 constants remain unchanged.
12. Runtime initialization is deterministic and source locked.
13. The frozen benchmark grid remains immutable.
14. Distribution-level central and ensemble routes execute where inputs permit.
15. Central DY routes execute where inputs permit.
16. Central SIDIS routes execute where inputs permit.
17. All 642 stochastic members execute where the exact source chain is complete.
18. Serial, parallel, and restart outputs agree.
19. Joint covariance and cross-process covariance are preserved.
20. At least two independent source-level oracles pass.
21. Author-provided, repository-provided, and regenerated outputs are distinguished.
22. No paper figure is digitized as source data.
23. The unchanged C24/C25 gates are rerun.
24. Every failed gate remains visible.
25. External ART25 and microscopic project process statuses remain separate.
26. No ART25 proton result is called a spin-1 or deuteron prediction.
27. No source W is combined with an analytic Y.
28. Historical C23-C25 manifests remain immutable.
29. Every C26 negative injection produces the expected diagnostic.
30. All prior C3-C25 tests, builders, requirements, injections, and manifests remain passing.
31. The production registry remains exactly 216 routes.
32. All eight authoritative artifacts remain byte-identical.
33. No likelihood, posterior, inference, or production route is created.
34. All C26 manifests reproduce byte-for-byte.
35. The working tree is clean.
36. A local completion commit is created and not pushed.

C26 may complete with source-process eligibility still zero only when the exact MAPFF, MSHT, and frozen-output acquisition status is exhausted and the residual request package is complete.

---

# 27. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C26_MAPFF10NNLOPIP_OFFICIAL_SET_HASH_LOCKED
C26_MAPFF10NNLOKAP_OFFICIAL_SET_HASH_LOCKED
C26_MAPFF_ART25_VERSION_COMPATIBILITY_VALIDATED
C26_MSHT20_REP_EXACT_SOURCE_HASH_LOCKED
C26_MSHT20_REP_GENERATOR_STATE_REPRODUCED
C26_ART25_COLLINEAR_INDEX_MAP_VALIDATED
C26_ARTEMIDE_V301_RUNTIME_INITIALIZED
C26_ART25_DISTRIBUTION_BENCHMARKS_REPRODUCED
C26_ART25_DY_CENTRAL_REPRODUCED
C26_ART25_SIDIS_CENTRAL_REPRODUCED
C26_ART25_642_MEMBER_ENSEMBLE_REPRODUCED
C26_ART25_JOINT_COVARIANCE_REPRODUCED
C26_C24_C25_SOURCE_GATES_RERUN
C26_EXTERNAL_ART25_SOURCE_PROCESS_VALIDATED
C26_PHYSICAL_INPUT_PREREQUISITE_MATRIX_COMPLETE
C26_SOURCE_REQUEST_DELTA_COMPLETE
```

Issue only those whose exact gates pass.

The following remain forbidden unless every corresponding condition genuinely closes:

```text
PROJECT_MICROSCOPIC_PHYSICAL_PROCESS_READY
PHYSICAL_DEUTERON_DY_PREDICTION
PHYSICAL_DEUTERON_SIDIS_PREDICTION
PHYSICAL_TODD_PROCESS_READY
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 28. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- MAPFF pion/kaon source locations, DataVersions, member counts, and hashes;
- whether the official current MAPFF sets match the ART25 versions;
- exact `MSHT20_REP` source or exact reason it remains unavailable;
- confirmation that `MSHT20nnlo_as118` was not substituted;
- ART25 collinear index ranges and validation residuals;
- v3.01 runtime initialization status;
- frozen output source statuses;
- distribution-level reproduction residuals;
- central DY residuals;
- central SIDIS residuals;
- number of stochastic members executed;
- failed/retried member count;
- serial/parallel/restart residuals;
- covariance and cross-process covariance residuals;
- independent-oracle residuals;
- external ART25 source-process count;
- microscopic-project source-process count;
- physical-input eligibility counts;
- source W and W+Y status;
- every remaining failed gate;
- whether a request delta remains necessary;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim source-qualified execution unless the exact custom PDF replicas, exact FF sets, joint member mapping, source domain, and output validation gates all pass.
