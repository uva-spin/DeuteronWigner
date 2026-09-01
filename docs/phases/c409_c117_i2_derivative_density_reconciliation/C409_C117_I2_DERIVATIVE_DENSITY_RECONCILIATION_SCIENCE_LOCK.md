# C409 science lock: C117 I2 derivative-density reconciliation

## Baseline and scope

C409 is frozen against local merge baseline
`ab0af6587131a2846425e9bb19cfdc784b9f0bdb` and addresses only the
number-preserving `J_gJ_g:qg->qg` product block of the first C117
`I2_density_projector` direction.

C409 does not select a C117 coefficient, coupling, current prescription,
physical target, rank, fit, or activation state. Historical source owners are
read-only.

## Source derivative count

The C114 instantaneous-current term is

\[
P^-_{\mathrm{IC}}
=-\frac{g_s^2}{2}
\int d x^- d^2x_\perp\,
\left[Q_0(i\partial^+)^{-1}j_a^+\right]
\left[Q_0(i\partial^+)^{-1}j_a^+\right],
\]

with

\[
J_g^{+a}=-f^{abc}A_\perp^b\partial^+A_\perp^c.
\]

Each source gluon current therefore contains exactly one longitudinal
derivative. `J_gJ_g` contains exactly two.

C406 evaluates the full number-preserving one-gluon current descendant,

\[
\gamma_g(k',k)
=-\frac{k'+k}{2\sqrt{k'k}}F^a,
\]

and C407 forms the product of two such current factors, the C114 nonzero-mode
inverse square, and the adjoint Casimir:

\[
w_g(k,r)
=\frac{C_A}{(r-k)^2}\frac{(k+r)^2}{4kr},
\qquad C_A=3.
\]

Thus the complete pair of source derivatives is already present in the C407
longitudinal descendant.

## Reconciliation of C119 and C124/C126

Historical symbolic layers expose all of the following:

- C119 `gluon_current` includes a `pi*k/L` derivative factor;
- C119 also lists a separate `derivative_or_helicity` `pi*k/L` leaf;
- C124/C126 attach a `pi*k/L` expression to the abstract
  `derivative_density` member;
- C406/C407 directly derive the full current momenta from the authenticated
  source current.

These are overlapping representations, not independent factors. On the C409
reduced route, multiplying either extra derivative expression would count a
third derivative; multiplying both would count four. Both operations are
forbidden.

The exact scale powers of the source-qualified subset are

\[
\left(\frac{L}{\pi}\right)^2
\left(\frac{\pi}{L}\right)
\left(\frac{\pi}{L}\right)=1.
\]

No residual `L` or `pi` power remains in this longitudinal subset.

## Reduced transverse kernel

The `partial^+` derivatives act on the longitudinal plane-wave phases, not on
the transverse HO wave functions. After their evaluation in the C406/C407
current descendant, the residual number-preserving transverse factor is the
finite density-member sum

\[
I_K^{gg,\mathrm{red}}
=\sum_{\rho\in\mathcal R_K} I_{K,\rho}^{(403)}.
\]

This unit residual member multiplier is specific to the C409 reduced
`J_gJ_g:qg->qg` route. It does not globally replace C124's abstract
`derivative_density` definition.

## Numerical primitive

The source-routed qg product-block primitive is

\[
B^{gg}_{qg,K}
=L^{gg}_K\otimes I_K^{gg,\mathrm{red}}
\otimes I_4\otimes I_3.
\]

`L_K^{gg}` is the C407 diagonal descendant and already contains `C_A=3`.
Therefore the residual triplet-color factor is `I_3`; multiplying the C404
`3 I_3` color matrix again would double count the Casimir. C409 verifies the
equivalent factorization obtained by moving `C_A` from the longitudinal factor
back to the color factor.

## Boundary

C409 adds three source-routed `J_gJ_g:qg->qg` primitives, raising the
source-routed product-block primitive count from nine to twelve. It does not
raise the complete C117 or C396 coordinate-action counts.

The q-sector `J_gJ_g` block remains unavailable rather than zero because the
number-preserving branch has no external gluon but number-changing pair and
vacuum descendants remain unresolved.

The complete C117 action still requires:

- q-sector gluon pair/vacuum descendants;
- route-reconciled finite-cell, field, state and `M^2` normalization;
- complete target count-once aggregation;
- `g_s^2` and `c_C117_1` values.

The final status is:

```text
source-routed product-block primitives: 12
complete C117 numerical actions:         0
complete C396 numerical actions:         6
physical rank:               RANK_NOT_EVALUATED
physical fit:                unauthorized
activation:                  NOT_READY
```
