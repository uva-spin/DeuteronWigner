# ADR-005: Convergence is an observable-level statement

Status: proposed for Stage A

Decision: `TruncationTower` records nested sector/OAM/Fock/twist/model levels,
but convergence is certified only for a named observable, kinematic domain,
norm, tolerance and adjacent sequence of levels. `ObservableLikelihood`
binds the process, data covariance, nuisance parameters and operator identity.

Rationale: adding formal sectors does not prove that an observable is stable.
Different observables weight OAM, tensor, nuclear, link and color components
differently.

Consequence: a single truncation level cannot claim convergence. Existing
model sensitivities remain named uncertainties until a documented observable
sequence satisfies its convergence criterion.
