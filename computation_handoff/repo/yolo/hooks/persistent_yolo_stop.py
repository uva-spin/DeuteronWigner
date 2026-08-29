#!/usr/bin/env python3
"""Transport-aware Stop hook for the persistent DeuteronWigner frontier.

Normal Stop events continue the scientific job. Repeated identical Stop events
request a fresh Codex process instead of directly changing the scientific
controller state to INFRASTRUCTURE_BLOCKER.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


TERMINAL_MODES = {
    "REAL_MATH_PHYSICS_BLOCKER",
    "INFRASTRUCTURE_BLOCKER",
    "PENNYLANE_PHYSICAL_ACTIVE",
}


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
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

    yolo_home = Path(
        os.environ.get("CODEX_HOME", "/Users/dustin/work/DeuteronWigner-yolo")
    ).resolve()
    state_path = yolo_home / "state" / "AUTOPILOT_STATE.json"
    guard_path = yolo_home / "state" / "STOP_HOOK_GUARD.json"
    restart_path = yolo_home / "state" / "RESTART_REQUESTED.json"
    kill_path = yolo_home / "STOP"

    if kill_path.exists():
        emit({
            "continue": False,
            "stopReason": f"Manual kill switch exists: {kill_path}",
        })
        return 0

    if not state_path.exists():
        emit({
            "continue": False,
            "stopReason": f"Persistent frontier state is missing: {state_path}",
        })
        return 0

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception as exc:
        emit({
            "continue": False,
            "stopReason": f"Persistent frontier state is invalid: {exc}",
        })
        return 0

    mode = str(state.get("mode", ""))
    if mode in TERMINAL_MODES:
        emit({
            "continue": False,
            "stopReason": state.get("stop_reason") or mode,
        })
        return 0

    repo = str(state.get(
        "repository",
        "/Users/dustin/work/DeuteronWigner",
    ))
    head = git_head(repo)
    revision = int(state.get("revision", 0))
    fingerprint = str(state.get("progress_fingerprint", ""))
    current_job = str(state.get("current_job", ""))
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

    atomic_write(guard_path, {
        "head": head,
        "revision": revision,
        "fingerprint": fingerprint,
        "current_job": current_job,
        "repeats": repeats,
        "stop_hook_active": stop_hook_active,
        "turn_id": hook_input.get("turn_id", ""),
        "updated_unix": time.time(),
    })

    # A repeated identical Stop sequence is usually a transport/session loop.
    # End only the Codex process and let the outer runner create a fresh session.
    # Do not change the scientific controller mode here.
    if repeats >= 6:
        reason = (
            "Fresh-session restart requested after repeated Stop events with "
            "identical HEAD, state revision, current job, and progress "
            "fingerprint. This is an infrastructure recovery request, not a "
            "scientific blocker."
        )
        atomic_write(restart_path, {
            "schema_version": "1.0",
            "reason": reason,
            "head": head,
            "revision": revision,
            "current_job": current_job,
            "progress_fingerprint": fingerprint,
            "requested_unix": time.time(),
        })
        emit({"continue": False, "stopReason": reason})
        return 0

    prompt_path = str(state.get("prompt_path", ""))
    contract = str(state.get("continuation_contract", ""))
    baseline = str(state.get("baseline_commit", head))
    first_object = str(state.get("first_missing_object", ""))

    emit({
        "decision": "block",
        "reason": (
            "Persistent DeuteronWigner frontier mode remains active. Do not "
            "end the session or ask the user what to run next. "
            f"Current job: {current_job}. Baseline: {baseline}. "
            f"First missing object: {first_object}. "
            f"Continuation contract: {contract}. "
            f"Full job prompt: {prompt_path}. "
            "Read the persistent master instruction and the C310 "
            "infrastructure-recovery launch authority, recover lawful partial "
            "work, complete and validate the current job, create one local "
            "completion commit and exactly one continuation, atomically advance "
            "AUTOPILOT_STATE.json, and continue. Never push."
        ),
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
