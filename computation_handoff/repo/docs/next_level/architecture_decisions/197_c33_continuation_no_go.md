# ADR 197: Tree-only soft closure selects C34/S0A and keeps continuation closed

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The C32 collinear continuation gate passes only if the vacuum basis, four-line
operator, tree normalization, one-loop bare soft factor, UV and rapidity
renormalization, gauge independence, continuum oracle, finite-basis trajectory,
regulator conversion, soft-collinear compatibility, and zero-bin interface all
pass.

C33 constructs and audits the two-root identity, B=0 basis, four-line operator,
and exact tree soft factor, but it does not have an executable source-derived
finite-basis one-loop interaction/diagram calculation. The selected outcome is
therefore:

`C33_SOFT_TREE_LEVEL_ONLY`

The continuation gate is false, and the exact next package is:

`C34/S0A — one-loop soft diagram, counterterm, and rapidity-renormalization completion`.

## Evidence

- The available C5/C6/C12-C14 objects are validation pilots and overlap ledgers,
  not a B=0 modified-delta soft calculation.
- C32 records all one-loop soft, UV, rapidity, overlap, and trajectory values as
  unavailable.
- A continuum oracle cannot replace the missing finite-basis calculation.

## Authority and status

- **Exact:** tree value `1`, tree zero-bin `0`, gate truth table, empty-not-zero
  downstream semantics, and selected branch.
- **Source-qualified:** list of one-loop contributions and target continuum
  checks required to reopen the gate.
- **Finite-regulator model:** proposed basis resolutions and future trajectory.
- **Temporary/open:** all one-loop values and renormalization closures. Unknown
  remainders remain `NONZERO_UNKNOWN`.

## Alternatives considered

- Issue readiness from tree identity: rejected.
- Import the continuum soft function and label it finite-basis: rejected.
- Select trajectory or compatibility branches before a one-loop value exists:
  rejected because the earlier structural gate is decisive.
- Export a proton TMD or rerun the bridge: forbidden in C33.

## Consequences

- `C33_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING` is not issued.
- The microscopic proton export remains absent/empty-not-zero and all twelve
  bridge points remain common-domain-only.
- No fit, likelihood, posterior, optimization, reweighting, emulator, process
  execution, or physical status is created.
- C34/S0A receives the exact missing-calculation ledger rather than fabricated
  coefficients.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_c32_continuation_gate.json`
- `docs/next_level/c33_source_sufficiency_decision.json`
- `docs/next_level/c33_no_go_decision_tree.json`
- `docs/next_level/c33_missing_calculation_specification.md`
- `docs/next_level/c33_unresolved_physics_gaps.md`
- `tests/test_c33_s0.py` gate truth-table, tree-only branch, forbidden-status,
  empty-not-zero, and no-bridge tests
- `scripts/build_c33_manifests.py`, `scripts/validate_c33.py`

## Revision triggers

Revise only when C34/S0A completes the finite-basis one-loop bare soft factor
and every dependent UV, rapidity, gauge, trajectory, compatibility, and
zero-bin gate is rerun. Source availability without execution does not revise
this decision.
