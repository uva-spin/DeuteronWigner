# ADR 205: Permit finite-basis soft conversion only after both endpoints exist

Status: accepted for C34/S0A.

## Decision

Define the finite-basis-to-continuum soft conversion as the difference between
two independently renormalized representations of the same operator.  The map
must be state, hadron, flavor, ART25-member, and gauge independent at its
declared order and must pass inverse and round-trip tests.  An absent
finite-basis endpoint produces an empty-not-zero conversion object.

## Rationale

A continuum soft expression alone defines the target, not the regulator
difference.  Taking a ratio to a proton distribution or fitting bridge points
would make a supposedly universal conversion state dependent.

## Consequences

C34 records no numerical conversion, inverse, or round-trip residual.  Every
conversion remainder class remains separately `NONZERO_UNKNOWN`.  State,
hadron, flavor, and ART25-member independence are requirements, not proved
properties of the absent one-loop kernel.

## Revision trigger

The renormalized finite-basis coefficient closes and an independent holdout
validates the forward and inverse conversion without data input.
