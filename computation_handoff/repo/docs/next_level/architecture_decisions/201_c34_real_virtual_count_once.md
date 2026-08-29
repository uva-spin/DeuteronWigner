# ADR 201: Require two-route, count-once real/virtual assembly

Status: accepted for C34/S0A.

## Decision

The authoritative one-loop soft coefficient must be reconstructed both from
the Wilson-operator vacuum contraction and from the cut one-gluon mode sum.
Every contribution is keyed by line pair, cut, mode cell, phase, and regulator
identity.  Duplicate real support, virtual support, conjugate pairs,
self-energies, cusp pieces, or inverse-soft allocations are hard failures.

C34 provides typed cut and assembly ledgers with structurally unique IDs and
candidate topology roles.  It does not infer a physical real/virtual branch
from the contribution name: every branch remains `UNRESOLVED_BLOCKING`, the
assembled branch sets are empty, and neither physical count-once closure nor
route equality is claimed while the finite-basis matrix elements are
unavailable.  Direct bare terms, the separate zero-mode control, the
nonadditive auxiliary route, and counterterms have disjoint IDs and assembly
roles.

## Rationale

The two routes expose different counting errors.  Their equality is a
physical validation, not a bookkeeping convention.

## Consequences

All one-loop equality residuals remain unavailable rather than zero.  The
continuation gate cannot pass until both routes execute and agree.

## Revision trigger

All real and virtual cell integrals execute with unique keys and the two
assemblies agree within a predeclared quadrature tolerance.
