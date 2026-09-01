# C408 C117 I2 source-weight and transverse-routing closure

## Accepted baseline

C408 is defined on the accepted local `main` baseline

```text
6da320adf775956e26e860e294c08e047c66c024
```

which contains the C407 same-species descendants and the complete Python 3.9 compatibility repair.

## Scientific purpose

C408 closes two source-level ambiguities that remained after C407:

1. the transverse graph route for `J_qJ_q:q->q`;
2. the finite member multiplier for the `I2_density_projector` descendants used by the qg-sector I2 programs.

It then assembles source-routed, coefficient-free product-block primitives for `J_qJ_q`, `J_qJ_g`, and `J_gJ_q` at K9, K11, and K13.

C408 does **not** select a physical coupling or C117 coefficient, evaluate response rank, fit data, average resolutions, or activate the Hamiltonian.

## 1. Program/sector graph routing

C116 and C126 independently assign

```text
J_qJ_q:q->q -> I4_local
```

while the C125 helper assigns `I2_density_projector` based only on the product name. The C125 rule is therefore overbroad for the q sector.

C408 follows the two agreeing product-and-sector authorities C116/C126 and records the C125 conflict without rewriting historical files.

The q-sector spatial structure is

\[
I^{(4)}_{0r;r0}(b)
=
\int d^2x_\perp\,
\phi_{00}^*(x;b)\phi_r^*(x;b)\phi_r(x;b)\phi_{00}(x;b),
\]

with `r` running over the complete finite C45 one-particle transverse-HO shell. The external q-sector transverse mode is the C123/C128 ground mode; helicity and color remain explicit six-dimensional axes.

## 2. C124/C126 I2 member multiplier

C117 writes the generic finite density as

\[
\sum_{r\in\mathcal R} w_r\,\phi_r^*(x)\phi_r(x).
\]

The later source-derived C124/C126 witness descendant assigns the exact member multiplier

\[
w_r^{\rm member}=1
\]

for `I2_density_projector`; `derivative_density` instead carries its own explicit derivative multiplier.

C408 uses this exact C124/C126 multiplier only after C407 has separately performed the longitudinal intermediate-mode sum and the exact helicity/color contractions. Thus the remaining C403 transverse member sum contains one copy of each canonical admitted transverse mode. This statement does not set

- the common current/field/state normalization;
- the target count-once multiplicity;
- `g_s^2`;
- `c_C117_1`;
- any physical coordinate value.

The generic C249 caller-weighted interface remains useful, but it no longer blocks this source-specific C124/C126 descendant.

## 3. Source-routed product-block primitives

For the qg `J_qJ_q` block, C408 replaces the diagnostic weight fixture by the exact C124/C126 unit member map and composes it with the C407 same-species longitudinal descendant.

For the mixed products, C408 sums the C406 single-member kernels over the same exact I2 member axis:

\[
B^{qg}_{qg,K}
=
\sum_{r\in\mathcal R_K} B^{qg}_{qg,K;r},
\qquad
B^{gq}_{qg,K}
=
\sum_{r\in\mathcal R_K} B^{gq}_{qg,K;r}.
\]

The source-order adjoint relation is preserved:

\[
\left(B^{qg}_{qg,K}\right)^\dagger=B^{gq}_{qg,K}.
\]

The q-sector mixed blocks remain exact source-derived zeros from C406.

For `J_qJ_q`, the q and qg blocks are assembled into the retained direct sum

\[
B^{qq}_K=
\begin{pmatrix}
B^{qq}_{q,K}&0\\
0&B^{qq}_{qg,K}
\end{pmatrix}.
\]

These are product-block primitives with common normalization factored. They are not complete C117 coordinate actions.

## 4. Derivative-density boundary

C408 does not promote `J_gJ_g:qg->qg`. The source chain contains a derivative-count conflict:

- C119 `gluon_current` already contains `pi*k/L`;
- C119 separately lists a `derivative_or_helicity` factor;
- C124 assigns `pi*k/L` to `derivative_density` members;
- C406/C407 derive both current momenta directly from the source current.

Blind multiplication would risk over-counting the ordered derivatives. The smallest remaining object is one product-level descendant that reconciles those authorities and fixes the complete normalization.

## 5. Numerical and physical nonclaims

C408 must retain:

```text
complete C117 numerical apply paths: 0
complete C396 numerical apply paths: 6
full C396 forward map: false
physical rank: RANK_NOT_EVALUATED
physical fit: unauthorized
activation: NOT_READY
```

No unavailable quantity is set to zero, one, or a minimum-norm representative.
