# ADR 210: Freeze an unavailable direct soft realization before coefficient evaluation

Status: draft; implemented as the C35/S0C fail-closed decision.

## Question

Which gauge-complete, regulator-identical finite-basis realization may be used
for the four-line `B=0` vacuum soft operator?

## Decision

Compile the covariant/Krein, light-front-physical, auxiliary-eikonal, and
unavailable candidates as mutually exclusive typed plans.  Select
`S0C-UNAVAILABLE` before evaluating any coefficient.  Record
`C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE`, Branch G, and do not
attempt the finite-basis one-loop coefficient.

The covariant candidate lacks a finite-cell BRST/Krein action and metric,
zero-mode/boundary completion, and finite-delta gauge closure.  The
light-front candidate lacks the instantaneous kernel, constrained zero modes,
residual-gauge prescription, and proved map to the covariant modified-delta
operator.  Available auxiliary-field methods define nonidentical Euclidean or
spacelike operators and lack the required endpoint and conversion proof.

## Physics basis and alternatives

The modified-delta source explicitly warns that the regulated Wilson lines do
not retain the original Wilson operator's gauge properties at finite delta.
The alternatives were to import a continuum coefficient, infer closure from
a reduced light-front benchmark, or treat another eikonal operator as
identical.  All three would change the operator and are rejected.

Classification: exact source constraint plus source-audited fail-closed
architecture decision; not a phenomenological approximation.

## Consequences

- All eighteen one-loop contributions remain `NONZERO_UNKNOWN`.
- The bare coefficient is unassigned and counterterms are not solved.
- No microscopic proton TMD or C32 continuation is reachable.
- The exact next package is C36/O4, a replacement regulator architecture.

## Affected evidence

- `src/deuteron_wigner/bridge/s0c/core.py`
- `docs/next_level/c35_gauge_complete_plan_selection.json`
- `docs/next_level/c35_no_go_decision_tree.json`
- C35 gauge-plan and coefficient-gating tests

## Revision trigger

A new versioned `B=0` root supplies a gauge-complete finite-regulator action,
operator-identical rapidity prescription or proved conversion, complete
boundary/zero-mode sectors, and passing gauge/constraint tests.
