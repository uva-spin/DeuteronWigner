# C400.S2M live-integration implementation report

The supplied C400.S2M merge-closure package was verified and its exact patch applied to the existing isolated C400 worktree.

The patch closes the two reviewed S2 defects: the S2 current adapter is now local to `c400_s2_corrective`, and projected-range membership is no longer treated as a verified sector eigenpair without Hamiltonian-range invariance and a passing full-space relative eigenresidual.

Validation completed:

- package verification: 26 declared files, 26 verified, 0 errors;
- supplied patch SHA-256: `c5f4421acbd53fd975f261433ce9b4f8fc42684179924fcaea8db55d36100d86`;
- compileall: pass;
- standalone S2M acceptance: 22 passed, 0 failed;
- S2/P1 development regression: 44 passed, 0 failed;
- merge-closure generator: pass; dependency closure and projected-state semantics pass;
- forbidden-import audit: no matches;
- relevant upstream profile: 41 passed, 2 failed because strict C274/C329 reloads require the absent read-only `data/runtime/c64_qgtm2/index.json`.

The worktree index could not be written in this managed environment: `git add` returned exit 128 because `.git/worktrees/c400_p1_mechanical_closure/index.lock` is not writable. Therefore no files were staged and no commit was created. The candidate diff and all required evidence are included in this record and handoff ZIP for user/ChatGPT review.

No physical inputs, coordinate values, current prescription, likelihood, rank claim, activation status, or C64 artifact were changed.
