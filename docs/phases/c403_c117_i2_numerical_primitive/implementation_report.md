# C403 C117 I2 finite-axis and spatial-kernel numerical primitive

Status: `C403_C117_I2_FINITE_AXIS_AND_SPATIAL_KERNEL_NUMERICAL_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE`
Accepted baseline: `fce8842e5ddc6660c735b7f69723f63c9bff7073`

## Scientific advance

C403 closes the first numerical substructure of the C117 `I2_density_projector` direction without promoting it to a complete C396 coordinate action.  It provides an exact finite internal-member axis and a K-local numerical transverse-HO spatial kernel for each admitted internal mode.

The finite-support theorem is:

```text
ADMITTED  iff  2 n + |m| <= Nmax - 2
REJECTED  iff  2 n + |m|  = Nmax - 1
```

For an admitted quark member, a ground-state gluon companion and CM ground produce the exact C62 witness coefficient `x_g^(shell/2)`.  For an admitted gluon member, the corresponding coefficient is `(-1)^shell x_q^(shell/2)`.  All positive C47 longitudinal partitions are covered.

The exhaustive certificate contains 1774 partition/species/mode rows: 1466 admitted exact nonzero witnesses and 308 exact shell exclusions.  All exact comparisons pass.

## Numerical spatial primitive

For external HO modes `a,b` and one contracted mode `r`, C403 evaluates

```text
I[a,b;r] = integral d^2x phi_a^*(x) phi_b(x) |phi_r(x)|^2.
```

The analytic route uses finite generalized-Laguerre coefficients and exact rational Gamma moments. An independent generalized Gauss--Laguerre route verifies deterministic representative modes at every resolution.  Every single-member matrix is checked separately for Hermiticity and positive semidefiniteness as a weighted Gram matrix.  An arbitrary signed aggregate is not claimed positive semidefinite.

The maximum analytic/quadrature residual is `8.413e-17` and the maximum sparse/matrix-free residual is `0.000e+00`.

## Axis counts

| Resolution | Species | candidate members | admitted members | rejected members |
|---|---:|---:|---:|---:|
| K9 | QUARK | 864 | 672 | 192 |
| K9 | GLUON | 2304 | 1792 | 512 |
| K11 | QUARK | 1650 | 1350 | 300 |
| K11 | GLUON | 4400 | 3600 | 800 |
| K13 | QUARK | 2808 | 2376 | 432 |
| K13 | GLUON | 7488 | 6336 | 1152 |

## C396 frontier

C403 updates 3 C117 binding rows, one per resolution. The number of complete numerical C396 coordinate actions remains 6; no complete C117 action is claimed.

The smallest remaining object is the source-faithful K-local contraction of the C114 inverse/source factor, C119 current factors, spin/color/normalization factors, and target q/qg aggregation with the new finite axis and spatial kernel.

## Scientific boundary

No coefficient, target, state, current, rank, fit, cross-resolution equality, or activation decision is made.  Missing full-operator factors remain unavailable, not zero.
