# ADR-007: Typed provenance nodes and relations

Status: accepted for C2

Provenance node and relation kinds are enums. Stable identity never depends on
memory address or traversal order. Directed derivation relations must form a
DAG; exclusion, replacement, alternative, ensemble, benchmark, normalization,
validation, and consumer relations remain semantically distinct. Graph
validation never requires loading numerical arrays.
