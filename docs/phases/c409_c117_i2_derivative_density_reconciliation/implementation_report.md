# C409 implementation report

## Result

`C409_C117_I2_JGJG_DERIVATIVE_COUNT_RECONCILED_NUMBER_PRESERVING_QG_PRODUCT_BLOCK_PRIMITIVE_READY_FULL_C117_ACTION_UNAVAILABLE`

C409 reconciles the derivative count for the number-preserving `J_gJ_g:qg->qg` route. The C114/C192 source contains exactly two longitudinal derivatives, one in each gluon current. C406 evaluates each complete one-gluon current descendant and C407 evaluates their product with the inverse-square kernel. C409 therefore excludes the additional C119 derivative leaf and C124/C126 `pi*k/L` member factor on this reduced route.

## Numerical checks

- Source authority rows: 14
- Exact derivative-reconstruction rows: 62
- Source-routed JgJg qg paths: 3
- Maximum sparse/matrix-free residual: 9.639e-14
- Maximum Hermiticity residual: 0.000e+00
- Maximum single-counted C_A equivalence residual: 4.252e-14
- Source-routed product-block primitive paths after C409: 12
- Complete C117 numerical apply paths: 0
- Complete C396 numerical apply paths: 6

## Remaining exact frontier

J_gJ_g q-sector number-changing pair/vacuum descendants; route-reconciled finite-cell, field, external-state and M2 normalization for all four current products; complete target count-once aggregation; g_s^2 and c_C117_1

No physical coefficient, rank, fit, complete C117 action, or activation is claimed.
