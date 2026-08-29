# C29/B0 bridge API

The public contract is in `deuteron_wigner.bridge.b0.core`. All records are
frozen dataclasses with deterministic content hashes.

## Roots and identities

- `ExternalRootId`, `MicroscopicRootId`, and `BridgeRootPairId` enforce the two
  disjoint provenance roots.
- `BridgeOperatorId` requires complete species, flavor, polarization, target,
  rank, link, color, twist, scheme, scale, and domain identity.
- `require_complete_match()` rejects any mismatch; array shape or TMD name is
  never a matching rule.
- target, partner, observable, measurement, scheme, scale, rank, link, color,
  threshold, and domain records preserve their separate responsibilities.

## Members and covariance

- `BridgeMemberRelation` defaults to `NO_JOINT_MEASURE` and rejects index
  pairing.
- `covariance_pushforward(A, B)` returns `A @ B.T` and its exact factor
  covariance, with no regularization.
- `nonlinear_memberwise()` evaluates every source member and empirically
  recenters the mapped ensemble.
- `rank_aware_diagnostic()` whitens only the nonzero covariance eigenspace and
  reports the null-space residual separately.

## Scientific safeguards

`BridgeDiscrepancyComponent` rejects an unknown discrepancy labeled as zero.
`FutureInferencePrerequisiteContract` cannot auto-qualify inference.
`BridgePlan` and `BridgeCapabilityEntry` carry both roots, member relation,
ancestry, role, discrepancy, and fail-closed status.

There is intentionally no inference API, optimizer, reweighter, likelihood,
posterior, emulator, or production-registry integration.
