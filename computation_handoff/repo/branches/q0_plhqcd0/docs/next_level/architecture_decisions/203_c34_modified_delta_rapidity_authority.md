# ADR 203: Derive modified-delta rapidity renormalization only after bare closure

Status: accepted for C34/S0A.

## Decision

Retain `delta_plus` and `delta_minus` as distinct operator regulators through
real/virtual assembly and UV separation.  Derive the rapidity counterterm,
rapidity anomalous dimension, and Collins-Soper convention only from a closed
finite-basis coefficient.  Neither zeta nor the ART25 nonperturbative kernel is
a bare rapidity regulator or an admissible substitute.

The frozen numerical probes vary one regulator at a time, including separate
one-axis holdouts.  A fixed-ratio diagonal scan is not accepted as evidence of
independent `delta_plus` and `delta_minus` dependence.  The probes are
regulator controls, not physical parameters.

## Rationale

The modified-delta signs and removal order are fixed by the Wilson paths, but
their numerical cancellation depends on the missing finite-basis graphs.
Extracting a derivative before that cancellation would turn a target-scheme
definition into a microscopic result.

## Consequences

The C34 rapidity counterterm and anomalous-dimension values remain
`NONZERO_UNKNOWN`; regulator, gauge, future/past, derivative, and cusp
residuals are unavailable (`null`), not numerical zero.  No positive
rapidity-closure status is issued.

## Revision trigger

The complete gauge-independent bare coefficient closes at independent
`delta_plus` and `delta_minus` values and its declared rapidity derivative
reproduces the source cusp relation.
