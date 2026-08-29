# ADR 191: Do not infer finite-basis soft UV renormalization from tree identity

Status: accepted for the fail-closed C33/S0 completion.

## Decision

Soft UV renormalization is decomposed into Wilson-line self energy,
cusp/endpoint, transverse-junction, auxiliary residual mass, vacuum energy, and
operator factors. Linear or power divergences remain distinct from logarithmic
UV counterterms. `Z_S^UV=1` is exact only at tree level.

C33 issues no one-loop UV counterterm, anomalous dimension, or validation
status because no regulated one-loop bare soft factor has been calculated.

## Evidence

- C32 lists Wilson self energy, cusp/endpoints, UV counterterms, and basis
  counterterms as calculation-required contributions.
- C13/C14 explicitly retain `UV_FINITE_MATCHING_REQUIRED`.
- Auxiliary-field sources require separate residual-line-mass and endpoint
  renormalization.
- The historical finite-basis UV scales are diagnostic, not exact cutoffs.

## Authority and status

- **Exact:** tree factor `Z_S^UV=1` and separation of counterterm ownership.
- **Source-qualified:** target continuum UV structure and anomalous-dimension
  oracle.
- **Finite-regulator model:** the C33 cutoff and basis-boundary definitions.
- **Temporary/open:** all one-loop counterterms and anomalous dimensions;
  `C33_SOFT_UV_RENORMALIZATION_VALIDATED` is not issued.

## Alternatives considered

- Import the continuum MS-bar counterterm as the finite-basis calculation:
  rejected.
- Hide power divergences inside a logarithmic factor: rejected.
- Reuse baryonic Hamiltonian counterterms for the vacuum operator: rejected
  without a proved regulator conversion.

## Consequences

- Bare, UV-renormalized, and target-scheme soft objects retain distinct IDs.
- A source oracle may be recorded but cannot open the microscopic gate.
- The package remains `C33_SOFT_TREE_LEVEL_ONLY`.
- C34/S0A must calculate the diagram ledger before extracting `Z_S^UV`.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_counterterm_ledger.json`
- `docs/next_level/c33_soft_uv_renormalization.json`
- `docs/next_level/c33_soft_uv_anomalous_dimension_report.json`
- `tests/test_c33_s0.py` tree-factor, counterterm-ownership, and premature-UV-
  claim rejection tests

## Revision triggers

Revise only after a complete regulated one-loop diagram calculation separates
all logarithmic and power structures at three or more resolutions, or after an
exact source-qualified regulator conversion is proved.
