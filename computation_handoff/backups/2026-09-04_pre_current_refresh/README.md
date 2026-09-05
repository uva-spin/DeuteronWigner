# Pre-refresh computation-handoff backup

This directory preserves the review-facing surface of
`computation_handoff/repo/` immediately before the 2026-09-04 refresh from the
canonical `/Users/dustin/work/DeuteronWigner` checkout.

Archive:

- `repo_review_surface_pre_refresh.tar.gz`
- SHA-256: `68bec6135598f3e93b451251aca5f1e5dc3594b5719583db476f1efc58ba4088`
- compressed size: approximately 18 MiB
- integrity: `tar -tzf` completed successfully

The archive contains the old snapshot's source, scripts, tests, reports,
references, handoff files, tools, validation records, top-level environment
and package declarations, source marker, README, and all four
`REPO_CONTENTS.*` inventory files.

The large historical payloads under `repo/archives/`, `repo/branches/`,
`repo/history/`, `repo/yolo/`, `repo/worktree_state/`, `repo/data/`, and
`repo/output/` are not duplicated here because this refresh does not modify
them. They remain preserved in place and in Git history.

To inspect without overwriting anything:

```sh
mkdir -p /tmp/deuteron-handoff-pre-refresh
tar -xzf repo_review_surface_pre_refresh.tar.gz \
  -C /tmp/deuteron-handoff-pre-refresh
```

This backup is historical evidence, not a current scientific authority.
