# ADR 200: Do not transfer continuum scalelessness to the finite regulator

Status: accepted for C34/S0A.

## Decision

A contribution that vanishes as a scaleless integral in dimensional
regularization is not assigned zero in the C33 finite basis without an
operator- and regulator-specific calculation.  Its C34 status remains
`UNRESOLVED_BLOCKING`, or
`TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO` only after the finite result is
actually obtained.  Exact zeros require an algebraic proof recorded with the
same operator and regulator identity.

## Rationale

Finite cutoffs can turn a continuum scaleless graph into a logarithm, power
divergence, line-mass term, boundary term, or finite conversion coefficient.
Copying a dimensional-regularization zero would hide precisely the regulator
matching C34 is intended to determine.

## Consequences

The continuum target remains a comparison oracle.  It cannot populate the
finite-basis diagram ledger, counterterm solution, or conversion kernel.

## Revision trigger

The corresponding finite-cell graph and subtraction are evaluated with a
declared measure, action, boundary prescription, and regulator trajectory.
