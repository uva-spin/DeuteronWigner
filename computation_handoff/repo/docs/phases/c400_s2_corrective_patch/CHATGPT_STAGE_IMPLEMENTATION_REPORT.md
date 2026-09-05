# C400.S2 ChatGPT Corrective Implementation Report

## Result

`CHATGPT_CORRECTIVE_PATCH_READY_FOR_CODEX_LIVE_INTEGRATION`

This patch is built against the self-contained C400.P1C replay.  It does not merge or alter the live repository.  Historical P1, P1B, and P1C artifacts remain immutable.

## Implemented components

1. **Truthful status layer** — narrows P1C's overbroad forward-map wording to a C144 diagnostic smoke path and an incomplete C396 19-coordinate binding.
2. **C396 binding ledger** — 57 source-faithful rows over K9/K11/K13, with no C144 proxies, no zero fill, and an exact missing-object field for every non-executable direction.
3. **Versioned C144 derivative adapter** — follows the polynomial actually evaluated by the public C144 operator without rewriting historical C144 roots.
4. **Sector-qualified state interface** — distinguishes unprojected diagnostic eigenpairs from numerically projected sector states.
5. **Corrected tracker** — sector-exact assignment, complete-objective ambiguity, surplus preservation, disjoint degeneracy components, rectangular subspace projectors, and Procrustes alignment.
6. **Canonical LF/LPS comparison** — validates route-local conventions, then compares dimensionless `GC`, `GM`, and `GQ` at common invariant kinematics and state identity.
7. **Semantic replay** — compares eigenvalues, residuals, overlaps, principal angles, projectors, and actual dependency exceptions; raw vector hashes are incidental only.
8. **Evidence generator** — creates only versioned C400.S2 records under `docs/phases/c400_s2_corrective_patch`; the generation summary excludes its own prior copy from the artifact hash list, and dependency messages are checkout-path independent.

## Numerical and structural results

- C396 binding rows: **57**.
- Complete C396 numerical apply paths: **0**.
- C144 derivative audit rows: **33**.
- Corrected C144 derivatives verified: **33/33**.
- Historical mismatches: **6**, namely `phi_coupling` and `eta_2` at K9/K11/K13.
- Numerically unbound fixture coordinates: `eta_3`–`eta_8` at every resolution.
- K9 smoke matrix: **1350 × 1350**, sparse, nonphysical.
- State identity: **UNPROJECTED_DIAGNOSTIC_EIGENPAIR** unless a numerical projector is supplied.
- Semantic replay fixture: **pass**, with phase/subspace invariance and exact dependency-path comparison.
- Physical fit/rank/current selection/activation: **not performed**.

## Tests

Executed:

```text
PYTHONPATH=src pytest -q \
  tests/test_c400_p1_mechanical_closure.py \
  tests/test_c400_p1b_autonomous.py \
  tests/test_c400_p1c.py \
  tests/test_c400_s2_corrective.py
```

Result:

```text
43 passed in 24.03 seconds
```

Compilation of the new package, generator, and test file also passed.

A fresh-checkout patch application regenerated all 16 non-summary evidence artifacts byte-for-byte identically.  The generated exception message is checkout-path independent, and `generation_result.json` excludes itself from its artifact list.

## Integration status

The patch is ready for one narrow Codex integration run in the live isolated worktree.  Codex is not authorized to redesign algorithms, choose scientific behavior, merge, push, fit, report physical rank, select a current prescription, or activate the Hamiltonian.
