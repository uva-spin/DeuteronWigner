#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
export PYTHONPATH="${ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
THREADS="${C400_NUM_THREADS:-1}"
export OMP_NUM_THREADS="$THREADS"
export OPENBLAS_NUM_THREADS="$THREADS"
export MKL_NUM_THREADS="$THREADS"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/c400_s2_generate.XXXXXX")"
cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

"$PYTHON_BIN" "$ROOT/tools/generate_c400_s2_corrective.py" \
  --derivative-worker "$TMP/derivatives.json"
"$PYTHON_BIN" "$ROOT/tools/generate_c400_s2_corrective.py" \
  --numerical-worker "$TMP/numerical.json" \
  --derivative-input "$TMP/derivatives.json"
"$PYTHON_BIN" "$ROOT/tools/generate_c400_s2_corrective.py" \
  --assemble \
  --derivative-input "$TMP/derivatives.json" \
  --numerical-input "$TMP/numerical.json"
