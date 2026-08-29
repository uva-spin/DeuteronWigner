# C22/M3 API

The public validation API is `deuteron_wigner.matching.m3`.

- `DistributionConvention`, `DeltaEndpointTerm`, `PlusDistribution`,
  `RegularDistributionTerm`, and `EndpointDistribution` encode exact endpoint
  algebra. `EndpointDistribution.act(phi, lower)` implements the declared
  lower-limit prescription; `mellin(n)` supplies the independent moment route.
- `HarmonicPolylogRecord` preserves HPL word, branch, and source identity and
  fails on unsupported domains or words.
- `Gamma5SchemeRecord`, `CollinearOperatorId`, and
  `TwistTwoCoefficientRecord` carry the decorated scheme/operator identity.
- `SplittingMatrix.moment(n)` evaluates matrix-valued distribution moments.
- `SmallBOPEMap.validate()` rejects rank/Bessel or Fourier-phase aliases.
- `coefficient_records(source_hashes)`, `splitting_library()`,
  `operator_classification()`, `rg_report()`, `rank_report()`, and
  `nuclear_report()` construct deterministic validation records.

Build manifests with:

```bash
python scripts/build_c22_manifests.py 1071
python scripts/validate_c22_architecture.py
```

The API intentionally contains no process, hard-factor, fragmentation, W+Y,
likelihood, or production entry point.
