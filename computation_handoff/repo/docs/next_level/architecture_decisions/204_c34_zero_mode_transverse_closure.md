# ADR 204: Give zero modes, endpoints, and transverse closure separate ownership

Status: accepted for C34/S0A.

## Decision

Preserve the C33 policy that exact light-front zero modes are excluded from
ordinary cells but retained as a separate control.  A missing zero-mode
calculation is never numerical zero.  Lightlike endpoints, infinity junctions,
transverse closure, cusp terms, and basis-boundary terms remain separately
identified and cannot be merged without an operator-level identity.

## Rationale

These sectors can restore Ward identities, carry regulator dependence, or
generate finite and power-divergent terms.  Their ownership is part of the
operator definition.

## Consequences

Zero-mode and closure contributions block the one-loop result.  C34 neither
drops them as numerical noise nor hides them in a generic remainder.

## Revision trigger

An explicit constrained zero-mode/boundary sector and parameterized closed
Wilson path pass gauge, regulator, and trajectory tests.
