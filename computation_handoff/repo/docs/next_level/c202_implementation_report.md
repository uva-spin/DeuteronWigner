# C202/HQCD4GVERT1 implementation report

Status: `C202_C201_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_FOUR_GLUON_PROPER_VERTEX_AUTHORITY_READY`
Plan: `FOURGVERT1-A`
Baseline: `9f77655bb35cc4ddaec0132d09e9acacbc178f25`
C201 package root: `b1d7f8c51a2aeef71153a7d1a9a51ef50ca8d2d99cc86f312044600042d09a59`

C202 adds a source-qualified, data-only conditional finite-basis four-gluon
proper-vertex package. It preserves ordered G1/G2/G3/G4 legs, all 24 S4
permutations, the three pair channels (`12|34`, `13|24`, `14|23`), separate
color and polarization records, the C43/C129/C131 quartic source, connected
response, C201 three-vertex derivative, C184 inverse two-point second
derivative, owner components, graph-cut subtraction, four-leg amputation,
projectors, conditional dressing, and nonmatrix boundary/link/holonomy
interfaces.

The C197-ST-4 row is replaced incrementally. The six counterterm directions
and nine null coordinates remain unselected. No C158 values, physical input,
Q0/Q1/Q2 mutation, C166 graph mutation, target MOMq coefficient, physical
coupling, state, TMD, or full-ST claim is present.

Verification: the focused C202 suite passed 5 tests; the selected C153-C202
regression set passed 98 tests; 384 live mutation cases passed. Two clean
wheels had identical 564-member payloads with zero member differences. The
isolated unrelated C134 diagnostic remains quarantined (2 passed, 1 known
failure: expected 4, observed 115). The user modification to
`handoff/ROADMAP.md` is preserved.

Next continuation: `C203/HQCDBRST1`, exact object `BRST source identities`
(C197-ST-5).
