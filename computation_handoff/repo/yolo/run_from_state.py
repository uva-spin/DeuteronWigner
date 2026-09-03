#!/usr/bin/env python3
"""Run or resume the persistent DeuteronWigner frontier from external state.

Unlike the original C203 bootstrap runner, this launcher never hard-codes a
scientific package. It reads current_job, baseline_commit, prompt_path, and the
continuation path from AUTOPILOT_STATE.json.
"""

from __future__ import annotations

import fcntl
import json
import os
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
STATE_PATH = YOLO_HOME / "state" / "AUTOPILOT_STATE.json"
SESSION_PATH = YOLO_HOME / "state" / "CODEX_SESSION_ID"
LOCK_PATH = YOLO_HOME / "state" / "RUN.lock"
LOG_DIR = YOLO_HOME / "logs"
MAX_RESTARTS = int(os.environ.get("YOLO_MAX_RESTARTS", "20"))


TERMINAL_MODES = {
    "REAL_MATH_PHYSICS_BLOCKER",
    "INFRASTRUCTURE_BLOCKER",
    "PENNYLANE_PHYSICAL_ACTIVE",
}


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(tmp, path)


def read_state() -> dict[str, Any]:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def is_terminal(state: dict[str, Any]) -> bool:
    return str(state.get("mode", "")) in TERMINAL_MODES


def current_prompt(state: dict[str, Any]) -> str:
    prompt_path = Path(str(state["prompt_path"])).expanduser()
    return (
        "Enter or resume persistent DeuteronWigner frontier mode from the "
        f"external state file {STATE_PATH}. Read {YOLO_HOME / 'AGENTS.override.md'} "
        f"and {YOLO_HOME / 'PERSISTENT_YOLO_MASTER_PROMPT.md'} completely. "
        f"Then read the current full launch/job prompt at {prompt_path} completely. "
        f"Current job: {state['current_job']}. "
        f"Exact baseline: {state['baseline_commit']}. "
        f"First missing object: {state['first_missing_object']}. "
        f"Expected continuation authority: {state['continuation_contract']}. "
        "Recover any already-created valid commit deterministically and never "
        "duplicate a completed job. Complete, validate, and locally commit the "
        "current job; create exactly one next prospective contract and prompt; "
        "atomically update AUTOPILOT_STATE.json; and continue without asking the "
        "user what to run next. The C258 REAL_BLOCKER.json remains historical "
        "evidence and does not override the newly human-authorized CONTINUE state. "
        "Never push. Stop only for a newly schema-certified real math/physics "
        "blocker, an exceptional infrastructure blocker, or "
        "PENNYLANE_PHYSICAL_ACTIVE."
    )


def resume_prompt(state: dict[str, Any]) -> str:
    return (
        "Resume the persistent DeuteronWigner frontier from "
        f"{STATE_PATH}. Read the current state, global AGENTS override, master "
        "prompt, and current prompt_path. Recover any commit or partial job "
        "deterministically. Continue from current_job "
        f"{state['current_job']} at baseline {state['baseline_commit']} until a "
        "certified terminal mode. Never push."
    )


def run_and_log(
    command: list[str],
    log_path: Path,
    *,
    capture_thread_id: bool,
) -> int:
    with log_path.open("a", encoding="utf-8") as log:
        process = subprocess.Popen(
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
        assert process.stdout is not None
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            log.write(line)
            log.flush()
            if capture_thread_id:
                try:
                    event = json.loads(line)
                except Exception:
                    event = {}
                if (
                    event.get("type") == "thread.started"
                    and event.get("thread_id")
                ):
                    SESSION_PATH.write_text(
                        str(event["thread_id"]) + "\n",
                        encoding="utf-8",
                    )
        return process.wait()


def set_infrastructure_blocker(reason: str) -> None:
    state = read_state()
    state["mode"] = "INFRASTRUCTURE_BLOCKER"
    state["stop_reason"] = reason
    atomic_write_json(STATE_PATH, state)


def main() -> int:
    if not STATE_PATH.exists():
        print(f"Missing state file: {STATE_PATH}", file=sys.stderr)
        return 2
    if not REPO.is_dir():
        print(f"Missing repository: {REPO}", file=sys.stderr)
        return 2

    YOLO_HOME.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOCK_PATH.open("w", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another persistent frontier runner owns the lock.", file=sys.stderr)
            return 2

        restart_count = 0
        while restart_count <= MAX_RESTARTS:
            if (YOLO_HOME / "STOP").exists():
                print(
                    f"Manual STOP file exists: {YOLO_HOME / 'STOP'}",
                    file=sys.stderr,
                )
                return 0

            state = read_state()
            if is_terminal(state):
                print(f"Terminal mode: {state['mode']}")
                print(state.get("stop_reason", ""))
                return 0 if state["mode"] == "PENNYLANE_PHYSICAL_ACTIVE" else 3

            session_id = (
                SESSION_PATH.read_text(encoding="utf-8").strip()
                if SESSION_PATH.exists()
                else ""
            )
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            log_path = LOG_DIR / f"codex-recovery-{timestamp}.jsonl"

            if session_id:
                command = [
                    "codex",
                    "--dangerously-bypass-hook-trust",
                    "exec",
                    "--json",
                    "resume",
                    session_id,
                    resume_prompt(state),
                ]
                capture_thread_id = False
            else:
                command = [
                    "codex",
                    "--dangerously-bypass-hook-trust",
                    "exec",
                    "--json",
                    current_prompt(state),
                ]
                capture_thread_id = True

            exit_code = run_and_log(
                command,
                log_path,
                capture_thread_id=capture_thread_id,
            )

            state = read_state()
            if is_terminal(state):
                return 0 if state["mode"] == "PENNYLANE_PHYSICAL_ACTIVE" else 3

            restart_count += 1
            if restart_count > MAX_RESTARTS:
                set_infrastructure_blocker(
                    "The Codex process exited repeatedly while the persistent "
                    "state remained nonterminal."
                )
                return 4

            print(
                f"Codex exited with code {exit_code}; state remains "
                f"{state.get('mode')}. Resuming in a few seconds.",
                file=sys.stderr,
            )
            time.sleep(min(5 * restart_count, 30))

    return 4


if __name__ == "__main__":
    raise SystemExit(main())
