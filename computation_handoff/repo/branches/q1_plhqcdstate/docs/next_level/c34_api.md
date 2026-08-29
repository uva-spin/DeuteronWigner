# C34/S0A API

## Purpose

The C34 API is a typed, immutable record and capability-gating layer for the
first one-loop calculation targeted at the B=0 vacuum/eikonal soft root.  At
the completed C34 status it is **not** a numerical finite-basis soft solver.
Its central responsibility is to prevent a source-qualified continuum result,
a symbolic current, or an enumerated diagram ledger from being promoted to a
calculated finite-basis coefficient.

The scientific root is

```text
C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT
```

with baryon number zero.  Every C34 identity envelope retains that root, the
exact four-line fundamental-singlet geometry, source and target regulator IDs,
perturbative order, and gauge and rapidity identities.  It records
`state_independence_required=true` and `hadron_independence_required=true`
separately from the corresponding `*_proved` fields, which remain false unless
the individual object carries an explicit proof.  Baryon-number-zero ownership
and hard-false reachability from ART25, process data, bridge residuals,
inference, and production enforce scope isolation; they are not a universality
proof.  The gauge identity is likewise an unresolved covariant-gauge probe
plan, not a completed gauge realization.

## Status contract

The contribution-status vocabulary is:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_IDENTITY
CANCELS_WITH_DECLARED_PARTNER
TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO
NOT_APPLICABLE_WITH_PROOF
UNRESOLVED_BLOCKING
```

An unresolved contribution must have:

- no numerical value;
- no numerical residual derived from that value;
- an exact missing-input or missing-calculation identifier;
- a dependency edge to every gate that it blocks;
- a nonempty source/derivation assessment;
- no replacement by a continuum, ART25, bridge, or fitted value.

`0.0` is reserved for a calculated zero or an exact identity carrying its
proof.  It is never the serialization of missing physics.

The package-level no-go is

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

and the positive statuses below are unavailable:

```text
C34_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED
C34_SOFT_UV_RENORMALIZATION_VALIDATED
C34_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C34_SOFT_REGULATOR_CONVERSION_VALIDATED
C34_SOFT_CONTINUUM_TRAJECTORY_RESOLVED
C34_SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST
C34_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING
```

## Principal immutable objects

The C34 architecture uses the object families required by the work package.
Their names describe contracts, not claims of numerical completion.

### Calculation and basis identity

- `SoftOneLoopPlan`: frozen plan, coupling normalization, Wilson geometry,
  gauge values, rapidity regulator, UV target, resolutions, zero-mode policy,
  frozen evaluation points, and holdouts.
- `SoftOneLoopOrder`: exact distinction among \(g_s^2\),
  \(a_s=\alpha_s/(4\pi)=g_s^2/(4\pi)^2\), the separate \(C_F\) prefactor, and the first omitted
  order.
- `SoftModeCellId`: identity of a cell.  C34 contains one illustrative
  descendant rectangular cell for type and phase-integral checks; that cell
  must not be represented as the complete reconstruction of the immutable
  C33 R1-R3 bases.
- `SoftModeQuadrature`: nodes, weights, measure, normalization, and generated
  code identity when available.  C34 freezes only the method family and nominal
  order; tolerances, subdivision limits, contour and pole-cell prescriptions,
  normalized modes, and the executable payload remain absent.
- `SoftModeCompletenessRecord`: finite-span and continuum/refinement checks.
  Tree-level dimension counting is not a one-loop completeness residual.

The helper `normalized_transverse_cell_phase` evaluates the exact normalized
rectangular-cell average of \(e^{ik_T\cdot b_T}\).  It is intentionally scoped
to the nonsingular transverse phase.  It does not evaluate the eikonal,
rapidity, energy, UV, zero-mode, or virtual integrals and therefore cannot
populate a one-loop coefficient.

### Wilson-line current and kernels

- `EikonalCurrent`: four-line symbolic current with complete line ancestry.
- `EikonalEmissionVertex` and `EikonalAbsorptionVertex`: conjugate vertex
  records.  A numerical matrix element requires a normalized gauge-field mode.
- `EikonalPairKernel`: ordered line-pair, color, phase, cut, pole, and
  regulator identity.
- `EikonalSelfKernel`: individual-line kernel and finite-cutoff divergence
  classification.
- `TransverseClosureKernel`: transverse-at-infinity path and junction kernel.

The line-level current contract is

\[
 J_a^\mu(k;b_T)=
 g\sum_\ell \mathcal T_\ell^a\sigma_\ell v_\ell^\mu
 e^{ik_T\cdot x_{\ell T}}D_\ell(k;\delta^\pm,i0).
\]

The API requires every numerator sign, tangent normalization, phase, and pole
to be derived from a parameterized path.  The C33 pole records alone are not a
complete vertex.

### Real, virtual, gauge, and boundary records

- `SoftVirtualAmplitude`, `SoftRealAmplitude`, `SoftCutLedger`, and
  `SoftRealVirtualAssembly` retain line-pair, cut, cell, phase, and count-once
  identities.
- `SoftGaugeContribution`, `SoftGhostContribution`, and
  `SoftInstantaneousContribution` prevent one gauge representation from
  silently borrowing the non-applicability rules of another.
- `SoftZeroModeContribution` and `SoftBoundaryContribution` preserve the C33
  exact-zero-mode exclusion as an unresolved control rather than a zero.

### Bare and renormalized coefficients

- `SoftBareCoefficient` and `SoftBareCoefficientDecomposition` carry the direct
  bare terms.  The zero-mode result is a separate control pending a later
  assembly decision; the nonadditive auxiliary route and the
  UV/rapidity/residual-line-mass decisions are also excluded explicitly.
  Counterterms use disjoint `C34.CT.*` IDs.  In Branch G the
  aggregate numerical value is absent because blocking inputs remain.
- `SoftUVStructure` and `SoftRapidityStructure` keep cutoff powers, cutoff
  logs, rapidity logs, finite terms, and remainders separate.
- `SoftUVCountertermSolution`, `SoftRapidityCountertermSolution`, and
  `SoftRenormalizedCoefficient` cannot validate unless every required bare
  input and inverse/closure check exists.
- `SoftRapidityDerivative`, `SoftCuspConsistency`, and `SoftCSKernelRecord`
  store derivative conventions separately from numerical availability.

### Continuum target and finite-regulator conversion

- `SoftContinuumTargetRecord` stores the modified-delta DR/MSbar source
  expression, normalization, and the status of graph-level and independent
  direct-integral reconstruction routes.  In C34 only the source's final
  formula is transcribed; both reconstruction routes remain false.  It always has
  `operator_identical_to_finite_basis = false`.
- `SoftFiniteRegulatorDifference`, `SoftFiniteRegulatorKernel`, and
  `SoftRoundTripReport` require both independently calculated sides.  In C34
  the finite side is absent, so the difference, kernel, inverse, and round-trip
  residual are absent.

The continuum target uses

```text
a_s = alpha_s/(4*pi) = g_s^2/(4*pi)^2
full one-loop correction = a_s * C_F * S^[1]
C_F = 4/3
```

with

\[
 S^{[1]}=-4\mu^{2\epsilon}(b_T^2/4)^\epsilon\Gamma(-\epsilon)
 [L_0-\psi(-\epsilon)-\gamma_E].
\]

It is a source-qualified target, not yet an independently reconstructed oracle,
and never a fallback value for `SoftBareCoefficient`.

### Trajectory and continuation

- `SoftResolutionSequence`, `SoftTrajectoryFitPlan`,
  `SoftTrajectoryHoldout`, and `SoftTrajectoryResult` distinguish support
  extension from true grid refinement and require separately variable
  regulator axes.
- `SoftSideZeroBinLimit` is an empty-not-zero soft-side object in C34.
- `SoftCollinearContinuationContract` retains the C32 domain, C33/C34
  codomain, common measurement requirement, count-once placement, and
  regulator-conversion requirement.
- `C34SoftCapabilityMatrix` and `C34ClosureReport` derive the no-go branch from
  the contribution and gate records.  They may not be set by a caller.

## Required contribution policy

The authoritative C34 policy is:

```text
N_NBAR_EXCHANGE                  UNRESOLVED_BLOCKING
CONJUGATE_LINE_EXCHANGE          UNRESOLVED_BLOCKING
SAME_DIRECTION_LINE_EXCHANGE     UNRESOLVED_BLOCKING
REAL_ONE_SOFT_GLUON              UNRESOLVED_BLOCKING
VIRTUAL_ONE_SOFT_GLUON           UNRESOLVED_BLOCKING
WILSON_LINE_SELF_ENERGY          UNRESOLVED_BLOCKING
CUSP_ENDPOINT                    UNRESOLVED_BLOCKING
TRANSVERSE_CLOSURE               UNRESOLVED_BLOCKING
AUXILIARY_FIELD_SELF_ENERGY      UNRESOLVED_BLOCKING
SOFT_VACUUM_ENERGY               UNRESOLVED_BLOCKING
LIGHT_FRONT_INSTANTANEOUS        UNRESOLVED_BLOCKING
GAUGE_FIXING                     UNRESOLVED_BLOCKING
GHOST                            UNRESOLVED_BLOCKING
ZERO_MODE                        UNRESOLVED_BLOCKING
BASIS_BOUNDARY                   UNRESOLVED_BLOCKING
RAPIDITY_COUNTERTERM             UNRESOLVED_BLOCKING
UV_COUNTERTERM                   UNRESOLVED_BLOCKING
RESIDUAL_LINE_MASS_COUNTERTERM   UNRESOLVED_BLOCKING
```

All eighteen machine statuses are therefore blocking.  Auxiliary self energy
is a candidate for a future non-applicability proof because the direct and
auxiliary plans are mutually exclusive.  A connected ghost graph is likewise
a candidate for a future order-counting proof in standard covariant QCD.
Neither candidate is promoted in C34: the explicit regulator-scope proof and
gauge-fixed finite-basis action required by the API are absent.

The cut API also separates a candidate topology label from a proved physical
branch.  Until an actual cut/mode calculation runs, every branch is
`UNRESOLVED_BLOCKING`, both assembled branch-ID lists are empty, and structural
ID uniqueness is not called physical count-once closure.

The modified-delta probe API stores independent one-axis-at-a-time
\(\delta^+\) and \(\delta^-\) variations and separate holdouts.  It does not
encode a fixed-ratio diagonal sequence as evidence of independent rapidity
dependence.

## Validation rules

A positive finite-basis one-loop gate requires all of the following:

1. Explicit normalized modes and cell measures at each resolution.
2. A gauge-complete action or rigorously equivalent contraction formulation.
3. Direct Wilson expansion and mode/cut assembly equality.
4. No blocking contribution status.
5. Separate and invertible UV and rapidity counterterms.
6. Gauge, path, Hermiticity, future/past, and rotation closure.
7. A source-aligned continuum target that was not used as input to the finite
   coefficient.
8. A true regulator trajectory with holdouts and separated remainders.
9. A finite-regulator conversion with inverse and round trip.
10. A typed, compatible soft-side zero-bin object.

The C34 outcome fails conditions 1--6 and consequently cannot reach 8--10.
Exact regression and deterministic serialization results are authoritative in
`docs/next_level/c34_regression_report.json` rather than duplicated here.

The negative-injection manifest contains 2,240 ordered, hash-verified semantic
control-state mutations spanning 80 named fault modes.  Each payload changes
one field derived from the corresponding safe baseline contract, executes the
post-mutation validator, and records the observed and expected diagnostic.
These are executed negative tests of the C34 control contracts; they mutate
isolated semantic control states, not live physics dataclasses or accepted
numerical artifacts.

## Forbidden interfaces

The C34 package intentionally exposes no API for:

- proton or deuteron TMD export;
- ART25 member access;
- bridge residual access or twelve-point bridge execution;
- fits, calibration, likelihoods, posteriors, optimization, reweighting, or
  emulation;
- process or physical-input promotion;
- production-registry mutation.

The next API that may add numerical finite-cell kernels is C35/S0C, after the
missing regulator definition in
`docs/next_level/c34_missing_calculation_specification.md` is satisfied.
