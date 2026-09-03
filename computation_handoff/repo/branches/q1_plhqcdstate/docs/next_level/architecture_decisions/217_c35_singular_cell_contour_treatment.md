# ADR 217: Forbid center sampling across singular cells

Status: draft; implemented as a C35/S0C analytic-method oracle.

## Question

How must a finite cell intersecting an eikonal or propagator pole be treated?

## Decision

Require an explicit principal-value plus cut, contour deformation, sector
partition, or analytic subtraction.  Store the pole location, prescription,
orientation-derived sign, cell partition, and recombination rule.  Center
sampling with a numerical epsilon is forbidden.

C35 implements analytic prototype identities for
`1/(x-i0)=PV(1/x)+i*pi*delta(x)` and finite-delta logarithms.  It records
`physical_cells_executed=0`; neither oracle is presented as a physical
finite-basis integration or virtual contour.

## Physics basis and alternatives

Singular distributions are defined by their prescription, not by a value at
the bin center.  Center sampling can select the wrong sign, miss the cut, and
make results grid dependent.  A fixed numerical epsilon has no status as a
physical rapidity or causal regulator.

Classification: exact distributional constraint and numerical-method rule;
physical cell execution remains unresolved.

## Consequences

- Pole signs remain tied to complete Wilson paths and Fourier convention.
- Virtual contours must be proved not to cross poles silently.
- Real and virtual singular pieces cannot be assembled before materialized
  modes, cells, and the selected action exist.

## Affected evidence

- `SingularCellOracle`
- `docs/next_level/c35_pole_cell_partition.json`
- `docs/next_level/c35_singular_cell_subtraction_report.json`
- `docs/next_level/c35_virtual_contour_report.json`

## Revision trigger

The replacement regulator executes physical singular cells with independently
validated prescriptions, refinement convergence, and correct cut/imaginary
parts.
