# C400.S2M merge-closure implementation report

C400.S2 live integration reproduced the supplied corrective patch exactly and passed its focused development suite, but independent merge review found two residual defects:

1. the S2 current comparison imported `p1b_current.py` from an unmerged P1/P1B/P1C worktree surface, so an S2-only commit was not dependency closed on the tracked baseline;
2. a Hermitian idempotent projector was sufficient to label a restricted Ritz vector as `PROJECTED_SECTOR_STATE`, even when the projector range was not invariant under the Hamiltonian and the full-space eigenresidual failed.

S2M copies the repaired no-default current adapter into the S2 package and redirects S2 source, tests, and generator imports to that local implementation. It also separates projected-range membership from spectral verification. A projected state is labeled `PROJECTED_SECTOR_EIGENPAIR_VERIFIED` only when projector membership, Hamiltonian invariance of the projected range, and the full-space relative eigenresidual all pass. Otherwise it is explicitly `PROJECTED_SUBSPACE_RITZ_PAIR_ONLY`.

This stage changes no physical inputs, coordinate values, current prescription, likelihood, rank claim, or activation status. The pre-existing C64 runtime-artifact gap remains outside this merge-closure patch.
