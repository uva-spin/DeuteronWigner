# C23/P0 analytic API

`deuteron_wigner.process.p0` provides immutable `ProcessId`,
`MeasurementRecord`, `HarmonicId`, `HardFactorRecord`, `PartnerRecord`,
`FixedOrderReference`, and `FactorizationGlauberCertificate` objects.

`EligibilityRegistry.require_analytic()` is the only input gate. It consumes
the C22Q eligibility matrix and rejects unknown or ineligible IDs.
`require_source()` and `require_physical()` always fail because those sets are
empty.

`AnalyticWYOracle.pieces(qT,Q)` returns W, its same-order asymptotic expansion,
FO, Y=FO-asymptotic, W+Y, and matching residual with `VALIDATION_ONLY` status.
`make_oracle()` requires a passing eligibility set and factorization/Glauber
certificate.

Reproduce with:

```bash
python scripts/build_c23_manifests.py 1095
python scripts/validate_c23_architecture.py
pytest -q tests/test_c23_p0_analytic.py tests/test_c23_manifests.py
```
