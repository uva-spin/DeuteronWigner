# C406 ChatGPT-stage implementation report

## Result

C406 implements the source-qualified one-gluon normal-order descendant of the C192 gluon current and closes the C405 BRA/KET derivative-assignment ambiguity for the two mixed current products. It also proves the mixed-current q-sector block is exactly zero and separates the still-unresolved same-species contraction problem.

Accepted baseline:

```text
4dbb0b8bbadc540f0da2337c46040afb971fffc1
```

Status:

```text
C406_C117_I2_ONE_GLUON_NORMAL_ORDER_DESCENDANT_AND_MIXED_CURRENT_ROUTING_READY_SAME_SPECIES_CONTRACTIONS_UNRESOLVED
```

## Implemented source layer

The implementation binds

\[
J_g^{+a}=-f^{abc}A_\perp^b\partial_-A_\perp^c
\]

to the exact one-gluon number-preserving descendant

\[
-(k_{\rm bra}+k_{\rm ket})(F^a)_{bc},
\qquad (F^a)_{bc}=-if^{abc}.
\]

The two normal-order terms are retained separately. The bosonic commutator vanishes through `f^{abb}=0`. An independent finite-boson Fock-space reconstruction verifies the result.

## Mixed-current routing

For `J_qJ_g` and `J_gJ_q`, C406 proves

```text
C406 = -(C405_BRA + C405_KET)
```

exactly for K9, K11, and K13. Sparse and independently evaluated matrix-free qg kernels are implemented, together with their adjoint relation and the exact mixed-current q-sector zero block.

For `J_qJ_q` and `J_gJ_g`, C406 fails closed and requires explicit intermediate one-particle contraction axes. The C405 external-pair stress kernels are not promoted.

## Evidence counts

```text
one-gluon external mode-pair rows:       77
product-routing rows:                    12
mixed routing rows:                       6
same-species unresolved rows:             6
mixed numerical kernel rows:              6
C406 K-local binding rows:                 3
complete C117 numerical apply paths:       0
complete C396 numerical apply paths:       6
```

## Validation

Required tests:

```text
C406 focused:                         24 passed
C405 regression:                      21 passed
C404 regression:                      15 passed
C403 regression:                      16 passed
C401 regression:                      14 passed
C400.S2 regression:                   26 passed
C114/C115/C117/C119 regression:       12 passed
C45/C47 selected regression:           4 passed
C151 convention regression:            4 passed
------------------------------------------------
Required total:                       136 passed
Failures:                               0
```

The historical C192 test remains blocked by the pre-existing absent C77 runtime package. C406 does not import the historical C192 execution chain; it verifies the exact C192 source text and hash directly and does not regenerate unavailable runtime artifacts.

Two independent clean generator builds are byte-identical.

## Scientific boundary

C406 does not establish a complete C117 coordinate action, a complete C396 forward map, physical response rank, a physical fit, or activation. The smallest remaining object is the source-qualified same-species one-particle contraction family plus the unresolved complete normalization and target aggregation.
