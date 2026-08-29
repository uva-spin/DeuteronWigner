# Spin-1 quark correlator convention map

The authoritative momentum-space source is arXiv:1612.06585, Eqs. (5)-(20).
The local PDF is `references/arxiv_1612.06585_spin1_quark_tmds.pdf`.

`Spin1QuarkCorrelator` stores the projections \(\gamma^+\),
\(\gamma^+\gamma_5\), and \(i\sigma^{i+}\gamma_5\). Target matrices are the
orthogonal Cartesian irreps `U,L,T_x,T_y,LL,LT_x,LT_y,TT_x,TT_y`.

At \(k=(k_x,k_y)\), the independently checked contractions are
\(\epsilon_T^{S_Tk_T}=S_xk_y-S_yk_x\),
\(k_T\cdot S_T=k_xS_x+k_yS_y\), and
\(k_T^{ij}S_{TT}^{ij}=S_{TT,x}(k_x^2-k_y^2)+2S_{TT,y}k_xk_y\).
The epsilon-rotated rank-two harmonic is
\((-2k_xk_y,k_x^2-k_y^2)\).

The project matrix `LL` is minus the physical \(S_{LL}\) convention, so
`f1LL` and `h1LLperp` carry an explicit adapter. Transverse sigma
projections use the four-dimensional identity relating
\(i\sigma^{i+}\gamma_5\) to epsilon-rotated \(\sigma^{j+}\) structures.

Time reversal is a relation between gauge links, not a naive
\(k_T\to-k_T\) substitution. `reverse_quark_gauge_link()` reverses exactly
the nine T-odd functions from Table I and leaves the nine T-even functions
unchanged. A transverse reflection alone is not light-front parity:
physical parity also reverses longitudinal momentum and changes the
helicity basis. Parity is therefore checked through the allowed covariant
structures and through the light-front parity reflection \(y\to-y\), whose
target-helicity representation and polar/axial operator transformations are
tested for every one of the 18 structures.

This audit exposed and corrected a missing epsilon rotation in the original
rank-three `h1TTperp` Cartesian projection. Eq. (17) is written with
\(\sigma^{\mu+}\), whereas the stored projection is
\(i\sigma^{i+}\gamma_5\); the conversion requires
\(\epsilon_T^{i\mu}k_T^{\mu\rho\sigma}S_{TT}^{\rho\sigma}\).

The definitions of \(h_1,h_{1LT},h_{1TT}\) are the definite-rank
combinations in Eqs. (18)-(20), not the older primed functions.
