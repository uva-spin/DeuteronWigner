# ADR 190: Exclude primary soft zero modes only with a visible unknown remainder

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The primary finite one-gluon basis excludes exact longitudinal zero modes from
its ordinary mode enumeration. It simultaneously carries an explicit
`ZERO_MODE_SEPARATE_CONTROL` identity, a frozen alternate-policy holdout, and a
`NONZERO_UNKNOWN` one-loop zero-mode remainder. Exclusion is a regulator choice,
not proof that the one-loop contribution vanishes.

The vacuum-only tree sector contains no gluon and therefore has an exact zero
tree contribution from the zero-mode ledger.

## Evidence

- The historical C32 collinear trajectory excludes gluon zero modes but marks
  sensitivity unresolved.
- C13/C14 zero-mode and gauge entries are validation fixtures, not a soft-vacuum
  calculation.
- The C33 acceptance contract forbids silent zeroing and requires an alternate
  policy control.

## Authority and status

- **Exact:** tree zero-mode contribution is zero because no tree gluon is
  present; the policy and holdout identities are frozen.
- **Finite-regulator model:** exclusion from the primary mode enumeration and
  boundary-cell definition.
- **Temporary:** alternate zero-mode control has not been evaluated.
- **Open:** one-loop zero-mode, instantaneous, and boundary contributions are
  `NONZERO_UNKNOWN` under `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Set all zero modes to zero: rejected as an unsupported omission.
- Copy the C32 collinear policy without a compatibility record: rejected because
  the soft basis is a distinct regulator.
- Include a formal zero mode with arbitrary normalization: rejected until its
  constraint and boundary prescription are derived.

## Consequences

- No continuum-trajectory, gauge, or rapidity claim may absorb the zero-mode
  remainder.
- The primary and alternate policies remain separate trajectory axes.
- C34/S0A must calculate or structurally resolve the omitted sector.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_zero_mode_policy.json`
- `docs/next_level/c33_soft_basis_manifest.json`
- `docs/next_level/c33_soft_power_correction_manifest.json`
- `docs/next_level/c33_soft_uncertainty_budget.json`
- `tests/test_c33_s0.py` silent-zero rejection and policy-holdout tests

## Revision triggers

Revise after an explicit constrained zero-mode construction, a source-qualified
proof of absence for this operator/regulator, or a completed alternate-policy
trajectory. Numerical smallness alone is not a trigger.
