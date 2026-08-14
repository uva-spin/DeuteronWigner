# C117/ICREG2 implementation report

Status: `C117_C116_SOURCE_DERIVED_GRAPH_SPECIFIC_CURRENT_PROJECTOR_AUTHORITY_READY`.

The four missing C116 classes are constructed as distinct finite-shell
objects. `I2_density_projector` is an orthogonal graph-conditioned mode
projector with a local density kernel; `derivative_density` is a weighted
non-idempotent density operator; `CM_ground` is the transformed exact
TM/CM-ground projector; and `triplet_projected` is the C74 `U3 U3^dagger`
color projector. Explicit ordered finite-mode routes and closed operator
identities agree with zero residual for all four. No continuum completeness,
threshold, C57/C58 reuse, or zero substitution is used.

The projector authority is complete, but current numerical component and
instantaneous-current block assembly remains deferred to `C118/ICASM2`.
