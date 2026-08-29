# C114/ICURRENT implementation report

Status: `C114_ICURRENT_FINITE_BASIS_PROJECTION_INCOMPLETE`.

The exact C43 Gauss-law authority is frozen as
`P^-_IC=-(g_s^2/2)∫[(i∂^+)^{-1}Q0 j_a^+]^2`, with
`j_q=\barψγ^+T^aψ` and `j_g=-f^{abc}A_\perp^b∂^+A_\perp^c`.  The
finite-cell nonzero-transfer kernel is `L^2/(π^2 n^2)` for
`exp(-iπ n x^-/L)`, and the coordinate and ordered-Fourier derivations
agree exactly.  Eight cross-sector entries are exact even-gluon-parity
zeros; eight diagonal entries remain unavailable because the source does
not provide the required finite-HO HO/spin/color/regulator evaluation.

No missing current term is represented by zero.  No C110 normalization is
applied outside its proven field-content scope.  No physical coupling,
counterterm coefficient, C53 propagation, C112 value, or complete local-QCD
polynomial is constructed.  The complete-block API fails closed.  The sole
continuation is `C115/ICHO` for the transverse-HO current projection.
