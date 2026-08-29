# ADR 186: Compose the regulated TMD from distinct collinear and soft roots

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The regulated microscopic TMD has two content-addressed Hilbert/provenance
roots over a typed joint-regulator contract:

- `C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION`, with baryon number `B=1`;
- `C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT`, with baryon number `B=0`.

They share no state vector, probability normalization, or fitted parameter.
Their only connection is a compatibility record for gauge group,
representation, Wilson geometry, transverse measurement, Fourier convention,
rapidity and UV conventions, scales, boundary conditions, and overlap map.

## Evidence

- The C7/C11 physical basis enforces baryon number one and has no vacuum
  state.
- C32 proved the completed operator's exact tree reduction to C11 but issued
  `C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED` at one loop.
- The required soft operator is a vacuum expectation value of four eikonal
  lines, not a component of the proton wave function.

## Authority and status

- **Exact:** root identities, baryon numbers, absence of shared normalization,
  tree factors `S^(0)=1` and `ZERO_BIN^(0)=0`.
- **Source-qualified:** multiplicative vacuum-soft allocation and count-once
  overlap structure.
- **Finite-regulator model:** the chosen C33 soft basis and resolution tuple.
- **Temporary/open:** the one-loop fiber-product compatibility map. It remains
  unresolved under `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Insert the vacuum factor into the C11 proton state: rejected because it
  aliases `B=0` and `B=1` state identities.
- Add vacuum and baryon probabilities: rejected because the TMD composition is
  an operator product/subtraction, not a probabilistic mixture.
- Use a continuum soft oracle as the C33 root: rejected because it is not a
  finite-basis microscopic calculation.

## Consequences

- C11 and the exact C32 tree oracle remain byte-immutable.
- C33 cannot export a proton TMD or rerun the bridge.
- Every later completion must traverse the compatibility and zero-bin edges;
  no direct state edge may connect the roots.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_two_root_tmd_identity.json`
- `docs/next_level/c33_soft_collinear_provenance_graph.json`
- `tests/test_c33_s0.py` two-root, baryon-number, and no-state-alias tests
- `scripts/build_c33_manifests.py`, `scripts/validate_c33.py`

## Revision triggers

Revise only if a later operator theorem changes the project soft allocation or
proves an explicit regulator-level composition with different root metadata.
A phenomenological fit, continuum formula, or bridge residual is not a valid
trigger. The current continuation remains C34/S0A.
