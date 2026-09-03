# C406 mathematical and algorithmic design

## A. Exact normal-ordering algebra

C406 treats the C192 source current as an ordered bilinear. The derivative remains on the second source field until the mode expansion is inserted. The two number-preserving terms are calculated separately, including the source minus sign and the C45 phase convention. Bosonic reordering produces a diagonal commutator term; adjoint-color antisymmetry kills it exactly.

No symbolic simplifier is permitted to drop one of the two number-preserving contributions. The final coefficient is tested both algebraically and by a finite truncated bosonic Fock-space construction restricted to the one-particle sector.

## B. Exact arithmetic and normalization layers

Mode labels are stored as `Fraction` objects. The raw dimensionless factor

\[
-(k_{\rm bra}+k_{\rm ket})
\]

is exact. The C151 canonical one-gluon factor is evaluated only after the exact mode check:

\[
-(k_{\rm bra}+k_{\rm ket})/(2\sqrt{k_{\rm bra}k_{\rm ket}}).
\]

The common box/current-density scale and the complete C117 product normalization are kept distinct. This prevents a route-specific one-body normalization from being promoted into a full Hamiltonian coefficient.

## C. Product routing

Products are partitioned into two classes:

- mixed: `J_qJ_g`, `J_gJ_q`;
- same species: `J_qJ_q`, `J_gJ_g`.

Only the mixed products use the external qg partition-transfer kernel. For them, the C406 normal-order result is compared exactly against the sum of the two C405 conditional candidates. The residual is represented with exact rational arithmetic and must vanish identically.

Same-species products raise a typed runtime error if passed to the mixed route. Their evidence records identify the required intermediate particle and explain why external transfer is insufficient.

## D. Sparse and matrix-free mixed kernels

The qg basis factorization is

\[
\text{partition}\otimes\text{relative HO}\otimes\text{spin}\otimes\text{triplet color}.
\]

The sparse route uses Kronecker products. The matrix-free route applies color, spin, spatial, and longitudinal factors independently. The spatial C403 ordering is explicitly permuted into C47 ordering. No matrix-free call delegates to the assembled sparse matrix.

The adjoint of `J_qJ_g` is tested against `J_gJ_q`. The full q-plus-qg direct-sum route inserts the q block only through the exact mixed-current zero certificate.

## E. Validation surface

The focused tests cover:

1. source authority and phase conventions;
2. exact normal-order coefficients and commutator cancellation;
3. invalid longitudinal modes;
4. C151 route symmetry;
5. adjoint-color Hermiticity;
6. independent finite-Fock-space reconstruction;
7. exhaustive 77-row external mode inventory;
8. all eight adjoint generators and all three resolutions;
9. exact collapse of every mixed C405 BRA/KET candidate;
10. sparse versus independent partition action;
11. exact q-sector zero;
12. same-species fail-closed behavior;
13. routing counts;
14. sparse/matrix-free/adjoint/direct-sum mixed kernels;
15. binding and completion counts;
16. forbidden-shortcut source scan.

## F. Deterministic evidence

The generator serializes exact fractions as numerator, denominator, exact string, and floating value. Generated evidence excludes `generation_result.json` from its own content root. Two clean output directories must produce byte-identical artifacts.
