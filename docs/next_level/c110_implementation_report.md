# C110/IFKERNELNORM2

Status: `C110_C80_SOURCE_DERIVED_FIELD_NORMALIZED_BOOST_INVARIANT_M2_KERNEL_READY`.

The missing inverse-energy factor is uniquely localized to the two
transverse gauge-field insertions. Route A (source expansion through the
finite cell) and Route B (canonical transverse commutator, unit one-gluon
norm, qg Gram, and C74 isometry) both give

`N_field = L/(2*pi*sqrt(k_g_out*k_g_in))`.

Thus the descendant corrected P-minus kernel is `N_field*C80` with GeV/g_s²
units. Using `P^+=pi*K/L`, its M² kernel is
`K/sqrt(k_g_out*k_g_in)*C80`, with GeV²/g_s² units. Arbitrary L and P⁺
cancel exactly. C80 remains unchanged; no C107 product, contact entry,
coupling, C53, C58, or counterterm is created.

The immutable public surface also exposes `gluon_field_normalization`,
`qg_state_normalization`, and `normalization_ancestry`; these return frozen
symbolic/source-ancestry records and never select numerical L or P⁺. The
normalization adapter is on-demand and contains no expanded logical payload.
