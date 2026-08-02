# C22Q/M3Q API

`deuteron_wigner.matching.m3q` exposes:

- `evaluate_qualification(operator_id, gates)`, the sole authoritative gate
  evaluator. It returns all validation, source, and physical failures.
- `reconcile_rows(c22_rows)`, which builds the 540-entry cross-layer record.
- `tier_counts(rows, field)`, used for deterministic qualification and process
  eligibility counts.
- `minimal_family_audit()`, `cs_largeb_manifest()`, and
  `nuclear_qualification()`, which preserve the corresponding tier semantics.

Rebuild and validate with:

```bash
python scripts/build_c22q_manifests.py 1081 a1527fefc259eb32e362ccda5db135fb52149ad5
python scripts/validate_c22q_architecture.py
```

This API evaluates eligibility only; it contains no process/W/Y execution.
