# C407 mathematical and algorithmic design

## 1. Source order and normal ordering

For a number-preserving current

\[
  J_s^a(q)=\sum_{\alpha\beta}
  c^\dagger_\alpha\,\Gamma_s^a(\alpha,\beta;q)\,c_\beta,
\]

normal ordering the source-ordered product produces the one-body term

\[
  D_s^{(1)}(q)=
  \sum_{\alpha\beta\gamma}
  c^\dagger_\alpha
  \Gamma_s^a(\alpha,\gamma;-q)
  \Gamma_s^a(\gamma,\beta;q)
  c_\beta.
\]

The fermionic anticommutator and bosonic commutator both give a positive
one-body matrix product. The common source coefficient `-g_s^2/2`, coupling,
finite-cell normalization and M2 conversion remain external to the C407
primitive.

## 2. Finite longitudinal modes

C45 supplies positive APBC quark modes and nonzero PBC gluon modes. At total
half-integer K, the finite mode counts are:

| resolution | quark modes | gluon modes |
|---|---:|---:|
| K9 | 5 | 4 |
| K11 | 6 | 5 |
| K13 | 7 | 6 |

For every external mode, C407 enumerates every same-species intermediate mode
except the identical mode. The transfer is therefore an exact nonzero integer
and the Q0 pole is absent by construction.

## 3. Exact rational weights

The quark weight is stored as `Fraction(4,3)/(r-k)^2`. The gluon product of
the two C406 current factors is exactly

\[
  \gamma_g(k,r)\gamma_g(r,k)
  =\frac{(k+r)^2}{4kr},
\]

so the gluon weight is also rational for finite C45 modes. Floating-point
conversion occurs only at sparse-matrix construction.

## 4. Independent Fock-space validation

C407 constructs finite fermionic and bosonic Fock representations and compares
the one-particle restriction of the source-ordered current product with the
independent matrix product `Gamma(-q) Gamma(q)`. Quark validation uses APBC
half-integer modes and gluon validation uses PBC positive-integer modes. This
tests the normal-ordering sign and multiplicity rather than merely comparing
two versions of the same formula.

## 5. Explicit graph-member weights

C403 deliberately exposes only individual spatial members and an explicit
weighted aggregation API. C117 writes the finite graph sum with coefficients
`w_r`; C407 therefore requires a complete caller-supplied mapping from every
admitted HO member to one finite real weight.

The boundary rejects:

- a missing or empty mapping;
- a partial mapping;
- duplicate canonical `(n,m)` members;
- nonfinite weights;
- modes outside the C403 admitted axis.

There is no unit-weight or minimum-norm default. For implementation validation,
C407 uses a deterministic, nonuniform and explicitly nonphysical fixture. The
fixture is not committed as a source-authorized operator coefficient set.

## 6. Caller-conditioned J_qJ_q qg composition

The C403 member kernels are permuted into the verified C47 intrinsic-mode
order before the tensor product is built. For explicit weights `w`, C407
combines the exact longitudinal descendant, the weighted C403 spatial sum and
spin/color identities.

A separate matrix-free action reshapes the qg vector into

`(partition, intrinsic_HO, spin_pair, triplet_color)`

and applies independently materialized single-member kernels in a batched
route. It does not call the weighted sparse aggregate under test.

## 7. Fail-closed surfaces

Attempts to omit graph-member weights, use an incomplete weight map, use the
C407 I2 composition for the q-sector `J_qJ_q` I4 graph, or use it for the
`J_gJ_g` derivative-density graph raise typed errors. Attempts to apply a
complete C117 action also fail closed.
