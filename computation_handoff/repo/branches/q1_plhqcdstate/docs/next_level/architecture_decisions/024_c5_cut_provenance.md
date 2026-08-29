# ADR 024: Cut provenance and double counting

**Decision:** `CutLedger` keys physical identity by on-shell support and
requires explicit distinct, equivalent-count-once, or subtraction relations.

**Reason:** Equal floating denominators need not be the same cut, while one
physical support can appear in eikonal and LF-resolvent representations.

**Status:** Executable finite C5 relation; not a general provenance 2-complex.
