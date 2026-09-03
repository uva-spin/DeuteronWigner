# C44/HQCD finite-mode projection no-go

C44 consumes the C43 action, source locks, physical C32 resolution trajectory,
and projection interfaces before attempting a matrix.  That preflight finds
that C43 deliberately records `COMPLETE_INTERFACE_ONLY`: it does not specify
the finite longitudinal cell/measure, normalized 2D oscillator functions and
phase convention, source-to-overlap spinor/polarization map, or global-color
and zero-mode projection for a colored matching probe.  These are necessary
to distinguish a source-derived matrix element from a convenient numerical
recipe.

No C44 mode vector, q/qg basis, color projector, Hamiltonian, vertex,
instantaneous/constrained/boundary/zero-mode operator, counterterm direction,
or comparison map is generated.  The provisional arrays created during
preflight were discarded rather than retained as physics. C40 remains
`EXECUTABLE_METHOD_ORACLE_ONLY`.

The exact result is `C44_MODE_PROJECTION_INCOMPLETE`. C45/MODES must first
close the four missing finite-projection contracts, after which C44/HQCD can
be retried without using C40 arrays or fitting a result.
