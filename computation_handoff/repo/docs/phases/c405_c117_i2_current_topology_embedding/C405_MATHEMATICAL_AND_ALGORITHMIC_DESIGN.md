# C405 mathematical and algorithmic design

## 1. Data model

C405 operates on the accepted C47 qg factorized order

```text
partition, intrinsic-HO mode, quark helicity, gluon helicity, triplet color
```

and on the accepted direct-sum order

```text
q sector, then qg sector.
```

It never changes C114--C127 or the accepted C403/C404 files.

## 2. Source-owner reconciliation

`topology.py` hash-locks C114, C115, C117, C119, C124, C125, C126, C127, C190, C192, C193, C249, and C250. Literal source checks expose graph-class conflicts, incomplete current-pair leaf records, derivative-factor overlap risk, and the absence of numerical finite-HO current-product matrices. C190 records the pre-C192 Gauss-current split as incomplete. C192 then fixes the ordered source AST and derivative on the second source field, while leaving the external BRA/KET image of that field unresolved after normal ordering.

The corrected current-pair grammar is reconstructed from the ordered product name itself and evaluated through both C119 current identities. This grammar is an identity layer only; it is not a normal-ordering result.

## 3. Ordered derivative kernels

`derivative_order.py` enumerates all \(2^{N_g(P)}\) BRA/KET assignments for each product. This is not ambiguity about the source derivative slot: C192 fixes that slot as the second ordered gluon field. The finite family represents the still-missing normal-ordering map from that fixed source field to an external qg BRA or KET leg. Exact rational arithmetic is used for the C404 transfer and discrete \(k_g\) factors. Sparse and independent matrix-free routes are provided, and every row is paired with its exact adjoint assignment.

No API exists that silently chooses an assignment.

## 4. Conditional qg composition

`conditioned.py` constructs

\[
L\otimes I\otimes S\otimes C
\]

in the exact C47 axis order. The sparse route uses SciPy Kronecker products. The independent action reshapes the vector into the factorized tensor, applies color, spin, spatial, and longitudinal factors independently, and then restores the flat order.

The `LinearOperator.rmatvec` route uses the source-order adjoint product and derivative assignment; it does not rely on post-hoc averaging.

## 5. Embedding mechanics

`embedding.py` exposes an explicit two-diagonal-block assembler. Shapes and finite values are validated. Matrix-free action is evaluated independently by slicing the direct-sum vector. The qg-only record is metadata and cannot return a complete operator.

## 6. Normalization boundary

`normalization.py` parses the literal symbolic source factors and records powers of \(L\), \(\pi\), and \(K\). It does not infer field/state multiplicities or contraction measures. `evaluate_complete_prefactor` fails closed.

## 7. Binding overlay and completion

`bindings.py` overlays the accepted C404 57-row inventory. Only the three `c_C117_1` rows are updated, and their complete numerical apply path remains `None`.

`closure.py` collects source, numerical, and embedding checks into one completion record and provides the single fail-closed complete-action API.

## 8. Numerical tolerances

The conditional-kernel sparse/matrix-free and adjoint residual tolerances are \(2\times10^{-11}\). Exact rational longitudinal relations and cross-sector zeros are tested at exact zero. These tolerances validate numerical implementations only; they do not define physical irrelevance or rank.
