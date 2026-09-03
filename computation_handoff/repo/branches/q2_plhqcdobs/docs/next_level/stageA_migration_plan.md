# Stage A migration plan: encode the accepted model without changing it

## Invariant

Stage A is an architectural migration, not a refit or physics revision. The
C0 hashes and accepted numerical metrics are immutable gates. New types may
reject invalid compositions; they may not change any valid central value,
normalization, sign, flavor mapping, nuclear ordering, wave-function choice,
member interpretation, or output tolerance.

## Execution sequence

### A1 — convention value objects

Add `formal/coordinates.py` with distinct Cartesian and radial types for
`KParton`, `DeltaParton`, `BDelta`, `BTMD`, `DeltaNuclear`, `PNuclear`,
`RNuclear`, and `QMeasured`. Units and conjugate partners are mandatory.
Add `formal/transverse_rank.py` with `TransverseRank`, tensor-basis convention,
reference mass identity, and Fourier phase/normalization identity.

Adapters belong in `formal/legacy_adapters.py`; existing APIs remain intact.

Acceptance:

* construction rejects negative radii and incompatible units;
* no `BTMD` can enter a `bDelta` transform, including radial transforms;
* rank/mass mismatch is rejected before numerical integration;
* wrappers reproduce every existing Fourier test to the current tolerance;
* deliberately swap all coordinate pairs and require deterministic failure.

### A2 — sector and operator identity spine

Add `formal/sector_space.py`, `formal/gauge_path.py`, and
`formal/operator_identity.py`. `SectorKey` must include partonic species and
flavor, color representation, target/nucleon sector, spin and SO(2) OAM
labels. `WilsonPathIdentity` must include endpoints, staple direction,
segments, cusp/closure information, and for gluons the two-link and `f/d`
class. `OperatorIdentity` must include:

* species/flavor and Dirac/Lorentz projection;
* initial/final momentum fibers;
* path and color representation;
* regulator, UV scheme, rapidity regulator and soft prescription;
* `mu`, `zeta`, transverse rank and mass-normalization convention.

Acceptance:

* every field missing in C0-OP-01 through C0-OP-10 is mandatory or represented
  by an explicit `Unknown` value that cannot be composed;
* no defaults silently select a path, scheme, color class or scale;
* quark flavor, antiquark flavor, gluon `f`, and gluon `d` identities remain
  distinct under hashing and serialization;
* future/past path inversion has the accepted T-odd signs;
* invalid scheme and gluon link/color combinations are injected and rejected.

### A3 — typed map classes

Add `formal/maps.py` protocols for `AmpMap`, `DensityMap`, `MatchingMap`,
`ReductionMap`, and `ProcessMap`. Each map exposes input/output identities,
linearity/CP status where applicable, provenance, and a compatibility check.
No implicit conversion is permitted between classes.

Acceptance:

* composing unlike map classes without an explicit bridge fails;
* domain/codomain mismatch fails before the callable executes;
* existing functions are wrapped through adapters with identical outputs;
* a deliberate “matching twice” chain and a reduction-before-required-
  matching chain are rejected.

### A4 — positive correlator and reduction wrappers

Add `formal/positive_correlator.py` and `formal/reduction.py`. Wrap
`Spin1QuarkCorrelator`, `Spin1GluonCorrelator`, and applicable spin-half
objects with Hilbert-space identity, normalization, trace and partial trace.
Positivity is a property/check, never a component-wise clip. Wrap the current
GTMD forward limit, `kT` integral, Fourier image, TMD projectors, and local
current as typed reductions.

Acceptance:

* wrapped and legacy matrices are elementwise identical;
* minimum eigenvalues reproduce the C0 baseline;
* TMD→PDF and GPD→PDF closure reproduces existing analytic fixtures;
* projector/reduction commutation passes on the current sampled GTMD and
  analytic two-body fixture;
* a controlled analytic three-body fixture is added and passes;
* wrong Fourier sign and wrong rank phase are injected and detected;
* no positivity repair is invoked on accepted central parents.

### A5 — hierarchical nuclear map and provenance complex

Add `formal/nuclear_amplitude.py` and `formal/provenance_complex.py`.
Represent the accepted order
partonic/nucleon operator → LF nuclear amplitude → density/response →
projection as explicit maps. Encode “adds with,” “replaces,” “excludes,” and
“requires” edges for impulse, off-shell, shadowing, pion exchange,
non-nucleonic, Wilson, shared-Fock/OAM and CP-response components.

Acceptance:

* the current canonical builder has one valid topological ordering equal to
  the accepted numerical ordering;
* all current central components have provenance nodes;
* adding both a component and its declared replacement is rejected;
* a deliberately duplicated nuclear response produces a double-counting
  error, not a changed prediction;
* proton/neutron and all flavor labels survive each map;
* resolved parent closures and response-chain residual reproduce C0.

### A6 — ensemble and observable convergence contracts

Add `formal/ensemble_store.py`, `formal/truncation.py`, and
`formal/observable_likelihood.py`. Preserve replica, Hessian, interval-hull,
model sensitivity and zero-centered alternative semantics as distinct kinds.
Bind process, hard/fragmentation/color weights, W+Y validity, dataset and
covariance to the observable identity. Record convergence by observable
across a nested truncation tower; do not infer convergence from the number of
formal components.

Acceptance:

* heterogeneous ensembles cannot be merged without an explicit rule;
* member IDs and cross-component correlation keys round-trip;
* W-only and W+Y domains remain those accepted by current tests;
* a process cannot consume the wrong Wilson path or gluon `f/d` class;
* convergence records identify the observable, norm, tolerance and adjacent
  truncations and cannot claim convergence from a single level.

### A7 — full oracle comparison

Add `scripts/validate_typed_architecture_regression.py` and
`tests/formal/test_authoritative_regression.py`. Rebuild all eight
authoritative TMD/correlator artifacts through typed wrappers into a temporary
directory. Compare shape, schema, row ordering, all values, metadata and
SHA-256 hashes. Re-run all acceptance builders and atlas rendering.

Acceptance:

* all eight artifact hashes equal `stage0_regression_baseline.json`;
* all accepted residuals/minima remain within their existing tolerances;
* all 36 evidence rows and all acceptance gates pass;
* the original 484-test suite remains clean in addition to new architecture
  tests;
* no generated authoritative file is overwritten during comparison.

## Dependencies and file order

1. `coordinates.py`, `transverse_rank.py`
2. `sector_space.py`
3. `gauge_path.py`, `operator_identity.py`
4. `maps.py`
5. `positive_correlator.py`, `reduction.py`
6. `legacy_adapters.py`
7. `nuclear_amplitude.py`, `provenance_complex.py`
8. `ensemble_store.py`, `truncation.py`, `observable_likelihood.py`
9. regression builder and exhaustive injected-failure tests

At every step, run the focused new tests, the original full suite, and the
hash comparator. A failed hash is a migration defect; it is not permission to
adjust the oracle.

## Definition of Stage A complete

Stage A is complete only when all `STA-*` matrix entries are `covered`, every
accepted parent passes byte-level regression, every decorated identity is
complete, all five map classes reject invalid compositions, all requested
negative tests fail for the intended reason, and the provenance graph rejects
known double-counting constructions. Interfaces alone are not completion.
