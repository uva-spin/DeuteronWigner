#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
YOLO_HOME="${YOLO_HOME:-/Users/dustin/work/DeuteronWigner-yolo}"
REPO="${DEUTERON_WIGNER_REPO:-/Users/dustin/work/DeuteronWigner}"

mkdir -p "$YOLO_HOME"
rsync -a --delete \
  --exclude 'state/CODEX_SESSION_ID' \
  --exclude 'state/STOP_HOOK_GUARD.json' \
  --exclude 'logs/' \
  "$SOURCE_DIR/" "$YOLO_HOME/"

python3 - "$YOLO_HOME" "$REPO" <<'PY'
from pathlib import Path
import json, os, sys, hashlib

home = Path(sys.argv[1]).resolve()
repo = Path(sys.argv[2]).resolve()

for rel in [
    "AGENTS.override.md",
    "hooks.json",
    "PERSISTENT_YOLO_MASTER_PROMPT.md",
    "hooks/persistent_yolo_stop.py",
    "run_forever.py",
    "state/AUTOPILOT_STATE.json",
]:
    path = home / rel
    text = path.read_text(encoding="utf-8")
    text = text.replace("__YOLO_HOME__", str(home))
    text = text.replace("/Users/dustin/work/DeuteronWigner", str(repo))
    path.write_text(text, encoding="utf-8")

state_path = home / "state" / "AUTOPILOT_STATE.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
state["repository"] = str(repo)
state["prompt_path"] = str(home / "prompts" / "c203_hqcdbrst1_codex_prompt.md")
contract_path = repo / state["continuation_contract"]
if contract_path.exists():
    state["continuation_contract_sha256"] = hashlib.sha256(contract_path.read_bytes()).hexdigest()
state["progress_fingerprint"] = hashlib.sha256(
    (
        state["current_job"] + "\n" +
        state["baseline_commit"] + "\n" +
        state["first_missing_object"] + "\n" +
        state["continuation_contract_sha256"]
    ).encode()
).hexdigest()
tmp = state_path.with_suffix(".tmp")
tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
os.replace(tmp, state_path)
PY

chmod +x "$YOLO_HOME/hooks/persistent_yolo_stop.py"
chmod +x "$YOLO_HOME/run_forever.py"
chmod +x "$YOLO_HOME/run_persistent_yolo.sh"

# Reuse the existing trusted Codex login without copying credential contents.
if [[ ! -e "$YOLO_HOME/auth.json" && -f "$HOME/.codex/auth.json" ]]; then
  ln -s "$HOME/.codex/auth.json" "$YOLO_HOME/auth.json"
fi

echo "Installed persistent YOLO controller at: $YOLO_HOME"
echo "Scientific repository: $REPO"
echo
echo "Review the files, then launch with:"
echo "  $YOLO_HOME/run_persistent_yolo.sh"
