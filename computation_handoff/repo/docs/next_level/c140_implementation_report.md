# C140/HQCDPHYSANCHOR implementation report

Baseline: `dbf7451c40d999819ebcfcb1520e5ed925b56406`

The historical `C140/HQCDINPUT5` contract is preserved unchanged but is not
executed. The user-authorized correction selects `PHYS-A`: define a physical
finite-basis anchor through C43-compatible short-distance probes and explicit
matching. Eight required primary sources were downloaded to the ignored
`data/raw/c140_sources/` cache and hash-locked; continuum RI/SMOM, MOMq, and
ALPHA sources are comparison/method authorities, not regulator-identical
conversions.

PDG candidates are recorded but not accepted as project values: the review
reports alpha_s^(5)(m_Z) = 0.1180 +/- 0.0009 and m_ud^MSbar(2 GeV, N_L=4) =
3.397 +/- 0.045 MeV. The project flavor registry does not expose enough
flavor identity to close the finite-basis flavor decision. No standard value
is copied into the legacy `M_R2_FB` or `g_R_FB(K_R)` capsules.

The C43 gauge/regulator identity is frozen, but the C43-compatible quark
two-point/resolvent, short-distance mass projector, field residues, amputated
vertex, conversion functions, and matching window are not available. The
legacy spectral and projected-vertex coordinates remain diagnostics, not
physical anchors. No derived project anchor, RGI value, nullspace coordinate,
full Hamiltonian, state, or downstream object is created.

Status: `C140_HQCDPHYSANCHOR_QUARK_TWO_POINT_INCOMPLETE`.
The sole targeted continuation is `C141/HQCD2PT`.
