# C171/HQCDB0ADJOINT1 implementation report

Status: `C171_HQCDB0ADJOINT1_GHOST_GAUGE_RESIDUAL_INCOMPLETE`

Plan: `B0ADJOINT1-J`

Baseline: `db7b994ce0e00fd992360c1c477ac1bda1ea6d1c`

The committed C170-to-C171 continuation contract was not present at the
specified path.  This run is therefore prompt-only and fail-closed; the
historical C170 missing-contract limitation is preserved in
`c171_contract_provenance_report.json`.

The exact eight C170 missing-sector records were imported through the C170
public API.  Four B=0 records were consumed by this package and four B=1
records remain preserved and unmodified.  No C166 graph node or edge was
added, no C158 value was consumed, and no C134 or inherited C157 test was
repaired.

Implemented authority:

- integer-total B=0 resolution records for K9/K11/K13, with positive
  half-integer q/qbar APBC modes and positive integer gluon PBC modes;
- source-derived `3 tensor anti-3 -> 8` adjoint multiplicity one;
- source-derived `8 tensor 8 -> 8` adjoint multiplicity two, retaining d and f
  channels;
- all-eight-generator intertwiner and projector checks;
- generic, non-averaged active-flavor semantics;
- finite intrinsic-HO/CM-ground factorized catalogs with reversible rank/unrank;
- read-only C151 one-gluon source crosswalk;
- C43 pair and three-gluon source ownership records without inventing direct
  vacuum sources;
- count-once direct/instantaneous/tadpole/normal-ordering ownership records;
- symbolic sparse/matrix-free free M2 actions and analytic nonphysical
  resolvent interfaces.

The remaining blocker is exact C43 global residual-gauge closure: the source
authority states nonzero-mode ghost decoupling, but the P0/Q0, finite-boundary,
and residual-link scope is not a complete no-ghost proof.  Interaction
projection, direct/instantaneous coefficients, and counterterm coefficients
remain explicitly nonzero and unresolved.

Validation:

- focused C131/C142/C151/C161-C171 regressions: 68 passed;
- C171 focused tests: 5 passed, including 384 live mutations;
- two clean local wheel builds succeeded;
- clean reload, restart, query-order, and safe-load checks passed;
- inherited untracked C157 test: two stale-expectation failures preserved as
  diagnostic; no file changes;
- unrelated C134 expectation remains quarantined; no repair performed.

Next continuation: `C172/HQCDB0GHOST1`, focused on the C43 ghost/no-ghost and
P0/Q0 residual-gauge authority boundary.
