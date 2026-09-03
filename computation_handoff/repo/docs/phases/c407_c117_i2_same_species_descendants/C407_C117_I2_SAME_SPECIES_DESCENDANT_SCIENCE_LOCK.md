# C407 C117 I2 same-species contraction science lock

## Baseline and objective

C407 starts from the accepted local C406 merge
`4f932604483701d18158164288674cea82a07b3f`. C406 closed the one-gluon
normal-order descendant for the mixed current products but left the
same-species products `J_qJ_q` and `J_gJ_g` unresolved because they require an
explicit intermediate one-particle mode.

C407 closes the finite longitudinal intermediate axes and their one-body
normal-ordering weights. It also provides a caller-conditioned numerical
composition interface joining the `J_qJ_q:qg->qg` longitudinal descendant to
the individual C403 `I2_density_projector` member kernels. The C117 source
still writes the transverse sum with explicit graph-member weights `w_r`; no
source-authorized weight set has been recovered. C407 therefore has no unit-
weight, minimum-norm, or other default aggregate.

## Exact intermediate axis

For an external same-species mode `k`, the contracted mode is

\[
  r\in \mathcal M_{s,K},\qquad q=r-k\ne0,
\]

where `s` is QUARK or GLUON and `\mathcal M_{s,K}` is the positive C45 APBC or
PBC mode axis at the selected resolution. Because both modes have the same
boundary parity, `q` is an integer. The C114 Q0 prescription removes exactly
`r=k`; no threshold is used.

The finite inventory contains 154 rows across K9, K11 and K13, including the
q-sector external quark and the qg-sector external quark/gluon modes. The
number-preserving gluon branch is not applicable to the q sector because no
external gluon exists; pair and vacuum branches remain unresolved, not zero.

## Quark one-body descendant

The C119 good-component current preserves quark helicity and carries the
fundamental color generator. After factoring the common finite-cell, field,
state and M2 normalization, its dimensionless one-body current factor is one.
The fermionic anticommutator gives the ordered color product

\[
  \sum_a T^aT^a=C_F I,\qquad C_F=\frac43.
\]

The exact longitudinal one-body weight is therefore

\[
  w_q(k,r)=\frac{C_F}{(r-k)^2},\qquad r\ne k.
\]

## Gluon one-body descendant

C406 established the C151-normalized one-gluon current factor

\[
  \gamma_g(k',k)=-\frac{k'+k}{2\sqrt{k'k}}F^a.
\]

The bosonic commutator in `J_g(-q)J_g(q)` gives

\[
  \sum_a F^aF^a=C_A I,\qquad C_A=3,
\]

and hence

\[
  w_g(k,r)=\frac{C_A}{(r-k)^2}\frac{(k+r)^2}{4kr},
  \qquad r\ne k.
\]

The longitudinal descendant is source derived. The transverse
`derivative_density` descendant remains open because the historical C119/C125
surfaces risk counting the gluon derivative twice. C407 does not resolve that
by convention.

## Caller-conditioned J_qJ_q qg composition

C125 assigns `J_qJ_q` to the C117 `I2_density_projector` graph. C403 supplies
the admitted transverse-HO axis and each individual member kernel
`I^(403)_{K,rho}`. C117 retains the graph-member coefficients as explicit
weights `w_rho`; their numerical values are not source-authorized.

For a complete caller-supplied finite weight mapping, C407 can form

\[
  B^{qq}_{K}[w]
  =
  \operatorname{diag}_{p}\!\left[
    \sum_{r\in\mathcal M_{q,K}\setminus\{k_q(p)\}}
    \frac{C_F}{(r-k_q(p))^2}
  \right]
  \otimes
  \left[\sum_{\rho\in\mathcal R_K}w_\rho I^{(403)}_{K,\rho}\right]
  \otimes I_4\otimes I_3.
\]

The ordering is the verified C47 order: partition, intrinsic HO mode, quark
helicity, gluon helicity, triplet color. Sparse and independently evaluated
matrix-free routes are supplied.

The API rejects absent, incomplete, duplicate, nonfinite or out-of-axis weight
mappings. Its deterministic validation weights are explicitly nonphysical and
exist only to stress the composition route. Consequently this interface is
classified as

`CALLER_CONDITIONED_JQJQ_QG_COMPOSITION_STRESS_TEST_NOT_OPERATOR_BINDING`.

## Strict nonclaims

C407 does not provide:

- source-authorized C117 `I2` graph-member weights for `J_qJ_q`;
- the `J_qJ_q:q->q` I4-local transverse kernel;
- the `J_gJ_g:qg->qg` derivative-density transverse action;
- the `J_gJ_g:q->q` pair/vacuum branches;
- route-reconciled finite-cell, field, state and M2 normalization;
- C125 target aggregation and count-once multiplicity;
- `g_s^2` or a value of `c_C117_1`;
- a complete C117 numerical action;
- a physical rank, fit or activation.

The complete C396 numerical-action count remains six.
