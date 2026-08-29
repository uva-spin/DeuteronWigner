# C44/HQCD API

`deuteron_wigner.bridge.hqcd.projection_audit()` reads the live C43 mode,
projection, and physical-resolution records and returns the exact C44
preflight decision. `assert_mode_projection_incomplete()` enforces the
fail-closed branch.

Run `PYTHONPATH=src python3 scripts/build_c44_fail_closed_artifacts.py` to
regenerate C44 records. This API has no numerical QCD matrix generator.
