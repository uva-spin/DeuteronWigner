# C172/HQCDB0GHOST1 implementation report

Status: `C172_C171_Q0_GHOST_DECOUPLING_READY_P0_RESIDUAL_GAUGE_INCOMPLETE`

Plan: `B0GHOST1-B`

Starting commit: `754b69c8920b8ce36cc0efeeaf1988f005ce255f`

The expected committed continuation contract was absent.  C172 therefore
uses only the supplied prompt (`5f4a0ce9bc9b8eb3a979f846c9d4c02a5a5426ea2791e34579533c7b7b78c471`),
and preserves the earlier C170 and C171 prompt-only provenance records.

Implemented:

- source-mapped C43 Hermitian-generator and covariant-derivative signs;
- exact finite periodic P0/Q0 projector identities on modes -13 through 13;
- Q0 Faddeev--Popov operator through direct variation and finite-mode routes;
- field-independent finite Q0 determinant ratio, with absolute normalization
  kept separate;
- residual-group taxonomy, global-color/open-adjoint separation, and explicit
  unresolved local P0 residual transformations;
- PV, finite-boundary, residual-link, Gauss-law, source/free/projector, and
  structural interaction-covariance ledgers;
- Q0/P0/constraint/boundary/target-ghost count-once separation;
- exact typed capsules for the unresolved P0 sub-gauge, residual link, and
  local Gauss-law completion.

The result releases the frozen C171 B=0 substrate only for
`Q0_NONZERO_MODE_GHOST_DECOUPLING_ONLY`.  It does not claim full P0 closure,
residual gauge-volume cancellation, trivial residual link, BRST, or full
Slavnov--Taylor closure.

No C171 bases were rebuilt, no B=1 sector was modified, no graph node or edge
was added, no C158 value or target ghost was imported, and no physical or
loop-level quantity was evaluated.

The inherited C157 stale-expectation test and unrelated C134 expectation
remain preserved diagnostics.  The next continuation is
`C173/HQCDB0RESGAUGE1`, focused on the source-qualified P0 residual sub-gauge
and gauge-volume boundary.
