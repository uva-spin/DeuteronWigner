# Q1/PLHQCDSTATE implementation report

Status: `Q1_PLHQCDSTATE_COMPLETE`.

Q1 consumes the immutable public Q0 backend from frozen completion commit
`b094fb8cb1046aea0062468d73826ea25eab6116`. Q0 is unchanged. The Q1 backend
uses the `COMPACT_INDEX_DIRECT_ORDER_V1` encoding, with K9's actual 1,350
compact states embedded in an 11-qubit, 2,048-state padded register. The basis
order remains `q followed by qg`.

## Routes

The exact route computes the lowest sparse/Krylov eigenstate and validates its
energy through the bounded `lightning.qubit`, `shots=None`, `complex128`
StatePrep oracle. This route is validation-only.

The production variational route uses a Hamiltonian-edge ADAPT pool. For K9,
the deterministic initial gradient selection chooses the authenticated
`EDGE-00-0-6:real` generator. Every selected two-level rotation is expanded to
ordinary CNOT, Pauli, Clifford, and single-qubit rotation gates; no
`QubitUnitary` is emitted. The circuit preserves zero padded-state amplitude
by construction. Optimization uses a deterministic QNode objective minimizer;
hardware, shots, cloud, and noise execution are disabled.

The explicit continuation sequence is:

1. `FIXTURE-FREE`
2. `FIXTURE-INTERACTING-A`
3. `FIXTURE-INTERACTING-B-NULL-SHIFT`
4. `FIXTURE-MASS-SIGN`

K9 is fully optimized with warm-started parameters. K11 and K13 are retained
as regression/resource holdouts and are not variationally optimized.

## Acceptance vector

The acceptance report tracks energy residual, eigenstate residual norm,
fidelity/principal angle, `P_q`, `P_qg`, `P_padding`, owner and coupling-degree
fingerprints, exact derivative/Hellmann-Feynman parity, source overlaps,
mass-sign response, and null-shift response. Positive status requires the
declared vector, not energy alone.

No physical mass, coupling, flavor, counterterm, null representative, kinetic
scheme, PDG input, Wilson/TMD operator, physical state, spectrum claim, fit,
or production object is selected.

## Validation

The machine-readable result is `q1_plhqcdstate_acceptance.json`. The build
entry point is `scripts/build_q1_plhqcdstate.py`.

The final local validation covers the Q0 boundary, all four explicit K9
fixtures, ordinary-gate decomposition, exact StatePrep parity, full K9
optimization, K11/K13 resource holdouts, derivative parity, and continuation
responses. The sole continuation is `Q2/PLHQCDOBS`.
