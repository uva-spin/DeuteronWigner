#!/usr/bin/env bash
set -euo pipefail
export YOLO_HOME="/Users/dustin/work/DeuteronWigner-yolo"
export CODEX_HOME="/Users/dustin/work/DeuteronWigner-yolo"
export DEUTERON_WIGNER_REPO="/Users/dustin/work/DeuteronWigner"
cd "/Users/dustin/work/DeuteronWigner"
exec python3 "/Users/dustin/work/DeuteronWigner-yolo/run_phase_from_state.py"
