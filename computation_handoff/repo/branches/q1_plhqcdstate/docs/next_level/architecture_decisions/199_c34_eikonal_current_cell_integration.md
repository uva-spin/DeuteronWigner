# ADR 199: Separate the stored symbolic eikonal-current identity from numerical cell matrix elements

Status: accepted for C34/S0A.

## Decision

Represent the four-line one-gluon current as a content-addressed symbolic
descendant of the immutable C33 operator.  Each term retains its line, color
action, ordering, orientation, transverse position, Fourier phase, momentum
flow, modified-delta component, and derived pole sign.  A numerical
one-gluon matrix element additionally requires an explicit normalized mode
function, cell domain, measure, polarization vector, and quadrature rule.

C34 records a typed symbolic current identity derived from the stored C33
lines and freezes the proposed cell-integration contract.  This is not a
validation of a gauge-complete physical current, a Ward-identity closure, or a
finite-basis matrix element: the C33 basis descriptors do not supply the
required numerical ingredients.  A cell that contains a pole must eventually
be integrated or analytically subtracted; sampling its center and adding an
epsilon is rejected.

## Rationale

The Wilson expansion fixes the current's algebraic identity, but a list of
mode counts and support bounds does not fix a Hilbert-space realization.
Keeping those statements separate prevents basis normalization and regulator
choices from being hidden in an apparently harmless numerical current.

## Consequences

- The symbolic four-line current schema is available as an input to C35/S0C;
  its physical cell matrix elements remain unexecuted.
- Physical cell amplitudes remain `NONZERO_UNKNOWN` and blocking.
- No numerical epsilon or singular-cell center prescription is permitted.
- C33 paths and tree normalization remain unchanged.

## Revision trigger

An explicit gauge-complete mode basis, cell map, measure, normalization, and
quadrature implementation passes completeness and refinement tests.
