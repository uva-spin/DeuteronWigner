# C157/HQCDMATCHIR2 implementation report

Status: `C157_HQCDMATCHIR2_FINITE_BASIS_NUMERICAL_INCOMPLETE`.

C157 consumed the sole committed import contract
`docs/next_level/c156_c157_hqcdmatchir2_import_contract.json` (SHA-256
`d5fb657cf7dc9fa3366aa3215f2f261969aa9a46d3c16b0e97fe19975d7976c4`). The
C156/C155/C154/C153/C152/C151/C150/C144 roots are hash-locked and unchanged.

The selected plan is `MATCHIR2-B`: the public C153 finite-basis surface
returns a symbolic coefficient label and no executable AST or numerical
enclosure. C157 fails closed at that first missing object. The continuum,
common-IR, derivative, conversion, remainder, and bracket authorities are
typed and explicit but remain blocked by that missing finite-basis evaluator.

All calls require explicit rho, mu, scheme, active N_f, external state, IR
prescription, order of limits, and exactly one parameter record or fixture.
Remainder calls additionally require an explicit coupling/log envelope.
Missing sectors are not zeroed. No PDG/FLAG/ALPHA value, running, threshold,
physical scale, full C156 grid, Q0/Q1 object, state, or TMD was created.

The sole continuation is `C158/HQCDFBNUM`.
