# C165/HQCDLFGDEP implementation report

Status: `C165_HQCDLFGDEP_DEPENDENCY_LOCATOR_INCOMPLETE`
Plan: `LFGDEP-D`
Next continuation: `C166/HQCDLFGDEP2`

Baseline commit: `51ac9228a9c31460db1210c74824e5875db9d32e`.
Consumed contract: `docs/next_level/c164_c165_hqcdlfgdep_continuation_contract.json`.
Contract SHA-256: `720a496fe37e704ca8ac128777c959cd7be51156a23352dc13ca88b570d3888a`.

The C164 package root was read from its committed manifest and verified as
`6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2`.
All eight C164 accepted locator records are imported from the C164 public API;
their hashes, labels, pages, boxes, render hashes, and visual statuses are
unchanged.

Dependency census:

- 8 immutable accepted C164 root objects.
- 55 bounded source-symbol/reference records.
- 114 exact candidate dependency locator records generated before selection.
- 55 accepted object-level dependency locators, all visually verified with
  page-text, render, crop, anchor, and bounding-box records.
- 8 acyclic, source-version-consistent graphs; 0 closed graphs and 32 exact
  unresolved dependency leaves.
- 25 descriptor records retained: 8 dependency-incomplete, 13 preserved
  absent-final-object records, and 4 preserved source-role mismatches.

Representative exact dependency groups are recorded by the public manifest:

- RI/SMOM: arXiv:0901.2599v2 printed pages 4, 5, 8, 9, and 10, including
  objects `(3)`, `(5)`, `(8)`, `(9)`, `(10)`, `(15)`, `(16)`, `(18)`, `(19)`,
  and `(23)`.
- MOMq: arXiv:1108.4806v1 printed pages 4, 5, 6, 8, 9, and 24, including
  `(2.1)`, `(2.3)`–`(2.8)`, `(3.1)`, `(3.5)`–`(3.7)`, and `(6.35)`; the qg
  branch retains the raw vertex object `(6.34)` as the immutable C164 root.
- Coupling step scaling: arXiv:1706.03821v2 printed page 2, objects `(4)`–`(8)`.
- Signed-mass step scaling: arXiv:1802.05243v2 printed pages 3 and 4,
  objects `(2.1)`, `(2.2)`, `(2.9a)`, `(2.9b)`, and `(2.10)`–`(2.13)`.

The unresolved leaves are not generic placeholders: each request identifies
the exact root, symbol/semantic dependency, required node class, source
version, missing object type, and effect on coordinate, projector,
gauge/scheme/N_f, or renormalization/step-scaling interpretation. The signed
mass and coupling dependency gate remains explicitly closed.

No complete expression was transcribed, no target program or value was
created, no C158 value was imported or recomputed, and no PDG value, running,
threshold, matching, common-IR, remainder, bracket, window, counterterm,
null-coordinate, or quantum object was consumed or modified. C134 remains the
pre-existing quarantined diagnostic, and the inherited untracked C157 test is
untouched.

Validation records cover the authoritative C153–C165 boundary, two clean
builds, restart/sharding/query-order checks, safe loading, dependency graph
holdouts, and 384 live mutations. Only the C165 package, runtime manifest,
tests, evidence records, and the single C166 continuation are committed.
