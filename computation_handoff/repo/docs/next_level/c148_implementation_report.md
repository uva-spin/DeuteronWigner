# C148/HQCD2PTFULL implementation report

Status: `C148_C147_SOURCE_DERIVED_CONSTRAINED_POSITIVE_FREQUENCY_FULL_SPINOR_TWO_POINT_READY`.

C148 consumes C147 through its public coordinate-field and mode-space APIs.
The C43 constraint is factored into `K_perp`, signed `m_q K_mass`,
`g_s K_A`, and the preserved `K_boundary/zero` interface. The q bad source
is q-supported; the qg bad source is constructed from an explicit
`A_perp psi_plus` composite with a mode-wise inverse-`partial_plus` action.

The four blocks `S_++`, `S_-+`, `S_+-`, and `S_--` are exposed with explicit
source orientation. `S_++` reproduces C147. Direct sparse, retained-block,
matrix-free, and constraint routes are public and route diagnostics close.
The Schur complement remains a resolvent identity, never a Hamiltonian.

Instantaneous contacts are ledgered separately from C112/C127 terms,
zero-mode/boundary interfaces, and the unavailable negative-frequency
antiquark sector. Signed mass-linear structure is preserved separately from
the M²/m_q² layer, and the mass-projector API remains uncreated.

No physical mass, coupling, Z_q, counterterm, null representative, state,
spectrum, or downstream object is created. The next continuation is
`C149/HQCDMPROJ` for the independently normalized mass projector.
