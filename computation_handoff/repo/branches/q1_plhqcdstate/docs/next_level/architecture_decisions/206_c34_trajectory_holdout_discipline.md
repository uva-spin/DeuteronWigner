# ADR 206: Require axis-resolved trajectories and pre-result holdouts

Status: accepted for C34/S0A.

## Decision

Freeze trajectory forms and holdouts before evaluating coefficients.  UV,
IR/volume, rapidity-window, transverse discretization, zero-mode, endpoint,
boundary, and quadrature axes must remain distinguishable.  The three C33
resolutions cannot support an over-parameterized log-plus-finite-plus-power
fit, particularly when a resolution is reserved as a holdout.

## Rationale

C33 changes several supports and counts simultaneously.  Treating its three
descriptors as a one-dimensional continuum sequence would confound physical
and numerical effects.

## Consequences

The C34 trajectory-fit form and holdout discipline are frozen, but no
one-loop R1--R3 sequence is executed, fitted, or audited as a physical
trajectory.  No continuum or conversion claim is inferred from the three
dimensions alone, and failed holdouts cannot be moved into construction.
Only the quadrature method family and nominal order are frozen: absent
tolerances, subdivision limits, contour/pole treatment, normalized modes, and
singular subtraction keep the execution plan explicitly incomplete.

## Revision trigger

Executable refinement maps and independently varied regulator axes, with
sufficient resolutions for the source-predicted ansatz, pass a frozen
holdout.
