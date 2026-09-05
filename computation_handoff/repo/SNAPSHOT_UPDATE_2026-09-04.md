# Computation-handoff refresh: 2026-09-04

## Review status

This directory is the local, review-ready refresh of the DeuteronWigner
continuation snapshot. It has not yet been committed or published. At the time
of this audit, public GitHub `main` was
`4075976deab34f1360278c41c16faf972038c017`, and the public
`computation_handoff/repo` still identified the C410 merge
`51d3919e4660f5709cc7bb94c576c8ec17c9de14` as its source.

The refreshed local snapshot has committed worktree base
`7dad2691607e833c0c4718a02dc2047739ab8d41` and also contains the reviewed
post-base working-tree science described below. The base commit alone does not
reproduce those post-base files. `CURRENT_SOURCE_COMMIT.txt`, the content
manifests, the current handoff, and the roadmap must be read together.

## Recovery point

Before synchronization, the prior review surface was preserved at:

`../backups/2026-09-04_pre_current_refresh/repo_review_surface_pre_refresh.tar.gz`

SHA-256:

`68bec6135598f3e93b451251aca5f1e5dc3594b5719583db476f1efc58ba4088`

The archive contains the old snapshot's live review surface: source, scripts,
tests, documents, references, handoff material, tools, validation material,
top-level environment/package declarations, source marker, README, and content
inventories. The large unchanged historical payloads under `archives/`,
`branches/`, `history/`, `worktree_state/`, and `yolo/` remain in this snapshot
and in Git history; they were deliberately not duplicated in the backup.

## What was refreshed

The following trees were synchronized from the canonical checkout while
excluding bytecode, caches, and local package-build products:

- `src/`
- `scripts/`
- `tests/`
- `docs/`
- `references/`
- `handoff/`
- `tools/`
- `validation/`

The current `AGENTS.md`, `pyproject.toml`, and `environment_quantum.yml` were
also copied. Root convenience copies of `CURRENT_PROJECT_HANDOFF.md` and
`ROADMAP.md` were added so a reviewer can find the governing state and route
without first navigating the embedded source tree.

Five small immutable runtime authority manifests required by the integrated
Q0/Q1 contracts were also copied under `data/runtime/`: C131, C142, C144,
C149, and C150. No generated bulk runtime tree was imported. This keeps the
public-authority gate executable without adding the canonical checkout's
multi-gigabyte runtime products.

The refresh preserves the older C401--C410 handoff, immutable history bundle,
frozen branch snapshots, old archives, worktree inventories, and public-safe
YOLO material as historical evidence. They are not promoted over the new
current handoff and roadmap.

## Scientific and implementation progression now represented

The refresh carries the project beyond the C410 retained-aggregation boundary:

- C411 supplies an exploratory first C117 action through the finite-C43
  adapter while keeping its source qualification and normalization limits
  explicit.
- Q0, Q1, and Q2 quantum-substrate source is integrated into the main package,
  with its acceptance reports and tests.
- A generic exploratory operator bundle now provides a dimension-checked
  contract instead of assuming that the older C7/C8 branch is automatically
  compatible.
- M2 contains the exploratory finite-K Hamiltonian/basis-map work and a K9
  invariant-projector diagnostic.
- The state/current interface now fails closed at the colored SU(3) boundary.
  The negative result is scientific information: a fixed nonzero fundamental
  quark color vector is not a physical singlet source.

The next construction is therefore not to reinterpret that colored diagnostic
as a deuteron state. It is to build the enlarged color-singlet finite-K
deuteron space `H_D,K`, then define the compatible finite-K current on that
space. Only after those contracts exist should the project form the LF/LPS
response and extend the calculation through K11, K13, continuum control,
matching/evolution, and observable prediction. The full ordered route is in
`ROADMAP.md`.

## Verification results

The following suites were run from this refreshed snapshot with the maintained
project-local Python 3.11 quantum environment, user-site imports disabled,
bytecode generation disabled, and pytest's cache disabled:

- focused M2 through the state/current boundary: 41 passed;
- frozen Q0/Q1/Q2 regressions: 33 passed (15/4/14);
- C47-plus-boundary regression: 199 passed; and
- relevant C47/C128/C401/C411/M2 integration regression: 264 passed; and
- current theory-note/machine-state contract: 6 passed.

The inventories in `REPO_CONTENTS.files`, `REPO_CONTENTS.sizes`, and
`REPO_CONTENTS.sha256` were regenerated as part of this refresh. The file and
size inventories each contain 44,776 entries; the checksum inventory contains
44,777 because it also authenticates `REPO_CONTENTS.sizes`. A complete
`shasum -a 256 -c REPO_CONTENTS.sha256` verification passed. The test runs
emitted only existing Python/SciPy warnings; there were no test failures.

## Formal-volume audit

The snapshot now contains all 22 existing formal TeX volumes, Volume 0 and
Volumes I--XXI. The only missing source was
`volume_xvi_scheme_qualified_tmds_resolved_evolution.tex`; it has been restored
from the canonical `references/` tree. The other 21 volume sources were
byte-identical between the old snapshot and the current canonical copies and
required no edits.

No Volume XXII was added. The C411 and M2 work is current implementation and
boundary-state material already owned by the living complete theory note,
machine-readable theory state, handoff, roadmap, contracts, and reports. It
does not yet establish a new formal physics contract that would justify a new
volume. Revisit that decision when the color-singlet `H_D,K` and compatible
finite-K current are mathematically fixed.

## Publication boundary

This refresh is deliberately labeled
`PREPARED_FOR_REVIEW_NOT_COMMITTED_NOT_PUBLISHED`. Review it locally before
publication. A later publication must use ordinary history-preserving Git
operations, update the public source marker in the same change, and must not
force-push or rewrite public history.
