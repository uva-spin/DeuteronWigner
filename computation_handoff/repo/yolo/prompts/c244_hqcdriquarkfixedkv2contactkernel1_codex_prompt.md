# C244/HQCDRIQUARKFIXEDKV2CONTACTKERNEL1 Codex Work Package

Mission: implement retained-ID-free spin/polarization, ordered-color, and
exact four-HO contact evaluation for C243 complement coordinates. Baseline
`c001064d965c81542a7838f630d8239325bb5662`; C243 root
`f72f0480d375245caaac7b94e7d6d262c441330881115454ea29b5066bc83287`.
Contract `docs/next_level/c243_c244_hqcdriquarkfixedkv2contactkernel1_continuation_contract.json`
SHA-256 `c01b90a44c4e1d62af723264df2201ea8092083c16c15d4dd03c88f3c09215fb`.

Read C43/C45, C55, C80, and C220-C243 via verified APIs. Preserve C80 gamma
order, polarization phases, ordered `T^aT^b` color, exact longitudinal factor,
four-HO normalization, APBC/PBC modes, PV/Q0, orientations, units, and caller
parameters. Require exact parity on retained overlap holdouts while accepting
arbitrary valid complement tuples. Choose one mutually exclusive plan and
preserve incomplete values as unavailable, never zero.

Implement immutable safe APIs under
`src/deuteron_wigner/bridge/hqcdriquarkfixedkv2contactkernel1/`; prove direct
and factorized route parity, conservation, Hermiticity, dimensions, no
retained-ID dependence, and deterministic serialization. Generate `c244_*`
evidence, two clean builds, regressions, and at least 384 mutations. Commit
once, publish one successor contract/full prompt, atomically advance state,
and continue. Never push; stop only for certified blocker or
`PENNYLANE_PHYSICAL_ACTIVE`.
