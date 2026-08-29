# C24/P1 source-qualification API

The `deuteron_wigner.process.p1` package is a validation-only gate layer. It
does not evaluate a physical cross section and is unreachable from the
production registry.

`SourceLock` binds paper, software, or data identity to a version, canonical
locator, local SHA-256, license, domain, and uncertainty tier. `verify(root)`
fails on a missing or modified source. Paper, software, and data are separate
records; ARTEMIDE 3.03 therefore cannot satisfy the ART25 3.01 lock.

`QualificationDecision` accepts the complete ordered source and physical gate
maps. `source_eligible` is true only if all thirteen source gates pass.
`physical_eligible` additionally requires all six covariance, joint-member,
domain, ancestry, non-synthetic, and nuclear-component gates. `record()`
returns every failed gate. The constructor rejects undeclared gate schemas,
unsupported ranks, and a matched-total nuclear plan.

`candidate_decisions()` provides the audited minimal T-even process families.
All currently remain source-interface-only because the official ART25 model
constants/replicas, compatible TMDFF member map, exact fixed-order software or
ancillary, and gluon boundary are incomplete. `injection_rows()` creates 880
stable ordered negative controls.

Rebuild and validate with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c24_manifests.py 1112
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c24_architecture.py
```

