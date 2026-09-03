# C407 ChatGPT-stage implementation report

## Scope

C407 is prepared against the accepted local C406 merge baseline
`4f932604483701d18158164288674cea82a07b3f`. It derives and implements the
finite same-species longitudinal intermediate-mode descendants required by the
`J_qJ_q` and `J_gJ_g` products of the C117 `I2` direction.

## Implemented result

The source-qualified C45/C47/C114/C115/C119 chain gives an exact finite axis

\[
  r\in\mathcal M_{s,K},\qquad q=r-k\ne0,
\]

for each external same-species mode. Across K9, K11 and K13 the generated
inventory contains 154 rows, no zero-transfer entries, no noninteger transfers
and no duplicate entries.

After factoring the common source coefficient and unresolved finite-cell,
field, state and \(M^2\) normalization, the exact longitudinal weights are

\[
  w_q(k,r)=\frac{C_F}{(r-k)^2},\qquad C_F=\frac43,
\]

and

\[
  w_g(k,r)=\frac{C_A}{(r-k)^2}\frac{(k+r)^2}{4kr},
  \qquad C_A=3.
\]

Independent finite fermionic and bosonic Fock-space calculations validate the
normal-ordering sign and multiplicity.

C407 also provides a numerical `J_qJ_q:qg->qg` composition interface joining
the exact longitudinal descendant to the individual C403 spatial kernels.
The C117 source retains explicit graph-member weights `w_r`; no authenticated
numerical weight set exists. The interface therefore requires a complete
caller-supplied weight mapping and rejects missing, partial, duplicate,
nonfinite or out-of-axis mappings.

A deterministic nonuniform weight fixture is used only to validate sparse and
independently evaluated matrix-free composition. It is explicitly nonphysical
and is not an operator binding.

## Corrective design decision made before packaging

An earlier internal draft used implicit unit weights for every C403 graph
member. That would have violated the source-owned C117 weighted-sum semantics
and the project rule that unavailable coefficients are not zero or one. The
final implementation removes that shortcut and has no unit-weight or
minimum-norm default.

## Truthful boundary

C407 does not provide the source-authorized graph-member weights, the
`J_qJ_q:q->q` I4-local transverse action, the `J_gJ_g:qg->qg`
derivative-density transverse action, q-sector gluon pair/vacuum branches,
complete normalization, target aggregation, `g_s^2`, or `c_C117_1`.

Therefore:

```text
complete numerical C117 apply paths: 0
complete numerical C396 apply paths: 6
physical rank: RANK_NOT_EVALUATED
physical fit: unauthorized
activation: NOT_READY
```

## Validation

The final C407 focused suite passes 26 tests. C406, C404 and C403 regressions
pass in the reconstructed review repository. Additional available subsets of
C405, C401 and C400.S2 pass; tests requiring historical files absent from the
replay snapshot are recorded separately and remain mandatory in the live
canonical repository.
