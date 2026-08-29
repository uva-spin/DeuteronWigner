# C9/H2 API

Public objects are under `deuteron_wigner.microscopic.h2`.

| API | Responsibility |
|---|---|
| `H2AssumptionBundle`, `compile_h2_plan`, `H2Plan` | Content-addressed coupled-sector plan and exclusivity certificate |
| `H2BasisState`, `CoupledH2Basis`, `build_coupled_basis_tower()` | Growing \(qqq\oplus qqqg\) tower with both color multiplicities |
| `H2InstantaneousTerm` | Typed inverse-derivative, endpoint, zero-mode and ownership policy |
| `CoupledH2Hamiltonian`, `build_hamiltonian()` | Hermitian coupled block and matrix-free action |
| `H2RenormalizationTrajectory`, `fit_h2_trajectory()` | Sector-dependent refit and identifiability record |
| `H2VectorCurrent` | Hamiltonian-owned multi-sector current |
| `ward_benchmark()` | Finite commuting-generator Ward identity and omission tests |
| `coupled_ttn_benchmark()` | Fock-root TTN Rayleigh--Ritz convergence |
| `gluon_oam_ledger()` | Probability, momentum, helicity, OAM and \(J^z\) closure |
| `feshbach_comparison()` | Explicit-sector elimination and declared remainder |
| `MicroscopicRescatteringInput`, `MicroscopicWilsonInputAdapter` | Validation-only C5/C6 reconnection boundary |

No H2 object is a production parton distribution or physical nucleon export.
