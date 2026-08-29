# C8/H1 API

The isolated public API is `deuteron_wigner.microscopic.h1`.

| Object/function | Role |
|---|---|
| `H1AssumptionBundle` | Frozen valence-only scientific choices and stable identity |
| `compile_plan`, `H1PredictionPlan` | Fail-closed assumption compiler and directed execution plan |
| `H1BasisState`, `H1ValenceBasis`, `H1BasisTower` | Symmetry-labelled nontrivial \(qqq\) tower |
| `build_basis_tower()` | Reference 4/7/10-dimensional proton or neutron tower |
| `ValenceHamiltonianTerm` | Term ownership, symmetry, kernel, status, provenance and ablation |
| `ValenceHamiltonian`, `build_hamiltonian()` | Hermitian interacting mass-squared block |
| `H1TruncationDiscrepancy` | Typed record of omitted, nonzero-unknown physics |
| `RenormalizationCondition` | Frozen calibration or holdout condition |
| `RenormalizationTrajectory`, `fit_trajectory()` | Resolution-indexed refit, Jacobian/Hessian and parameter flow |
| `exact_solve()`, `krylov_solve()` | Dense and matrix-free eigenproblem oracles |
| `ValenceVectorCurrent` | Hamiltonian-compatible flavor vector current |
| `ValenceStateTracker` | Overlap, fingerprint, principal-angle and phase tracking |
| `SymmetryTensorIndex`, `BlockSparseTensor` | Physical TTN indices and allowed-block-only storage |
| `ValenceCouplingTree`, `ValenceTTNState` | Three-quark symmetry coupling tree and state |
| `ValenceTensorOperator` | Factorized H1 operator application |
| `TTNOptimizationResult`, `BondDimensionManifest` | Rayleigh--Ritz results and convergence records |
| `ValenceMicroscopicStateBundle` | Versioned `VALENCE_ONLY` state/current export |

Example:

```python
from deuteron_wigner.microscopic.h1 import (
    H1AssumptionBundle, build_basis_tower, compile_plan,
    exact_solve, fit_trajectory,
)

plan = compile_plan(H1AssumptionBundle(
    "INDUCED_REFIT", "EFFECTIVE_COLOR_SPIN"
))
tower = build_basis_tower(target="PROTON")
trajectory = fit_trajectory(plan, tower)
solution = exact_solve(trajectory.hamiltonians[-1])
```

The resulting state is a finite H1 validation state, not a production
nucleon wave function or a source of physical TMDs.
