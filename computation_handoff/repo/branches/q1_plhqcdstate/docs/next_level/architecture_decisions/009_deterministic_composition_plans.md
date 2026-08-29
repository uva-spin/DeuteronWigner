# ADR-009: Deterministic composition plans

Status: accepted for C2

A `CompositionPlan` stores an ordered tuple of stable node IDs. Validation
precedes evaluation. Dry-run output includes the exact order and deterministic
ancestry. The accepted default plan selects the already resolved constituent
parent, preserving the legacy internal ordering and avoiding a second
numerical composition.
