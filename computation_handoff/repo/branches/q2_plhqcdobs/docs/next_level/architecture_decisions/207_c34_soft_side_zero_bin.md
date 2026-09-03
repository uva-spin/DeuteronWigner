# ADR 207: Define the soft-side zero-bin object without assuming equality

Status: accepted for C34/S0A.

## Decision

Create a typed soft-side limit carrying the C32 measurement, transverse
coordinate, UV target, gauge convention, rapidity convention, off-shell IR
identity, and regulator-removal order.  Citation-level soft/zero-bin
equivalence is not sufficient for the frozen off-shell finite-basis pair.
Only a later operator-identical collinear calculation can test equality and
count the overlap once.

## Rationale

The soft factor and collinear zero-bin live in disjoint B=0 and B=1 roots and
use incompletely matched regulator realizations.  A typed interface exposes
the comparison without prejudging it.

## Consequences

The C34 object is defined but not numerically ready.  The C32 continuation
gate stays false and no completed TMD is claimed.

## Revision trigger

The C34 soft-side limit and C35 collinear zero-bin execute with identical or
explicitly converted operator/regulator identities and pass the signed
missing/duplicate-overlap tests.
