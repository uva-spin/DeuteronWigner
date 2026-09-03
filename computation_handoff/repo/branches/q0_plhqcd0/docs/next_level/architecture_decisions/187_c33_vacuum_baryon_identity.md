# ADR 187: Keep the B=0 vacuum identity disjoint from the B=1 proton basis

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The C33 vacuum Hilbert space is constructed independently from the historical
C7/C11 baryonic basis. At one-loop scope its declared span contains a unique
vacuum and finite one-soft-gluon modes. It does not inherit the proton's fixed
total-`K`, charge, `Jz`, center-of-mass, or probability-normalization gates.
Every vacuum and soft-gluon state carries `B=0` explicitly.

## Evidence

- `PhysicalFockBasis` requires baryon number one for every historical state.
- The H6/H7 towers contain only sectors rooted in `QQQ`.
- C32 identified the absence of a vacuum/eikonal action as the structural
  obstruction to a microscopic soft factor.

## Authority and status

- **Exact:** `B=0` vacuum identity, orthogonality to all C11 proton states,
  unique tree vacuum, and `S^(0)=1`.
- **Finite-regulator model:** mode cells, normalizations, rapidity bins,
  transverse basis, and boundary conditions.
- **Temporary:** one-gluon completeness beyond the frozen finite resolution.
- **Open:** interacting one-loop vacuum matrix elements; they are not supplied
  by the tree construction and remain `NONZERO_UNKNOWN`.

## Alternatives considered

- Add a vacuum sector to `PhysicalFockBasis`: rejected because its exact
  `B=1` and total-`K` gates are historical C11 identity.
- Treat an empty proton Fock sector as the vacuum: rejected because an empty
  baryonic sector is not the soft vacuum state.
- Infer the vacuum normalization from C11: rejected because the roots share no
  probability normalization.

## Consequences

- The finite soft resolution has its own content hash and continuum trajectory.
- Tree normalization can close independently while every one-loop contribution
  remains fail-closed.
- The package outcome remains `C33_SOFT_TREE_LEVEL_ONLY`; the next calculation
  is C34/S0A.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_vacuum_hilbert_manifest.json`
- `docs/next_level/c33_soft_basis_manifest.json`
- `docs/next_level/c33_soft_basis_trajectory_plan.json`
- `tests/test_c33_s0.py` vacuum uniqueness, `B=0`, mode normalization, and
  historical-basis rejection tests

## Revision triggers

Revise when a source-audited interacting B=0 basis with explicit completeness
and normalization is implemented, or when the chosen soft-basis trajectory is
replaced. Never revise by mutating C11 or relabeling its state normalization.
