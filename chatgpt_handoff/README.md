# DeuteronWigner ChatGPT Handoff

This directory contains the project handoff bundle for ChatGPT review. It is
the only new directory in this branch; existing repository files are not
replaced.

## Reconstruct the ZIP

From this directory, concatenate the parts in lexical order:

```bash
cat DeuteronWigner_ChatGPT_Handoff_2026-08-28.zip.part-* \
  > DeuteronWigner_ChatGPT_Handoff_2026-08-28.zip
shasum -a 256 DeuteronWigner_ChatGPT_Handoff_2026-08-28.zip
```

Expected SHA-256:

```text
9f807d32be336e5ce68fbfef5d5add9a2bc63675a70de6df55ba8c8fad80df9e
```

The reconstructed ZIP is about 244 MiB and contains the current project
source, tests, scripts, references, handoff materials, validation evidence,
tracked data/output, the frozen Q0/Q1 backend worktrees, and MSHT20 metadata.
Local environments, caches, generated bulk data, and the roughly 845 MB raw
MSHT20 replica grid are excluded. See `CHATGPT_HANDOFF_INDEX.md` inside this
directory and inside the reconstructed ZIP for the reading order and scope
boundaries.

The MSHT20 source is identified in the project as a protected direct-author
transfer. Confirm permission before redistributing any replica payload.
