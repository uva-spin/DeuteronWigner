# Local layout after consolidation

The canonical project checkout is:

```text
/Users/dustin/work/DeuteronWigner
```

The former `/Users/dustin/work/DeuteronWigner-yolo` controller workspace now
lives at:

```text
/Users/dustin/work/DeuteronWigner/.yolo
```

The `.yolo` directory is local-only and ignored by Git. It contains the
controller configuration, prompts, policies, state, logs, sessions, caches,
and the local credential symlink. The public, sanitized controller snapshot
is separately preserved under `computation_handoff/repo/yolo/`.

All active Git worktrees are rooted below the canonical checkout:

```text
deuteron_wigner_q0_plhqcd0
deuteron_wigner_q1_plhqcdstate
deuteron_wigner_q2_plhqcdobs
deuteron_wigner_computational_handoff
```

The Q0/Q1/Q2 branches remain independent worktrees and retain their existing
commits. The computational handoff worktree remains the source of the public
handoff branch. Missing temporary worktrees under `/private/tmp` were pruned
from Git metadata; no live project worktree was removed.

Archived YOLO records are retained as records of their original runs. Current
operational scripts and prompts use the consolidated `.yolo` path.
