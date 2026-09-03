# ADR 202: Keep finite-cutoff power divergences separate from logarithmic UV renormalization

Status: accepted for C34/S0A.

## Decision

Store line, cusp, endpoint, transverse-closure, residual-line-mass, vacuum,
operator, logarithmic, and power-divergent UV structures separately.  No
linear or higher-power cutoff dependence may be absorbed silently into an
MS-bar logarithmic factor.  Counterterms must be state and hadron independent,
possess an inverse at the declared order, and retain the first omitted order.

## Rationale

Wilson lines in a finite regulator can carry divergences absent or scaleless
in dimensional regularization.  Lumping them makes a finite conversion
scheme-dependent and non-reproducible.

## Consequences

C34 records an unresolved UV decomposition and no numerical counterterm.
The target continuum MS-bar expression is not a counterterm solution for the
finite basis.  The representation contains separate power and logarithmic
slots, but their numerical separation is not marked proved.  Counterterm state
and hadron independence is required and remains unproved until a solution
exists.

## Revision trigger

Resolution-resolved bare diagrams determine every UV structure and a frozen
holdout validates the inverse counterterm without tuning a finite constant.
