# C404 merge-readiness checklist

- [ ] Patch applies to `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1`.
- [ ] Package and patch hashes verify.
- [ ] C47 partition and intrinsic-mode ordering checks pass at K9/K11/K13.
- [ ] Exact Q0 transfer matrices have zero diagonal and correct rational off-diagonal values.
- [ ] Triplet color products reproduce `4/3`, `-3/2`, `-3/2`, and `3`.
- [ ] Total triplet color charge reproduces `4/3`.
- [ ] Sparse and matrix-free longitudinal routes agree.
- [ ] Algebraic factorization stress-test sparse and matrix-free routes agree.
- [ ] Stress tests remain labeled non-operator bindings.
- [ ] Full C117 action fails closed.
- [ ] C396 complete numerical apply count remains six.
- [ ] C404, C403, C401, C400.S2, and selected C114/C115/C119 tests pass.
- [ ] Generated evidence is deterministic across two clean builds.
- [ ] No C117 coefficient, coupling, state, current, rank, fit, merge, or push is selected by Codex.
