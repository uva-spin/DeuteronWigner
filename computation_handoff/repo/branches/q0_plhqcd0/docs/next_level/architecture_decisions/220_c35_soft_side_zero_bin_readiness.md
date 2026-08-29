# ADR 220: Keep the C32 soft-side zero-bin interface closed

Status: draft; implemented as the C35/S0C continuation gate.

## Question

Does the C35 soft information suffice to construct the soft overlap required
by the frozen C32 collinear operator?

## Decision

No.  Export `SOFT_LIMIT_C35` as empty-not-zero and set the C32 continuation
gate false.  Require equality or an executed conversion across operator
identity, gauge, partonic IR prescription, rapidity regulator, basis and
continuum maps, Wilson geometry, pole prescriptions, scale, and perturbative
order before a soft-side object can be subtracted exactly once.

Do not infer the zero-bin from a continuum citation, from formal small-soft
power counting, or from the C32 collinear calculation alone.  The historical
C32 exact tree reduction remains unchanged and is not promoted to a
renormalized TMD.

## Physics basis and alternatives

The zero-bin/overlap is an operator-level equality in compatible regulators.
Using a nonidentical soft function can leave double counting or subtract the
wrong IR content.  A missing overlap is not numerically zero.

Classification: exact matching and count-once requirement; C35 result is
empty-not-zero.

## Consequences

- No microscopic `u`, `d`, `ubar`, or `dbar` proton TMD is exported.
- The twelve-point bridge is not rerun.
- A later soft result must remain separate from the `B=1` proton state and
  preserve C32's frozen identity.

## Affected evidence

- `docs/next_level/c35_soft_side_zero_bin_limit.json`
- `docs/next_level/c35_soft_collinear_continuation_contract.json`
- `docs/next_level/c35_c32_continuation_gate.json`
- overlap-identity, count-once, and scope-leakage tests

## Revision trigger

C36 or a later package produces a nonempty regulator-specific soft limit and
passes the complete operator-identity and conversion contract against C32.
