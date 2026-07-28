# C1 typed-identity API

The `deuteron_wigner.formal` package is an immutable, dependency-light spine
around the accepted numerical model.

* `CoordinateSpec` identifies one of eight physically distinct transverse
  coordinates, its frame, units, conjugate, Fourier sign, and measure.
* `RankSpec` identifies angular weight, tensor basis, extracted momentum and
  impact powers, reference mass, Bessel order, Fourier phase, and whether the
  stored value is a coefficient or a contracted modulation.
* `SectorId` distinguishes microscopic Fock, hadronic nuclear, and
  phenomenological-component resolution. Equal array shape has no identity
  significance.
* `WilsonPathId` and `GluonLinkId` preserve staple orientation, ordered
  segments, representation, ordered link pairs, and `F_TYPE`/`D_TYPE`.
* `DecoratedOperatorId` binds species/flavor/projection, fibers, coordinates,
  rank, Wilson/color, regulator/scheme/scales, normalization, evidence, and
  version. Completeness is operation-specific.
* `TypedMap` distinguishes `AMP`, `DENS`, `MATCH`, `RED`, and `PROC`.
  `AdapterRegistry.compose` permits exact endpoint equality or a registered
  provenance-bearing adapter. It never coerces by array shape.
* `ArchitectureError` supplies a requirement ID, expected and received
  identities, and a suggested explicit adapter when one is known.

`legacy_adapters.registry_operator_identity` decorates registry entries from
existing schemes, scales and link labels. `typed_bessel_b_to_k` checks
coordinate and rank metadata, then calls the unchanged accepted transform.
The adapters never modify their numerical inputs.

`NOT_APPLICABLE` means a field has no physical role for that object;
`UNSPECIFIED` means it has not been declared. Production completeness checks
reject the latter and never silently convert it to the former.
