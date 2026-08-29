# ADR 017: minimal positive-x sea benchmark

Status: accepted for validation only.

Use the orthogonal direct sum `|qqq> + |qqqq qbar>` with explicit positive-x
quark and antiquark slots. The first member uses a neutral `d dbar` pair.
Sector probabilities are stored before observable evaluation and sum to one.
Negative-x copying is rejected.

The five-parton color state is the normalized cluster tensor
`epsilon_abc delta_de / sqrt(18)`. It is an exact total singlet but is
explicitly not claimed to be a fully antisymmetrized five-body nucleon basis.
This construction tests selection, color, number, charge, momentum, and
reduction algebra without presenting a phenomenological sea distribution.
