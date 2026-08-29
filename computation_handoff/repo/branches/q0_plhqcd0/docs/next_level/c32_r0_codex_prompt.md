# C32/R0 Codex Work Package

## Title

**Regulator-specific microscopic TMD operator completion, one-loop renormalization, soft/rapidity subtraction, and light-front-to-project matching**

## Authoritative baseline

Start from the local C31/B1A completion commit:

```text
f0f48602a7aba3c07b17fd911e32bb33c70ec8b4
```

This commit must retain the complete C29/B0, Volume XX, C30/B1, and C31/B1A ancestry.

The required C28/P1D scientific ancestor remains:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when the complete C31 baseline reproduces before any scientific change.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

The pre-existing untracked source directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Do not push the final completion commit.

---

# 1. Why C32/R0 is the exact next package

C31/B1A resolves the conceptual ambiguity and identifies one missing calculation.

It separates:

```text
Layer I:
    C11 regulated finite-basis light-front model density

Layer II:
    UV-renormalized, soft-subtracted, rapidity-renormalized project TMD

Layer III:
    ART25/arTeMiDe optimal TMD
```

C31 finds:

```text
C11 classification:
    REGULATED_MODEL_DENSITY

C11 Wilson status:
    Wilson order zero

strongest validated C11 TMD status:
    TREE_LEVEL_OPERATOR_LIMIT_VALIDATED

first omitted order:
    O(alpha_s)

direct C11-regulator matching source:
    unavailable

proved regulator-equivalence theorem:
    unavailable

operator-identical partonic matching calculation:
    not yet performed

LF-to-project matching:
    NO_SOURCE_QUALIFIED_LF_TO_TMD_MATCHING

project-to-ART25 continuum alignment:
    formally supported for an already-renormalized project TMD

microscopic renormalized export:
    empty unavailable vector

bridge:
    12 BRIDGE_COMMON_DOMAIN_ONLY
    0 BRIDGE_DISTRIBUTION_COMPARISON_READY

external representation:
    642 x 0 empty-not-zero projection

cross-root member relation:
    NO_JOINT_MEASURE
```

C31 also identifies fifteen required microscopic components that remain blocking:

```text
1. quark-field renormalization
2. bilocal-operator UV renormalization
3. Wilson-line self energy
4. endpoint/cusp terms
5. soft factor
6. square-root-soft allocation
7. zero-bin or overlap subtraction
8. rapidity regulator
9. rapidity counterterm
10. rapidity anomalous dimension
11. UV anomalous dimension
12. Hamiltonian/basis counterterms
13. regulator conversion
14. operator mixing
15. regulator/power corrections
```

The next package must therefore perform a new regulator-specific calculation. It must not search for another generic continuum identity and must not fit a finite multiplier to the external ART25 ensemble.

C32 must calculate the same declared quark TMD operator in:

```text
A. a microscopic light-front finite-basis regulator derived from C11;

B. the target project renormalized-TMD definition;
```

using a common infrared prescription, and extract the state-independent, infrared-finite difference.

The result may be a rigorous no-go or a partial tree/one-loop calculation. A positive matching result is not assumed.

---

# 2. Primary objective

Implement the chain:

```text
C11 state and regulator identity
    -> versioned microscopic TMD operator completion
    -> explicit staple Wilson operator
    -> explicit rapidity regulator
    -> microscopic unsubtracted quark correlator
    -> microscopic soft factor
    -> microscopic zero-bin/overlap subtraction
    -> microscopic UV and rapidity counterterms
    -> one-loop partonic matrix element
    -> target project-scheme partonic matrix element
    -> common-IR matching difference
    -> finite LF-to-project matching kernel
    -> regulator and basis convergence trajectory
    -> state-independence and flavor/charge-conjugation tests
    -> conditional microscopic proton export
    -> conditional twelve-point bridge rerun
```

The central matching relation is:

\[
F_{q}^{\mathrm{project}}(x,b;\mu,\zeta)
=
\sum_j
\int_x^1 \frac{dz}{z}\,
Z_{q\leftarrow j}^{\mathrm{LF}\to\mathrm{project}}
\left(
\frac{x}{z},
b;
\Lambda_{\mathrm{LF}},
\mu,
\zeta
\right)
F_{j}^{\mathrm{LF,reg}}
\left(
z,b;
\Lambda_{\mathrm{LF}}
\right)
+
R_q .
\]

At one loop:

\[
Z_{q\leftarrow j}^{\mathrm{LF}\to\mathrm{project}}
=
\delta_{qj}\,\delta(1-x)
+
a_s\,Z_{q\leftarrow j}^{(1)}
+
\mathcal O(a_s^2).
\]

C32 must determine rather than assume:

```text
whether the map is diagonal in parton species;
whether q<-g mixing is present at the required operator level;
whether the finite-basis regulator permits a convolutional state-independent kernel;
whether endpoint and basis artifacts are removable counterterms or power corrections;
whether the rapidity subtraction can be defined consistently in the microscopic regulator;
whether the matching has a controlled common domain;
whether only a tree-level limit is supportable.
```

---

# 3. Scientific boundary

C32 is:

```text
operator specific
regulator specific
external-state specific
one-loop targeted
UV explicit
rapidity explicit
soft-sector explicit
zero-bin/overlap explicit
distributional in x
b-space first
basis-convergence aware
state-independence tested
validation only
non-inferential
```

C32 is not:

```text
a fit
a calibration
a phenomenological ratio correction
a fitted normalization
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
an ART25 refit
a physical TMD extraction
a process prediction
a deuteron prediction
a gluon or T-odd matching package
a production promotion
```

The package must distinguish:

```text
MICROSCOPIC_OPERATOR_COMPLETION
MICROSCOPIC_RENORMALIZATION
LF_TO_PROJECT_MATCHING
PROJECT_TO_ART25_CONTINUUM_ALIGNMENT
TWO_SCALE_EVOLUTION
NONPERTURBATIVE_BOUNDARY
```

These are separate operations.

The C31 project-to-ART25 convention result remains read-only. C32 must not redo it by fitting an external ratio.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C5-C32 operator, Wilson, Hamiltonian, regulator, matching, evolution, source, bridge, formal-volume, API, manifest, test, ADR, and roadmap files before changing the repository.

Continue autonomously until every applicable C32 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect source code and git history;
- preserve additional primary papers or official ancillary files;
- derive analytic one-loop expressions;
- build symbolic distributional calculations;
- construct finite-basis partonic matrix elements;
- implement an explicit microscopic soft sector;
- run UV, rapidity, gauge, and infrared cancellations;
- run regulator and basis trajectories;
- compare independent analytic and numerical routes;
- execute conditional exports only after gates pass;
- rebuild deterministic manifests.

Do not:

- contact authors;
- alter ARTEMIDE or the ART25 ensemble;
- alter the accepted C11 state or Hamiltonian;
- silently reinterpret C11 historical outputs;
- fit the matching kernel to ART25 data or members;
- use the twelve bridge residuals in the derivation;
- introduce a free hadronic normalization;
- move a holdout after inspecting results;
- create a likelihood or posterior;
- reweight members;
- execute a process bridge;
- modify production;
- push the completion commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 5.1 Wilson, cut, and soft-overlap pilots

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md
docs/next_level/c5_benchmark_manifest.json

docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c6_benchmark_manifest.json

docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
```

These are validation oracles and finite-order operator ingredients. They are not automatically the required continuum microscopic soft sector.

## 5.2 Microscopic light-front root

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c11_regression_report.json
docs/next_level/c14_regression_report.json
```

## 5.3 Matching and evolution root

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c19_matching_basis.json
docs/next_level/c19_matching_fit_manifest.json

docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json

docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_anomalous_dimension_library.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_accuracy_manifest.json

docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_accuracy_manifest.json
```

## 5.4 Bridge and C31 no-go sources

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c29_frozen_bridge_grid.json
docs/next_level/c29_constraint_role_split.json
docs/next_level/c29_cross_root_member_relation.json
docs/next_level/c29_no_double_counting_contract.json

docs/next_level/c30_implementation_report.md
docs/next_level/c30_art25_tmd_definition_manifest.json
docs/next_level/c30_microscopic_tmd_definition_manifest.json
docs/next_level/c30_bridge_scheme_selection.json
docs/next_level/c30_common_bridge_domain.json
docs/next_level/c30_distribution_bridge_capability_matrix.json

docs/next_level/c31_implementation_report.md
docs/next_level/c31_api.md
docs/next_level/c31_normative_source_integration.json
docs/next_level/c31_primary_source_manifest.json
docs/next_level/c31_source_relevance_matrix.json
docs/next_level/c31_three_layer_identity_manifest.json
docs/next_level/c31_microscopic_bare_operator_manifest.json
docs/next_level/c31_microscopic_regulator_manifest.json
docs/next_level/c31_microscopic_wilson_soft_audit.json
docs/next_level/c31_renormalization_component_ledger.json
docs/next_level/c31_source_sufficiency_matrix.json
docs/next_level/c31_project_tmd_definition_manifest.json
docs/next_level/c31_project_scheme_implementation_gap.json
docs/next_level/c31_art25_operator_scheme_manifest.json
docs/next_level/c31_scheme_versus_scale_decomposition.json
docs/next_level/c31_continuum_scheme_equivalence_matrix.json
docs/next_level/c31_hard_tmd_companion_transformation.json
docs/next_level/c31_lf_to_tmd_matching_strategy.json
docs/next_level/c31_partonic_external_state_manifest.json
docs/next_level/c31_partonic_diagram_ledger.json
docs/next_level/c31_tree_level_limit_report.json
docs/next_level/c31_source_sufficiency_decision.json
docs/next_level/c31_missing_calculation_specification.md
docs/next_level/c31_distribution_bridge_capability_matrix.json
docs/next_level/c31_unresolved_physics_gaps.md
```

## 5.5 Formal sources

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

The authoritative Volume XVI PDF remains normative. Do not invent its missing TeX source.

Create:

```text
docs/next_level/c32_normative_source_integration.json
```

---

# 6. Primary-source and derivation authority

Reuse the fourteen C31 source locks. Preserve any additional source under:

```text
data/raw/c32_sources/
```

with exact version and SHA-256 identity.

Classify every source as:

```text
TARGET_PROJECT_OPERATOR_AUTHORITY
TARGET_PROJECT_ONE_LOOP_AUTHORITY
MICROSCOPIC_REGULATOR_METHOD_AUTHORITY
LIGHT_FRONT_PERTURBATION_AUTHORITY
SOFT_RAPIDITY_AUTHORITY
ZERO_BIN_AUTHORITY
HAMILTONIAN_RENORMALIZATION_AUTHORITY
COMPARISON_ONLY
NOT_OPERATOR_IDENTICAL
```

A continuum result may serve as the target oracle. It cannot be labeled a calculation in the C11 regulator.

Every new analytic formula created in C32 must have:

```text
derivation identifier
source assumptions
operator identity
regulator identity
external-state identity
gauge
perturbative order
symbolic-expression hash
generated-code hash
independent check
```

Create:

```text
docs/next_level/c32_primary_source_manifest.json
docs/next_level/c32_derivation_authority_manifest.json
```

---

# 7. Immutable C31 baseline

Before edits, reproduce and record:

```text
1,157 tests
31 builders
37/37 evidence rows
163/163 atlas pages
1,760 C31 requirements
1,680/1,680 C31 negative injections

C28-C31 validators passing
deterministic C31 regeneration

C11:
    REGULATED_MODEL_DENSITY
    gauge-fixed finite-basis overlap
    Wilson order zero
    positive-x antiquark slots
    not a renormalized TMD

renormalization ledger:
    15 C11-specific required components
    all blocking
    all nonzero-unknown where required

matching strategy:
    P-E_UNAVAILABLE

tree status:
    TREE_LEVEL_OPERATOR_LIMIT_VALIDATED
    first omitted order O(alpha_s)

continuum:
    project-to-ART25 convention alignment formally supported
    finite aligned operator factor identity
    ζ prescription/evolution/FNP/CS separate

bridge:
    12 BRIDGE_COMMON_DOMAIN_ONLY
    0 comparison-ready
    no microscopic export
    no rerun
    642 x 0 empty-not-zero external projection
    NO_JOINT_MEASURE

integrity:
    216 production routes
    eight authoritative artifacts byte-identical
    MSHT20_REP outside Git
    no fit, inference, calibration, or status promotion
```

Do not proceed if this baseline does not reproduce.

C32 must not modify:

- C11 historical operator identities or values;
- C12-C14 historical Wilson records;
- C19-C22 historical validation objects;
- C29-C31 frozen bridge grid, roles, or holdouts;
- ART25 members or source covariance;
- C31 project-to-ART25 continuum alignment;
- data ancestry or no-double-counting plans;
- production registry or authoritative artifacts.

Create a new versioned operator-completion and matching root.

---

# 8. Required architecture

Implement or extend immutable objects equivalent to:

```text
C32OperatorCompletionId
MicroscopicTMDOperatorDefinition
MicroscopicStaplePath
MicroscopicRapidityRegulator
MicroscopicSoftSectorId
MicroscopicZeroBinId

LightFrontBasisRegulator
LongitudinalBasisRegulator
TransverseBasisRegulator
EndpointRegulator
ZeroModePolicy
BasisContinuumTrajectory

PartonicStatePlan
PartonicIRRegulator
GaugePlan
PerturbativeOrderPlan

BarePartonicCorrelator
BareSoftFactor
ZeroBinContribution
UVCounterterm
RapidityCounterterm
HamiltonianBasisCounterterm

DistributionTerm
DeltaEndpointTerm
PlusDistributionTerm
RegularDistributionTerm
MellinMomentRecord

RenormalizedPartonicTMD
ProjectPartonicTMDOracle
MatchingDifference
LFToProjectKernel
MatchingRemainder

IRCancellationReport
UVCancellationReport
RapidityCancellationReport
GaugeIndependenceReport
AnomalousDimensionReport
StateIndependenceReport
BasisTrajectoryReport

C32MicroscopicExportGate
C32BridgeRerunGate
C32CapabilityMatrix
C32ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about operator and regulator;
- explicit about perturbative order;
- explicit about external-state IR prescription;
- explicit about basis and continuum trajectory;
- explicit about gauge;
- explicit about UV and rapidity schemes;
- explicit about distributional support;
- state independent when labeled a matching kernel;
- unable to consume ART25 fit data or bridge residuals;
- unreachable from inference and production.

---

# 9. Versioned microscopic operator completion

C32 must not retroactively declare the C11 density to be a physical TMD.

Construct a new validation root:

```text
C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION
```

derived from, but distinct from:

```text
C11_REGULATED_MODEL_DENSITY
```

The new operator definition must specify:

```text
active quark field
bilocal separation
light-front time
Dirac projection gamma+
future/past or common T-even staple choice
staple direction
transverse closure segment
color representation
path ordering
gauge
rapidity regulator
UV regulator
finite-basis regulator
endpoint regulator
zero-mode policy
soft-factor definition
square-root allocation
zero-bin/overlap convention
state normalization
operator normalization
positive-x antiquark convention
```

The relation to C11 must be one of:

```text
EXTENDS_OPERATOR_WITH_DECLARED_WILSON_SOFT_STRUCTURE
TREE_LEVEL_REDUCES_TO_C11
NOT_OPERATOR_EQUIVALENT
UNRESOLVED
```

Required gate:

\[
F_{\mathrm{C32}}^{(0)} = F_{\mathrm{C11}}
\]

only in the exact declared tree-level limit and with every normalization and regulator identity aligned.

If this equality fails, stop before one-loop matching and issue the operator-construction branch.

Create:

```text
docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_operator_identity_decision.json
```

---

# 10. Freeze the regulator and external-state plans

Before calculating one-loop graphs, freeze mutually exclusive plans.

## 10.1 Microscopic regulator plan

Record:

```text
longitudinal resolution K
transverse basis Nmax
oscillator scale bHO
endpoint regulator
basis UV scale
basis IR scale
zero-mode exclusion
boundary conditions
Hamiltonian counterterm identity
continuum trajectory
```

At least three regulator points are required for every claimed asymptotic coefficient.

## 10.2 Partonic infrared plan

Select exactly one primary common IR prescription, for example:

```text
off-shell external quark
small quark mass
declared analytic IR regulator
```

The microscopic and target-project calculations must use the same IR regulator or a separately proved conversion.

## 10.3 Gauge plan

Select a primary covariant-gauge calculation with a symbolic or multi-value gauge parameter. Light-cone-gauge calculations may be independent checks but cannot silently replace the primary route.

## 10.4 Rapidity plan

Use the exact rapidity regulator required by the project target scheme, or define a regulator-specific intermediate scheme with an explicit conversion to the project target.

The rapidity regulator cannot be the finite basis itself unless a theorem or explicit calculation proves it regulates all rapidity regions correctly.

Create:

```text
docs/next_level/c32_regulator_plan_manifest.json
docs/next_level/c32_partonic_external_state_plan.json
docs/next_level/c32_gauge_plan.json
docs/next_level/c32_rapidity_plan.json
```

No plan may be selected after inspecting the matching residual.

---

# 11. Diagram and contribution ledger

At order \(a_s\), audit and calculate every required contribution.

The ledger must include, where nonzero or required:

```text
quark self energy
bilocal operator vertex
real quark emission
real gluon emission into the measured channel
staple-leg attachment
transverse-staple attachment
Wilson-line self energy
staple cusp/endpoints
soft Wilson-line exchange
soft Wilson-line self energies
zero-bin/overlap subtraction
UV counterterm
rapidity counterterm
quark-field counterterm
bilocal-operator counterterm
Hamiltonian mass counterterm
Hamiltonian vertex counterterm
instantaneous-fermion light-front term
instantaneous-gluon light-front term
basis-boundary term
endpoint-regulator term
zero-mode term or proved absence
operator-mixing channel
```

For each contribution record:

```text
diagram ID
operator side
cut/virtual status
color factor
gauge dependence
UV dependence
IR dependence
rapidity dependence
basis dependence
x support
b dependence
source or derivation
symbolic result
numerical result
cancellation partners
```

No absent contribution may be assigned zero without a proof.

Create:

```text
docs/next_level/c32_partonic_diagram_ledger.json
docs/next_level/c32_counterterm_ledger.json
docs/next_level/c32_contribution_dependency_graph.json
```

---

# 12. Distributional x-space authority

Represent one-loop results as typed distributions:

\[
F^{(1)}(x,b)
=
c_\delta(b)\,\delta(1-x)
+
\sum_n c_n(b)\,
\left[\frac{\ln^n(1-x)}{1-x}\right]_+
+
f_{\mathrm{reg}}(x,b).
\]

Do not approximate endpoint distributions with bins or cutoffs in the authoritative analytic result.

Implement:

```text
delta endpoint
plus distributions
regular support
lower-limit plus prescription
Mellin moments
convolution with analytic test functions
```

Required independent checks:

- direct distribution action;
- numerical regulated-limit convergence;
- Mellin moments;
- quark-number moment;
- endpoint cancellation;
- x-space reconstruction.

Create:

```text
docs/next_level/c32_distributional_result_library.json
docs/next_level/c32_endpoint_mellin_report.json
```

---

# 13. Microscopic unsubtracted partonic correlator

Calculate the C32 microscopic unsubtracted quark correlator in the frozen regulator plan:

\[
F_{q,\mathrm{unsub}}^{\mathrm{LF,reg}}
(x,b;
K,N_{\max},b_{\mathrm{HO}},
\rho_{\mathrm{end}},
\delta_{\mathrm{rap}},
p^2,\xi_g).
\]

The result must retain separately:

```text
tree term
virtual term
real term
Wilson term
instantaneous term
basis-boundary term
endpoint-regulator term
zero-mode term
```

Required checks:

- Hermiticity;
- future/past equality for the T-even channel;
- charge conjugation;
- support \(0<x\le 1\);
- tree-level C11 reduction;
- exact color factor;
- basis selection rules;
- assembled versus matrix-free route where applicable;
- finite-volume or quadrature convergence;
- no numerical epsilon stored as physical support.

Create:

```text
docs/next_level/c32_microscopic_unsubtracted_correlator.json
docs/next_level/c32_microscopic_correlator_oracle_report.json
```

---

# 14. Microscopic soft factor

Construct the vacuum soft factor for the same Wilson geometry and rapidity regulator:

\[
S_{\mathrm{LF,reg}}(b)
=
\frac{1}{N_c}
\langle 0|
\operatorname{Tr}
\left[
S_n^\dagger(b)S_{\bar n}(b)
S_{\bar n}^\dagger(0)S_n(0)
\right]
|0\rangle_{\mathrm{reg}} .
\]

The microscopic soft factor must not be imported from the target continuum scheme while calling the result a calculation in the C11 regulator.

Determine whether the finite-basis regulator applies to the soft sector, and if so, how. If the microscopic Hilbert-space regulator has no meaningful vacuum soft-sector implementation, report that as a structural obstruction.

Required checks:

- Wilson geometry identity;
- color representation;
- rapidity divergence;
- UV divergence;
- gauge dependence before combination;
- future/past T-even equality;
- exponentiation/order consistency at one loop;
- continuum-regulator comparison;
- basis trajectory where applicable.

Create:

```text
docs/next_level/c32_microscopic_soft_factor.json
docs/next_level/c32_soft_sector_capability_report.json
```

---

# 15. Zero-bin and overlap subtraction

Calculate the overlap between the microscopic collinear region and the soft region.

Implement the declared subtraction:

```text
zero-bin
soft-bin
overlap projector
or a proved equivalent
```

The subtraction must use the same measurement, external state, rapidity regulator, and basis conventions as the collinear calculation.

Required checks:

- overlap limit of the collinear integrand;
- equality to the corresponding soft-region expansion where expected;
- missing-subtraction residual;
- duplicate-subtraction residual;
- rapidity-log cancellation pattern;
- no double counting.

Create:

```text
docs/next_level/c32_zero_bin_overlap_manifest.json
docs/next_level/c32_overlap_subtraction_report.json
```

---

# 16. UV and rapidity renormalization

Define:

\[
F_q^{\mathrm{LF,ren}}
=
Z_q^{\mathrm{UV}}
R_q^{\mathrm{rap}}
\,
F_{q,\mathrm{unsub}}^{\mathrm{LF,reg}}
\,
\left[
S_{\mathrm{LF,reg}}
\right]^{-1/2}
\]

with any zero-bin/overlap subtraction placed exactly once according to the selected convention.

Extract separately:

```text
quark-field UV factor
bilocal-operator UV factor
Wilson/cusp UV factor
rapidity counterterm
soft allocation
Hamiltonian/basis counterterms
```

Required closure:

- UV poles or cutoff logarithms cancel according to the declared renormalization condition;
- rapidity poles/logarithms cancel from the renormalized TMD;
- the remaining \(\mu\) anomalous dimension matches the target operator;
- the remaining \(\zeta\) anomalous dimension matches the target operator;
- gauge-parameter dependence cancels;
- the soft factor is not counted twice.

Create:

```text
docs/next_level/c32_uv_renormalization_manifest.json
docs/next_level/c32_rapidity_renormalization_manifest.json
docs/next_level/c32_renormalized_partonic_tmd.json
```

---

# 17. Target project-scheme oracle

Evaluate the same partonic operator in the declared project TMD scheme using the same external-state IR prescription.

The target oracle must preserve:

```text
operator
Wilson geometry
soft allocation
UV scheme
rapidity scheme
mu
zeta
external momentum
IR regulator
gauge
x distribution
b convention
```

Use the source-qualified continuum expression where available and independently reproduce at least:

```text
tree term
one-loop delta term
one-loop plus/regular terms
UV anomalous dimension
rapidity anomalous dimension
quark-number moment
```

Create:

```text
docs/next_level/c32_project_partonic_tmd_oracle.json
docs/next_level/c32_project_oracle_validation_report.json
```

The C31 project-to-ART25 adapter remains a downstream read-only transformation.

---

# 18. Extract the matching difference

At one loop, extract the matching kernel from the difference between the target and microscopic renormalized partonic matrix elements.

Schematically:

\[
Z^{(1)}_{\mathrm{LF}\to\mathrm{project}}
=
F_{\mathrm{project}}^{(1)}
-
F_{\mathrm{LF,ren}}^{(1)}
\]

with the precise convolution/inverse relation implemented distributionally.

The matching coefficient must be:

```text
IR finite
state independent
gauge independent
independent of ART25 members and data
independent of the proton wave function
explicit in the finite-basis regulator
explicit in mu and zeta
explicit in first omitted order
```

Audit possible channels:

```text
q <- q
q <- g
q <- qbar
flavor nonsinglet
quark singlet
```

Do not assume the off-diagonal channels vanish. Prove their status at the declared order.

Create:

```text
docs/next_level/c32_lf_to_project_matching_library.json
docs/next_level/c32_matching_channel_matrix.json
docs/next_level/c32_matching_remainder_manifest.json
```

---

# 19. Cancellation and closure tests

A positive one-loop matching status requires all applicable tests.

## 19.1 Infrared closure

Report:

```text
IR regulator dependence on microscopic side
IR regulator dependence on target side
IR dependence of their difference
```

The difference must be IR finite within symbolic identity or controlled numerical convergence.

## 19.2 UV closure

Report:

```text
bare UV dependence
counterterms
renormalized remainder
target anomalous dimension
matching-kernel UV dependence
```

## 19.3 Rapidity closure

Report:

```text
unsubtracted rapidity dependence
soft rapidity dependence
zero-bin rapidity dependence
rapidity counterterm
renormalized rapidity dependence
CS-kernel convention
```

## 19.4 Gauge closure

Evaluate at symbolic \(\xi_g\) or at enough frozen values to establish cancellation independently.

## 19.5 Sum-rule closure

Test:

```text
quark number
charge conjugation
flavor universality
tree limit
small-b limit
```

## 19.6 Threshold and RG closure

Test:

```text
mu RG
zeta RG
commuting two-scale evolution
threshold round trip
project-to-ART25 downstream compatibility
```

Create:

```text
docs/next_level/c32_ir_cancellation_report.json
docs/next_level/c32_uv_cancellation_report.json
docs/next_level/c32_rapidity_cancellation_report.json
docs/next_level/c32_gauge_independence_report.json
docs/next_level/c32_sum_rule_report.json
docs/next_level/c32_rg_threshold_report.json
```

Do not fabricate a zero residual where a calculation is unavailable.

---

# 20. Basis and regulator convergence trajectory

A matching coefficient extracted at one finite basis point is not sufficient.

Run at least three nested points in:

```text
K
Nmax
bHO
endpoint-regulator scale
basis UV scale
basis IR scale
```

where the project supports them.

Determine separately:

```text
logarithmic cutoff dependence
finite regulator constant
power-suppressed basis dependence
endpoint artifacts
zero-mode sensitivity
interpolation/quadrature error
```

Fit only analytically predicted cutoff structures. Do not fit the kernel to ART25 or hadronic output.

Required convergence statuses:

```text
CONTINUUM_TRAJECTORY_RESOLVED
LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
FINITE_BASIS_ONLY
NONUNIVERSAL_TRAJECTORY
UNAVAILABLE
```

Create:

```text
docs/next_level/c32_basis_regulator_trajectory.json
docs/next_level/c32_continuum_extrapolation_report.json
docs/next_level/c32_regulator_power_correction_manifest.json
```

---

# 21. State-independence tests

A matching kernel must not depend on the hadron state.

Test the extracted kernel using at least:

```text
two external quark momenta
two IR-regulator values
u and d labels
quark and positive-x antiquark charge-conjugate states
at least one alternate finite-basis resolution
```

Where meaningful, test the kernel on a simple composite toy state not used in extraction.

Required result:

```text
same kernel within declared order and regulator remainder
```

If the kernel depends irreducibly on the C11 proton coefficients, classify:

```text
STATE_DEPENDENT_MODEL_MAP
```

and do not call it matching.

Create:

```text
docs/next_level/c32_state_independence_report.json
docs/next_level/c32_flavor_charge_conjugation_report.json
```

---

# 22. Conditional microscopic proton export

Only when all of the following pass:

```text
operator completion
tree reduction
microscopic soft sector
zero-bin/overlap
UV renormalization
rapidity renormalization
one-loop project oracle
IR-finite matching difference
gauge independence
state independence
basis trajectory
remainder control
```

export:

```text
u
d
ubar
dbar
```

on the immutable twelve-point grid.

The export chain is:

```text
C11 state
    -> C32 completed microscopic operator
    -> LF-regulated matrix element
    -> LF-to-project matching
    -> project renormalized TMD
    -> read-only C31 project-to-ART25 alignment
    -> ART25 mu=Q, zeta=Q^2 scale map
```

Every row retains all regulator, matching, evolution, scheme, and remainder identity.

No free normalization is permitted.

Create:

```text
docs/next_level/c32_microscopic_renormalized_tmd_export.json
docs/next_level/c32_microscopic_export_execution_report.json
```

If any gate fails, output deterministic empty coordinates, never zero-valued physical TMDs.

---

# 23. Conditional twelve-point bridge rerun

Only when the microscopic export gate passes, rerun the immutable C30 bridge.

Preserve:

```text
all 642 ART25 members
external covariance rank
external covariance null space
eight calibration-candidate and four holdout roles
NO_JOINT_MEASURE
data ancestry
no-double-counting plan
all discrepancy classes
```

Allowed diagnostics:

```text
pointwise residual
relative residual
external percentile
whitened residual
null-space residual
regulator-trajectory comparison
matching-order comparison
holdout summary
```

Forbidden:

```text
likelihood
p-value
posterior
parameter optimization
member reweighting
```

Create:

```text
docs/next_level/c32_distribution_bridge_rerun.json
docs/next_level/c32_distribution_bridge_capability_matrix.json
docs/next_level/c32_distribution_bridge_closure_report.json
```

Historical C30 and C31 matrices remain immutable.

---

# 24. Remainder and uncertainty separation

Keep separate:

```text
first omitted perturbative order
finite-basis UV remainder
finite-basis IR remainder
endpoint-regulator remainder
zero-mode remainder
soft-sector remainder
zero-bin remainder
rapidity-renormalization remainder
Hamiltonian counterterm remainder
operator-mixing remainder
continuum-extrapolation remainder
project-to-ART25 downstream remainder
C11/C14 parent-axis difference
TTN/basis state truncation
external ART25 covariance
external-model discrepancy
numerical error
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No microscopic matching remainder may be absorbed into ART25 covariance.

Create:

```text
docs/next_level/c32_matching_uncertainty_budget.json
docs/next_level/c32_remainder_separation_manifest.json
```

---

# 25. Scientifically valid no-go outcomes

C32 must support a rigorous negative result.

## 25.1 Operator-completion obstruction

Issue:

```text
C32_OPERATOR_COMPLETION_INCOMPATIBLE_WITH_C11
```

when the explicit Wilson/soft operator does not reduce to C11 at tree level.

## 25.2 Soft-sector obstruction

Issue:

```text
C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED
```

when the finite-basis regulator has no consistent vacuum soft-sector realization.

## 25.3 Nonuniversal matching obstruction

Issue:

```text
C32_STATE_INDEPENDENT_MATCHING_UNAVAILABLE
```

when the extracted difference depends on the proton state or basis coefficients.

## 25.4 Continuum-trajectory obstruction

Issue:

```text
C32_REGULATOR_TRAJECTORY_UNRESOLVED
```

when the basis sequence does not separate logarithmic, finite, and power-suppressed terms.

## 25.5 One-loop incompleteness

Issue:

```text
C32_TREE_LEVEL_ONLY
```

when the tree limit closes but one-loop UV/rapidity/soft/gauge conditions do not.

Every no-go status must include the next missing calculation, not merely a generic “more work” statement.

Create:

```text
docs/next_level/c32_source_sufficiency_decision.json
docs/next_level/c32_no_go_decision_tree.json
docs/next_level/c32_missing_calculation_specification.md
```

---

# 26. Holdouts

Freeze holdouts before analytic simplification, numerical tuning, or trajectory fitting.

Reserve at least:

```text
one delta-endpoint coefficient
one plus-distribution coefficient
one regular x-space term
one Mellin moment
one quark-number moment
one quark self-energy term
one Wilson-line term
one soft-factor term
one zero-bin term
one UV counterterm
one rapidity counterterm
one gauge-parameter point
one IR-regulator point
one alternate external momentum
one alternate basis resolution
one endpoint-regulator point
one q<-g channel decision
one antiquark charge-conjugation check
one project-oracle point
one project-to-ART25 downstream round trip
one frozen u bridge point
one frozen d bridge point
one frozen ubar bridge point
one frozen dbar bridge point
one large-b unavailable control
one ART25-member-independence control
```

No failed holdout may be moved into derivation or trajectory fitting.

---

# 27. Required benchmark families

Implement at least:

## R0-A: immutable baseline and three-layer identity

- C11 model density;
- C32 operator completion;
- project TMD;
- ART25 downstream object.

## R0-B: operator completion and tree reduction

- staple;
- regulator;
- soft definition;
- exact C11 tree reduction.

## R0-C: frozen regulator and external-state plans

- basis;
- IR;
- gauge;
- rapidity;
- no post-result changes.

## R0-D: complete one-loop diagram ledger

- real;
- virtual;
- Wilson;
- soft;
- instantaneous;
- counterterms.

## R0-E: distributional x-space algebra

- delta;
- plus;
- regular;
- Mellin;
- convolution.

## R0-F: microscopic unsubtracted correlator

- support;
- Hermiticity;
- link-even identity;
- basis rules.

## R0-G: microscopic soft factor

- same Wilson geometry;
- same rapidity regulator;
- UV/rapidity structure.

## R0-H: zero-bin and overlap

- region expansion;
- count once;
- missing/duplicate controls.

## R0-I: UV renormalization

- field;
- operator;
- Wilson/cusp;
- Hamiltonian/basis.

## R0-J: rapidity renormalization

- regulator;
- soft cancellation;
- counterterm;
- anomalous dimension.

## R0-K: target project oracle

- same external state;
- source formula;
- independent checks.

## R0-L: IR-finite matching difference

- channel matrix;
- state independence;
- no hadronic fitting.

## R0-M: gauge and anomalous-dimension closure

- gauge;
- mu;
- zeta;
- threshold.

## R0-N: basis/regulator trajectory

- three or more points;
- logarithm;
- finite constant;
- power correction.

## R0-O: flavor and charge conjugation

- u/d universality where proved;
- quark/antiquark relation;
- mixing decisions.

## R0-P: conditional microscopic export

- exact gate;
- no free normalization;
- empty-not-zero failure.

## R0-Q: conditional bridge rerun

- 642 members;
- null space;
- frozen roles;
- no inference.

## R0-R: deterministic isolation

- no source mutation;
- no fit;
- no production change.

---

# 28. Negative injections

Create at least **1,840 ordered C32 negative injections** with stable IDs and deterministic expected diagnostics.

Include:

## Operator completion

- C11 silently relabeled renormalized;
- staple omitted;
- transverse closure omitted;
- wrong path direction;
- color representation lost;
- operator normalization changed;
- tree reduction failure hidden;
- new operator treated as historical C11.

## Regulator plans

- regulator changed after results;
- K/Nmax/bHO identity dropped;
- endpoint regulator omitted;
- zero-mode policy omitted;
- basis UV/IR scales conflated;
- microscopic basis called rapidity regulator without proof;
- different IR regulators used on two sides;
- gauge plan changed after holdout inspection.

## Diagram ledger

- self energy omitted;
- real graph omitted;
- Wilson attachment omitted;
- Wilson self energy omitted;
- cusp term omitted;
- soft graph omitted;
- zero-bin omitted;
- instantaneous-fermion term omitted;
- instantaneous-gluon term omitted;
- Hamiltonian counterterm omitted;
- basis-boundary term omitted;
- zero-mode term silently zeroed.

## Distributional algebra

- delta term dropped;
- plus distribution replaced by cutoff;
- endpoint cutoff treated as identity;
- Mellin moment inconsistent;
- quark-number moment violated;
- numerical bin fit substituted for distribution.

## Soft and zero-bin

- continuum soft factor copied into microscopic regulator;
- soft factor counted twice;
- square-root allocation wrong;
- overlap omitted;
- overlap duplicated;
- rapidity log hidden by numerical cutoff;
- vacuum soft sector assumed without construction.

## UV and rapidity

- UV pole/log left uncanceled;
- rapidity pole/log left uncanceled;
- field factor omitted;
- bilocal factor omitted;
- cusp counterterm omitted;
- rapidity counterterm omitted;
- anomalous dimension mismatch hidden;
- gauge dependence hidden.

## Matching extraction

- ART25 hadron ratio used;
- twelve-point ratio fitted;
- member-dependent kernel;
- state-dependent kernel called matching;
- IR dependence left in kernel;
- q<-g channel assumed zero;
- flavor dependence invented;
- antiquark copied without charge conjugation;
- first omitted order set to zero.

## Basis trajectory

- one basis point called continuum;
- arbitrary polynomial fit;
- ART25 residual used to select trajectory;
- logarithmic and power terms merged;
- endpoint artifact hidden;
- zero-mode sensitivity discarded;
- nonconvergent trajectory called converged.

## Conditional export and bridge

- export before matching gates;
- free normalization introduced;
- failed coordinate imputed;
- empty vector treated as zero;
- ART25 member dropped;
- covariance null space regularized;
- holdout moved;
- residual called likelihood;
- p-value reported;
- member reweighted.

## Scope and integrity

- project-to-ART25 alignment refitted;
- process bridge executed;
- W+Y claimed;
- gluon/T-odd adapter activated;
- deuteron prediction claimed;
- calibration performed;
- posterior sampled;
- emulator trained;
- C31 historical record overwritten;
- raw MSHT files committed;
- production registry changed;
- authoritative artifact changed;
- nondeterministic manifest.

---

# 29. Deliverables

Create at least:

```text
docs/next_level/c32_implementation_report.md
docs/next_level/c32_api.md
docs/next_level/c32_requirement_coverage.json
docs/next_level/c32_normative_source_integration.json
docs/next_level/c32_primary_source_manifest.json
docs/next_level/c32_derivation_authority_manifest.json

docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_operator_identity_decision.json

docs/next_level/c32_regulator_plan_manifest.json
docs/next_level/c32_partonic_external_state_plan.json
docs/next_level/c32_gauge_plan.json
docs/next_level/c32_rapidity_plan.json

docs/next_level/c32_partonic_diagram_ledger.json
docs/next_level/c32_counterterm_ledger.json
docs/next_level/c32_contribution_dependency_graph.json

docs/next_level/c32_distributional_result_library.json
docs/next_level/c32_endpoint_mellin_report.json

docs/next_level/c32_microscopic_unsubtracted_correlator.json
docs/next_level/c32_microscopic_correlator_oracle_report.json
docs/next_level/c32_microscopic_soft_factor.json
docs/next_level/c32_soft_sector_capability_report.json
docs/next_level/c32_zero_bin_overlap_manifest.json
docs/next_level/c32_overlap_subtraction_report.json

docs/next_level/c32_uv_renormalization_manifest.json
docs/next_level/c32_rapidity_renormalization_manifest.json
docs/next_level/c32_renormalized_partonic_tmd.json

docs/next_level/c32_project_partonic_tmd_oracle.json
docs/next_level/c32_project_oracle_validation_report.json

docs/next_level/c32_lf_to_project_matching_library.json
docs/next_level/c32_matching_channel_matrix.json
docs/next_level/c32_matching_remainder_manifest.json

docs/next_level/c32_ir_cancellation_report.json
docs/next_level/c32_uv_cancellation_report.json
docs/next_level/c32_rapidity_cancellation_report.json
docs/next_level/c32_gauge_independence_report.json
docs/next_level/c32_sum_rule_report.json
docs/next_level/c32_rg_threshold_report.json

docs/next_level/c32_basis_regulator_trajectory.json
docs/next_level/c32_continuum_extrapolation_report.json
docs/next_level/c32_regulator_power_correction_manifest.json
docs/next_level/c32_state_independence_report.json
docs/next_level/c32_flavor_charge_conjugation_report.json

docs/next_level/c32_microscopic_renormalized_tmd_export.json
docs/next_level/c32_microscopic_export_execution_report.json
docs/next_level/c32_distribution_bridge_rerun.json
docs/next_level/c32_distribution_bridge_capability_matrix.json
docs/next_level/c32_distribution_bridge_closure_report.json

docs/next_level/c32_matching_uncertainty_budget.json
docs/next_level/c32_remainder_separation_manifest.json

docs/next_level/c32_source_sufficiency_decision.json
docs/next_level/c32_no_go_decision_tree.json
docs/next_level/c32_missing_calculation_specification.md

docs/next_level/c32_holdout_report.json
docs/next_level/c32_injection_manifest.json
docs/next_level/c32_regression_report.json
docs/next_level/c32_unresolved_physics_gaps.md
```

Add ADRs for:

- C32 operator completion versus historical C11;
- microscopic soft-sector authority;
- common partonic IR regulator;
- finite-basis rapidity regulator;
- zero-bin/overlap convention;
- Hamiltonian/basis counterterms in a TMD operator;
- distributional endpoint authority;
- state-independent matching criterion;
- basis-to-continuum trajectory;
- conditional export gate;
- rigorous no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy symbolic expressions, quadrature tables, basis trajectories, and conditional member arrays may remain outside Git under a declared content-addressed runtime directory. Commit their schemas, hashes, dimensions, plan order, and deterministic reconstruction commands.

---

# 30. Acceptance criteria

C32/R0 is complete only when:

1. The exact C31 baseline reproduces before edits.
2. Historical C11 remains a regulated model density.
3. A versioned C32 operator-completion identity is created.
4. The C32 operator reduces exactly to C11 at the declared tree limit, or fails closed.
5. The finite-basis regulator is fully specified.
6. The external-state IR regulator is frozen before calculation.
7. The gauge plan is frozen before calculation.
8. The rapidity-regulator plan is frozen before calculation.
9. Every required one-loop contribution receives an explicit status.
10. No absent contribution is silently zero.
11. Endpoint distributions are represented exactly.
12. Mellin and quark-number checks close where claimed.
13. The microscopic unsubtracted correlator is calculated or explicitly unavailable.
14. The microscopic soft factor is calculated in the same operator/regulator geometry or explicitly unavailable.
15. Zero-bin/overlap subtraction is placed exactly once.
16. UV renormalization is explicit.
17. Rapidity renormalization is explicit.
18. The target project oracle uses the same IR prescription.
19. The matching difference is IR finite when claimed.
20. Gauge dependence cancels when claimed.
21. UV dependence closes according to the declared scheme when claimed.
22. Rapidity dependence closes according to the declared scheme when claimed.
23. The \(\mu\) anomalous dimension matches the target when claimed.
24. The \(\zeta\) anomalous dimension matches the target when claimed.
25. Threshold and RG round trips are tested.
26. All possible one-loop mixing channels receive a decision.
27. The matching kernel is independent of ART25 members and data.
28. The matching kernel is state independent when labeled matching.
29. At least three basis/regulator points support any continuum claim.
30. Logarithmic, finite, and power-suppressed regulator effects remain separate.
31. Tree-level closure is not promoted to one-loop readiness.
32. First omitted order and remainder remain visible.
33. Microscopic proton export occurs only after every matching gate passes.
34. Failed exports remain empty, not zero.
35. The twelve-point bridge reruns only after the export gate passes.
36. All 642 external identities and covariance null spaces survive any rerun.
37. Frozen bridge roles and holdouts remain unchanged.
38. `NO_JOINT_MEASURE` remains unchanged.
39. Data ancestry and no-double-counting remain intact.
40. No matching remainder is absorbed into ART25 covariance.
41. No fit, calibration, likelihood, posterior, optimization, reweighting, or emulator is created.
42. No process bridge is executed or promoted.
43. Gluon, T-odd, spin-1, and deuteron matching remain outside scope.
44. Every no-go status contains an exact missing-calculation specification.
45. All prior tests, builders, requirements, injections, and manifests remain passing.
46. The production registry remains exactly 216 routes.
47. All eight authoritative artifacts remain byte-identical.
48. Raw transferred source files remain outside Git absent permission.
49. Every C32 negative injection yields the expected diagnostic.
50. All C32 manifests reproduce byte-for-byte.
51. The working tree is clean.
52. A local completion commit is created and not pushed.

C32 may complete without a one-loop matching kernel. A rigorous operator, soft-sector, state-independence, or regulator-trajectory obstruction is a valid scientific result.

---

# 31. Outcome branches

## Branch A: one-loop microscopic matching closes

When:

```text
C32_OPERATOR_COMPLETION_VALIDATED
C32_MICROSCOPIC_SOFT_SECTOR_VALIDATED
C32_LF_TO_PROJECT_ONE_LOOP_MATCHING_VALIDATED
C32_STATE_INDEPENDENT_MATCHING_VALIDATED
```

and at least one flavor becomes:

```text
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

the exact next package is:

> **C33/B2 — frozen-bridge sensitivity, parameter ownership, identifiability, and discrepancy-prior readiness, still without calibration**

## Branch B: operator and one-loop calculation close but regulator trajectory does not

The exact next package is:

> **C33/R1 — finite-basis continuum trajectory, zero-mode, and regulator-power-correction completion**

## Branch C: operator completion closes but the microscopic soft sector is unavailable

The exact next package is:

> **C33/S0 — explicit finite-basis vacuum soft sector and rapidity-renormalization construction**

## Branch D: the matching difference is state dependent

The exact next package is:

> **C33/O2 — redesign of the microscopic TMD operator and regulator to admit universal matching**

## Branch E: the completed operator does not reduce to C11

The exact next package is:

> **C33/O1 — replace the C11 density bridge with a new microscopic subtracted-TMD operator root**

## Branch F: only the tree-level limit closes

The exact next package is:

> **C33/R0A — one-loop diagram, counterterm, and subtraction completion**

Do not authorize inference from any branch automatically.

---

# 32. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C32_OPERATOR_COMPLETION_AUDITED
C32_C11_TREE_REDUCTION_VALIDATED
C32_REGULATOR_EXTERNAL_STATE_PLANS_FROZEN
C32_ONE_LOOP_DIAGRAM_LEDGER_COMPLETE
C32_DISTRIBUTIONAL_ALGEBRA_VALIDATED
C32_PROJECT_PARTONIC_ORACLE_VALIDATED
C32_BASIS_REGULATOR_TRAJECTORY_AUDITED
C32_SOURCE_SUFFICIENCY_DECISION_COMPLETE
C32_DISTRIBUTION_BRIDGE_CAPABILITY_MATRIX_COMPLETE
```

Issue only when every corresponding gate passes:

```text
C32_MICROSCOPIC_UNSUBTRACTED_CORRELATOR_VALIDATED
C32_MICROSCOPIC_SOFT_SECTOR_VALIDATED
C32_ZERO_BIN_OVERLAP_VALIDATED
C32_UV_RENORMALIZATION_VALIDATED
C32_RAPIDITY_RENORMALIZATION_VALIDATED
C32_LF_TO_PROJECT_ONE_LOOP_MATCHING_VALIDATED
C32_STATE_INDEPENDENT_MATCHING_VALIDATED
C32_MICROSCOPIC_RENORMALIZED_TMD_EXPORT_VALIDATED
BRIDGE_DISTRIBUTION_COMPARISON_READY
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

# 33. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- operator-completion identity and C11 tree-reduction status;
- frozen regulator, external-state, gauge, and rapidity plans;
- one-loop diagram and counterterm coverage;
- distributional endpoint and Mellin residuals;
- microscopic unsubtracted-correlator status;
- microscopic soft-sector status;
- zero-bin/overlap status;
- UV and rapidity renormalization status;
- target project-oracle status;
- matching channels and perturbative order;
- IR, UV, rapidity, gauge, RG, threshold, and sum-rule residuals;
- basis/regulator trajectory and continuum status;
- state-independence and flavor/antiquark results;
- first omitted order and remainder;
- microscopic export count and hashes;
- bridge point counts by status;
- external covariance and null-space preservation;
- exact no-go status when blocked;
- exact next-package branch;
- confirmation that no ART25 data/member entered the matching derivation;
- confirmation that no fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a finite-basis tree-level overlap, a continuum project oracle, or a state-dependent hadronic conversion as a completed regulator-specific TMD matching kernel.
