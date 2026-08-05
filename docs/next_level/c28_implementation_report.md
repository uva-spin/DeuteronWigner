# C28/P1D implementation report

## Result

C28 reproduces the complete public ART25 low-qT dataset route at the narrow
`SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION` tier. It does not claim an
author-frozen reproduction, full W+Y, a physical deuteron prediction, a
microscopic-project calibration, inference readiness, or production readiness.

The authoritative historical source is public `artemide-DataProcessor` commit
`761f3fcdd3701c5cf69e822f9ffbbd5db394fc58`; current public commit
`9f9dda71b69dd26e288be189a396736827cfeed3` remains a separate comparison.
A complete-history bundle and every dataset/source file are hash locked.

## Native dataset and selection closure

The historical ART25 analysis names 36 unpolarized Drell–Yan datasets and 10
unpolarized SIDIS datasets. Native `DataSet.LoadCSV` loading gives 8,675 source
points. Executing the historical `cutFunc` retains 1,209 points and excludes
7,466: 627 DY and 582 SIDIS. A separate explicit reason ledger reproduces every
native decision with zero disagreement; it is an audit oracle, not the
selection authority.

CDF1 remains the immutable regression: SHA-256
`c0a178d9579017a7de91abf63df667d1bb3009253ce15b56fe428d32fc430c81`,
50 loaded, 33 retained, and CDF1.0 exactly 3.4394876804377352 pb/GeV. Its raw
native integral is 1.7197438402188676 and its theory factor is 2.0. The result
is absolute, qT-bin integrated and averaged, and W-only.

## Executed observable semantics

The DY route is `DataProcessor.harpyInterface` to `harpy.DY.xSecList`, with
native qT, Q-squared, and physical-rapidity bin integration, per-point theory
factor, source electroweak process code, and fiducial cuts. The SIDIS route is
the corresponding native `harpy.SIDIS.xSecList` integration in transverse
momentum, z, x, and Q-squared. Its dataset theory factors carry the source
multiplicity/DIS normalization convention and the source process code fixes
target and hadron charge. Both routes use unchanged ARTEMIDE v3.01 source
settings and return the resummed low-qT W term only.

The central technical record completed all 1,209 points without a dropped
point. Native per-dataset chi2 values and profiles were computed using
DataProcessor’s own variance columns, correlated systematic columns,
normalization directions, A-matrix solution, and decomposition. Central
chi2 is 733.3634803213348 for DY, 536.8536205509276 for SIDIS, and
1270.2171008722626 combined. These are source-regenerated central-record
values, not published fit anchors and not degrees-of-freedom claims.

## Joint source ensemble and covariance

All 642 stochastic ART25 rows are executed as indivisible joint identities:
the Lambda row, 22 fitted parameters, six controls, MSHT replica, pion and
kaon MAPFF replicas, CS kernel, TMDPDF, and both TMDFFs stay coupled across all
datasets. Heavy predictions, chi2, and nuisance arrays are stored outside Git
under `data/runtime/c28_art25/`; committed manifests record hashes, dimensions,
member order, and reconstruction.

The exact theory covariance is represented by the 642 by 1,209 anomaly factor

`A[member, point] = (T[member, point] - mean[point]) / sqrt(641)`.

Selected dense blocks are reconstructed as `A[:, I].T @ A[:, J]`. The same
joint rows preserve DY–DY, SIDIS–SIDIS, DY–SIDIS, and C27
distribution–process covariance. Experimental covariance, normalization
nuisances, numerical integration uncertainty, and source-version uncertainty
remain separate; C28 creates no likelihood.

Member 1 was recomputed through independent serial and clean-restart routes.
Prediction and restart residuals are exactly zero; the serial-versus-shard
chi2 residual is `2.842170943040401e-14` and the nuisance-profile residual is
`6.827871601444713e-15`, both floating-point roundoff.

The exact C27 extension binary exposes only the seven-argument
`dy_xsec_single` ABI. The public Python wrapper advertises an optional `Num`
qT-section argument, but that eighth argument cannot be passed to this binary.
C28 therefore records the higher-section diagnostic as unavailable rather
than recompiling or changing the validated source route. The source-compiled
default reproduces CDF1.0 with zero residual.

## W+Y and provenance decision

The public source tree does not provide a DY or SIDIS fixed-order/asymptotic
pair with exact ART25 measurement, cut, scheme, mass, scale, threshold, rank,
harmonic, and order identity. `OtherPrograms/ptW-benchmark` is a mismatched DY
benchmark. The C23 analytic Y is deliberately excluded. Thus all 1,209
retained points qualify only as source-reproducible low-qT W; full source
process, W+Y, and physical-input eligibility remain zero.

External ART25 phenomenology and the project microscopic spin-1 root remain
disjoint. The former neither replaces the microscopic boundary nor converts a
proton result—or a phenomenological deuterium-target SIDIS record—into a
microscopic deuteron prediction.

## Reproduction and evidence

The machine-readable manifests in this directory contain the complete point
inventory, cut decisions, central predictions, nuisance profiles, member
identities, anomaly-factor hashes, covariance blocks, readiness matrices,
1,360 requirement records, and 1,320 ordered negative controls. Rebuild with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c28_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c28.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

Raw transferred `MSHT20_REP` grids remain outside Git because explicit public
redistribution permission is unresolved. See `c28_source_release_policy.md`.

The complete suite passes: 1,131 tests. C28 validation and the inherited C27
validator pass, all eight authoritative artifacts are byte-identical, and the
production registry remains fixed at 216 routes. Two consecutive manifest
builds produced byte-identical hashes for all 45 C28 JSON records.
