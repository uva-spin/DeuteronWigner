# C145/HQCD2PTQ2 implementation report

Status: `C145_C144_SOURCE_DERIVED_PARAMETERIZED_FORWARD_QUARK_GOOD_COMPONENT_TWO_POINT_READY`.

The exact C144 baseline is consumed through its public API. Every numerical
call requires exactly one explicit `parameter_record` or fixture ID. The
deterministic atlas contains the four C144 fixtures and rational complex-z
queries in GeV²; `Im(z)` is an analytic coordinate and never a physical
width.

Plan `2PTQ2-A` closes the source-projected forward good-component authority.
Route A uses sparse six-right-hand-side full-space solves, Route B uses the
retained q/qg block-resolvent identity, and Route C uses independent
matrix-free Krylov solves. No dense full inverse is constructed and no Schur
complement is promoted to a Hamiltonian. Route residuals and analytic,
positivity, source-weight, and high-energy checks close for the diagnostic
atlas.

The positive-frequency conversion is retained symbolically as
`G_psi+ = R_M2/(2 P_plus)` with `P_plus = pi*K/L`, symbolic L, the C142
source normalization, C45 good-spinor projector, and positive-frequency
Fourier convention. Negative-frequency antiquark contributions remain
absent by authority scope.

The inverse source two-point, retained qg self-energy
`B(zI-D)^-1 C`, and order-g_s² ownership ledger are exposed. A/B null-shift
fixtures preserve identified coordinates while changing matrix-valued null
directions; no representative is preferred. The mass-sign diagnostic does
not infer a signed short-distance mass.

No physical coupling, mass, counterterm, pole, state, spectrum, full Dirac
propagator, or downstream object is created. Continuation:
`C146/HQCD2PTFULL`.
