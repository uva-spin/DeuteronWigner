# ADR-014: Analytic pilot isolation

Status: accepted for C3

C3 objects are `VALIDATION_ONLY` and `NOT_AUTHORIZED_FOR_PRODUCTION`. Their
provenance graph is disjoint from the accepted C2 graph; their reductions use
a separate registry. Production promotion, registry insertion, Gaussian-width
promotion, and production-builder consumption fail closed.
