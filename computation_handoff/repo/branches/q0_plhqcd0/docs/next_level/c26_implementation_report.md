# C26/P1B implementation report

## Outcome

C26 acquired the exact official CERN LHAPDF archives named `MAPFF10NNLOPIp` and `MAPFF10NNLOKAp`. Both are DataVersion 1 Monte Carlo sets containing member 0 (mean) and members 1–200. Their current archive timestamps are June 2022, before the ART25 analysis, and the ART25 constants use these exact names. All 402 member files, both `.info` files, and both tarballs are hash locked. No negative-charge, charge-sum, NLO, or renamed set was used.

Every pion and kaon index in all 642 stochastic Lambda rows resolves exactly: both ranges are 0–199, with 1,284 successful FF resolutions, no wrap, clip, drop, duplicate, or central replacement. Independent LHAPDF evaluations use Lambda member 1’s exact pion member 75 and kaon member 109.

## Residual source blocker

`MSHT20_REP` remains unavailable after auditing the complete ARTEMIDE and DataProcessor Git histories and bundles, the official LHAPDF index, ART25 paper sources, relevant Zenodo releases, and Software Heritage. The ART25 rows require PDF indices 0–999. The public `MSHT20nnlo_as118` set is DataVersion 4 with 65 Hessian members and is neither dimensionally nor statistically identical. It was not installed as an alias, converted, wrapped, or substituted.

Consequently the immutable ARTEMIDE v3.01 extension remains buildable/importable, but exact ART25 initialization and collinear convolution cannot complete. The constants and engine were not changed. Preflight failure prevents expensive partial process runs: zero full-source stochastic members were attempted, failed, or retried.

## Executed validation

The direct, independently translated ART25 NP functions were evaluated for all 642 stochastic members and the central record. Their small-b unity limit closes exactly; their empirical intervals and covariance are preserved. The official MAPFF grids were independently loaded with LHAPDF 6.5.5 and evaluated at exact joint-member indices. These are model-factor and FF-grid validations, not complete TMD predictions.

There is no author- or repository-provided frozen observable bundle. Therefore central DY, central SIDIS, full TMDPDF/TMDFF/CS convolution, 642-member process execution, serial/parallel/restart comparisons, and DY–SIDIS covariance remain explicitly unavailable. No figure was digitized.

## Qualification

The unchanged gates were rerun. External ART25 source-process eligibility is zero, microscopic-project source-process eligibility is zero, and physical-input eligibility is zero. A source W term was not reproduced and no C23 analytic Y was combined with it. The 438/102 analytic split, 216 production routes, and eight authoritative artifacts remain unchanged.

## Exact next package

C27/P1C should ingest an author-supplied exact `MSHT20_REP` archive or fully specified generator state and a source-owned frozen-output bundle, verify every member and checksum, then execute the immutable frozen grid and all 642 joint members. Without those source objects, qualification must remain closed.
