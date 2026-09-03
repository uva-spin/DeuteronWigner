# ADR 194: Compatibility requires an explicit C32-to-C33 regulator pair

Status: accepted for the fail-closed C33/S0 completion.

## Decision

C32 collinear and C33 soft regulators are paired by an immutable compatibility
record. It compares gauge group, parton representation, Wilson directions,
transverse coordinate and measurement, Fourier convention, rapidity
prescription, UV target, IR treatment where applicable, boundary conditions,
regulator-removal order, and soft-limit definition.

Shared labels establish only metadata compatibility. Because the C33 one-loop
soft action and the C32 one-loop collinear soft limit are both unavailable, the
pair remains `SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED` and cannot open the
continuation gate.

## Evidence

- C32 freezes a three-point `K/Nmax/bHO` collinear trajectory and modified-delta
  plan while explicitly treating its UV/IR scales as diagnostic.
- C33 uses a distinct B=0 mode basis and zero-mode policy.
- A common rapidity name does not prove equality of finite regulators or
  overlap measurements.

## Authority and status

- **Exact:** immutable identities of the C32 and C33 records and comparison
  fields.
- **Source-qualified:** conditions required for soft-collinear factorization.
- **Finite-regulator model:** any proposed conversion between their basis
  cutoffs and boundary cells.
- **Temporary/open:** the one-loop compatibility map and regulator conversion.

## Alternatives considered

- Declare the regulators identical because both say modified-delta: rejected.
- Copy C32 fixed total `K` into the soft root: rejected.
- Treat a valid standalone soft factor as a complete TMD: rejected.

## Consequences

- `C33_SOFT_COLLINEAR_COMPATIBILITY_VALIDATED` is not issued.
- Compatibility remainder remains separate from soft and collinear remainders.
- The C32 tree identity remains untouched and no collinear coefficient is
  fabricated.
- The package remains `C33_SOFT_TREE_LEVEL_ONLY`; C34/S0A is next.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_collinear_regulator_pair.json`
- `docs/next_level/c33_soft_collinear_compatibility_report.json`
- `docs/next_level/c33_two_root_tmd_identity.json`
- `tests/test_c33_s0.py` field-by-field compatibility and premature-identical-
  status rejection tests

## Revision triggers

Revise when C34/S0A or C34/R0B evaluates both sides with the stored measurement
and proves identity or a finite conversion at the declared order. Matching
labels alone do not qualify.
