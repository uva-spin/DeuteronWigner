# C404 mathematical and algorithmic design

## A. Exact arithmetic layer

Longitudinal momenta and fractions are represented by `fractions.Fraction`.  For every resolution, `partition_axis()` imports the C47 positive APBC/PBC partitions and verifies exact total-\(K\) conservation and \(x_q+x_g=1\).

`transfer_record()` computes the exact integer current-mode transfer and the exact rational \(Q_0/n^2\) factor.  The diagonal is set to zero only by the C114 \(Q_0\) identity.

## B. C47 mode-order reconciliation

`c47_relative_modes()` obtains the intrinsic-mode order from the C47 Talmi--Moshinsky CM-ground map.  `c47_to_c403_mode_permutation()` maps this order to the C403 spatial-kernel order.  Every partition is checked to use the same intrinsic labels and order.

## C. Sparse and matrix-free longitudinal action

The partition primitive has a dense diagnostic route, a CSR route, and an independently loop-evaluated matrix-free route.  Agreement is exact at floating representation for the small K-local partition matrices.

## D. Color algebra

The structure constants are recomputed from the C45 fundamental generators, the Hermitian adjoint generators are constructed, and the C47 triplet isometry is applied.  Each of the four ordered products is checked against its exact scalar multiple of the triplet identity, and the full color charge is checked against \(C_F=4/3\).

## E. Spin selection

The current-component selection is stored independently from color and from the unresolved derivative factor.  No spin-flip or polarization-flip matrix element is introduced.

## F. Factorization stress test

For a C403 internal spatial mode, the stress-test CSR matrix is assembled in exact C47 qg order as

```text
kron(partition_Q0, C403_spatial_in_C47_order, spin_selection, triplet_color_product)
```

The independent action applies the four factors sequentially without reading the Kronecker matrix.  The C403/C47 ordering permutation is applied in both directions around the spatial matrix-free action.

The test is explicitly not a current-product topology implementation.  It verifies that the closed factors can coexist numerically and that basis order, sparse serialization, and matrix-free evaluation agree.

## G. Fail-closed full action

`apply_complete_c117_i2()` always raises.  The C396 overlay retains `numerical_apply_path = null`, `selected = false`, and `zeroed = false` for all three `c_C117_1` records.

## H. Numerical tolerances

- color and isometry residuals: `2e-12`;
- sparse/matrix-free stress-test residual: `2e-11`;
- Hermiticity residual: `2e-11`.

These are implementation tolerances, not physical uncertainties or identifiability thresholds.
