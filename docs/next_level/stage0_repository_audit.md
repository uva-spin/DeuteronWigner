# C0 Stage 0 repository audit

## Scope and result

This audit maps the accepted leading-twist, forward spin-1 quark/gluon model
onto the formal architecture proposed in
`references/algebraic_geometric_next_level_model_note.tex`, while preserving
the physics documented in `references/model_construction_note.tex` and the
GTMD-first construction in `Deuteron_GTMD.pdf`. It is non-destructive:
no parent value, sign, normalization, flavor composition, gauge-link/color
assignment, nuclear ordering, wave function, ensemble semantic, table, or
tolerance was changed.

The numerical oracle is reproducible and clean. The full suite gives **484
passed, 0 failed**. All nine documented acceptance/report commands pass; all
36 quark/gluon evidence rows pass; and all 162 pages of the authoritative TMD
atlases render. Exact commands, versions, hashes, and numerical invariants are
in `stage0_regression_baseline.json`.

## Authoritative present boundary

The immutable regression boundary consists of canonical composed and resolved
nuclear quark/gluon TMD tables plus their unprojected correlator tables. The
resolved parents contain 38,880 quark rows and 49,680 gluon rows. The
scientific-inspection, resolved-parent, evidence-parity, and WP12-E JSON
reports are the acceptance witnesses. Their SHA-256 values are frozen in the
baseline file. The boundary is the leading-twist forward model at
`Q = 5 GeV`, sampled at `x_N = 0.02, 0.05, 0.10, 0.20, 0.40`; full rank-aware
multi-Q evolution is not part of that accepted boundary.

Accepted extrema include minimum joint-density eigenvalues
`4.126115619596484e-4` (quark) and `2.088097121459657e-2` (gluon), response
closure `1.3877787807814457e-17`, exact resolved quark closure, resolved
gluon closure `1.734723475976807e-18`, exact quark link reversal, and gluon
link reversal residual `1.2851608666153425e-9`.

## Convention audit

### Light-front convention and mass operator

`kinematics.LightFrontVector` explicitly uses
`v^± = (v^0 ± v^3)/sqrt(2)`, hence
`v^2 = 2 v^+ v^- - v_T^2` and
`p^- = m^2/(2p^+)` for an on-shell collinear state. The symmetric
zero-skewness frame is consistent with this convention. No contradictory
light-front mass formula was found in executable source.

The gap is architectural: wave-function and convolution modules do not
consume a typed `LFMassOperator`. A future implementation could therefore
introduce a convention-inconsistent Hamiltonian without being rejected by
the type boundary. C1 must encode and test the factor of two rather than
altering any current wave-function value.

### Fourier pairs and transverse coordinates

The central convention module correctly distinguishes:

* GTMD imaging:
  `W(bDelta) = ∫ d²Delta/(2π)² exp(-i Delta·bDelta) W(Delta)`;
* TMD impact space:
  `F~(bTMD) = ∫ d²k exp(+i bTMD·k) F(k)`.

`BDelta` and `BTMD` are distinct Python types at the direct Cartesian Fourier
boundary, and a test rejects their interchange. This protection stops at
that boundary. The radial Bessel transforms, matching/evolution providers,
pion and Sivers boundaries, and evolved grids use a generic scalar or array
named `b`. Wigner scripts also use generic `b` for `bDelta`. Nuclear impact
coordinates use the same notation.

The complete ambiguity catalog is `coordinate_uses` in the coverage JSON.
The highest-risk cases are:

1. untyped radial `bTMD` in `fourier.py`, matching, evolution and model
   providers;
2. raw `delta_x/delta_y` and tuples in GTMD/nuclear convolution;
3. no types for nuclear `DeltaNT`, internal `pT`, or impact `RT`;
4. raw measured `qT`/hadron transverse momentum in process code;
5. `gluon_correlator.DELTA_T` denotes the transverse identity metric, not a
   momentum transfer, creating a name-level collision.

Fourier signs are explicit in `conventions.py` and the common Fourier
functions. Some specialized analytic transforms encode signs and factors in
formulas/comments inside `pion_tmd.py`, `bpv20_sivers.py`,
`evolved_quark_model.py`, and the gluon linear-polarization adapter. They are
tested numerically but are not instances of a typed transform convention.

### Rank, mass normalization, and tensor sign

The full quark/gluon registries store transverse rank, and
`transverse_tensors.py` constructs definite-rank symmetric-traceless tensors.
Correlator bases explicitly include powers of the supplied mass. However:

* Fourier-Bessel functions accept a bare integer rank;
* `rank_normalization` is an arbitrary scalar rather than a named convention;
* correlator arrays do not carry the mass used to define their scalar TMD;
* serialized rows do not require rank or mass-normalization metadata.

The `deltaT_f1 ↔ f1LL` sign adapter is centralized in `conventions.py`, and
quark basis code documents the internal/physical `S_LL` sign. Named
projection tests exercise the adapter. No conflicting accepted tensor sign
was found.

## Map-class audit

The five map classes exist as physics, but not as enforced interfaces.

| Class | Existing realization | Implicit/untyped composition |
|---|---|---|
| `Amp` | LF partial waves, wave functions, off-forward overlaps, GTMD and parent convolutions | callables and arrays pass from wave-function overlap into nuclear convolution without declared representation-valued domain/codomain |
| `Dens` | spin-half/spin-1 correlators, joint density matrices, CP response maps, positivity audits | correlator arrays and CP maps do not share a Hilbert-space identity or typed partial trace |
| `Match` | `TMDScheme`, scale points, quark/gluon small-b matching and CSS evolution | scheme/scale records are adjacent to, rather than part of, the operator/value identity |
| `Red` | `SampledGTMD.tmd/gpd/pdf/wigner_at`, projectors, current convolution | methods/functions return matrices or dictionaries without typed reduction domains, codomains, or commutation certificates |
| `Proc` | SIDIS Bessel integral and W+Y validity gate | no object jointly identifies hard kernel, fragmentation, Wilson path/color weight, matching scheme, measured coordinate and validity region |

Particularly important cross-class compositions occur in
`gtmd_convolution.py`, `parent_quark_tmd.py`,
`canonical_parent_enrichment.py`, `resolved_nuclear_parent.py`,
`pion_tmd.py`, `tmd_evolution.py`, and `sidis.py`. Their current numerical
ordering is accepted; C1 must wrap it, not reorder it.

## Operator-identity audit

No existing operator/correlator object is identity-complete. The detailed
object-by-object assessment is in `operator_identity_assessments` in the
coverage JSON.

`SampledGTMD` comes closest at the GTMD level: it stores species, a projection
string, a minimal two-direction link, momentum axes, and target-helicity
fibers. It lacks flavor, explicit incoming/outgoing momentum fibers,
representation and gluon color class, a path/cusp/closure description,
renormalization and rapidity data, scales, rank, and mass normalization.

The spin-half and spin-1 correlators deliberately store only matrix content.
Their species/flavor/link/member/scale labels are supplied by outer loops or
unconstrained CSV-label mappings. `TMDEntry` stores species, rank, target
channel, T parity, and a Boolean “link required,” but not a particular link.
`TMDScheme` and `TMDScalePoint` contain the missing scheme/scales but are not
bound to the correlator. `PredictionTrace` contains species/flavor/projection/
channel/link strings and component provenance, but not the full typed
operator identity. This fragmentation permits an invalid composition to be
representable.

For gluons the most serious omission is that the link pair and `f`/`d` color
class are not intrinsic to `Spin1GluonCorrelator` or serialized correlator
identity. Present builders preserve them in outer labels and tests; the
architecture cannot yet make a wrong combination unrepresentable.

## Core-object coverage

All fifteen requested future objects have entries `C0-OBJ-01` through
`C0-OBJ-15` in the machine-readable matrix. Each entry records formal
responsibility, partial implementation, missing behavior, dependencies,
physics risk, proposed source location, tests, and migration order.

The strongest existing foundations are:

* explicit LF and Fourier conventions;
* complete spin-1 quark/gluon correlator bases and projectors;
* joint positive matrices and CP nuclear response maps;
* scheme compatibility guards;
* flavor-resolved parent tables and named uncertainty axes;
* component provenance records and numerical acceptance reports.

The most serious missing objects are:

* one decorated `OperatorIdentity`;
* typed `Amp/Dens/Match/Red/Proc` protocols;
* `PathGroupoid` plus representation-aware `WilsonTransport`;
* `ProvenanceComplex` with explicit replacement/exclusion edges;
* a common `EnsembleStore`;
* an `ObservableLikelihood` and observable-level `TruncationTower`.

## Stage 0/Stage A formal coverage

The coverage matrix assigns stable IDs to every C0 requirement, all four
revised-architecture Stage A requirements, and the GTMD-first Stage 0
requirements. Existing coverage is not overstated: complete helicity
containers and projectors are covered; coordinate separation, reductions,
map classes and operator identity are partial or missing; the formal Stage A
objects are planned.

## Risks and unresolved ambiguities

1. **Identity fragmentation (critical):** compatible-looking arrays can have
   different link, scheme, scale, rank or mass conventions.
2. **Coordinate aliasing (critical):** generic `b`, `DeltaT`, and `qT`
   arguments cross physically distinct Fourier and process layers.
3. **Map-class collapse (high):** amplitude, density, matching, reduction and
   process maps can be composed as ordinary functions.
4. **Gluon path/color identity (critical):** the two links and `f/d` class are
   outer metadata rather than operator identity.
5. **Provenance exclusion (high):** component records do not encode
   replacement or mutual exclusion, so double counting is prevented by
   builder logic and tests rather than graph validity.
6. **Rank normalization (high):** rank is registered but not carried through
   every transform and serialized object.
7. **Observable convergence (high):** model variants and uncertainty members
   exist, but no object records convergence along a nested truncation tower
   for a specified observable.

These are architecture gaps, not evidence that the accepted numerical
parents should be changed.

## C0 acceptance audit

| Criterion | Evidence | Result |
|---|---|---|
| Full regression and acceptance run | baseline commands/results | pass |
| Every Stage 0/A requirement mapped | `requirements` with stable IDs | pass |
| Every ambiguous coordinate use catalogued | `coordinate_uses` | pass |
| Every operator family assessed | `operator_identity_assessments` | pass |
| Every proposed core object mapped | `core_objects` | pass |
| File/test-level migration plan | `stageA_migration_plan.md` | pass |
| Accepted physics unchanged | parent hashes equal frozen oracle | pass |
| Unambiguous next job | C1 below and handoff update | pass |
| JSON consistency/format | `python -m json.tool` and Stage 0 validator | pass after validation command recorded |

## Exact next implementation job

**C1: Typed convention and identity spine.** Add the isolated
`src/deuteron_wigner/formal/` value objects for transverse coordinates,
transverse-rank/mass conventions, sector keys, Wilson-path identity, complete
operator identity, and typed map protocols. Add adapters that wrap—but do not
replace—the current accepted correlators and reductions. Inject rejection
tests for coordinate, sign, rank, scheme and gluon color-class mismatches,
then prove byte-for-byte equality of every authoritative C0 artifact.
