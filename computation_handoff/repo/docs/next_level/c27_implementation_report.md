# C27/P1C implementation report

## Result

C27 closes the exact collinear-input and execution gaps identified in C26.
The directory transferred directly by Alexey Vladimirov is the custom
`MSHT20_REP` DataVersion 3 ensemble used by ART25. It contains metadata and
grid files numbered 0000 through 1000. The source metadata declares 1000
members, and the ART25 generator selects indices 0 through 999; therefore the
extra 1000 grid is preserved but excluded rather than silently changing source
semantics. Redistribution permission was not supplied and remains unresolved.

All 642 stochastic ART25 rows now resolve an exact MSHT PDF member and exact
MAPFF pion and kaon members. The unchanged ARTEMIDE v3.01 engine initializes
with the unchanged official ART25 constants. A source-neutral derivative of
the constants changes only the absolute LHAPDF search path because `/data` is
not writable on this platform; it changes no set name or physics value.

## Execution and uncertainty

The central technical record and all 642 stochastic rows were executed for a
CS-kernel point, eleven-component TMDPDF, pion and kaon TMDFF vectors, three
DY points, and two charge-resolved SIDIS points. All 642 completed with no
failure or imputation. A four-process reconstruction and two independent
restart shards agree exactly with the uninterrupted serial calculation.

The 39-dimensional empirical joint covariance is constructed from the same
indivisible members, including distribution/process and DY/SIDIS cross blocks.
It is symmetric and positive semidefinite within the recorded numerical
tolerance. Marginal reshuffling is explicitly prohibited.

Four independent checks pass: direct NP formulas, an LHAPDF evaluation of
exact MSHT member 599, independent NumPy ensemble statistics, and an
independently initialized restart calculation.

## Scientific qualification

The numerical outputs are `SOURCE_REGENERATED_OUTPUT`; no author-provided or
repository-frozen output bundle was supplied, and no figure was digitized.
The five explicitly regenerated low-qT validation points establish a
`SOURCE_TMD_W_TERM_REPRODUCED` record. They do not establish W+Y because a
source-identical fixed-order/asymptotic partner is absent. The status remains
`SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE`.

Unchanged gates were rerun. External ART25 source-process eligibility remains
zero because authoritative frozen anchors, complete measurement provenance,
fixed-order partners, and experimental covariance are missing. Physical-input
eligibility is zero. The project microscopic/deuteron root also remains zero;
the proton ART25 reproduction is never promoted to a deuteron prediction.

## Reproduction

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c27_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c27.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

The heavy transferred grids and runtime checkpoints are deliberately kept out
of Git. Their hashes, provenance, member mapping, and exact local locations are
recorded in the machine-readable C27 manifests.
