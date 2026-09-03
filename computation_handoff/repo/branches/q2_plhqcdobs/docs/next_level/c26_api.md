# C26/P1B API

`deuteron_wigner.process.p1b` provides immutable validation-only objects for collinear source locks, exact member resolution, ART25 joint-member identities, and independent nonperturbative model oracles.

- `CollinearMemberEnsemble.resolve(index)` resolves only an existing, hash-locked source member and fails on missing indices.
- `ART25CollinearIndexMap.validate(ensemble)` preserves each Lambda row’s PDF, pion-FF, and kaon-FF indices. It never wraps, clips, or fills a missing source.
- `tmdpdf_np` and `tmdff_np` directly translate the official Fortran nonperturbative functions without calling ARTEMIDE.

The module is disconnected from production and cannot promote an external proton fit to the microscopic or deuteron process plan.

```bash
PYTHONPATH=src python scripts/build_c26_manifests.py <test-count>
PYTHONPATH=src python scripts/validate_c26.py
```
