# ADR 215: Require executable parameterization of every Wilson segment

Status: draft; implemented as a C35/S0C empty-not-zero Wilson contract.

## Question

What information must be stored before the four eikonal lines and transverse
closure can generate finite-mode vertices?

## Decision

Require every longitudinal and transverse segment to store its path map,
parameter interval, orientation, representation, color action, endpoints,
path ordering, transverse position, Fourier phase, momentum flow, regulator
action, and finite-mode coupling.  The transverse link at infinity and each
junction are mandatory operator segments rather than optional metadata.

C35 preserves the symbolic C33/C34 geometry but marks executable segment
status empty-not-zero.  It derives no physical vertex or line-pair kernel from
an incomplete segment collection.

## Physics basis and alternatives

Eikonal pole signs and endpoint terms follow from line orientation, Fourier
convention, and path ordering.  Supplying a pole sign manually, omitting the
transverse closure, or treating infinite lines as complete finite-volume
objects would change Ward and boundary contributions and is rejected.

Classification: exact operator-identity requirement; finite-mode realization
is unresolved.

## Consequences

- The symbolic current is not a numerical one-gluon matrix element.
- Cusp, endpoint, self-energy, and transverse-closure slots remain
  independently `NONZERO_UNKNOWN`.
- Full antiunitary/path/color reversal must be tested once segments exist.

## Affected evidence

- `docs/next_level/c35_wilson_segment_parameterization.json`
- `docs/next_level/c35_transverse_infinity_segment.json`
- `docs/next_level/c35_executable_eikonal_vertex.json`
- `docs/next_level/c35_line_to_pole_derivation_report.json`

## Revision trigger

A gauge-complete root provides all finite-volume segments and their mode
matrix elements, with orientation, reversal, endpoint, and transverse-junction
tests passing.
