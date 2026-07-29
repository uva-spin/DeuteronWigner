# ADR-010: Forward-only is distinct from unavailable transfer dependence

Status: accepted for C2

Accepted TMD projections are marked `AVAILABLE_FORWARD`. A typed nonzero
`DeltaT` interface may exist later, but its reduction is
`UNAVAILABLE_NONZERO_TRANSFER` until a genuine GTMD parent supplies it.
Forward data are never promoted into fabricated transfer dependence.
