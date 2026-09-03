# ADR 037: Hamiltonian resolution and scale separation

**Decision:** Store exact \(K\), \(N_{\max}\), oscillator scale, Hamiltonian
scale, endpoint regulator, and boundary conditions in one immutable
`HamiltonianResolution`, while retaining distinct scale value types.

**Reason:** Equal numerical values do not make basis, Hamiltonian,
renormalization, and factorization scales interchangeable.

**Status:** Implemented and fail-closed in C7/H0.
