# C14/H7 validation API

C14 is an isolated finite-basis benchmark. It does not export a physical
nucleon, GTMD, TMD, nuclear state, matching coefficient, evolution object,
process prediction, or inference likelihood.

The public validation surface is `deuteron_wigner.microscopic.h7`.

- `plans()` returns mutually exclusive H7-PLAN-A/B descendants of C13.
- `basis_tower()` returns ten typed sector branches at three resolutions.
- `H7ColorBasis.construct(sector)` returns the common-total-generator
  nullspace certificate and permutation decomposition for each new sector.
- `GluonPermutationState` rejects color/spin-orbital products that do not
  contain the total symmetric bosonic representation.
- `build_hamiltonian(plan, basis)` creates a Hermitian ten-block benchmark
  with typed mechanisms and generated adjoints.
- `renormalization_trajectory()` exposes mass/charge conditions, separate
  bare/counterterm/induced/discrepancy flow, a null direction, and unfitted
  antiquark/gluon order-two holdouts.
- `support_table()` and `require_support()` authorize Wilson orders one and
  two for quarks, antiquarks, and gluons; order three fails closed.
- `strict_dyson()` and `strict_magnus()` construct order-two polynomials only.
  `representation_generators()` supports fundamental, anti-fundamental,
  adjoint, and ordered two-link validation classes.
- `matrix_parents()` retains complete order-resolved quark, antiquark, and
  gluon matrix identities before link-even/link-odd projection.
- `compile_plan()` rejects mixed plans, Wilson order three, and all downstream
  physical requests.

The diagnostics module exports deterministic reports for color/permutation,
Hamiltonian/Krylov/TTN closure, strict Dyson/Magnus equivalence, spectral
cuts, square-root-soft subtraction, finite gauge closure, convergence,
matrix parents, and readiness gates.

Rebuild and validate with:

```bash
PYTHONPATH=src python scripts/build_c14_manifests.py 945
PYTHONPATH=src python scripts/validate_c14_architecture.py
PYTHONPATH=src python -m pytest -q
```
