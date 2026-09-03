# C40/M0B API

`deuteron_wigner.bridge.m0b.build_basis(K)` builds coordinate q/qg vectors,
tables, Grams, and mass arrays for declared `K` values 17, 23, and 31.
`build_bundle(K)` returns all executable arrays for one resolution.
`assert_ready(bundle, coarse=None)` performs the non-metadata numerical gate.
`readiness_report()` returns deterministic applied-operator diagnostics.

Run `PYTHONPATH=src python3 scripts/build_c40_m0b_artifacts.py` to recreate
the ignored `.npz` bundles and committed inventory/report JSON.  This API is
substrate only: it has no correlator, soft subtraction, matching, proton, or
ART25 entry point.
