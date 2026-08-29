#!/usr/bin/env python3
"""State-driven, fresh-session-capable persistent Codex runner.

The runner resumes a healthy session when progress has occurred. When a
transport/session loop is detected, it archives that session and starts a new
one without changing the scientific baseline or revision.
"""

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
STATE_PATH = YOLO_HOME / "state" / "AUTOPILOT_STATE.json"
SESSION_PATH = YOLO_HOME / "state" / "CODEX_SESSION_ID"
GUARD_PATH = YOLO_HOME / "state" / "STOP_HOOK_GUARD.json"
RESTART_REQUEST_PATH = YOLO_HOME / "state" / "RESTART_REQUESTED.json"
RESTART_STATE_PATH = YOLO_HOME / "state" / "SESSION_RESTART_STATE.json"
LOCK_PATH = YOLO_HOME / "state" / "RUN.lock"
LOG_DIR = YOLO_HOME / "logs"
ARCHIVE_DIR = YOLO_HOME / "state" / "archive"
RECOVERY_LAUNCH = YOLO_HOME / "prompts" / "c310_infrastructure_recovery_launch.md"

MAX_STAGNANT_SESSIONS = int(
    os.environ.get("YOLO_MAX_STAGNANT_SESSIONS", "8")
)
MAX_TRANSPORT_ERRORS_PER_PROCESS = int(
    os.environ.get("YOLO_MAX_TRANSPORT_ERRORS_PER_PROCESS", "4")
)

TERMINAL_MODES = {
    "REAL_MATH_PHYSICS_BLOCKER",
    "INFRASTRUCTURE_BLOCKER",
    "PENNYLANE_PHYSICAL_ACTIVE",
}

TRANSPORT_PATTERNS = (
    "wss://chatgpt.com/backend-api/codex/responses",
    "websocket",
    "connection reset",
    "connection refused",
    "failed to refresh",
    "model refresh",
    "model-refresh",
    "network error",
    "timed out",
    "timeout",
    "temporary failure",
)


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(tmp, path)


def read_json(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if not path.exists():
        return {} if default is None else dict(default)
    return json.loads(path.read_text(encoding="utf-8"))


def read_state() -> dict[str, Any]:
    return read_json(STATE_PATH)


def terminal(state: dict[str, Any]) -> bool:
    return str(state.get("mode", "")) in TERMINAL_MODES


def git_head() -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "HEAD"],
        text=True,
        timeout=20,
    ).strip()


def snapshot(state: dict[str, Any]) -> tuple[str, int, str, str]:
    return (
        git_head(),
        int(state.get("revision", 0)),
        str(state.get("progress_fingerprint", "")),
        str(state.get("current_job", "")),
    )


def archive_path(path: Path, label: str) -> None:
    if not path.exists():
        return
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    target = ARCHIVE_DIR / f"{timestamp}-{label}-{path.name}"
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(target))


def fresh_session() -> None:
    archive_path(SESSION_PATH, "session")
    archive_path(GUARD_PATH, "guard")
    archive_path(RESTART_REQUEST_PATH, "request")


def set_infrastructure_blocker(reason: str) -> None:
    state = read_state()
    state["mode"] = "INFRASTRUCTURE_BLOCKER"
    state["stop_reason"] = reason
    atomic_write_json(STATE_PATH, state)


def initial_prompt(state: dict[str, Any]) -> str:
    prompt_path = str(state.get("prompt_path", ""))
    recovery_text = (
        f" Read {RECOVERY_LAUNCH} completely before touching the worktree."
        if RECOVERY_LAUNCH.exists()
        else ""
    )
    return (
        "Enter persistent DeuteronWigner frontier mode from the external "
        f"state file {STATE_PATH}.{recovery_text} "
        f"Read {YOLO_HOME / 'AGENTS.override.md'} and "
        f"{YOLO_HOME / 'PERSISTENT_YOLO_MASTER_PROMPT.md'} completely. "
        f"Then read the current full job prompt at {prompt_path}. "
        f"Current job: {state.get('current_job')}. "
        f"Exact baseline: {state.get('baseline_commit')}. "
        f"First missing object: {state.get('first_missing_object')}. "
        f"Continuation contract: {state.get('continuation_contract')}. "
        "This is infrastructure recovery: inspect and preserve all partial "
        "current-job work, never reset or clean it blindly, and never create a "
        "duplicate completion commit. Complete, validate, and locally commit "
        "the current job; create exactly one next contract and prompt; "
        "atomically advance state; and continue. Never push."
    )


def resume_prompt(state: dict[str, Any]) -> str:
    return (
        "Resume the persistent DeuteronWigner frontier from "
        f"{STATE_PATH}. Re-read the current state, persistent master prompt, "
        f"current prompt_path {state.get('prompt_path')}, and continuation "
        f"{state.get('continuation_contract')}. Recover partial work "
        "deterministically, continue the current job, then advance the exact "
        "frontier. Never push."
    )


def event_text(event: dict[str, Any]) -> str:
    try:
        return json.dumps(event, sort_keys=True).lower()
    except Exception:
        return str(event).lower()


def run_codex(
    command: list[str],
    log_path: Path,
    capture_thread: bool,
) -> tuple[int, int]:
    transport_errors = 0
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

            try:
                event = json.loads(line)
            except Exception:
                event = {}

            if capture_thread and (
                event.get("type") == "thread.started"
                and event.get("thread_id")
            ):
                SESSION_PATH.write_text(
                    str(event["thread_id"]) + "\n",
                    encoding="utf-8",
                )

            if event.get("type") in {"error", "turn.failed"}:
                text = event_text(event)
                if any(pattern in text for pattern in TRANSPORT_PATTERNS):
                    transport_errors += 1

            if (
                transport_errors >= MAX_TRANSPORT_ERRORS_PER_PROCESS
                and process.poll() is None
            ):
                log.write(
                    json.dumps({
                        "runner": "terminating_transport_loop",
                        "transport_errors": transport_errors,
                    }) + "\n"
                )
                log.flush()
                process.terminate()
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    process.kill()
                break

        return process.wait(), transport_errors


def main() -> int:
    if not STATE_PATH.exists():
        print(f"Missing state file: {STATE_PATH}", file=sys.stderr)
        return 2
    if not (REPO / ".git").exists():
        print(f"Missing Git repository: {REPO}", file=sys.stderr)
        return 2

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOCK_PATH.open("w", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another persistent frontier runner owns RUN.lock.", file=sys.stderr)
            return 2

        restart_state = read_json(
            RESTART_STATE_PATH,
            {"consecutive_stagnant_sessions": 0},
        )

        while True:
            if (YOLO_HOME / "STOP").exists():
                print(f"Manual STOP file exists: {YOLO_HOME / 'STOP'}")
                return 0

            state = read_state()
            if terminal(state):
                print(f"Terminal controller mode: {state.get('mode')}")
                print(state.get("stop_reason", ""))
                return (
                    0
                    if state.get("mode") == "PENNYLANE_PHYSICAL_ACTIVE"
                    else 3
                )

            before = snapshot(state)
            session_id = (
                SESSION_PATH.read_text(encoding="utf-8").strip()
                if SESSION_PATH.exists()
                else ""
            )
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            log_path = LOG_DIR / f"codex-c310-recovery-{timestamp}.jsonl"

            common = [
                "codex",
                "--dangerously-bypass-hook-trust",
                "exec",
                "--json",
                "--sandbox",
                "danger-full-access",
            ]

            if session_id:
                command = common + [
                    "resume",
                    session_id,
                    resume_prompt(state),
                ]
                capture_thread = False
            else:
                command = common + [initial_prompt(state)]
                capture_thread = True

            exit_code, transport_errors = run_codex(
                command,
                log_path,
                capture_thread,
            )

            state_after = read_state()
            if terminal(state_after):
                return (
                    0
                    if state_after.get("mode") == "PENNYLANE_PHYSICAL_ACTIVE"
                    else 3
                )

            after = snapshot(state_after)
            requested_restart = RESTART_REQUEST_PATH.exists()
            progressed = after != before

            if progressed:
                restart_state["consecutive_stagnant_sessions"] = 0
                restart_state["last_progress_snapshot"] = list(after)
                restart_state["last_progress_unix"] = time.time()
                atomic_write_json(RESTART_STATE_PATH, restart_state)
                # A session may continue or resume after scientific progress.
                time.sleep(2)
                continue

            # No scientific/state progress: discard only the transport session,
            # never the scientific worktree.
            fresh_session()
            count = int(
                restart_state.get("consecutive_stagnant_sessions", 0)
            ) + 1
            restart_state.update({
                "consecutive_stagnant_sessions": count,
                "last_exit_code": exit_code,
                "last_transport_error_count": transport_errors,
                "last_restart_requested": requested_restart,
                "last_stagnant_snapshot": list(after),
                "last_stagnant_unix": time.time(),
            })
            atomic_write_json(RESTART_STATE_PATH, restart_state)

            if count > MAX_STAGNANT_SESSIONS:
                reason = (
                    "Fresh Codex sessions repeatedly exited without changing "
                    "HEAD, state revision, progress fingerprint, or current "
                    f"job after {count} attempts. Latest exit code: "
                    f"{exit_code}; transport-error events: {transport_errors}."
                )
                set_infrastructure_blocker(reason)
                return 4

            delay = min(10 * (2 ** (count - 1)), 300)
            print(
                "No scientific progress was recorded; starting a fresh Codex "
                f"session after {delay} seconds "
                f"(stagnant session {count}/{MAX_STAGNANT_SESSIONS}).",
                file=sys.stderr,
            )
            time.sleep(delay)


if __name__ == "__main__":
    raise SystemExit(main())
