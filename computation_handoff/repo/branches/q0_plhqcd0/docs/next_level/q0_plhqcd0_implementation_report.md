# Q0/PLHQCD0 implementation report

## Scope

Q0 implements the actual source-ordered compact operator backend for K9, K11,
and K13. It consumes C131, C142, C144, C149, and C150 only through their
exported immutable public APIs. The numerical boundary is an explicit C144
diagnostic fixture; no physical parameter, C150 kinetic scheme, `Z_q`, mass,
counterterm, null representative, VQE state, ansatz, or hardware result is
selected.

The implementation is in
`src/deuteron_wigner/bridge/plhqcd0/core.py` and provides:

- cross-checked public-authority loading;
- C142 `q followed by qg` compact dimensions and C144 operator support;
- compact-index to big-endian computational-bitstring encoding;
- exact physical-subspace, q-sector, and qg-sector sparse projectors;
- certified zero-padded sparse Hamiltonians with no dense materialization;
- independent sparse, C144 matrix-free, encoded, and PennyLane QNode routes;
- sector weights and padded-state leakage diagnostics;
- exact public C144 derivative construction and route parity;
- explicit resource accounting and a hard generic-Pauli-decomposition boundary.

The primary QNode uses `lightning.qubit`, `shots=None`, and `complex128`.
The production compiler never constructs a generic full Pauli decomposition.

## Dimensions

| Resolution | q | qg | compact | padded | qubits |
|---|---:|---:|---:|---:|---:|
| K9 | 6 | 1344 | 1350 | 2048 | 11 |
| K11 | 6 | 2700 | 2706 | 4096 | 12 |
| K13 | 6 | 4752 | 4758 | 8192 | 13 |

## Validation

Environment: `.venv311`, Python 3.11.15, PennyLane 0.38.0,
PennyLane-Lightning 0.38.0, Autoray 0.6.12, NumPy 1.26.4.

```text
15 passed: tests/test_q0_plhqcd0.py
17 passed: tests/test_c131_hqcd4.py tests/test_c142_hqcdfield.py
             tests/test_c144_hqcdopapi.py tests/test_c149_hqcdmproj.py
             tests/test_c150_hqcdzqmass.py
```

Sparse versus independent matrix-free action parity is checked at
`rtol=1e-13`, `atol=2e-12`; the largest observed K13 residual is approximately
`1.3e-12`, attributable to floating-point accumulation order. Derivative
route parity is exact for the public derivative entries.

## Continuation

The sole continuation is Q1/PLHQCDSTATE, limited to source-compatible physical
state preparation and state-level sector/projector diagnostics. It must not
start VQE, choose an ansatz, select a physical parameter, or consume C151.
