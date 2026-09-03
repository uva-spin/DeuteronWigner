# C146/HQCD2PTNORM implementation report

Status: `C146_C145_M2_RESOLVENT_READY_GOOD_COMPONENT_NORMALIZATION_INCOMPLETE`.

The exact operator algebra closes independently:

`z I - M² = 2 P⁺ (p⁻ I - P⁻)` and therefore
`R_Pminus = 2 P⁺ R_M2`, with `P⁺ = πK/L` symbolic,
`[R_M2] = GeV^-2`, and `[R_Pminus] = GeV^-1`.

C145's M² resolvent, sparse/block/matrix-free routes, self-energy, and
diagnostic boundaries are preserved. The reported field relation
`G_psi+ = R_M2/(2P_plus)` is not promoted: the authenticated C142 source map
is a unit q-state Gram/isometry, but it does not independently publish the
coordinate-field source and sink factors required to determine the final
field-correlator normalization. The factorization is kept explicit as
kinematic `2P⁺`, source, sink, C45 good-spinor, Fourier/i, and finite-cell
factors; the net field factor remains unresolved.

Free K9/K11/K13 and interacting A/B holdouts close the kinematic relation
without selecting numerical L, P⁺, a physical parameter, counterterm, or
null representative. No antiquark, full-spinor, physical pole, or state is
created.

Continuation: `C147/HQCDFIELDNORM`.
