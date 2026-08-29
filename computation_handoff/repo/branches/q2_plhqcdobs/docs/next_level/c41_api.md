# C41/R2B API

`deuteron_wigner.bridge.r2b.audit_c40_substrate()` returns the source and
derivation audit for each required C40 object.  `assert_c40_not_eligible()`
asserts the Branch-B result: zero objects are eligible for a C41 diagram.

Regenerate C41 records with:

```bash
PYTHONPATH=src python3 scripts/build_c41_fail_closed_artifacts.py
```

This package intentionally exposes no one-loop correlator, counterterm
solver, continuum oracle, soft subtraction, matching kernel, proton, ART25,
or production API.
