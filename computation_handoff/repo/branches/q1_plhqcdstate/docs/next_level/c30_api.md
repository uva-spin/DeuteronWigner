# C30/B1 distribution-bridge API

The public contract is in `deuteron_wigner.bridge.b1.core`. Records are frozen
dataclasses with deterministic content hashes.

## Definitions and plans

- `TMDDefinitionRecord` stores complete root, operator, target, flavor, rank,
  link/color, regulator, UV, rapidity, soft, scale, Fourier, normalization,
  domain, numerical, and evidence identity.
- `BridgeSchemeId` and `BridgeSchemePlan` make direction and external/microscopic
  scheme ownership explicit.
- `CommonBridgePoint` distinguishes kinematic overlap from executable
  definition overlap.

## Finite adapter

`FiniteSchemeAdapter` requires source authority, perturbative order, inverse,
round-trip, RG, rapidity, threshold, domain, and remainder records. `convert()`
refuses execution when the expression is unavailable or unaudited. C30 ships
no numerical adapter because no qualified expression was found.

## Capability and safeguards

`DistributionBridgeCapability` reports common-domain and numerical-readiness
states separately. `detect_injection()` rejects the ordered negative controls
used by the C30 validator. The package intentionally exposes no likelihood,
optimizer, calibration, reweighting, posterior, emulator, process, or
production API.
