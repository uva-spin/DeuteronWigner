# C25/P1A API

`deuteron_wigner.process.p1a` is a validation-only, production-isolated API for the official ART25 member file.

- `ART25MemberParser.parse(path)` returns an immutable `ART25MemberEnsemble` and `ART25MemberValidationReport`.
- `ART25LambdaMember` retains the 22 fitted values, all 28 stored NP slots, the PDF/pion-FF/kaon-FF member triplet, role, record locator, and source hash.
- `ART25MemberEnsemble.statistics()` independently calculates stochastic-member means, 16/84 percentiles, the central record, and the full 22-by-22 correlation matrix.

The API does not initialize ARTEMIDE, substitute unavailable collinear sets, execute process predictions, or connect to the 216-route production registry.

Rebuild and validate with:

```bash
PYTHONPATH=src python scripts/build_c25_manifests.py <test-count>
PYTHONPATH=src python scripts/validate_c25.py
```
