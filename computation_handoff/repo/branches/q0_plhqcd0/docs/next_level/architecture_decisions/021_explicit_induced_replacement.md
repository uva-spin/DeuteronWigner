# ADR 021: explicit-sector versus induced-operator replacement

Status: accepted for finite validation models.

Explicit higher sectors and retained-space induced operators are alternative
representations of the same eliminated physics. The C4 provenance graph
records `ALTERNATIVE_TO` and `EXCLUDES`, while separate remainder nodes make
the replacement identity explicit.

The finite Feshbach benchmark verifies the operator equivalence including the
norm kernel and demonstrates that `POP` alone fails. Selecting both an
explicit sector and its induced operator is rejected before evaluation.
Neither representation is connected to accepted production.
