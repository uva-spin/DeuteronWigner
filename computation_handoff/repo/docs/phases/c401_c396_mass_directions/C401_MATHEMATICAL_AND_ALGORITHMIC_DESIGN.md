# C401 mathematical and algorithmic design

**Stage:** first source-faithful numerical slice of the C396 Hamiltonian family
**Accepted scientific baseline:** `ada80920fb51617333c9b87a40d6538a0b0de915`
**Status:** `C396_FIRST_SIX_K_LOCAL_NUMERICAL_BINDINGS_READY_DIAGNOSTIC_ONLY`
**Physical fit:** not authorized
**Physical rank:** not evaluated
**Activation:** not ready

## 1. Purpose

C400.S2 reduced the C396 frontier to a truthful 57-row symbolic inventory: nineteen
coordinate labels at each of K9, K11, and K13, with zero complete numerical apply paths.
C401 implements the first two matrix-valued primitives at each resolution.  The objective
is not to fit masses.  It is to turn two source-owned coordinate derivatives into actual
sparse and matrix-free operators while preserving every unresolved physical choice.

The implemented directions are

\[
D_{q,K}=\frac{\partial H_K}{\partial\mu_{q,K}^{2}},
\qquad
D_{g,K}=\frac{\partial H_K}{\partial\delta\mu_{g,K}^{2}}.
\]

Here \(\mu_{q,K}^{2}\) denotes the effective mass-squared monomial associated with the
C128/C131 mass-bilinear direction, including the scheme-dependent bare-mass/counterterm
split only through its identified one-body operator.  The gluon direction is an allowed
counterterm insertion around the source value \(m_g^2=0\); no nonzero physical gluon mass
is asserted.

## 2. Resolution and basis authority

The resolution labels are aliases for exact light-front resolutions:

| label | full ID | \(K_2\) | exact \(K\) | \(N_{\max}\) | \(b_{\rm HO}\) |
|---|---|---:|---:|---:|---:|
| K9 | `K9_2_N8_b0.40` | 9 | \(9/2\) | 8 | 0.40 GeV |
| K11 | `K11_2_N10_b0.45` | 11 | \(11/2\) | 10 | 0.45 GeV |
| K13 | `K13_2_N12_b0.50` | 13 | \(13/2\) | 12 | 0.50 GeV |

C45/C47 own the exact positive APBC/PBC longitudinal partitions.  For a qg state,

\[
k_q+k_g=K,\qquad x_q=\frac{k_q}{K},\qquad x_g=\frac{k_g}{K},
\qquad x_q+x_g=1,
\]

with \(k_q\) a positive half-integer and \(k_g\) a positive integer.  C128/C112 own the
accepted direct-sum dimensions and sector order,

\[
\mathcal H_K=\mathcal H_{q,K}\oplus\mathcal H_{qg,K},
\]

with the q sector first and the qg sector partition-major.  C401 uses no C144 fixture-value
rule.

The C47 source field defines \(b_{\rm HO}\) in GeV.  A later C396 metadata field is named
`bHO_GeVinv`; C401 records this conflict and does not silently resolve it.  The two mass
operators are independent of \(b_{\rm HO}\), so the conflict does not affect this slice.

## 3. Operator derivation

For a one-quark retained state,

\[
D_{q,K}|q,\alpha\rangle=|q,\alpha\rangle,
\qquad
D_{g,K}|q,\alpha\rangle=0.
\]

For a qg state in partition \(p\),

\[
D_{q,K}|qg,p,\alpha\rangle=\frac{1}{x_{q,p}}|qg,p,\alpha\rangle,
\qquad
D_{g,K}|qg,p,\alpha\rangle=\frac{1}{x_{g,p}}|qg,p,\alpha\rangle.
\]

Thus each direction is diagonal and Hermitian.  Its coefficient has units GeV\(^2\) and
the operator itself is dimensionless.  The qg blocks are constant within each longitudinal
partition, so the unresolved transverse sub-ordering is immaterial for these two actions.

C401 supplies four independent computational views:

1. a canonical exact block ledger;
2. a serialized sparse COO record;
3. a SciPy CSR matrix and `LinearOperator`;
4. an independent matrix-free block action.

A fifth route reconstructs the source mass functional directly from C47 partitions for
finite-difference holdout tests.

## 4. Historical C128 defect and supersession boundary

The historical private helper `free2.core._partitions` does not implement the C47
partition identity.  For doubled resolution label \(K_2=N\), it yields

\[
k_q^{\rm hist}=k_q+\frac12,
\qquad
x_q^{\rm hist}=x_q+\frac1N,
\qquad
x_g^{\rm hist}=x_g,
\]

and therefore

\[
x_q^{\rm hist}+x_g^{\rm hist}=1+\frac1N.
\]

This changes the historical qg quark-mass derivative and transverse kinetic denominator.
It leaves the gluon-mass derivative unchanged at the declared material tolerance.  C401
records the defect but does not edit or re-root C128.  The source-corrected C401 adapter
uses C47 fractions and C128 only for accepted dimensions and partition-major ordering.

The C144 smoke calculation is not retroactively changed: C144 uses a nonphysical
ID-derived fixture rule and does not evaluate C128's longitudinal fractions.

## 5. Coordinate ontology reduction

The nineteen C396 labels are not nineteen homogeneous additive matrices.  C401 uses the
following provisional ontology:

- `ct_mass`: numerical mass-bilinear direction ready as `D_mu_q_sq`;
- `ct_gluon_mass`: numerical gluon one-body direction ready as `D_delta_mu_g_sq`;
- `ct_vacuum_energy`: vacuum-only and outside the retained q\(\oplus\)qg direct sum;
- `ct_boundary`: a nonmatrix domain/boundary parameter;
- `ct_truncation`: an observable-space discrepancy, not a fabricated matrix;
- `ct_sector`: a matrix candidate whose owner normalization remains unresolved;
- `null_1...null_9`: source-owner classification required;
- `c_C117_1...c_C117_4`: source-qualified numerical insertion paths still required.

After excluding the three nonmatrix slots, sixteen is a provisional upper bound on
candidate matrix-affecting directions per resolution.  It is not a physical or numerical
rank.  C401 completes two coordinate-operator apply paths at each of three resolutions,
for six K-local paths in total.

## 6. Validation design

The acceptance suite establishes:

- exact positive fractions and \(x_q+x_g=1\);
- direct-sum dimensions and partition-major block boundaries;
- exact q-sector values \(1\) and \(0\);
- exact qg values \(1/x_q\) and \(1/x_g\);
- equality of COO, CSR, `LinearOperator`, and independent matrix-free actions;
- Hermiticity;
- independent source-formula finite differences at \(h=10^{-2},10^{-4},10^{-6}\);
- exposure of the historical C128 quark-fraction defect;
- material agreement of the historical and corrected gluon-mass derivatives;
- no C144 proxy and no physical parameter selection;
- deterministic, self-excluding evidence generation.

The validation vectors include q-only support, one probe at each partition boundary, and a
deterministic complex random vector.  No eigensolve, physical state, likelihood, or
identifiability analysis is performed.

## 7. Result and next source-ordered frontier

The accepted result is

```text
57 symbolic K-local C396 rows
6 complete numerical coordinate-operator apply paths
full C396 numerical forward map: false
rank status: RANK_NOT_EVALUATED
physical fit: not authorized
activation: NOT_READY
```

The next operator question is `ct_sector`: determine from source ownership whether it is an
independent q\(\leftrightarrow\)qg insertion or a renormalization of the canonical C53
vertex, and fix its exact normalization before numerical implementation.  The four C117
insertions follow, then owner-by-owner classification of the nine source-null directions.
