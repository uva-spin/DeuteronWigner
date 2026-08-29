# ADR 213: Do not equate scalar cell normalization with gauge-mode completeness

Status: draft; implemented as a C35/S0C type and status boundary.

## Question

What does the normalized finite-cell prototype establish, and what additional
structure is required before it becomes a physical soft gauge mode?

## Decision

Permit a scalar top-hat prototype whose exact real-chart cell measure obeys
`measure*normalization^2=1`.  Label it
`NORMALIZED_SCALAR_CELL_PROTOTYPE_NOT_GAUGE_MODE`.  Do not use it as evidence
for Lorentz/polarization completeness, a Krein metric, physical commutators,
ghost or auxiliary modes, light-front constraints, zero modes, boundary
modes, or a partition of unity.

The R1--R3 dimensions 3,841, 30,721, and 103,681 remain support descriptors,
not materialized mode arrays.

## Physics basis and alternatives

A scalar `L2` normalization fixes only a measure convention.  Gauge fields
require a selected action and its metric or constraint structure.  Assigning
polarizations after scalar integration or assuming that a mode count proves
completeness would hide the central missing physics and is rejected.

Classification: exact normalization oracle plus a field-theoretic
completeness requirement.

## Consequences

- The scalar normalization test may pass while the gauge-mode gate remains
  false.
- No one-gluon vertex or coefficient may consume the prototype as a physical
  mode.
- C36/O4 must define complete boundaries, modes, metrics/commutators, weights,
  partitions, zero modes, and boundary sectors.

## Affected evidence

- `SoftCellBoundary`, `SoftCellPrototype`, and `real_cell_prototype`
- `docs/next_level/c35_soft_mode_normalization_report.json`
- `docs/next_level/c35_soft_mode_collection_manifest.json`
- scalar-normalization and mode-completeness negative controls

## Revision trigger

A selected gauge-complete action supplies and validates normalized finite
modes and their full completeness or constraint identities on nested grids.
