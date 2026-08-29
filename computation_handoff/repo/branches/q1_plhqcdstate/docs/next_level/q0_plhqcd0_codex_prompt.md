# Q0/PLHQCD0

Proceed with Q0/PLHQCD0.

## Authoritative baseline

`8b866b3d69276b976c913ab23842aa5d9b171018`

This is a new parallel quantum-computing track. Do not consume, modify,
merge, or wait for the concurrent C151/HQCDG2PT worktree.

Consume C131/C142/C144/C149/C150 only through immutable public APIs.

Implement the actual K9/K11/K13 compact-index operator backend, not an
unrelated toy Hamiltonian.

Close:

- public authority import
- basis-to-bitstring encoding
- physical-subspace projector
- certified padded Hamiltonian
- PennyLane SparseHamiltonian expectation oracle
- classical/sparse/matrix-free/encoded/QNode parity
- sector and leakage diagnostics
- exact derivative parity
- resource and Pauli-decomposition boundary

Do not begin VQE or select an ansatz in Q0.

Use an isolated Python 3.11-or-newer PennyLane environment. Do not alter the
project's existing Python 3.9 environment.

Use `lightning.qubit`, `shots=None`, `complex128` for the primary exact oracle.

Do not use a generic full Pauli decomposition as the production compiler.

Do not rescale the Hamiltonian with C150 Z_q or select a kinetic scheme
implicitly.

Do not create a physical parameter, counterterm, null representative, VQE
state, hardware result, TMD, fit, or production object.

Create exactly one Q1 continuation, preferably Q1/PLHQCDSTATE after positive
closure.

Create one local completion commit, do not push, and leave the protected paths
untouched and outside Git.
