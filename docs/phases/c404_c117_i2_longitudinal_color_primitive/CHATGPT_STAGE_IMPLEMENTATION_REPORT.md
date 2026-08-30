# C404 ChatGPT-stage implementation report

## Result

C404 implements the next source-faithful numerical primitives needed by the first C117 `I2_density_projector` direction on the accepted C403/C401 baseline.

Status:

```text
C404_C117_I2_Q0_LONGITUDINAL_AND_TRIPLET_COLOR_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE
```

Accepted local baseline for live integration:

```text
bd568280de5fb2846b4ec5cdaff36e7ec973b8f1
```

## Implemented numerical factors

1. Exact C47 fixed-K qg partition axes at K9, K11, and K13.
2. Exact dimensionless C114 Q0/nonzero-transfer factor `1/n^2`, with exact zero at `n=0`.
3. Explicit reconciliation of the C47 intrinsic-HO order with the differently ordered C403 spatial-kernel basis.
4. Exact C45/C47 triplet color-charge products:
   - `J_qJ_q = 4/3 I_3`;
   - `J_qJ_g = -3/2 I_3`;
   - `J_gJ_q = -3/2 I_3`;
   - `J_gJ_g = 3 I_3`.
5. Exact diagonal J+ quark-helicity/gluon-polarization selection.
6. Sparse and independently evaluated matrix-free algebraic tensor-product stress tests with the C403 spatial kernels.
7. A C396 binding overlay for the three K-local `c_C117_1` records.

## Deliberate boundary

The tensor-product construction is **not** treated as a source-qualified current-product operator. Product-specific normal ordering, external-mode contractions, C119 finite-cell normalization, the ordered gluon derivative and source phase, q/qg target aggregation, and the Hermitian source-order reverse remain unbound.

Consequently:

```text
complete C117 numerical apply paths: 0
complete C396 numerical apply paths: 6
full C396 forward map: false
physical rank: RANK_NOT_EVALUATED
physical fit: unauthorized
activation: NOT_READY
```

## Numerical results

```text
partition counts:                 K9=4, K11=5, K13=6
nonzero Q0 partition pairs:       K9=12, K11=20, K13=30
qg dimensions:                    K9=1344, K11=2700, K13=4752
maximum longitudinal symmetry residual: 0
maximum triplet color scalar residual:   1.48e-15
maximum sparse/matrix-free stress residual: 4.28e-16
maximum stress-test Hermiticity residual:   0
```

The C47-to-C403 intrinsic-mode permutation is nontrivial and is now applied explicitly in both sparse and matrix-free routes.

## Validation

```text
C404 focused tests:                  15 passed
C403 regression:                     16 passed
C401 regression:                     14 passed
C400.S2 regression:                  26 passed
C114/C115/C119 source regression:     9 passed
C45/C47 source regression:            4 passed
Selected total:                      84 passed
Python compilation:                   PASS
Two clean generator builds:          11/11 byte-identical
```

## Next smallest object

The next scientific implementation is the product-specific current-factor and target-embedding program joining:

```text
C114 normal-ordering/current-product topology
C119 finite-cell and ordered-current factors
C115 source phase and gluon derivative
C124/C125 count-once q/qg target aggregation
C403 spatial primitive
C404 transfer/color/spin primitives
independently constructed Hermitian reverse
```

No coefficient or physical target should be selected during that assembly.
