# C35/S0C typed API

## Purpose and scientific boundary

The package `deuteron_wigner.bridge.s0c` is the typed, content-addressed C35
regulator-completion layer for the distinct baryon-number-zero soft root.  It
does **not** implement a finite-basis one-loop soft coefficient.  Its default
and only source-supported selection is `S0C-UNAVAILABLE`, with Branch G and
the exact continuation `C36/O4 — replacement regulator architecture for the
microscopic TMD soft root`.

The API makes the negative result executable: an unavailable gauge-complete,
regulator-identical realization cannot be converted into a coefficient,
counterterm, renormalized soft factor, collinear export, bridge result,
inference object, or production route.  Exact convention and geometric
oracles remain usable, but their types and status strings prevent them from
being confused with an executable gauge-mode basis.

Authoritative implementation:

- `src/deuteron_wigner/bridge/s0c/` (formal typed public surface);
- `src/deuteron_wigner/bridge/s0c/core.py` (compatibility, analytic-oracle,
  manifest, and injection helpers);
- `scripts/build_c35_manifests.py`
- baseline commit `6bdb44be2afc79e817f69ce0e35813da8a394db7`
- prompt SHA-256
  `1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9`
- Volume XXI SHA-256
  `613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4`
- modified-delta source SHA-256
  `dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d`

## Package layers and import discipline

The package intentionally has two distinguishable layers:

1. `deuteron_wigner.bridge.s0c` exports the formal architecture records from
   `identity.py`, `conventions.py`, `basis.py`, `gauge.py`, `wilson.py`,
   `sectors.py`, `renormalization.py`, `trajectory.py`, and `overlap.py`.
   These records use explicit `C35IdentityEnvelope`, `ProofSet`, availability,
   and validation fields.  `FORMAL_ARCHITECTURE_TYPES` is the authoritative
   inventory.
2. `deuteron_wigner.bridge.s0c.core` retains compact compatibility records,
   executable analytic oracles, manifest construction helpers, and injection
   generators.  It is available explicitly as `s0c.core`; its same-named
   compact records do not shadow the formal package exports.

Code must not mix a formal record and a compact `core` record merely because
their class names match.  Cross-layer movement occurs only through the
deterministic manifests and explicit identities validated by the C35 tests.

## Immutable identities and statuses

The compact `core` module exports the ancestry and scope constants
`C35_BASELINE_COMMIT`, `C35_C33_BASELINE`, `C35_C32_ANCESTOR`,
`C35_C28_ANCESTOR`, `C35_DESCENDANT_ROOT`, and `C34_DESCENDANT_ROOT`.
The formal top-level surface exports the corresponding explicit names
`C34_STARTING_COMMIT`, `C32_OPERATOR_COMPLETION_COMMIT`, and
`C28_SCIENTIFIC_ANCESTOR` in addition to the shared root and baseline names.
The decisive status constants are:

```text
C35_PRIMARY_NO_GO       = C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
C35_SECONDARY_MODE_NO_GO = C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
C35_OUTCOME_BRANCH      = G
NONZERO_UNKNOWN         = NONZERO_UNKNOWN
EMPTY_NOT_ZERO          = EMPTY_NOT_ZERO
```

`EMPTY_NOT_ZERO` denotes an absent executable object whose value is not
asserted to vanish.  `NONZERO_UNKNOWN` is the value semantics for an
uncomputed contribution which may be nonzero.  Neither may be interpreted as
numeric zero.

## Content addressing and identity envelope

Formal public records derive from `serialization.ContentAddressed`, which
supplies `to_canonical_dict()`, `to_deterministic_json()`, and the `sha256`
property.  Each formal physics record carries an explicit
`identity: C35IdentityEnvelope` field.  `identity_for(...)` creates an
envelope without inferring convention, regulator, scale, or scheme from an
object name.  `EvidenceRef` identifies one audited assertion, while
`ProofSet` separates required, proved, and missing obligations.

The formal identity fixes the C35/C34/C33/C32/C28 roots and ancestry, `B=0`,
operator type, gauge plan, convention and chart identities, mode and Wilson
sets, UV/IR/rapidity/basis regulators, order and schemes, first omitted order,
evidence, universality, ART25 independence, and hard-false downstream
reachability.  The helper validators `require_identity`, `require_closed`,
`require_materialized`, and `validate_contribution` reject type mismatches,
positive claims with open proof sets, unavailable objects with hidden
material, and unresolved contributions carrying fabricated values.

Compact records in `core.py` derive from its internal `_ContentAddressed`
mixin.  It supplies:

- `c35_identity_envelope`: a `C35IdentityEnvelope` attached during canonical
  serialization;
- `deterministic_json`: sorted, compact, finite-number-only JSON;
- `content_hash`: SHA-256 of the deterministic JSON representation.

The compact `core.C35IdentityEnvelope` fixes, and validates at construction
time:

- C35 scope, baseline, C34 parent hashes, C33 soft root, C32 collinear root,
  and the distinct C35 `B=0` descendant root;
- the explicitly carried candidate/selected gauge plan (falling back to the
  authoritative unavailable plan only when an object has no plan field) and
  the inherited UV, IR, rapidity, and basis regulator identities;
- exact light-front and real/virtual chart identities;
- empty-not-zero mode and Wilson-segment status;
- modified-delta source identity;
- mandatory state and hadron independence, both explicitly unproved;
- hard-false ART25, process-data, bridge-residual, inference, and production
  reachability.

Construction fails if ancestry, scope, root identity, convention, chart,
source hash, universality requirement, or isolation is changed silently.
`deterministic_json(value)` and `content_hash(value)` are also available as
functions in both the formal serialization module and the compact core.  Use
the implementation belonging to the record layer being serialized.

## Formal architecture records

The top-level package exports the following typed families:

- **Identity and proof:** `AvailabilityStatus`, `ValidationStatus`,
  `ContributionStatus`, `GaugePlanKind`, `OutcomeBranch`, `EvidenceRef`,
  `ProofSet`, and `C35IdentityEnvelope`.
- **Gauge realization:** `GaugeCompleteSoftPlan`, `CovariantKreinPlan`,
  `LightFrontPhysicalPlan`, `GaugePlanSupersession`, `SoftGaugeMode`,
  `SoftPolarizationMetric`, `SoftGhostMode`, `SoftAuxiliaryMode`,
  `SoftInstantaneousKernel`, `SoftFreeAction`, `SoftFreeHamiltonian`, and
  `SoftBRSTOrConstraintReport`.
- **Conventions and charts:** `LightFrontConvention`,
  `NullVectorNormalization`, `RapidityRegulatorRescaling`,
  `SoftCoordinateChart`, `RealSoftCoordinateChart`,
  `VirtualSoftCoordinateChart`, `SoftJacobian`, `RealCutMeasure`,
  `VirtualLoopMeasure`, and `VirtualContourPlan`.
- **Basis:** `SoftCellBoundary`, `SoftCellShape`, `SoftCellMeasure`,
  `SoftCellQuadrature`, `SoftCell`, `SoftPartitionOfUnity`,
  `SoftRefinementMap`, `SoftModeCollection`, `PoleCellPartition`, and
  `SingularCellSubtraction`.
- **Wilson/operator kernels:** `WilsonSegmentParameterization`,
  `LongitudinalWilsonSegment`, `TransverseInfinitySegment`,
  `ModifiedDeltaDampingOperator`, `FiniteSegmentLimit`,
  `ExecutableEikonalVertex`, `ExecutableLinePairKernel`,
  `ExecutableSelfKernel`, `ExecutableCuspKernel`, and
  `ExecutableBoundaryKernel`.
- **Remaining sectors and closure:** `SoftZeroModeSector`,
  `SoftBoundarySector`, `SoftBareOneLoopResult`, `SoftCountertermSystem`,
  `SoftRenormalizedOneLoopResult`, `SoftTrajectoryAxis`,
  `SoftTrajectoryFamily`, `SoftTrajectoryResult`,
  `SoftSideOverlapObject`, `C35CapabilityMatrix`, and `C35ClosureReport`.

These are strict contracts, not placeholder physics.  An object marked
available must carry the corresponding material arrays/expressions and a
closed proof set; an unavailable object must be empty-not-zero.  C35's
manifests instantiate the exact oracles that close and leave the physical
gauge, mode, graph, counterterm, trajectory, and overlap records unavailable.

## Compact gauge-plan and analytic-oracle API

The remainder of this document describes the executable compact helpers in
`s0c.core`.  Formal consumers should use the package-level records above and
the generated manifests; they should call these helpers only when reproducing
the C35 analytic or injection checks.

### `GaugePlanKind`

The enum has exactly four mutually exclusive members:

```text
S0C-COVARIANT-KREIN
S0C-LIGHT_FRONT-PHYSICAL
S0C-AUXILIARY-EIKONAL
S0C-UNAVAILABLE
```

### `GaugePlanCandidate`

Stores the candidate identity, kind, support flag, finite-regulator gauge
closure, regulator identity, source authority, blockers, and whether a
coefficient is allowed.  A candidate cannot permit coefficient execution
unless it is simultaneously supported, gauge complete at finite regulator,
and regulator identical.

### `GaugePlanSelection`

Requires all four candidates in enum order, freezes the decision before a
coefficient attempt, and stores the selected plan, no-go code, branch, and
next package.  Selecting `S0C-UNAVAILABLE` while claiming a coefficient was
attempted raises an error.

### `default_gauge_plan_selection()`

Returns the authoritative C35 selection.  The covariant-Krein candidate lacks
the finite-cell BRST/Krein action and metric, zero-mode/boundary completion,
and finite-delta gauge closure.  The light-front-physical candidate lacks the
instantaneous kernel, constrained zero modes, residual-gauge prescription,
and proved modified-delta map.  The auxiliary candidate is not the same
Minkowski lightlike operator and lacks the endpoint and finite-regulator
conversion.  The returned selection is therefore `S0C-UNAVAILABLE`,
`coefficient_attempted=False`, Branch G.

## Exact convention API

### `LightFrontConvention`

The immutable default `C35.LF.CONVENTION.SQRT2.v1` fixes

```text
metric:   (+---)
v+/-:     (v0 +/- v3)/sqrt(2)
n:        (1,0,0,1)/sqrt(2)
nbar:     (1,0,0,-1)/sqrt(2)
n.nbar:   1
Fourier:  A(x) = integral[d4k/(2pi)^4] exp(-i k.x) A(k)
```

Methods:

- `dot(a, b)` evaluates the Minkowski scalar product;
- `plus_minus(v)` returns `(v_plus, v_minus)`;
- `reconstruct(plus, minus, transverse)` returns a Cartesian four-vector;
- `pole_components(k)` returns `(k_plus, k_minus)` through
  `(nbar.k, n.k)`.

The constructor validates nullness and `n.nbar=1`.  Consequently
`k^2=2*k_plus*k_minus-kT^2`.  This class is a convention oracle, not a gauge
realization.

### `RapidityRegulatorRescaling`

The immutable default `C35.NULL.DELTA.RESCALING.v1` implements

```text
n -> lambda n
nbar -> lambda^-1 nbar
delta_minus -> lambda delta_minus
delta_plus -> lambda^-1 delta_plus
```

`transform(lambda, delta_plus, delta_minus)` enforces positive inputs and
returns the transformed pair.  `invariant_product(...)` verifies invariance
of `delta_plus*delta_minus`.  `source_to_project_delta_scale=1/sqrt(2)` maps
the source convention `n.nbar=2` to the project convention `n.nbar=1`.

## Coordinate, measure, and cell oracles

### `RealSoftCoordinateChart`

`C35.REAL.CHART.KAPPA_Y_PHI.v1` maps `(kappa,y,phi)` to

```text
k_plus  = kappa exp(y)/sqrt(2)
k_minus = kappa exp(-y)/sqrt(2)
kx      = kappa cos(phi)
ky      = kappa sin(phi)
```

with `kappa>0`, finite rapidity, and `phi` in `[0,2*pi)`.  The measure density
is `kappa/[2*(2*pi)^3]`; `mass_shell_residual` checks the exact massless
identity.  Its status is
`EXECUTABLE_GEOMETRIC_CHART_NOT_GAUGE_MODE_BASIS`.

### `VirtualSoftCoordinateChart`

`C35.VIRTUAL.CHART.KPLUS_KMINUS_KX_KY.v1` stores the direct virtual measure
`d4k/(2*pi)^4`, invariant `2*k_plus*k_minus-kT^2`, and propagator denominator
with `+i0`.  It supplies `invariant` and `measure_density`.  Its contour status
is `UNRESOLVED_BLOCKING_NO_REGULATOR_IDENTICAL_CONTOUR`; it is not an
executable physical loop integral.

### `SoftCellBoundary`, `SoftCellPrototype`, and `real_cell_prototype`

`SoftCellBoundary` validates matching dimensions and strictly ordered finite
intervals.  `real_cell_prototype(...)` integrates the real-chart scalar
measure over one rectangular `(kappa,y,phi)` cell and returns a normalized
top-hat `SoftCellPrototype`.  The invariant
`measure_value*top_hat_normalization**2=1` is checked at construction.

This proves only scalar cell normalization.  The prototype has no Lorentz,
polarization, ghost, auxiliary, constraint, commutator, or boundary-mode
content and must not be promoted to a gauge mode.

## Modified-delta and singular-cell oracles

### `ModifiedDeltaDampingOperator`

The operator records the source locator and the decisive flags
`gauge_property_at_finite_delta=False`,
`gauge_property_restored_only_in_delta_limit=True`, and
`power_delta_terms_must_be_discarded=True`.

`finite_segment_factor(omega, delta, length)` evaluates

```text
[exp((-delta+i*omega)*length)-1]/(-delta+i*omega)
```

and `infinite_segment_factor(omega,delta)` evaluates
`1/(delta-i*omega)`.  Positive damping and, for a finite segment, positive
length are mandatory.  `ward_bulk_defect(...)` returns the explicit
finite-delta bulk-versus-endpoint defect.  The damping is part of the Wilson
path integral.  These methods do not restore gauge invariance or define a
complete finite-mode Wilson operator.

### `SingularCellOracle`

The oracle implements an analytic principal value, the distributional
identity `1/(x-i0)=PV(1/x)+i*pi*delta(x)` with explicit pole sign, and a
finite-delta logarithmic comparison.  It requires an interior pole for the
principal-value case.  `center_sampling_forbidden=True` and
`physical_cells_executed=0` are scientific invariants: this is a method
oracle, not evidence that a physical pole-containing cell has been
integrated.

## Architecture and closure records

### `ArchitectureObjectRecord` and `architecture_records()`

The architecture inventory covers every named C35 plan, chart, mode, action,
Wilson, graph, counterterm, trajectory, overlap, and closure type.  Exact
convention/geometric objects are marked
`EXACT_OR_GEOMETRIC_ORACLE_IMPLEMENTED`; gauge candidates are
`PLAN_COMPILED_FAIL_CLOSED`; unresolved physical objects are
`UNAVAILABLE_EMPTY_NOT_ZERO`.  `positive_regulator_claim=True` is rejected on
Branch G.

### `ContributionStatus`, `SoftContributionResult`, and
`fail_closed_contribution_ledger()`

The ledger has exactly eighteen contribution classes.  On the authoritative
branch every row is `UNRESOLVED_BLOCKING`, has expression
`NONZERO_UNKNOWN`, and stores its exact missing calculation.  Resolved-zero,
cancellation, target-scaleless, and not-applicable statuses exist only as
typed future states; each requires the corresponding exact proof and cannot
be assigned merely from a topology name or continuum convention.

### `SoftBareOneLoopResult`

The class enforces tree value one and forbids continuum-coefficient
substitution.  If all contribution slots are not resolved, the only legal
one-loop state is `one_loop_value=None` with `NONZERO_UNKNOWN`.  It therefore
cannot serialize a fabricated finite-basis coefficient.

### `SoftCountertermSystem`

The UV, rapidity, and residual-line-mass counterterms cannot be populated
until a bare coefficient is available.  Conversely, declaring a bare
coefficient available requires all three counterterm fields.  C35 leaves the
system empty-not-zero.

### `C35ClosureReport` and `default_closure_report()`

The default closure report records a decided plan, validated light-front
normalization and chart geometry, but false gauge-complete realization,
executable mode basis, one-loop coefficient, UV/rapidity renormalization, and
soft-side zero-bin readiness.  Dependency checks prohibit claiming a mode
basis without a gauge realization, a one-loop result without a mode basis,
or renormalization without the bare coefficient.

## Injection and validation helpers

`injection_rows(count=2511)` builds deterministic negative-control payloads
covering ancestry, gauge realization, convention, modes, measures, Wilson
segments, diagrams, counterterms/trajectory, the soft-collinear interface,
and scope leakage.  The 93 distinct fault modes are paired with concrete
targets spanning all 53 architecture classes, 18 contribution slots, and 27
frozen holdouts; the 2,511 fault--target pairs are unique rather than copies
distinguished only by an ordinal.  `execute_injection_payload(...)` evaluates one payload
and optionally verifies its content hash.  These helpers test fail-closed
contracts; they do not produce physics values.

The manifest builder writes the C35 JSON records under `docs/next_level/`.
The decisive machine-readable files include:

- `c35_gauge_complete_plan_selection.json`;
- `c35_light_front_convention.json` and
  `c35_null_vector_regulator_rescaling.json`;
- `c35_real_coordinate_chart.json` and
  `c35_virtual_coordinate_chart.json`;
- `c35_modified_delta_operator.json`;
- `c35_contribution_closure_matrix.json`;
- `c35_bare_soft_coefficient.json` and
  `c35_soft_counterterm_results.json`;
- `c35_c32_continuation_gate.json`;
- `c35_no_go_decision_tree.json` and `c35_regression_report.json`.

## Forbidden interpretations and usage

The following uses are invalid:

- treating a chart, scalar top-hat, source transcription, continuum limit,
  or interface record as a gauge-complete finite-basis calculation;
- assigning zero to any unresolved graph, zero mode, boundary term, or
  counterterm;
- solving UV or rapidity counterterms before the bare coefficient;
- copying the continuum modified-delta coefficient into the finite basis;
- exporting a proton TMD or invoking C32 continuation;
- consuming ART25 members, data, chi-squared values, bridge residuals, or
  proton-level ratios;
- constructing a fit, likelihood, posterior, emulator, process prediction,
  deuteron prediction, inference route, or production route.

Any future positive calculation must descend through a new versioned C36/O4
regulator architecture and satisfy the dependency gates in
`c35_missing_calculation_specification.md`.
