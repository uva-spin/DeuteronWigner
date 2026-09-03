# ADR 096: analytic-only C23 scope

C23 executes only synthetic analytic process oracles. Source and physical APIs
fail closed, and every observable carries `VALIDATION_ONLY`.
