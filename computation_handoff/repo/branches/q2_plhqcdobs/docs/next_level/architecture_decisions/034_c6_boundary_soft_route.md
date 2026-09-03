# ADR 034: Analytic boundary-only soft route

**Decision:** Implement only `BOUNDARY_ONLY_RESCATTERING` and an explicit
first-order half-soft overlap subtraction. The joint microscopic soft route
is typed but unimplemented and mutually exclusive.

**Reason:** Combining both without an overlap map would double count the same
soft region.

**Status:** MATCH-class analytic benchmark, not a continuum TMD scheme.
