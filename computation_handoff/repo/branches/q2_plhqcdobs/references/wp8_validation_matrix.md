# WP8 machine-readable validation matrix

The authoritative requirement map is `validation/wp8_manifest.json`. Generate
the current report with:

```text
/Users/dustin/miniforge3/bin/python \
  scripts/build_wp8_validation_report.py \
  --python /Users/dustin/miniforge3/bin/python
```

The builder collects pytest node IDs, verifies every mapped selector,
provenance document, and required artifact, executes the full suite once, and
writes `outputs/validation/wp8_acceptance_report.json`. It distinguishes:

- `verified`: an implemented requirement has mapped evidence and the full
  suite passes;
- `partial`: mapped evidence passes but the manifest records a remaining
  scope deficiency;
- `open`: no implementation is claimed;
- `missing_or_failed_evidence`: an expected selector/artifact/provenance item
  is absent or the suite fails.

`completion_ready` is true only if every entry is verified. It cannot become
true merely because pytest is green.

The current 2026-07-26 report collected and passed 334 tests. All 12
requirements are verified, none is partial/open, no evidence mapping is
missing, and `completion_ready=true`.
