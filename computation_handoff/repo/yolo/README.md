# DeuteronWigner Persistent YOLO Frontier

This is the simpler alternative to the API-supervisor controller.

It uses one persistent Codex session, a global `AGENTS.override.md`, an
external state file, and a `Stop` hook. Whenever Codex tries to finish an
ordinary turn, the hook returns `decision: "block"` with the next continuation
instruction, which Codex treats as a new user prompt.

## Policy

```text
operational YOLO
scientific fail-closed
```

Codex autonomously:

```text
implements;
tests and repairs;
commits locally;
reads the next exact frontier;
generates the next contract and prompt;
updates persistent state;
continues.
```

It stops only on:

```text
a schema-certified real math/physics blocker;
an exceptional infrastructure blocker;
or PENNYLANE_PHYSICAL_ACTIVE.
```

The repository’s current baseline is C202 commit:

```text
2c595d90f6b520fa52ea337c08521996442eaa3c
```

The first job is:

```text
C203/HQCDBRST1
```

## Installation

Unpack this directory, then:

```bash
cd deuteron_wigner_persistent_yolo
./install.sh
```

The default installation root is:

```text
/Users/dustin/work/DeuteronWigner-yolo
```

The default scientific repository is:

```text
/Users/dustin/work/DeuteronWigner
```

Override them with:

```bash
YOLO_HOME=/another/path \
DEUTERON_WIGNER_REPO=/another/repo \
./install.sh
```

The installer does not edit the scientific repository. It creates a separate
`CODEX_HOME` and symlinks the existing `~/.codex/auth.json` when present.

## Launch

```bash
/Users/dustin/work/DeuteronWigner-yolo/run_persistent_yolo.sh
```

The configuration uses:

```text
approval_policy = never
sandbox_mode = danger-full-access
web_search = live
hooks = enabled
goals = enabled
multi-agent = enabled
```

Run this only on the trusted DeuteronWigner repository and host.

## Stop

Create:

```bash
touch /Users/dustin/work/DeuteronWigner-yolo/STOP
```

Remove it before resuming:

```bash
rm /Users/dustin/work/DeuteronWigner-yolo/STOP
/Users/dustin/work/DeuteronWigner-yolo/run_persistent_yolo.sh
```

## State and logs

```text
state/AUTOPILOT_STATE.json
state/REAL_BLOCKER.json
state/CODEX_SESSION_ID
logs/*.jsonl
```

The launcher resumes the same Codex session after a process crash. The
repository and external state remain the source of truth after context
compaction.

## Why this is different from the earlier autopilot

There is no separate OpenAI API supervisor and no attempt to communicate with
a ChatGPT web conversation. Codex generates and executes each next prompt
itself. The deterministic state and Stop hook prevent it from ending after a
normal job.

## Security boundary

This is intentionally YOLO mode and grants `danger-full-access`. The master
prompt still forbids pushes, history rewriting, unsupported physical
selection, protected-path changes, and scientific gate weakening. The manual
`STOP` file is the kill switch.
