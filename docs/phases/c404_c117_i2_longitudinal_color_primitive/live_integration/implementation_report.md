# C404 live integration report

C404 was integrated from the frozen patch at baseline `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1` in the isolated phase worktree, with no manual reconciliation.

The live generator completed with status `C404_C117_I2_Q0_LONGITUDINAL_AND_TRIPLET_COLOR_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE`. Its package root is `0bdd5e00acb768c8db0af8fbfd3ff9f7b7fbc08f80a38f567f310da6ec4e3d59`; the stage reference root is `2873002fdb99074a1a00fa8ca4f3520ed772a4accd5618e8b22f8bc236f63552`. The difference is environment-dependent and two clean live builds are byte-identical across 11/11 generated artifacts.

Required selected tests pass 84/84: C404 15, C403 16, C401 14, C400.S2 26, C114/C115/C119 9, and C45/C47 4. Compilation passes. The five C400 deprecation warnings are recorded and do not affect the exit code.

Validated invariants include partition counts K9/K11/K13 = 4/5/6, qg dimensions 1344/2700/4752, exact Q0 zero diagonal, zero longitudinal symmetry residual, triplet color products 4/3, -3/2, -3/2, 3, total Casimir 4/3, and false source-qualified product topology. Complete C117 paths remain 0 and complete C396 paths remain 6; rank is not evaluated, fit is unauthorized, and activation is `NOT_READY`.

The factorization matrices remain explicitly `ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING`. The smallest remaining object is product-specific C114 normal ordering/current topology, C119 finite-cell and ordered-current factors, C115 source phase and gluon derivative, C124/C125 target aggregation, and an independently constructed Hermitian reverse, with coefficients unselected.

The requested local commit could not be created because the sandbox cannot write the linked worktree index; the exact error is recorded in `commands.jsonl`. No merge or push was performed.
