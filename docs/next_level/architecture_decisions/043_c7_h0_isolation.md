# ADR 043: H0 isolation from production and C5/C6 dynamics

**Decision:** Place C7 objects in a disjoint validation-only provenance graph
and reject reachability from production, nuclear, evolution, process, or
inference roots.

**Reason:** A finite H0 architecture benchmark cannot replace the accepted
phenomenological parents or the C5/C6 Wilson-line dynamics.

**Status:** Implemented. Production and authoritative outputs remain
immutable regression oracles.
