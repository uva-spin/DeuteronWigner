# ADR 208: Select Branch G at the first unresolved one-loop dependency

Status: accepted for C34/S0A.

## Decision

C34 selects `C34_SOFT_ONE_LOOP_INCOMPLETE` and Branch G.  The exact next
package is `C35/S0C — targeted unresolved soft-diagram and counterterm
completion`.  This is the first failing dependency: the C33 descriptors do not
define a gauge-complete B=0 action, normalized cell basis, propagator and cut
measure, Wilson-segment discretization, zero-mode sector, or finite-regulator
renormalization conditions.

Secondary rapidity, gauge, zero-mode, trajectory, conversion, and
soft-collinear gates remain unresolved, but they do not replace the primary
diagnosis.  The C32 continuation gate remains false.

## Alternatives rejected

- Copying the continuum coefficient into the finite basis.
- Calling uncalculated finite-regulator graphs scaleless.
- Fitting counterterms or conversion constants to ART25 or bridge data.
- Treating the exact tree identity or a structural ledger as one-loop closure.

## Consequences

No proton TMD export, bridge rerun, fit, likelihood, inference, process
promotion, deuteron prediction, or production route is created.

## Revision trigger

C35/S0C supplies and validates every missing regulator-specific input and all
eighteen required contribution/counterterm statuses cease to be blocking.
