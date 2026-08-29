#!/usr/bin/env python3
"""Validate deterministic C25 artifacts and fail-closed qualification."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def main() -> None:
    required = [
        "c25_art25_member_validation.json", "c25_art25_parameter_reproduction.json",
        "c25_artemide_v301_build_manifest.json", "c25_v301_payload_compatibility.json",
        "c25_source_gate_report.json", "c25_injection_manifest.json", "c25_regression_report.json",
    ]
    rows = {n: json.loads((DOCS / n).read_text()) for n in required}
    assert rows[required[0]]["parsed_stochastic"] == 642
    assert rows[required[2]]["source_patched"] is False
    assert rows[required[3]]["all_nine_model_files_byte_identical"] is True
    assert rows[required[4]]["source_process_eligible"] == rows[required[4]]["physical_input_eligible"] == 0
    assert rows[required[5]]["count"] >= 960 and rows[required[5]]["all_detected"]
    assert rows[required[6]]["production_registry"] == 216 and rows[required[6]]["all_artifacts_unchanged"]
    print("C25/P1A validation: PASS")


if __name__ == "__main__":
    main()
