#!/usr/bin/env bash
set -euo pipefail

YOLO_HOME="${YOLO_HOME:-/Users/dustin/work/DeuteronWigner-yolo}"
REPO="${DEUTERON_WIGNER_REPO:-/Users/dustin/work/DeuteronWigner}"

export YOLO_HOME
export CODEX_HOME="$YOLO_HOME"
export DEUTERON_WIGNER_REPO="$REPO"

cd "$REPO"
exec python3 "$YOLO_HOME/run_forever.py"
