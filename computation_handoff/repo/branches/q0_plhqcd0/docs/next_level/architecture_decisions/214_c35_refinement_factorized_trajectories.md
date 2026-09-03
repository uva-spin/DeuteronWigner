# ADR 214: Require factorized, held-out regulator trajectories

Status: draft; implemented as a C35/S0C unavailable trajectory contract.

## Question

How must finite-basis convergence be organized before a continuum soft result
can be claimed?

## Decision

Track UV extent, IR extent, rapidity window, rapidity-cell size, transverse
extent, transverse-cell size, zero-mode cutoff, line-length cutoff, and
quadrature order as separate axes.  Freeze training and held-out points before
evaluating results, use at least three nested points for every claimed limit,
and test the soft coefficient and all Ward/constraint, anomalous-dimension,
boundary, zero-mode, and conversion residuals.

C35 types all nine axes but evaluates no points because no gauge-complete
regulator exists.  It therefore claims no trajectory, conversion, round trip,
continuum limit, or uncertainty estimate.

## Physics basis and alternatives

Different regulator limits need not commute, and energy convergence does not
imply convergence of a nonlocal Wilson operator.  A single composite cutoff,
one- or two-point trend, or tuning on held-out points cannot identify the
individual discrepancies and is rejected.

Classification: numerical-analysis and regulator-separation requirement;
C35 status is empty-not-zero.

## Consequences

- The inherited R1--R3 dimensions do not constitute a continuum trajectory.
- Unknown trajectory discrepancy cannot be set to zero.
- C36/O4 must record refinement maps and order-of-limits diagnostics.

## Affected evidence

- `docs/next_level/c35_factorized_regulator_grid.json`
- `docs/next_level/c35_refinement_map_manifest.json`
- `docs/next_level/c35_soft_trajectory_report.json`
- `docs/next_level/c35_holdout_report.json`

## Revision trigger

A new regulator root executes pre-frozen nested trajectories with enough
independent variation to identify every claimed limit and passes held-out
observable-level convergence tests.
