# C410 mathematical and algorithmic design

## 1. Vacuum pair witness

For one Cartesian transverse-polarization witness, define a one-gluon mode by longitudinal momentum `k>0` and adjoint color. The ordered pair-creation coefficient from the source current uses the second-slot derivative and canonical mode factors,

\[
\Gamma^a_{bc}(k_b,k_c)
=(F^a)_{bc}\frac{k_c}{2\sqrt{k_bk_c}}.
\]

The normalized unordered two-boson pair coefficient is obtained by summing both source orders. Since `(F^a)_{cb}=-(F^a)_{bc}`,

\[
\Gamma^a_{bc}+\Gamma^a_{cb}
=(F^a)_{bc}\frac{k_c-k_b}{2\sqrt{k_bk_c}}.
\]

It vanishes for equal longitudinal momenta and is generically nonzero for unequal momenta. The pair-annihilation branch is its adjoint, so the vacuum product is the pair-state norm. This validates source presence but does not compute the physical vacuum-energy coefficient.

## 2. Projection into the retained connected Hamiltonian

The full-source q-sector branch is a spectator identity times a vacuum c-number. The project’s C129/C131/C136 scheme routes this to the nonmatrix vacuum direction. The retained connected matrix is the full spectator term minus its vacuum direction and is exactly zero. The implementation records the diagnostic scalar only to verify this algebra; it never serializes it as a physical Hamiltonian contribution.

## 3. Product routing

C410 imports only the accepted source-routed primitives:

- `J_qJ_q`: C408 direct-sum primitive;
- `J_qJ_g`: C408/C406 mixed source order;
- `J_gJ_q`: its explicit source-order partner;
- `J_gJ_g`: C409 qg block plus C410 exact retained q zero.

The aggregation is a direct sum of all four blocks with multiplicity one. The matrix-free route calls each product action independently and therefore does not reuse the sparse sum.

## 4. Source coefficient and normalization boundary

The common C114 factor `-1/2` is applied exactly once. The C259/C260 convention keeps `g_s^2` factored from the four C117 operator directions. The derivative with respect to `c_C117_1` does not require a chosen value of that coordinate.

The result cannot be called `O_C117_1,R` until C260/C262 supplies the finite-C43 mapping and remaining field, external-state, `P^-`-to-`M^2`, and normalized-wavepacket convention.

## 5. Validation

The acceptance suite checks:

- source hashes and exact source phrases;
- nonzero unequal-momentum and zero equal-momentum pair witnesses;
- no full-source vacuum-zero claim;
- exact retained q-sector zero after explicit routing;
- exact source-product multiplicity;
- sparse versus independent matrix-free agreement;
- Hermiticity and mixed-order adjoint relations;
- exact `-1/2` scaling;
- fail-closed normalization capsule validation;
- unchanged C396 complete-path count;
- Python 3.9 compatibility and absence of C144 proxies or minimum-norm defaults.
