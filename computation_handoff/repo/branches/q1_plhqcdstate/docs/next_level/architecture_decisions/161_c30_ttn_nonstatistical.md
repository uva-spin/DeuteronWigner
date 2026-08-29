# ADR 161: Treat TTN bond dimension as truncation, not statistics

**Decision.** Bond dimension labels deterministic numerical approximations and
must not be paired with ART25 member indices or interpreted as replicas.

**Reason.** The two axes have different probability and provenance semantics.
