# ADR 219: Solve counterterms only after the bare finite-basis coefficient

Status: draft; implemented as a C35/S0C dependency invariant.

## Question

Can continuum anomalous dimensions or target-scheme expressions be used to
fill finite-basis UV, rapidity, or line-mass counterterms before the bare
calculation exists?

## Decision

No.  First resolve all eighteen regulator-specific contribution classes and
assemble the bare finite-basis coefficient.  Only then extract and solve the
UV, rapidity, and residual-line-mass counterterms in the same regulator.  C35
has no bare coefficient, so all three counterterms remain empty-not-zero and
no renormalized result is defined.

The continuum modified-delta expression may serve later as a separately
sourced target oracle.  It cannot be copied into the bare result or inverted
to manufacture regulator-specific counterterms.

## Physics basis and alternatives

Counterterms cancel divergences of a particular regulated operator.  Without
that operator's graph sum, finite-cell power terms, boundary terms, operator
mixing, and rapidity structure are unknown.  Inferring them from ART25,
bridge residuals, a hadron-level ratio, or a target continuum coefficient
would be a fit or scheme substitution rather than microscopic matching.

Classification: exact renormalization ordering requirement.

## Consequences

- `SoftCountertermSystem` rejects populated counterterms when the bare
  coefficient is unavailable.
- There is no C35 rapidity anomalous dimension, cusp residual, conversion, or
  round trip.
- Counterterm state and hadron independence remain required but unproved.

## Affected evidence

- `SoftBareOneLoopResult` and `SoftCountertermSystem`
- `docs/next_level/c35_bare_soft_coefficient.json`
- `docs/next_level/c35_soft_counterterm_results.json`
- `docs/next_level/c35_soft_renormalization_closure.json`

## Revision trigger

A new regulator root supplies a complete, independently validated bare graph
sum from which all counterterms and anomalous dimensions are solved and pass
RG, rapidity, gauge, threshold, and universality tests.
