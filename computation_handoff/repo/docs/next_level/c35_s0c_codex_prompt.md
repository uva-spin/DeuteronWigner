# C35/S0C Codex Work Package

## Title

**Gauge-complete finite-cell soft regulator, executable mode basis, Wilson-segment quantization, and targeted one-loop soft-diagram and counterterm completion**

## Authoritative baseline

Start from the local C34/S0A completion commit:

```text
6bdb44be2afc79e817f69ce0e35813da8a394db7
```

Its authoritative clean C33 baseline is:

```text
e0b34c74e8f39c9d42cf49cc598f1533d9353a7e
```

The C32 operator-completion ancestor is:

```text
0d7b94a5e86882b23a56d4c1f11900d554756a18
```

and the required C28 scientific ancestor remains:

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when these commits remain in its ancestry and the complete C34 baseline reproduces before any scientific change.

Do not use `origin/main` when the local branch is ahead of the remote.

The authoritative Volume XXI source is:

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

Read and hash-audit it. Preserve its 65 stable requirements and the C34 crosswalk semantics.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Create a local completion commit. Do not push.

---

# 1. Why C35/S0C is the exact next package

C34 reaches the rigorous fail-closed status:

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

and follows Branch G:

```text
C35/S0C — targeted unresolved soft-diagram and counterterm completion.
```

This does not mean that the one-loop soft coefficient vanishes. C34 establishes:

```text
the exact C33 B=0 root
the four-line color and pole identities
the tree result S_FB^(0)=1
the symbolic eikonal-current contract
an exact nonsingular transverse-cell phase average
the source-qualified continuum modified-delta expression
```

but the repository still lacks enough regulator information to define a unique, gauge-complete, regulator-specific finite-cell contraction.

The exact inherited soft identity is:

```text
soft plan:
    S0-FB-EIKONAL-FOCK

B=0 root:
    C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT

boundary:
    FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT

zero mode:
    EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL
    AUDIT_REQUIRED

tree:
    S_FB^(0)(b_T)=1
    C_F=4/3

one-loop convention:
    S = exp[a_s C_F S_FB^[1],bare + O(a_s^2)]

one-loop coefficient:
    NONZERO_UNKNOWN
```

The four Wilson lines remain:

| Order | Line | Representation/action | Ordering | Pole component |
|---:|---|---|---|---|
| 1 | \(S_n^\dagger(b_T)\) | conjugate fundamental | anti-path ordered | \(k^-+i\delta^-\) |
| 2 | \(S_{\bar n}(b_T)\) | fundamental | path ordered | \(k^+-i\delta^+\) |
| 3 | \(S_{\bar n}^\dagger(0)\) | conjugate fundamental | anti-path ordered | \(k^++i\delta^+\) |
| 4 | \(S_n(0)\) | fundamental | path ordered | \(k^--i\delta^-\) |

All eighteen inherited one-loop contribution classes remain:

```text
UNRESOLVED_BLOCKING.
```

C34 identifies the missing regulator definition precisely. No repository object yet supplies:

```text
complete R1-R3 cell boundaries, nodes, or weights
a map from transverse_index to a 2D kT cell
a definition of omega and its relation to k+, k-, rapidity, and kT
an on-shell relation for cuts or an off-shell virtual spectral representation
normalized mode functions, commutators, or completeness
polarization four-vectors or a gauge-complete polarization metric
a gauge-fixed B=0 action and free Hamiltonian
a BRST/Krein completion or a complete light-front instantaneous alternative
a partition of unity between n and nbar rapidity regions
parameterized finite-volume Wilson segments
the action of modified-delta damping on finite modes
an explicit constrained zero-mode sector
finite-cutoff renormalization conditions
a finite-basis-to-MSbar conversion
an unambiguous normalization of n, nbar, delta+, and delta-
```

The nominal R1-R3 descriptors also vary UV support, IR support, rapidity window, transverse extent, zero-mode scale, and cell counts simultaneously and contain no proved refinement maps. They cannot presently separate logarithmic, finite, volume, rapidity-window, transverse, endpoint, or zero-mode effects.

Therefore C35 must first complete the regulator and executable mode basis. It may calculate one-loop diagrams and counterterms only after that regulator definition closes.

---

# 2. Primary objective

Implement the chain:

```text
C33/C34 structural B=0 root
    -> one gauge-complete finite-cell realization
    -> exact light-front normalization
    -> executable real and virtual mode bases
    -> normalized cells, measures, commutators, and completeness
    -> nested refinement and factorized regulator trajectories
    -> parameterized four-line Wilson geometry
    -> modified-delta damping as an operator on finite modes
    -> gauge-complete eikonal vertices
    -> zero-mode and boundary sectors
    -> real and virtual one-loop pair kernels
    -> line, cusp, endpoint, transverse, instantaneous,
       gauge, ghost, and vacuum terms
    -> bare finite-basis soft coefficient
    -> UV and rapidity counterterms
    -> renormalized finite-basis soft function
    -> finite-basis-to-continuum conversion
    -> soft-side zero-bin object
    -> exact continuation/no-go decision
```

The primary one-loop object remains:

\[
S_{\rm FB}^{\rm bare}
=
1+a_s C_F S_{\rm FB}^{[1],\rm bare}
+\mathcal O(a_s^2).
\]

A positive coefficient is not assumed.

The package must determine rather than assume:

```text
whether a covariant finite-cell/Krein realization or a light-front
physical-polarization realization is the correct executable regulator;

whether the C33 direct eikonal-Fock plan can be made gauge complete;

whether all finite-cell singularities can be represented with normalized
cell functions and explicit subtraction;

whether the zero-mode and transverse-at-infinity sectors are necessary
for Ward and gauge closure;

whether a unique regulator-specific coefficient exists;

whether all eighteen contribution classes can be calculated or proved
non-applicable;

whether UV and rapidity counterterms are state independent;

whether a universal finite-basis-to-continuum conversion exists;

whether the soft-side object is ready for the later off-shell collinear
zero-bin comparison.
```

---

# 3. Scientific boundary

C35 is:

```text
B=0 vacuum/eikonal specific
fundamental quark soft-function specific
regulator-definition first
one-loop targeted
gauge complete
modified-delta rapidity regulated
finite-cell and mode-function explicit
real/virtual explicit
zero-mode and boundary explicit
UV and rapidity explicit
trajectory and refinement aware
state and hadron independent
validation only
non-inferential
```

C35 is not:

```text
a modification of the proton state
a microscopic proton TMD export
a completed LF-to-project matching kernel
a fitted soft coefficient
a ratio to ART25
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a process prediction
a deuteron prediction
a gluon-representation soft function
a T-odd process package
a production promotion
```

The continuum modified-delta expression is the target oracle. It is not the finite-cell answer.

The auxiliary-field representation is an alternative oracle unless exact conversion is established. It is never added to the direct result.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all C5-C35 Wilson, soft, cut, light-front, regulator, matching, bridge, formal-volume, source, API, manifest, test, ADR, and roadmap files before edits.

Continue autonomously until every applicable C35 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository source and git history;
- preserve additional source papers and ancillaries;
- select and implement one gauge-complete realization;
- derive normalized mode functions and measures;
- build explicit mode collections and refinement maps;
- define the virtual loop representation;
- parameterize the Wilson segments;
- implement modified-delta damping;
- calculate one-loop real and virtual pair kernels;
- evaluate zero-mode and boundary controls;
- solve counterterms after the bare coefficient exists;
- execute regulator trajectories and holdouts;
- rebuild deterministic manifests.

Do not:

- contact authors;
- alter C11, C32, C33, C34, ARTEMIDE, or ART25;
- use ART25 members, data, chi2, or bridge residuals;
- fit a coefficient or counterterm to proton or process observables;
- copy a continuum coefficient as the finite-basis result;
- call a target-DR scaleless graph zero in the finite regulator without calculation;
- create a microscopic proton TMD;
- rerun the twelve-point bridge;
- create inference or production routes;
- push the completion commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 5.1 Wilson, pole, cut, and overlap roots

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

## 5.2 Microscopic collinear/operator roots

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md

docs/next_level/c31_implementation_report.md
docs/next_level/c31_three_layer_identity_manifest.json
docs/next_level/c31_continuum_scheme_equivalence_matrix.json

docs/next_level/c32_implementation_report.md
docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_regulator_plan_manifest.json
docs/next_level/c32_partonic_external_state_plan.json
docs/next_level/c32_gauge_plan.json
docs/next_level/c32_rapidity_plan.json
docs/next_level/c32_zero_bin_overlap_manifest.json
```

## 5.3 Structural and audit soft roots

```text
docs/next_level/c33_implementation_report.md
docs/next_level/c33_api.md
docs/next_level/c33_vacuum_hilbert_manifest.json
docs/next_level/c33_soft_basis_manifest.json
docs/next_level/c33_soft_basis_trajectory_plan.json
docs/next_level/c33_soft_zero_mode_policy.json
docs/next_level/c33_eikonal_color_space.json
docs/next_level/c33_four_line_operator_manifest.json
docs/next_level/c33_eikonal_denominator_report.json
docs/next_level/c33_soft_diagram_ledger.json
docs/next_level/c33_soft_counterterm_ledger.json
docs/next_level/c33_soft_collinear_compatibility_report.json
docs/next_level/c33_zero_bin_interface_contract.json

docs/next_level/c34_implementation_report.md
docs/next_level/c34_api.md
docs/next_level/c34_requirement_coverage.json
docs/next_level/c34_normative_source_integration.json
docs/next_level/c34_derivation_authority_manifest.json
docs/next_level/c34_one_loop_plan.json
docs/next_level/c34_mode_quadrature_plan.json
docs/next_level/c34_trajectory_fit_plan.json
docs/next_level/c34_eikonal_current_manifest.json
docs/next_level/c34_mode_cell_integration_report.json
docs/next_level/c34_soft_diagram_results.json
docs/next_level/c34_soft_counterterm_results.json
docs/next_level/c34_continuum_soft_target.json
docs/next_level/c34_soft_basis_trajectory.json
docs/next_level/c34_soft_side_zero_bin_limit.json
docs/next_level/c34_source_sufficiency_decision.json
docs/next_level/c34_missing_calculation_specification.md
docs/next_level/c34_regression_report.json
```

## 5.4 Matching and evolution roots

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
```

## 5.5 Formal sources

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

Use actual filenames when they differ. Do not invent missing sources.

Create:

```text
docs/next_level/c35_normative_source_integration.json
docs/next_level/c35_volume_xxi_requirement_crosswalk.json
```

---

# 6. Required primary-source and derivation authority

Reuse all C31-C34 source locks. Preserve new sources under:

```text
data/raw/c35_sources/
```

with exact version and SHA-256 identity.

Audit sources relevant to:

```text
light-front gauge-field quantization
covariant-gauge finite-mode/Krein or BRST representations
light-front physical-polarization and instantaneous kernels
finite-volume gauge-field mode normalization
Wilson-loop perturbation theory with finite regulators
modified-delta Wilson-line damping
zero modes and transverse boundary links
finite-cutoff Wilson-line renormalization
```

Classify each as:

```text
GAUGE_COMPLETE_ACTION_AUTHORITY
LIGHT_FRONT_MODE_AUTHORITY
FINITE_VOLUME_MODE_AUTHORITY
MODIFIED_DELTA_OPERATOR_AUTHORITY
WILSON_SEGMENT_AUTHORITY
ZERO_MODE_AUTHORITY
FINITE_CUTOFF_RENORMALIZATION_AUTHORITY
METHOD_ONLY
NOT_OPERATOR_REGULATOR_IDENTICAL
```

Every new formula and generated array must record:

```text
derivation ID
source assumptions
gauge-complete realization
light-front convention
mode coordinate map
measure
normalization
commutator or metric
boundary conditions
Wilson segment
rapidity regulator
perturbative order
symbolic hash
generated-code hash
independent check
```

Create:

```text
docs/next_level/c35_primary_source_manifest.json
docs/next_level/c35_derivation_authority_manifest.json
```

---

# 7. Immutable C34 baseline

Before edits, reproduce and record:

```text
starting C34 commit:
    e0b34c74e8f39c9d42cf49cc598f1533d9353a7e

C34 completion:
    6bdb44be2afc79e817f69ce0e35813da8a394db7

tests:
    1,231 passed

validators:
    C28-C34 pass

C34 semantic fault injections:
    2,240

roots:
    C32 B=1 collinear
    C33 B=0 soft

plan:
    S0-FB-EIKONAL-FOCK

basis dimensions:
    3,841
    30,721
    103,681

tree:
    S_FB^(0)=1

continuum convention:
    S = exp[a_s C_F S_FB^[1],bare + O(a_s^2)]

one-loop:
    all 18 slots UNRESOLVED_BLOCKING
    coefficient NONZERO_UNKNOWN

status:
    C34_SOFT_ONE_LOOP_INCOMPLETE

Volume XXI:
    source hash 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4

integrity:
    74 immutable C33 paths byte-identical
    216 production routes
    eight authoritative artifacts
    MSHT20_REP outside Git
```

Do not proceed if the baseline does not reproduce.

C35 must not modify:

- C11;
- the C32 root or exact tree reduction;
- the C33 root, paths, basis descriptors, or tree identity;
- the C34 continuum transcription or historical fail-closed status;
- the bridge grid, roles, holdouts, ancestry, or `NO_JOINT_MEASURE`;
- ART25;
- production or authoritative artifacts.

Create versioned C35 regulator and one-loop descendants.

---

# 8. Required architecture

Implement or extend immutable objects equivalent to:

```text
GaugeCompleteSoftPlan
CovariantKreinPlan
LightFrontPhysicalPlan
GaugePlanSupersession

LightFrontConvention
NullVectorNormalization
RapidityRegulatorRescaling

SoftCoordinateChart
RealSoftCoordinateChart
VirtualSoftCoordinateChart
SoftJacobian

SoftCell
SoftCellBoundary
SoftCellShape
SoftCellMeasure
SoftCellQuadrature
SoftPartitionOfUnity
SoftRefinementMap
SoftModeCollection

SoftGaugeMode
SoftPolarizationMetric
SoftGhostMode
SoftAuxiliaryMode
SoftInstantaneousKernel
SoftFreeAction
SoftFreeHamiltonian

RealCutMeasure
VirtualLoopMeasure
VirtualContourPlan
PoleCellPartition
SingularCellSubtraction

WilsonSegmentParameterization
LongitudinalWilsonSegment
TransverseInfinitySegment
ModifiedDeltaDampingOperator
FiniteSegmentLimit

ExecutableEikonalVertex
ExecutableLinePairKernel
ExecutableSelfKernel
ExecutableCuspKernel
ExecutableBoundaryKernel

SoftZeroModeSector
SoftBoundarySector
SoftBRSTOrConstraintReport

SoftBareOneLoopResult
SoftCountertermSystem
SoftRenormalizedOneLoopResult

SoftTrajectoryFamily
SoftTrajectoryAxis
SoftTrajectoryResult

SoftSideOverlapObject
C35CapabilityMatrix
C35ClosureReport
```

Every object must be:

- immutable;
- content addressed;
- deterministic;
- explicit about gauge realization;
- explicit about coordinate chart and measure;
- explicit about mode normalization;
- explicit about path parameterization;
- explicit about singular-cell treatment;
- explicit about regulator and order;
- state and ART25 independent;
- unreachable from inference and production.

---

# 9. Select one gauge-complete realization

Compile mutually exclusive plans:

## 9.1 `S0C-COVARIANT-KREIN`

A finite-cell covariant-gauge realization with:

```text
four-vector gauge modes or an equivalent indefinite-metric completion
stored polarization metric
gauge-fixing parameter xi_g
Nakanishi-Lautrup or equivalent constraint sector
ghost sector where required
BRST/Krein or exact Ward certificate
covariant propagator projection
```

## 9.2 `S0C-LIGHT_FRONT-PHYSICAL`

A light-front physical-polarization realization with:

```text
two transverse propagating modes
declared light-front gauge
instantaneous-gluon kernel
boundary link at infinity
constrained zero modes
residual-gauge prescription
a proved map to the target covariant soft function
```

## 9.3 `S0C-AUXILIARY-EIKONAL`

An auxiliary-field primary route only when its Minkowski/light-front, lightlike-path, modified-delta, endpoint, and finite-regulator identities are proved.

## 9.4 `S0C-UNAVAILABLE`

No gauge-complete realization is supported.

Select exactly one primary plan before calculating any coefficient.

If the selected plan differs from the C34 planned covariant-\(\xi_g\) route, create an explicit versioned supersession; do not silently change the gauge plan.

Create:

```text
docs/next_level/c35_gauge_complete_plan_manifest.json
docs/next_level/c35_gauge_complete_plan_selection.json
```

---

# 10. Fix the light-front normalization authority

C35 must eliminate the inherited \(\sqrt2\) ambiguity.

Declare normalized lightlike vectors consistent with:

\[
v^\pm=\frac{v^0\pm v^3}{\sqrt2},
\qquad
n\cdot\bar n=1.
\]

Record explicitly:

```text
n^mu
nbar^mu
which scalar product is k+
which scalar product is k-
Wilson-line parameter units
rescaling law under n -> lambda n
rescaling of delta+ and delta-
eikonal numerator normalization
integration measure normalization
```

Derive the stored pole components from this normalized convention.

Required checks:

- \(n^2=\bar n^2=0\);
- \(n\cdot\bar n=1\);
- exact \(k^\pm\) reconstruction;
- line-rescaling covariance;
- regulator-rescaling covariance;
- agreement with the continuum target convention.

Create:

```text
docs/next_level/c35_light_front_convention.json
docs/next_level/c35_null_vector_regulator_rescaling.json
```

---

# 11. Define executable real and virtual coordinate charts

Real and virtual contributions require different executable representations.

## 11.1 Real on-shell chart

Define a massless on-shell map, for example:

\[
k^+
=
\frac{\kappa}{\sqrt2}e^y,
\qquad
k^-
=
\frac{\kappa}{\sqrt2}e^{-y},
\qquad
|\bm k_T|=\kappa,
\]

or another exactly derived chart.

Record:

```text
coordinate ranges
Jacobian
on-shell delta
positive-energy condition
phase-space measure
azimuthal coordinate
rapidity coordinate
IR and UV boundaries
```

## 11.2 Virtual chart

Define one primary virtual representation:

```text
direct k+,k-,kT loop quadrature with contour plan
spectral representation
Feynman-parameter representation with exact finite-cutoff map
another source-audited regulator-identical plan
```

The virtual route must retain the modified-delta denominators and finite-cell cutoff identity.

It may not be replaced by the continuum dimensional result.

Create:

```text
docs/next_level/c35_real_coordinate_chart.json
docs/next_level/c35_virtual_coordinate_chart.json
docs/next_level/c35_real_virtual_measure_report.json
```

---

# 12. Materialize normalized finite-cell modes

For every executable resolution, generate the actual mode collection.

Every cell must have:

```text
exact boundaries
coordinate chart
measure
normalized shape function
quadrature nodes
quadrature weights
mode normalization
polarization/color identity
rapidity-region ownership
zero-mode relation
content hash
```

For real modes, require:

\[
\langle g_{\lambda,C}^a
|
g_{\lambda',C'}^{a'}
\rangle
=
\delta^{aa'}
\delta_{\lambda\lambda'}
\delta_{CC'}
\]

or the exact selected indefinite-metric generalization.

Define cell functions \(\chi_C(k)\) with an explicit completeness/partition statement over the regulated domain.

The existing `implicit_mode_collection_sha256` descriptors are not mode collections and must not be reused as if they were.

Create:

```text
docs/next_level/c35_soft_mode_collection_manifest.json
docs/next_level/c35_soft_mode_normalization_report.json
docs/next_level/c35_soft_partition_of_unity_report.json
```

Store heavy mode arrays outside Git under a content-addressed runtime path.

---

# 13. Build nested refinement maps and factorized trajectories

The C33 R1-R3 descriptors are preserved but do not themselves prove nesting.

C35 must build explicit refinement/coarsening maps or declare them unavailable.

In addition to any global resolution sequence, create separately varied families for:

```text
UV extent
IR extent
rapidity window
rapidity cell size
transverse extent
transverse cell size
zero-mode cutoff
endpoint/line-length cutoff
quadrature order
```

Vary one family at a time where possible.

A trajectory cannot identify a UV logarithm while UV, IR, rapidity, and transverse support all change without a controlled factorized design.

Require enough independent points for every fitted coefficient plus at least one holdout.

Create:

```text
docs/next_level/c35_refinement_map_manifest.json
docs/next_level/c35_factorized_regulator_grid.json
docs/next_level/c35_trajectory_identifiability_report.json
```

---

# 14. Define the gauge-field action and mode metric

For the selected gauge-complete plan, store the complete free B=0 action or Hamiltonian.

The record must determine:

```text
propagating mode content
polarization metric
commutators
propagator
gauge parameter
constraint modes
ghost action/status
instantaneous kernels
vacuum normalization
boundary conditions
zero-mode constraints
```

At \(O(g^2)\), prove every `NOT_APPLICABLE` decision from the action and vertex counting.

In particular, decide explicitly whether:

```text
GHOST
AUXILIARY_FIELD_SELF_ENERGY
LIGHT_FRONT_INSTANTANEOUS
GAUGE_FIXING
SOFT_VACUUM_ENERGY
```

are nonzero, canceling, or not applicable.

Create:

```text
docs/next_level/c35_soft_free_action.json
docs/next_level/c35_soft_mode_metric.json
docs/next_level/c35_brst_constraint_or_instantaneous_report.json
```

---

# 15. Parameterize every Wilson segment

For each of the four paths, store an executable piecewise parameterization:

```text
starting point
direction
affine parameter
finite regulator length or limit prescription
modified-delta damping
transverse-at-infinity segment
orientation
path/anti-path order
endpoint/junction identity
```

The longitudinal segments and transverse closure must be explicit.

The infinite-length limit and regulator-removal order must be defined.

The line parameterization must reproduce the stored pole denominators and phases.

Create:

```text
docs/next_level/c35_wilson_segment_parameterization.json
docs/next_level/c35_transverse_infinity_segment.json
docs/next_level/c35_line_to_pole_derivation_report.json
```

---

# 16. Implement modified-delta damping on finite modes

Implement the rapidity regulator as an operator on each Wilson segment, not as metadata attached after integration.

For every mode/cell record:

```text
delta+ or delta-
line orientation
damping kernel
complex pole
conjugation
rescaling under n/nbar normalization
finite-line limit
infinite-line limit
```

Test:

- line conjugation;
- future/past reversal;
- \(\delta^+\leftrightarrow\delta^-\) relations;
- regulator-removal order;
- independence from numerical epsilon;
- convergence of finite-line to damped infinite-line expressions.

Create:

```text
docs/next_level/c35_modified_delta_operator.json
docs/next_level/c35_modified_delta_mode_action_report.json
```

---

# 17. Singular-cell and contour authority

Eikonal poles may lie within finite cells.

Define:

```text
pole-cell detection
cell splitting
principal-value treatment
delta/cut contribution
contour deformation
analytic subtraction
remainder quadrature
tolerance
maximum subdivisions
failure status
```

Center sampling is forbidden for singular cells.

Use independent analytic test integrals to verify:

\[
\frac1{x\mp i0}
=
\operatorname{PV}\frac1x
\pm i\pi\delta(x)
\]

and its modified-delta counterpart under the selected finite-cell measure.

Create:

```text
docs/next_level/c35_pole_cell_partition.json
docs/next_level/c35_singular_cell_subtraction_report.json
docs/next_level/c35_virtual_contour_report.json
```

---

# 18. Executable eikonal vertices and pair kernels

Construct the numerical one-gluon matrix elements:

\[
\langle g_{\lambda,C}^a
|
J\cdot A
|
\Omega
\rangle
\]

with exact mode normalization.

For every line pair \((\ell,m)\), build a typed kernel retaining:

```text
line identities
color contraction
representation action
orientation
transverse phase
real/virtual status
gauge contribution
rapidity regulator
cell identity
quadrature identity
```

Required checks:

- direct versus sparse/matrix-free action;
- conjugation;
- path reversal;
- color-singlet projection;
- Ward contraction;
- cell-refinement consistency;
- real/virtual measure compatibility.

Create:

```text
docs/next_level/c35_executable_eikonal_vertex.json
docs/next_level/c35_line_pair_kernel_library.json
docs/next_level/c35_vertex_ward_report.json
```

---

# 19. Complete the eighteen contribution slots

Calculate or prove non-applicability for all inherited classes:

```text
N_NBAR_EXCHANGE
CONJUGATE_LINE_EXCHANGE
SAME_DIRECTION_LINE_EXCHANGE
REAL_ONE_SOFT_GLUON
VIRTUAL_ONE_SOFT_GLUON
WILSON_LINE_SELF_ENERGY
CUSP_ENDPOINT
TRANSVERSE_CLOSURE
AUXILIARY_FIELD_SELF_ENERGY
SOFT_VACUUM_ENERGY
LIGHT_FRONT_INSTANTANEOUS
GAUGE_FIXING
GHOST
ZERO_MODE
BASIS_BOUNDARY
RAPIDITY_COUNTERTERM
UV_COUNTERTERM
RESIDUAL_LINE_MASS_COUNTERTERM
```

Allowed statuses:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_IDENTITY
CANCELS_WITH_DECLARED_PARTNER
TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO
NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF
UNRESOLVED_BLOCKING
```

Do not issue one-loop readiness while a required slot remains blocking.

Create:

```text
docs/next_level/c35_soft_diagram_results.json
docs/next_level/c35_soft_counterterm_results.json
docs/next_level/c35_contribution_closure_matrix.json
```

---

# 20. Real/virtual assembly and bare soft coefficient

Construct independent routes:

```text
direct Wilson expansion
finite-mode real/cut assembly plus virtual loop assembly
```

The assembled coefficient is:

\[
S_{\rm FB}^{[1],\rm bare}
=
S_{\rm exchange}
+
S_{\rm real}
+
S_{\rm virtual}
+
S_{\rm line}
+
S_{\rm cusp}
+
S_{\rm transverse}
+
S_{\rm inst}
+
S_{\rm zero}
+
S_{\rm boundary}
+
S_{\rm vacuum}.
\]

Retain dependence on:

```text
b_T
delta+
delta-
xi_g
resolution
UV support
IR support
rapidity support
zero-mode policy
line-length regulator
```

Required checks:

- direct versus mode-sum equality;
- real/virtual count once;
- future/past equality;
- Hermitian conjugation;
- transverse rotation;
- gauge closure;
- no physical numerical epsilon.

Create:

```text
docs/next_level/c35_real_virtual_assembly.json
docs/next_level/c35_bare_soft_coefficient.json
docs/next_level/c35_bare_soft_validation_report.json
```

---

# 21. Independently reconstruct the continuum target

C34 transcribed the source expression but did not complete an independent oracle.

C35 must reconstruct the continuum one-loop target by a second route:

```text
graph-level assembly
or
direct scalar-integral reconstruction
```

Test:

- unexpanded versus Laurent form;
- fractional \((\delta^+\delta^-)^{-\epsilon}\) cancellation;
- dependence only on \(|\delta^+\delta^-|\) after assembly;
- rapidity-log linearity;
- future/past equality;
- cusp and rapidity anomalous dimensions.

Create:

```text
docs/next_level/c35_continuum_soft_reconstruction.json
docs/next_level/c35_continuum_oracle_two_route_report.json
```

This still validates only the target continuum convention.

---

# 22. Solve UV and rapidity counterterms only after the bare result exists

Separate:

```text
linear/power Wilson-line divergence
logarithmic line divergence
cusp/endpoint divergence
transverse-junction divergence
vacuum normalization
residual line mass
soft-operator UV factor
modified-delta rapidity divergence
```

Do not tune counterterms to continuum finite constants.

Define:

\[
S_{\rm FB}^{\rm ren}
=
Z_S^{\rm UV}
R_S^{\rm rap}
S_{\rm FB}^{\rm bare}.
\]

Required checks:

- state independence;
- gauge independence;
- resolution holdout;
- rapidity-regulator cancellation;
- inverse counterterm;
- first omitted order;
- cusp consistency.

Create:

```text
docs/next_level/c35_soft_uv_counterterm_solution.json
docs/next_level/c35_soft_rapidity_counterterm_solution.json
docs/next_level/c35_soft_renormalization_closure.json
```

If the bare coefficient remains incomplete, counterterms remain empty-not-zero.

---

# 23. Finite-basis-to-continuum conversion and trajectory

Only after renormalization closes, calculate:

\[
Z_{\rm FB\to cont}^{S,[1]}
=
S_{\rm cont}^{[1],\rm ren}
-
S_{\rm FB}^{[1],\rm ren}.
\]

Separate:

```text
UV-log conversion
rapidity conversion
finite constant
IR/volume remainder
transverse discretization
zero-mode remainder
endpoint remainder
numerical remainder
```

Test:

- inverse;
- round trip;
- state and hadron independence;
- gauge independence;
- factorized regulator trajectory;
- holdout prediction.

Create:

```text
docs/next_level/c35_soft_regulator_conversion.json
docs/next_level/c35_soft_regulator_roundtrip.json
docs/next_level/c35_soft_trajectory_report.json
```

---

# 24. Zero-mode and boundary completion

The inherited zero-mode control must be made executable or remain the exact blocker.

Construct the constrained zero-mode sector appropriate to the selected gauge realization.

Audit its role in:

```text
Ward identities
line self energy
rapidity logarithms
transverse links at infinity
residual gauge transformations
finite conversion constants
```

Similarly evaluate:

```text
basis-boundary terms
cusp/endpoints
transverse-at-infinity junctions
```

Create:

```text
docs/next_level/c35_zero_mode_sector.json
docs/next_level/c35_zero_mode_closure_report.json
docs/next_level/c35_boundary_endpoint_report.json
```

---

# 25. Soft-side zero-bin and C32 continuation contract

C35 does not calculate the full C32 collinear one-loop correlator.

Construct an executable:

```text
SOFT_LIMIT_C35
```

with the exact soft measurement and a typed relation to the frozen C32 off-shell IR plan.

Do not claim off-shell soft/zero-bin equality from citation alone.

Allowed statuses:

```text
SOFT_SIDE_ZERO_BIN_OBJECT_READY
SOFT_COLLINEAR_EXACT_CONVERSION_READY
SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST
SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED
SOFT_COLLINEAR_INCOMPATIBLE
```

Create:

```text
docs/next_level/c35_soft_side_zero_bin_limit.json
docs/next_level/c35_soft_collinear_continuation_contract.json
docs/next_level/c35_c32_continuation_gate.json
```

A true continuation gate authorizes only the next collinear calculation. It does not export a proton TMD.

---

# 26. Tensor-network and quantum interface

Materialize the soft tensor-network representation only after the mode basis exists.

Retain:

```text
vacuum root
mode-cell index
rapidity region
polarization or metric index
adjoint color
four eikonal color legs
real/virtual branch
zero-mode/boundary branch
singlet trace
```

Compare full contraction with sparse/matrix-free one-loop assembly.

Bond dimension remains a numerical/truncation axis, not a statistical member.

Update the future PennyLane/QTN interface contract. Do not train or fit.

Create:

```text
docs/next_level/c35_soft_tensor_network_execution.json
docs/next_level/c35_soft_quantum_interface_update.json
```

---

# 27. Uncertainty and remainder separation

Keep separate:

```text
first omitted perturbative order
gauge-realization remainder
mode-basis completeness remainder
real-cell quadrature remainder
virtual-contour remainder
singular-cell subtraction remainder
UV-counterterm remainder
rapidity-counterterm remainder
finite-volume/IR remainder
rapidity-window remainder
transverse-discretization remainder
zero-mode remainder
boundary/cusp/transverse remainder
line-length remainder
finite-basis-to-continuum conversion remainder
soft-collinear compatibility remainder
numerical precision
```

Unknown remains:

```text
NONZERO_UNKNOWN.
```

No remainder may be absorbed into ART25 covariance, the proton state, or a fitted normalization.

Create:

```text
docs/next_level/c35_soft_uncertainty_budget.json
docs/next_level/c35_soft_remainder_separation.json
```

---

# 28. Scientifically valid no-go outcomes

C35 must support rigorous negative results.

## 28.1 No gauge-complete direct realization

```text
C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
```

Next branch:

> **C36/S2 — auxiliary-eikonal soft-root validation and conversion**

or, when neither route closes:

> **C36/O4 — new regulator architecture for the microscopic soft root**

## 28.2 Mode-basis obstruction

```text
C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
```

Next branch:

> **C36/S0D — finite-cell mode-function, measure, and completeness construction**

## 28.3 Zero-mode obstruction

```text
C35_SOFT_ZERO_MODE_COMPLETION_REQUIRED
```

Next branch:

> **C36/Z0 — constrained soft zero-mode and transverse-boundary sector**

## 28.4 Diagram incompleteness

```text
C35_SOFT_ONE_LOOP_STILL_INCOMPLETE
```

Next branch:

> **C36/S0E — targeted remaining one-loop graph and counterterm closure**

## 28.5 Rapidity/gauge obstruction

```text
C35_SOFT_RAPIDITY_OR_GAUGE_CLOSURE_FAILED
```

Next branch:

> **C36/S0B — modified-delta rapidity and gauge-closure completion**

## 28.6 Trajectory obstruction

```text
C35_SOFT_TRAJECTORY_UNRESOLVED
```

Next branch:

> **C36/S1 — factorized continuum trajectory and power-correction completion**

Every no-go result must state the exact missing calculation.

Create:

```text
docs/next_level/c35_source_sufficiency_decision.json
docs/next_level/c35_no_go_decision_tree.json
docs/next_level/c35_missing_calculation_specification.md
```

---

# 29. Holdouts

Freeze holdouts before plan selection, basis tuning, counterterm solution, or trajectory fitting.

Reserve at least:

```text
one gauge parameter
one unphysical/constraint-mode contribution
one ghost/non-applicability proof
one real mode cell
one virtual contour point
one singular pole cell
one line-pair coefficient
one same-direction coefficient
one Wilson self-energy coefficient
one cusp/endpoint coefficient
one transverse-junction coefficient
one zero-mode contribution
one basis-boundary contribution
one delta+ variation
one delta- variation
one diagonal delta+/delta- variation
one b point
one b-to-zero controlled limit
one UV-support point
one IR-support point
one rapidity-window point
one transverse-refinement point
one continuum-oracle coefficient
one counterterm coefficient
one regulator-conversion round trip
one soft-side zero-bin point
one ART25-independence control
```

No failed holdout may be moved into construction or fitting.

---

# 30. Required benchmark families

Implement at least:

## S0C-A: baseline and immutable two-root identity

## S0C-B: gauge-complete plan selection

## S0C-C: light-front normalization and regulator rescaling

## S0C-D: real/virtual coordinate charts and measures

## S0C-E: executable mode collection and completeness

## S0C-F: refinement maps and factorized trajectories

## S0C-G: gauge action, metric, ghosts, and instantaneous sector

## S0C-H: Wilson-segment parameterization

## S0C-I: modified-delta finite-mode action

## S0C-J: singular-cell and contour treatment

## S0C-K: executable eikonal vertices and Ward closure

## S0C-L: complete line-pair and self kernels

## S0C-M: real/virtual count-once assembly

## S0C-N: independent continuum oracle reconstruction

## S0C-O: UV and rapidity counterterms

## S0C-P: zero-mode, boundary, and trajectory closure

## S0C-Q: soft-side zero-bin and continuation decision

## S0C-R: deterministic isolation and no readiness leakage

---

# 31. Negative injections

Create at least **2,440 ordered C35 semantic fault injections** with stable IDs and deterministic diagnostics.

Include:

## Baseline and provenance

- wrong C34 baseline;
- C34 report absent;
- Volume XXI hash changed;
- C33/C34 historical record overwritten;
- B=0 state inserted into proton normalization.

## Gauge realization

- physical transverse modes used for covariant xi scan without completion;
- indefinite metric omitted;
- constraint mode omitted;
- ghost omitted without proof;
- instantaneous kernel omitted;
- residual gauge prescription omitted;
- gauge plan changed after residual inspection.

## Light-front convention

- \(n\cdot\bar n\neq1\);
- k+ and k- swapped;
- missing \(\sqrt2\);
- delta regulator not rescaled with n/nbar;
- eikonal numerator normalization inconsistent.

## Mode basis

- descriptor hash treated as a mode collection;
- cell boundaries omitted;
- weights omitted;
- shape functions unnormalized;
- commutator wrong;
- polarization metric wrong;
- n/nbar regions overlap without partition;
- refinement map invented;
- one resolution called complete.

## Real and virtual measures

- real mode taken off shell;
- virtual mode forced on shell;
- phase-space Jacobian wrong;
- contour omitted;
- pole crossing hidden;
- center sampling of singular cell;
- numerical epsilon stored as support.

## Wilson segments

- line length undefined;
- transverse closure omitted;
- endpoint omitted;
- modified-delta damping applied after integration;
- wrong path order;
- wrong conjugation;
- wrong basepoint.

## One-loop diagrams

- any of the eighteen slots silently zeroed;
- target-DR scaleless result copied to finite regulator;
- real or virtual term omitted;
- line self energy omitted;
- cusp or boundary term merged without identity;
- vacuum term omitted;
- zero mode omitted;
- counterterm solved before bare coefficient.

## Counterterms and trajectory

- power divergence hidden in log;
- finite constant tuned to continuum;
- underdetermined three-point fit;
- holdout used in fit;
- multiple regulator axes varied and interpreted as one coefficient;
- first omitted order set to zero.

## Soft-collinear interface

- off-shell zero-bin equality claimed from citation;
- different measurement accepted;
- different b convention accepted;
- valid soft sector called complete TMD;
- C32 collinear coefficient fabricated.

## Scope leakage

- ART25 member or data used;
- proton TMD exported;
- bridge rerun;
- likelihood or p-value produced;
- calibration or reweighting;
- process/deuteron/gluon/T-odd promotion;
- production mutation;
- raw MSHT files committed;
- nondeterministic manifest.

---

# 32. Deliverables

Create at least:

```text
docs/next_level/c35_implementation_report.md
docs/next_level/c35_api.md
docs/next_level/c35_requirement_coverage.json
docs/next_level/c35_normative_source_integration.json
docs/next_level/c35_volume_xxi_requirement_crosswalk.json
docs/next_level/c35_primary_source_manifest.json
docs/next_level/c35_derivation_authority_manifest.json

docs/next_level/c35_gauge_complete_plan_manifest.json
docs/next_level/c35_gauge_complete_plan_selection.json
docs/next_level/c35_light_front_convention.json
docs/next_level/c35_null_vector_regulator_rescaling.json

docs/next_level/c35_real_coordinate_chart.json
docs/next_level/c35_virtual_coordinate_chart.json
docs/next_level/c35_real_virtual_measure_report.json

docs/next_level/c35_soft_mode_collection_manifest.json
docs/next_level/c35_soft_mode_normalization_report.json
docs/next_level/c35_soft_partition_of_unity_report.json
docs/next_level/c35_refinement_map_manifest.json
docs/next_level/c35_factorized_regulator_grid.json
docs/next_level/c35_trajectory_identifiability_report.json

docs/next_level/c35_soft_free_action.json
docs/next_level/c35_soft_mode_metric.json
docs/next_level/c35_brst_constraint_or_instantaneous_report.json

docs/next_level/c35_wilson_segment_parameterization.json
docs/next_level/c35_transverse_infinity_segment.json
docs/next_level/c35_line_to_pole_derivation_report.json

docs/next_level/c35_modified_delta_operator.json
docs/next_level/c35_modified_delta_mode_action_report.json
docs/next_level/c35_pole_cell_partition.json
docs/next_level/c35_singular_cell_subtraction_report.json
docs/next_level/c35_virtual_contour_report.json

docs/next_level/c35_executable_eikonal_vertex.json
docs/next_level/c35_line_pair_kernel_library.json
docs/next_level/c35_vertex_ward_report.json

docs/next_level/c35_soft_diagram_results.json
docs/next_level/c35_soft_counterterm_results.json
docs/next_level/c35_contribution_closure_matrix.json

docs/next_level/c35_real_virtual_assembly.json
docs/next_level/c35_bare_soft_coefficient.json
docs/next_level/c35_bare_soft_validation_report.json

docs/next_level/c35_continuum_soft_reconstruction.json
docs/next_level/c35_continuum_oracle_two_route_report.json

docs/next_level/c35_soft_uv_counterterm_solution.json
docs/next_level/c35_soft_rapidity_counterterm_solution.json
docs/next_level/c35_soft_renormalization_closure.json

docs/next_level/c35_soft_regulator_conversion.json
docs/next_level/c35_soft_regulator_roundtrip.json
docs/next_level/c35_soft_trajectory_report.json

docs/next_level/c35_zero_mode_sector.json
docs/next_level/c35_zero_mode_closure_report.json
docs/next_level/c35_boundary_endpoint_report.json

docs/next_level/c35_soft_side_zero_bin_limit.json
docs/next_level/c35_soft_collinear_continuation_contract.json
docs/next_level/c35_c32_continuation_gate.json

docs/next_level/c35_soft_tensor_network_execution.json
docs/next_level/c35_soft_quantum_interface_update.json

docs/next_level/c35_soft_uncertainty_budget.json
docs/next_level/c35_soft_remainder_separation.json
docs/next_level/c35_source_sufficiency_decision.json
docs/next_level/c35_no_go_decision_tree.json
docs/next_level/c35_missing_calculation_specification.md

docs/next_level/c35_holdout_report.json
docs/next_level/c35_injection_manifest.json
docs/next_level/c35_regression_report.json
docs/next_level/c35_unresolved_physics_gaps.md
```

Add ADRs for:

- gauge-complete direct-soft realization;
- light-front normalization and \(\sqrt2\) authority;
- real versus virtual mode charts;
- finite-cell normalization and completeness;
- refinement and factorized trajectories;
- Wilson-segment parameterization;
- modified-delta operator action;
- singular-cell and contour treatment;
- zero-mode and boundary ownership;
- counterterm solution ordering;
- soft-side zero-bin readiness;
- exact no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy mode collections, matrices, quadrature arrays, contour data, and tensor-network tensors may remain outside Git under content-addressed runtime directories. Commit their schemas, hashes, dimensions, coordinate order, and deterministic reconstruction commands.

---

# 33. Acceptance criteria

C35/S0C is complete only when:

1. The exact C34 baseline reproduces before edits.
2. The C32/C33/C34 roots and historical results remain immutable.
3. Volume XXI retains its exact source hash and meaning.
4. One gauge-complete realization is selected before results.
5. Any gauge-plan change is a typed supersession.
6. Light-front normalization and \(\sqrt2\) conventions are explicit.
7. The rescaling of \(n,\bar n,\delta^\pm\) is explicit.
8. Real and virtual coordinate charts are executable.
9. Their measures and Jacobians are validated.
10. Complete mode collections are materialized.
11. Cell functions and normalizations are explicit.
12. A partition of unity or exact regulated completeness statement is tested.
13. Refinement maps are explicit or fail closed.
14. Regulator trajectories vary identifiable axes.
15. No underdetermined trajectory fit is performed.
16. The gauge-field action/Hamiltonian is complete at the declared scope.
17. Every ghost, constraint, and instantaneous contribution receives a proof-backed status.
18. Every Wilson segment is parameterized.
19. Modified-delta damping acts on finite modes.
20. Singular pole cells are treated analytically or by validated subtraction.
21. The numerical eikonal vertex is executable.
22. Ward closure is tested at the finite regulator.
23. Every one-loop contribution receives a calculated or proved status.
24. No finite-regulator graph is called scaleless by continuum analogy alone.
25. Real and virtual terms are counted once.
26. A bare soft coefficient is reported only from a complete required ledger.
27. The continuum target is independently reconstructed.
28. UV counterterms are solved only after the bare structure exists.
29. Rapidity counterterms are solved only after bare rapidity dependence exists.
30. Gauge independence is demonstrated when claimed.
31. Cusp consistency is tested when claimed.
32. Zero modes remain explicit.
33. Endpoint, cusp, and transverse closure remain separately auditable.
34. Finite-basis-to-continuum conversion is state, hadron, and ART25 independent.
35. The soft-side zero-bin object is explicit.
36. Off-shell soft/zero-bin equality is not assumed.
37. A valid soft result is not called a complete microscopic TMD.
38. No microscopic proton export is created.
39. The twelve-point bridge is not rerun.
40. All 642 ART25 identities remain unchanged.
41. `NO_JOINT_MEASURE`, ancestry, roles, and holdouts remain unchanged.
42. No fit, likelihood, posterior, optimization, reweighting, or emulator is created.
43. No process, deuteron, gluon, T-odd, inference, or production status is promoted.
44. Every no-go result contains an exact missing-calculation specification.
45. All inherited tests, builders, validators, requirements, injections, and manifests remain passing.
46. The production registry remains exactly 216 routes.
47. All eight authoritative artifacts remain byte-identical.
48. `MSHT20_REP/` remains outside Git.
49. At least 2,440 C35 semantic fault injections produce the expected diagnostics.
50. All C35 manifests reproduce byte-for-byte.
51. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
52. A local completion commit is created and not pushed.

A rigorous regulator-definition or one-loop no-go result is valid. Do not weaken the regulator to obtain a coefficient.

---

# 34. Outcome branches

## Branch A: regulator and one-loop soft sector close

When:

```text
C35_GAUGE_COMPLETE_SOFT_REGULATOR_VALIDATED
C35_EXECUTABLE_SOFT_MODE_BASIS_VALIDATED
C35_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED
C35_SOFT_UV_RENORMALIZATION_VALIDATED
C35_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C35_SOFT_SIDE_ZERO_BIN_OBJECT_READY
```

the exact next package is:

> **C36/R0B — microscopic one-loop collinear correlator, operator-identical zero-bin comparison, UV/rapidity combination, and LF-to-project matching closure**

## Branch B: regulator closes but diagrams remain

> **C36/S0E — targeted remaining one-loop soft graphs and counterterms**

## Branch C: mode basis does not close

> **C36/S0D — finite-cell mode-function, measure, and completeness construction**

## Branch D: zero modes block closure

> **C36/Z0 — constrained soft zero-mode and transverse-boundary sector**

## Branch E: direct gauge-complete route is unavailable but auxiliary route is viable

> **C36/S2 — auxiliary-eikonal soft-root validation and conversion**

## Branch F: trajectory remains unresolved

> **C36/S1 — factorized soft continuum trajectory and power-correction completion**

## Branch G: no compatible soft regulator exists

> **C36/O4 — replacement regulator architecture for the microscopic TMD soft root**

No branch automatically authorizes fitting or inference.

---

# 35. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C35_GAUGE_COMPLETE_PLAN_DECIDED
C35_LIGHT_FRONT_NORMALIZATION_VALIDATED
C35_REAL_VIRTUAL_MEASURES_VALIDATED
C35_EXECUTABLE_MODE_COLLECTION_AUDITED
C35_WILSON_SEGMENT_PARAMETERIZATION_VALIDATED
C35_MODIFIED_DELTA_MODE_ACTION_VALIDATED
C35_SINGULAR_CELL_TREATMENT_VALIDATED
C35_ONE_LOOP_CONTRIBUTION_MATRIX_COMPLETE
C35_CONTINUUM_ORACLE_TWO_ROUTE_VALIDATED
C35_SOFT_SIDE_ZERO_BIN_OBJECT_DEFINED
C35_C32_CONTINUATION_GATE_DECIDED
C35_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when all exact gates pass:

```text
C35_GAUGE_COMPLETE_SOFT_REGULATOR_VALIDATED
C35_EXECUTABLE_SOFT_MODE_BASIS_VALIDATED
C35_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED
C35_SOFT_UV_RENORMALIZATION_VALIDATED
C35_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C35_SOFT_REGULATOR_CONVERSION_VALIDATED
C35_SOFT_TRAJECTORY_RESOLVED
C35_SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST
C35_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING
```

The following remain forbidden:

```text
C35_MICROSCOPIC_PROTON_TMD_EXPORTED
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

# 36. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, injection, and fault-mode counts;
- exact gauge-complete realization and supersession status;
- light-front and null-vector normalization;
- real and virtual coordinate charts and measures;
- mode collection dimensions, hashes, normalization, and completeness;
- refinement maps and factorized regulator grid;
- free action/Hamiltonian, polarization metric, ghost, constraint, and instantaneous statuses;
- Wilson-segment parameterizations;
- modified-delta finite-mode action;
- singular-cell and contour treatment;
- executable eikonal-vertex and Ward residuals;
- all eighteen contribution statuses;
- real/virtual count-once residuals;
- bare coefficient values or exact blocking status;
- independent continuum-oracle residuals;
- UV and rapidity counterterm results or exact unavailability;
- gauge and cusp-consistency residuals;
- zero-mode and boundary results;
- finite-basis-to-continuum conversion and trajectory status;
- soft-side zero-bin and C32 continuation status;
- exact no-go and exact next branch;
- confirmation that no ART25 object or proton residual entered the calculation;
- confirmation that no microscopic TMD export, bridge rerun, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a structural regulator plan, a continuum target, or an incomplete mode basis as a completed one-loop finite-basis soft function.
