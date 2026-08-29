#!/usr/bin/env python3
"""State-driven persistent runner for classical phase-package mode."""

from __future__ import annotations

import fcntl
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


YOLO_HOME = Path(
    os.environ.get("YOLO_HOME", "/Users/dustin/work/DeuteronWigner-yolo")
).resolve()
REPO = Path(
    os.environ.get("DEUTERON_WIGNER_REPO", "/Users/dustin/work/DeuteronWigner")
).resolve()
STATE = YOLO_HOME / "state" / "AUTOPILOT_STATE.json"
SESSION = YOLO_HOME / "state" / "CODEX_SESSION_ID"
LOCK = YOLO_HOME / "state" / "RUN.lock"
LOGS = YOLO_HOME / "logs"
ARCHIVE = YOLO_HOME / "state" / "archive"
MAX_STAGNANT = int(os.environ.get("YOLO_MAX_STAGNANT_PHASE_SESSIONS", "8"))

TERMINAL = {
    "REAL_MATH_PHYSICS_BLOCKER",
    "INFRASTRUCTURE_BLOCKER",
    "PENNYLANE_PHYSICAL_ACTIVE",
}


def read_state() -> dict[str, Any]:
    return json.loads(STATE.read_text(encoding="utf-8"))


def atomic_write(payload: dict[str, Any]) -> None:
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(tmp, STATE)


def head() -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "HEAD"],
        text=True,
        timeout=20,
    ).strip()


def snapshot(state: dict[str, Any]) -> tuple[str, int, str, str]:
    return (
        head(),
        int(state.get("revision", 0)),
        str(state.get("progress_fingerprint", "")),
        str(state.get("current_job", "")),
    )


def archive_session() -> None:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for path in [
        SESSION,
        YOLO_HOME / "state" / "STOP_HOOK_GUARD.json",
        YOLO_HOME / "state" / "RESTART_REQUESTED.json",
    ]:
        if path.exists():
            shutil.move(
                str(path),
                str(ARCHIVE / f"{timestamp}-phase-{path.name}"),
            )


def prompt(state: dict[str, Any], resumed: bool) -> str:
    verb = "Resume" if resumed else "Enter"
    return (
        f"{verb} persistent classical phase-package mode from {STATE}. "
        f"Read {YOLO_HOME / 'AGENTS.override.md'}, "
        f"{YOLO_HOME / 'PERSISTENT_YOLO_MASTER_PROMPT.md'}, "
        f"{YOLO_HOME / 'policy' / 'CLASSICAL_PHASE_PACKAGE_POLICY.md'}, "
        f"and the current prompt {state.get('prompt_path')} completely. "
        f"Current phase: {state.get('current_job')}. "
        f"Baseline: {state.get('baseline_commit')}. "
        f"First object: {state.get('first_missing_object')}. "
        "Recover partial stage work deterministically. Do not split internal "
        "stages into top-level C packages. Complete one accepted phase commit, "
        "one next phase contract, atomically advance state, and continue until "
        "the physical PennyLane handoff or a certified blocker. Never push."
    )


def run(command: list[str], log_path: Path, capture: bool) -> int:
    with log_path.open("a", encoding="utf-8") as log:
        proc = subprocess.Popen(
            command,
            cwd=REPO,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            env={
                **os.environ,
                "YOLO_HOME": str(YOLO_HOME),
                "CODEX_HOME": str(YOLO_HOME),
                "DEUTERON_WIGNER_REPO": str(REPO),
            },
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            log.write(line)
            log.flush()
            if capture:
                try:
                    event = json.loads(line)
                except Exception:
                    event = {}
                if (
                    event.get("type") == "thread.started"
                    and event.get("thread_id")
                ):
                    SESSION.write_text(
                        str(event["thread_id"]) + "\n",
                        encoding="utf-8",
                    )
        return proc.wait()


def main() -> int:
    if not STATE.exists() or not (REPO / ".git").exists():
        print("Missing controller state or scientific repository.", file=sys.stderr)
        return 2

    LOGS.mkdir(parents=True, exist_ok=True)
    LOCK.parent.mkdir(parents=True, exist_ok=True)

    with LOCK.open("w", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another persistent runner owns RUN.lock.", file=sys.stderr)
            return 2

        stagnant = 0
        while True:
            if (YOLO_HOME / "STOP").exists():
                print("Manual STOP file detected.")
                return 0

            state = read_state()
            mode = str(state.get("mode", ""))
            if mode in TERMINAL:
                print(f"Terminal mode: {mode}")
                print(state.get("stop_reason", ""))
                return 0 if mode == "PENNYLANE_PHYSICAL_ACTIVE" else 3

            before = snapshot(state)
            session_id = (
                SESSION.read_text(encoding="utf-8").strip()
                if SESSION.exists()
                else ""
            )
            stamp = time.strftime("%Y%m%d-%H%M%S")
            log_path = LOGS / f"codex-phase-{stamp}.jsonl"

            common = [
                "codex",
                "--dangerously-bypass-hook-trust",
                "exec",
                "--json",
                "--sandbox",
                "danger-full-access",
            ]
            if session_id:
                command = common + ["resume", session_id, prompt(state, True)]
                capture = False
            else:
                command = common + [prompt(state, False)]
                capture = True

            exit_code = run(command, log_path, capture)
            after_state = read_state()
            after = snapshot(after_state)

            if str(after_state.get("mode", "")) in TERMINAL:
                return (
                    0
                    if after_state.get("mode") == "PENNYLANE_PHYSICAL_ACTIVE"
                    else 3
                )

            if after != before:
                stagnant = 0
                time.sleep(2)
                continue

            stagnant += 1
            archive_session()
            if stagnant > MAX_STAGNANT:
                after_state["mode"] = "INFRASTRUCTURE_BLOCKER"
                after_state["stop_reason"] = (
                    "Repeated fresh phase-mode Codex sessions exited without "
                    "changing HEAD, revision, fingerprint, or current phase."
                )
                atomic_write(after_state)
                return 4

            delay = min(10 * (2 ** (stagnant - 1)), 300)
            print(
                f"Codex exited {exit_code} without recorded phase progress; "
                f"starting a fresh session in {delay}s.",
                file=sys.stderr,
            )
            time.sleep(delay)


if __name__ == "__main__":
    raise SystemExit(main())
