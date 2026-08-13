# C109 C80 schema-versus-science audit

C80 declares its `Pminus_coefficient` in GeV, but its implemented factors
are a dimensionless longitudinal factor, dimensionless representative
spin/polarization and color factors, and a four-HO overlap carrying
`b_HO^2` (GeV²). The persisted central value therefore does not establish a
true P-minus dimension. Its M² field remains `2*P_plus*(Pminus_coefficient)`.

This is `NORMALIZATION_INCOMPLETE`, not a frame choice. C109 does not select
P⁺ or L and does not form products or a contact operator.
