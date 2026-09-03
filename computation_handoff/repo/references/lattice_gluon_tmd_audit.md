# Lattice-QCD and perturbative-QCD audit for nucleon gluon TMD inputs

Date: 2026-07-24

## Scope and conclusion

This audit is deliberately restricted to lattice QCD and perturbative QCD.
Spectator models and phenomenological TMD extractions may be used to compare
definitions, but they are not numerical inputs to the deuteron calculation.

No published numerical lattice calculation was located that presently fixes
the proton's nonperturbative \(b_T\) or \(k_T\) dependence for
\(f_1^g\), \(g_1^g\), or \(h_1^{\perp g}\). The published lattice literature
does provide the LaMET factorization and matching needed to ingest such data
when it becomes available. Consequently, it would be incorrect to label the
current Gaussian profile "lattice constrained."

The immediate controlled improvement is instead a \(b_T\)-space model with:

1. perturbative small-\(b_T\) operator-product matching;
2. the existing collinear \(g(x,\mu)\) and \(\Delta g(x,\mu)\) inputs;
3. perturbatively generated \(h_1^{\perp g}\);
4. an explicitly varied, nonperturbative large-\(b_T\) remainder.

## Source audit

| Source | Result | Numerical lattice data? | Usable now |
|---|---|---:|---|
| Schindler, Stewart, Zhao, arXiv:2205.12369, JHEP 08 (2022) 084 | One-loop factorization of gluon quasi-TMDs onto Collins TMDs; spin-independent matching coefficient and no quark mixing at this order | No | Defines matching and scheme-conversion requirements for a future lattice-data reader |
| Zhu, Ji, Zhang, Zhao, arXiv:2209.05443, JHEP 02 (2023) 114 | LaMET extraction framework and one-loop matching for unpolarized and helicity gluon TMDs | No | Operator and matching conventions for \(f_1^g\) and \(g_1^g\) |
| Zhao, arXiv:2212.00825 | UV-finite Euclidean degree-of-linear-polarization ratio; soft factor cancels and matching is trivial through one loop | No | Defines a particularly clean future lattice observable related to \(h_1^{\perp g}/f_1^g\) |
| Xie and Lu, arXiv:2512.08292, Phys. Rev. D 113, 054013 (2026) | Perturbative LaMET analysis of the leading-twist gluon TMD operator basis | No | Cross-check of spin-dependent operator matching; not a spectator-model input |
| Gutierrez-Reyes et al., arXiv:1907.03780 | NNLO small-\(b_T\) matching for linearly polarized gluons | Not applicable | Directly usable perturbative boundary condition for \(h_1^{\perp g}\) |
| Zhu, arXiv:2509.01703 | N3LO twist-2 matching for linearly polarized gluon TMDs | Not applicable | Higher-order upgrade after the lower-order implementation and convention checks |
| Avkhadiev et al., arXiv:2402.06725, PRL 132, 231901 (2024) | Continuum-extrapolated **quark** Collins-Soper kernel | Yes, quark | Not a direct gluon numerical input |
| Tan et al., arXiv:2511.22547 | Physical-mass, continuum **quark** Collins-Soper kernel to large \(b_T\) | Yes, quark | Not a direct gluon numerical input |
| Fu et al., Lattice 2024 and 2026 conference material | First numerical gluon Collins-Soper-kernel calculation reported as in progress/preliminary | Preliminary conference result | Track for publication; no stable public numerical dataset identified |

## Input status by distribution

| Distribution | Collinear input | Perturbative transverse information | Published numerical lattice constraint | Project treatment |
|---|---|---|---|---|
| \(f_1^g(x,b_T)\) | CT18 \(g(x,\mu)\) already installed | Small-\(b_T\) OPE and gluon LaMET matching available | None located | Implement matched small-\(b_T\) core; vary large-\(b_T\) completion |
| \(g_1^g(x,b_T)\) | BDSSV24 \(\Delta g(x,\mu)\) and replicas already installed | One-loop helicity-gluon LaMET matching available | None located | Implement matched small-\(b_T\) core with PDF uncertainty; vary large-\(b_T\) completion separately |
| \(h_1^{\perp g}(x,b_T)\) | No independent collinear PDF is required at leading perturbative matching | Matching known through NNLO, with an N3LO result available | No numerical ratio or TMD data located | Generate the small-\(b_T\) term perturbatively; do not introduce an arbitrary fixed fraction of \(f_1^g\) |
| Collins-Soper evolution | — | Perturbative kernel at small \(b_T\) | Published numerical results located only for quarks; gluon result preliminary | Do not substitute the quark kernel as a nonperturbative gluon kernel |

## Important interpretation boundary

Perturbative Casimir scaling and the one-loop spin independence of a matching
coefficient do not establish that a nonperturbative quark Collins-Soper
kernel can be copied into the gluon channel over all \(b_T\). Any such use
would need a stated approximation and a dedicated sensitivity test. It is
therefore excluded from the baseline.

Likewise, a perturbative small-\(b_T\) result does not determine the
large-\(b_T\), low-\(k_T\) shape. The latter remains a declared model
uncertainty until numerical gluon lattice data or another first-principles
constraint becomes available.

## Implementation contract

The next numerical layer should expose

\[
\widetilde F^g(x,b_T;\mu,\zeta)
= \sum_i C_{g\leftarrow i}(x,b_T;\mu,\zeta)\otimes f_i(x,\mu)
\,F^g_{\mathrm{NP}}(x,b_T),
\]

with the perturbative and nonperturbative pieces separately inspectable.
The first implementation should:

- work in \(b_T\) space and declare its TMD and rapidity schemes;
- reproduce the collinear normalization where such a limit exists;
- use a controlled \(b_T\) transition prescription and vary it;
- keep \(F_{\mathrm{NP}}^g\) as a family of nuisance profiles, not a fitted
  central truth;
- generate \(h_1^{\perp g}\) from its matching coefficients at small \(b_T\);
- preserve the existing Gaussian calculation only as a regression and
  sensitivity fixture;
- accept future lattice tables as values plus covariance, ensemble metadata,
  momentum, renormalization scheme, \(\mu\), \(\zeta\), and matching order.

## Primary sources

- https://arxiv.org/abs/2205.12369
- https://arxiv.org/abs/2209.05443
- https://arxiv.org/abs/2212.00825
- https://arxiv.org/abs/2512.08292
- https://arxiv.org/abs/1907.03780
- https://arxiv.org/abs/2509.01703
- https://arxiv.org/abs/2402.06725
- https://arxiv.org/abs/2511.22547

