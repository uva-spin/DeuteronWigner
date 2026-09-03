# ADR 038: Exact longitudinal-mode representation

**Decision:** Represent longitudinal modes and total \(K\) with exact rational
arithmetic. Fermions use positive half-integers, bosons positive integers,
and gluon zero modes are excluded with an explicit closure ledger.

**Reason:** Floating labels can admit forbidden states or obscure exact
momentum conservation.

**Status:** Implemented for the finite C7 sectors; zero-mode physics is
deferred, not silently approximated.
