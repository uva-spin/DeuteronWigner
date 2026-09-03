"""Byte-level C1 guard for the eight immutable numerical parents."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_c1_all_eight_authoritative_artifacts_are_byte_identical():
    baseline = json.loads(
        (ROOT / "docs/next_level/stage0_regression_baseline.json").read_text()
    )
    for record in baseline["authoritative_artifacts"][:8]:
        digest = hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest()
        assert digest == record["sha256"], record["id"]


def test_c1_manifests_are_deterministic_and_complete():
    for name in (
        "c1_requirement_coverage.json",
        "c1_operator_identity_completeness.json",
        "c1_adapter_manifest.json",
        "c1_regression_report.json",
    ):
        value = json.loads((ROOT / "docs/next_level" / name).read_text())
        assert value["schema_version"] == "1.0.0"
    regression = json.loads(
        (ROOT / "docs/next_level/c1_regression_report.json").read_text()
    )
    assert regression["all_byte_identical"]
    assert len(regression["artifacts"]) == 8
