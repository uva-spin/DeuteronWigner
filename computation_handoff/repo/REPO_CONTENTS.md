# DeuteronWigner computation repository snapshot

This directory is a public, reproducible continuation snapshot assembled from
the canonical `/Users/dustin/work/DeuteronWigner` checkout. The current source
commit is recorded in `CURRENT_SOURCE_COMMIT.txt`; the C401-C410 continuation
summary is in `C401_C410_REPOSITORY_HANDOFF.md`.

The historical archive material in this snapshot was originally assembled on
2026-08-28. The live continuation tree is maintained against accepted `main`
commits and must be refreshed after each accepted phase or material scientific
commit.

## Contents

- The project source tree at the accepted source commit recorded in
  `CURRENT_SOURCE_COMMIT.txt`.
- The current tracked working-tree state plus the explicitly present
  untracked code, tests, reports, and documentation from the root checkout.
- Clean source snapshots of `q0/plhqcd0`, `q1/plhqcdstate`, and
  `q2/plhqcdobs` under `branches/`.
- A complete all-ref Git history in `history/`, split into files below the
  GitHub per-file limit. Reassemble with:

  ```bash
  cat history/DeuteronWigner-all-refs.bundle.part-* \
    > /tmp/DeuteronWigner-all-refs.bundle
  git bundle verify /tmp/DeuteronWigner-all-refs.bundle
  ```

- The reproducible YOLO controller, policies, prompts, hooks, skills, plugin
  metadata, and non-session state under `yolo/`.
- Archive parts and source metadata under `archives/`.
- Exact status, patch, untracked-path, and published-YOLO-path inventories
  under `worktree_state/`.

## Deliberate safety and size exclusions

The local worktrees contain credentials, session transcripts, SQLite state,
caches, virtual/Conda environments, nested Git worktree pointers, raw source
replicas, and generated multi-gigabyte data. These are not public source-code
artifacts and were not copied here. In particular, the local `auth.json`
symlink and all session/log/database content were excluded. The exact local
untracked inventory remains in `worktree_state/actual_repo_untracked_paths.txt`.

The raw/generated exclusions are also consistent with the project’s existing
`.gitignore` and handoff policy. Their metadata, source locks, acquisition
instructions, and reproducibility records remain where available.

This directory is a nested source-and-history repository payload inside the
outer `computation_handoff` directory. Its `history/` bundle preserves the
Git commits and refs; the outer repository does not treat this nested payload
as a Git submodule.
