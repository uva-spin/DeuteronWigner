# C410 C117 I2 retained aggregation boundary science lock

**Status:** `C410_C117_I2_Q_SECTOR_VACUUM_ROUTING_AND_RETAINED_CONNECTED_CURRENT_SQUARE_AGGREGATION_READY_C260_OPERATOR_NORMALIZATION_UNAVAILABLE`

**Accepted baseline:** `160eb887f393177170b4c3486cea27b41968dfce`

## Objective

C410 closes two bounded source-reduction problems left by C409:

1. classify the `J_g K J_g:q->q` pair/vacuum branches without replacing an unavailable contribution by zero; and
2. aggregate the twelve K-local source-routed product-block primitives into one retained connected current-square shape per resolution, preserving every source-ordered product exactly once.

C410 does not promote the result to the RI/SMOM-normalized C117 operator. The finite-C43 C260/C262 adapter and operator-normalization record remain unavailable.

## Source identity

The instantaneous current source is

\[
P^-_{\mathrm{IC}}
=-\frac{g_s^2}{2}\int dx^-d^2x_\perp
\left[(i\partial^+)^{-1}Q_0J_a^+\right]
\left[(i\partial^+)^{-1}Q_0J_a^+\right],
\qquad
J_a^+=J_{q,a}^+ + J_{g,a}^+.
\]

Therefore the current square contains four ordered products,

\[
J_qKJ_q+J_qKJ_g+J_gKJ_q+J_gKJ_g,
\]

with multiplicity one each. The two mixed orders remain separate Hermitian partners; there is no factor-two shortcut.

## q-sector gluon pair/vacuum branch

C192 exposes number-changing gluon pair-creation and pair-annihilation branches. Their vacuum product can be nonzero. With an external quark spectator, the contribution factorizes as

\[
I_q\otimes\langle 0_g|J_g(-q)K(q)J_g(q)|0_g\rangle.
\]

C129 classifies the double-contraction descendant as a vacuum c-number. C131 and C136 classify the associated vacuum direction as nonmatrix in the retained fixed-particle Hamiltonian and impose

\[
P_R\,(\text{vacuum direction})\,P_R=0.
\]

Accordingly, the retained connected q-sector block is exactly zero **after explicit vacuum-direction routing**. C410 does not claim that the full-source vacuum c-number vanishes, discard the pair branch, or insert an identity shift.

A finite SU(3) witness validates that unequal-momentum pair creation is nonzero, while equal-momentum pair creation cancels by the antisymmetry of the adjoint color generator. This witness is diagnostic; it is not a calculation of the physical vacuum energy.

## Retained connected aggregate shape

For each K-local resolution, C410 constructs

\[
\mathcal J^{(\mathrm{ret})}_K
= B_K^{qq}+B_K^{qg}+B_K^{gq}+B_K^{gg},
\]

using the accepted C408/C409 product primitives and the C410 q-sector vacuum projection. It then applies the exact source coefficient once,

\[
\mathcal S^{(410)}_K=-\frac12\,\mathcal J^{(\mathrm{ret})}_K,
\]

while keeping `g_s^2` factored and leaving `c_C117_1` unselected.

The result is a source-coefficient-reduced retained connected **shape primitive**, not the complete `O_C117_1,R` action.

## Numerical boundary

C410 provides:

- three exact retained q-sector `J_gJ_g` zero paths, with a nonzero full-source pair witness preserved separately;
- twelve source-routed K-local product-block primitive paths;
- three K-local retained connected aggregate shape paths;
- sparse and independently evaluated matrix-free routes;
- exact four-product decomposition, Hermiticity, mixed-order adjoint, and source-coefficient checks.

The complete C117 and C396 counts remain:

```text
complete C117 numerical apply paths: 0
complete C396 numerical apply paths: 6
physical rank: RANK_NOT_EVALUATED
physical fit: unauthorized
activation: NOT_READY
```

## Exact remaining object

The smallest remaining object is:

> a source-qualified K-local C260/C262 finite-C43 adapter and operator-normalization record mapping the C410 source-reduced retained connected shape to the `PROJECT_C117_RI_SMOM_V1` `O_C117_1,R` insertion, including the remaining field/state/M2 and normalized-wavepacket convention.

A physical value of `g_s` or `c_C117_1` is not required to define the derivative-operator shape. Those values remain external to this normalization gate and are not selected here.

## Prohibitions

C410 must not:

- claim the full-source vacuum c-number is zero;
- insert a q-sector identity shift;
- merge mixed current orders with an extra factor two;
- apply `g_s^2` or choose `c_C117_1`;
- invent the C260/C262 adapter or normalization;
- promote the shape primitive to a complete C117 coordinate action;
- evaluate physical rank, fit, activate, merge, or push.
