# C400.S2 Merge-Readiness Checklist

## ChatGPT replay gate

- [x] Historical P1C evidence remains unchanged.
- [x] Truthful status supersession is versioned.
- [x] C396 ledger contains 57 rows: 19 at each of K9, K11, and K13.
- [x] No C144-to-C396 proxy substitution is permitted.
- [x] All 33 corrected C144 diagnostic derivatives pass the matrix audit.
- [x] Six historical derivative mismatches are exposed (`phi_coupling` and `eta_2` at each K).
- [x] `eta_3`–`eta_8` are labeled numerically unbound, not irrelevant.
- [x] Unprojected eigenpairs carry no deuteron-sector claim.
- [x] A numerical rank-one sector projector is supported and tested.
- [x] Tracker surplus, sector crossing, global ambiguity, and rectangular-subspace cases pass.
- [x] LF and LPS analytic fixtures compare in a common canonical observable space.
- [x] Replay uses eigenvalues, residuals, overlaps, projectors, and dependency-exact records.
- [x] Step/tolerance scan rejects single-step certification.
- [x] Focused regression: 43 passed.
- [x] New source, tool, and test files compile.

## Live-repository Codex integration gate

- [ ] Verify the corrective-package manifest and baseline hashes.
- [ ] Apply the unified patch to the isolated live phase worktree.
- [ ] Reconcile import/path drift mechanically, without changing scientific behavior.
- [ ] Run the exact 43-test focused command.
- [ ] Run the relevant upstream regression and full local profile.
- [ ] Regenerate `docs/phases/c400_s2_corrective_patch` from the live repository.
- [ ] Compare generated invariant fields with `C400_S2_ACCEPTANCE_SPEC.json`.
- [ ] Record all repository-specific failures without suppressing them.
- [ ] Return the final diff, commands, environment, test ledger, and artifact hashes.
- [ ] Create at most one local phase-branch commit, only after required tests pass.
- [ ] Do not merge or push.

## User/ChatGPT scientific acceptance gate

- [ ] Review the Codex integration diff.
- [ ] Confirm no historical evidence was rewritten.
- [ ] Confirm no physical fit/rank/current selection/activation was introduced.
- [ ] Resolve any repository-only discrepancy.
- [ ] Authorize or reject the local phase commit.
- [ ] Authorize merge separately.
