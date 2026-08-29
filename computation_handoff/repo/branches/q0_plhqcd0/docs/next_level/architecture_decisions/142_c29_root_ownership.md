# ADR 142: external and microscopic root ownership

Decision: ART25 and the microscopic operator construction remain immutable,
disjoint provenance roots. No source member is a microscopic state and no
readiness status crosses the bridge. This is exact architectural provenance.
Affected: `bridge/b0/core.py`, root and provenance manifests, root tests.
Revisit only with a documented physical map; never by member-index convention.
