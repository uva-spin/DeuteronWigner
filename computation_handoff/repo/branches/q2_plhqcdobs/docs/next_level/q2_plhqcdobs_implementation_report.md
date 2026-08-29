# Q2/PLHQCDOBS implementation report

Status: `Q2_PLHQCDOBS_COMPLETE`.

Q2 consumes the immutable public Q0/Q1 interfaces at the Q1 baseline and
keeps the Q0 later-evidence descendant recorded but unconsumed. The package
implements source-structured observables and measurement manifests for K9,
with K11 and K13 retained as resource/regression holdouts. The compact-index
encoding and `q followed by qg` basis order are preserved.

The registry contains 471 records across the three resolutions, including
Q0 total and derivative operators, Q1 owner sums, sector/projector records,
source-overlap diagnostics, and the authenticated ADAPT edge pool. The K9
registry contains 157 records. Hermitian observables are represented by
diagonal bitstring terms and physical two-level edge terms; ADAPT generators
remain explicitly action-only. No dense Pauli enumeration or production
`QubitUnitary` is used.

Validation covers the exact Q1 StatePrep oracle and Q1 variational state on
the four-fixture continuation sequence, source-term compilation, QNode and
matrix-free parity, padding leakage, derivative/Hellmann--Feynman parity,
state residuals, source overlaps, variance-proportional shot-plan creation,
cross-resolution resource counts, and 384 focused mutation boundaries.
The default execution remains `lightning.qubit`, `shots=None`, and
`complex128`; shot plans require caller-explicit budgets or target precision.

The machine-readable result is `q2_plhqcdobs_acceptance.json`. The build
entry point is `scripts/build_q2_plhqcdobs.py`, and the runtime manifest is
`data/runtime/q2_plhqcdobs/manifest.json`.

Q2 remains conditional finite-basis Hamiltonian-diagnostic infrastructure.
It selects no physical parameter, physical state, hardware execution,
production fit, spectrum claim, or TMD/phenomenological observable. The next
continuation is reserved for the subsequent handoff.
