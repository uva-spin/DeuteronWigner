# ADR 195: Define zero-bin ownership without fabricating collinear matching

Status: accepted for the fail-closed C33/S0 completion.

## Decision

C33 defines the typed interface
`ZERO_BIN: COLL_C32 -> SOFT_LIMIT_C33` and preserves C32's ordering: subtract
the overlap exactly once before inverse-square-root soft allocation. The
contract stores source and target regulator IDs, measurement, momentum scaling,
boundary and zero-mode rules, subtraction owner, and regulator-removal order.

At tree level the zero-bin contribution is exactly zero. At one loop only the
interface is defined; no collinear coefficient, numerical subtraction, or
validated zero-bin status is claimed.

## Evidence

- C5/C6 provide count-once ledger patterns but not the required regulator-level
  map.
- C32 stores the placement and tree zero while marking its one-loop overlap
  unavailable.
- The C32 microscopic collinear one-loop correlator lies outside C33 scope.

## Authority and status

- **Exact:** tree zero, subtraction ordering, and single-owner contract.
- **Source-qualified:** soft-limit/zero-bin count-once theorem.
- **Finite-regulator model:** concrete C32-to-C33 mode-scaling map.
- **Temporary/open:** one-loop image, residual, and cancellation; therefore
  `C33_ZERO_BIN_INTERFACE_VALIDATED` is not issued.

## Alternatives considered

- Omit the zero-bin because the soft factor is separate: rejected.
- Subtract both a zero-bin and the same half-soft region: rejected as double
  counting.
- Fill the interface with a continuum collinear coefficient: rejected because
  C32's finite regulator has not been calculated.

## Consequences

- The interface can be consumed by C34/R0B without changing C32 history.
- Missing and duplicate overlap controls remain signed and visible.
- No TMD export or bridge rerun follows from an interface definition alone.
- The package remains `C33_SOFT_TREE_LEVEL_ONLY`; C34/S0A is next.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_zero_bin_interface_contract.json`
- `docs/next_level/c33_soft_dependency_graph.json`
- `docs/next_level/c33_c32_continuation_gate.json`
- `tests/test_c33_s0.py` count-once, ownership, tree-zero, and premature-
  matching rejection tests

## Revision triggers

Revise after the finite-regulator collinear soft limit is explicitly calculated
and compared with the C33 soft limit, including zero modes and boundary terms.
