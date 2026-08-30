# C404 C117 I2 longitudinal, spin, and triplet-color numerical primitives

Status: `C404_C117_I2_Q0_LONGITUDINAL_AND_TRIPLET_COLOR_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE`
Accepted local baseline: `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1`

## Scientific advance

C404 closes three independently source-owned factor classes needed by the first C117 direction: the exact dimensionless C114 Q0/nonzero-transfer kernel on the C47 qg partition axis, the C45/C47 triplet color-charge products, and the diagonal J+ helicity/polarization selection rule.

The exact partition kernel is

```text
kappa(p',p) = 0                         if p'=p (Q0 exclusion)
              1/[kq(p')-kq(p)]^2       otherwise.
```

It is K-local and preserves exact total-K transfer: `n_q+n_g=0`.

## K-local axis and transfer counts

| resolution | partitions | nonzero Q0 pairs | qg dimension |
|---|---:|---:|---:|
| K9 | 4 | 12 | 1344 |
| K11 | 5 | 20 | 2700 |
| K13 | 6 | 30 | 4752 |

C404 explicitly verifies the C47 intrinsic-mode order and records the permutation needed to read the C403 spatial kernel in that order.

## Triplet color algebra

The four exact scalar products are `4/3`, `-3/2`, `-3/2`, and `3` for `J_qJ_q`, `J_qJ_g`, `J_gJ_q`, and `J_gJ_g`, respectively. Their sum gives the triplet Casimir `4/3`. The maximum color residual is `1.473e-15`.

## Factorization stress test

The closed longitudinal, C403 spatial, spin-selection, and color factors are composed in sparse and independent matrix-free routes. This is deliberately classified as:

```text
ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING
```

The maximum sparse/matrix-free residual is `4.275e-16` and the maximum Hermiticity residual is `0.000e+00`.

The missing product-specific normal-ordering and external-mode contraction map prevents these stress-test matrices from being interpreted as current-product matrix elements.

## C396 frontier

C404 updates 3 K-local `c_C117_1` rows. The complete numerical C396 path count remains 6 and the complete C117 path count remains zero.

The smallest missing object is the source-qualified product topology and finite-cell/current-factor assembly, followed by count-once q/qg target embedding and an independently constructed Hermitian reverse.

No coefficient, coupling, target, state, current, rank, fit, resolution average, merge, push, or activation decision is made.
