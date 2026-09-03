# C30/B1 Codex Work Package

## Title

**Source-audited finite scheme adapter and converged microscopic rank-zero proton quark/antiquark bridge**

## Authoritative baseline

Start from the local C29 plus Volume XX integration commit:

```text
c603aa7a5cd0943ad441bad22ae4b5f3122847be
```

This commit must retain the complete C29/B0 implementation and the integrated authoritative Volume XX source in its ancestry.

The required C28/P1D scientific ancestor is:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when the complete C29 and Volume XX baseline reproduces before any scientific change.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

The untracked source directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Do not push the final completion commit.

---

# 1. Why C30/B1 is the exact next package

C29 establishes a typed, immutable span between:

```text
ART25_EXTERNAL_SOURCE_ROOT
```

and:

```text
PROJECT_MICROSCOPIC_OPERATOR_ROOT
```

without identifying or statistically merging the two roots.

C29 also establishes:

```text
14 minimum operator families crosswalked
34-point frozen bridge grid
20 microscopic C11 operator identities exported
exact external covariance projection from the C28 source ensemble
complete 46-dataset / 1,209-point ART25 ancestry
frozen calibration-candidate, holdout-candidate, diagnostic, and unavailable roles
13 typed discrepancy components
no invented cross-root member relation
```

The rank-zero unpolarized proton entries:

```text
u
d
ubar
dbar
```

have a common validation domain, but C29 deliberately leaves them not distribution-ready because two numerical ingredients are missing:

```text
1. a source-audited finite ART25-to-microscopic TMD-scheme adapter;

2. a scheme-qualified microscopic numerical TMD vector with explicit
   convergence and discrepancy inputs.
```

The quark Collins–Soper bridge is diagnostic only. Gluon, spin-1 LL, helicity, transversity, T-odd, and multiparton candidates remain unavailable.

C30 must close the genuinely common numerical distribution-level bridge for the rank-zero, T-even proton quark and positive-x antiquark TMDPDFs before any sensitivity, calibration, identifiability, likelihood, reweighting, or inference package is authorized.

---

# 2. Primary objective

Implement the chain:

```text
ART25 external rank-zero proton quark/antiquark ensemble
    -> exact source definition and convention trace
    -> source-audited finite TMD-scheme adapter
    -> one frozen common bridge scheme
    -> one frozen common x-b-Q domain
    -> microscopic rank-zero proton quark/antiquark export
    -> matching, evolution, and finite scheme conversion
    -> resolution/Fock/Wilson/TTN/numerical convergence ledger
    -> covariance-preserving external projection
    -> typed discrepancy inputs
    -> non-inferential common-space diagnostics
    -> distribution-level bridge capability decision
```

C30 must determine whether a nonempty set of:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

entries exists for:

```text
u, d, ubar, dbar
```

at the frozen C29 bridge points.

The result may remain unavailable. Scientific accuracy is more important than a positive bridge count.

---

# 3. Scientific boundary

C30 is:

```text
operator matched
proton target only for executable bridge candidates
rank-zero
T-even
quark and positive-x antiquark resolved
b-space first
source-audited at declared finite order
scheme and scale explicit
convergence resolved
covariance preserving
non-inferential
validation only
```

C30 is not:

```text
a fit
a calibration
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a physical TMD extraction
a process prediction
a deuteron prediction
a gluon bridge
a T-odd bridge
a production promotion
```

A successful distribution bridge does not upgrade process, physical-input, microscopic-deuteron, or production readiness.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C11-C30 microscopic, matching, evolution, source, bridge, formal-volume, API, manifest, test, ADR, and roadmap files before changing the repository.

Continue autonomously until every applicable C30 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect source and git history;
- read preserved primary papers and official ancillaries;
- inspect the ARTEMIDE v3.01 source implementation;
- inspect C19-C22 scheme, matching, and evolution records;
- evaluate existing microscopic states at frozen points;
- add exact deterministic numerical exporters;
- construct source-audited finite conversion records;
- perform memberwise external transformations;
- run convergence sweeps;
- rebuild deterministic manifests.

Do not:

- contact authors;
- modify ARTEMIDE;
- modify ART25 members;
- modify microscopic Hamiltonians or fitted validation conditions;
- tune any microscopic parameter to ART25;
- move a holdout into a calibration role;
- create a likelihood or posterior;
- train an emulator;
- reweight any member;
- modify production;
- push the completion commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 5.1 Microscopic parent and convergence sources

```text
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c11_regression_report.json

docs/next_level/c12_implementation_report.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
docs/next_level/c14_regression_report.json
```

## 5.2 Matching, evolution, and small-b sources

```text
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
docs/next_level/c21_anomalous_dimension_library.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_multiq_grid.json

docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_accuracy_manifest.json
```

## 5.3 Source-reproducible ART25 root

```text
docs/next_level/c25_art25_reproduction_source_plan.json
docs/next_level/c25_art25_member_schema.json
docs/next_level/c25_art25_parameter_reproduction.json

docs/next_level/c27_art25_joint_member_map.json
docs/next_level/c27_joint_covariance_manifest.json
docs/next_level/c27_distribution_reproduction_manifest.json

docs/next_level/c28_implementation_report.md
docs/next_level/c28_art25_dataset_inventory.json
docs/next_level/c28_measurement_semantics_manifest.json
docs/next_level/c28_theory_ensemble_factor_manifest.json
docs/next_level/c28_cross_process_covariance_report.json
docs/next_level/c28_lowqt_source_reproducibility_contract.json
docs/next_level/c28_source_release_policy.md
```

## 5.4 Bridge and formal sources

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c29_api.md
docs/next_level/c29_requirement_coverage.json
docs/next_level/c29_root_identity_manifest.json
docs/next_level/c29_operator_crosswalk.json
docs/next_level/c29_operator_bridge_capability.json
docs/next_level/c29_target_crosswalk.json
docs/next_level/c29_scheme_scale_adapter_manifest.json
docs/next_level/c29_domain_intersection_manifest.json
docs/next_level/c29_bridge_observable_registry.json
docs/next_level/c29_bridge_observable_capability_matrix.json
docs/next_level/c29_frozen_bridge_grid.json
docs/next_level/c29_external_bridge_projection_manifest.json
docs/next_level/c29_external_bridge_anomaly_factor_manifest.json
docs/next_level/c29_microscopic_bridge_export.json
docs/next_level/c29_microscopic_axis_manifest.json
docs/next_level/c29_cross_root_member_relation.json
docs/next_level/c29_data_ancestry_graph.json
docs/next_level/c29_no_double_counting_contract.json
docs/next_level/c29_constraint_role_split.json
docs/next_level/c29_discrepancy_interface.json
docs/next_level/c29_discrepancy_availability_matrix.json
docs/next_level/c29_compatibility_diagnostic_manifest.json
docs/next_level/c29_bridge_plan_manifest.json
docs/next_level/c29_bridge_capability_matrix.json
docs/next_level/c29_future_inference_prerequisite_contract.json
docs/next_level/c29_volume_xix_requirement_crosswalk.json
docs/next_level/c29_volume_xx_requirement_crosswalk.json
```

```text
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/volume_xx_source_reproducible_bridge_geometry.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

The authoritative Volume XVI PDF remains normative. If the Volume XVI TeX source remains absent, record the absence and do not invent it.

Create:

```text
docs/next_level/c30_normative_source_integration.json
```

---

# 6. Immutable C29 plus Volume XX baseline

Before edits, reproduce and record:

```text
1,141 tests
all C29 validators
all 53 Volume XX requirements mapped
deterministic C29 regeneration
production registry exactly 216
all eight authoritative artifacts byte-identical

roots:
    ART25_EXTERNAL_SOURCE_ROOT
    PROJECT_MICROSCOPIC_OPERATOR_ROOT

operator audit:
    14 minimum families

target audit:
    proton
    neutron
    antiproton
    phenomenological deuterium
    microscopic NN deuteron
    matched-total deuteron

frozen bridge grid:
    34 points

external projection:
    642 ordered members
    ten frozen process coordinates
    one linearly dependent null-space control
    normalization sqrt(641)
    dense/factor covariance agreement at floating-point precision
    covariance symmetry exact
    PSD and null-space reported without clipping or ridge

microscopic export:
    20 C11 operator identities
    plan/member/target/species/Wilson/matching/evolution/scheme/numerical/evidence identity retained
    TTN plan explicit
    bond dimension retained as a nonstatistical numerical/truncation axis

data ancestry:
    46 ART25 datasets
    1,209 retained point identities

discrepancy:
    13 components
    2 with separate auditable information
    11 nonzero-unknown

readiness:
    no distribution-ready entry
    no process-ready entry
    no calibration
    no inference
    no status promotion
```

Do not proceed if this baseline does not reproduce.

C30 must not modify:

- C29 root identities;
- the 34-point bridge grid;
- C29 constraint roles;
- C29 holdouts;
- the C28 source anomaly factor;
- the 642 ART25 member identities;
- any C8-C22 microscopic or perturbative result;
- C29 microscopic evidence axes;
- C29 data ancestry or no-double-counting plans;
- process readiness;
- production registry;
- authoritative artifacts.

---

# 7. Required C30 architecture

Extend the existing bridge types. Do not create a parallel untyped comparison framework.

Implement or extend immutable objects equivalent to:

```text
BridgeSchemeId
BridgeSchemePlan
BridgeSchemeSelectionRecord

ExternalTMDDefinitionRecord
MicroscopicTMDDefinitionRecord
TMDNormalizationConvention
FlavorConvention
AntiquarkConvention

FiniteSchemeAdapter
FiniteSchemeAdapterTerm
FiniteSchemeAdapterOrder
FiniteSchemeAdapterRemainder
FiniteSchemeRoundTripReport
FiniteSchemeRGReport

MicroscopicDistributionPlan
MicroscopicDistributionSourceId
MicroscopicForwardParentId
MicroscopicProjectorId
MicroscopicMatchingPlan
MicroscopicEvolutionPlan
MicroscopicSchemeExport

MicroscopicConvergenceAxis
MicroscopicConvergenceSequence
MicroscopicConvergenceReport
MicroscopicNumericalErrorBudget

CommonBridgePoint
CommonBridgeVector
CommonBridgeMemberVector
CommonBridgeDomain

BridgeDiscrepancyInput
BridgeDiscrepancyBudget
BridgeCompatibilityVector
BridgeWhiteningReport
BridgeNullSpaceReport

DistributionBridgeCapability
DistributionBridgeCapabilityMatrix
C30ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about root ownership;
- explicit about source and target schemes;
- explicit about perturbative order;
- explicit about flavor and antiquark identity;
- explicit about target and transverse rank;
- explicit about domain and remainder;
- unable to mutate source or microscopic parameters;
- unreachable from inference and production.

---

# 8. Exact external ART25 TMD definition audit

Trace the exact source-level definition of the ART25 unpolarized proton TMDPDF.

Audit the source paper, ARTEMIDE v3.01 source, ART25 model code, constants, and Python/Fortran interfaces.

For each flavor:

```text
u
d
ubar
dbar
```

record:

```text
returned object name
operator channel
target
positive-x convention
whether the stored quantity is f, x f, or another weighted object
b-space normalization
Fourier convention
mu
zeta
zeta-prescription/optimal-TMD status
hard-scheme relation
soft-factor convention
rapidity-renormalization convention
UV convention
threshold history
alpha_s convention
flavor indexing
member indexing
valid x domain
valid b domain
valid Q domain
large-b model
small-b matching status
```

At least two independent code paths or source equations must confirm every convention that enters the bridge.

Create:

```text
docs/next_level/c30_art25_tmd_definition_manifest.json
docs/next_level/c30_art25_flavor_convention_manifest.json
docs/next_level/c30_art25_scale_scheme_trace.json
```

Do not infer `f` versus `x f` from plotting labels.

---

# 9. Microscopic TMD definition audit

Trace the microscopic rank-zero forward proton quark/antiquark object from the retained operator parent.

For each executable candidate record:

```text
microscopic parent
Hamiltonian plan
resolution
Fock-sector content
target
species
flavor
positive-x antiquark identity
Wilson order
forward projector
normalization
stored scalar convention
regulator
matching record
evolution record
scheme
mu
zeta
valid x/b/Q domain
evidence status
```

The current C29 export uses C11 operator identities.

C30 must audit the relation among:

```text
C11/H4 T-even forward parent
C13/H6 higher-Fock state
C14/H7 higher-Fock/Wilson-completed state
C19-C22 matching/evolution identities
```

Allowed microscopic source-plan statuses:

```text
C11_PRIMARY_WITH_LATER_LEVELS_AS_CONVERGENCE_AXES
C14_PRIMARY_WITH_TYPED_C11_TO_C14_SUPERSESSION
C11_ONLY_VALIDATION
UNRESOLVED
```

Select exactly one primary microscopic bridge plan before computing an external comparison.

Do not silently replace a C11 operator ID with a C14 result.

Do not add C11 and C14 predictions.

Create:

```text
docs/next_level/c30_microscopic_tmd_definition_manifest.json
docs/next_level/c30_microscopic_source_plan.json
docs/next_level/c30_microscopic_parent_supersession_report.json
```

---

# 10. Bridge-scheme plans

Compile mutually exclusive scheme plans:

```text
B1-SCHEME-ART25
    Keep the external ART25 object unchanged.
    Convert the microscopic export into the exact ART25 source convention.

B1-SCHEME-PROJECT
    Keep the microscopic C19-C22 project convention unchanged.
    Convert the external ART25 object into the project convention.

B1-SCHEME-CANONICAL
    Convert both roots into a separately declared common canonical convention.
```

Select one authoritative plan before evaluating compatibility.

Selection criteria:

```text
source support
operator identity
available finite conversion
available perturbative order
round-trip checks
RG consistency
threshold consistency
domain size
remainder control
minimum synthetic content
```

Plans are alternatives, not additive models.

Create:

```text
docs/next_level/c30_bridge_scheme_plan_manifest.json
docs/next_level/c30_bridge_scheme_selection.json
```

---

# 11. Source-audited finite scheme adapter

For a source scheme \(S_A\) and bridge scheme \(S_B\), implement:

\[
\widetilde F_a^{S_B}(x,b;\mu,\zeta)
=
Z^{a}_{A\rightarrow B}(b;\mu,\zeta)
\otimes_x
\widetilde F_a^{S_A}(x,b;\mu,\zeta)
+
R^{a}_{A\rightarrow B}.
\]

At the declared finite order:

\[
Z^{a}_{A\rightarrow B}
=
\mathbf 1
+
\sum_{n=1}^{N}
a_s^n Z^{a,(n)}_{A\rightarrow B}.
\]

Every adapter record must contain:

```text
source operator
target operator
parton representation
flavor dependence or proven flavor universality
quark/antiquark relation
source scheme
target scheme
UV convention
rapidity convention
soft-factor convention
zeta prescription
alpha_s convention
implemented order
first omitted order
distributional structure
source paper
equation/code locator
source hash
transcription/build hash
independent oracle
domain
remainder
```

The finite adapter must not absorb:

```text
different nonperturbative CS kernels
different large-b boundaries
missing matching orders
microscopic Fock truncation
target mismatch
nuclear effects
missing Y term
```

Those remain separate discrepancy components.

Required checks:

\[
Z_{A\rightarrow B}\otimes Z_{B\rightarrow A}
=
\mathbf 1
+
\mathcal O(a_s^{N+1}),
\]

with separate residuals for:

```text
finite conversion
x convolution
mu evolution
zeta evolution
threshold crossing
numerical integration
```

Create:

```text
docs/next_level/c30_finite_scheme_adapter_library.json
docs/next_level/c30_finite_scheme_roundtrip_report.json
docs/next_level/c30_finite_scheme_rg_report.json
docs/next_level/c30_finite_scheme_remainder_manifest.json
```

A source paper’s existence does not qualify an adapter unless the actual required expression is ingested or exactly manageable at the declared order.

---

# 12. Common bridge domain

Use the immutable C29 frozen bridge grid.

For every rank-zero proton quark/antiquark point, determine:

```text
x
b
Q
mu
zeta
flavor
target
external-domain status
microscopic-domain status
scheme-adapter status
matching status
evolution status
small-b status
large-b status
bridge status
blocking reasons
```

Define the executable common domain as the exact intersection of:

```text
external source domain
microscopic regulator domain
matching domain
evolution domain
finite scheme-adapter domain
numerical convergence domain
```

Do not extrapolate to enlarge the bridge count.

Large-b points for which the adapter or microscopic export is not source controlled remain:

```text
DOMAIN_UNAVAILABLE
```

They may remain frozen holdouts or negative controls.

Create:

```text
docs/next_level/c30_common_bridge_domain.json
docs/next_level/c30_bridge_point_eligibility.json
```

---

# 13. Microscopic numerical export

For every eligible frozen point and every executable microscopic plan, produce:

\[
\widetilde F^{\rm Mic,B}_a(x,b;Q)
\]

in the selected bridge scheme.

The export chain must be explicit:

```text
microscopic state
    -> forward rank-zero operator parent
    -> flavor/antiquark projector
    -> regulator-aware b-space transform
    -> LF-to-QCD matching
    -> collinear/small-b coefficient route where required
    -> two-scale evolution
    -> finite scheme adapter
    -> common bridge vector
```

Every output row retains:

```text
root ID
microscopic source plan
Hamiltonian plan
resolution
Fock content
state member
target
flavor
operator
Wilson order
projector
matching plan
evolution plan
scheme plan
x/b/Q point
numerical route
value
all error components
```

Do not introduce a free normalization.

Do not normalize the microscopic vector to the ART25 mean.

Create:

```text
docs/next_level/c30_microscopic_distribution_export.json
docs/next_level/c30_microscopic_bridge_vector_manifest.json
docs/next_level/c30_microscopic_export_execution_report.json
```

Heavy vectors may remain outside Git under a content-addressed runtime directory. Commit exact hashes, schemas, dimensions, and reconstruction commands.

---

# 14. Microscopic convergence program

Run an explicit convergence sequence over all axes that are available and scientifically relevant.

At minimum audit:

```text
longitudinal/basis resolution
transverse/UV support
infrared scale
Fock-sector level
C11 versus typed later-parent lift
Wilson order for the link-even object
exact versus Krylov
exact versus full-bond TTN
TTN bond dimension
b-transform quadrature
matching order
evolution path
finite scheme-adapter order
interpolation
floating precision
```

The tensor-network bond dimension remains a numerical/truncation axis, not a statistical member.

For every bridge point report:

```text
central primary-plan value
successive-resolution differences
Fock-extension difference
Wilson-order difference
full-bond residual
reduced-bond defect
quadrature residual
matching/evolution residual
scheme-adapter residual
declared convergence status
```

Energy convergence cannot substitute for TMD convergence.

Create:

```text
docs/next_level/c30_microscopic_convergence_manifest.json
docs/next_level/c30_ttn_tmd_convergence_report.json
docs/next_level/c30_numerical_error_budget.json
```

---

# 15. External bridge vectors and covariance

Evaluate the ART25 external ensemble at every eligible frozen distribution point.

Preserve:

```text
all 642 stochastic members
central/mean technical record
u, d, ubar, dbar identity
x/b/Q
source scheme
bridge scheme
adapter identity where used
member ordering
```

For a linear conversion:

\[
A_{\rm bridge}
=
A_{\rm ext}B^T.
\]

For a nonlinear or member-dependent conversion, evaluate all 642 members and recenter empirically.

Required checks:

- 642 members retained;
- no technical record in stochastic covariance;
- no flavor shuffle;
- no quark/antiquark alias;
- deterministic member order;
- covariance symmetry;
- PSD within tolerance;
- rank and null-space report;
- direct dense reconstruction on frozen blocks;
- scheme round-trip on selected members.

Create:

```text
docs/next_level/c30_external_distribution_bridge_manifest.json
docs/next_level/c30_external_distribution_anomaly_factor_manifest.json
docs/next_level/c30_external_distribution_covariance_blocks.json
```

---

# 16. Bridge discrepancy budget

Instantiate the C29 discrepancy interface for the rank-zero distribution bridge.

Retain separately:

```text
finite scheme-conversion truncation
matching-order truncation
evolution finite-order/path uncertainty
external CS/large-b model uncertainty
microscopic Hamiltonian truncation
Fock-sector truncation
Wilson-order truncation
basis/resolution truncation
TTN bond truncation
regulator dependence
numerical transform/interpolation error
external-fit model discrepancy
target/operator mismatch
```

For every component record:

```text
available numerical estimate
source
domain
owner
mean status
covariance status
additive/multiplicative/operator-valued status
whether zero is justified
whether it blocks comparison readiness
```

Unknown components remain:

```text
NONZERO_UNKNOWN
```

Do not combine the discrepancy components into a fitted covariance.

Do not inflate ART25 covariance to hide microscopic differences.

Create:

```text
docs/next_level/c30_distribution_bridge_discrepancy_budget.json
docs/next_level/c30_distribution_bridge_discrepancy_availability.json
```

---

# 17. Non-inferential numerical comparison

Only after the operator, target, scheme, domain, convergence, and discrepancy gates close may C30 compare the microscopic vector with the external source ensemble.

For an eligible bridge vector:

\[
r = m-\mu_{\rm ext}.
\]

Using the nonzero covariance eigenspace:

\[
C_{\rm ext}=U_r\Lambda_rU_r^T,
\]

report:

\[
z=\Lambda_r^{-1/2}U_r^T r,
\]

and separately:

\[
r_0=(I-U_rU_r^T)r.
\]

Allowed outputs:

```text
pointwise residuals
relative residuals
external member percentile locations
whitened residual vector
whitened norm
covariance rank
null-space residual
flavor-separated shape correlations
x-region summaries
b-region summaries
Q summaries
microscopic-plan comparisons
convergence-versus-residual comparisons
```

Forbidden interpretations:

```text
chi-square probability
p-value
likelihood
posterior
confidence region
parameter constraint
model selection probability
```

Do not optimize a microscopic parameter.

Do not reweight microscopic or external members.

Create:

```text
docs/next_level/c30_distribution_compatibility_diagnostic.json
docs/next_level/c30_distribution_bridge_comparison_report.md
```

---

# 18. Frozen roles and holdouts

Preserve the C29 role assignments.

The bridge must retain:

```text
CALIBRATION_CANDIDATE
HOLDOUT_CANDIDATE
DIAGNOSTIC_ONLY
UNAVAILABLE
```

C30 does not calibrate.

Report diagnostics separately for candidate and holdout points.

A failed holdout cannot be moved.

A domain-unavailable holdout remains unavailable rather than being extrapolated.

Create:

```text
docs/next_level/c30_constraint_role_execution_report.json
docs/next_level/c30_holdout_report.json
```

---

# 19. Distribution bridge capability matrix

For each of:

```text
u
d
ubar
dbar
```

and for every frozen distribution point, report:

```text
operator identity
target identity
external definition
microscopic definition
common scheme
finite adapter
common domain
external member vector
external covariance
microscopic vector
convergence status
discrepancy status
constraint role
diagnostic status
distribution bridge readiness
blocking reasons
```

Allowed positive status:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

Allowed limited statuses:

```text
BRIDGE_DISTRIBUTION_DIAGNOSTIC_ONLY
BRIDGE_COMMON_DOMAIN_ONLY
BRIDGE_SCHEME_ADAPTER_ONLY
BRIDGE_MICROSCOPIC_EXPORT_ONLY
BRIDGE_UNAVAILABLE
```

Do not preselect a positive count.

Create:

```text
docs/next_level/c30_distribution_bridge_capability_matrix.json
docs/next_level/c30_distribution_bridge_closure_report.json
```

---

# 20. Process bridges remain gated

Do not execute a new DY one-leg or SIDIS target-leg process bridge in C30.

Audit only whether a validated distribution bridge removes one prerequisite.

The process entries must remain blocked by all still-missing items, including as applicable:

```text
process-specific measurement identity
partner ownership
source W-only status
missing Y
target map
hard/process status
source-process qualification
physical-input qualification
```

Create:

```text
docs/next_level/c30_process_bridge_prerequisite_delta.json
```

A distribution bridge does not promote process readiness.

---

# 21. Data ancestry and no-double-counting preservation

Preserve the complete C29 ancestry and future-plan alternatives:

```text
PLAN_EXTERNAL_COMPRESSED_CONSTRAINT
PLAN_DIRECT_DATA
PLAN_EXTERNAL_HOLDOUT
PLAN_DIAGNOSTIC_ONLY
```

The selected C30 diagnostics must record whether each point derives from an ART25-fit dataset and which future no-double-counting plan would apply.

Do not create a likelihood.

Do not use both ART25 compressed information and its underlying data as independent evidence.

Create:

```text
docs/next_level/c30_data_ancestry_bridge_report.json
docs/next_level/c30_no_double_counting_regression.json
```

---

# 22. Cross-root member relation

The default remains:

```text
NO_JOINT_MEASURE
```

C30 may compare each microscopic plan deterministically against the ART25 external ensemble.

It must not:

```text
pair member indices
add cross-root covariances
construct a joint posterior
construct a Cartesian-product ensemble and call it statistical
average microscopic assumption plans using ART25 member weights
```

Create:

```text
docs/next_level/c30_cross_root_member_relation_regression.json
```

---

# 23. Future package decision

If at least one flavor has a nonempty:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

set with convergence and discrepancy gates closed, the exact next package is:

> **C31/B2 — frozen-bridge sensitivity, parameter ownership, identifiability, and discrepancy-prior readiness, still without calibration**

If no distribution bridge closes because the finite adapter remains incomplete, the exact next package is:

> **C31/B1A — targeted source-ingestion and finite scheme-adapter completion**

If the adapter closes but the microscopic vector does not converge, the exact next package is:

> **C31/B1M — microscopic rank-zero TMD convergence and regulator-trajectory completion**

Do not authorize inference solely because a bridge comparison is ready.

---

# 24. Required holdouts

Freeze and retain at least:

```text
one u point
one d point
one ubar point
one dbar point
one low-x point
one intermediate-x point
one high-x point
one small-b point
one large-b/domain-boundary point
one Q value distinct from the primary comparison Q
one scheme round-trip point
one threshold-history point
one C11/C14 parent-comparison point
one TTN bond holdout
one quadrature holdout
one external covariance-null-space direction
one discrepancy-unavailable control
one target-mismatch control
one T-odd negative control
one external-versus-microscopic provenance control
```

No holdout may be moved or used to choose the bridge scheme after inspection.

---

# 25. Required benchmark families

Implement at least:

## B1-A: external ART25 TMD definition

- exact returned object;
- \(f\) versus \(x f\);
- scale and scheme;
- flavor and antiquark semantics.

## B1-B: microscopic TMD definition

- parent;
- projector;
- normalization;
- matching/evolution identity;
- no free normalization.

## B1-C: microscopic source-plan selection

- C11/C14 relation;
- primary versus convergence axis;
- no additive parents.

## B1-D: bridge-scheme selection

- ART25, project, or canonical plan;
- frozen before comparison;
- mutually exclusive.

## B1-E: finite scheme adapter

- source audit;
- declared order;
- round trip;
- RG and threshold closure;
- visible remainder.

## B1-F: common domain

- x/b/Q intersection;
- no extrapolation;
- boundary failures.

## B1-G: microscopic numerical export

- u/d/ubar/dbar;
- exact identities;
- common scheme;
- deterministic values.

## B1-H: resolution and basis convergence

- three resolutions where available;
- UV/IR support;
- exact/Krylov.

## B1-I: Fock and Wilson convergence

- C11 versus typed later level;
- Wilson-order effect;
- no double counting.

## B1-J: TTN convergence

- full bond;
- reduced bonds;
- TMD-specific error;
- energy not used as substitute.

## B1-K: external covariance conversion

- all 642 members;
- linear/memberwise routes;
- rank and null space.

## B1-L: discrepancy budget

- auditable versus unknown;
- unknown not zero;
- no covariance inflation.

## B1-M: frozen compatibility diagnostics

- residuals;
- whitening;
- null-space;
- no probability claim.

## B1-N: role and holdout preservation

- candidate versus holdout;
- no movement after inspection.

## B1-O: distribution capability

- per flavor;
- per point;
- complete blocking reasons.

## B1-P: process gate preservation

- no one-leg process execution;
- no process promotion.

## B1-Q: data ancestry and member relation

- no double counting;
- no joint measure.

## B1-R: deterministic isolation

- prior manifests immutable;
- no calibration/inference;
- no production mutation.

---

# 26. Negative injections

Create at least **1,520 ordered C30 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## External definition

- \(x f\) treated as \(f\);
- quark/antiquark alias;
- wrong flavor index;
- wrong target;
- wrong \(\mu\);
- wrong \(\zeta\);
- optimal-TMD object treated as ordinary fixed-scale object;
- wrong b units;
- Fourier normalization omitted;
- member identity dropped.

## Microscopic definition

- C11 operator replaced by C14 without supersession;
- C11 and C14 added;
- antiquark copied from quark;
- proton copied from neutron;
- free normalization introduced;
- Wilson order lost;
- regulator identity omitted;
- unmatched object called matched;
- unevolved object called evolved.

## Scheme adapter

- source paper cited without expression ingestion;
- finite order overstated;
- wrong alpha_s normalization;
- rapidity scheme mismatch hidden;
- soft factor counted twice;
- inverse adapter omitted;
- round-trip failure hidden;
- threshold mismatch hidden;
- flavor dependence invented;
- quark adapter copied to gluon;
- large-b difference absorbed into finite scheme conversion.

## Domain

- external extrapolation;
- microscopic extrapolation;
- large-b point forced through small-b adapter;
- Q outside evolution grid;
- x outside support;
- domain selected after residual inspection;
- holdout excluded after failure.

## Microscopic export

- state member shuffled;
- matching plan changed per point;
- evolution path changed per flavor;
- TMD-specific normalization fitted;
- output row dropped;
- failed point imputed;
- exact/Krylov mismatch hidden;
- numerical units changed.

## Convergence

- energy convergence substituted for TMD convergence;
- TTN bond called statistical member;
- reduced-bond defect omitted;
- Fock and Wilson axes merged;
- resolution axis averaged;
- regulator dependence set to zero;
- quadrature tolerance tuned per point;
- matching remainder absorbed into numerical error.

## External covariance

- technical record included in stochastic covariance;
- member dropped;
- member duplicated;
- flavor member shuffle;
- quark/antiquark member shuffle;
- marginal resampling;
- diagonal covariance substituted;
- null space ridge regularized silently;
- PSD clipping without report;
- nonlinear conversion linearized without memberwise validation.

## Discrepancy

- unknown discrepancy set to zero;
- ART25 covariance inflated;
- scheme and Hamiltonian discrepancy merged;
- target mismatch treated as noise;
- large-b mismatch hidden;
- Fock truncation absorbed into external uncertainty;
- fitted discrepancy introduced.

## Diagnostics

- whitened norm called chi-square probability;
- p-value produced;
- likelihood constructed;
- posterior produced;
- parameter optimized;
- member reweighted;
- bridge scheme selected by best residual;
- holdout used in scheme selection;
- null-space residual discarded.

## Process and readiness

- distribution bridge called process bridge;
- DY one-leg executed;
- SIDIS target-leg executed;
- source W called W+Y;
- physical-input status promoted;
- deuteron prediction claimed;
- T-odd bridge activated;
- gluon bridge copied from quark.

## Integrity

- C29 grid modified;
- C29 roles modified;
- C28 anomaly factor modified;
- historical manifest overwritten;
- raw MSHT files added to Git;
- production registry mutated;
- authoritative artifact mutated;
- nondeterministic manifest.

---

# 27. Deliverables

Create at least:

```text
docs/next_level/c30_implementation_report.md
docs/next_level/c30_api.md
docs/next_level/c30_requirement_coverage.json
docs/next_level/c30_normative_source_integration.json

docs/next_level/c30_art25_tmd_definition_manifest.json
docs/next_level/c30_art25_flavor_convention_manifest.json
docs/next_level/c30_art25_scale_scheme_trace.json

docs/next_level/c30_microscopic_tmd_definition_manifest.json
docs/next_level/c30_microscopic_source_plan.json
docs/next_level/c30_microscopic_parent_supersession_report.json

docs/next_level/c30_bridge_scheme_plan_manifest.json
docs/next_level/c30_bridge_scheme_selection.json
docs/next_level/c30_finite_scheme_adapter_library.json
docs/next_level/c30_finite_scheme_roundtrip_report.json
docs/next_level/c30_finite_scheme_rg_report.json
docs/next_level/c30_finite_scheme_remainder_manifest.json

docs/next_level/c30_common_bridge_domain.json
docs/next_level/c30_bridge_point_eligibility.json

docs/next_level/c30_microscopic_distribution_export.json
docs/next_level/c30_microscopic_bridge_vector_manifest.json
docs/next_level/c30_microscopic_export_execution_report.json
docs/next_level/c30_microscopic_convergence_manifest.json
docs/next_level/c30_ttn_tmd_convergence_report.json
docs/next_level/c30_numerical_error_budget.json

docs/next_level/c30_external_distribution_bridge_manifest.json
docs/next_level/c30_external_distribution_anomaly_factor_manifest.json
docs/next_level/c30_external_distribution_covariance_blocks.json

docs/next_level/c30_distribution_bridge_discrepancy_budget.json
docs/next_level/c30_distribution_bridge_discrepancy_availability.json

docs/next_level/c30_distribution_compatibility_diagnostic.json
docs/next_level/c30_distribution_bridge_comparison_report.md
docs/next_level/c30_constraint_role_execution_report.json
docs/next_level/c30_holdout_report.json

docs/next_level/c30_distribution_bridge_capability_matrix.json
docs/next_level/c30_distribution_bridge_closure_report.json
docs/next_level/c30_process_bridge_prerequisite_delta.json

docs/next_level/c30_data_ancestry_bridge_report.json
docs/next_level/c30_no_double_counting_regression.json
docs/next_level/c30_cross_root_member_relation_regression.json

docs/next_level/c30_injection_manifest.json
docs/next_level/c30_regression_report.json
docs/next_level/c30_unresolved_physics_gaps.md
```

Add ADRs for:

- external ART25 TMD definition authority;
- microscopic primary-parent selection;
- bridge-scheme plan selection;
- finite scheme-adapter authority and remainder;
- common-domain restriction;
- microscopic TMD convergence;
- tensor-network bond as a nonstatistical TMD-error axis;
- discrepancy separation;
- diagnostic versus likelihood semantics;
- distribution versus process bridge readiness.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy microscopic vectors and external memberwise bridge arrays may remain outside Git under a declared content-addressed runtime directory. Commit their schemas, hashes, dimensions, member/plan order, and deterministic reconstruction commands.

---

# 28. Acceptance criteria

C30/B1 is complete only when:

1. The exact C29 plus Volume XX baseline reproduces before edits.
2. The external and microscopic roots remain disjoint.
3. The ART25 TMDPDF definition is traced exactly.
4. \(f\) versus \(x f\) semantics are explicit.
5. Quark and positive-x antiquark identities remain separate.
6. One microscopic primary source plan is selected before comparison.
7. C11/C14 relations are typed and nonadditive.
8. One bridge-scheme plan is selected before comparison.
9. The finite adapter is source audited at its declared order.
10. The finite adapter has explicit inverse/round-trip status.
11. RG, rapidity, and threshold consistency are tested.
12. The finite-order remainder is visible.
13. The common bridge domain is an exact intersection.
14. No external or microscopic extrapolation is used to enlarge readiness.
15. Eligible microscopic u/d/ubar/dbar vectors are exported numerically.
16. No free normalization is introduced.
17. Matching, evolution, and scheme identities remain explicit.
18. Resolution and basis convergence are reported.
19. Fock and Wilson axes remain separate.
20. TTN bond convergence is evaluated on the TMD itself.
21. Energy convergence is not used as a TMD proxy.
22. Numerical and perturbative errors remain separate.
23. All 642 external members survive bridge conversion.
24. External covariance rank and null space remain visible.
25. Dense frozen covariance blocks reconstruct from the factor.
26. Discrepancy components are typed.
27. Unknown discrepancy remains nonzero-unknown.
28. External covariance is not inflated.
29. Compatibility diagnostics use only frozen eligible points.
30. Holdouts remain frozen.
31. Diagnostics preserve null-space residual.
32. No probability, likelihood, fit, posterior, optimization, or reweighting is created.
33. The distribution bridge capability matrix is complete.
34. Every positive distribution-ready entry passes all identity, scheme, domain, convergence, and discrepancy gates.
35. Process bridge entries are not executed or promoted.
36. Data ancestry and no-double-counting contracts remain intact.
37. Cross-root member relation remains `NO_JOINT_MEASURE` unless an explicit map is independently proven.
38. Gluon, LL, helicity, transversity, T-odd, and multiparton bridges remain fail-closed.
39. No deuteron or spin-1 prediction is claimed.
40. All previous tests, builders, requirements, injections, and manifests remain passing.
41. The production registry remains exactly 216 routes.
42. All eight authoritative artifacts remain byte-identical.
43. Raw transferred source files remain outside Git absent permission.
44. Every C30 negative injection yields the expected diagnostic.
45. All C30 manifests reproduce byte-for-byte.
46. The working tree is clean.
47. A local completion commit is created and not pushed.

C30 may complete with zero distribution-ready entries when the finite scheme adapter or microscopic convergence cannot be established. It must report the exact blocker rather than weaken the bridge definition.

---

# 29. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C30_ART25_TMD_DEFINITION_SOURCE_AUDITED
C30_MICROSCOPIC_RANK0_TMD_EXPORT_VALIDATED
C30_FINITE_SCHEME_ADAPTER_SOURCE_AUDITED
C30_COMMON_BRIDGE_DOMAIN_VALIDATED
C30_MICROSCOPIC_TMD_CONVERGENCE_AUDITED
C30_EXTERNAL_DISTRIBUTION_COVARIANCE_PRESERVED
C30_DISTRIBUTION_DISCREPANCY_BUDGET_DEFINED
C30_NONINFERENTIAL_DISTRIBUTION_DIAGNOSTICS_VALIDATED
C30_DISTRIBUTION_BRIDGE_CAPABILITY_MATRIX_COMPLETE
```

Entry-level statuses may include:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
BRIDGE_DISTRIBUTION_DIAGNOSTIC_ONLY
BRIDGE_COMMON_DOMAIN_ONLY
BRIDGE_SCHEME_ADAPTER_ONLY
BRIDGE_MICROSCOPIC_EXPORT_ONLY
BRIDGE_UNAVAILABLE
```

The following remain forbidden:

```text
MICROSCOPIC_MODEL_CALIBRATED
ART25_CONSTRAINED_MICROSCOPIC_POSTERIOR
GLOBAL_LIKELIHOOD_READY
GLOBAL_INFERENCE_READY
REPLICA_REWEIGHTED
PARAMETERS_OPTIMIZED
EMULATOR_TRAINED
BRIDGE_PROCESS_READY
SOURCE_PROCESS_PROMOTED
PHYSICAL_INPUT_PROMOTED
PHYSICAL_DEUTERON_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
PRODUCTION_READY
```

---

# 30. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- selected bridge-scheme plan;
- exact external TMD definition and \(f\)/\(x f\) convention;
- selected microscopic primary source plan;
- C11/C14 supersession or convergence relation;
- finite adapter source, order, and domain;
- round-trip, RG, rapidity, threshold, and numerical residuals;
- common bridge-point counts by flavor and status;
- microscopic export dimensions and hashes;
- values and convergence residuals by microscopic axis;
- TTN bond-convergence results;
- external bridge-member dimensions and hashes;
- covariance rank, symmetry, PSD, block-reconstruction, and null-space residuals;
- discrepancy-component availability;
- frozen calibration-candidate and holdout diagnostics;
- whitened and null-space diagnostic summaries;
- distribution bridge counts by readiness status;
- process-bridge prerequisite deltas;
- data-ancestry and no-double-counting status;
- cross-root member-relation status;
- exact next package branch;
- confirmation that no fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a distribution bridge as a constraint, calibration, process prediction, physical extraction, or posterior result.
