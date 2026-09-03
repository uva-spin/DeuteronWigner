# ADR 218: Keep zero-mode and boundary sectors explicit and separately owned

Status: draft; implemented as a C35/S0C unresolved-physics ledger.

## Question

May zero modes, basis boundaries, endpoints, cusps, or the transverse link be
discarded under the inherited finite-basis policy?

## Decision

No.  Preserve the historical zero-mode policy
`EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL / AUDIT_REQUIRED`, but interpret it
as an unresolved control sector, not a zero theorem.  Keep zero-mode,
basis-boundary, cusp/endpoint, and transverse-closure contributions in
separate count-once slots with value `NONZERO_UNKNOWN`.

A contribution may become zero only through an exact identity in the selected
finite-regulator action.  A cancellation must identify both calculated
partners.  Dimensional-regularization scalelessness does not prove a
finite-cell boundary or power contribution vanishes.

## Physics basis and alternatives

Light-front zero modes and finite-support boundaries can carry constraints,
residual gauge transformations, line energy, rapidity dependence, and
transverse-junction information.  Silently absorbing them into a bulk graph
or dropping them because they disappear in a different regulator risks Ward
failure and double counting.

Classification: exact provenance/ownership rule; numerical values remain
unconstrained and blocking.

## Consequences

- Four dedicated ledger classes remain unresolved.
- Excluding the primary zero-mode sector cannot open the one-loop or C32
  continuation gate.
- C36/O4 must calculate these sectors or prove non-applicability from its
  selected action.

## Affected evidence

- `docs/next_level/c35_zero_mode_sector.json`
- `docs/next_level/c35_zero_mode_closure_report.json`
- `docs/next_level/c35_boundary_endpoint_report.json`
- `docs/next_level/c35_contribution_closure_matrix.json`

## Revision trigger

A gauge-complete replacement root provides explicit zero/boundary modes and
passes Ward/constraint, rapidity, line-energy, endpoint, transverse-closure,
and count-once tests on nested trajectories.
