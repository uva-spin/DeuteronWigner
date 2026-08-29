# Missing C35 gauge-complete regulator and finite-basis soft calculation

## Binding C35 result

C35/S0C terminates on the typed unavailable branch:

```text
gauge plan:      S0C-UNAVAILABLE
primary no-go:   C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
secondary no-go: C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
branch:          G
coefficient:     not attempted; NONZERO_UNKNOWN
counterterms:    not solved; EMPTY_NOT_ZERO
continuation:    C36/O4 — replacement regulator architecture for the
                 microscopic TMD soft root
```

This document specifies the missing calculation.  It is not a proposal to
fill empty fields in the incompatible C33/C34 descriptor.  The next positive
calculation must begin from a new, versioned, baryon-number-zero regulator
root and preserve the C32 collinear root as a distinct object.

The result follows from the audited implementation in
`src/deuteron_wigner/bridge/s0c/core.py` and the machine-readable decision in
`docs/next_level/c35_gauge_complete_plan_selection.json`.  The authoritative
starting commit is `6bdb44be2afc79e817f69ce0e35813da8a394db7`.

## Object that is missing

The missing object is a regulator-identical, gauge-complete finite-basis
definition of the four-line vacuum soft operator, including its free field
theory, path-ordered Wilson operator, one-loop real and virtual sectors,
renormalization, regulator trajectory, and soft-side overlap limit.  It must
make executable all of the following together:

1. a selected gauge realization at finite regulator;
2. normalized modes and a complete metric/constraint structure;
3. all finite Wilson segments and the transverse closure at infinity;
4. rapidity damping acting on finite modes inside the Wilson operator;
5. pole-safe real and virtual integration machinery;
6. all eighteen contribution classes counted exactly once;
7. the bare finite-basis coefficient before any counterterm solution;
8. UV, rapidity, and residual-line-mass renormalization;
9. a finite-basis-to-continuum conversion and held-out regulator trajectory;
10. an operator-identical soft-side limit for the C32 zero-bin contract.

The exact tree value

```text
S_FB^(0)(bT) = 1
```

and the convention

```text
S_FB^bare = 1 + a_s C_F S_FB^[1],bare + O(a_s^2)
a_s = alpha_s/(4*pi) = g_s^2/(4*pi)^2,   C_F = 4/3
```

are already fixed.  The missing quantity is
`S_FB^[1],bare`, not its convention.  It has no numerical value in C35.

## Why integration cannot start from the inherited descriptor

The exact light-front convention and coordinate charts are known, but they
are kinematic oracles rather than a gauge field theory.  The normalized real
top-hat prototype is a scalar cell, not a mode with a Lorentz or physical
polarization metric.  The virtual chart has no regulator-identical contour.
The R1--R3 dimensions are support descriptors rather than materialized mode
collections.

More decisively, the modified-delta source
`data/raw/c31_sources/1511.05590.pdf` states that the regulated Wilson lines
do not retain the original Wilson operator's gauge properties at finite
delta.  Gauge properties are recovered only under its regulator-removal
prescription, including the stated treatment of power-divergent delta terms.
The inherited finite-cell construction supplies neither a gauge-restoring
completion at finite delta nor a proved conversion from another
gauge-complete regulator.  Its explicit finite-delta Ward defect therefore
cannot be renamed gauge closure.

The three positive candidates fail for different reasons:

- **Covariant/Krein:** no finite-cell BRST/Krein action, indefinite metric,
  constraint complex, ghost sector, zero-mode completion, transverse-boundary
  completion, or finite-delta gauge proof.
- **Light-front physical:** no complete instantaneous-gluon kernel,
  constrained zero modes, residual-gauge boundary prescription, or proved
  map to the covariant lightlike modified-delta target.
- **Auxiliary eikonal:** available constructions define different Euclidean
  or spacelike operators; no proof supplies the same Minkowski lightlike
  modified-delta endpoint structure and finite-regulator conversion.

Consequently no graph coefficient is well defined in the inherited basis.
Continuum modified-delta coefficients cannot be copied into it, and
dimensional-regularization scalelessness cannot be used to erase finite-cell
power or boundary terms.

## C36/O4 dependency-ordered execution specification

### O4.1 Create and freeze a replacement soft-regulator root

Define a new versioned `B=0` operator-completion root.  Its identity must
include gauge realization, action/Hamiltonian, basis and volume regulators,
IR regulator, rapidity regulator, boundary conditions, Wilson geometry,
renormalization target, regulator-removal path, and source provenance.  It
must be distinct from C11's `B=1` proton state, C32's collinear root, and the
historical C33/C34/C35 soft descriptors.

Freeze the complete choice before evaluating any one-loop coefficient.
Changing the gauge, rapidity action, boundary condition, zero-mode policy, or
trajectory creates a new root rather than mutating results in place.

**Gate:** one and only one gauge-complete realization is selected; all
identity fields and regulator-removal limits are explicit.

### O4.2 Define the finite-regulator gauge theory

For a covariant/Krein route, provide the regulated free action, gauge-fixing
term, ghost/BRST complex, indefinite polarization metric, physical-state
condition, finite-cell commutators, and Ward or Slavnov--Taylor identities.
For a light-front-physical route, provide the complete constraint solution,
physical polarization completeness, instantaneous-gluon interactions,
zero-mode and residual-gauge sectors, and transverse boundary prescription.

An auxiliary-field route is admissible only after an operator-level proof
that it represents the same Minkowski lightlike soft operator, or after a
finite conversion with a quantified remainder to the target operator.

**Gate:** gauge/constraint identities close at finite regulator or an exact
typed regulator conversion carries the defect; no continuum-limit assertion
may stand in for this proof.

### O4.3 Define finite volume, coordinates, and modes

Retain the exact project convention

```text
v+/-=(v0+/-v3)/sqrt(2),  n.nbar=1,
k^2=2*k+*k- - kT^2,     Fourier phase exp(-i k.x).
```

Implement complete real and virtual cell boundaries, measures, mode
functions, polarization/ghost/auxiliary metrics or physical-mode
commutators, quadrature nodes and weights, rapidity partitions of unity,
nested refinement maps, and explicit zero-mode cells.  The real on-shell
chart and direct virtual chart in C35 are exact seeds; they do not themselves
satisfy this task.

**Gate:** normalization and completeness identities close independently on
at least three nested resolutions, including held-out cells and all boundary
sectors.

### O4.4 Make every Wilson segment executable

Store the affine or piecewise parameterization, orientation, representation,
endpoint, path ordering, regulator action, and cell coupling for all four
fundamental/conjugate longitudinal lines and every segment of the transverse
closure at infinity.  Derive line-to-pole signs from the path and Fourier
conventions; they are not user-set coefficients.

**Gate:** reversing the complete operator performs the required
antiunitary/path/color conjugation, and endpoint plus transverse-junction
identities close without silent segment omission.

### O4.5 Resolve the rapidity regulator

Choose one of two defensible routes:

1. construct a finite-regulator gauge-restoring completion of modified delta,
   including the finite-mode damping action and any necessary compensator or
   counteroperator; or
2. select a gauge-complete finite-basis rapidity regulator and derive an
   operator-level conversion to the project modified-delta target.

Under the inherited null-vector normalization the exact rescaling remains

```text
n -> lambda n,        nbar -> lambda^-1 nbar,
delta- -> lambda delta-,   delta+ -> lambda^-1 delta+,
delta+ delta- invariant.
```

The source-to-project delta parameters are divided by `sqrt(2)`.  The
regulator must act inside the finite-mode Wilson operator, never only as
metadata or a post-integration multiplier.

**Gate:** the finite-regulator Ward/constraint defect vanishes or is carried
by a derived conversion/remainder that closes in the removal limit.

### O4.6 Specify singular-cell and virtual-contour machinery

Partition every cell intersected by an eikonal, propagator, endpoint, or
zero-mode singular surface.  Use an explicit principal-value plus cut,
contour deformation, sector decomposition, or analytic subtraction.  Store
the prescription as part of the operator identity.  Center sampling across a
singular cell is forbidden.

**Gate:** independent analytic or high-resolution oracles validate pole
signs, imaginary parts, deformations, and partition recombination; contour
changes cannot cross a pole silently.

### O4.7 Re-establish the exact tree reduction

Prove the new root reduces to the same four-line color-singlet tree operator
with value one, and that no vacuum state is inserted into the proton Hilbert
space.  Prove all color, link, endpoint, and conjugate-line identities before
opening the one-loop graph ledger.

**Gate:** exact tree equality holds at every trajectory point and is
independent of any hadron state.

### O4.8 Calculate and close all eighteen contribution classes

Every contribution below must be calculated, proved zero by an exact
identity, proved to cancel with a named partner, or proved not applicable by
the selected gauge action.  Each result must retain its regulator dependence
and count-once provenance.

| Contribution class | Exact missing calculation |
|---|---|
| `N_NBAR_EXCHANGE` | Sum the regulator-specific one-gluon exchanges between oppositely directed lightlike sectors, with orientation-derived eikonal prescriptions and all conjugate-line partners. |
| `CONJUGATE_LINE_EXCHANGE` | Evaluate exchanges joining amplitude and conjugate-amplitude Wilson lines with the full color trace, antiunitary reversal, cuts, and endpoint assignments. |
| `SAME_DIRECTION_LINE_EXCHANGE` | Evaluate exchanges between parallel lines at finite volume and rapidity regulator; do not infer zero from a continuum scaleless integral. |
| `REAL_ONE_SOFT_GLUON` | Integrate the complete on-shell one-gluon cut measure over normalized gauge modes, including rapidity partitions, pole cells, and all line attachments. |
| `VIRTUAL_ONE_SOFT_GLUON` | Integrate the complete virtual graph set using the selected contour, gauge/ghost or physical-constraint sector, and finite-mode Wilson vertices. |
| `WILSON_LINE_SELF_ENERGY` | Evaluate finite-length/self-line graphs and separate UV, rapidity, endpoint, and residual line-energy structures. |
| `CUSP_ENDPOINT` | Compute each cusp and finite endpoint term with explicit ownership; test reversal and cusp-anomalous-dimension signs. |
| `TRANSVERSE_CLOSURE` | Compute attachments to and self-contributions of the transverse link at infinity, including its junctions and boundary limit. |
| `AUXILIARY_FIELD_SELF_ENERGY` | Calculate it if the chosen realization has auxiliary eikonal fields, or supply a selected-action proof of non-applicability. |
| `SOFT_VACUUM_ENERGY` | Evaluate and subtract the finite-basis vacuum normalization according to a declared count-once prescription. |
| `LIGHT_FRONT_INSTANTANEOUS` | Calculate the complete instantaneous kernel for a light-front realization, or provide a covariant/auxiliary action proof locating its equivalent contribution. |
| `GAUGE_FIXING` | Include the selected gauge-fixing sector and demonstrate gauge-parameter or constraint independence of the completed result. |
| `GHOST` | Calculate finite-cell ghost graphs for a BRST route, or prove non-applicability from the selected physical/auxiliary action. |
| `ZERO_MODE` | Calculate the explicit constrained/zero-mode sector and its Ward, rapidity, line-energy, transverse-link, and conversion effects; exclusion alone is not zero. |
| `BASIS_BOUNDARY` | Calculate finite-volume, support-edge, rapidity-window, and cell-interface terms and follow them along refinement trajectories. |
| `RAPIDITY_COUNTERTERM` | After the bare sum exists, extract the rapidity divergence in the same regulator and solve the counterterm and rapidity anomalous dimension. |
| `UV_COUNTERTERM` | After the bare sum exists, extract the UV divergence, mix all permitted operators, and solve the target-scheme counterterm. |
| `RESIDUAL_LINE_MASS_COUNTERTERM` | Determine any regulator-induced line-energy/power subtraction from the same finite-basis calculation and prove its state independence. |

**Gate:** the ledger contains exactly eighteen resolved entries; all
cancellations name both partners; all zeros cite an exact identity; the sum
contains no duplicate ownership or unassigned residual.

### O4.9 Construct the bare coefficient

Only after O4.1--O4.8 pass may the eighteen entries be assembled into
`S_FB^[1],bare`.  Preserve separately UV logarithms, rapidity logarithms,
IR dependence, finite terms, power dependence, zero-mode/boundary terms, and
numerical quadrature error.

**Gate:** independent direct-assembly and graph-ledger routes agree at held-out
regulator points, and gauge/constraint and real-virtual residuals close.

### O4.10 Solve renormalization and anomalous dimensions

Using the bare result in the same regulator, solve UV, rapidity, and any
residual-line-mass counterterms.  Test the renormalization group, rapidity
group, cusp relation, mixed derivative consistency, regulator independence,
and state/hadron independence.  Counterterms cannot be inferred from ART25,
bridge points, or a continuum coefficient substituted for the bare result.

**Gate:** all counterterms are fixed from ultraviolet/rapidity structure of
the operator calculation and pass independent holdouts.

### O4.11 Establish the continuum conversion and trajectory

Derive a finite-basis-to-continuum modified-delta conversion, its inverse,
round trip, perturbative order, domain, and remainder.  Vary independently
the UV extent, IR extent, rapidity window, rapidity-cell size, transverse
extent, transverse-cell size, zero-mode cutoff, line-length cutoff, and
quadrature order.  Use at least three nested points on every claimed
continuum axis and reserve held-out trajectories before fitting.

Energy convergence is not a soft-function convergence criterion.  Required
observables include the bare and renormalized soft coefficients, Ward or
constraint residuals, anomalous dimensions, conversion residuals, and all
boundary/zero-mode components.

**Gate:** continuum and order-of-limits claims are identifiable, held-out
residuals close, and unknown trajectory discrepancy remains explicit rather
than set to zero.

### O4.12 Close the soft-side C32 zero-bin interface

Construct the soft limit in the same partonic IR prescription as the frozen
C32 collinear calculation.  Prove equality of operator identity, gauge,
rapidity regulator, basis/continuum map, Wilson geometry, pole prescriptions,
and perturbative order before subtracting exactly once.  If a conversion is
needed, execute it with its remainder before comparison.

**Gate:** a nonempty `SOFT_LIMIT_C36` object and an operator-identical C32
overlap exist; only then may a later package consider a microscopic proton
TMD export.  C36/O4 itself should not infer a proton result merely from soft
closure.

## Required negative controls

At minimum, the replacement package must inject and reject:

- wrong `sqrt(2)` normalization or Fourier sign;
- swapped `delta+`/`delta-` rescaling;
- modified-delta damping applied after rather than inside path ordering;
- a missing transverse segment or wrong line orientation;
- scalar-cell normalization mislabeled as gauge-mode completeness;
- center sampling of a pole-containing cell;
- a virtual contour that crosses a pole;
- dropped ghost, instantaneous, zero-mode, endpoint, or boundary sectors
  without a selected-action proof;
- a continuum coefficient substituted for a finite-basis graph sum;
- counterterms solved before the bare coefficient;
- dimensional scalelessness used to set a finite-regulator contribution to
  zero;
- duplicate real/virtual or soft/zero-bin ownership;
- a one- or two-point trajectory presented as a continuum limit;
- state-dependent or hadron-dependent soft counterterms;
- ART25, process data, chi-squared values, bridge residuals, or proton ratios
  entering any kernel, counterterm, or trajectory fit.

## Non-negotiable exclusions

C36/O4 must not mutate the historical C11 density, C32 tree reduction,
C33--C35 roots, frozen bridge roles/holdouts, `NO_JOINT_MEASURE`, the 216-route
registry, or the eight authoritative artifacts.  It must not create a fit,
likelihood, posterior, emulator, process prediction, deuteron prediction,
inference route, or production route.  `MSHT20_REP/` remains untouched and
outside Git.

## Completion condition

The missing calculation is complete only when the selected replacement root
passes every gate above.  If no gauge-complete, regulator-identical
realization can be constructed, C36/O4 must retain a typed empty-not-zero
result and issue a more specific no-go.  It must not return to C35 and assign
a coefficient to the unavailable plan.
