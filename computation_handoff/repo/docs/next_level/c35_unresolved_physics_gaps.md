# C35/S0C unresolved physics gaps

## Status boundary

C35/S0C resolves the regulator question negatively and precisely.  The
source-supported plan is `S0C-UNAVAILABLE`; the result is Branch G with

```text
C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
```

The absence of a calculation is represented as empty-not-zero, and every
potentially nonzero unresolved contribution is `NONZERO_UNKNOWN`.  The next
package is exactly `C36/O4 — replacement regulator architecture for the
microscopic TMD soft root`.

## What is exact in C35

The following statements are closed and may be inherited by C36:

- the soft root is a distinct `B=0` vacuum/eikonal object, not part of the
  `B=1` C11 proton state;
- the ancestry through C34, C33, C32, and C28 is fixed;
- the metric is `(+---)`,
  `v+/-=(v0+/-v3)/sqrt(2)`, `n.nbar=1`, and
  `k^2=2*k+*k--kT^2`;
- the Fourier phase is `exp(-i k.x)`;
- null-vector rescaling requires
  `delta- -> lambda*delta-` and
  `delta+ -> lambda^-1*delta+`, leaving `delta+*delta-` invariant;
- the source delta parameters map to project normalization with a factor
  `1/sqrt(2)`;
- the real massless chart and its measure, and the virtual geometric chart and
  its measure, are exact coordinate oracles;
- a scalar top-hat can be normalized with the real measure, but is not a gauge
  mode;
- a pole-containing cell must use a principal-value/cut, contour, or analytic
  subtraction; center sampling is forbidden;
- modified-delta damping belongs inside the finite Wilson path operator;
- the tree soft factor is one in the declared perturbative convention;
- counterterms cannot be solved before the regulator-specific bare
  coefficient;
- ART25, process data, bridge residuals, and proton-level ratios have no
  derivational role in this soft calculation.

## What the source establishes but C35 does not calculate

The modified-delta source is transcribed with explicit provenance.  It gives
the continuum regulator prescription and states that regulated Wilson lines
do not have the original Wilson operator's gauge properties at finite delta;
those properties are recovered only in the prescribed regulator-removal
limit, together with its treatment of power-divergent delta terms.  C35 also
records the finite- and infinite-segment damping factors and the resulting
finite-delta Ward defect.

These are source facts and analytic operator oracles.  They are not a
finite-cell gauge action, a finite-mode graph calculation, an independent
continuum reconstruction, or a finite-basis-to-continuum conversion.

## Blocking physics gaps

### 1. No gauge-complete regulator-identical realization

No audited route supplies the same lightlike Minkowski modified-delta
operator together with a complete finite-cell gauge theory.  The
covariant/Krein, light-front-physical, and auxiliary-eikonal candidates each
miss essential, different ingredients.  This is the first blocker; later
graph and renormalization gaps cannot be solved coherently before it.

### 2. No finite-regulator gauge or constraint identity

There is no finite-cell BRST/Krein complex, Slavnov--Taylor closure,
gauge-parameter independence proof, or complete light-front physical
constraint algebra.  The finite-delta Ward defect remains explicit.  A
continuum-limit gauge statement cannot certify the finite regulator.

### 3. No executable gauge-mode basis

The R1--R3 dimensions 3,841, 30,721, and 103,681 are descriptors only.  The
repository does not have complete gauge-mode cell boundaries, mode
functions, polarization/ghost/auxiliary metrics, commutators, quadrature
nodes and weights, partitions of unity, or nested refinement maps.  The
available scalar top-hat oracle does not close this gap.

### 4. No regulator-identical virtual contour

The direct `(k+,k-,kx,ky)` chart and `+i0` denominator are fixed, but pole
crossing, contour deformation, cut structure, and finite-cell virtual
quadrature are unresolved.  No physical virtual cell has been integrated.

### 5. Wilson geometry is not executable on finite modes

The four longitudinal directions and transverse closure are known
geometrically, but there is no complete finite-volume parameterization and
mode coupling for every segment, endpoint, and transverse junction.  Thus
line-to-pole signs cannot yet be propagated through a complete graph
calculation.

### 6. Modified-delta finite-mode gauge completion is absent

C35 can evaluate the analytic damping factor for a mode, but cannot make the
finite-delta Wilson operator gauge complete.  No compensator, counteroperator,
or alternative gauge-complete rapidity regulator with a proved conversion to
the target operator has been derived.

### 7. Singular physical cells remain unevaluated

Principal-value, cut, and finite-delta analytic identities are available only
as controlled method oracles.  The actual eikonal and propagator singular
surfaces have not been partitioned across a materialized basis, and no
physical cell has passed contour/subtraction convergence.

### 8. Zero modes and residual gauge structure are unresolved

The historical policy `EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL /
AUDIT_REQUIRED` does not prove a zero contribution.  Effects on Ward
identities, line energy, rapidity structure, transverse closure, and
conversion constants remain `NONZERO_UNKNOWN`.

### 9. Endpoints, transverse closure, and basis boundaries are unresolved

Cusp, finite-endpoint, transverse-infinity junction, finite-volume edge,
rapidity-window edge, and cell-interface terms have no regulator-specific
values.  They cannot be assigned to a continuum scaleless sector or hidden
inside a residual without explicit count-once ownership.

### 10. Real/virtual and gauge-sector completeness is absent

There is no complete one-gluon real cut and virtual graph assembly.  The
selected action has not determined the ghost, gauge-fixing, auxiliary,
instantaneous, and vacuum normalization sectors.  Therefore none can be
declared absent merely from the desired final gauge.

### 11. All eighteen contribution classes remain open

The complete inventory is:

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

Each is `UNRESOLVED_BLOCKING` and `NONZERO_UNKNOWN`.  A future entry may be
zero or not applicable only after an exact identity or selected-action proof;
a cancellation must name and calculate both partners.

### 12. No bare finite-basis coefficient

Only the tree coefficient exists.  The one-loop coefficient was deliberately
not attempted after the unavailable plan was frozen.  The continuum
modified-delta coefficient remains a source transcription and is not a
finite-basis value.

### 13. No counterterm or anomalous-dimension solution

Because the bare coefficient does not exist, the UV, rapidity, and residual
line-mass counterterms are empty-not-zero.  There is no regulator-specific
renormalized soft function, rapidity anomalous dimension, gauge residual,
cusp residual, or mixed RG/rapidity closure.

### 14. No regulator conversion or continuum trajectory

Nine regulator axes are typed—UV extent, IR extent, rapidity window,
rapidity-cell size, transverse extent, transverse-cell size, zero-mode
cutoff, line-length cutoff, and quadrature order—but have no evaluated
points.  Hence there is no conversion, inverse, round trip, extrapolation,
order-of-limits study, or uncertainty budget.  A short energy-convergence
tower would not establish soft-function convergence.

### 15. No independent continuum second route

The continuum target has not been reconstructed through an independent
graph-level or direct-integral route in this package.  Source transcription
alone cannot serve simultaneously as calculation and validation oracle.

### 16. No C32 soft-side overlap

`SOFT_LIMIT_C35` is empty-not-zero.  No exact map matches the C35 soft
regulator to C32's frozen spacelike-off-shell collinear regulator.  The
zero-bin cannot be subtracted or certified from a continuum citation, and the
C32 continuation gate remains false.

### 17. Universality remains required but unproved

The soft operator must be independent of the proton state and hadron
flavor.  With no complete regulator or coefficient, state and hadron
independence cannot yet be tested.  Any state-dependent counterterm or
hadron-level ratio would invalidate the soft root.

### 18. No downstream physics route is reachable

C35 exports no microscopic proton TMD, no twelve-point bridge, no process or
deuteron observable, and no inference or production object.  The production
registry remains at 216 routes and all eight authoritative artifacts remain
unchanged.  This is an enforced isolation property, not optional future
cleanup.

## Exact replacement target

The first executable task is not another graph estimate inside C35.  It is
`C36/O4`, which must create and freeze a replacement gauge-complete regulator
architecture and then satisfy the staged gates in
`c35_missing_calculation_specification.md`.  Only after that architecture
passes its finite-regulator gauge, mode, Wilson, singular-cell, and tree
tests may it open the eighteen-entry one-loop ledger.

If C36/O4 cannot provide such an architecture, it must fail closed with a new
typed no-go and leave the coefficient empty-not-zero.  It must not import the
continuum coefficient, silently discard zero modes or boundary terms, or use
phenomenological information to fill the missing operator calculation.
