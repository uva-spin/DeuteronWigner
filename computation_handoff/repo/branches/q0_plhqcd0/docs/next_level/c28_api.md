# C28/P1D typed API

C28 adds immutable validation records in
`src/deuteron_wigner/process/p1d/core.py`. They describe evidence; they do not
create a fit, posterior, production route, or microscopic-to-ART25 bridge.

## Identity and source records

- `DataProcessorRepositoryId` locks repository URL, commit, branch, and bundle.
- `ART25AnalysisSourceId` identifies the historical analysis source separately
  from current public master.
- `DatasetFileLock` binds one native dataset file to its hash and source commit.
- `DatasetPointId` preserves dataset and point identity through every table.
- `MeasurementConvention` stores process, observable, units, integration, and
  normalization semantics.

## Prediction and uncertainty records

- `ART25SelectionDecision` records a source-derived accept/reject decision.
- `ART25PointPrediction` binds a joint member, point, prediction, and semantics.
- `TheoryEnsembleFactor` describes the exact mean-subtracted member anomaly
  factor, normalized by `sqrt(Nmember - 1)`.
- `SourceReproducibleLowQtContract` encodes the narrow public-source W tier.
- `WYReadinessRecord` keeps W evidence distinct from fixed-order/asymptotic
  partner closure.

All records are frozen dataclasses, validate mandatory identity fields, and
serialize deterministically with content hashes. Invalid identities fail
closed. Heavy member-by-point matrices live in `data/runtime/c28_art25/`; the
committed manifests give their schema, shape, hash, and reconstruction command.

## Reproduction

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/run_c28_art25_datasets.py --help
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c28_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c28.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

The member runner must execute in isolated processes because ARTEMIDE has
mutable global replica state. Merge only by explicit `lambda_index`; never by
array position alone.

