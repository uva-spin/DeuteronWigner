# C408 mathematical and algorithmic design

## A. Exact q-sector I4 member

Let the external q-sector transverse mode be the C45 ground state `a=b=(0,0)` and let the contracted intermediate quark transverse mode be `r=(n,m)`. In the C45 coordinate convention,

\[
I_r(b)=\int d^2x\,|\phi_{00}(x;b)|^2|\phi_{nm}(x;b)|^2.
\]

After the angular integral and the change of variable `z=b^2 r^2`,

\[
I_r(b)=\frac{b^2}{\pi}\frac{n!}{(n+|m|)!}
\int_0^\infty dz\,e^{-2z}z^{|m|}
\left[L_n^{|m|}(z)\right]^2.
\]

The analytic route expands the finite Laguerre polynomial and evaluates exact Gamma moments. The independent route uses generalized Gauss--Laguerre quadrature. The complete finite C45 mode axis satisfies

\[
2n+|m|\le N_{\max}-1.
\]

The source-routed q-sector scalar is

\[
\beta^{qq}_{q,K}
=
\left[\sum_{r_L\ne K}\frac{C_F}{(r_L-K)^2}\right]
\left[\sum_{r_\perp\in\mathcal M_{\perp,K}}I_{r_\perp}(b_K)\right],
\]

and the six-dimensional q-sector primitive is

\[
B^{qq}_{q,K}=\beta^{qq}_{q,K}I_6.
\]

The common C114/C119 normalization and coupling remain factored.

## B. I2 member sum

For each resolution, C403 supplies the admitted transverse modes

\[
\mathcal R_K=\{(n,m):2n+|m|\le N_{\max}-2\}.
\]

C124/C126 assign the exact I2 member multiplier one. Hence

\[
I_K^{\rm I2}=\sum_{r\in\mathcal R_K} I_{K,r}^{(403)}.
\]

The implementation preserves the C47 intrinsic-HO ordering through the exact C404 permutation.

## C. Product blocks

`J_qJ_q:qg->qg` is assembled as

\[
B^{qq}_{qg,K}
=L^{qq}_K\otimes I_K^{\rm I2}\otimes I_4\otimes I_3,
\]

where `L^{qq}_K` is the positive C407 same-species longitudinal diagonal containing the fundamental Casimir.

The mixed products are

\[
B^{qg}_{qg,K}
=L^{qg}_K\otimes I_K^{\rm I2}\otimes S_K\otimes C_{qg},
\]

\[
B^{gq}_{qg,K}
=L^{gq}_K\otimes I_K^{\rm I2}\otimes S_K\otimes C_{gq}.
\]

Sparse and independent tensor/matrix-free routes are required. The mixed adjoint residual must vanish at numerical tolerance.

## D. Fail-closed boundary

The implementation has no API that selects `g_s`, `c_C117_1`, graph normalization, or physical target values. The complete C117 apply method raises until the derivative-density and normalization/aggregation descendants are available.
