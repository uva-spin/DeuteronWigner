# C38/M0A Codex Work Package

## Title

**Finite-basis spacelike Wilson insertion, common-IR partonic probe states, light-front instantaneous/boundary sectors, counterterm architecture, and discrete-to-distributional longitudinal map**

## Authoritative baseline

Start from the clean local C37/R2 completion commit whose abbreviated hash is:

```text
0ac139f
```

The uploaded implementation report does not provide the full hash. Do not invent it. Resolve and record the authoritative baseline before edits:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor dee1dfb HEAD
git merge-base --is-ancestor bbefd963ea14bf79884ec3a5c1a503581a6dd21e HEAD
```

The resolved clean `HEAD` is the C38 starting commit only when it contains and reproduces:

```text
docs/next_level/c37_implementation_report.md
docs/next_level/c37_source_sufficiency_decision.json
docs/next_level/c37_no_go_decision_tree.json
docs/next_level/c37_missing_calculation_specification.md
docs/next_level/c37_regression_report.json
handoff/ROADMAP.md
```

Required ancestry includes:

```text
C36/O4:
    resolve full local commit abbreviated dee1dfb

C35/S0C:
    bbefd963ea14bf79884ec3a5c1a503581a6dd21e

C34/S0A:
    6bdb44be2afc79e817f69ce0e35813da8a394db7

C32/R0:
    0d7b94a5e86882b23a56d4c1f11900d554756a18

C28/P1D:
    52678312906bf5cc0bb8664e2486d5d676a6b723
```

Do not use `origin/main` when the local branch is ahead of the remote.

The authoritative Volume XXI source remains:

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

Read and hash-audit it. Preserve its historical two-root and renormalization semantics. Add a versioned finite-basis partonic-probe crosswalk or addendum rather than silently rewriting Volume XXI.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Why C38/M0A is the exact next package

C37 keeps the C36 physical regulator decision fixed:

```text
O4-SPACELIKE-COLLINS-JMY
```

but reaches the rigorous no-go:

```text
C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE
```

The no-go is not a statement that the finite-basis correction vanishes. It establishes that the finite light-front regulator lacks the operator and probe infrastructure needed to define the one-loop partonic matrix element.

The exact missing prerequisites are:

```text
1. a regulator-identical spacelike Wilson insertion in the finite basis;

2. common-IR, color-fundamental partonic probe states rather than a proton
   state or color-singlet baryon basis;

3. executable one-quark and quark-gluon probe sectors with exact
   normalization and comparison maps;

4. a complete light-front instantaneous, constrained, transverse-boundary,
   endpoint, and zero-mode sector at the declared order;

5. partonic mass, field, Hamiltonian, vertex, operator, Wilson-line, and
   basis counterterm records and renormalization conditions;

6. an exact map from discrete longitudinal support to the continuum
   distributional x algebra;

7. a factorized basis/regulator trajectory with refinement maps and
   holdouts.
```

Therefore no common-IR continuum-to-finite-basis difference and no matching kernel were calculated. C38 must build these prerequisites. It must not manufacture the kernel or use a proton-level ratio.

C38 is the materialization package that turns the architecture-ready C36 spacelike scheme into an executable finite-basis partonic calculation root.

---

# 2. Fixed scientific decisions

The following decisions are immutable in C38:

```text
physical rapidity scheme:
    O4-SPACELIKE-COLLINS-JMY

paired roots:
    C36_COLLINEAR_ROOT, B=1 hadronic ownership
    C36_SOFT_ROOT,      B=0 universal soft ownership

soft ownership:
    outside the hadron TTN

historical negative control:
    C35 finite-cell modified-delta no-go and Ward defect

historical microscopic parent:
    C11 finite-basis regulated model density

tree identity:
    the C36 spacelike operator reduces to all twelve nonzero
    C11 u/d/ubar/dbar parents at g=0

downstream target:
    selected spacelike scheme
      -> project renormalized scheme
      -> read-only project/ART25 convention
```

C38 must not reopen the regulator-family audit.

C38 must not replace the selected spacelike scheme with modified delta, an exponential regulator, a finite-length regulator, an auxiliary representation, or a dressed-field architecture merely because one is easier to implement.

An auxiliary-field construction may remain an oracle or representation of the selected spacelike Wilson geometry. It is not an additional physical soft factor.

---

# 3. Primary objective

Create a distinct partonic finite-basis calculation root:

```text
C38_FINITE_BASIS_PARTONIC_PROBE_ROOT
```

and materialize the chain:

```text
C36 spacelike finite-rapidity operator
    -> color-fundamental one-quark external probe sector
    -> one-quark-plus-one-gluon intermediate/real sector
    -> common IR prescription shared with the continuum oracle
    -> executable spacelike longitudinal and transverse Wilson insertion
    -> finite-basis real and virtual operator matrix elements
    -> instantaneous, constrained, zero-mode, endpoint, and boundary terms
    -> complete counterterm architecture and renormalization conditions
    -> discrete-x distribution functional and convolution interface
    -> factorized resolution/regulator trajectory
    -> exact readiness gate for the C39 one-loop matching calculation
```

C38 normally stops before calculating the complete one-loop matching difference.

It may calculate tree-level and selected first-order matrix-element oracles needed to validate the new infrastructure, but it must not issue a universal matching kernel unless every C39-level one-loop, subtraction, renormalization, channel, and state-independence gate has unexpectedly and independently closed.

---

# 4. Scientific boundary

C38 is:

```text
finite-basis partonic-probe specific
color-fundamental
spacelike finite-rapidity Wilson-line specific
one-quark and quark-gluon sector specific
common-IR explicit
light-front Hamiltonian explicit
instantaneous/boundary/zero-mode explicit
counterterm and renormalization-condition explicit
distributional-x interface explicit
trajectory and refinement explicit
validation only
non-inferential
```

C38 is not:

```text
a proton calculation
a hadron-level matching ratio
a microscopic proton TMD export
a complete one-loop matching result by assumption
an ART25 comparison
a fit
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a process calculation
a deuteron prediction
a gluon-TMD or T-odd package
a production promotion
```

The external partonic probe is an unphysical matching state and must never be confused with the C11 proton.

---

# 5. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C5-C38 Hamiltonian, basis, Wilson, cut, soft, regulator, partonic, matching, evolution, bridge, formal-volume, primary-source, test, API, manifest, ADR, and roadmap files before edits.

Continue autonomously until every applicable acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository source and complete git history;
- preserve additional primary sources and ancillaries;
- construct the dedicated partonic probe Hilbert space;
- define one-quark and quark-gluon states;
- select and implement one common IR plan;
- implement spacelike Wilson segments and their finite-basis matrix elements;
- construct instantaneous and constrained sectors;
- materialize zero-mode and transverse-boundary controls;
- define counterterm equations and renormalization conditions;
- build discrete distribution functionals and refinement maps;
- execute deterministic validation and fault injections.

Do not:

- contact authors;
- alter C11-C37 historical results;
- use the proton as the matching probe;
- use ART25 members, data, chi2, residuals, or frozen bridge values;
- fit counterterms to hadron observables;
- infer a continuous distribution from the twelve bridge points;
- call energy convergence TMD convergence;
- export a microscopic proton TMD;
- rerun the bridge;
- create inference or production routes;
- push the completion commit.

---

# 6. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 6.1 Finite light-front basis and Hamiltonian roots

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
```

C9’s partonic-looking quark-gluon vertices and instantaneous benchmarks are methodological ancestors. They are not automatically the C38 color-fundamental partonic probe calculation.

## 6.2 Wilson, cut, path, and soft roots

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md
docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
```

## 6.3 Distribution, matching, and evolution roots

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
```

The C22 distribution algebra is a target interface and oracle. It is not a finite-basis longitudinal map.

## 6.4 Regulator and matching history

```text
docs/next_level/c31_implementation_report.md
docs/next_level/c32_implementation_report.md
docs/next_level/c33_implementation_report.md
docs/next_level/c34_implementation_report.md
docs/next_level/c35_implementation_report.md

docs/next_level/c36_implementation_report.md
docs/next_level/c36_joint_root_identity.json
docs/next_level/c36_finite_rapidity_direction_manifest.json
docs/next_level/c36_joint_regulator_manifest.json
docs/next_level/c36_spacelike_collinear_definition.json
docs/next_level/c36_spacelike_soft_definition.json
docs/next_level/c36_soft_allocation_convention.json
docs/next_level/c36_c11_tree_reduction_report.json
docs/next_level/c36_finite_basis_compatibility.json
docs/next_level/c36_future_matching_strategy.json
docs/next_level/c36_overlap_convention.json
docs/next_level/c36_continuation_gate.json

docs/next_level/c37_implementation_report.md
docs/next_level/c37_api.md
docs/next_level/c37_requirement_coverage.json
docs/next_level/c37_normative_source_integration.json
docs/next_level/c37_primary_source_manifest.json
docs/next_level/c37_derivation_authority_manifest.json
docs/next_level/c37_calculation_plan.json
docs/next_level/c37_external_state_plan.json
docs/next_level/c37_finite_basis_partonic_collinear.json
docs/next_level/c37_finite_basis_contribution_ledger.json
docs/next_level/c37_finite_basis_counterterm_ledger.json
docs/next_level/c37_discrete_x_distribution_map.json
docs/next_level/c37_basis_regulator_trajectory.json
docs/next_level/c37_source_sufficiency_decision.json
docs/next_level/c37_missing_calculation_specification.md
docs/next_level/c37_regression_report.json
```

## 6.5 Formal sources

```text
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/volume_xx_source_reproducible_bridge_geometry.tex
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Create:

```text
docs/next_level/c38_normative_source_integration.json
docs/next_level/c38_volume_xxi_partonic_probe_crosswalk.json
```

---

# 7. Primary-source and derivation authority

Reuse the exact C36/C37 source locks.

Preserve any new source under:

```text
data/raw/c38_sources/
```

with exact version and SHA-256 identity.

Audit source authority for:

```text
light-front one-particle and qg Fock-state normalization
light-front perturbation theory and energy denominators
off-shell or massive partonic external-state matching
spacelike Wilson-line insertions in Hamiltonian/basis language
transverse gauge links and boundary terms
instantaneous-fermion and instantaneous-gluon interactions
zero modes and constrained fields
sector-dependent counterterms
finite-basis to continuum distributional limits
```

Classify every source as:

```text
PARTONIC_PROBE_AUTHORITY
LIGHT_FRONT_FOCK_NORMALIZATION_AUTHORITY
LIGHT_FRONT_PERTURBATION_AUTHORITY
SPACELIKE_WILSON_INSERTION_AUTHORITY
INSTANTANEOUS_TERM_AUTHORITY
ZERO_MODE_BOUNDARY_AUTHORITY
FINITE_BASIS_COUNTERTERM_AUTHORITY
DISCRETE_DISTRIBUTION_LIMIT_AUTHORITY
METHOD_ONLY
NOT_REGULATOR_IDENTICAL
```

Every new formula, matrix, or generated array must record:

```text
derivation ID
source assumptions
external-state identity
color
spin
basis resolution
IR regulator
spacelike direction
path
measure
normalization
counterterm convention
perturbative order
symbolic hash
generated-code hash
independent check
```

Create:

```text
docs/next_level/c38_primary_source_manifest.json
docs/next_level/c38_derivation_authority_manifest.json
```

---

# 8. Immutable C37 baseline

Before edits, reproduce and record:

```text
resolved full C37 completion commit
fixed C36 spacelike scheme
C37 validator and dedicated tests passing
C35/C36 validators passing
C33-C36 focused suite: 98 passed
2,840 C37 semantic injections
deterministic C37 manifests

C37 outcome:
    C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE

missing prerequisites:
    regulator-identical Wilson insertion
    common-IR partonic probes
    instantaneous/boundary/zero-mode/counterterm sector
    distributional x map
    basis trajectory

matching:
    no coefficient
    no state-independent kernel

exports:
    no microscopic proton TMD
    no bridge comparison

integrity:
    all 642 ART25 identities unchanged
    NO_JOINT_MEASURE
    216 production routes
    eight authoritative artifacts
    MSHT20_REP outside Git
```

Do not proceed if the baseline fails.

C38 must not modify:

- C11-C37 roots or historical no-go results;
- the fixed C36 spacelike scheme;
- the exact C36 tree reduction;
- the C35 finite-delta Ward defect;
- frozen bridge roles, holdouts, ancestry, or `NO_JOINT_MEASURE`;
- ART25;
- production or authoritative artifacts.

Create only versioned C38 descendants.

---

# 9. Required C38 architecture

Implement or extend immutable objects equivalent to:

```text
PartonicProbeRootId
PartonicProbePlan
PartonicProbeResolution

FundamentalColorState
PartonicOneQuarkState
PartonicQuarkGluonState
PartonicProbeWavePacket
PartonicProbeComparisonMap

PartonicIRPlan
OffShellProbe
MassRegulatedProbe
AnalyticIRProbe
IRPlanSelection

FiniteBasisSpacelikePath
FiniteBasisWilsonInsertion
LongitudinalWilsonInsertion
TransverseWilsonInsertion
WilsonEmissionVertex
WilsonVirtualKernel

PartonicFreeHamiltonian
PartonicInteractionHamiltonian
PartonicInstantaneousFermion
PartonicInstantaneousGluon
PartonicConstraintSector
PartonicZeroModeSector
PartonicBoundarySector

PartonicMassCounterterm
PartonicFieldCounterterm
PartonicVertexCounterterm
PartonicOperatorCounterterm
PartonicWilsonCounterterm
PartonicBasisCounterterm
PartonicCountertermSystem

DiscreteLongitudinalSupport
DiscreteDistributionFunctional
BasisTestFunction
BasisPlusDistribution
BasisDeltaEndpoint
BasisConvolution
DistributionRefinementMap

PartonicResolutionSequence
FactorizedBasisGrid
PartonicTrajectoryReport

SoftInterfacePrerequisite
C39CalculationPrerequisite
C38CapabilityMatrix
C38ClosureReport
```

Every object must be:

- immutable;
- content addressed;
- deterministic;
- explicit about probe versus hadron ownership;
- explicit about color and spin;
- explicit about basis and IR regulator;
- explicit about Wilson path and finite rapidity;
- explicit about counterterms;
- explicit about distributional action;
- independent of ART25;
- unreachable from inference and production.

---

# 10. Create a distinct partonic probe root

The partonic matching probe must not descend from the proton state as a physical-state member.

Create:

```text
C38_FINITE_BASIS_PARTONIC_PROBE_ROOT
```

with scope:

```text
MATCHING_PROBE_ONLY
COLOR_FUNDAMENTAL
NO_HADRON_IDENTITY
NO_PROBABILITY_INTERPRETATION
```

At minimum support:

\[
\mathcal H_{\rm probe}^{(0)}
=
\operatorname{span}\{|q\rangle\},
\]

and at one-loop support:

\[
\mathcal H_{\rm probe}^{(1)}
=
\operatorname{span}\{|q\rangle,|qg\rangle\}.
\]

Every state retains:

```text
flavor
fundamental color
helicity
longitudinal mode
transverse basis mode
orbital label
external momentum label
IR-regulator identity
resolution
normalization
```

The root is color fundamental, not color singlet.

Create:

```text
docs/next_level/c38_partonic_probe_root.json
docs/next_level/c38_partonic_probe_scope.json
```

---

# 11. Select the external-probe representation

Compile mutually exclusive probe plans:

## 11.1 `M0A-EXACT-MODE-PROBE`

Use normalized discrete one-particle basis modes as the matching probes.

## 11.2 `M0A-PROJECTED-WAVEPACKET`

Use normalized wave packets with declared momentum means and widths, projected into the finite basis.

## 11.3 `M0A-HYBRID-MODE-WAVEPACKET`

Use exact modes as the primary regulator authority and wave packets as independent external-momentum checks.

## 11.4 `M0A-UNAVAILABLE`

No state with controlled normalization and common-IR identity can be constructed.

Select one primary plan before evaluating a Wilson matrix element.

A wave packet may not be tuned to reproduce the continuum result.

Create:

```text
docs/next_level/c38_probe_plan_manifest.json
docs/next_level/c38_probe_plan_selection.json
```

---

# 12. Select one common IR prescription

Compile mutually exclusive common-IR plans:

```text
M0A-IR-OFFSHELL
M0A-IR-MASS
M0A-IR-ANALYTIC
M0A-IR-UNAVAILABLE
```

The selected plan must be implementable on both:

```text
the continuum selected-scheme oracle;
the finite-basis partonic probe.
```

For an off-shell plan, define precisely how the finite-basis probe realizes:

\[
p^2<0
\]

without treating a non-eigenstate as an exact asymptotic hadron.

For a mass plan, distinguish the IR mass from the Hamiltonian renormalized quark mass and preserve the regulator-removal order.

For an analytic regulator, define its action on both real and virtual terms.

Required records:

```text
external momenta
external helicities
color normalization
IR values
removal order
continuum map
finite-basis map
holdouts
```

Create:

```text
docs/next_level/c38_common_ir_plan.json
docs/next_level/c38_common_ir_realization_report.json
```

If no common IR plan closes, C38 must fail before one-loop operator construction.

---

# 13. Materialize one-quark states

Construct normalized one-quark states in the selected finite light-front basis.

Record:

```text
K or longitudinal momentum unit
positive half-integer or selected boundary convention
Nmax
bHO
radial and azimuthal oscillator labels
helicity
fundamental color
flavor
center-of-mass policy
external momentum or wave-packet map
```

Required checks:

- exact normalization;
- orthogonality;
- color metric;
- helicity metric;
- longitudinal momentum reconstruction;
- free invariant mass;
- comparison map across resolutions;
- charge conjugation to the antiquark probe;
- no color-singlet projection.

Create:

```text
docs/next_level/c38_one_quark_state_manifest.json
docs/next_level/c38_one_quark_normalization_report.json
```

---

# 14. Materialize the qg sector

Construct the one-quark–one-gluon sector needed for real emission and virtual intermediate states.

Every qg state retains:

```text
quark longitudinal and transverse modes
gluon longitudinal and transverse modes
quark helicity
gluon helicity/polarization
fundamental color and adjoint color
total momentum
orbital labels
fermion sign
zero-mode status
resolution
```

Use the complete color action:

\[
t^a_{c'c}.
\]

The qg sector must not use the baryonic color-singlet nullspace.

Required checks:

- total momentum conservation;
- free invariant mass;
- orthonormality;
- quark/gluon exchange and statistics status;
- comparison maps;
- matrix-free versus assembled free action;
- correct zero-mode exclusion or explicit control.

Create:

```text
docs/next_level/c38_quark_gluon_state_manifest.json
docs/next_level/c38_qg_normalization_report.json
```

---

# 15. Define the partonic free and interaction Hamiltonians

Create a dedicated matching-probe Hamiltonian root, distinct from the C8-C14 hadronic Hamiltonian.

At the declared order retain:

```text
free quark term
free gluon term
canonical q<->qg vertex
generated adjoint
instantaneous-fermion partner
instantaneous-gluon partner
mass counterterm
field counterterm
vertex counterterm
basis/regulator term
```

Use C9 as a methodological ancestor only where operator and normalization identities agree.

Required checks:

- Hermiticity;
- color action;
- helicity selection;
- longitudinal conservation;
- matrix-free/assembled equality;
- Ward or commuting-generator pilot;
- every omitted term has a typed status.

Create:

```text
docs/next_level/c38_partonic_hamiltonian_manifest.json
docs/next_level/c38_partonic_hamiltonian_validation.json
```

---

# 16. Materialize the spacelike Wilson insertion

Implement the exact C36 selected spacelike path in the finite basis.

The operator record must retain:

```text
spacelike direction v
v^2<0
finite-rapidity invariant
future/past orientation
longitudinal path
transverse closure
endpoint identities
path ordering
anti-path ordering
fundamental/anti-fundamental action
Fourier convention
```

Expand the insertion at the order needed for the next calculation.

At first order construct:

\[
W_v^{(1)}
=
ig\int ds\,v\cdot A^a(x+sv)\,t^a.
\]

Materialize its matrix element between:

```text
|q>
and
|qg>
```

using the actual finite-basis mode functions and measures.

The Wilson insertion must not be represented only by a continuum eikonal denominator or by metadata.

Create:

```text
docs/next_level/c38_spacelike_wilson_insertion.json
docs/next_level/c38_wilson_emission_vertex.json
docs/next_level/c38_wilson_matrix_element_report.json
```

---

# 17. Transverse closure, endpoints, and boundary sector

Implement the transverse closure and its endpoint/junction structure required by the selected source convention.

Record:

```text
finite/infinite endpoint prescription
transverse path
junctions
residual-gauge transformation
basis-boundary representation
cusp/endpoint ownership
```

Do not assume the transverse segment is unity because a convenient gauge was selected.

Required controls:

- omit transverse closure;
- reverse orientation;
- remove endpoint;
- change boundary convention;
- test gauge transformation at the declared scope.

Create:

```text
docs/next_level/c38_transverse_boundary_operator.json
docs/next_level/c38_endpoint_boundary_report.json
```

---

# 18. Instantaneous and constrained sectors

Materialize or prove non-applicability for:

```text
instantaneous fermion
instantaneous gluon
constrained gauge component
residual gauge field
contact term
boundary-induced interaction
```

These terms must be derived from the selected finite-basis light-front action/Hamiltonian.

Do not inherit the numerical C9 terms without proving normalization and operator identity.

Create:

```text
docs/next_level/c38_instantaneous_sector.json
docs/next_level/c38_constraint_sector_report.json
```

---

# 19. Zero-mode sector

The zero-mode policy must be executable rather than a string.

Audit separately:

```text
gluon k+=0
constrained fermion zero modes
transverse boundary zero modes
Wilson-line endpoint zero modes
```

Allowed statuses:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_CONSTRAINT
CANCELS_WITH_DECLARED_PARTNER
EXCLUDED_WITH_PROVED_POWER_COUNTING
UNRESOLVED_BLOCKING
```

No zero mode may be set to zero because it was absent from the historical finite basis.

Create:

```text
docs/next_level/c38_partonic_zero_mode_sector.json
docs/next_level/c38_zero_mode_decision_report.json
```

---

# 20. Counterterm architecture

Create explicit, separate counterterm records for:

```text
quark mass
quark field normalization
q<->qg vertex
instantaneous partners
bilocal operator
spacelike Wilson line
endpoint/cusp
transverse closure
basis boundary
sector-dependent truncation
```

Every counterterm must record:

```text
renormalization condition
input observables or partonic conditions
resolution dependence
UV structure
IR independence
finite-rapidity dependence
first omitted order
holdouts
```

Counterterms may not be fitted to:

```text
the proton mass
a proton TMD
ART25
the twelve bridge points
a desired continuum finite constant
```

unless the term is explicitly part of the pre-existing hadronic Hamiltonian and is kept read-only. The partonic matching counterterms must be fixed by partonic renormalization conditions.

Create:

```text
docs/next_level/c38_partonic_counterterm_system.json
docs/next_level/c38_counterterm_renormalization_conditions.json
docs/next_level/c38_counterterm_solvability_report.json
```

C38 may leave numerical counterterm values empty when the complete one-loop bare structures belong to C39. It must nevertheless make the system well posed and executable.

---

# 21. Discrete-to-distributional longitudinal map

The finite basis has discrete longitudinal fractions:

\[
x_n = \frac{k_n}{K}.
\]

Construct a regulated distribution functional rather than a point interpolant.

For a smooth test function \(\varphi(x)\), define the finite-basis action:

\[
\langle \mathcal F_K,\varphi\rangle
=
\sum_n w_{n,K}\,
F_{n,K}\,
\varphi(x_{n,K}),
\]

or the exact basis-specific generalization.

Implement typed finite-basis analogues of:

```text
delta(1-x)
regular support
plus distributions
lower-limit plus prescription
Mellin moments
convolution
```

The map must support the continuum limit without using ART25 or the twelve bridge coordinates.

Required checks:

- support \(0<x\le1\);
- partition/completeness;
- quark-number moment;
- test-function action;
- endpoint identity;
- refinement across resolutions;
- comparison to C22 analytic distribution oracles;
- no arbitrary spline.

Create:

```text
docs/next_level/c38_discrete_distribution_functional.json
docs/next_level/c38_basis_endpoint_distribution.json
docs/next_level/c38_basis_convolution_interface.json
docs/next_level/c38_distribution_refinement_report.json
```

---

# 22. Factorized basis and regulator trajectory

The inherited three C7/C11 resolution points vary several quantities together. They remain historical comparison points, not a sufficient matching trajectory.

Construct a factorized trajectory plan that varies independently where possible:

```text
K
Nmax
bHO
basis UV support
basis IR support
endpoint regulator
zero-mode cutoff
external-state IR regulator
finite-rapidity value
Wilson path length or endpoint regulator
quadrature order
```

Build explicit refinement/coarsening maps.

Require:

```text
enough points for every fitted trajectory coefficient
at least one holdout per fitted family
no energy-only convergence claim
TMD/operator-specific observables
```

Allowed statuses:

```text
PARTONIC_TRAJECTORY_READY
REFINEMENT_ONLY
DIAGONAL_HISTORICAL_POINTS_ONLY
NONIDENTIFIABLE_TRAJECTORY
TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c38_factorized_resolution_grid.json
docs/next_level/c38_refinement_map_manifest.json
docs/next_level/c38_partonic_trajectory_plan.json
docs/next_level/c38_trajectory_identifiability_report.json
```

---

# 23. Tree and first-order infrastructure tests

C38 must execute, at minimum:

## 23.1 Tree operator

- one-quark matrix element;
- exact normalization;
- correct \(\delta(1-x)\) finite-basis functional;
- future/past T-even equality;
- quark/antiquark charge conjugation.

## 23.2 Canonical q<->qg vertex

- color factor;
- helicity structure;
- momentum conservation;
- adjoint relation;
- matrix-free equality.

## 23.3 Spacelike Wilson emission vertex

- path-derived sign;
- finite-rapidity dependence;
- color action;
- transverse phase;
- endpoint behavior;
- comparison with the selected continuum eikonal numerator at common kinematics.

## 23.4 Ward/count-once pilot

- propagating plus instantaneous terms;
- boundary term;
- Wilson term;
- exact defect when any required contribution is removed.

These are infrastructure tests. They are not the complete one-loop TMD.

Create:

```text
docs/next_level/c38_tree_partonic_operator_report.json
docs/next_level/c38_qg_vertex_report.json
docs/next_level/c38_wilson_vertex_oracle_report.json
docs/next_level/c38_partonic_ward_pilot.json
```

---

# 24. Universal soft and overlap interface

Reuse the C36 universal spacelike soft root as a read-only operator authority.

C38 must define how the finite-basis collinear probe will consume:

```text
soft allocation
finite-rapidity value
transverse measurement
UV convention
overlap/zero-bin convention
common IR plan
```

Do not numerically subtract a soft factor before the C39 bare collinear result exists.

Create:

```text
docs/next_level/c38_soft_interface_prerequisite.json
docs/next_level/c38_overlap_interface_prerequisite.json
```

Allowed readiness statuses:

```text
SOFT_INTERFACE_READY
OVERLAP_TEST_READY
SOFT_CONVERSION_REQUIRED
OVERLAP_UNRESOLVED
INCOMPATIBLE
```

---

# 25. C39 calculation prerequisite gate

C38 may issue:

```text
C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY
```

only when all of the following pass:

```text
partonic probe root
probe-state plan
common IR plan
one-quark states
qg states
partonic Hamiltonian
spacelike Wilson insertion
transverse boundary operator
instantaneous/constrained sector
zero-mode decision
counterterm system
discrete distribution functional
factorized trajectory plan
soft/overlap interfaces
tree and first-order infrastructure tests
```

Create:

```text
docs/next_level/c38_c39_prerequisite_gate.json
docs/next_level/c38_capability_matrix.json
```

C38 does not issue:

```text
C37_LF_TO_SELECTED_MATCHING_VALIDATED
C38_MICROSCOPIC_PROTON_TMD_EXPORTED
BRIDGE_DISTRIBUTION_COMPARISON_READY
```

---

# 26. Tensor-network and quantum interface

Represent the partonic probe sectors separately from the hadron TTN.

The partonic network contains:

```text
probe root
q sector
qg sector
longitudinal mode
transverse/OAM mode
helicity
fundamental/adjoint color
Wilson insertion edge
instantaneous/boundary/zero-mode branches
```

It is a regulator and matching-calculation object, not the hadron variational state.

Define a future PennyLane/QTN operator contract for:

```text
one-quark preparation
qg sector-changing gates
spacelike Wilson emission
instantaneous kernels
distributional measurement
```

Do not fit or train.

Create:

```text
docs/next_level/c38_partonic_tensor_network_manifest.json
docs/next_level/c38_partonic_quantum_interface.json
```

---

# 27. Uncertainty and remainder separation

Keep separate:

```text
probe wave-packet remainder
external IR remainder
longitudinal discretization
transverse basis truncation
basis UV remainder
basis IR remainder
endpoint/boundary remainder
zero-mode remainder
instantaneous-sector remainder
Wilson-insertion truncation
counterterm-system remainder
distributional-map remainder
refinement/trajectory remainder
soft-interface remainder
overlap-interface remainder
numerical error
first omitted perturbative order
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No remainder may be absorbed into ART25 covariance, a proton normalization, or a matching coefficient not yet calculated.

Create:

```text
docs/next_level/c38_uncertainty_budget.json
docs/next_level/c38_remainder_separation.json
```

---

# 28. Scientifically valid no-go outcomes

## 28.1 Partonic probe root cannot be constructed

```text
C38_PARTONIC_PROBE_ROOT_UNAVAILABLE
```

Next:

> **C39/P0 — color-fundamental light-front matching-probe Hilbert-space construction**

## 28.2 No common IR plan closes

```text
C38_COMMON_IR_REALIZATION_UNAVAILABLE
```

Next:

> **C39/IR0 — common continuum/finite-basis partonic IR regulator construction**

## 28.3 Spacelike Wilson insertion cannot be materialized

```text
C38_SPACELIKE_WILSON_INSERTION_UNAVAILABLE
```

Next:

> **C39/W0 — finite-basis spacelike path, endpoint, and emission-vertex construction**

## 28.4 Instantaneous, boundary, or zero modes block closure

```text
C38_CONSTRAINED_SECTOR_INCOMPLETE
```

Next:

> **C39/Z2 — partonic instantaneous, zero-mode, and transverse-boundary completion**

## 28.5 Counterterm system is not well posed

```text
C38_PARTONIC_COUNTERTERM_SYSTEM_UNRESOLVED
```

Next:

> **C39/CT0 — finite-basis partonic renormalization conditions and sector-counterterm completion**

## 28.6 Distributional map does not close

```text
C38_DISCRETE_DISTRIBUTION_MAP_UNAVAILABLE
```

Next:

> **C39/X0 — finite-K distribution functional, endpoint algebra, and convolution completion**

## 28.7 Trajectory is not identifiable

```text
C38_PARTONIC_TRAJECTORY_UNRESOLVED
```

Next:

> **C39/R1A — factorized partonic basis trajectory and power-correction completion**

## 28.8 All prerequisites close

```text
C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY
```

Next:

> **C39/R2B — execute the finite-basis one-loop spacelike collinear correlator, universal soft/overlap subtraction, renormalization, and state-independent matching difference**

Every no-go must name the exact absent state, operator, term, map, condition, or trajectory.

Create:

```text
docs/next_level/c38_source_sufficiency_decision.json
docs/next_level/c38_no_go_decision_tree.json
docs/next_level/c38_missing_calculation_specification.md
```

---

# 29. Holdouts

Freeze before construction or tuning:

```text
one one-quark mode
one qg mode
one wave-packet momentum
one IR-regulator value
one quark helicity
one antiquark charge-conjugate state
one Wilson longitudinal matrix element
one transverse-boundary matrix element
one instantaneous-fermion term
one instantaneous-gluon term
one zero-mode control
one endpoint contribution
one mass-counterterm condition
one field-counterterm condition
one vertex-counterterm condition
one operator-counterterm condition
one endpoint delta functional
one plus-distribution test function
one Mellin moment
one convolution test
one K refinement point
one Nmax refinement point
one finite-rapidity point
one soft-interface decision
one ART25-independence control
```

No failed holdout may be moved into construction.

---

# 30. Required benchmark families

Implement at least:

```text
M0A-A  immutable C37 no-go and fixed C36 scheme
M0A-B  distinct color-fundamental probe root
M0A-C  common-IR plan
M0A-D  one-quark state normalization
M0A-E  qg sector normalization and free action
M0A-F  partonic Hamiltonian and instantaneous partners
M0A-G  spacelike Wilson insertion
M0A-H  transverse closure and endpoints
M0A-I  zero-mode and constrained sectors
M0A-J  counterterm architecture
M0A-K  discrete distribution functional
M0A-L  endpoint/plus/Mellin/convolution algebra
M0A-M  factorized regulator trajectory
M0A-N  tree partonic operator
M0A-O  qg and Wilson first-order vertices
M0A-P  Ward/count-once pilot
M0A-Q  soft/overlap and C39 readiness
M0A-R  deterministic isolation and no readiness leakage
```

---

# 31. Negative injections

Create at least **3,040 ordered C38 semantic fault injections** with stable IDs and deterministic diagnostics.

Include:

## Baseline and scope

- wrong C37 commit;
- C36 regulator changed;
- C37 no-go overwritten;
- probe root aliased to proton;
- color-singlet projection applied to the probe.

## Probe states

- one-quark normalization wrong;
- qg state missing color;
- external momentum not reconstructed;
- wave packet tuned to continuum result;
- antiquark copied without charge conjugation;
- probe called a physical hadron.

## Common IR

- different IR plans on the two sides;
- off-shellness not implemented in the basis;
- IR mass confused with renormalized quark mass;
- regulator-removal order omitted;
- IR value changed after holdout inspection.

## Hamiltonian

- qg vertex copied from C9 without normalization proof;
- generated adjoint omitted;
- instantaneous fermion omitted;
- instantaneous gluon omitted;
- mass counterterm omitted;
- matrix-free mismatch hidden.

## Wilson insertion

- continuum denominator substituted for a matrix element;
- spacelike direction lost;
- transverse closure omitted;
- endpoint omitted;
- path order wrong;
- anti-fundamental action wrong;
- finite-rapidity identity changed.

## Zero modes and boundaries

- historical zero-mode exclusion interpreted as zero;
- transverse boundary set to unity by gauge choice;
- constrained field omitted;
- zero-mode defect called numerical noise.

## Counterterms

- proton mass used to fix a partonic counterterm;
- ART25 used;
- desired continuum finite constant used as a fit;
- UV and IR conditions conflated;
- operator and Wilson counterterms aliased;
- underdetermined system declared solved.

## Distributional map

- twelve bridge points used as an x grid;
- arbitrary spline used;
- delta endpoint omitted;
- plus distribution replaced by cutoff;
- number moment violated;
- support outside \(0<x\le1\);
- one K point called continuum.

## Trajectory

- diagonal historical points called factorized;
- refinement map invented;
- energy convergence used;
- holdout used in fit;
- more coefficients than independent points.

## Readiness leakage

- matching kernel created before C39;
- proton TMD exported;
- bridge residual calculated;
- likelihood or p-value created;
- calibration, reweighting, or emulator created;
- process/deuteron/gluon/T-odd status promoted.

## Integrity

- ART25 identity changed;
- `NO_JOINT_MEASURE` changed;
- production registry changed;
- authoritative artifact changed;
- raw MSHT files committed;
- nondeterministic manifest.

---

# 32. Deliverables

Create at least:

```text
docs/next_level/c38_implementation_report.md
docs/next_level/c38_api.md
docs/next_level/c38_requirement_coverage.json
docs/next_level/c38_normative_source_integration.json
docs/next_level/c38_volume_xxi_partonic_probe_crosswalk.json
docs/next_level/c38_primary_source_manifest.json
docs/next_level/c38_derivation_authority_manifest.json

docs/next_level/c38_partonic_probe_root.json
docs/next_level/c38_partonic_probe_scope.json
docs/next_level/c38_probe_plan_manifest.json
docs/next_level/c38_probe_plan_selection.json

docs/next_level/c38_common_ir_plan.json
docs/next_level/c38_common_ir_realization_report.json

docs/next_level/c38_one_quark_state_manifest.json
docs/next_level/c38_one_quark_normalization_report.json
docs/next_level/c38_quark_gluon_state_manifest.json
docs/next_level/c38_qg_normalization_report.json

docs/next_level/c38_partonic_hamiltonian_manifest.json
docs/next_level/c38_partonic_hamiltonian_validation.json

docs/next_level/c38_spacelike_wilson_insertion.json
docs/next_level/c38_wilson_emission_vertex.json
docs/next_level/c38_wilson_matrix_element_report.json
docs/next_level/c38_transverse_boundary_operator.json
docs/next_level/c38_endpoint_boundary_report.json

docs/next_level/c38_instantaneous_sector.json
docs/next_level/c38_constraint_sector_report.json
docs/next_level/c38_partonic_zero_mode_sector.json
docs/next_level/c38_zero_mode_decision_report.json

docs/next_level/c38_partonic_counterterm_system.json
docs/next_level/c38_counterterm_renormalization_conditions.json
docs/next_level/c38_counterterm_solvability_report.json

docs/next_level/c38_discrete_distribution_functional.json
docs/next_level/c38_basis_endpoint_distribution.json
docs/next_level/c38_basis_convolution_interface.json
docs/next_level/c38_distribution_refinement_report.json

docs/next_level/c38_factorized_resolution_grid.json
docs/next_level/c38_refinement_map_manifest.json
docs/next_level/c38_partonic_trajectory_plan.json
docs/next_level/c38_trajectory_identifiability_report.json

docs/next_level/c38_tree_partonic_operator_report.json
docs/next_level/c38_qg_vertex_report.json
docs/next_level/c38_wilson_vertex_oracle_report.json
docs/next_level/c38_partonic_ward_pilot.json

docs/next_level/c38_soft_interface_prerequisite.json
docs/next_level/c38_overlap_interface_prerequisite.json
docs/next_level/c38_c39_prerequisite_gate.json
docs/next_level/c38_capability_matrix.json

docs/next_level/c38_partonic_tensor_network_manifest.json
docs/next_level/c38_partonic_quantum_interface.json

docs/next_level/c38_uncertainty_budget.json
docs/next_level/c38_remainder_separation.json

docs/next_level/c38_source_sufficiency_decision.json
docs/next_level/c38_no_go_decision_tree.json
docs/next_level/c38_missing_calculation_specification.md

docs/next_level/c38_holdout_report.json
docs/next_level/c38_injection_manifest.json
docs/next_level/c38_regression_report.json
docs/next_level/c38_unresolved_physics_gaps.md
```

Add ADRs for:

- matching probe versus proton-state ownership;
- common IR regulator;
- color-fundamental finite-basis root;
- one-quark/qg sector construction;
- partonic Hamiltonian ownership;
- spacelike Wilson insertion in the finite basis;
- instantaneous and constrained sectors;
- zero-mode and transverse-boundary ownership;
- partonic counterterm conditions;
- discrete distribution functional;
- factorized basis trajectory;
- exact C39 readiness and no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy basis vectors, qg matrices, Wilson-insertion matrices, distribution tables, and refinement maps may remain outside Git under content-addressed runtime directories. Commit their schemas, hashes, dimensions, mode order, and deterministic reconstruction commands.

---

# 33. Acceptance criteria

C38/M0A is complete only when:

1. The full C37 baseline commit is resolved rather than invented.
2. The complete C37 baseline reproduces.
3. The C36 spacelike regulator remains fixed.
4. The C37 no-go remains explicit.
5. A distinct matching-probe root is created.
6. The probe is color fundamental and not a proton state.
7. One probe representation is selected before matrix-element evaluation.
8. One common IR plan is selected and implemented on both sides or fails closed.
9. One-quark states are normalized and compared across resolutions.
10. qg states are normalized and carry complete color, helicity, and mode identity.
11. The dedicated partonic free Hamiltonian is explicit.
12. The canonical q<->qg vertex and adjoint are explicit.
13. Instantaneous partners receive exact statuses.
14. The spacelike Wilson path is materialized in the finite basis.
15. The Wilson matrix element is not replaced by a continuum denominator.
16. Transverse closure and endpoints are explicit.
17. Zero modes receive calculated or exact blocking statuses.
18. No historical exclusion is interpreted as a physical zero.
19. The partonic counterterm system is explicit.
20. Counterterms use partonic rather than hadronic fit conditions.
21. The counterterm system’s solvability and null directions are reported.
22. A discrete distribution functional is implemented.
23. Delta, plus, regular, Mellin, and convolution actions are explicit.
24. The twelve bridge points are not used as the x grid.
25. Distribution refinement is tested across resolutions.
26. A factorized regulator grid is created.
27. Refinement maps are explicit or fail closed.
28. No trajectory is overfit.
29. Tree partonic matrix elements close.
30. The qg canonical vertex is independently checked.
31. The Wilson first-order vertex is independently checked.
32. The Ward/count-once pilot includes all required terms at its scope.
33. The universal soft factor remains outside the hadron TTN.
34. The soft and overlap prerequisites are explicit.
35. C39 readiness is issued only after every prerequisite passes.
36. C38 creates no universal matching kernel by assumption.
37. C38 creates no microscopic proton TMD export.
38. C38 does not rerun the bridge.
39. All 642 ART25 identities remain unchanged.
40. `NO_JOINT_MEASURE`, ancestry, roles, and holdouts remain unchanged.
41. No fit, likelihood, posterior, optimization, reweighting, or emulator is created.
42. No process, deuteron, gluon, T-odd, inference, or production status is promoted.
43. Every no-go includes an exact missing-calculation specification.
44. All inherited tests, validators, builders, requirements, injections, and manifests remain passing.
45. The production registry remains exactly 216 routes.
46. All eight authoritative artifacts remain byte-identical.
47. `MSHT20_REP/` remains outside Git.
48. At least 3,040 C38 semantic fault injections produce the expected diagnostics.
49. All C38 manifests reproduce byte-for-byte.
50. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
51. A local completion commit is created and not pushed.

A rigorous prerequisite no-go is valid. Do not weaken color, common-IR, Wilson-path, zero-mode, counterterm, distributional, or trajectory identities to issue readiness.

---

# 34. Allowed and forbidden statuses

The strongest generally permitted statuses include:

```text
C38_PARTONIC_PROBE_ROOT_VALIDATED
C38_COMMON_IR_PLAN_DECIDED
C38_ONE_QUARK_SECTOR_VALIDATED
C38_QG_SECTOR_VALIDATED
C38_PARTONIC_HAMILTONIAN_AUDITED
C38_SPACELIKE_WILSON_INSERTION_AUDITED
C38_CONSTRAINED_SECTOR_AUDITED
C38_COUNTERTERM_SYSTEM_AUDITED
C38_DISCRETE_DISTRIBUTION_MAP_AUDITED
C38_PARTONIC_TRAJECTORY_AUDITED
C38_SOFT_OVERLAP_PREREQUISITES_DECIDED
C38_C39_GATE_DECIDED
C38_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when every exact gate passes:

```text
C38_COMMON_IR_REALIZATION_VALIDATED
C38_SPACELIKE_WILSON_INSERTION_VALIDATED
C38_INSTANTANEOUS_BOUNDARY_ZERO_MODE_COMPLETION_VALIDATED
C38_PARTONIC_COUNTERTERM_SYSTEM_READY
C38_DISCRETE_DISTRIBUTION_MAP_VALIDATED
C38_PARTONIC_TRAJECTORY_READY
C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY
```

The following remain forbidden:

```text
C38_LF_TO_SELECTED_MATCHING_VALIDATED
C38_MICROSCOPIC_PROTON_TMD_EXPORTED
BRIDGE_DISTRIBUTION_COMPARISON_READY
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

# 35. Final Codex response

Report:

- resolved full starting and final commits;
- test, validator, builder, evidence, atlas, requirement, injection, and fault-mode counts;
- exact primary sources and hashes;
- immutable C36 scheme and C37 no-go status;
- selected partonic probe plan;
- selected common IR plan;
- one-quark and qg sector dimensions, identities, and normalization residuals;
- partonic Hamiltonian and matrix-free residuals;
- canonical qg vertex and instantaneous-term statuses;
- spacelike Wilson-path and insertion identities;
- Wilson matrix-element residuals;
- transverse boundary, endpoint, constrained, and zero-mode statuses;
- counterterm equations, rank/null directions, and solvability;
- discrete distributional map, endpoint, Mellin, and convolution residuals;
- factorized trajectory and refinement status;
- tree, qg, Wilson, and Ward-pilot results;
- soft/overlap prerequisite status;
- C39 readiness gate;
- exact no-go and next branch where blocked;
- confirmation that no ART25 member, data, chi2, residual, bridge point, or proton-level ratio entered the work;
- confirmation that no matching kernel, microscopic proton TMD, bridge comparison, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a structural probe root, a tree-level Wilson vertex, an unsolved counterterm system, or a discrete-x interface as a completed one-loop matching calculation.
