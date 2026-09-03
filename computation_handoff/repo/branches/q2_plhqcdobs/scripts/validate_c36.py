#!/usr/bin/env python3
"""Independent validator for the C36/O4 replacement-root package."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess

from deuteron_wigner.bridge import o4
from deuteron_wigner.bridge.s0c import core as c35
import build_c36_manifests as builder


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"


def load(name: str) -> dict:
    return json.loads((DOCS / name).read_text())


def canonical_hash(value: dict) -> str:
    value = dict(value); expected = value.pop("content_hash")
    actual = sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()).hexdigest()
    assert actual == expected
    return actual


def validate() -> None:
    assert subprocess.run(("git", "merge-base", "--is-ancestor", o4.C36_BASELINE_COMMIT, "HEAD"), cwd=ROOT).returncode == 0
    assert c35.C35_PRIMARY_NO_GO == o4.C35_PRIMARY_NO_GO
    assert c35.C35_SECONDARY_MODE_NO_GO == o4.C35_SECONDARY_NO_GO
    c35_ward = json.loads((DOCS / "c35_vertex_ward_report.json").read_text())
    assert abs(c35_ward["analytic_single_segment_gauge_defect_abs"] - o4.C35_FINITE_DELTA_WARD_DEFECT) < 1e-7
    for name in builder.JSON_DELIVERABLES:
        canonical_hash(load(name))
    selection = load("c36_regulator_plan_selection.json")
    assert selection["selected"] == o4.C36_SELECTED_PLAN
    manifest = load("c36_regulator_plan_manifest.json")
    assert sum(row["selected"] for row in manifest["plans"]) == 1
    assert not manifest["plans_summed"]
    roots = load("c36_joint_root_identity.json")
    assert roots["collinear_root"]["baryon_number"] == 1
    assert roots["soft_root"]["baryon_number"] == 0
    assert not roots["shared_state_vector"] and not roots["soft_root"]["hadron_probability_tensor_member"]
    gauge = load("c36_finite_regulator_gauge_report.json")["report"]
    assert gauge["ward_residual"] == 0.0 and gauge["inherited_c35_ward_defect"] == o4.C35_FINITE_DELTA_WARD_DEFECT
    tree = load("c36_c11_tree_reduction_report.json")
    assert len(tree["rows"]) == 12 and tree["tree"]["maximum_residual"] == 0.0
    assert {row["flavor"] for row in tree["rows"]} == {"u", "d", "ubar", "dbar"}
    assert not tree["one_loop_matching"]
    conversion = load("c36_selected_to_project_conversion.json")
    assert conversion["conversion"]["direct_to_c11_forbidden"] and conversion["art25_inputs_used"] is False
    assert load("c36_conversion_roundtrip_report.json")["round_trip_residual"] == 0.0
    assert load("c36_injection_manifest.json")["count"] >= 2640
    gate = load("c36_continuation_gate.json")["gate"]
    assert gate["status"] == "C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY"
    assert not any(gate[key] for key in ("proton_tmd_exported", "bridge_rerun", "production_reachable", "finite_basis_one_loop_complete"))
    report = load("c36_regression_report.json")
    assert report["production_route_count"] == 216 and report["authoritative_artifact_count"] == 8 and report["ART25_identity_count"] == 642


if __name__ == "__main__":
    validate()
    print("C36_VALIDATION_PASS")
