# C409 mathematical and algorithmic design

## Exact factorization

For an external gluon mode `k` and an intermediate nonzero PBC gluon mode `r`,
with transfer `q=r-k != 0`, the C409 weight is reconstructed from three
independent source-owned factors:

\[
K_{Q_0}(k,r)=\frac{1}{(r-k)^2},
\]

\[
G(k,r)=\frac{(k+r)^2}{4kr},
\]

\[
C_A=3.
\]

Their product is

\[
C_A G(k,r)K_{Q_0}(k,r)
=\frac{3(k+r)^2}{4kr(r-k)^2},
\]

which is checked exactly, using rational arithmetic, against every C407 gluon
same-species row at K9, K11, and K13.

## Transverse implementation

The C403 single-member matrices are generated in C403 HO order. C409 sums all
source-admitted members with multiplier one and then applies the existing
C47-to-C403 permutation on both matrix axes. A separate matrix-free route:

1. maps C47 vectors into C403 order;
2. applies every C403 member action independently;
3. sums the results;
4. maps the result back to C47 order.

It does not call the assembled sparse matrix.

## Product-block basis

The qg basis ordering is

```text
partition, intrinsic transverse-HO mode,
quark helicity, gluon polarization, triplet color
```

and the product block is assembled as

```text
C407 longitudinal diagonal
x C409 reduced spatial sum
x C404 spin identity
x residual triplet-color identity.
```

The residual color identity is required because the C407 longitudinal
coefficient already includes the exact adjoint Casimir. A validation route
divides that longitudinal factor by three and restores the C404 `3 I_3` color
matrix; the two matrices must agree.

## Numerical contracts

The sparse and matrix-free routes must agree to `5e-10` in vector norm at each
resolution. The matrix must be Hermitian to `5e-12`. Positivity is established
factorwise from a positive longitudinal diagonal and the C403 positive
semidefinite spatial sum.

All vector inputs must be finite and exactly match the qg dimension. There is
no complete direct-sum API because the q-sector number-changing gluon branches
remain unresolved.

## Compatibility

The code is written for the canonical Python 3.9.6 environment. It uses no
runtime PEP 604 aliases, `int.bit_count`, or `zip(..., strict=...)`.
