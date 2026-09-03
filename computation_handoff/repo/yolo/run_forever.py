#!/usr/bin/env python3
"""Launch or resume one persistent Codex frontier session."""

from __future__ import annotations

import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path


YOLO_HOME = Path(os.environ.get("YOLO_HOME", "/Users/dustin/work/DeuteronWigner-yolo")).resolve()
REPO = Path(os.environ.get("DEUTERON_WIGNER_REPO", "/Users/dustin/work/DeuteronWigner")).resolve()
STATE_PATH = YOLO_HOME / "state" / "AUTOPILOT_STATE.json"
SESSION_PATH = YOLO_HOME / "state" / "CODEX_SESSION_ID"
LOCK_PATH = YOLO_HOME / "state" / "RUN.lock"
LOG_DIR = YOLO_HOME / "logs"
MAX_RESTARTS = int(os.environ.get("YOLO_MAX_RESTARTS", "20"))


def read_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def terminal(state: dict) -> bool:
    return state.get("mode") in {
        "REAL_MATH_PHYSICS_BLOCKER",
        "INFRASTRUCTURE_BLOCKER",
        "PENNYLANE_PHYSICAL_ACTIVE",
    }


def run_and_log(command: list[str], log_path: Path, parse_thread: bool) -> int:
    with log_path.open("a", encoding="utf-8") as log:
        process = subprocess.Popen(
            command,
            cwd=REPO,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            env={**os.environ, "CODEX_HOME": str(YOLO_HOME)},
        )
        assert process.stdout is not None
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            log.write(line)
            log.flush()
            if parse_thread:
                try:
                    event = json.loads(line)
                    if event.get("type") == "thread.started" and event.get("thread_id"):
                        SESSION_PATH.write_text(event["thread_id"] + "\n", encoding="utf-8")
                except Exception:
                    pass
        return process.wait()


def main() -> int:
    YOLO_HOME.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOCK_PATH.open("w", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another persistent frontier runner owns the lock.", file=sys.stderr)
            return 2

        restart = 0
        while restart <= MAX_RESTARTS:
            if (YOLO_HOME / "STOP").exists():
                print("Manual STOP file detected.")
                return 0

            state = read_state()
            if terminal(state):
                print(f"Persistent frontier terminal mode: {state['mode']}")
                print(state.get("stop_reason", ""))
                return 0 if state["mode"] == "PENNYLANE_PHYSICAL_ACTIVE" else 3

            session_id = SESSION_PATH.read_text(encoding="utf-8").strip() if SESSION_PATH.exists() else ""
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            log_path = LOG_DIR / f"codex-{timestamp}.jsonl"

            if session_id:
                resume_prompt = (
                    "Resume the persistent DeuteronWigner frontier from the "
                    "external AUTOPILOT_STATE.json. Read the global AGENTS "
                    "instruction and master prompt. Recover any commit or "
                    "partially completed job deterministically. Continue until "
                    "a certified terminal mode. Never push."
                )
                command = [
                    "codex",
                    "--dangerously-bypass-hook-trust",
                    "exec",
                    "--json",
                    "resume",
                    session_id,
                    resume_prompt,
                ]
                parse_thread = False
            else:
                initial_prompt = (
                    "Enter persistent DeuteronWigner frontier mode. Read "
                    f"{YOLO_HOME / 'PERSISTENT_YOLO_MASTER_PROMPT.md'} and "
                    f"{YOLO_HOME / 'prompts' / 'c203_hqcdbrst1_codex_prompt.md'} "
                    "completely. Start C203/HQCDBRST1 from the exact C202 "
                    "baseline. Continue autonomously across all later jobs "
                    "until PENNYLANE_PHYSICAL_ACTIVE or a certified blocker. "
                    "Never push."
                )
                command = [
                    "codex",
                    "--dangerously-bypass-hook-trust",
                    "exec",
                    "--json",
                    initial_prompt,
                ]
                parse_thread = True

            exit_code = run_and_log(command, log_path, parse_thread)
            state = read_state()
            if terminal(state):
                return 0 if state["mode"] == "PENNYLANE_PHYSICAL_ACTIVE" else 3

            restart += 1
            if restart > MAX_RESTARTS:
                state["mode"] = "INFRASTRUCTURE_BLOCKER"
                state["stop_reason"] = (
                    f"Codex process exited {MAX_RESTARTS + 1} times while "
                    "persistent state remained CONTINUE."
                )
                tmp = STATE_PATH.with_suffix(".tmp")
                tmp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
                os.replace(tmp, STATE_PATH)
                return 4

            print(
                f"Codex exited with code {exit_code}; persistent state is "
                f"{state.get('mode')}. Resuming after a short delay.",
                file=sys.stderr,
            )
            time.sleep(min(5 * restart, 30))

    return 4


if __name__ == "__main__":
    raise SystemExit(main())
