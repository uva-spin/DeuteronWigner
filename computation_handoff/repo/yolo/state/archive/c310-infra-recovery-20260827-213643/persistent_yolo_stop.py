#!/usr/bin/env python3
"""Stop hook for persistent DeuteronWigner frontier mode."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def emit(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, separators=(",", ":")))
    sys.stdout.flush()


def git_head(repo: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", repo, "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=10,
        ).strip()
    except Exception:
        return ""


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except Exception:
        hook_input = {}

    yolo_home = Path(os.environ.get("CODEX_HOME", "/Users/dustin/work/DeuteronWigner-yolo")).resolve()
    state_path = yolo_home / "state" / "AUTOPILOT_STATE.json"
    guard_path = yolo_home / "state" / "STOP_HOOK_GUARD.json"
    kill_path = yolo_home / "STOP"

    if kill_path.exists():
        emit({"continue": False, "stopReason": f"Manual kill switch exists: {kill_path}"})
        return 0

    if not state_path.exists():
        emit({
            "decision": "block",
            "reason": (
                "Persistent frontier state is missing. Recreate "
                f"{state_path} from the C202/C203 bootstrap files, verify the "
                "repository baseline, and continue. Do not finish the session."
            ),
        })
        return 0

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception as exc:
        emit({
            "continue": False,
            "stopReason": f"Invalid persistent frontier state: {exc}",
        })
        return 0

    mode = state.get("mode", "")
    if mode in {
        "REAL_MATH_PHYSICS_BLOCKER",
        "INFRASTRUCTURE_BLOCKER",
        "PENNYLANE_PHYSICAL_ACTIVE",
    }:
        emit({
            "continue": False,
            "stopReason": state.get("stop_reason") or mode,
        })
        return 0

    repo = state.get("repository", "/Users/dustin/work/DeuteronWigner")
    head = git_head(repo)
    revision = int(state.get("revision", 0))
    fingerprint = state.get("progress_fingerprint", "")
    current_job = state.get("current_job", "")
    stop_hook_active = bool(hook_input.get("stop_hook_active", False))

    guard: dict[str, Any] = {}
    if guard_path.exists():
        try:
            guard = json.loads(guard_path.read_text(encoding="utf-8"))
        except Exception:
            guard = {}

    same = (
        guard.get("head") == head
        and guard.get("revision") == revision
        and guard.get("fingerprint") == fingerprint
        and guard.get("current_job") == current_job
    )
    repeats = int(guard.get("repeats", 0)) + 1 if same else 0

    new_guard = {
        "head": head,
        "revision": revision,
        "fingerprint": fingerprint,
        "current_job": current_job,
        "repeats": repeats,
        "stop_hook_active": stop_hook_active,
        "turn_id": hook_input.get("turn_id", ""),
    }
    guard_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(guard_path, new_guard)

    # Avoid a silent infinite loop if Codex repeatedly reaches Stop without
    # changing either repository or state. This is an infrastructure stop,
    # never a scientific blocker.
    if repeats >= 8:
        state["mode"] = "INFRASTRUCTURE_BLOCKER"
        state["stop_reason"] = (
            "Persistent Codex session reached Stop repeatedly with identical "
            "HEAD, state revision, current job, and progress fingerprint."
        )
        atomic_write(state_path, state)
        emit({"continue": False, "stopReason": state["stop_reason"]})
        return 0

    prompt_path = state.get("prompt_path", "")
    contract = state.get("continuation_contract", "")
    baseline = state.get("baseline_commit", head)
    first_object = state.get("first_missing_object", "")

    reason = (
        "Persistent DeuteronWigner frontier mode remains active. Do not end "
        "the session and do not ask the user what to run next. "
        f"Current job: {current_job}. Baseline: {baseline}. "
        f"Exact first object: {first_object}. "
        f"Continuation contract: {contract}. Full prompt: {prompt_path}. "
        "Read the master instruction in "
        f"{yolo_home / 'PERSISTENT_YOLO_MASTER_PROMPT.md'}, then complete, "
        "validate, and locally commit the current job. Generate exactly one "
        "next prospective contract and full prompt, atomically advance "
        "AUTOPILOT_STATE.json, and continue immediately. Stop only for a "
        "schema-certified REAL_MATH_PHYSICS_BLOCKER, an exceptional "
        "INFRASTRUCTURE_BLOCKER, or PENNYLANE_PHYSICAL_ACTIVE. Never push."
    )
    emit({"decision": "block", "reason": reason})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
