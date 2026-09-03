# C2 native reduction and provenance API

`ReductionId` decorates a `MapClass.RED` operation with source operator and
parent identities, source/target coordinates and ranks, target channel,
parton polarization, collinear/moment semantics, adapters, availability,
evidence status, and version. `ReductionRegistry` rejects duplicates and
returns deterministic ordering. `accepted_reduction_registry()` constructs
216 accepted forward routes: 72 quark, 72 antiquark, and 72 gluon.

`ProvenanceNode`, `ProvenanceEdge`, and `ProvenanceGraph` provide typed
semantic ancestry. Directed derivation cycles and unknown endpoints fail
closed. `CompositionPlan` validates duplicates, alternatives, replacements,
exclusions, and central eligibility before numerical evaluation; `dry_run`
does not load arrays.

`BoundaryTraceIndex` exposes `trace_named_output`, `trace_artifact_row`,
`explain_composition`, `explain_exclusion`, `list_reductions`, and
`list_consumers`. All results are stable-ID metadata and deterministic.
