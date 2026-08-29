# Pretzelosity input and rank-two convention

## Field-theoretic status

Pretzelosity \(h_{1T}^{\perp}\) is a leading-twist TMD, but its small-\(b_T\)
operator product expansion is not an ordinary copy of transversity matching.
Chai, Chen, and Ma, [arXiv:1808.10560](https://arxiv.org/abs/1808.10560),
show that it vanishes to all perturbative orders for a single massless-quark
state and that its nonzero hadronic content is tied to quark-gluon/bound-state
structure and higher-twist collinear operators. Consequently:

- the perturbative small-\(b_T\) central boundary remains zero;
- a nonzero hadronic component is represented separately as a model
  sensitivity, not labeled as a fitted transversity contribution;
- improved lattice or phenomenological inputs can replace the component
  without changing the parent correlator or rank-two Fourier adapter.

## Current configurable ensemble

The Gaussian nonperturbative component is normalized through

\[
 h_{1T}^{\perp(1)}(x)
 = \int d^2 k_T\,\frac{k_T^2}{2M^2}h_{1T}^{\perp}(x,k_T^2),
\qquad
 |h_{1T}^{\perp(1)}|\leq \frac{f_1-g_1}{2}.
\]

The central fraction is zero. Signed sensitivity members use fractions
\(-0.25\) and \(+0.25\) of this moment bound. They are not a confidence
interval. Proton and neutron flavor components remain separate and charge
symmetry rotates both flavor and transverse width.

The parent correlator contains
\(-k_T^{ij}h_{1T}^{\perp}/M^2\). The b-space adapter therefore evolves its
rank-two directional coefficient and inverts it with \(J_2\); it never applies
the scalar \(J_0\) transform.

## Reproduction

```bash
/Users/dustin/miniforge3/bin/python3.9 scripts/audit_pretzelosity_scenarios.py
/Users/dustin/miniforge3/bin/python3.9 -m pytest -q \
  tests/test_nucleon_inputs.py tests/test_quark_tmd_matching.py
```

The scenario audit checks the full joint target/quark spin-density eigenvalues
over proton/neutron, four flavors, four x values, and nonzero transverse
momenta. The zero-evolution tests independently verify the analytic
rank-two Gaussian Fourier round trip, including the \(k_T=0\) limit.
