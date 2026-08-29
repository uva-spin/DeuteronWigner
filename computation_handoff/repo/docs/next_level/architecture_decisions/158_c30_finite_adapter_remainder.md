# ADR 158: Fail closed without a finite adapter expression

**Decision.** The adapter is non-executable and its remainder is
`NONZERO_UNKNOWN` until a source-qualified expression, inverse, round-trip,
RG, rapidity, threshold, and domain record are available.

**Reason.** An identity map would silently equate inequivalent regulated and
renormalized TMD objects.
