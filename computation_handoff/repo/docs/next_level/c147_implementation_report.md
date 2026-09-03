# C147/HQCDFIELDNORM implementation report

Status: `C147_C146_SOURCE_DERIVED_C43_COORDINATE_FIELD_NORMALIZATION_READY`.

The C146 M² resolvent and retained-qg self-energy are consumed read-only. The
selected route is FIELDNORM-A. C147 derives the finite-cell antiperiodic
longitudinal mode, C45 transverse HO ground mode, C45 good-component spinor,
and the source/sink factorization

`J_R(x) = B_R C_R(x)` and `J_R†(y) = C_R†(y) B_R†`.

The operator identity is `z I-M² = 2 P⁺ (p⁻ I-P⁻)`, hence
`R_Pminus = 2 P⁺ R_M2`, with `2P⁺ = 2πK/L`. The light-front-time Fourier
factor is kept separately as `i`; longitudinal, transverse, spinor, color,
and C142 unit-isometry factors are not compressed into an unexplained scalar.

Routes F-A/F-B/F-C agree with zero route, source/sink, jump, and holdout
mismatches. Free K9/K11/K13 and explicitly named C144 diagnostic fixtures are
covered. No physical parameter, L, P⁺, Z_q, antiquark block, full-spinor
propagator, state, spectrum, or downstream object is created.

The C148 continuation is `C148/HQCD2PTFULL`; it must consume this authority
and perform the complete full-spinor/two-point task without changing C145 or
C146.
