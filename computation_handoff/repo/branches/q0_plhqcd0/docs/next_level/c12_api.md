# C12/H5 API

The package `deuteron_wigner.microscopic.h5` attaches first-Wilson-order
validation dynamics to the complete C11/H4 helicity matrices. It never
accepts projected scalar tables as microscopic input.

`SpectralSupportRule` and `ContinuumCutMeasure` define an analytic continuum
with an explicit threshold. The imaginary part is the distributional cut
`-sigma*pi*rho(Ei)*N(Ei)` and is exactly zero below threshold.
`FiniteVolumeSpectralRule` provides a typed discretized-continuum sequence;
its smearing is quadrature metadata and is absent from physical identity.

`wilson_segment` constructs the existing C5 `BareWilsonSegment` conventions.
`H5WilsonInsertion` derives its pole sign through `derived_eikonal_pole`.
`MicroscopicCutLedger` reuses the C5 ledger to count equivalent eikonal and
resolvent cuts once while retaining physically distinct support.

`H4WilsonKernel.apply` acts on a full H4 4x4 matrix. It returns a
`LinkOddHelicityParent` containing future, antiunitarily transformed past,
link-even, and link-odd matrices, exact parent/member/path identities, and a
`FockOrderSupportManifest`. Coupling, cut, and OAM removal give exact zero.

`QuarkLinkOddProjectorRegistry` and
`AntiquarkLinkOddProjectorRegistry` apply distinct Sivers and Boer-Mulders
spin projectors to the common matrix. The antiquark registry requires a
direct positive-x anti-fundamental parent.

`ordered_gluon_pairs` returns all four C6 ordered adjoint-link words.
`gluon_fd_parents` applies independent normalized f-type and d-type color
reductions and trace, helicity, and linear-polarization reductions to one H4
gluon matrix. No default color mixture exists.

`MicroscopicSoftOverlapAccount` reuses the C6 half-soft accounting. Exactly
one subtraction closes the rapidity derivative; zero and two subtractions
give equal-and-opposite residuals. The joint microscopic soft route remains
unavailable.

Diagnostics in `h5.diagnostics` generate spectral, cut, link-odd, gluon,
soft, Fock-support, convergence, replacement, and readiness reports.
