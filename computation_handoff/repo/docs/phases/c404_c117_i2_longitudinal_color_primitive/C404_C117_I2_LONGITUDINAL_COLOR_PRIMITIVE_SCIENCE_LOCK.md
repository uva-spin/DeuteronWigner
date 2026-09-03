# C404 C117 `I2_density_projector` longitudinal, spin, and triplet-color numerical primitives

**Accepted local baseline:** `bd568280de5fb2846b4ec5cdaff36e7ec973b8f1`
**Status:** `C404_C117_I2_Q0_LONGITUDINAL_AND_TRIPLET_COLOR_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE`

## 1. Scope

C404 advances the first C117 coordinate only at the level of independently source-owned numerical factors.  It does **not** assemble a complete current-current matrix element and does not increase the count of complete C396 numerical coordinate actions beyond the six C401 mass directions.

The closed numerical primitives are:

1. the dimensionless nonzero-transfer part of the C114 kernel,
   \[
   \kappa(n)=\begin{cases}
     n^{-2}, & n\ne0,\\
     0, & n=0\quad(Q_0\text{ exclusion}),
   \end{cases}
   \]
   on the exact C47 fixed-\(K\) qg partition axis;
2. the four C45/C47 triplet color-charge products;
3. the diagonal \(J^+\) quark-helicity and gluon-polarization selection factors;
4. an algebraic sparse/matrix-free tensor-product stress test with the C403 spatial kernel.

The fourth object is deliberately **not** a source-qualified operator binding. C114/C115/C119 have not yet supplied the product-specific normal-ordering and external-mode contraction program that would identify the algebraic tensor product with a physical `J_qJ_q`, `J_qJ_g`, `J_gJ_q`, or `J_gJ_g` matrix element.

## 2. Exact longitudinal transfer primitive

For each C47 qg partition,
\[
 k_q+k_g=K,\qquad x_q=\frac{k_q}{K},\qquad x_g=\frac{k_g}{K},\qquad x_q+x_g=1.
\]
For bra and ket partition labels \(p',p\), define
\[
 n_q=k_q(p')-k_q(p),\qquad n_g=k_g(p')-k_g(p)=-n_q.
\]
Because the quark modes are half-integer and the gluon modes are integer while total \(K\) is fixed, \(n_q,n_g\in\mathbb Z\).  C114 gives
\[
 (i\partial^+)^{-2}\longrightarrow \left(\frac{L}{\pi}\right)^2\frac{1}{n^2},
 \qquad n\ne0,
\]
and the exact \(Q_0\) projector removes \(n=0\).  C404 implements only
\[
 \kappa_{p'p}=\begin{cases}
  1/[k_q(p')-k_q(p)]^2,&p'\ne p,\\
  0,&p'=p.
 \end{cases}
\]
The factor \((L/\pi)^2\), current normalization, source coefficient, and \(M^2\) conversion remain separate.

This partition-space matrix is a kinematic transfer primitive. It is not a proof that every current product realizes every partition transition. In particular, C114 still requires product-specific normal ordering and contraction ownership.

## 3. Exact C47 qg basis order

The accepted qg direct-sum order is

```text
partition, C47 intrinsic/relative HO mode, quark helicity,
gluon helicity, triplet color.
```

The C403 generic support list and the C47 intrinsic-mode list contain the same modes but use different deterministic orderings. C404 records and verifies the exact permutation rather than assuming that the two lists are index-compatible.

The resulting qg dimensions are:

| Resolution | partitions | intrinsic modes | spin states | colors | qg dimension |
|---|---:|---:|---:|---:|---:|
| K9 | 4 | 28 | 4 | 3 | 1344 |
| K11 | 5 | 45 | 4 | 3 | 2700 |
| K13 | 6 | 66 | 4 | 3 | 4752 |

## 4. Triplet color-charge products

C45 fixes
\[
 T^a=\frac{\lambda^a}{2},\qquad
 \mathrm{Tr}(T^aT^b)=\frac12\delta^{ab},\qquad
 (F^a)_{bc}=-if^{abc}.
\]
C47 fixes the triplet isometry
\[
 U_{(c,b),\alpha}=\frac{T^b_{c\alpha}}{\sqrt{C_F}},
 \qquad C_F=\frac43.
\]
Projecting the charge-generator products into this triplet gives
\[
 U^\dagger\sum_a T_q^aT_q^aU=\frac43 I_3,
\]
\[
 U^\dagger\sum_a T_q^aF_g^aU
 =U^\dagger\sum_a F_g^aT_q^aU
 =-\frac32 I_3,
\]
\[
 U^\dagger\sum_a F_g^aF_g^aU=3I_3.
\]
Their sum obeys the triplet Casimir identity
\[
 \sum_a(T_q^a+F_g^a)^2\Big|_{\mathbf 3}=\frac43I_3.
\]

These are Hermitian charge-generator primitives. The source phase in \(J_g^+=-f^{abc}A^b\partial^+A^c\), its ordered derivative factor, and the finite-cell normalization are not yet numerically bound.

## 5. Spin and polarization selection

At the factor level, the good-component quark current and the transverse gluon current preserve the external quark helicity and gluon polarization. On the ordered axis
\[
(h_q,h_g)=(-1,-1),(-1,+1),(+1,-1),(+1,+1),
\]
C404 therefore provides the exact selection matrix \(I_4\). The ordered gluon derivative momentum factor is explicitly excluded.

## 6. Algebraic factorization stress test

C404 composes
\[
 \mathcal B^{(p)}_{K,r}
 =\kappa_K\otimes I^{(403)}_{K,r}\otimes I_{4}\otimes C_p
\]
for each algebraic color product \(p\) and selected C403 internal mode \(r\). Sparse and independently evaluated matrix-free routes agree and the matrices are Hermitian.

This construction is classified as

```text
ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING
```

because the exact source topology and normal-ordering descendants are not yet bound. It cannot be multiplied by an assumed coefficient and inserted into the C396 Hamiltonian.

## 7. Current C396 status

C404 updates the three K-local records for `c_C117_1` with the new primitive paths, but:

```text
complete C117 numerical apply paths: 0
complete C396 numerical apply paths: 6
full C396 forward map: false
physical response rank: not evaluated
physical fit: unauthorized
activation: NOT_READY
```

No C117 coefficient, coupling, target aggregation, state, or current prescription is selected.

## 8. Smallest remaining source-owned object

The next implementation target is the product-specific current-factor assembly:

\[
\boxed{
\text{C114 product topology and normal ordering}
\otimes
\text{C119 finite-cell/current factors}
\otimes
\text{C115 source phase and ordered derivative}
\otimes
\text{C124/C125 count-once target embedding}
}
\]

joined to the already validated C403 spatial and C404 transfer/color/spin primitives, with the Hermitian source-order reverse constructed independently.

The first lawful complete component should be selected by source ownership, not by convenience. Missing factors remain unavailable, not zero.
