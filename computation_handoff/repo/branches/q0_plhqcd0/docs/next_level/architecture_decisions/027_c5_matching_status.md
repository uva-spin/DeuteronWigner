# ADR 027: Validation-only matching and phase status

**Decision:** Every result retains unresolved UV, rapidity/soft,
link-shortening, evolution, and process fields. Uncalculated terms are
`UNRESOLVED_NOT_ZERO`.

**Reason:** Zero would be a physical claim; omission would allow premature
downstream use.

**Status:** Fail-closed scientific-status contract.
