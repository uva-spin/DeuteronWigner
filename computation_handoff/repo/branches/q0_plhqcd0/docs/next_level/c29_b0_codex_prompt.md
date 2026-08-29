# C29/B0 Codex Work Package

## Title

**Typed covariance-preserving bridge between the source-reproducible ART25 ensemble and the microscopic operator root**

## Authoritative baseline

Start from the local C28/P1D completion commit:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C28 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

Do not push the final completion commit.

---

# 1. Why C29/B0 is the exact next package

C28 completes the public, source-reproducible ART25 low-\(q_T\) process route:

```text
historical DataProcessor commit:
    761f3fcdd3701c5cf69e822f9ffbbd5db394fc58

current-public comparison:
    9f9dda71b69dd26e288be189a396736827cfeed3

datasets:
    36 Drell-Yan
    10 SIDIS

source points:
    8,675

retained points:
    1,209
    627 DY
    582 SIDIS

excluded points:
    7,466

central predictions:
    1,209 / 1,209
    zero failures

source members:
    642 / 642
    zero failures
    zero imputations

central chi2:
    DY      733.3634803213348
    SIDIS   536.8536205509276
    total  1270.2171008722626

theory anomaly factor:
    642 x 1,209
    SHA-256 c959dfef644a16d5300254d0b4b164ce383b8eb059bc41a45ebf69a0d44a9eb8

covariance reconstruction:
    zero residual

source status:
    SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION
```

C28 does not establish:

```text
author-frozen reproduction
full W+Y
source-process eligibility under the stronger historical gate
physical-input eligibility
microscopic-project process qualification
a deuteron or spin-1 prediction
a likelihood
a fit
posterior inference
production readiness
```

The exact next scientific problem is therefore not another source-ingestion task and not yet inference.

C29 must define the typed bridge by which the external ART25 ensemble can later constrain, calibrate, or test the microscopic operator construction without:

- replacing the microscopic state by ART25;
- treating a phenomenological proton fit as a deuteron prediction;
- losing the 642-member ART25 covariance;
- inventing a cross-root member correlation;
- double counting the ART25 datasets;
- fitting or updating any microscopic parameter;
- changing any process-readiness status.

---

# 2. Primary objective

Implement the chain:

```text
ART25 external source root
    -> exact source/operator/process identity
    -> common operator and observable crosswalk
    -> scheme, scale, flavor, target, rank, link, and domain adapters
    -> covariance-preserving projection into a shared comparison space
    -> microscopic member/plan export into the same space
    -> non-inferential compatibility diagnostics
    -> frozen calibration-candidate / holdout-candidate / diagnostic roles
    -> data-ancestry and no-double-counting contract
    -> future inference prerequisite contract
```

The package must produce a complete bridge contract and capability matrix.

It must not optimize parameters, construct a likelihood, issue a posterior, reweight members, or promote any physical/process status.

---

# 3. Scientific boundary

C29 is:

```text
identity preserving
operator level
observable level where exact process identity exists
covariance preserving
scheme and domain explicit
data-ancestry aware
no-double-counting aware
validation only
future-calibration ready only at the contract level
```

C29 is not:

```text
a fit
Bayesian inference
frequentist profiling
replica reweighting
parameter optimization
emulation
a new ART25 extraction
a microscopic calibration
a source-process promotion
a physical deuteron prediction
a production promotion
```

Any numerical compatibility statistic is diagnostic only and must not be interpreted as a likelihood, posterior probability, confidence level, or parameter constraint.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant microscopic, matching, evolution, process, source-reproduction, covariance, formal-volume, test, ADR, and roadmap files before changing the repository.

Continue autonomously until every applicable C29 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository content and exact source histories;
- read C7-C28 manifests and runtime schemas;
- inspect heavy C28 runtime artifacts by their recorded local paths;
- construct typed crosswalks and adapters;
- evaluate existing microscopic members and plans at frozen bridge points;
- project the ART25 anomaly factor into bridge spaces;
- build deterministic sparse/low-rank covariance queries;
- create compatibility diagnostics;
- generate deterministic manifests and negative controls.

Do not:

- contact authors;
- refit ART25;
- refit the microscopic model;
- create a likelihood;
- sample a posterior;
- train an emulator;
- recompile or alter the validated ARTEMIDE route;
- alter the 216-route production registry;
- push the final commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
# Microscopic nucleon and deuteron roots
docs/next_level/c7_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c12_implementation_report.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c15_implementation_report.md
docs/next_level/c16_implementation_report.md
docs/next_level/c17_implementation_report.md
docs/next_level/c18_implementation_report.md

# Matching, evolution, and process layers
docs/next_level/c19_implementation_report.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
docs/next_level/c22q_implementation_report.md
docs/next_level/c22q_capability_reconciliation.json
docs/next_level/c22q_process_eligibility_matrix.json
docs/next_level/c22q_qualification_contract.json
docs/next_level/c23_implementation_report.md
docs/next_level/c23_process_capability_matrix.json
docs/next_level/c23_wy_matching_manifest.json

# ART25 source and dataset closure
docs/next_level/c24_implementation_report.md
docs/next_level/c25_implementation_report.md
docs/next_level/c26_implementation_report.md
docs/next_level/c27_implementation_report.md
docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_joint_covariance_manifest.json
docs/next_level/c28_implementation_report.md
docs/next_level/c28_art25_dataset_inventory.json
docs/next_level/c28_measurement_semantics_manifest.json
docs/next_level/c28_art25_selection_manifest.json
docs/next_level/c28_observable_semantics_manifest.json
docs/next_level/c28_central_point_predictions.json
docs/next_level/c28_global_chi2_manifest.json
docs/next_level/c28_full_dataset_member_execution.json
docs/next_level/c28_theory_ensemble_factor_manifest.json
docs/next_level/c28_theory_covariance_query_manifest.json
docs/next_level/c28_selected_covariance_blocks.json
docs/next_level/c28_cross_process_covariance_report.json
docs/next_level/c28_covariance_separation_manifest.json
docs/next_level/c28_lowqt_source_reproducibility_contract.json
docs/next_level/c28_lowqt_source_reproducibility_matrix.json
docs/next_level/c28_wy_readiness_matrix.json
docs/next_level/c28_source_process_eligibility_matrix.json
docs/next_level/c28_physical_input_eligibility_matrix.json
docs/next_level/c28_gate_delta_report.json
docs/next_level/c28_source_release_policy.md
docs/next_level/c28_unresolved_physics_gaps.md

# Formal sources
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

If Volume XX is present, read and hash-audit it. If it is absent, record the absence and do not invent its contents.

Create:

```text
docs/next_level/c29_normative_source_integration.json
```

---

# 6. Immutable C28 baseline

Before edits, reproduce and record:

```text
1,131 tests
all C28 builders and validators
36/36 evidence rows
162/162 atlas pages
1,360 C28 requirements
1,320/1,320 C28 negative controls

historical DataProcessor:
    761f3fcdd3701c5cf69e822f9ffbbd5db394fc58

current-public comparison:
    9f9dda71b69dd26e288be189a396736827cfeed3

datasets:
    36 DY
    10 SIDIS

points:
    8,675 source
    1,209 retained
    7,466 excluded
    627 retained DY
    582 retained SIDIS

selection disagreements:
    0

CDF1:
    50 loaded
    33 selected
    CDF1.0 = 3.4394876804377352 pb/GeV

central execution:
    1,209 / 1,209
    0 failures

ensemble:
    642 / 642
    0 failures
    0 imputations

central chi2:
    DY      733.3634803213348
    SIDIS   536.8536205509276
    total  1270.2171008722626

anomaly factor:
    dimensions 642 x 1,209
    SHA-256 c959dfef644a16d5300254d0b4b164ce383b8eb059bc41a45ebf69a0d44a9eb8

covariance:
    reconstruction residual 0
    symmetry residual 0
    serial/restart prediction residual 0

status:
    SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION
    W-only
    no exact DY fixed-order/asymptotic partner
    no exact SIDIS fixed-order/asymptotic partner
    no W+Y

integrity:
    production registry exactly 216
    all eight authoritative artifacts byte-identical
    all 45 C28 JSON artifacts deterministic
```

Do not proceed if this baseline does not reproduce.

C29 must not modify:

- any C7-C28 scientific result;
- ARTEMIDE v3.01;
- ART25 constants or model payload;
- MSHT20_REP;
- MAPFF archives;
- the 642 ART25 rows;
- any C28 dataset or point selection;
- the 642 x 1,209 anomaly factor;
- C28 chi2 results;
- C19-C23 operator/process identities;
- C22Q qualification semantics;
- C23 analytic process outputs;
- historical source/process/physical eligibility matrices;
- production registry or authoritative artifacts.

---

# 7. Required bridge architecture

Implement or extend immutable types equivalent to:

```text
ExternalRootId
MicroscopicRootId
BridgeRootPairId

BridgeOperatorId
BridgeObservableId
BridgeMeasurementId
BridgeTargetId
BridgePartnerId

FlavorMap
SpeciesMap
TargetMap
ChargeConjugationMap
RankMap
LinkMap
ColorMap
SchemeMap
ScaleMap
ThresholdMap
DomainIntersection

BridgeSourceMemberId
BridgeMicroscopicMemberId
BridgeMemberRelation
BridgeMemberRelationStatus

ExternalMeanVector
ExternalAnomalyFactor
ExternalCovarianceQuery
MicroscopicPredictionVector
MicroscopicSensitivityAxis

BridgeProjection
BridgeProjectionResult
BridgeCovariancePushforward
BridgeCovarianceBlock

BridgeDataAncestry
BridgeDatasetConflict
NoDoubleCountingPlan
ConstraintRole
ConstraintRoleSplit

BridgeDiscrepancyComponent
BridgeDiscrepancyInterface
BridgeCompatibilityDiagnostic

BridgePlan
BridgeCapabilityEntry
BridgeCapabilityMatrix
BridgeClosureReport
FutureInferencePrerequisiteContract
```

Every bridge object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about both root identities;
- explicit about operator, scheme, scale, target, rank, link, and domain;
- explicit about data ancestry;
- explicit about member relation;
- fail-closed on missing identity;
- unable to mutate either root;
- unreachable from inference and production code.

---

# 8. Two disjoint provenance roots

Define and enforce:

```text
ART25_EXTERNAL_SOURCE_ROOT
PROJECT_MICROSCOPIC_OPERATOR_ROOT
```

## 8.1 External root

The external root owns:

```text
ART25 source parameters
ART25 CS kernel
ART25 TMDPDF members
ART25 TMDFF members
MSHT20_REP members
MAPFF members
DataProcessor datasets and cuts
source-reproducible low-qT W predictions
642-member source covariance
```

## 8.2 Microscopic root

The microscopic root owns:

```text
light-front Hamiltonian plans
Fock-sector amplitudes
microscopic proton/neutron states
microscopic deuteron state and component ancestry
Wilson-order identities
LF-to-QCD matching records
evolution records
microscopic process compiler records
microscopic truncation and assumption axes
```

## 8.3 Prohibited root collapse

The bridge must reject:

```text
ART25 TMD used as the microscopic wave-function output
ART25 member substituted for a microscopic member
ART25 proton result called a deuteron result
phenomenological deuterium data treated as a microscopic deuteron state
external covariance labeled microscopic posterior covariance
external source readiness copied to the microscopic root
```

Create:

```text
docs/next_level/c29_root_identity_manifest.json
docs/next_level/c29_provenance_separation_report.json
```

---

# 9. Common operator crosswalk

Construct a complete operator-level crosswalk between the external ART25 objects and the microscopic operator registry.

For every candidate pair record:

```text
external object ID
microscopic operator ID
species
flavor
parton polarization
target
rank
naive-T parity
link class
color class
twist
scheme
reference scales
collinear operator
matching status
evolution status
process status
domain
bridge status
blocking reasons
```

Do not match by TMD name alone.

At minimum audit:

```text
unpolarized u
unpolarized d
unpolarized ubar
unpolarized dbar
unpolarized quark singlet
quark CS kernel
unpolarized gluon
rank-two linearly polarized gluon
spin-1 LL quark/antiquark
helicity
transversity
T-odd/multiparton families
```

Expected behavior:

- rank-zero T-even quark/antiquark families receive the deepest audit;
- CS-kernel comparison remains quark/gluon representation specific;
- LL cannot inherit proton unpolarized identity merely by scalar shape;
- T-odd and multiparton families remain unavailable;
- gluon families remain separate and must not inherit a quark kernel;
- no operator absent from one root is assigned zero.

Create:

```text
docs/next_level/c29_operator_crosswalk.json
docs/next_level/c29_operator_bridge_capability.json
```

---

# 10. Target and nuclear identity

Audit target compatibility separately from partonic operator compatibility.

Allowed target statuses include:

```text
SAME_PROTON_TARGET
SAME_NEUTRON_TARGET
CHARGE_CONJUGATE_HADRON_WITH_PROVEN_MAP
MICROSCOPIC_DEUTERON_TARGET
PHENOMENOLOGICAL_DEUTERIUM_RECORD
NUCLEAR_TARGET_UNMAPPED
TARGET_INCOMPATIBLE
```

The bridge must not identify:

```text
phenomenological deuterium SIDIS
```

with:

```text
the C15-C18 microscopic deuteron state
```

without a complete target/nuclear adapter.

For every deuteron candidate retain component status:

```text
NN
NNPI
DELTADELTA
SIX_QUARK_CLUSTER
SIX_QUARK_HIDDEN_COLOR
TRANSITION_AND_INTERFERENCE
COHERENT_PILOT
MATCHED_TOTAL
```

A bridge may operate on an explicitly selected NN-only microscopic assumption plan, but it must not call that the complete deuteron target.

Create:

```text
docs/next_level/c29_target_crosswalk.json
docs/next_level/c29_nuclear_bridge_scope.json
```

---

# 11. Scheme, scale, and domain adapters

For every candidate bridge define:

```text
external TMD scheme
microscopic TMD scheme
UV scheme
rapidity scheme
soft-factor convention
zeta prescription
mu prescription
threshold history
b convention
Fourier normalization
rank convention
reference mass
x convention
target momentum convention
Q domain
x domain
b domain
process domain
```

Allowed statuses:

```text
IDENTICAL
EXACT_ADAPTER
DECLARED_FINITE_ORDER_ADAPTER
VALIDATION_ONLY_ADAPTER
UNRESOLVED
INCOMPATIBLE
```

No adapter may silently absorb:

```text
large-b model differences
CS-kernel differences
missing matching orders
nuclear effects
missing Y term
target mismatch
```

Those remain separate discrepancy or unavailable statuses.

Create:

```text
docs/next_level/c29_scheme_scale_adapter_manifest.json
docs/next_level/c29_domain_intersection_manifest.json
```

---

# 12. Bridge observable spaces

Construct bridge spaces only where both roots can be evaluated with complete identity.

Audit at least:

## 12.1 Distribution-level quark bridge

Candidate shared objects:

```text
u, d, ubar, dbar rank-zero T-even TMDPDFs
selected x-b-Q points
selected moments or basis projections
```

Requirements:

```text
same target
same scheme or declared adapter
same scale
same flavor convention
same positive-x antiquark convention
same normalization
common domain
```

## 12.2 Quark CS-kernel bridge

Requirements:

```text
same rapidity convention
same derivative convention
same b units
same perturbative subtraction convention
same quark representation
```

This is a comparison object only. It must not replace the microscopic kernel.

## 12.3 Drell-Yan one-leg bridge

A candidate hybrid observable may replace one external distribution leg with a microscopic proton/nucleon leg while retaining the source-owned partner leg and measurement map.

Record explicitly:

```text
microscopic leg
external partner leg
hard factor
measurement
source member
microscopic member/plan
link class
process domain
```

The bridge must fail when:

- the target leg is ambiguous;
- both legs are silently replaced;
- an antihadron map is assumed without proof;
- a nuclear target is unmapped;
- the missing Y term is hidden.

## 12.4 SIDIS target-leg bridge

A candidate hybrid observable may replace the external target TMDPDF with a microscopic target-side TMD while retaining the external TMDFF member and native measurement map.

It remains unavailable unless:

```text
target identity
TMDPDF scheme
TMDFF scheme
z convention
hard factor
source member identity
measurement identity
```

all close.

## 12.5 Deuteron bridge

Audit only. Do not force a positive result.

The bridge must distinguish:

```text
external phenomenological deuterium record
microscopic NN-only plan
microscopic full selected-component plan
complete matched total
```

## 12.6 Gluon bridge

Audit only unless exact common objects exist.

Do not infer a gluon bridge from quark-source success.

Create:

```text
docs/next_level/c29_bridge_observable_registry.json
docs/next_level/c29_bridge_observable_capability_matrix.json
```

---

# 13. Frozen bridge grid

Freeze bridge points before evaluating microscopic predictions.

The grid must contain, at minimum:

```text
distribution-level x-b-Q points
one or more quark CS-kernel b points
representative low-qT DY points where one-leg identity is candidate
representative SIDIS points where target-leg identity is candidate
target-mismatch negative controls
scheme-mismatch negative controls
domain-boundary points
```

Selection principles:

- cover the common domain;
- include calibration-candidate and holdout-candidate regions;
- include low, intermediate, and high x where supported;
- include multiple Q values only where both roots support them;
- include small-b and large-b boundary points separately;
- do not select points after inspecting microscopic residuals.

Create:

```text
docs/next_level/c29_frozen_bridge_grid.json
```

---

# 14. External covariance projection

The C28 source anomaly factor is authoritative:

\[
A_{\mathrm{ext}}[s,i]
=
\frac{T_{s i}-\bar T_i}{\sqrt{641}},
\qquad
A_{\mathrm{ext}}\in\mathbb R^{642\times1209},
\]

with:

\[
C_{\mathrm{ext}}=A_{\mathrm{ext}}^T A_{\mathrm{ext}}.
\]

## 14.1 Linear bridge projections

For a declared linear bridge map \(B\),

\[
y_{\mathrm{bridge}} = B y_{\mathrm{ext}},
\]

store:

\[
\bar y_{\mathrm{bridge}}=B\bar y_{\mathrm{ext}},
\qquad
A_{\mathrm{bridge}}=A_{\mathrm{ext}}B^T,
\qquad
C_{\mathrm{bridge}}=A_{\mathrm{bridge}}^T A_{\mathrm{bridge}}.
\]

## 14.2 Nonlinear bridge projections

For a nonlinear map \(g\), evaluate every external source member:

\[
y_s^{\mathrm{bridge}}=g(y_s^{\mathrm{ext}}),
\]

then recenter empirically.

Do not use a linearized Jacobian as the authoritative route when exact memberwise evaluation is available.

## 14.3 Required checks

- exact member count;
- exact member order;
- no marginal resampling;
- no independent TMDPDF/TMDFF/CS shuffling;
- covariance symmetry;
- PSD within tolerance;
- direct dense reconstruction on frozen blocks;
- projection composition;
- deterministic rebuild;
- null-space preservation;
- no silent diagonal regularization.

Create:

```text
docs/next_level/c29_external_bridge_projection_manifest.json
docs/next_level/c29_external_bridge_anomaly_factor_manifest.json
docs/next_level/c29_external_bridge_covariance_blocks.json
```

---

# 15. Microscopic prediction export

Export microscopic predictions into the frozen bridge grid without modifying the microscopic model.

Every exported row must retain:

```text
Hamiltonian plan
resolution
Fock-sector plan
state member
target
species
flavor
operator
Wilson order
nuclear component plan
matching plan
evolution plan
process plan
scheme adapter
numerical route
```

Distinguish:

```text
statistical/calibration member
Hamiltonian alternative
resolution/truncation axis
Fock-sector axis
Wilson-order axis
nuclear-component axis
scheme/matching axis
numerical axis
```

Do not call a finite set of assumption plans a statistical posterior.

Do not merge unlike axes into one covariance band.

Create:

```text
docs/next_level/c29_microscopic_bridge_export.json
docs/next_level/c29_microscopic_axis_manifest.json
docs/next_level/c29_microscopic_bridge_execution_report.json
```

---

# 16. Cross-root member relation

The external and microscopic roots do not presently possess a demonstrated joint probability measure.

Implement statuses:

```text
NO_JOINT_MEASURE
INDEPENDENT_BY_EXPLICIT_ASSUMPTION
CORRELATED_BY_EXPLICIT_MAP
SHARED_SOURCE_COMPONENT
INCOMPATIBLE
```

Default:

```text
NO_JOINT_MEASURE
```

Consequences:

- do not pair ART25 member \(s\) with microscopic member \(s\) by index;
- do not add external and microscopic covariances by default;
- do not form a Cartesian-product posterior;
- do not independently sample marginal bands and call them joint;
- do not claim cross-root covariance.

C29 may store conditional external covariance around each microscopic prediction when the bridge observable is well defined, but it must keep the microscopic axis separate.

Create:

```text
docs/next_level/c29_cross_root_member_relation.json
```

---

# 17. Data ancestry and no-double-counting

The ART25 ensemble is derived from the 1,209 retained source points.

Construct a complete ancestry graph:

```text
ART25 member ensemble
    <- ART25 fit
    <- exact retained datasets and point IDs
```

For every external bridge observable record:

```text
underlying datasets
underlying point IDs
process
target
source publication
selection status
role in ART25
```

Define mutually exclusive future-use plans:

```text
PLAN_EXTERNAL_COMPRESSED_CONSTRAINT
    Use the ART25 ensemble or bridge covariance.
    Exclude its underlying ART25 data from a direct likelihood.

PLAN_DIRECT_DATA
    Use the underlying data directly.
    Do not add ART25 ensemble information as an independent constraint.

PLAN_EXTERNAL_HOLDOUT
    Use ART25 only for withheld comparison.
    Do not tune to its ensemble or underlying points.

PLAN_DIAGNOSTIC_ONLY
    Structural comparison only.
```

Plans are alternatives, not additive evidence.

Create:

```text
docs/next_level/c29_data_ancestry_graph.json
docs/next_level/c29_no_double_counting_contract.json
docs/next_level/c29_dataset_conflict_matrix.json
```

---

# 18. Constraint roles and frozen split

Assign every bridge observable one role:

```text
CALIBRATION_CANDIDATE
HOLDOUT_CANDIDATE
DIAGNOSTIC_ONLY
UNAVAILABLE
```

C29 does not execute calibration.

The split must be frozen before compatibility calculations.

The split should preserve:

- process diversity;
- kinematic separation;
- target separation;
- distribution/process separation;
- source-dataset ancestry;
- common-domain coverage;
- at least one withheld dataset family where a process bridge exists;
- at least one distribution-level holdout;
- at least one scheme/domain negative control.

Create:

```text
docs/next_level/c29_constraint_role_split.json
```

No failed holdout may be reclassified after inspection.

---

# 19. Discrepancy interface

Define, but do not fit, a typed discrepancy interface.

Possible components include:

```text
scheme-conversion truncation
matching-order truncation
CS-kernel difference
large-b boundary difference
external-fit model discrepancy
microscopic Hamiltonian truncation
Fock-sector truncation
Wilson-order truncation
nuclear-component truncation
missing Y term
target mismatch
partner-function uncertainty
numerical integration
```

Each component must record:

```text
owner
domain
mean status
covariance status
source
whether estimable now
whether zero is justified
whether it is additive, multiplicative, or operator valued
```

Unknown discrepancy is not zero.

Do not inflate external covariance to hide microscopic disagreement.

Create:

```text
docs/next_level/c29_discrepancy_interface.json
docs/next_level/c29_discrepancy_availability_matrix.json
```

---

# 20. Non-inferential compatibility diagnostics

C29 may compute frozen diagnostics without fitting.

For a microscopic prediction \(m\), external mean \(\mu\), and external covariance \(C\), define a rank-aware whitening using the exact nonzero eigenspace:

\[
C=U_r\Lambda_r U_r^T,
\qquad
z=\Lambda_r^{-1/2}U_r^T(m-\mu).
\]

Allowed diagnostics include:

```text
component residuals
whitened residual vector
whitened norm
projection onto covariance null space
external percentile location where memberwise evaluation permits
shape correlation
moment differences
domain-by-domain summaries
```

Required rules:

- record covariance rank and SVD threshold;
- preserve the null-space residual separately;
- do not add ridge regularization silently;
- do not convert the diagnostic into a p-value;
- do not define a likelihood;
- do not optimize parameters;
- do not reweight members;
- do not change bridge roles after seeing results.

Create:

```text
docs/next_level/c29_compatibility_diagnostic_manifest.json
docs/next_level/c29_bridge_comparison_report.json
```

---

# 21. Bridge plans

Compile mutually exclusive bridge plans such as:

```text
B0-DIST-QUARK
    Distribution-level rank-zero unpolarized quark/antiquark comparison.

B0-CS-QUARK
    Quark CS-kernel comparison in a common declared convention.

B0-DY-ONELEG
    One microscopic proton/nucleon DY leg;
    external partner leg and source measurement retained.

B0-SIDIS-TARGETLEG
    Microscopic target-side TMD;
    external TMDFF and source measurement retained.

B0-NN-DEUTERON-DIAGNOSTIC
    Explicit microscopic NN-only deuteron comparison;
    never called a full deuteron result.

B0-FULL-DEUTERON
    Unavailable unless every selected nuclear component and process identity closes.

B0-GLUON
    Audit-only unless a complete common gluon object exists.

B0-NEGATIVE-TODD
    Required fail-closed T-odd/multiparton control.
```

Plans cannot be summed.

Every plan records:

```text
external root
microscopic root
operator map
target map
scheme map
member relation
data ancestry plan
constraint role set
discrepancy status
capability status
```

Create:

```text
docs/next_level/c29_bridge_plan_manifest.json
```

---

# 22. Bridge capability matrix

Construct a deterministic matrix over all candidate operator and observable pairs.

For each entry report:

```text
external object available
microscopic object available
operator identity
target identity
scheme adapter
scale adapter
rank/link/color identity
domain intersection
external covariance
microscopic export
measurement map
partner ownership
member relation
data ancestry
discrepancy status
constraint role
distribution-level readiness
one-leg process readiness
holdout readiness
future-calibration readiness
blocking reasons
```

Do not preselect a positive count.

Allowed statuses include:

```text
BRIDGE_IDENTITY_AUDITED
BRIDGE_COMMON_DOMAIN_IDENTIFIED
BRIDGE_DISTRIBUTION_COMPARISON_READY
BRIDGE_ONE_LEG_PROCESS_COMPARISON_READY
BRIDGE_HOLDOUT_CANDIDATE
BRIDGE_FUTURE_CALIBRATION_CANDIDATE
BRIDGE_DIAGNOSTIC_ONLY
BRIDGE_UNAVAILABLE
```

Create:

```text
docs/next_level/c29_bridge_capability_matrix.json
```

---

# 23. Minimal bridge-family audit

Audit at least:

```text
u rank-zero unpolarized
d rank-zero unpolarized
ubar rank-zero unpolarized
dbar rank-zero unpolarized
quark singlet
quark CS kernel
unpolarized gluon
linearly polarized gluon
spin-1 LL quark
helicity quark
transversity quark
T-odd quark
T-odd gluon
DY one-leg proton
SIDIS target-leg proton
SIDIS phenomenological deuterium
microscopic NN-only deuteron
microscopic matched-total deuteron
```

For each report:

```text
operator bridge
process bridge
common domain
external covariance
microscopic axes
constraint role
discrepancy status
future-calibration prerequisites
```

Do not force qualification.

Create:

```text
docs/next_level/c29_minimal_bridge_family_audit.json
```

---

# 24. Future inference prerequisite contract

Define the exact gates a later inference package would need.

At minimum:

```text
nonempty bridge capability
frozen calibration/holdout split
complete operator and scheme adapters
complete data ancestry
selected no-double-counting plan
valid cross-root member relation or conditional formulation
declared discrepancy model
parameter ownership
identifiability plan
differentiable or auditable forward map
numerical convergence
physical/process status appropriate to the intended claim
```

The contract must state explicitly:

```text
C29 does not satisfy these gates merely by defining them.
```

Create:

```text
docs/next_level/c29_future_inference_prerequisite_contract.json
```

Do not create an inference API.

---

# 25. Holdouts

Freeze holdouts before microscopic bridge execution.

Reserve at least:

```text
one u distribution point
one d distribution point
one antiquark point
one CS-kernel point
one small-b point
one large-b point
one Q value not used in any future calibration candidate
one DY dataset family
one SIDIS dataset family
one target-mismatch control
one phenomenological-deuterium versus microscopic-deuteron control
one covariance-null-space direction
one cross-process covariance block
one scheme-adapter holdout
one microscopic resolution plan
one nuclear-component plan
one external-versus-microscopic provenance control
```

Do not move a failed holdout into the calibration-candidate set.

---

# 26. Required benchmark families

Implement at least:

## B0-A: root identity and immutability

- external root;
- microscopic root;
- no root collapse;
- no mutation.

## B0-B: operator crosswalk

- species/flavor/rank/link/scheme identity;
- no TMD-name-only matching.

## B0-C: target and nuclear crosswalk

- proton;
- neutron;
- phenomenological deuterium;
- microscopic NN;
- matched-total failure.

## B0-D: scheme and domain adapters

- exact;
- finite-order;
- validation-only;
- incompatible.

## B0-E: frozen bridge grid

- pre-comparison freeze;
- domain coverage;
- holdouts.

## B0-F: external covariance projection

- linear and nonlinear;
- memberwise identity;
- covariance reconstruction.

## B0-G: microscopic export

- full plan/member identity;
- no statistical reinterpretation of assumption axes.

## B0-H: cross-root member relation

- no index pairing;
- no invented covariance;
- explicit assumption plans.

## B0-I: distribution-level bridge

- quark/antiquark;
- CS kernel;
- moments.

## B0-J: DY one-leg bridge

- partner ownership;
- target identity;
- W-only status.

## B0-K: SIDIS target-leg bridge

- external TMDFF;
- z convention;
- target identity.

## B0-L: deuteron negative control

- phenomenological deuterium is not microscopic deuteron;
- NN-only is not matched total.

## B0-M: data ancestry

- all 1,209 source points;
- compressed-constraint versus direct-data exclusivity.

## B0-N: discrepancy interface

- unknown is not zero;
- no covariance inflation.

## B0-O: compatibility diagnostics

- covariance rank;
- null-space residual;
- no p-value or optimization.

## B0-P: future inference contract

- gates defined;
- no inference route created.

## B0-Q: deterministic isolation

- prior manifests immutable;
- no process promotion;
- no production mutation.

---

# 27. Negative injections

Create at least **1,400 ordered C29 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## Root and provenance

- external root replaced by microscopic root;
- microscopic state replaced by ART25 member;
- ART25 covariance labeled microscopic posterior;
- source readiness copied across roots;
- historical manifest overwritten.

## Operator identity

- TMD-name-only matching;
- quark/gluon alias;
- quark/antiquark alias;
- rank mismatch;
- link mismatch;
- color mismatch;
- twist mismatch;
- LL copied from U without operator proof;
- unavailable operator set to zero.

## Target identity

- proton called deuteron;
- phenomenological deuterium called microscopic deuteron;
- NN-only called full deuteron;
- nuclear target ignored;
- charge conjugation assumed without map;
- target leg changed after freezing.

## Scheme and domain

- scheme mismatch hidden;
- CS convention mismatch;
- b units mismatch;
- Fourier normalization mismatch;
- reference mass mismatch;
- scale mismatch;
- threshold mismatch;
- extrapolation outside common domain;
- large-b difference absorbed into scheme adapter.

## Covariance

- anomaly-factor orientation reversed;
- wrong normalization \(1/\sqrt{N}\);
- member dropped;
- member duplicated;
- member order shuffled;
- marginal resampling;
- diagonal-only covariance substituted;
- null space regularized silently;
- PSD clipping without report;
- nonlinear map linearized without memberwise check.

## Microscopic axes

- Hamiltonian alternatives called posterior replicas;
- resolution axis merged with statistical covariance;
- Fock alternatives averaged without plan;
- Wilson orders added;
- nuclear mechanisms double counted;
- numerical error called model uncertainty.

## Cross-root member relation

- ART25 member 1 paired with microscopic member 1 by index;
- independent roots called correlated;
- covariance added without assumption;
- Cartesian product called posterior;
- shared source component ignored.

## Process bridges

- both DY legs silently replaced;
- external partner identity dropped;
- antihadron map assumed;
- SIDIS TMDFF replaced by collinear FF;
- z convention lost;
- W-only called W+Y;
- missing Y hidden;
- external measurement changed.

## Data ancestry

- ART25 ensemble and its underlying points used as independent evidence;
- direct-data and compressed-constraint plans combined;
- excluded ART25 point treated as fit input;
- point ancestry omitted;
- holdout point used for calibration;
- dataset family moved after diagnostics.

## Discrepancy

- unknown discrepancy set to zero;
- external covariance inflated to hide disagreement;
- missing Y absorbed into discrepancy silently;
- target mismatch treated as noise;
- microscopic truncation absorbed into ART25 band;
- fitted discrepancy introduced.

## Compatibility diagnostics

- diagnostic called likelihood;
- whitened norm called chi-square probability;
- p-value reported;
- SVD threshold omitted;
- null-space residual discarded;
- parameters optimized;
- members reweighted.

## Readiness leakage

- calibration executed;
- posterior sampled;
- emulator trained;
- source-process status promoted;
- physical-input status promoted;
- deuteron prediction claimed;
- T-odd process activated;
- production registry mutated;
- authoritative artifact mutated;
- raw MSHT grids committed publicly;
- nondeterministic manifest.

---

# 28. Deliverables

Create at least:

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c29_api.md
docs/next_level/c29_requirement_coverage.json
docs/next_level/c29_normative_source_integration.json

docs/next_level/c29_root_identity_manifest.json
docs/next_level/c29_provenance_separation_report.json

docs/next_level/c29_operator_crosswalk.json
docs/next_level/c29_operator_bridge_capability.json
docs/next_level/c29_target_crosswalk.json
docs/next_level/c29_nuclear_bridge_scope.json

docs/next_level/c29_scheme_scale_adapter_manifest.json
docs/next_level/c29_domain_intersection_manifest.json
docs/next_level/c29_bridge_observable_registry.json
docs/next_level/c29_bridge_observable_capability_matrix.json
docs/next_level/c29_frozen_bridge_grid.json

docs/next_level/c29_external_bridge_projection_manifest.json
docs/next_level/c29_external_bridge_anomaly_factor_manifest.json
docs/next_level/c29_external_bridge_covariance_blocks.json

docs/next_level/c29_microscopic_bridge_export.json
docs/next_level/c29_microscopic_axis_manifest.json
docs/next_level/c29_microscopic_bridge_execution_report.json
docs/next_level/c29_cross_root_member_relation.json

docs/next_level/c29_data_ancestry_graph.json
docs/next_level/c29_no_double_counting_contract.json
docs/next_level/c29_dataset_conflict_matrix.json
docs/next_level/c29_constraint_role_split.json

docs/next_level/c29_discrepancy_interface.json
docs/next_level/c29_discrepancy_availability_matrix.json
docs/next_level/c29_compatibility_diagnostic_manifest.json
docs/next_level/c29_bridge_comparison_report.json

docs/next_level/c29_bridge_plan_manifest.json
docs/next_level/c29_bridge_capability_matrix.json
docs/next_level/c29_minimal_bridge_family_audit.json
docs/next_level/c29_future_inference_prerequisite_contract.json

docs/next_level/c29_holdout_report.json
docs/next_level/c29_injection_manifest.json
docs/next_level/c29_regression_report.json
docs/next_level/c29_unresolved_physics_gaps.md
```

Add ADRs for:

- external versus microscopic root ownership;
- operator-level rather than name-level crosswalk;
- target and deuterium/deuteron identity;
- scheme/domain adapter authority;
- covariance pushforward;
- cross-root member relation;
- data ancestry and no double counting;
- calibration-candidate versus holdout-candidate roles;
- discrepancy interface;
- diagnostic versus likelihood semantics;
- future inference gates.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy projected member arrays may remain outside Git under a declared content-addressed runtime directory. Commit their schemas, hashes, dimensions, and deterministic reconstruction commands.

---

# 29. Acceptance criteria

C29/B0 is complete only when:

1. The exact C28 baseline reproduces before edits.
2. The external and microscopic roots are immutable and disjoint.
3. Every candidate bridge is operator matched, not name matched.
4. Target identity is explicit.
5. Phenomenological deuterium is not identified with the microscopic deuteron.
6. NN-only is not identified with the complete matched total.
7. Scheme, scale, rank, link, color, and domain status are explicit.
8. The bridge grid is frozen before microscopic comparison.
9. The C28 anomaly factor is consumed without member loss or reordering.
10. Linear bridge covariance closes exactly.
11. Nonlinear bridge covariance uses memberwise evaluation where available.
12. Covariance null spaces remain visible.
13. Microscopic plans retain their evidence class.
14. Assumption alternatives are not reinterpreted as posterior replicas.
15. No cross-root member correlation is invented.
16. Data ancestry covers the complete ART25 retained-point set.
17. Compressed ART25 constraints and underlying direct data are mutually exclusive future plans.
18. Calibration-candidate, holdout-candidate, diagnostic, and unavailable roles are frozen.
19. No calibration is executed.
20. No likelihood is created.
21. No posterior or member reweighting is created.
22. Discrepancy components are typed and unavailable components remain nonzero-unknown.
23. Compatibility diagnostics preserve covariance rank and null-space residual.
24. Diagnostics are not reported as probabilities.
25. Distribution-level quark/antiquark bridge candidates receive complete decisions.
26. The quark CS-kernel bridge receives a complete decision.
27. DY one-leg candidates receive complete decisions.
28. SIDIS target-leg candidates receive complete decisions.
29. Deuteron candidates fail or qualify with exact component scope.
30. T-odd/multiparton candidates remain fail-closed.
31. The bridge capability matrix is complete and deterministic.
32. The future inference prerequisite contract is complete.
33. No source-process, physical-input, microscopic-process, or production status is promoted.
34. All previous tests, builders, requirements, injections, and manifests remain passing.
35. The production registry remains exactly 216 routes.
36. All eight authoritative artifacts remain byte-identical.
37. Raw transferred source files remain outside public Git absent permission.
38. Every C29 negative injection yields the expected diagnostic.
39. All C29 manifests reproduce byte-for-byte.
40. The working tree is clean.
41. A local completion commit is created and not pushed.

C29 may complete with zero process-level bridge-ready entries, provided every operator, target, scheme, covariance, ancestry, and discrepancy decision is explicit.

---

# 30. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C29_EXTERNAL_MICROSCOPIC_ROOT_SEPARATION_VALIDATED
C29_OPERATOR_CROSSWALK_COMPLETE
C29_TARGET_NUCLEAR_CROSSWALK_COMPLETE
C29_SCHEME_DOMAIN_ADAPTERS_AUDITED
C29_EXTERNAL_COVARIANCE_PUSHFORWARD_VALIDATED
C29_MICROSCOPIC_BRIDGE_EXPORT_VALIDATED
C29_DATA_ANCESTRY_NO_DOUBLE_COUNTING_VALIDATED
C29_CONSTRAINT_ROLE_SPLIT_FROZEN
C29_DISCREPANCY_INTERFACE_DEFINED
C29_NONINFERENTIAL_COMPATIBILITY_DIAGNOSTICS_VALIDATED
C29_BRIDGE_CAPABILITY_MATRIX_COMPLETE
C29_FUTURE_INFERENCE_PREREQUISITE_CONTRACT_COMPLETE
```

Entry-level statuses may include:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
BRIDGE_ONE_LEG_PROCESS_COMPARISON_READY
BRIDGE_HOLDOUT_CANDIDATE
BRIDGE_FUTURE_CALIBRATION_CANDIDATE
BRIDGE_DIAGNOSTIC_ONLY
BRIDGE_UNAVAILABLE
```

The following remain forbidden:

```text
MICROSCOPIC_MODEL_CALIBRATED
ART25_CONSTRAINED_MICROSCOPIC_POSTERIOR
GLOBAL_LIKELIHOOD_READY
GLOBAL_INFERENCE_READY
SOURCE_PROCESS_PROMOTED
PHYSICAL_INPUT_PROMOTED
PHYSICAL_DEUTERON_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
PRODUCTION_READY
```

---

# 31. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- external and microscopic root IDs;
- operator-crosswalk counts by status;
- target/nuclear-crosswalk counts by status;
- scheme/domain adapter counts;
- frozen bridge-grid dimensions and hashes;
- external bridge anomaly-factor dimensions and hashes;
- covariance reconstruction, symmetry, PSD, and null-space residuals;
- microscopic export counts by evidence axis;
- cross-root member-relation statuses;
- data-ancestry and dataset-conflict counts;
- calibration-candidate, holdout-candidate, diagnostic, and unavailable counts;
- discrepancy-component availability;
- compatibility-diagnostic results on frozen calibration candidates and holdouts;
- distribution-level bridge counts;
- DY one-leg bridge counts;
- SIDIS target-leg bridge counts;
- deuteron and gluon bridge decisions;
- future inference prerequisite status;
- confirmation that no fit, likelihood, posterior, reweighting, calibration, emulator, or process-status promotion occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a bridge candidate as a constraint, calibration, posterior, physical prediction, or process qualification unless a later package explicitly executes and validates those stronger steps.
