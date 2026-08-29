# ADR 188: Select direct eikonal Fock space and keep the auxiliary route separate

Status: accepted for the fail-closed C33/S0 completion.

## Decision

`S0-FB-EIKONAL-FOCK` is the primary microscopic representation. It carries the
vacuum, one-soft-gluon modes, and four non-dynamical eikonal color sources.
`S0-AUXILIARY-EIKONAL` is a separate methodological oracle for path transport,
endpoint composition, and orientation reversal. Direct and auxiliary results
are alternatives, never additive soft factors.

At C33 tree level both routes may reduce to the identity. No one-loop
equivalence is claimed without a Minkowski/light-front, modified-delta, UV,
endpoint, and residual-energy conversion proof.

## Evidence

- C5/C14 provide direct Wilson expansion and representation-algebra oracles.
- The audited auxiliary-field sources provide a Wilson-line representation and
  renormalization methodology, but not automatic identity with the C33 finite
  regulator.
- Euclidean/lattice auxiliary constructions do not by themselves establish the
  required light-front modified-delta operator.

## Authority and status

- **Exact:** separate route identities, non-additivity, tree identity, and path
  reversal algebra where executed.
- **Source-qualified:** auxiliary propagator representation and need for line
  mass/residual-energy and endpoint counterterms.
- **Finite-regulator model:** direct one-gluon mode realization.
- **Temporary/open:** one-loop auxiliary/direct conversion; status is
  `CALCULATION_REQUIRED` under `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Make the auxiliary route primary: rejected until its C33 regulator conversion
  is proved.
- Use `S0-CONTINUUM-ORACLE-ONLY`: retained solely as a target oracle and cannot
  issue microscopic finite-basis status.
- Add direct and auxiliary values: rejected as double counting.

## Consequences

- The plan is selected before any numerical comparison.
- Auxiliary residual mass, endpoints, junctions, and transverse closure remain
  visible in their own ledger.
- A tree agreement cannot open UV, rapidity, trajectory, or continuation gates.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_sector_plan_manifest.json`
- `docs/next_level/c33_soft_sector_plan_selection.json`
- `docs/next_level/c33_auxiliary_field_soft_oracle.json`
- `docs/next_level/c33_auxiliary_direct_equivalence_report.json`
- `tests/test_c33_s0.py` route exclusivity, non-additivity, and tree-equivalence
  tests

## Revision triggers

Revise if C34/S0A or C34/S2 supplies a source-locked one-loop auxiliary/direct
conversion with matched regulator, endpoint, and UV identities. Methodological
similarity or numerical agreement at one point is insufficient.
