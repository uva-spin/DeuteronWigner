# C13/H6 API

`deuteron_wigner.microscopic.h6` defines the seven-sector H6 validation
state, explicit higher-Fock support, and strict second-order quark Wilson
benchmark. It reuses the H3 state ancestry, H4 matrix parent, and C5/C6
Wilson conventions.

`H6ColorBasis.construct` supplies common-total-generator nullspace
certificates for `QQQGG`, `QQQUUBARG`, and `QQQDDBARG`, with invariant
multiplicities 6, 8, and 8. `TwoGluonExchangeSymmetry` requires the product
of color and spin-orbital exchange parities to be bosonic.

`basis_tower`, `build_hamiltonian`, and `renormalization_trajectory` create
three resolution levels, Hermitian generated-adjoint couplings, refitted
mass counterterms, holdouts, and one visible Jacobian null direction.

`support_table` makes first-order quark, antiquark, and gluon support
explicit. Only the quark has second-order support; unsupported requests fail
through `require_support`.

`strict_dyson` and `strict_magnus` return polynomials truncated exactly at
order two. `dyson_magnus_oracle` covers commuting and noncommuting SU(3)
paths without comparing against a full Magnus exponential.

`SecondOrderSpectralRule` separates two single-cut surfaces and the real
double-cut intersection. `second_order_soft` implements signed first- and
second-order subtraction tests. Diagnostics export color, Hamiltonian,
Krylov/TTN, Wilson, spectral, soft, gauge, convergence, and readiness data.
