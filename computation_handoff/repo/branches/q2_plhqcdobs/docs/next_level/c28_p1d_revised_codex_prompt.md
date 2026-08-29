# C28/P1D Codex Work Package — Revised After the Native CDF1 Diagnostic

## Title

**Complete public ART25 dataset reproduction, nuisance-aware ensemble covariance, source-reproducible low-\(q_T\) process validation, and \(W+Y\) readiness audit**

## Authoritative baseline

Start from the local native-DataProcessor diagnostic commit:

```text
97e1aa2dce86925002bd2f6c5e0bad91390446ac
```

Its required scientific C27/P1C ancestor is:

```text
f95171d3e87203fe2dcfa2d155c87b4c27c8d171
```

A documentation-only descendant is acceptable only when both commits remain in its ancestry and the complete C27 plus CDF1-diagnostic baseline reproduces before any scientific changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

Do not execute the older C28 prompt. Preserve it as a historical superseded work package if it is already present.

Do not push the final completion commit.

---

# 1. Why this revised package is required

The native CDF1 diagnostic closes several questions that the earlier C28 plan still treated as unresolved.

The public `VladimirovAlexey/artemide-DataProcessor` repository is sufficient for an unambiguous source-regenerated process diagnostic. The current public checkout is:

```text
9f9dda71b69dd26e288be189a396736827cfeed3
```

and the public history contains the ART25 analysis update:

```text
761f3fcdd3701c5cf69e822f9ffbbd5db394fc58
```

including the public ART25 dataset list and cut function.

The public file:

```text
DataLib/unpolDY/CDF1.csv
```

has SHA-256:

```text
c0a178d9579017a7de91abf63df667d1bb3009253ce15b56fe428d32fc430c81
```

The native loader returns 50 points, and the public ART25 selection retains exactly:

```text
CDF1.0 through CDF1.32
```

The immutable native benchmark is:

```text
point:
    CDF1.0

process:
    [1, 1, -1, 3]

sqrt(s):
    1800 GeV

qT bin:
    [0, 0.5] GeV

Q bin:
    [66, 116] GeV

rapidity:
    full physical range through the source sentinel [-1000, 1000]

experimental value:
    3.35 +/- 0.54

raw ARTEMIDE bin integral:
    1.7197438402188676

theory factor:
    2 GeV^-1

native DataProcessor prediction:
    3.4394876804377352 pb/GeV
```

The native result is:

```text
absolute
not theory normalized
integrated over qT, Q^2, and physical rapidity
divided by the qT-bin width through the stored theory factor
leading-power resummed TMD W term
N4LO hard coefficient in the declared ARTEMIDE setup
no fixed-order Y term
no W+Y matching
```

Repeated serial execution, clean ARTEMIDE reinitialization, the C27 restart route, and direct raw-engine-bin-integral times the stored theory factor all agree exactly.

All 33 selected CDF1 points execute successfully.

Therefore C28 must no longer spend time rediscovering whether native DataProcessor execution works. It must promote that route into immutable source regression and extend it to the complete public ART25 dataset and statistical-analysis layer.

---

# 2. Scientific starting point inherited from C27

C27 already establishes:

```text
author-supplied MSHT20_REP DataVersion 3
metadata plus grid files 0000 through 1000
ART25 uses exact PDF indices 0 through 999
grid 1000 preserved but excluded

MAPFF10NNLOPIp DataVersion 1
MAPFF10NNLOKAp DataVersion 1

642 stochastic ART25 members
2 technical records
all joint PDF/pion-FF/kaon-FF indices resolved exactly

unchanged ARTEMIDE v3.01 engine
unchanged ART25 physics constants
source-neutral absolute-path adapter only

642 stochastic members completed
0 failed
0 imputed
serial == four-process parallel == restart

39-dimensional joint covariance
symmetric
positive semidefinite within numerical precision

SOURCE_REGENERATED_OUTPUT
SOURCE_TMD_W_TERM_REPRODUCED
SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE
```

The external ART25 source-process, external physical-input, microscopic-project source-process, and microscopic-project physical-input eligibility counts remain zero under the stronger historical qualification contracts.

C28 must preserve those historical statuses and add a narrower, accurately named public-source-reproducibility tier rather than weakening the existing full source-process or physical-input gates.

---

# 3. Primary objective

Implement the chain:

```text
exact C27 ART25 joint member
    -> exact public ART25 DataProcessor commit
    -> exact source dataset and native loader
    -> exact source point selection and cuts
    -> exact native bin integration and theory factor
    -> central predictions for every retained ART25 point
    -> native nuisance and chi2 treatment
    -> all 642 members over the complete retained dataset
    -> exact low-rank theory-covariance representation
    -> source-reproducible low-qT W process qualification
    -> fixed-order/asymptotic partner audit
    -> full W+Y readiness decision
```

The core scientific deliverable is a source-reproducible dataset-level ART25 ensemble, not another isolated benchmark point.

C28 must determine, from the public source code and executed semantics:

```text
which datasets ART25 uses
which points are retained
why excluded points are excluded
what observable every native theory call returns
how normalization and correlated systematic errors are represented
how nuisance parameters are profiled or otherwise treated
how dataset and global chi2 are defined
how all 642 correlated source members propagate through every point
whether any source-identical fixed-order/asymptotic partner exists
```

---

# 4. Scope and nonclaims

C28 is:

```text
public-source reproducible
dataset and point resolved
measurement and binning aware
nuisance and covariance aware
member correlated
low-qT W focused
version locked
validation only
external ART25 provenance only
```

C28 is not:

```text
a refit of ART25
a new global extraction
an author-frozen reproduction unless an author-owned anchor is actually supplied
a full W+Y calculation unless exact fixed-order/asymptotic identity closes
a replacement of the microscopic model by ART25
a spin-1 or deuteron process prediction
a likelihood or posterior for the microscopic model
a T-odd or multiparton process package
a production promotion
```

Do not use a successful external proton ART25 reproduction to qualify any microscopic nucleon, deuteron, spin-1, non-NN nuclear, or matched-total process.

---

# 5. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C23-C27 reports, APIs, source locks, runtime manifests, point and member manifests, covariance records, negative tests, source files, DataProcessor history, ART25 analysis scripts, and roadmap entries before changing the repository.

Continue autonomously until every applicable C28 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository content and complete git histories;
- preserve official source commits, datasets, and scripts;
- install routine source-locked dependencies;
- execute the exact ARTEMIDE v3.01 and DataProcessor chain;
- load every public ART25 dataset natively;
- evaluate every retained point;
- execute all 642 members with deterministic checkpointing;
- compute nuisance profiles and native chi2 values;
- construct scalable covariance factors and block queries;
- audit fixed-order and asymptotic source candidates;
- rebuild deterministic manifests.

Do not contact the authors during this package.

Do not digitize figures.

Do not change frozen points, cuts, tolerances, or holdouts after seeing results.

---

# 6. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c23_implementation_report.md
docs/next_level/c23_api.md
docs/next_level/c23_process_capability_matrix.json
docs/next_level/c23_wy_matching_manifest.json

docs/next_level/c24_implementation_report.md
docs/next_level/c24_api.md
docs/next_level/c24_source_process_eligibility_matrix.json
docs/next_level/c24_physical_input_prerequisite_matrix.json

docs/next_level/c25_implementation_report.md
docs/next_level/c25_art25_reproduction_source_plan.json
docs/next_level/c25_art25_member_schema.json
docs/next_level/c25_art25_member_validation.json
docs/next_level/c25_frozen_benchmark_grid.json

docs/next_level/c26_implementation_report.md
docs/next_level/c26_mapff_pion_source_lock.json
docs/next_level/c26_mapff_kaon_source_lock.json
docs/next_level/c26_art25_collinear_index_map.json
docs/next_level/c26_gate_delta_report.json

docs/next_level/c27_implementation_report.md
docs/next_level/c27_api.md
docs/next_level/c27_requirement_coverage.json
docs/next_level/c27_incoming_source_manifest.json
docs/next_level/c27_msht20_rep_source_lock.json
docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_joint_member_validation.json
docs/next_level/c27_artemide_v301_runtime_manifest.json
docs/next_level/c27_distribution_reproduction_manifest.json
docs/next_level/c27_dy_central_reproduction.json
docs/next_level/c27_sidis_central_reproduction.json
docs/next_level/c27_full_member_execution_manifest.json
docs/next_level/c27_joint_covariance_manifest.json
docs/next_level/c27_source_wy_status.json
docs/next_level/c27_source_process_eligibility_matrix.json
docs/next_level/c27_physical_input_eligibility_matrix.json
docs/next_level/c27_gate_delta_report.json
docs/next_level/c27_regression_report.json
docs/next_level/c27_unresolved_physics_gaps.md

docs/next_level/c27_cdf1_smoke_test.md
docs/next_level/c27_cdf1_dataset_manifest.json
docs/next_level/c27_cdf1_native_prediction.json
docs/next_level/c27_cdf1_code_path_manifest.json
docs/next_level/c27_cdf1_comparison_report.json

references/volume_xix_source_qualified_process_inputs.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c28_normative_source_integration.json
```

with exact hashes, source roles, missing-file statuses, and supersession relations.

---

# 7. Immutable baseline reproduction

Before edits, reproduce and record:

```text
1,127 tests
all C27 and CDF1 builders and validators
36/36 evidence rows
162/162 atlas pages
1,120/1,120 inherited C27 negative injections

C27:
    642 stochastic members
    0 failed
    0 imputed
    serial/parallel/restart equality
    39-dimensional covariance
    SOURCE_TMD_W_TERM_REPRODUCED
    SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE

CDF1:
    DataProcessor current commit 9f9dda71b69dd26e288be189a396736827cfeed3
    ART25 public commit 761f3fcdd3701c5cf69e822f9ffbbd5db394fc58
    CDF1 SHA-256 c0a178d9579017a7de91abf63df667d1bb3009253ce15b56fe428d32fc430c81
    50 loaded points
    33 ART25-retained points
    exact CDF1.0 value 3.4394876804377352 pb/GeV
    all determinism residuals zero

capability:
    438 analytic-process-oracle eligible
    102 not process eligible
    historical full source-process eligibility 0
    historical physical-input eligibility 0

integrity:
    production registry exactly 216
    all eight authoritative artifacts byte-identical
    all pinned C15-C27 manifests byte-identical
    deterministic C19-C27 manifest reconstruction
```

Do not proceed if the CDF1 native benchmark does not reproduce exactly.

C28 must not modify:

- ARTEMIDE v3.01;
- ART25 physics constants;
- MSHT20_REP;
- either MAPFF archive;
- ART25 member rows;
- the C25/C27 frozen diagnostic grids;
- CDF1.csv;
- the CDF1.0 benchmark identity or value;
- C24-C27 qualification semantics;
- historical capability matrices;
- C23 analytic process plans;
- microscopic/nuclear model identities;
- production registry or authoritative artifacts.

---

# 8. Required architecture

Extend the typed process and provenance system. Do not create a parallel untyped analysis stack.

Implement or extend objects equivalent to:

```text
DataProcessorRepositoryId
DataProcessorCommitLock
DataProcessorVersionComparison

ART25AnalysisSourceId
ART25DatasetList
ART25SelectionRule
ART25SelectionDecision

DatasetSourceId
DatasetFileLock
DatasetMetadata
DatasetPointId
DatasetPointRecord
MeasurementConvention
TheoryFactorRecord
NativeIntegrationSemantics

ExperimentalErrorRecord
CorrelatedSystematicRecord
NormalizationNuisanceRecord
ExperimentalCovarianceBundle
NativeChi2Definition
NativeNuisanceProfile

ART25CentralPrediction
ART25PointPrediction
ART25DatasetPredictionBundle
ART25MemberDatasetPrediction
ART25FullDatasetEnsemble

TheoryEnsembleFactor
TheoryCovarianceQuery
TheoryCovarianceBlock
TheoryExperimentalCovarianceSeparation

SourceReproducibleLowQtContract
SourceReproducibleLowQtEligibility
FixedOrderPartnerRecord
AsymptoticPartnerRecord
WYReadinessRecord

C28DatasetClosureReport
C28RegressionAuthority
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about repository and source commit;
- explicit about point, bin, units, process, and theory factor;
- explicit about member identity;
- fail-closed on missing source identity;
- isolated from inference and production.

---

# 9. DataProcessor source locking

## 9.1 Historical ART25 route

Treat:

```text
761f3fcdd3701c5cf69e822f9ffbbd5db394fc58
```

as the authoritative public ART25 analysis commit for:

```text
dataset list
selection and cut logic
analysis scripts
measurement construction
theory-call route
```

Preserve a complete git bundle or immutable source archive.

Record all relevant file hashes.

## 9.2 Current public comparison

Treat:

```text
9f9dda71b69dd26e288be189a396736827cfeed3
```

as a separate current-public comparison route.

Compare historical ART25 and current-public behavior for:

```text
dataset files
point IDs
dataset metadata
selection logic
process codes
normalization
theory factors
bin integration
covariance/error handling
chi2 implementation
nuisance handling
harpy interface
```

Do not silently use current `master` as the historical ART25 source.

## 9.3 Version-delta report

Create:

```text
docs/next_level/c28_dataprocessor_source_lock.json
docs/next_level/c28_dataprocessor_version_comparison.json
```

Classify every relevant difference as:

```text
BYTE_IDENTICAL
METADATA_ONLY
NUMERICALLY_EQUIVALENT
SCIENTIFICALLY_RELEVANT
UNRESOLVED
```

---

# 10. CDF1 as immutable source regression

Promote the successful diagnostic into a permanent regression authority.

Create a typed record for:

```text
CDF1.0
```

containing all source and observable semantics listed in section 1.

Required exact identities:

```text
raw integral:
    1.7197438402188676

theory factor:
    2.0

native result:
    3.4394876804377352

raw integral * theory factor - native result:
    0

serial residual:
    0

reinitialization residual:
    0

restart residual:
    0
```

The regression must also verify:

```text
50 total CDF1 points
33 retained ART25 points
retained IDs CDF1.0 through CDF1.32
one 3.9% normalization error
one uncorrelated error per point
no point-to-point correlated error
isNormalized = false
```

Create:

```text
docs/next_level/c28_cdf1_regression_authority.json
```

No C28 change may alter this result.

---

# 11. Complete ART25 dataset inventory

Recover the complete dataset lists from the historical ART25 analysis source.

Load every referenced dataset with the native DataProcessor loader.

Classify separately:

```text
unpolarized Drell-Yan
unpolarized SIDIS
any source-listed auxiliary or validation datasets
```

For each dataset record:

```text
dataset name
source filename
file SHA-256
source commit
reference
process type
process codes
beam and target
hadron species and charge
number of points
normalization errors
isNormalized
uncorrelated error count
correlated systematic count
point IDs
kinematic variables
bin edges
representative values
includeCuts
cutParams
theory factors
weight-process metadata
units
source publication
```

Create:

```text
docs/next_level/c28_art25_dataset_inventory.json
docs/next_level/c28_dataset_file_lock_manifest.json
docs/next_level/c28_measurement_semantics_manifest.json
```

Do not manually reinterpret CSV fields when the native loader provides their semantics.

---

# 12. Exact ART25 selection and cut reproduction

Execute the historical ART25 dataset list and cut function exactly.

For every point record:

```text
dataset ID
point ID
selected or rejected
all evaluated cut quantities
ordered cut decisions
final reason
source function and line
source commit
```

Required checks:

- exact selected dataset count;
- exact total point count;
- exact retained point count;
- exact excluded point count;
- no off-by-one inequality;
- no current-master cut substitution;
- no unit mismatch;
- no missing point ID;
- deterministic order;
- CDF1.0 through CDF1.32 retained exactly.

Create:

```text
docs/next_level/c28_art25_selection_manifest.json
docs/next_level/c28_selection_reason_ledger.json
docs/next_level/c28_selection_version_delta.json
```

The selected-point set must be frozen before central or ensemble evaluation.

---

# 13. Native observable semantics

Trace the executed DataProcessor/harpy code path for each process and dataset class.

For every native observable determine:

```text
bin integrated or bin center
integration variables
physical support clipping
theory-factor action
absolute or normalized
cross section or multiplicity
units
electroweak normalization
hard-factor order
W-only or W+Y
fiducial cuts
hadron charge
z convention
normalization convention
numerical integration mode
tolerance
```

Do not infer semantics from names alone.

Required process-specific audits:

## Drell-Yan

Trace:

```text
DataProcessor.harpyInterface
harpy.DY.xSecList or actual executed equivalent
qT, Q^2, and rapidity integration
fiducial-cut branches
theory factor
```

## SIDIS

Trace:

```text
DataProcessor.harpyInterface
harpy.SIDIS native route
x, z, Q^2, and transverse-momentum integration
multiplicity or cross-section normalization
hadron charge
target identity
theory factor
```

Create:

```text
docs/next_level/c28_native_code_path_manifest.json
docs/next_level/c28_observable_semantics_manifest.json
```

Any unresolved observable semantics fail the corresponding point before process qualification.

---

# 14. Central prediction over the complete retained dataset

Using the exact central/mean ART25 technical record, evaluate every retained point.

For each point preserve:

```text
dataset ID
point ID
joint central member ID
complete kinematic bin
representative values
native experimental value
experimental errors
native theory value
theory factor
units
observable semantics
integration status
runtime ID
source commit
absolute residual
relative residual
pull ingredients
```

Do not treat data residuals as a refit objective.

Do not change source parameters.

Required execution checks:

- all retained points attempted;
- every completed point recorded;
- every failure typed;
- no failure silently dropped;
- serial/reinitialization/restart checks on a frozen subset;
- current-public comparison on a frozen subset;
- CDF1.0 exact regression.

Create:

```text
docs/next_level/c28_central_point_predictions.json
docs/next_level/c28_central_dataset_prediction_manifest.json
docs/next_level/c28_central_execution_failure_manifest.json
```

Large point tables may be stored as deterministic Parquet or another content-addressed machine-readable format under a non-public runtime/output directory. Commit the schema, hashes, row counts, summaries, and selected regression rows.

---

# 15. Native experimental error and nuisance semantics

Do not replace DataProcessor’s statistical treatment with a generic covariance formula.

Inspect and execute the exact source implementation for:

```text
uncorrelated errors
point-to-point correlated errors
normalization errors
normalization nuisance
systematic shifts
covariance or nuisance-matrix construction
chi2
best-normalization logic
profiled shifts
dataset combination
global combination
```

For every dataset record:

```text
native error model
number of nuisance directions
normalization convention
covariance representation
profile or marginalization status
chi2 components
source function and line
```

Where the source implementation admits equivalent matrix and nuisance representations, validate both independently.

Create:

```text
docs/next_level/c28_experimental_error_model_manifest.json
docs/next_level/c28_normalization_nuisance_manifest.json
docs/next_level/c28_native_chi2_definition.json
```

---

# 16. Dataset and global chi2 reproduction

Using only the native source definitions, compute:

```text
per-dataset chi2
per-point residual contribution where defined
uncorrelated contribution
correlated-systematic contribution
normalization penalty
profiled nuisance values
global DY chi2
global SIDIS chi2
combined ART25 chi2 when source-defined
point counts and degrees-of-freedom conventions
```

Distinguish:

```text
raw central-member chi2
ensemble-mean-prediction chi2
mean of member chi2
published-fit chi2 if source anchored
```

These are not interchangeable.

Do not claim reproduction of a published number when no source numerical anchor exists.

Create:

```text
docs/next_level/c28_central_chi2_manifest.json
docs/next_level/c28_nuisance_profile_manifest.json
docs/next_level/c28_global_chi2_manifest.json
```

---

# 17. Full 642-member dataset execution

Execute every stochastic ART25 member over every retained point.

For each member preserve one indivisible identity:

```text
Lambda_i row
22 fitted NP parameters
6 fixed/model-control slots
MSHT20_REP index
MAPFF pion index
MAPFF kaon index
CS-kernel member
TMDPDF member
pion-TMDFF member
kaon-TMDFF member
all point predictions
all dataset chi2 values
all nuisance profiles
runtime and checkpoint identity
```

The execution system must support:

```text
deterministic serial reference
deterministic multiprocess execution
checkpoint/restart
content-addressed shards
per-member failure records
deterministic merge
```

Required checks:

- 642 stochastic members attempted;
- 642 completed when the source chain supports every selected point;
- zero imputed members;
- no technical record in stochastic statistics;
- no member shuffle between datasets or processes;
- serial/parallel equality on frozen shards;
- restart/uninterrupted equality;
- deterministic member and point order;
- no duplicate or missing rows.

Create:

```text
docs/next_level/c28_full_dataset_member_execution.json
docs/next_level/c28_member_execution_failure_manifest.json
docs/next_level/c28_checkpoint_restart_manifest.json
```

Heavy raw outputs remain outside Git unless explicitly appropriate. Preserve exact hashes and schemas.

---

# 18. Scalable exact theory covariance

Do not require a dense \(N_{\rm point}\times N_{\rm point}\) covariance file when it is unnecessarily large.

Construct the exact empirical anomaly factor:

\[
A_{is}
=
\frac{T_{is}-\overline T_i}{\sqrt{N_{\rm member}-1}},
\]

so that:

\[
C_{\rm theory}=AA^T.
\]

Store the member-by-point anomaly factor or an exactly equivalent content-addressed representation.

Implement typed block queries for:

```text
point variances
within-dataset covariance
cross-dataset covariance
DY-DY covariance
SIDIS-SIDIS covariance
DY-SIDIS covariance
distribution-process covariance where the C27 distribution points are included
chi2 covariance
nuisance-profile covariance
```

Required checks:

- covariance symmetry;
- positive semidefiniteness within tolerance;
- direct dense reconstruction on frozen blocks;
- exact agreement with selected empirical covariance calculations;
- permutation covariance when member IDs are retained;
- failure under marginal member reshuffling;
- no independent PDF/FF/TMD member sampling.

Create:

```text
docs/next_level/c28_theory_ensemble_factor_manifest.json
docs/next_level/c28_theory_covariance_query_manifest.json
docs/next_level/c28_selected_covariance_blocks.json
docs/next_level/c28_cross_process_covariance_report.json
```

---

# 19. Separation of theory and experimental covariance

Preserve independently:

```text
ART25 source-member theory covariance
experimental statistical/uncorrelated covariance
experimental correlated-systematic covariance
normalization-nuisance structure
numerical integration uncertainty
source-version uncertainty
```

Do not combine them into one likelihood covariance in C28.

Implement a typed separation manifest that records how they could later be assembled without actually creating an inference route.

Create:

```text
docs/next_level/c28_covariance_separation_manifest.json
```

---

# 20. Source-reproducible low-qT W qualification

Introduce a new, narrower evidential tier:

```text
SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION
```

This tier requires:

```text
exact public source repository and commit
exact source engine and model payload
exact source member ensembles
exact native dataset loader
exact source dataset file
exact source selection and cuts
complete measurement semantics
native bin integration and theory factor
deterministic central execution
complete 642-member execution or an explicitly scoped member-complete subset
joint member covariance
low-qT factorization/W-term identity
no synthetic process object
```

It does not require:

```text
author-frozen numerical output
fixed-order asymptotic partner
Y term
full W+Y
physical deuteron input
microscopic-project bridge
```

It must remain distinct from:

```text
SOURCE_ANCHORED_LOWQT_W_VALIDATION
SOURCE_PROCESS_VALIDATION_ELIGIBLE
PHYSICAL_PROCESS_INPUT_ELIGIBLE
```

Create:

```text
docs/next_level/c28_lowqt_source_reproducibility_contract.json
docs/next_level/c28_lowqt_source_reproducibility_matrix.json
```

Classify independently by:

```text
dataset
point
process
observable semantics
member completeness
source version
```

The existing stronger source-process and physical-input gates must not be weakened or overwritten.

---

# 21. Author-frozen anchor status

The public source route now works without another email.

Continue to distinguish:

```text
AUTHOR_PROVIDED_FROZEN_OUTPUT
OFFICIAL_REPOSITORY_FROZEN_OUTPUT
SOURCE_REGENERATED_OUTPUT
PUBLISHED_NUMERICAL_ANCHOR
NO_SOURCE_NUMERICAL_ANCHOR
```

Audit the repository for existing numerical anchors, but do not contact authors.

Do not block the new source-reproducible tier solely because author-frozen outputs are absent.

Do not issue an author-anchored status without an actual author- or repository-owned numerical anchor.

Create:

```text
docs/next_level/c28_source_anchor_status.json
```

---

# 22. Fixed-order and asymptotic partner audit

Audit Drell-Yan and SIDIS separately.

For every candidate fixed-order or asymptotic partner record:

```text
process
external states
measurement
cuts
binning
hard current
electroweak normalization
TMD/TMDFF/soft scheme
mass treatment
renormalization/factorization scales
threshold history
rank
harmonic
perturbative order
software version
source paper/code
source reproducibility
numerical benchmark
```

Search the ARTEMIDE/DataProcessor source first.

Then audit exact source candidates cited by the ART25 and process papers.

Do not use:

```text
C23 analytic fixed-order oracle
C23 analytic Y term
a mismatched inclusive fixed-order result
a different fiducial definition
a different TMD/soft scheme
```

Create:

```text
docs/next_level/c28_dy_fixed_order_partner_manifest.json
docs/next_level/c28_sidis_fixed_order_partner_manifest.json
docs/next_level/c28_asymptotic_partner_manifest.json
docs/next_level/c28_wy_readiness_matrix.json
```

---

# 23. W versus W+Y decision

For every supported source-reproducible point or dataset record one of:

```text
SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION
SOURCE_ANCHORED_LOWQT_W_VALIDATION
SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE
SOURCE_WY_IDENTITY_MISMATCH
SOURCE_WY_VALIDATED_AT_DECLARED_ORDER
```

A W+Y record may be issued only when:

\[
Y^{[N]}=
\sigma_{\rm FO}^{[N]}
-
[W^{[N]}]_{\rm asy,FO}^{[N]}
\]

has exact identity in:

```text
process
external states
measurement
cuts
binning
scheme
hard factor
masses
scales
thresholds
rank
harmonic
order
```

Do not retune ART25 parameters, source members, the CS kernel, or the microscopic boundary to repair a Y mismatch.

---

# 24. External ART25 versus microscopic-project provenance

Maintain disjoint roots:

```text
ART25_EXTERNAL_SOURCE_REPRODUCTION
PROJECT_MICROSCOPIC_TMD_PROCESS_PLAN
```

C28 may qualify public source-reproducible proton DY/SIDIS low-\(q_T\) W records.

C28 may not qualify:

```text
microscopic nucleon source process
microscopic deuteron source process
spin-1 source process
inclusive b1
tagged DIS
non-NN nuclear process
matched nuclear total
physical deuteron prediction
```

A later bridge must be a separate object with:

```text
operator map
scheme adapter
scale map
joint covariance
parameter ownership
calibration/holdout split
model discrepancy
double-counting exclusions
```

Do not implement that bridge in C28.

---

# 25. Source permission and release policy

C27 records direct author transfer of `MSHT20_REP`, but explicit public redistribution permission remains unresolved.

For C28:

- continue using the source locally for the requested research/reproduction purpose;
- keep raw transferred grids out of Git;
- publish only permitted derived summaries, hashes, and metadata;
- do not infer public redistribution permission;
- do not make permission status a blocker for local source-reproducible computation;
- record the release boundary explicitly.

Create:

```text
docs/next_level/c28_source_permission_status.json
docs/next_level/c28_source_release_policy.md
```

Do not send a permission request in this package.

---

# 26. Numerical integration and source-version uncertainty

The CDF1 route uses ARTEMIDE v3.01 fast/approximate integration settings:

```text
minimum six-section qT integration
G7 rapidity integration
special adaptive Z-region Q integration
non-qT relative tolerance 1e-3
```

Preserve the source settings for the authoritative route.

For a frozen holdout subset, compare with any available more accurate mode without replacing the source route.

Record separately:

```text
source numerical mode
accurate-mode diagnostic
integration residual
runtime/reproducibility residual
historical-versus-current DataProcessor residual
```

Do not tune source tolerances dataset by dataset.

Create:

```text
docs/next_level/c28_numerical_accuracy_manifest.json
```

---

# 27. Holdouts

Freeze holdouts before source-adapter, performance, tolerance, or nuisance work.

Reserve at least:

```text
CDF1.0 exact regression
one excluded CDF1 point
one additional fixed-target DY point
one collider/fiducial DY point
one rapidity-integrated DY point
one HERMES pion SIDIS point
one COMPASS kaon SIDIS point
one normalized dataset
one absolute dataset
one dataset with correlated systematics
one normalization nuisance
one cut-boundary point
one dataset chi2
one global chi2 component
one stochastic member and point
one DY-SIDIS covariance element
one historical/current DataProcessor version comparison
one accurate-mode numerical comparison
one fixed-order/asymptotic compatibility point
one external-versus-microscopic provenance control
```

Do not move a failed holdout into calibration or adapter tuning without a new version and independent replacements.

---

# 28. Required benchmark families

Implement at least:

## P1D-A: historical DataProcessor source lock

- historical ART25 commit;
- current-public comparison;
- source bundles;
- no silent master substitution.

## P1D-B: CDF1 immutable regression

- exact file hash;
- exact 50/33 counts;
- exact point semantics;
- exact prediction;
- all zero determinism residuals.

## P1D-C: complete dataset inventory

- all source-listed DY/SIDIS datasets;
- native loader;
- metadata and file hashes;
- point identities.

## P1D-D: ART25 selection and cuts

- exact retained/excluded points;
- source line identity;
- cut reasons;
- version comparison.

## P1D-E: native observable semantics

- bin integration;
- theory factors;
- units;
- normalization;
- W-only status;
- process-specific conventions.

## P1D-F: central complete-dataset execution

- every retained point;
- deterministic output;
- typed failures;
- no dropped points.

## P1D-G: native error and nuisance model

- uncorrelated errors;
- correlated systematics;
- normalization errors;
- source-equivalent nuisance treatment.

## P1D-H: central dataset and global chi2

- native source definition;
- dataset components;
- nuisance profile;
- central versus ensemble-mean distinction.

## P1D-I: all-642 dataset execution

- exact member identity;
- deterministic shards;
- checkpoint/restart;
- no imputation.

## P1D-J: exact theory ensemble factor

- anomaly factor;
- selected dense-block reconstruction;
- PSD;
- member-permutation covariance.

## P1D-K: DY-SIDIS cross covariance

- shared source members;
- cross-process blocks;
- marginal reshuffling failure.

## P1D-L: covariance separation

- source theory;
- experimental;
- nuisance;
- numerical;
- no premature likelihood assembly.

## P1D-M: source-reproducible low-qT W tier

- complete public source route;
- dataset/point classifications;
- no author-anchor requirement;
- no W+Y inflation.

## P1D-N: Drell-Yan fixed-order/asymptotic audit

- source candidates;
- measurement and scheme identity;
- readiness decision.

## P1D-O: SIDIS fixed-order/asymptotic audit

- source candidates;
- TMDFF and z convention;
- readiness decision.

## P1D-P: W versus W+Y status

- source W;
- exact partner identity;
- analytic Y rejection;
- no boundary retuning.

## P1D-Q: external versus microscopic provenance

- disjoint roots;
- no proton-to-deuteron promotion;
- no calibration bridge yet.

## P1D-R: deterministic isolation

- prior manifests immutable;
- no likelihood/posterior;
- no production route;
- deterministic rebuild.

---

# 29. Negative injections

Create at least **1,200 ordered C28 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## DataProcessor provenance

- current master silently substituted;
- wrong ART25 commit;
- truncated git history;
- dataset file from wrong commit;
- modified CSV;
- source hash omitted;
- source line locator omitted.

## Dataset loading

- manual CSV reinterpretation;
- point ID lost;
- process code changed;
- normalized flag changed;
- theory factor omitted;
- units omitted;
- correlated and uncorrelated errors merged.

## Selection and cuts

- off-by-one inequality;
- wrong qT/Q cut;
- wrong Q cut;
- wrong z cut;
- wrong unit conversion;
- current-master cut substituted;
- excluded point retained;
- retained point excluded;
- cut reason omitted;
- CDF1 33-point count changed.

## Observable semantics

- bin center substituted for bin integral;
- raw integral compared to qT-averaged result;
- theory factor applied twice;
- theory factor omitted;
- rapidity sentinel not clipped to physical support;
- normalized observable called absolute;
- W-only result called W+Y;
- hard-factor order lost;
- wrong hadron charge;
- wrong SIDIS z convention.

## Central execution

- failed point dropped;
- output row duplicated;
- point order changed without ID;
- source member changed;
- constants modified;
- integration mode changed silently;
- CDF1 value changed.

## Nuisance and chi2

- generic covariance substituted for native source treatment;
- normalization nuisance omitted;
- correlated systematic treated as independent;
- uncorrelated error treated as correlated;
- central-member chi2 confused with ensemble-mean chi2;
- mean member chi2 confused with mean chi2;
- dataset point count changed;
- nuisance profile tuned after holdout failure.

## Full-member execution

- technical record in stochastic ensemble;
- stochastic member dropped;
- failed member imputed;
- member duplicated;
- PDF/FF/NP member shuffle;
- one process uses a different member identity;
- serial/parallel mismatch hidden;
- restart mismatch hidden.

## Covariance

- dense covariance required when factor representation is exact;
- anomaly normalization wrong;
- mean subtraction omitted;
- cross-process block dropped;
- marginal bands sampled independently;
- member weights altered;
- theory and experimental covariance irreversibly merged;
- PSD defect clipped without report.

## Qualification inflation

- public source execution called author anchored;
- source-reproducible W called full source process;
- W called W+Y;
- author-frozen anchor invented;
- physical-input eligibility issued without physical bridge;
- historical stronger gate weakened;
- source process count overwritten.

## W+Y

- C23 analytic Y inserted;
- fixed-order process mismatch;
- cut mismatch;
- scheme mismatch;
- rank mismatch;
- order mismatch;
- mass mismatch;
- source boundary retuned;
- asymptotic subtraction missing or duplicated.

## External versus microscopic

- ART25 proton result called deuteron prediction;
- external ensemble replaces microscopic boundary;
- spin-1 process promoted;
- NN result promoted to matched nuclear total;
- non-NN components silently added.

## Integrity and readiness

- raw transferred grids committed publicly;
- historical C27 output overwritten;
- likelihood created;
- posterior sampled;
- T-odd process promoted;
- production registry changed;
- authoritative artifact changed;
- nondeterministic manifest.

---

# 30. Deliverables

Create at least:

```text
docs/next_level/c28_implementation_report.md
docs/next_level/c28_api.md
docs/next_level/c28_requirement_coverage.json
docs/next_level/c28_normative_source_integration.json

docs/next_level/c28_dataprocessor_source_lock.json
docs/next_level/c28_dataprocessor_version_comparison.json
docs/next_level/c28_cdf1_regression_authority.json

docs/next_level/c28_art25_dataset_inventory.json
docs/next_level/c28_dataset_file_lock_manifest.json
docs/next_level/c28_measurement_semantics_manifest.json
docs/next_level/c28_art25_selection_manifest.json
docs/next_level/c28_selection_reason_ledger.json
docs/next_level/c28_selection_version_delta.json

docs/next_level/c28_native_code_path_manifest.json
docs/next_level/c28_observable_semantics_manifest.json
docs/next_level/c28_central_point_predictions.json
docs/next_level/c28_central_dataset_prediction_manifest.json
docs/next_level/c28_central_execution_failure_manifest.json

docs/next_level/c28_experimental_error_model_manifest.json
docs/next_level/c28_normalization_nuisance_manifest.json
docs/next_level/c28_native_chi2_definition.json
docs/next_level/c28_central_chi2_manifest.json
docs/next_level/c28_nuisance_profile_manifest.json
docs/next_level/c28_global_chi2_manifest.json

docs/next_level/c28_full_dataset_member_execution.json
docs/next_level/c28_member_execution_failure_manifest.json
docs/next_level/c28_checkpoint_restart_manifest.json
docs/next_level/c28_theory_ensemble_factor_manifest.json
docs/next_level/c28_theory_covariance_query_manifest.json
docs/next_level/c28_selected_covariance_blocks.json
docs/next_level/c28_cross_process_covariance_report.json
docs/next_level/c28_covariance_separation_manifest.json

docs/next_level/c28_lowqt_source_reproducibility_contract.json
docs/next_level/c28_lowqt_source_reproducibility_matrix.json
docs/next_level/c28_source_anchor_status.json

docs/next_level/c28_dy_fixed_order_partner_manifest.json
docs/next_level/c28_sidis_fixed_order_partner_manifest.json
docs/next_level/c28_asymptotic_partner_manifest.json
docs/next_level/c28_wy_readiness_matrix.json

docs/next_level/c28_source_process_eligibility_matrix.json
docs/next_level/c28_physical_input_eligibility_matrix.json
docs/next_level/c28_gate_delta_report.json

docs/next_level/c28_source_permission_status.json
docs/next_level/c28_source_release_policy.md
docs/next_level/c28_numerical_accuracy_manifest.json

docs/next_level/c28_holdout_report.json
docs/next_level/c28_injection_manifest.json
docs/next_level/c28_regression_report.json
docs/next_level/c28_unresolved_physics_gaps.md
```

Preserve new official source bundles under:

```text
data/raw/c28_sources/
```

Store heavy runtime member-by-point tables, anomaly factors, checkpoints, and optional dense covariance blocks outside Git under a declared content-addressed output directory. Commit their schemas, hashes, dimensions, and reconstruction commands.

Add ADRs for:

- historical ART25 versus current DataProcessor commits;
- CDF1 regression authority;
- native dataset/measurement semantics;
- source nuisance and chi2 semantics;
- exact low-rank theory covariance;
- source-reproducible versus author-anchored low-qT W;
- W-only versus W+Y;
- external ART25 versus microscopic-project provenance;
- raw transferred-source release policy.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

---

# 31. Acceptance criteria

C28/P1D is complete only when:

1. The exact C27 plus CDF1 baseline reproduces before edits.
2. The historical ART25 DataProcessor commit is hash locked.
3. The current public commit remains a separate comparison route.
4. CDF1.csv retains its exact source hash.
5. CDF1 retains 50 loaded and 33 selected points.
6. CDF1.0 reproduces exactly at `3.4394876804377352 pb/GeV`.
7. CDF1 observable semantics remain bin-integrated, qT-bin averaged, absolute, and W-only.
8. All source determinism residuals for CDF1 remain zero.
9. The complete public ART25 dataset inventory is loaded natively.
10. Every dataset and point has source identity and hashes.
11. ART25 selection and cut reasons are reproduced exactly.
12. Selected-point counts are frozen before theory execution.
13. Native observable semantics are traced for every process class.
14. Every retained central point is attempted.
15. No failed point is silently dropped.
16. Native experimental error and nuisance semantics are represented exactly.
17. Dataset and global chi2 definitions are source locked.
18. Central dataset and chi2 routes execute where the public source supports them.
19. All 642 stochastic members are attempted over the retained dataset.
20. No failed member is imputed.
21. Joint PDF/FF/NP/process member identity is preserved.
22. Serial, parallel, and restart checks close on frozen shards.
23. The exact theory anomaly factor is constructed.
24. Selected dense covariance blocks reproduce from the factor.
25. DY-DY, SIDIS-SIDIS, and DY-SIDIS covariance remain available.
26. Theory, experimental, nuisance, numerical, and source-version uncertainties remain separate.
27. The source-reproducible low-qT W tier is implemented without weakening stronger historical gates.
28. Author-anchored status is not issued without an actual author/repository numerical anchor.
29. Drell-Yan fixed-order and asymptotic partner readiness is decided.
30. SIDIS fixed-order and asymptotic partner readiness is decided.
31. No source W is combined with an analytic Y.
32. Full W+Y status is issued only with exact identity closure.
33. External ART25 and microscopic-project roots remain separate.
34. No proton ART25 result is called a deuteron or spin-1 prediction.
35. Raw transferred source files remain out of public Git absent explicit permission.
36. Holdouts remain outside adapter or tolerance tuning.
37. Every C28 negative injection produces the expected diagnostic.
38. All prior tests, builders, requirements, injections, and manifests remain passing.
39. The production registry remains exactly 216 routes.
40. All eight authoritative artifacts remain byte-identical.
41. No likelihood, posterior, microscopic calibration bridge, or production route is created.
42. All C28 manifests reproduce byte-for-byte.
43. The working tree is clean.
44. A local completion commit is created and not pushed.

C28 may complete with full source-process and W+Y eligibility still zero, provided the public source-reproducible low-\(q_T\) W tier and every remaining blocker are reported exactly.

---

# 32. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C28_DATAPROCESSOR_ART25_SOURCE_LOCK_VALIDATED
C28_CDF1_NATIVE_REGRESSION_VALIDATED
C28_ART25_DATASET_INVENTORY_COMPLETE
C28_ART25_SELECTION_REPRODUCED
C28_NATIVE_MEASUREMENT_SEMANTICS_VALIDATED
C28_ART25_CENTRAL_DATASET_EXECUTION_COMPLETE
C28_NATIVE_NUISANCE_CHI2_SEMANTICS_VALIDATED
C28_ART25_642_MEMBER_DATASET_ENSEMBLE_REPRODUCED
C28_ART25_THEORY_ENSEMBLE_FACTOR_VALIDATED
C28_ART25_DY_SIDIS_CROSS_COVARIANCE_VALIDATED
C28_SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION
C28_DY_FIXED_ORDER_ASYMPTOTIC_READINESS_AUDITED
C28_SIDIS_FIXED_ORDER_ASYMPTOTIC_READINESS_AUDITED
C28_SOURCE_WY_READINESS_DECIDED
C28_EXTERNAL_ART25_CAPABILITY_MATRIX_COMPLETE
```

Issue only those whose exact gates pass.

The following remain forbidden unless every corresponding gate genuinely closes in a later package:

```text
AUTHOR_ANCHORED_PROCESS_VALIDATED
SOURCE_WY_VALIDATED_AT_DECLARED_ORDER
PROJECT_MICROSCOPIC_SOURCE_PROCESS_READY
PHYSICAL_DEUTERON_DY_PREDICTION
PHYSICAL_DEUTERON_SIDIS_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

If an author anchor or exact source-identical W+Y chain is discovered and genuinely passes every gate, issue only the narrower corresponding status and document the evidence. Do not infer downstream physical or microscopic readiness.

---

# 33. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- historical and current DataProcessor commits;
- relevant source-file hashes;
- complete dataset counts by process;
- total, selected, and excluded point counts;
- selection and version-delta residuals;
- exact CDF1 regression result;
- central point execution count and failures;
- native observable semantics by process class;
- experimental error and nuisance semantics;
- central dataset and global chi2 results;
- members attempted/completed/failed/retried;
- serial/parallel/restart residuals;
- theory anomaly-factor dimensions and hash;
- covariance symmetry/PSD/block-reconstruction residuals;
- DY-DY, SIDIS-SIDIS, and DY-SIDIS covariance status;
- source-reproducible low-qT W eligibility counts;
- author-anchor status;
- full source-process and physical-input eligibility counts;
- Drell-Yan fixed-order/asymptotic decision;
- SIDIS fixed-order/asymptotic decision;
- W and W+Y statuses;
- external ART25 versus microscopic-project statuses;
- source permission/release status;
- every remaining failed gate;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim author-frozen reproduction, full W+Y, physical process readiness, microscopic calibration, deuteron prediction, inference readiness, or production readiness beyond the exact tier whose gates pass.
