# C138/HQCDINPUT3 implementation report

Baseline: `d851e0e984d4c32c5bdd35460f54c6c75e1ec159`
Import contract: `docs/next_level/c137_c138_hqcdinput3_import_contract.json`
Contract SHA-256: `bd73c9a31505612c210651f2431b8e4eeaf8620e29eb467aa571b3197d29c962`
C137 package root: `96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c`
C138 package root: `075c29f17e149b35ae2b78dcbc0f33c25d7457b321fd01479238cecd875eec9b`

Plan INPUT3-C is selected because no authorized numerical capsule files are
present. The exact request contains two required inputs: `M_R2_FB` in GeV²
for `C136_MASS_K9` and `g_R_FB(K_R)` dimensionless for
`C136_VERTEX_LONGITUDINAL`. Both identified-coordinate/operator bindings are
closed and the C137 map remains available, but numerical evaluation fails
closed. The nine null coordinates remain explicit and unresolved. No C8–C14,
PDG, physical-hadron, ART25, TMD, test, example, or diagnostic value was
mined or used as a default. The contract-frozen status is
`C138_HQCDINPUT3_EXTERNAL_INPUT_INCOMPLETE`; continuation is
`C139/HQCDINPUT4`.
