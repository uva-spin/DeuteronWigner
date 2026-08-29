# Q1/PLHQCDSTATE

Continue from Q0/PLHQCD0 in the same isolated worktree.

Consume Q0 and C131/C142/C144/C149/C150 only through immutable public APIs.
Do not consume, modify, merge, or wait for the concurrent C151/HQCDG2PT
worktree.

Implement source-compatible physical-subspace state preparation and state-level
diagnostics for the existing K9/K11/K13 compact-index embedding. Preserve the
`q followed by qg` basis order, exact padded physical projector, leakage checks,
and the sparse Hamiltonian boundary from Q0.

Do not begin VQE, choose an ansatz, select a physical parameter or kinetic
scheme, construct a counterterm/null representative, or produce a hardware,
TMD, fit, or production result. Keep the primary exact oracle on
`lightning.qubit`, `shots=None`, and `complex128`.
