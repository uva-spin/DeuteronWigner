# ADR-006: One native typed reduction registry

Status: accepted for C2

The C1 `MapClass.RED` and decorated identities are extended by `ReductionId`;
no second map hierarchy is introduced. Stable IDs include species, flavor,
named function, link direction, and gluon color class. Registry order is
lexical and duplicate IDs fail closed. The registry describes the accepted
forward boundary and its existing callables without changing their kernels.
