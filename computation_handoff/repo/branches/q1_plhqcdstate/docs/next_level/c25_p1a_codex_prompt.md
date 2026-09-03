# C25/P1A Codex Work Package

## Title

**ART25 ancillary closure, exact ARTEMIDE v3.01 reproduction, correlated-member validation, and source-gate rerun**

## Authoritative baseline

Start from the local C24/P1 completion commit:

```text
91e0f6e7c2af6320827f03ad4289fbb5e724a11b
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C24 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline if the local branch is ahead of the remote.

Do not push the final completion commit.

---

# 1. Scientific reason for C25/P1A

C24 correctly preserved and audited:

```text
ARTEMIDE v3.01 Zenodo archive
ARTEMIDE v3.03 metadata as a distinct comparison release
16 primary papers
one source-qualified unpolarized-quark LO coefficient
```

but found:

```text
438 analytic-process-oracle eligible
102 not process eligible
0 source-process-validation eligible
0 physical-input eligible
```

The immediate source blocker is the missing ART25 model payload needed to reproduce the joint Drell–Yan/SIDIS extraction:

```text
model and setup/constants files
complete correlated Lambda_i ensemble
declared replica/member semantics
PDF/FF replica indices
frozen process benchmark points
```

The ART25 paper states that the ensemble of fit vectors, model code, and setup file are located in `Models/ART25` of the official artemide repository. The current official repository exposes a `Models/ART25` directory, although that directory is not present in the archived v3.01 Zenodo zip audited by C24.

C25 must recover and provenance-lock the official ART25 payload at the exact source commit, determine its compatibility with the v3.01 engine, reproduce frozen ART25 observables, and rerun every C24 source and physical-input gate.

The current master branch, v3.02, or v3.03 engine must not silently replace ARTEMIDE v3.01.

---

# 2. Primary objective

Implement the chain:

```text
official ART25 paper statement
    -> official repository history and ART25 payload
    -> exact payload commit and file hashes
    -> ARTEMIDE v3.01 engine plus source-locked ART25 model payload
    -> deterministic member parser
    -> central and correlated-member reproduction
    -> frozen DY/SIDIS benchmark reproduction
    -> C24 thirteen-gate source evaluator
    -> C24 six-gate physical-input evaluator
    -> updated source-process and physical-input capability matrices
```

The scientific objective is not to force a positive qualification result.

C25 is complete when the official payload has been obtained and validated, or when an exhaustive official-source audit proves that the required payload is still incomplete and produces an exact author/source-request package.

A positive source-process qualification may be issued only if every source gate closes.

---

# 3. Scope and nonclaims

C25 is:

```text
source-acquisition and provenance focused
version locked
member and covariance aware
reproduction based
T-even and unpolarized-first
validation only
isolated from inference and production
```

C25 is not:

```text
a refit of ART25
a reconstruction of missing replicas from published marginal errors
a digitization of paper figures
a substitution of ARTEMIDE v3.03 for v3.01
a new phenomenological TMD extraction
a global likelihood or posterior package
a physical spin-1 process prediction
a production promotion
```

Do not generate pseudo-replicas from Table 4, Fig. 3, Gaussian assumptions, or marginal uncertainties.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read every relevant C20-C24 report, API, manifest, source lock, source-gate decision, test, ADR, roadmap entry, and source archive before changing the repository.

Continue autonomously until every C25 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect the complete local git repository and source archives;
- query and clone official public git repositories;
- fetch official Zenodo, Software Heritage, GitHub, arXiv, and DataProcessor artifacts;
- inspect all tags, branches, commits, and file histories;
- preserve exact source packages locally;
- build ARTEMIDE v3.01 in an isolated environment;
- install routine compilers and dependencies when permitted;
- run official source software;
- create deterministic parsers and adapters;
- generate independent numerical checks;
- rebuild deterministic manifests.

If the official payload is absent or incomplete after all official-source paths are exhausted, do not fabricate it. Produce the exact request package specified below and retain all stronger gates as unavailable.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c23_implementation_report.md
docs/next_level/c23_api.md
docs/next_level/c23_process_capability_matrix.json
docs/next_level/c23_wy_matching_manifest.json

docs/next_level/c24_implementation_report.md
docs/next_level/c24_api.md
docs/next_level/c24_requirement_coverage.json
docs/next_level/c24_normative_source_integration.json
docs/next_level/c24_primary_source_manifest.json
docs/next_level/c24_source_package_lock_manifest.json
docs/next_level/c24_source_coefficient_library.json
docs/next_level/c24_cs_largeb_source_manifest.json
docs/next_level/c24_fragmentation_source_manifest.json
docs/next_level/c24_hard_fixed_order_source_manifest.json
docs/next_level/c24_source_process_eligibility_matrix.json
docs/next_level/c24_physical_input_prerequisite_matrix.json
docs/next_level/c24_dy_source_validation_manifest.json
docs/next_level/c24_sidis_source_validation_manifest.json
docs/next_level/c24_source_wy_manifest.json
docs/next_level/c24_holdout_report.json
docs/next_level/c24_regression_report.json
docs/next_level/c24_unresolved_physics_gaps.md

references/volume_xix_source_qualified_process_inputs.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c25_normative_source_integration.json
```

with exact hashes, source roles, and any missing-file statuses.

---

# 6. Immutable C24 baseline

Before edits, reproduce and record:

```text
1,112 tests
24 builders
36/36 evidence rows
162/162 atlas pages
825 C24 requirements
880/880 C24 negative injections

438 analytic eligible
102 not process eligible
0 source-process eligible
0 physical-input eligible

exact ARTEMIDE v3.01 archive lock
ARTEMIDE v3.03 metadata lock without substitution
16 primary-paper locks
one unpolarized-quark LO coefficient source qualified

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C24 manifests byte-identical
deterministic C19-C24 validators and manifest rebuild
```

C25 must not modify:

- the ARTEMIDE v3.01 engine archive;
- the C24 v3.03 comparison record;
- the C24 source-qualified LO coefficient;
- any C19-C24 operator or process identity;
- the C23 analytic process plans or outputs;
- C24 source-gate semantics;
- the 438/102 analytic split;
- T-odd and multiparton unavailable statuses;
- the production registry, provenance, or composition;
- authoritative artifacts.

Add new source records and supersession relations; do not overwrite historical records.

---

# 7. Official-source acquisition order

Search in this order and record every result:

## 7.1 Official artemide repository

Audit:

```text
https://github.com/VladimirovAlexey/artemide-public
```

including:

```text
master
all tags
all branches
full commit history
Models/ART25
Models/SnowART25 as a distinct and non-substitutable model
release assets
git notes/submodules/LFS pointers
deleted or renamed files
```

Use:

```text
git log --all --follow -- Models/ART25
git rev-list --all --objects
git fsck --full --no-reflogs
```

where appropriate.

Identify:

- the exact commit that first introduced `Models/ART25`;
- every later commit that modified it;
- the commit intended to correspond to the published ART25 analysis;
- whether the payload is complete at that commit;
- whether the model payload is engine-independent or tied to a later engine.

Preserve a git bundle or equivalent immutable repository snapshot and exact commit hashes.

## 7.2 Zenodo and Software Heritage

Audit:

```text
Zenodo 15006449 — ARTEMIDE v3.01
Zenodo 17153216 — ARTEMIDE v3.02
Zenodo 20638667 — ARTEMIDE v3.03
Software Heritage snapshot for v3.01
all related Zenodo versions and supplemental records
creator records and linked deposits
```

Do not use a newer engine as the ART25 engine.

A model-data payload found in a later official release may be used only as a separately versioned source artifact after its provenance and compatibility with v3.01 are demonstrated.

## 7.3 ART25 paper source

Preserve and inspect:

```text
arXiv:2503.11201v1
arXiv:2503.11201v2
published JHEP version
TeX source and any ancillary files
```

Extract the exact source contract for:

```text
Models/ART25 location
model and setup-file statement
Lambda_i member definition
central-member definition
PDF/FF replica-index semantics
fit parameter order
uncertainty/quantile prescription
declared member/replica count
ARTEMIDE v3.01 usage
DataProcessor usage
```

## 7.4 Official DataProcessor source

Follow the paper's exact official DataProcessor citation and preserve:

```text
repository URL
exact commit/tag used by ART25 if identifiable
analysis scripts
experimental datasets
configuration files
benchmark-generation scripts
member-reader implementation
```

Do not substitute an unrelated package called DataProcessor.

## 7.5 Author-provided or correspondence payload

If the official public sources remain incomplete, create the exact request package in section 21.

Do not claim acquisition until received files have hashes, license/permission status, and source provenance.

---

# 8. Two-component source identity

C25 must distinguish:

```text
ARTEMIDE_ENGINE_ID
ART25_MODEL_PAYLOAD_ID
```

The preferred source plan is:

```text
ARTEMIDE_ENGINE_ID:
    exact v3.01 Zenodo/git engine

ART25_MODEL_PAYLOAD_ID:
    exact official commit or archive containing Models/ART25
```

This is allowed only when compatibility is demonstrated.

Do not identify the current master, v3.02, or v3.03 engine as v3.01.

Create:

```text
ART25ReproductionSourcePlan
```

containing:

```text
engine version and hash
engine git commit
model payload commit and hash
payload introduction date
payload modification history
constants/setup hash
member-list hash
model-code hashes
DataProcessor commit and hashes
compiler/environment identity
compatibility evidence
source-license status
```

---

# 9. Payload completeness audit

The official payload must be audited for:

```text
model source code
setup/constants file
fit-vector/member list
parameter-order declaration
PDF member index
pion-FF member index
kaon-FF member index
central member
stochastic members
member IDs
process configuration
data-selection configuration
scale/profile settings
electroweak and mass constants
output/reader format
license and citation
```

Distinguish exactly:

```text
number of pseudo-data replica fits
number of central fits
number of stochastic Lambda_i members
number of total stored members
whether indexing begins at 0 or 1
whether "500 replicas" includes or excludes the central member
```

Do not hard-code 500 total rows until the official payload semantics are verified.

Create:

```text
docs/next_level/c25_art25_payload_completeness.json
```

with every required element and its source locator.

---

# 10. Correlated-member parser

Implement immutable types equivalent to:

```text
ART25MemberId
ART25ParameterOrder
ART25CollinearReplicaTriplet
ART25LambdaMember
ART25MemberEnsemble
ART25MemberParser
ART25MemberValidationReport
```

Each member must retain:

```text
all 22 nonperturbative parameters
PDF replica index
pion-FF replica index
kaon-FF replica index
central/stochastic role
member index
source line/record
source file hash
```

If the official payload has a different dimensionality, follow the source and document the discrepancy.

Required parser checks:

- identical dimensionality;
- complete parameter names and order;
- finite numerical values;
- unique member IDs;
- valid collinear replica indices;
- central member semantics;
- no dropped or duplicated rows;
- deterministic round trip;
- exact source-file preservation;
- ensemble content hash.

No independent Gaussian resampling is permitted.

---

# 11. Published-parameter reproduction

Using the official member ensemble, reproduce the source uncertainty prescription:

```text
mean
16th percentile
84th percentile
central-member value
correlation matrix
```

Compare against the published ART25 parameter table and correlation information.

At minimum test:

```text
c0, c1
all TMDPDF parameters
all pion-TMDFF parameters
all kaon-TMDFF parameters
```

Report separately:

```text
published rounding residual
member-parser residual
quantile residual
central-versus-mean difference
correlation residual where a numerical source is available
```

Do not use the published marginal table to generate the ensemble.

Figure-only correlation information may be used as a qualitative holdout, not a numerical covariance source, unless official numerical data are supplied.

---

# 12. ARTEMIDE v3.01 build and environment lock

Build the exact v3.01 engine in an isolated environment.

Record:

```text
operating system/container
Fortran compiler and version
compiler flags
Python version
NumPy/f2py version
BLAS/LAPACK identity
OpenMP status
integration mode
precompiled-kernel status
random seeds where relevant
floating-point mode
```

The v3.01 source says the integration mode can trade accuracy for speed. Reproduction must use the paper's source setup or audit both modes and select the documented one.

Create:

```text
docs/next_level/c25_artemide_v301_build_manifest.json
```

The build must not patch physics silently.

Every required compatibility patch must be:

```text
minimal
versioned
diff recorded
scientifically neutral
covered by a negative test
```

---

# 13. v3.01/payload compatibility

Demonstrate that the recovered ART25 payload is valid with the v3.01 engine.

Check:

```text
constants-file schema
module API
model function signatures
parameter count/order
process enumeration
TMDPDF/TMDFF initialization
PDF/FF internal library identifiers
large-x resummation option
scale/profile settings
DataProcessor/harpy interface
```

If the payload came from a later official commit:

1. identify every file-level difference relative to v3.01;
2. classify it as model data, model code, engine code, or analysis code;
3. prove that no later engine behavior is imported;
4. run an independent compatibility benchmark;
5. retain a visible compatibility remainder/status.

If compatibility cannot be proven, source qualification remains blocked.

---

# 14. Frozen reproduction points

Freeze benchmark points before adapting code.

Select source-derived points covering:

## Drell–Yan

At least:

```text
one fixed-target point
one collider Z-region point
one nontrivial rapidity or fiducial point
```

## SIDIS

At least:

```text
one HERMES-like point
one COMPASS-like point
one pion channel
one kaon or charge-separated channel if supported
```

## Distribution-level outputs

At least:

```text
one CS-kernel b point
one TMDPDF (x,b,Q) point
one pion-TMDFF (z,b,Q) point
one kaon-TMDFF point if supported
```

Use official saved tables, source scripts, or source-produced benchmark values.

Do not digitize figures.

If no numerical source output exists, freeze the input points and compare independent v3.01 executions rather than claiming paper-plot reproduction.

Create:

```text
docs/next_level/c25_frozen_benchmark_grid.json
```

before tuning any adapter.

---

# 15. Central-member reproduction

Reproduce, where source inputs permit:

```text
published central/mean parameter values
selected DY cross sections
selected SIDIS multiplicities/cross sections
selected CS-kernel values
selected TMDPDF values
selected TMDFF values
selected chi2 components
```

Every comparison must retain:

```text
source observable definition
kinematics
cuts/bin integration
member identity
engine/payload/DataProcessor IDs
integration mode
tolerance
source value
reproduced value
residual
```

Do not compare a central-member prediction with a published ensemble mean without labeling the distinction.

---

# 16. Correlated-member reproduction

Run:

```text
central member
a deterministic small diagnostic subset
all official correlated members when computationally feasible
```

The full ensemble is required for qualification unless the source contract explicitly supports an equivalent compressed representation.

Validate:

```text
mean and 68% intervals
cross-process DY/SIDIS member correlation
TMDPDF/TMDFF/CS shared-member identity
PDF/FF replica-index propagation
member-order invariance
deterministic parallel execution
```

Do not independently shuffle TMDPDF, TMDFF, CS, PDF, or FF members.

Create:

```text
docs/next_level/c25_art25_member_reproduction.json
docs/next_level/c25_art25_joint_covariance_manifest.json
```

---

# 17. Independent source-level oracle

At least one part of the reproduction must be independently implemented.

Examples:

```text
direct evaluation of the published NP model functions
independent member quantiles and covariance
independent LO/NLO normalization limit
independent b -> 0 or Q-scaling limit
DataProcessor-independent bin-center oracle for a controlled point
```

The independent oracle must not call the same ARTEMIDE routine under another wrapper.

---

# 18. C24 source-gate rerun

Rerun the unchanged C24 thirteen-gate source evaluator and six-gate physical-input evaluator for:

```text
unpolarized quark/antiquark source family
quark CS/large-b source plan
unpolarized TMDPDF bundle
unpolarized pion TMDFF bundle
unpolarized kaon TMDFF bundle
DY_UU_UNPOLARIZED_RANK0
SIDIS_UU_UNPOLARIZED_D1_RANK0
```

Audit but do not force qualification for:

```text
spin-1 LL
helicity
transversity
unpolarized gluon
linearly polarized gluon
inclusive b1
tagged DIS
heavy-quark-pair DIS
```

Return every failed gate.

Create versioned matrices:

```text
docs/next_level/c25_source_process_eligibility_matrix.json
docs/next_level/c25_physical_input_eligibility_matrix.json
```

Do not alter the historical C24 matrices.

---

# 19. Source-qualified process reproduction

Only if the corresponding source gates close, construct versioned source-validation plans for:

```text
DY_UU_UNPOLARIZED_RANK0
SIDIS_UU_UNPOLARIZED_D1_RANK0
```

These plans must use:

```text
v3.01 engine
official ART25 model payload
official correlated members
official source process setup
official DataProcessor source
source-locked measurement definitions
source-qualified hard and partner records
source-qualified CS/large-b boundary
```

Do not mix ART25 source TMDs with the C23 synthetic W/Y objects.

A source-validation plan remains separate from the project's microscopic process plan.

Do not issue a physical spin-1 or deuteron prediction from ART25.

---

# 20. Source-qualified W/Y boundary

C25 does not need to implement a full new fixed-order source package unless all required inputs are already source locked.

If an executable source W/Y chain is available, verify exact identity of:

```text
process
measurement and cuts
hard factor
TMD/TMDFF scheme
masses
scales
thresholds
rank
perturbative order
fixed-order reference
asymptotic expansion
```

Otherwise retain:

```text
SOURCE_TMD_W_TERM_REPRODUCED
SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE
```

Do not use an analytic C23 Y term inside a source-qualified plan.

---

# 21. Official-source request package

If any required ART25 files remain absent after exhaustive official-source acquisition, create:

```text
docs/next_level/c25_art25_author_request.md
docs/next_level/c25_art25_requested_file_schema.json
docs/next_level/c25_art25_source_gap_manifest.json
```

The request must ask precisely for:

```text
the exact Models/ART25 directory used for arXiv:2503.11201/JHEP publication
the setup/constants file used with ARTEMIDE v3.01
the complete Lambda_i ensemble
the parameter order
the PDF/pion-FF/kaon-FF replica-index convention
central-versus-replica count semantics
the exact ARTEMIDE and DataProcessor commits
commands for selected frozen DY/SIDIS benchmark points
license/citation/redistribution permission
checksums or a DOI/archive
```

Address the request to the paper authors using the contact information in the primary paper, but do not send it.

The package should be ready for the user to send without technical rewriting.

---

# 22. Qualification semantics

Allowed source tiers:

```text
OFFICIAL_PAYLOAD_LOCATED
OFFICIAL_PAYLOAD_HASH_LOCKED
OFFICIAL_PAYLOAD_COMPLETE
V301_PAYLOAD_COMPATIBILITY_VALIDATED
CENTRAL_MEMBER_REPRODUCED
CORRELATED_MEMBER_ENSEMBLE_REPRODUCED
ART25_SOURCE_BUNDLE_VALIDATED
SOURCE_PROCESS_VALIDATION_ELIGIBLE
PHYSICAL_PROCESS_INPUT_ELIGIBLE
```

These are not synonyms.

For example:

```text
OFFICIAL_PAYLOAD_LOCATED
```

does not imply:

```text
SOURCE_PROCESS_VALIDATION_ELIGIBLE
```

A source process may qualify while physical-input qualification remains false.

---

# 23. Holdouts

Freeze holdouts before adapter tuning.

Reserve at least:

- one ART25 parameter;
- one member-index triplet;
- one CS-kernel point;
- one TMDPDF point;
- one pion-TMDFF point;
- one kaon-TMDFF point;
- one fixed-target DY point;
- one collider/fiducial DY point;
- one HERMES-like SIDIS point;
- one COMPASS-like SIDIS point;
- one member-covariance observable;
- one v3.01/current-master compatibility diagnostic.

Do not move a failed holdout into calibration without a new version and new holdouts.

---

# 24. Required benchmark families

Implement at least:

## P1A-A: repository-history provenance

- exact ART25 introduction commit;
- modification history;
- tag/branch relations;
- official-source status;
- SnowART25 rejection.

## P1A-B: engine/payload separation

- v3.01 engine lock;
- payload commit lock;
- no v3.03 substitution;
- compatibility checks.

## P1A-C: payload completeness

- code;
- constants/setup;
- member list;
- parameter order;
- replica indices;
- licenses.

## P1A-D: member parser

- central role;
- stochastic roles;
- dimensionality;
- unique IDs;
- source round trip.

## P1A-E: member-count semantics

- central count;
- replica count;
- total count;
- zero/one indexing;
- published statement reconciliation.

## P1A-F: published parameter table

- means;
- 16/84 quantiles;
- central values;
- rounding residuals;
- correlation diagnostics.

## P1A-G: v3.01 build

- source-locked environment;
- integration mode;
- deterministic build;
- neutral-patch checks.

## P1A-H: source model functions

- independent NP-function evaluation;
- source parameter order;
- limits and domain.

## P1A-I: DY central reproduction

- fixed-target;
- collider;
- fiducial/rapidity;
- source normalization.

## P1A-J: SIDIS central reproduction

- HERMES;
- COMPASS;
- pion;
- kaon/charge channel.

## P1A-K: full correlated ensemble

- all members;
- mean and bands;
- shared member identity;
- deterministic parallel order.

## P1A-L: DataProcessor source lock

- exact official repository;
- commit/tag;
- datasets;
- scripts;
- no unrelated package.

## P1A-M: C24 source-gate rerun

- all thirteen gates;
- every failed gate;
- historical matrices immutable.

## P1A-N: physical-input gate

- joint covariance;
- domain;
- no synthetic inputs;
- positive/negative controls.

## P1A-O: author-request fallback

- exact requested files;
- no fabrication;
- ready-to-send technical request.

## P1A-P: deterministic isolation

- all manifests deterministic;
- no inference or production;
- prior artifacts unchanged.

---

# 25. Negative injections

Create at least **960 ordered C25 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## Provenance

- unofficial fork;
- wrong ART25 commit;
- unverified current-master snapshot;
- SnowART25 substituted;
- v3.03 engine substituted;
- v3.02 engine substituted;
- payload hash missing;
- git history truncated;
- local file edited after acquisition.

## Payload

- constants missing;
- model code missing;
- member list missing;
- parameter order missing;
- PDF/FF index columns missing;
- license missing;
- duplicate member;
- dropped member;
- reordered member without ID;
- central member missing;
- central member duplicated;
- central/replica count conflated.

## Member semantics

- 500 assumed without source;
- central included/excluded incorrectly;
- parameter dimensionality mismatch;
- PDF/FF indices shuffled;
- TMDPDF/TMDFF/CS members independently sampled;
- Gaussian pseudo-replicas generated from Table 4;
- correlation reconstructed from Figure 3.

## Engine/build

- compiler/version unrecorded;
- integration mode changed;
- physics patch hidden;
- constants schema silently adapted;
- current engine used;
- later process enumeration imported;
- nondeterministic build.

## Reproduction

- central compared to mean without label;
- paper plot digitized;
- mismatched cuts;
- mismatched normalization;
- wrong hadron charge;
- wrong SIDIS z convention;
- wrong DY electroweak current;
- benchmark selected after tuning;
- holdout reused.

## Qualification

- payload located treated as process qualified;
- central-only treated as covariance qualified;
- partial members treated as full ensemble;
- source W mixed with analytic Y;
- source process claimed physical;
- ART25 proton fit called deuteron prediction;
- C24 gate weakened;
- failed gate omitted.

## Integrity

- historical C24 matrix overwritten;
- C23 analytic plan overwritten;
- T-odd channel promoted;
- nuclear matched total created;
- likelihood/inference created;
- production registry mutated;
- authoritative artifact mutated;
- nondeterministic manifest.

---

# 26. Deliverables

Create at least:

```text
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
docs/next_level/c25_art25_central_reproduction.json
docs/next_level/c25_art25_member_reproduction.json
docs/next_level/c25_art25_joint_covariance_manifest.json
docs/next_level/c25_dy_reproduction_manifest.json
docs/next_level/c25_sidis_reproduction_manifest.json
docs/next_level/c25_source_process_eligibility_matrix.json
docs/next_level/c25_physical_input_eligibility_matrix.json
docs/next_level/c25_source_gate_report.json
docs/next_level/c25_holdout_report.json
docs/next_level/c25_injection_manifest.json
docs/next_level/c25_regression_report.json
docs/next_level/c25_unresolved_physics_gaps.md
```

When needed, also create:

```text
docs/next_level/c25_art25_author_request.md
docs/next_level/c25_art25_requested_file_schema.json
docs/next_level/c25_art25_source_gap_manifest.json
```

Preserve official raw sources under:

```text
data/raw/c25_sources/
```

Add ADRs for:

- v3.01 engine versus later model-payload commits;
- official repository-history provenance;
- central/replica count semantics;
- ART25 joint-member identity;
- source benchmark selection;
- source-gate rerun;
- author-request fallback.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md  # documentation only if appropriate
```

All generated JSON must reproduce byte-for-byte.

---

# 27. Acceptance criteria

C25/P1A is complete only when:

1. The exact C24 baseline reproduces before edits.
2. Every official acquisition path is audited.
3. The exact ART25 introduction and payload commits are identified.
4. The v3.01 engine remains byte-identical.
5. No v3.02/v3.03 engine is substituted.
6. The ART25 payload is hash locked or explicitly proven incomplete.
7. Engine and model-payload identities are separate.
8. The constants/setup file is identified and parsed.
9. The official member ensemble is identified and parsed.
10. Central, replica, and total member counts are reconciled from source.
11. Parameter order and PDF/FF replica-index semantics are complete.
12. No pseudo-replica reconstruction is used.
13. Published parameter means and intervals are reproduced where the payload permits.
14. ARTEMIDE v3.01 builds reproducibly.
15. Payload/v3.01 compatibility is demonstrated or fails closed.
16. Frozen benchmark points are selected before tuning.
17. Central DY and SIDIS benchmark routes are reproduced where source outputs permit.
18. Correlated-member propagation is validated.
19. TMDPDF, TMDFF, CS, PDF, and FF member identity remains joint.
20. An independent source-level oracle passes.
21. The unchanged C24 source and physical gates are rerun.
22. Every failed source/physical gate remains visible.
23. Historical C23/C24 records remain immutable.
24. No T-odd or multiparton channel is promoted.
25. No spin-1 or complete-deuteron physical claim is made from ART25.
26. If public sources are incomplete, the exact author-request package is produced.
27. Every C25 negative injection produces the expected diagnostic.
28. All prior C3-C24 tests, builders, requirements, injections, and manifests remain passing.
29. The production registry remains exactly 216 routes.
30. All eight authoritative artifacts remain byte-identical.
31. No likelihood, posterior, inference, or production route is created.
32. All C25 manifests reproduce byte-for-byte.
33. The working tree is clean.
34. A local completion commit is created and not pushed.

C25 may complete with source-process eligibility still zero only if the official-source audit and fallback request package are complete and the remaining blockers are exact.

---

# 28. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C25_ART25_OFFICIAL_PAYLOAD_LOCATED
C25_ART25_PAYLOAD_HASH_LOCKED
C25_ART25_PAYLOAD_COMPLETE
C25_ARTEMIDE_V301_BUILD_REPRODUCED
C25_V301_ART25_PAYLOAD_COMPATIBILITY_VALIDATED
C25_ART25_MEMBER_ENSEMBLE_VALIDATED
C25_ART25_PARAMETER_TABLE_REPRODUCED
C25_ART25_DY_SIDIS_BENCHMARKS_REPRODUCED
C25_ART25_JOINT_MEMBER_COVARIANCE_VALIDATED
C25_C24_SOURCE_GATES_RERUN
C25_SOURCE_PROCESS_ELIGIBILITY_MATRIX_COMPLETE
C25_PHYSICAL_INPUT_PREREQUISITE_MATRIX_COMPLETE
C25_ART25_SOURCE_REQUEST_PACKAGE_COMPLETE
```

Issue these only when their exact gates pass.

The following remain forbidden unless every corresponding condition genuinely closes:

```text
PHYSICAL_TMD_EXTRACTION
PHYSICAL_DRELL_YAN_PREDICTION
PHYSICAL_SIDIS_PREDICTION
PHYSICAL_SPIN1_PROCESS_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 29. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- all official source paths audited;
- exact ART25 payload commit and history;
- exact v3.01 engine identity;
- whether payload and engine came from different commits;
- payload file inventory and hashes;
- constants/setup status;
- central/stochastic/total member counts;
- parameter dimensionality and replica-index semantics;
- published parameter-table residuals;
- v3.01 build environment and build status;
- compatibility residual/status;
- frozen benchmark points;
- central DY/SIDIS reproduction residuals;
- full-ensemble reproduction and covariance residuals;
- independent-oracle residuals;
- updated source-process and physical-input counts;
- every remaining failed gate;
- whether an author-request package was required;
- unresolved source files if any;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim a source-qualified process chain unless the official payload, v3.01 compatibility, member ensemble, source uncertainty, and process reproduction gates all pass.
