# DeuteronWigner Computation Handoff

The live public continuation handoff is
<https://github.com/uva-spin/DeuteronWigner/tree/main/computation_handoff/repo>.
The canonical source checkout is `/Users/dustin/work/DeuteronWigner`; this
bundle is its published continuation view and must track the accepted `main`
commit.

This directory contains the project handoff bundle for independent technical
review and continued development. It is
the only new directory in this branch; existing repository files are not
replaced.

## Synchronization rule

After every accepted phase or material scientific commit on `main`, update the
published tree in the same publication cycle. Update
`computation_handoff/repo/CURRENT_SOURCE_COMMIT.txt`, the relevant phase
evidence, and the current repository handoff; refresh `REPO_CONTENTS.*` when
the published inventory changes; then verify, commit, and push `main`. If the
public snapshot history is not fast-forwardable from the canonical checkout,
use an authenticated GitHub Git Database/API commit based on the current
public `main`; never force-push or rewrite the public branch.
The source commit marker must identify the accepted source commit represented
by the published handoff before it is described as current. A handoff-only
publication commit may follow that source commit. The ZIP parts below are a
historical 2026-08-28 archive unless separately regenerated and relabeled.

## Reconstruct the ZIP

From this directory, concatenate the parts in lexical order:

```bash
cat DeuteronWigner_Computation_Handoff_2026-08-28.zip.part-* \
  > DeuteronWigner_Computation_Handoff_2026-08-28.zip
shasum -a 256 DeuteronWigner_Computation_Handoff_2026-08-28.zip
```

Expected SHA-256:

```text
9f807d32be336e5ce68fbfef5d5add9a2bc63675a70de6df55ba8c8fad80df9e
```

For a one-command, temporary-file-only verification (including ZIP
integrity), run:

```bash
./verify_handoff.sh
```

The verifier requires all six expected parts, checks their documented
SHA-256, tests the assembled ZIP, and removes its temporary output on exit.

The reconstructed ZIP is about 244 MiB and contains the current project
source, tests, scripts, references, handoff materials, validation evidence,
tracked data/output, the frozen Q0/Q1 backend worktrees, and MSHT20 metadata.
Local environments, caches, generated bulk data, and the roughly 845 MB raw
MSHT20 replica grid are excluded. See `COMPUTATION_HANDOFF_INDEX.md` inside this
directory and inside the reconstructed ZIP for the reading order and scope
boundaries.

The MSHT20 source is identified in the project as a protected direct-author
transfer. Confirm permission before redistributing any replica payload.
