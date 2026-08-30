# C405 C117 `I2_density_projector` current-topology and embedding science lock

**Status:** `C405_C117_I2_CURRENT_ORDER_DERIVATIVE_FAMILY_AND_DIRECT_SUM_EMBEDDING_READY_PRODUCT_NORMAL_ORDERING_UNRESOLVED`
**Accepted local baseline:** `6e7601881256d17fe14767d203cb4742143051c2`
**Coordinate under study:** `c_C117_1 / I2_density_projector`
**Physical fit:** not authorized
**Rank:** `RANK_NOT_EVALUATED`
**Activation:** `NOT_READY`

## 1. Purpose

C403 and C404 close exact finite-axis, transverse-HO, nonzero longitudinal-transfer, spin-selection, and triplet-color primitives for the first C117 direction. C405 determines how far those primitives can be joined to the source current-product records without inventing the still-missing normal-ordering and finite-cell contraction map.

The governing source operator is

\[
P^-_{\rm IC}
=-\frac{g_s^2}{2}
\int dx^-d^2x_\perp\,
\big[(i\partial^+)^{-1}Q_0 j_a^+\big]
\big[(i\partial^+)^{-1}Q_0 j_a^+\big],
\]

with

\[
j_a^+=J_{q,a}^+ + J_{g,a}^+,
\qquad
J_{q,a}^+=\bar\psi\gamma^+T^a\psi,
\qquad
J_{g,a}^+=-f^{abc}A_\perp^b\partial^+A_\perp^c.
\]

The ordered products are

\[
J_qJ_q,\qquad J_qJ_g,\qquad J_gJ_q,\qquad J_gJ_g.
\]

C405 does not infer a numerical matrix element merely from these operator identities.

## 2. Source reconciliation result

The hash-locked C114--C127 and later C190/C192/C193/C249/C250 surfaces do not provide one internally consistent, numerical product-to-matrix map.

C405 records the following facts.

1. C115 and C125 disagree on the graph-class assignment for three of the four current products.
2. Every one of the eight C119 product/sector leaf programs contains only the current identity selected from the first current in the product, rather than both ordered current identities.
3. The literal C119 gluon-current expression already contains the ordered derivative factor \(\pi k_c/L\), while historical C119/C126 leaf programs may add a separate derivative factor for four left-gluon program rows.
4. C126 and C249 retain one current-factor reference per product. C250 repairs the pair identity by evaluating both left and right currents, but still does not supply product-specific normal ordering.
5. C127 describes complete symbolic target programs while reporting zero numerical sparse entries and zero matrix-free actions.
6. C190 records the Gauss-current split as incomplete, while C192 subsequently derives the ordered gluon-current source AST
   \[
   -f^{abc}A_\perp^b\partial^+A_\perp^c,
   \]
   fixes the derivative on the second ordered source field, and keeps the two mixed-current owners separate with no factor-two merge.
7. C192 remains symbolic: it does not map the differentiated second source field to an external qg BRA or KET leg after product-specific normal ordering.
8. C193 identifies direct mixed-current contact owners, preserves their separate order, and reports zero finite-HO numerical evaluations and zero contact matrices.
9. C125 does establish a one-member/one-target count-once identity, but no source record maps the C405 conditional numerical kernels onto those C125 witnesses and target spans.

Consequently no historical product-to-projector assignment or derivative factor may be promoted by convenience.

## 3. Exact identities retained

The following identities are accepted.

- There are four ordered current products and two surviving diagonal Fock-sector blocks, `q->q` and `qg->qg`.
- The `q->qg` and `qg->q` blocks vanish exactly by the C114 even-gluon-number-parity proof.
- `J_qJ_g` and `J_gJ_q` are source-order adjoints.
- Every ordered product requires both left and right current identities.
- C192 fixes the gluon-current derivative on the second ordered source field.
- C192/C193 retain `J_q K J_g` and `J_g K J_q` as separate owners and forbid a factor-two merge.
- C125's witness-level count-once identity is accepted; the C405-kernel-to-C125-witness map remains absent.

The `q->q` diagonal block is unavailable, not zero.

## 4. Ordered gluon-derivative candidate family

The source current

\[
J_g^+=-f^{abc}A_\perp^b\partial^+A_\perp^c
\]

places the derivative on the source-ordered \(c\) field. C192 makes this source-slot statement authoritative. The available records do not identify that fixed second source field, after product-specific normal ordering, with an incoming or outgoing external gluon. C405 therefore retains an explicit finite candidate family for the remaining external-leg map.

For an ordered product \(P\), let \(N_g(P)\in\{0,1,2\}\) be the number of gluon currents and let

\[
\boldsymbol\ell=(\ell_1,\ldots,\ell_{N_g}),
\qquad \ell_i\in\{\mathrm{BRA},\mathrm{KET}\}.
\]

On the C47 qg partition axis,

\[
\kappa_K(p',p)=
\begin{cases}
0, & p'=p,\\[3pt]
\big[k_q(p')-k_q(p)\big]^{-2}, & p'\ne p,
\end{cases}
\]

and the conditional dimensionless ordered kernel is

\[
L_K^{(P,\boldsymbol\ell)}(p',p)
=
\kappa_K(p',p)
\prod_{i=1}^{N_g(P)}
\begin{cases}
k_g(p'),&\ell_i=\mathrm{BRA},\\
k_g(p),&\ell_i=\mathrm{KET}.
\end{cases}
\]

The explicit \(\pi/L\) factor for each gluon derivative remains in the normalization ledger. No default \(\boldsymbol\ell\) is selected.

The adjoint rule is

\[
(P,\ell_1,\ldots,\ell_n)^\dagger
=
\big(P^\dagger,\bar\ell_n,\ldots,\bar\ell_1\big),
\qquad
\overline{\mathrm{BRA}}=\mathrm{KET}.
\]

This gives nine assignments per resolution and 27 K-local rows in total.

## 5. Conditional qg kernels

For a caller-selected internal transverse mode \(r\), product \(P\), and derivative assignment \(\boldsymbol\ell\), C405 defines the diagnostic qg kernel

\[
\mathcal B_{K,r}^{(P,\boldsymbol\ell)}
=
L_K^{(P,\boldsymbol\ell)}
\otimes
I_{K,r}^{(403)}
\otimes
S^{(404)}
\otimes
C_P^{(404)}.
\]

Here \(I_{K,r}^{(403)}\) is the accepted C403 single-member transverse-HO density kernel, \(S^{(404)}\) is the accepted spin-selection matrix, and \(C_P^{(404)}\) is the accepted triplet-color product.

These matrices are classified as

```text
CALLER_CONDITIONED_CURRENT_ORDER_STRESS_TEST_NOT_OPERATOR_BINDING
```

because the source-qualified normal-ordering descendant, full normalization, source phase, target aggregation, q-sector diagonal action, \(g_s^2\), and `c_C117_1` remain factored or unavailable.

## 6. Literal scale ledger

Combining only the literal C114/C119 factors—the Q0 inverse, the \(x^-\) measure, two current expressions, and the conversion \(M^2=2P^+P^- - P_\perp^2\)—gives the following unresolved post-exponents:

| product | \(L\) | \(\pi\) | \(K\) |
|---|---:|---:|---:|
| \(J_qJ_q\) | 0 | -1 | 1 |
| \(J_qJ_g\) | -1 | 0 | 1 |
| \(J_gJ_q\) | -1 | 0 | 1 |
| \(J_gJ_g\) | -2 | 1 | 1 |

These are not final operator dimensions. They demonstrate that field/state normalization ownership and product-specific contraction multiplicities are indispensable. C405 therefore refuses to evaluate a complete numerical prefactor.

## 7. Direct-sum embedding boundary

The retained basis is ordered as

\[
\mathcal H_K=\mathcal H_{q,K}\oplus\mathcal H_{qg,K}.
\]

C405 provides the exact mechanical assembler

\[
\mathcal D_K=
\begin{pmatrix}
D_{q,K}&0\\
0&D_{qg,K}
\end{pmatrix}
\]

only when both diagonal blocks are supplied explicitly. The cross-sector zeros follow from C114. A qg conditional kernel alone is a partial block and may not be promoted to a complete direct-sum action by zero-filling \(D_{q,K}\).

## 8. C396 binding status

C405 updates the three K-local `c_C117_1` binding records with source-audit, current-pair, derivative-family, conditional-qg, and direct-sum-embedding paths. It does not increase the complete numerical action count.

```text
C405 boundary rows:                       3
complete C117 numerical apply paths:      0
complete C396 numerical apply paths:      6
full C117 I2 action:                      false
full C396 forward map:                    false
rank:                                     RANK_NOT_EVALUATED
physical fit:                             unauthorized
activation:                               NOT_READY
```

## 9. Smallest missing object

The smallest missing source-owned object is a product/sector normal-ordering descendant table that assigns:

- both ordered current matrix elements;
- graph class and contracted member species;
- the external BRA/KET image of each C192-fixed second source field;
- source phase and contraction sign;
- finite-cell, field, and state normalization ownership and multiplicities;
- the C405-to-C125 witness and target map;
- target aggregation multiplicity;
- the q-sector diagonal action;
- and the source-order Hermitian reverse.

Until this object is derived, unavailable factors remain unavailable rather than zero.
