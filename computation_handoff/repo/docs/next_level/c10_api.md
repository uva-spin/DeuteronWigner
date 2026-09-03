# C10/H3 API

The API under `deuteron_wigner.microscopic.h3` provides:

- `H3AssumptionBundle`, `H3Plan`, and `compile_h3_plan`;
- `FivePartonState`, `H3Basis`, and `build_h3_basis_tower`;
- `PairCreationVertex`, its adjoint, and `ChiralPairVertex`;
- `H3Hamiltonian`, `build_hamiltonian`, and `H3Trajectory`;
- `AxialCurrentOperator`, `PseudoscalarOperator`, and
  `PionPoleOrInducedOperator`;
- `AntiquarkOverlapEvaluator` for direct positive-x active antiquarks;
- executable PCAC, ledger, TTN, common-parent, Feshbach, and Wilson-handoff
  diagnostics.

Every export is `C10_H3_VALIDATION_ONLY`; none is a matched physical
distribution or production state.
