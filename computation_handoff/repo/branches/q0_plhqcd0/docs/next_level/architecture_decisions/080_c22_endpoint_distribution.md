# ADR 080: exact endpoint-distribution convention

**Decision.** Store delta, regular, and logarithmic plus terms as distinct
immutable objects on [0,1]. For a lower limit, retain the integral over the
excluded interval required by the plus prescription. Endpoint cutoffs are not
physical parameters. Independent quadrature and Mellin moments are required.
