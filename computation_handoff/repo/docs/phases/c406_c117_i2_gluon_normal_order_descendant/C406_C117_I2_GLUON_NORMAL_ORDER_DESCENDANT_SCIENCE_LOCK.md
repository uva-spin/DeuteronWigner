# C406 C117 I2 gluon normal-order descendant science lock

**Accepted local baseline:** `4dbb0b8bbadc540f0da2337c46040afb971fffc1`
**Phase:** `C406/C117-I2-GLUON-NORMAL-ORDER-DESCENDANT`
**Status:** `C406_C117_I2_ONE_GLUON_NORMAL_ORDER_DESCENDANT_AND_MIXED_CURRENT_ROUTING_READY_SAME_SPECIES_CONTRACTIONS_UNRESOLVED`

## 1. Scientific purpose

C405 retained a finite family of BRA/KET derivative assignments because C192 fixes the derivative on the second source-ordered gluon field but does not, by itself, identify the external one-gluon matrix element after normal ordering. C406 performs that missing source-to-one-particle reduction for the gluon current

\[
J_g^{+a}(x)=-f^{abc}A_\perp^b(x)\,\partial_-A_\perp^c(x),
\]

where `partial_-` is the C192 notation for the derivative conjugate to the positive longitudinal momentum. The source sign, ordered field slots, derivative placement, C45 longitudinal phase, C151 one-gluon normalization, and adjoint-generator convention are retained explicitly.

C406 does not assemble the complete C117 `I2_density_projector` coordinate action. It closes one normal-ordering descendant, resolves the mixed-current external derivative routing, proves the mixed-current q-sector block is exactly zero, and identifies the genuinely different same-species contraction problem.

## 2. Source-owned mode conventions

The C45 longitudinal mode is

\[
\phi_k(x^-)=\frac{e^{+i\pi kx^-/L}}{\sqrt{2L}},
\qquad
p_k^+=\frac{\pi k}{L},
\qquad k>0.
\]

For a real transverse gluon field, the annihilation and creation pieces carry conjugate longitudinal phases. C151 fixes

\[
[a,a^\dagger]=\delta
\]

and supplies a one-gluon field coefficient proportional to `(2k_plus)^(-1/2)`.

The adjoint color generators are

\[
(F^a)_{bc}=-if^{abc}.
\]

## 3. Exact one-gluon normal-order descendant

The number-preserving terms arise in two ways.

First-field creation and differentiated second-field annihilation give

\[
-f^{abc}a_b^\dagger\,(-ik_{\rm ket})a_c
= -k_{\rm ket}(F^a)_{bc}a_b^\dagger a_c.
\]

First-field annihilation and differentiated second-field creation give, after bosonic reordering and exchange of the two field-color labels,

\[
-f^{abc}a_b\,(+ik_{\rm bra})a_c^\dagger
= -k_{\rm bra}(F^a)_{bc}a_b^\dagger a_c
+\text{commutator}.
\]

The commutator is proportional to

\[
f^{abc}\delta_{bc}=f^{abb}=0
\]

and therefore vanishes exactly. The dimensionless mode coefficient multiplying the Hermitian adjoint generator is

\[
\boxed{
-(k_{\rm bra}+k_{\rm ket})(F^a)_{bc}
}
\]

or, in source structure-constant form,

\[
i f^{abc}(k_{\rm bra}+k_{\rm ket}).
\]

With the C151 one-gluon factors included, the route-specific one-body coefficient is

\[
\boxed{
-\frac{k_{\rm bra}+k_{\rm ket}}
{2\sqrt{k_{\rm bra}k_{\rm ket}}}
(F^a)_{bc}
}.
\]

This is a one-gluon current matrix element. It is not the complete product normalization of the C117 Hamiltonian insertion.

## 4. Mixed-current routing theorem

For `J_qJ_g` and `J_gJ_q`, the retained qg-to-qg descendant acts directly on the external quark and gluon. Therefore C405's two conditional external assignments collapse exactly:

\[
\boxed{
L_K^{\rm C406}
=-\left(L_K^{\rm C405,BRA}+L_K^{\rm C405,KET}\right)
}
\]

with

\[
L_K^{\rm C406}(p',p)
=\kappa_K(p',p)\left[-k_g(p')-k_g(p)\right],
\]

and

\[
\kappa_K(p',p)=
\begin{cases}
[k_q(p')-k_q(p)]^{-2},&p'\ne p,\\[3pt]
0,&p'=p.
\end{cases}
\]

The zero-transfer diagonal remains exactly zero by the C114 `Q0` prescription.

The mixed-current q-sector block is also exactly zero. In the q-only sector the gluon current has no external gluon. Its one-body commutator contribution is proportional to `f^{abb}=0`, while its pair-creation and pair-annihilation branches have zero vacuum-to-vacuum matrix element. This zero is a source-derived selection rule, not a convenience zero-fill.

## 5. Same-species products are a different problem

The products `J_qJ_q` and `J_gJ_g` do not reduce to the same external-pair transfer kernel. Both currents act on the same particle and require an explicit intermediate one-particle mode/current-transfer axis. Their internal transfer can be nonzero even when the external partition is diagonal.

C406 therefore forbids promoting the C405 external-pair stress kernels for these two products. The smallest missing objects are source-qualified quark and gluon one-particle contraction descendants with:

- an explicit finite intermediate mode axis;
- the product-specific normal-ordering sign and multiplicity;
- finite-cell and state normalization;
- the target embedding and count-once rule;
- the Hermitian reverse action.

## 6. Numerical primitive assembled in C406

For the two mixed products only, C406 composes

\[
\mathcal M_{K,r}^{(P)}
=
L_K^{(P)}
\otimes I_{K,r}^{(403)}
\otimes S^{(404)}
\otimes C_P^{(404)},
\]

where `P` is `J_qJ_g` or `J_gJ_q`. Sparse, matrix-free, adjoint, and direct-sum routes are implemented. The q-sector block is inserted only through the exact zero certificate above.

The missing factors remain factored:

- route-reconciled field, external-state, and finite-cell normalization;
- C405-to-C125 member/witness aggregation;
- target count-once multiplicity;
- the complete C114 mass-squared conversion;
- `g_s^2`;
- the coefficient `c_C117_1`;
- both same-species current products.

The mixed matrices are numerical primitives, not complete C117 coordinate actions.

## 7. Binding status

C406 updates the three K-local `c_C117_1` binding records with:

- a source-derived one-gluon normal-order descendant;
- an exact mixed-product BRA/KET collapse;
- numerical mixed qg sparse and matrix-free primitives;
- an exact mixed-product q-sector zero certificate;
- a fail-closed same-species requirement.

The complete-path counts do not change:

```text
C406 descendant binding rows:               3
one-gluon descendant inventory rows:       77
product-routing rows:                      12
mixed numerical kernel rows:                6
complete C117 numerical apply paths:        0
complete C396 numerical apply paths:        6
full C117 I2 action:                    false
full C396 forward map:                  false
physical rank:              RANK_NOT_EVALUATED
physical fit:               unauthorized
activation:                 NOT_READY
```

## 8. Nonclaims and forbidden substitutions

C406 does not establish:

- a complete `I2_density_projector` Hamiltonian insertion;
- a complete product prefactor;
- the `J_qJ_q` or `J_gJ_g` contraction kernel;
- a physical value for `g_s` or `c_C117_1`;
- a physical Hamiltonian, state, rank, fit, or activation.

It is forbidden to replace unavailable objects by:

- a C144 diagnostic proxy;
- a zero matrix;
- a minimum-norm representative;
- an external-pair kernel for a same-species internal contraction;
- a factor-of-two merge of `J_qJ_g` and `J_gJ_q`;
- a default field/state normalization.

## 9. Next scientific frontier

The next source-faithful stage should build the finite intermediate contraction axes for `J_qJ_q` and `J_gJ_g`, or isolate their smallest missing numerical primitive. Only after those are source qualified can the four current products be joined to a complete normalization, target aggregation, and Hermitian action.
