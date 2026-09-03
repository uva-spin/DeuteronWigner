# C410 merge-readiness checklist

- [ ] Required baseline is `160eb887f393177170b4c3486cea27b41968dfce`.
- [ ] Branch is `codex/c410-c117-i2-retained-aggregation-boundary`.
- [ ] Package manifest and patch hash verify.
- [ ] C410 source hash audit passes for 12 owners.
- [ ] Vacuum-pair validation preserves a nonzero unequal-momentum witness.
- [ ] Equal-momentum pair witness cancels exactly.
- [ ] Full-source vacuum c-number is not claimed zero.
- [ ] Retained q-sector `J_gJ_g` block is zero only after explicit vacuum routing.
- [ ] Four products are included exactly once; mixed orders remain separate.
- [ ] Sparse and matrix-free aggregate routes agree at K9/K11/K13.
- [ ] Aggregate is Hermitian and source `-1/2` is applied once.
- [ ] `g_s^2` remains factored and `c_C117_1` remains unselected.
- [ ] C260/C262 normalization is unavailable, not defaulted.
- [ ] Complete C117 path count remains zero; C396 path count remains six.
- [ ] All 276 live acceptance tests pass on Python 3.9.
- [ ] Exactly 50 approved paths are staged.
- [ ] No ZIP, patch, bytecode, `.phase_mode`, merge, push, fit, rank, or activation work is included.
