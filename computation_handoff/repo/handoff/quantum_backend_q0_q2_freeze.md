# Q0–Q2 conditional quantum backend freeze

Date: 2026-08-23

Status: **accepted and frozen locally**.

This note is the durable handoff for the PennyLane backend continuation. Q0,
Q1, and Q2 are accepted as one conditional finite-basis quantum-backend
stack. The stack is a validated computational and diagnostic boundary; it is
not a physical parameter fit, physical state, spectrum claim, hardware
execution, TMD observable, or production phenomenology object.

## Frozen package chain

| Layer | Worktree / branch | Frozen implementation commit | Acceptance status | Acceptance root |
|---|---|---|---|---|
| Q0/PLHQCD0 | `deuteron_wigner_q0_plhqcd0`, `q0/plhqcd0` | `58596e628ea7cb999d58e0e2dd0f83b81f060d41` (later evidence; audited implementation `b094fb8cb1046aea0062468d73826ea25eab6116`) | `Q0_CLOSED_POSITIVE` | `2848cb692ce20cf21f654107acbcf9ed1a803cdd1c968f576c8271ae27df3b9c` |
| Q1/PLHQCDSTATE | `deuteron_wigner_q1_plhqcdstate`, `q1/plhqcdstate` | `e7b6aef3ea4fb8d8a3dd850754cd994873258e1f` | `Q1_PLHQCDSTATE_COMPLETE` | `604c2797f4b12a5409a63643635c093c1653cf3b02ccccb04f7f22e2f0645547` |
| Q2/PLHQCDOBS | `deuteron_wigner_q2_plhqcdobs`, `q2/plhqcdobs` | `69bc52d70c66db7d86b329898f9786ce43121895` | `Q2_PLHQCDOBS_COMPLETE` | `23ee186d0fb292b159a9acbfb9f52468f6d65b9fc13103014637034ae43394c1` |

The machine-readable authorities are:

- Q0: `deuteron_wigner_q0_plhqcd0/docs/next_level/q0_plhqcd0_closure_audit.json`
- Q1: `deuteron_wigner_q1_plhqcdstate/docs/next_level/q1_plhqcdstate_acceptance.json`
- Q2: `deuteron_wigner_q2_plhqcdobs/docs/next_level/q2_plhqcdobs_acceptance.json`

The Q0 later-evidence commit `58596e6` adds closure/audit evidence only. Q2
records it as descendant evidence and does not consume it as a replacement
for the Q0 executable backend. Q1 consumes the frozen Q0 implementation
authority at `b094fb8`; Q2 consumes the public Q0/Q1 APIs at the Q1 baseline.

## Common invariant boundary

All three layers preserve:

- `COMPACT_INDEX_DIRECT_ORDER_V1`;
- basis order `q followed by qg`;
- wire order `0,1,...,n-1` and big-endian bitstrings with wire 0 leftmost;
- physical compact support embedded at the front of the padded register;
- K9 `(1350 physical, 2048 padded, 11 qubits)`, K11 `(2706, 4096, 12)`,
  and K13 `(4758, 8192, 13)` dimensions;
- `lightning.qubit`, `complex128`, and deterministic `shots=None` execution;
- zero padded-sector amplitude for accepted state routes and zero physical-to-
  padding transfer for accepted measurement terms.

## Accepted responsibilities

### Q0/PLHQCD0

Q0 is the compact-index operator authority. It provides the positive padded
Hamiltonians, q/qg/padding projectors, derivative operators, sparse and
matrix-free actions, native encoded routes, and bounded PennyLane expectation
semantics across K9/K11/K13 and the four explicit diagnostic fixtures.

The closure audit reports 15 Q0 tests and 17 authority tests passed, zero
padding spectral contamination, maximum sparse/matrix-free residual
`1.1102230246251565e-16`, maximum derivative parity residual
`3.469446951953614e-18`, reproducible clean/restart/sharded builds, safe
loading, no network, and 2,304/2,304 focused mutation checks.

### Q1/PLHQCDSTATE

Q1 adds source-compatible state preparation and state diagnostics. The exact
sparse/Krylov eigenstate plus bounded `lightning.qubit` StatePrep oracle is a
validation route. The trainable route is a bounded K9 replay using the
Hamiltonian-edge ADAPT pool and ordinary gate decomposition; it is not a
physical VQE or an ansatz-selection claim. K11/K13 remain regression/resource
holdouts.

The accepted continuation sequence is exactly:

1. `FIXTURE-FREE`
2. `FIXTURE-INTERACTING-A`
3. `FIXTURE-INTERACTING-B-NULL-SHIFT`
4. `FIXTURE-MASS-SIGN`

The selected bounded layer is `EDGE-00-0-6:real`. The Q1 acceptance record
reports StatePrep oracle residual `3.1e-12`, trainable energy residual
`4.6e-12`, maximum eigenstate residual norm `2.1e-8`, observable residual
`5.3e-10`, padded leakage `1.1e-31`, and positive K11/K13 holdouts.

### Q2/PLHQCDOBS

Q2 adds the source-structured observable registry and measurement compiler.
It contains 471 records across all three resolutions, including 157 K9
records, Q0 total/derivative/projector records, Q1 owner sums and source
overlaps, and the authenticated ADAPT edge pool. Hermitian measurement terms
are diagonal bitstring terms or physical two-level edge terms. ADAPT
generators remain explicitly action-only.

Q2 acceptance covers exact and Q1 variational state routes, source-term
compilation, QNode/matrix-free parity, derivative/Hellmann–Feynman parity,
state residuals, source overlaps, variance-proportional shot-plan creation,
cross-resolution resource accounting, and 384/384 focused mutations. The
maximum measured route residual is `1.1102230246251565e-16`, maximum padding
leakage is zero for measurement terms, and no production `QubitUnitary` is
emitted. The largest bounded state residual is
`2.0116115644217026e-08`, within the declared Q2 `3e-8` residual gate.

Resource holdout census:

| Resolution | Source terms | Measurement groups | Dense Pauli enumeration | Variational optimization |
|---|---:|---:|---|---|
| K9 | 48,790 | 180 | false | false |
| K11 | 97,634 | 180 | false | false |
| K13 | 173,542 | 180 | false | false |

## Explicit nonclaims and freeze rules

The frozen stack does not select or create:

- physical masses, couplings, flavors, counterterms, renormalization points,
  standard-scheme conversions, or null representatives;
- a physical state, physical spectrum, pole, width, or production object;
- hardware, cloud, noise, finite-shot execution, or a default shot budget;
- a VQE/physical ansatz, TMD/Wilson observable, fit, or phenomenological band;
- dense Pauli enumeration, production dense unitaries, or an inferred omitted
  Fock-sector contribution.

No Q0, Q1, or Q2 implementation commit is to be amended in place. Any new
quantum-backend capability must begin in a new continuation worktree, consume
only the frozen public APIs and roots above, publish a new acceptance root,
and preserve this note as the prior boundary. No Q3 continuation is currently
authorized by this freeze.

## Re-entry checklist

Before any future quantum-backend work:

1. Read this file and the three acceptance JSON files.
2. Confirm the three worktree branches and commits match the table above.
3. Import Q0/Q1/Q2 through their public package surfaces only.
4. Re-run the relevant focused tests before changing scope.
5. Treat any request for physical parameters, physical states, hardware,
   shots, fits, TMDs, or production outputs as a new authorization boundary.
