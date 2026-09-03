# C33/S0 API

## Runtime module

`deuteron_wigner.bridge.s0.core`, implemented at
`src/deuteron_wigner/bridge/s0/core.py`, is the typed C33 contract. The package
`deuteron_wigner.bridge.s0` re-exports that surface. All scientific records are
frozen dataclasses with canonical JSON serialization and SHA-256 content
identity.

The module exposes these fixed root and unknown-value identities:

```text
C32_COLLINEAR_ROOT = C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION
C33_SOFT_ROOT      = C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT
NONZERO_UNKNOWN    = NONZERO_UNKNOWN
```

`deterministic_json()` rejects non-finite floating values and canonicalizes
dataclasses, enums, fractions, mappings, and sequences. `content_hash()` hashes
that canonical byte representation. Each content-addressed record also exposes
`.deterministic_json` and `.content_hash` properties.

## Status types

`SoftSectorPlan` distinguishes the direct Fock, auxiliary, continuum-oracle,
and unavailable routes. `ContributionStatus` distinguishes exact tree,
calculated, calculation-required, structurally unresolved,
not-applicable-with-proof, and source-oracle-only values.

`CompatibilityStatus` provides the five allowed soft-collinear decisions,
including `SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED`.
`TrajectoryStatus` provides the resolved, logarithmic-only, finite-basis-only,
nonuniversal, and unavailable trajectory decisions.

## Root and basis records

`SoftRootId`, `VacuumHilbertId`, `VacuumStateId`, and `VacuumSectorPlan`
enforce B=0, unit vacuum normalization, frozen plan selection, state
independence, and the prohibition on shared proton state or probability
normalization. ART25 members, process data, and bridge residuals are rejected
as plan inputs.

`SoftBasisId`, `SoftBasisResolution`, `SoftMomentumMode`, `SoftGluonMode`,
`SoftZeroModePolicy`, `SoftBoundaryCondition`, and
`SoftContinuumTrajectory` describe the vacuum-plus-one-gluon basis. Momentum
modes must declare `n` or `nbar`, boundary and zero-mode status; gluon modes
must retain polarization, adjoint color, and positive normalization. Exact
zero modes are excluded from the ordinary cells but remain an explicit
`NONZERO_UNKNOWN` separate control and holdout. A
trajectory requires at least three strictly nested resolutions and declared
analytic log/finite/power structures. The runtime envelope has cell tuples
`(4,6,5)`, `(8,12,10)`, and `(12,18,15)`, corresponding to exact
vacuum-plus-one-gluon dimensions 3,841, 30,721, and 103,681 after including two
rapidity regions, two transverse polarizations, and eight adjoint colors. These
are structural dimensions, not calculated one-loop samples.

## Eikonal operator and regulators

`EikonalSourceId`, `EikonalDirection`, `EikonalColorSpace`,
`EikonalAuxiliaryField`, `EikonalPathOperator`, and `FourLineSoftOperator`
represent four independently ordered fundamental/conjugate lines, transverse
closure, the singlet trace, and the auxiliary-method oracle. The quark color
space fixes `N_c=3`, `C_F=4/3`, and `1/N_c` trace normalization.
`FourLineSoftOperator.tree_level_soft_factor` returns the exact fraction one.

`SoftRapidityRegulator.derive_denominator()` constructs an
`EikonalDenominator` from stored orientation, Fourier, momentum-flow,
covariant-derivative, line-conjugation, and modified-delta conventions. It does
not accept hand-entered pole signs. `SoftUVRegulator`, `SoftIRRegulator`,
`SoftMeasurement`, and `SoftFourierConvention` retain the remaining regulator
and b-space identities. A finite basis cannot be labeled a rapidity regulator.

## One-loop, renormalization, and oracle records

`BareSoftFactor` requires the exact tree value one and gives a positive
`.one_loop_calculated` property only for a genuinely calculated expression.
The component records are `SoftVirtualContribution`, `SoftRealContribution`,
`SoftSelfEnergyContribution`, `SoftCuspEndpointContribution`,
`SoftTransverseClosureContribution`, `SoftInstantaneousContribution`, and
`SoftZeroModeContribution`.

`SoftUVCounterterm`, `SoftRapidityCounterterm`, `RenormalizedSoftFactor`,
`SoftRapidityAnomalousDimension`, and `SoftCollinsSoperKernel` expose
`.validated` only when their required calculation, source convention,
state/basis independence, and zero residuals exist. An unresolved expression
must be exactly `NONZERO_UNKNOWN`; it cannot be serialized as zero.

`SoftContinuumOracle` requires two independent routes and rejects promotion to
a finite-basis result. `SoftAuxiliaryFieldOracle` rejects addition of the
auxiliary and direct routes. `SoftRegulatorMatching`,
`SoftRegulatorRemainder`, and `SoftBasisTrajectoryReport` keep conversion,
inverse/round-trip, omitted order, and log/finite/power claims explicit.

## Compatibility and continuation records

`SoftCollinearRegulatorPair` preserves the distinct C32 B=1 and C33 B=0
roots. `SoftCollinearCompatibilityMap` can validate only an identical,
exact-conversion, or declared-order-compatible pair whose checks all pass.

`SoftCollinearOverlapInterface` types
`COLL_C32 -> SOFT_LIMIT_C33` and records measurement identity, count-once
semantics, and whether C32 one-loop coefficients exist.
`ZeroBinCompatibilityGate`, `OneLoopSoftGate`, and `C33ContinuationGate`
compose the required booleans without fallback. `C33ClosureReport` rejects a
premature continuation, a C33 proton export, or a C33 bridge rerun.

`SoftTensorNetworkPlan` is a deterministic truncation interface, not a
statistical ensemble. `C33SoftCapabilityMatrix` is a capability record, not a
production-readiness claim.

## Factories and audit catalogs

`default_soft_root()` returns the versioned B=0 root.
`default_four_line_operator()` constructs the ordered four-line quark soft
operator. `architecture_examples()` creates one deterministic, deliberately
non-promoted example of each architecture record, including three structural
resolutions and the exact tree/no-go closure.

`fail_closed_one_loop_ledger()` returns every required one-loop contribution
with blocking status and `NONZERO_UNKNOWN`. `REQUIRED_ONE_LOOP_CONTRIBUTIONS`
and `SOFT_REMAINDER_CLASSES` are the authoritative audit catalogs.

`injection_rows()` and `detect_injection()` provide deterministic negative
controls; unknown, malformed, out-of-range, or wrong-cycle IDs fail closed.
Final regenerated injection and aggregate test counts are recorded by the
builder, not asserted in this narrative API.

## Consumers and exclusions

`tests/test_c33_s0.py` is the direct contract suite.
`scripts/build_c33_manifests.py` serializes the records into deterministic C33
artifacts. `scripts/validate_c33.py` checks those artifacts and preserved
baseline identities.

There is intentionally no API for a microscopic proton TMD export, twelve-point
bridge rerun, ART25 fitting, calibration, likelihood, posterior, optimization,
reweighting, emulator training, process bridge, or production promotion.
