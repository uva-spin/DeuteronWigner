# C401 merge-readiness checklist

## Required source behavior

- [x] Exact K9/K11/K13 C45/C47 fractions are used.
- [x] C128/C112 direct-sum dimensions and q-followed-by-qg order are preserved.
- [x] `D_mu_q_sq` and `D_delta_mu_g_sq` exist as COO, CSR, LinearOperator, and matrix-free actions.
- [x] No C144 diagnostic value rule is imported.
- [x] Historical C128 is not edited.
- [x] Vacuum, boundary, and truncation labels are not materialized as fake matrices.
- [x] No physical mass/counterterm value is selected.
- [x] No physical rank, convergence, state, current, or activation claim is made.

## Required validation

- [x] C401 focused suite: 14 passed.
- [x] C128 and selected C47 source regression: 4 passed.
- [x] Accepted C400.S2 regression: 26 passed.
- [x] Total selected acceptance surface: 44 passed, 0 failed.
- [x] Python compilation passes.
- [x] Two clean external evidence builds are byte-identical.
- [x] `generation_result.json` excludes itself from its package root.

## Live-repository integration gates

- [ ] Package manifest and patch hash verified on the live machine.
- [ ] `git apply --check` passes against the intended C401 worktree.
- [ ] Any local source drift is reported rather than scientifically reinterpreted.
- [ ] Exact 44-test acceptance surface passes under the live project environment.
- [ ] Evidence is regenerated from the live source and its declared invariants match.
- [ ] Broader relevant regression is run and pre-existing dependency failures are separated.
- [ ] Only C401 source, tests, tool, and phase evidence are staged.
- [ ] Local phase commit created; no merge or push performed automatically.

## Commit boundary

The commit may claim only the first six K-local numerical C396 coordinate-operator apply
paths.  It may not claim a complete C396 Hamiltonian, a sector-qualified deuteron state, a
physical fit, physical rank, resolution convergence, production current, or activation.
