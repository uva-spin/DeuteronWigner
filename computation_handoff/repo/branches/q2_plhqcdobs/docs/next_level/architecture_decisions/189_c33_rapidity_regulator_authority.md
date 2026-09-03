# ADR 189: Modified-delta authority is explicit and separate from basis truncation

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The C33 soft rapidity convention is the source-qualified modified-delta
regulator frozen by C32. Every eikonal denominator must derive its `delta+` or
`delta-`, momentum flow, Fourier sign, line orientation, conjugation, and `i0`
from stored line metadata. A finite mode cutoff, rapidity window, numerical
epsilon, or Collins-Soper scale is not the bare rapidity regulator.

At tree level the rapidity regulator is inactive. C33 records the denominator
contract but does not claim one-loop implementation or cancellation.

## Evidence

- C5 derives an orientation-dependent `i0` sign but implements no
  modified-delta shift.
- C6's `L_RAP` benchmark has `physical_scheme=NOT_ASSIGNED`.
- C32 explicitly freezes modified-delta and says the microscopic vacuum
  realization is unavailable.
- The audited continuum papers are target authorities, not finite-basis
  calculations.

## Authority and status

- **Exact:** convention tuple, distinct `delta+`/`delta-` identities, derived
  conjugation/reversal rules, and regulator-inactive tree value.
- **Source-qualified:** continuum modified-delta denominator and regulator-
  removal structure.
- **Finite-regulator model:** rapidity-cell truncation used to represent modes.
- **Temporary/open:** one-loop regulated sums and rapidity counterterm. They
  remain unavailable in `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Reuse `DELTA_ANALYTIC` from C5/C12: rejected because it is an identity string
  plus `i0`, not modified-delta dynamics.
- Identify finite basis with rapidity regulation: rejected.
- Fit a rapidity coefficient or CS kernel: forbidden.

## Consequences

- Future/past equality at tree level is exact; one-loop equality requires the
  full regulated calculation.
- No physical numerical epsilon enters support.
- Rapidity-renormalization and continuation gates remain closed.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_rapidity_regulator_manifest.json`
- `docs/next_level/c33_eikonal_denominator_report.json`
- `docs/next_level/c33_continuum_soft_oracle.json`
- `tests/test_c33_s0.py` derived-sign, conjugation, distinct-delta, and
  basis-not-rapidity tests

## Revision triggers

Revise when a source-audited modified-delta one-loop implementation closes for
all four lines and regulator removal, or when C32's target rapidity convention
is replaced through an exact conversion. C34/S0A owns the current completion.
