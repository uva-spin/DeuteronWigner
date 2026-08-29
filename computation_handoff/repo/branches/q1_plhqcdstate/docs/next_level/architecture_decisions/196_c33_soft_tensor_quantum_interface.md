# ADR 196: Tensor and quantum soft interfaces are deterministic representations

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The soft tensor-network plan represents one B=0 vacuum root, finite one-gluon
modes, adjoint color, polarization, rapidity and transverse cells, four
eikonal color legs, and a singlet trace. Bond dimension and register truncation
are deterministic numerical axes, not statistical members or probability
weights.

The quantum interface is a future compilation contract for vacuum/one-gluon
registers, eikonal color registers, controlled emission/absorption, and singlet
projection. C33 executes no circuit, optimization, fitting, or inference.

## Evidence

- Historical H5-H7 tensor-network alternatives are explicitly numerical
  truncations and do not define statistical ensembles.
- The C33 soft operator requires color-source legs that are not proton
  constituents.
- Tree identity can be represented without supplying the missing one-loop
  Hamiltonian or counterterms.

## Authority and status

- **Exact:** tensor index identities, root separation, tree trace, and
  deterministic serialization.
- **Finite-regulator model:** bond dimensions, ordering, truncation, and future
  register encoding.
- **Temporary:** circuit decomposition and resource estimates.
- **Open:** one-loop observable tensors and controlled dynamics under
  `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Interpret bond alternatives as replicas or posterior members: rejected.
- Reuse the proton tensor network and append vacuum legs: rejected as root
  mixing.
- Claim quantum advantage or execute a fit: outside scope.

## Consequences

- Tensor and quantum manifests remain isolated from inference and production.
- Full-bond equality, when tested, is a numerical reconstruction oracle only.
- No continuation gate depends on an unexecuted quantum plan.
- The package remains `C33_SOFT_TREE_LEVEL_ONLY`; C34/S0A is next.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_tensor_network_manifest.json`
- `docs/next_level/c33_soft_quantum_interface_contract.json`
- `tests/test_c33_s0.py` index completeness, deterministic bond-axis, no-
  probability, and production-isolation tests

## Revision triggers

Revise when an explicit one-loop soft operator is compiled and validated in a
tensor or quantum representation. Resource studies alone cannot promote the
scientific status.
