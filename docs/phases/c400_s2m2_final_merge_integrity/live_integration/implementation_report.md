# C400.S2M2 final merge-integrity implementation report

The supplied C400.S2M2 package was verified and its exact three-file patch was applied to the existing S2/S2M worktree.

The correction adds finite LF/LPS current validation, converts dimensional LPS current matrices using the declared mass units, rejects noncanonical LPS spin-order and spin-phase metadata until an explicit basis transform exists, and adds a stale-evidence acceptance test. The mandatory full S2 generator was rerun before the focused gate, refreshing state-identity evidence to the S2M schema.

Validation completed:

- package verification: 16 manifest entries, pass;
- supplied patch SHA-256: `636a9e4640ee40f9e927018358eafd467ebee4c28c41a9fae5dd39495c6d47c5`;
- replacement files: all 3 byte-identical;
- compileall: pass;
- full S2 regeneration: pass; 16 artifacts, 57 symbolic C396 binding rows, 0 complete numerical apply paths, 33/33 corrected derivatives, 6 historical derivative mismatches, semantic replay pass;
- S2M regeneration: pass; dependency closure, projected-state semantics, and current-adapter semantics pass;
- focused S2/S2M2 suite: 26 passed, 0 failed;
- regenerated state-evidence fields and S2 generation hash linkage: pass;
- relevant upstream profile: 41 passed, 2 failed because strict C274/C329 reloads require the absent read-only `data/runtime/c64_qgtm2/index.json`.

The worktree Git index is not writable in this managed environment: the exact staging attempt returned exit 128 while creating `.git/worktrees/c400_p1_mechanical_closure/index.lock`. No files were staged and no commit, merge, or push was performed. The exact authorized staging-path list and user-run commands are included in this record.

No C396 numerical forward-map claim, physical state, production-current selection, physical fit/rank, coordinate choice, resolution averaging, Hamiltonian activation, or C64 artifact manufacture was performed.
