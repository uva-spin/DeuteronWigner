# ADR 023: Explicit cuts, not numerical broadening

**Decision:** Physical absorption comes only from `IntermediateStateCut`
support. Finite epsilon is confined to `EpsilonConvergence` and cannot be
marked physical.

**Reason:** An off-shell discrete spectrum has zero discontinuity. A
Lorentzian width cannot manufacture continuum physics.

**Status:** Exact spectral constraint; continuum weights are validation-only.
