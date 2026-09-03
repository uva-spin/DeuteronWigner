# C407 implementation report

## Result

`C407_C117_I2_SAME_SPECIES_LONGITUDINAL_DESCENDANTS_AND_CALLER_CONDITIONED_JQJQ_QG_COMPOSITION_READY_GRAPH_WEIGHTS_AND_JGJG_TRANSVERSE_DESCENDANT_UNRESOLVED`

C407 closes 154 exact same-species longitudinal intermediate-mode rows and
154 exact one-body longitudinal weights across K9, K11 and K13.
It additionally implements three K-local caller-conditioned `J_qJ_q:qg->qg` I2 composition interfaces. The C117 graph-member weights remain source-unbound and no unit-weight default is used.

## Numerical checks

- Source authority rows: 12
- Longitudinal sparse/matrix-free maximum residual: 0.000e+00
- Caller-conditioned J_qJ_q qg sparse/matrix-free maximum residual: 1.305e-14
- Direct finite-Fock normal-order validation: True
- Complete C117 numerical apply paths: 0
- Complete C396 numerical apply paths: 6

## Remaining exact frontier

source-authorized C117 I2 graph-member weights for J_qJ_q; source-qualified J_qJ_q q-sector I4-local transverse kernel; J_gJ_g derivative-density transverse descendant with derivative-count reconciliation; J_gJ_g q-sector pair/vacuum branches; route-reconciled finite-cell/field/state/M2 normalization; C125 target count-once aggregation; g_s^2 and c_C117_1

No physical coefficient, rank, fit or activation is claimed.
