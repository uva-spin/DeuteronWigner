# C400 ChatGPT handoff

This archive is the complete live-integration handoff for the C400 P1/P1B/P1C work and the supplied C400.S2 corrective patch. Review `docs/phases/c400_s2_corrective_patch/live_integration/implementation_report.md` first, then `blocker_or_completion.json`, `upstream_tests.json`, and `repository_discrepancies.json`.

## Current status

- Primary S2 status: `LIVE_INTEGRATION_ACCEPTANCE_READY`.
- Next owner: `USER_CHATGPT`.
- Isolated branch: `codex/c400-p1-mechanical-closure-v2`.
- Baseline HEAD: `44b2d6002865b819fc524efb0af7988c0b6304a8`.
- S2 patch SHA-256: `37ef4a6f61cc70c908a84be6d7466db50fff238c78542aace029b0e49126089f`.

## What was integrated

The supplied S2 patch adds truthful status supersession, a 57-row C396 coordinate-binding ledger, versioned C144 derivative-integrity checks, projector-qualified state identity, adversarial state tracking, canonical LF/LPS comparison, semantic replay, and a deterministic evidence generator. It does not replace C396 operators with C144 fixtures.

## Validation

- Focused P1/P1B/P1C/S2 suite: 43 passed, 0 failed.
- Generated invariant checks: all pass; 33/33 corrected C144 derivatives, 6 historical mismatches, 57 C396 binding rows, 0 complete C396 numerical apply paths, semantic replay pass.
- Relevant upstream suite: 41 passed, 2 strict failures caused by the absent `data/runtime/c64_qgtm2/index.json`.
- Full local profile: 76 collection errors from the same strict C64 artifact gap.
- Compilation: passed with `PYTHONPYCACHEPREFIX=/tmp/c400_s2_pycache`; default macOS cache location was not writable.
- No manual reconciliation, commit, merge, push, activation, physical fit/rank/current selection, or P2 launch.

## Scientific boundary

No physical Hamiltonian, C396 numerical forward map, physical deuteron-sector identity, production current, physical likelihood, physical rank, coordinate irrelevance, resolution average, or activation was established. The unprojected C144 eigenpair remains diagnostic only.

## Archive contents

The handoff includes the frozen `.phase_mode` inputs; current P1/P1B/P1C/S2 source, test, and generator files; P1/P1B/P1C/S2 reports and generated evidence; restored raw C140/C43/C395 sources and Abbott/BLAST records; the original supplied S2 package and its manifest; the live-integration record; and a file/hash manifest for this archive.

The full local pytest profile is intentionally not represented as passing. The C64 artifact is not regenerated or substituted.
