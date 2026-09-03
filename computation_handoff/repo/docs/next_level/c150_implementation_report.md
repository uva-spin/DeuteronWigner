# C150/HQCDZQMASS implementation report

Status: `C150_C149_SOURCE_DERIVED_CONDITIONAL_FINITE_BASIS_ZQ_MASS_SCHEME_FAMILY_READY`.

C150 consumes C149 read-only and requires an explicit off-shell subtraction
record, explicit `kinetic_scheme_id`, and exactly one C144 fixture or caller
parameter record for every numerical operation. The registry contains the
three distinct schemes `K_MINUS`, `K_PLUS`, and `K_PERP`; no averaging or
implicit selection is allowed.

The declared convention is `psi_R=sqrt(Z_q) psi_B`, with
`Gamma_hat_k=Gamma_B/A_k`, `Z_q=A_k`, and
`m_R,k^FB=B_mass/A_k`. Tree limits and the chiral guard for `Z_m` are
explicit. Unselected coefficients are exposed as restoration diagnostics
`A_j/A_k`, not statistical uncertainty. Internal conversions are finite-
basis scheme conversions only and are not MSbar or physical conversions.

Four ratio/reprojection routes close with zero mismatches. Prospective
renormalization rank remains 2 with nine null coordinates; no physical
`Z_q`, mass, scale, counterterm, null representative, state, or continuum
extrapolation is created. The next continuation is `C151/HQCDG2PT`.
