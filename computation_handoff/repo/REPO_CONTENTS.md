# DeuteronWigner computation repository snapshot

This directory is a public, reproducible snapshot assembled from the local
`/Users/dustin/work/DeuteronWigner` checkout and its companion
`/Users/dustin/work/DeuteronWigner-yolo` controller workspace on 2026-08-28.

## Contents

- The project source tree at local `main` commit `df125f2d`.
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
