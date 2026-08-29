# ADR 221: Make Branch G and the C36/O4 continuation exact

Status: draft; implemented as the C35/S0C completion branch.

## Question

What is the scientifically correct completion status when no positive gauge
plan is regulator identical and complete?

## Decision

Complete C35 on Branch G with the exact codes

```text
C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
```

and the exact continuation

```text
C36/O4 — replacement regulator architecture for the microscopic TMD soft root
```

Keep every missing physical object empty-not-zero and all eighteen graph
slots `NONZERO_UNKNOWN`.  Do not reinterpret this branch as a vanishing soft
factor, a failed numerical convergence test, or permission to populate
placeholders.  Do not use the historical S0D/S0E labels for the next job: the
first unresolved dependency is the regulator architecture itself.

## Physics basis and alternatives

Volume XXI and the C35 contract explicitly permit a rigorous negative result
and forbid a continuum coefficient from masquerading as a finite-basis
calculation.  Continuing directly to graphs, counterterms, proton export, or
bridge evaluation would bypass the failed gauge and mode gates.

Classification: source-supported architecture and workflow decision.

## Consequences

- C35 is complete as a regulator audit/no-go, not as a one-loop soft
  calculation.
- C36/O4 must create a new versioned `B=0` root before any coefficient attempt.
- ART25/data/bridge/inference/production reachability remains hard false; the
  216-route registry and authoritative artifacts remain unchanged.

## Affected evidence

- `docs/next_level/c35_no_go_decision_tree.json`
- `docs/next_level/c35_c32_continuation_gate.json`
- `docs/next_level/c35_requirement_coverage.json`
- `docs/next_level/c35_implementation_report.md`

## Revision trigger

This record may be superseded only by a later versioned package with evidence
for a gauge-complete, regulator-identical realization.  Historical C35
artifacts remain immutable even if the later calculation succeeds.
