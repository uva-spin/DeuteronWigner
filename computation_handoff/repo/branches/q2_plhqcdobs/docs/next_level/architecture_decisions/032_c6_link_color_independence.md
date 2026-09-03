# ADR 032: Link topology and f/d color are independent

**Decision:** Link words and normalized `f`/`d` projections are separate
fields and separate RED operations. No link word implies a color channel and
no default channel sum exists.

**Reason:** Process-dependent color weights are later PROC data, not
properties of the universal validation operator.

**Status:** Exact architecture constraint; no physical process weights.
