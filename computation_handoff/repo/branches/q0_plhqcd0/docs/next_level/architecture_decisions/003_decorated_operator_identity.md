# ADR-003: Fully decorated operator identity

Status: proposed for C1

Decision: an operator identity includes species/flavor, Dirac or Lorentz
projection, initial/final momentum fibers, Wilson path, color representation,
gluon link pair and `f/d` class where applicable, cusp/closure, UV and
rapidity regulators, renormalization and soft schemes, `mu`, `zeta`,
transverse rank, and mass-normalization convention.

No physics-bearing field receives a silent default. Incomplete imported
records use an explicit non-composable `Unknown`.

Rationale: these decorations define the operator, not optional metadata.
Today they are split among correlators, registry entries, scheme records,
provenance and unconstrained CSV labels.

Consequence: serialization versioning is required. Legacy adapters must supply
identity from existing authoritative labels and fail when the information is
not present; they may not guess.
