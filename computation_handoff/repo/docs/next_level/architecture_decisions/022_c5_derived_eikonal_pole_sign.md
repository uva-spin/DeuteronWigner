# ADR 022: Derive the eikonal pole sign

**Decision:** The pole prescription is derived from orientation, Fourier,
coupling, and momentum-flow conventions stored by `BareWilsonSegment`.
Callers cannot pass a sign.

**Reason:** Path reversal must determine the absorptive sign independently of
the hadron model. A manual sign could create an arbitrary T-odd phase.

**Status:** Exact convention constraint for the declared C5 convention tuple.
