# C4 validation-pilot API

`SectorSuperposition` and `SectorRecord` represent normalized orthogonal Fock
direct sums. `sea_state(P_sea, pair_flavor)` and `gluon_state(P_g)` build the
minimal Benchmark-E families. `ProductGaussianState` implements the
arbitrary-particle amplitude protocol consumed by the unchanged C3
`AnalyticOverlapEvaluator`.

`PositiveXActiveSelector` returns typed quark, antiquark, or gluon slot
records. `parents_from_state` constructs regulated diagonal parents and
returns an empty tuple for structurally absent species.

`SeaColorSinglet` and `GluonColorSinglet` expose normalized tensors and total
SU(3)-generator residuals. The latter records the selected `rho` octet
multiplicity channel.

`CommonReductionRoutes` provides regulated TMD, GPD, PDF, direct integration,
and local-moment routes. Every `RouteResult` carries matching, operator, path,
species, flavor, scalar, Mellin, transfer, and residual metadata.
It also carries the outstanding matching morphisms: UV plus rapidity/soft for
the TMD route, and link-shortening plus UV matching for regulated
GPD/PDF/current routes.

`project_gluon_polarization` implements the typed transverse trace,
antisymmetric-helicity, and symmetric-traceless projectors and reconstructs
the original two-dimensional gluon polarization matrix.

`FiniteFeshbachModel` supplies the exact two-sector Hamiltonian and induced
operator benchmark. `require_exclusive_representation` and the C4 provenance
plans reject explicit-plus-induced double counting.

All APIs are validation-only. `RegulatedParent.promote_to_production()` fails
closed, and no production builder imports the pilot package.
