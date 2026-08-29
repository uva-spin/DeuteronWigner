#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
load = lambda name: json.loads((DOCS / name).read_text())

cap = load("c24_source_process_eligibility_matrix.json")
phys = load("c24_physical_input_prerequisite_matrix.json")
src = load("c24_primary_source_manifest.json")
lock = load("c24_source_package_lock_manifest.json")
reg = load("c24_regression_report.json")
inj = load("c24_injection_manifest.json")
req = load("c24_requirement_coverage.json")

assert cap["counts"] == {"analytic": 438, "not_process_eligible": 102, "physical": 0, "source": 0}
assert phys["physical_eligible"] == 0
assert lock["artemide_paper_release"] == "3.01" and not lock["current_release_substituted"]
assert lock["art25_replicas_in_archive"] == 0 and lock["art25_replica_count_declared"] == 500
assert inj["count"] >= 880 and inj["all_detected"]
assert req["count"] == len(req["rows"])
assert reg["production_registry"] == 216 and reg["all_artifacts_unchanged"]
assert reg["analytic_c23_plans_immutable"] and not reg["source_process_executed"]
assert not reg["physical_process_executed"] and not reg["inference_created"] and not reg["production_reachable"]
for row in src["records"]:
    path = ROOT / row["local_path"]
    assert path.is_file(), row["local_path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
for row in cap["rows"]:
    assert not row["source_eligible"] or not row["failed_source_gates"]
    assert not row["physical_eligible"] or (row["source_eligible"] and not row["failed_physical_gates"])
print("C24/P1 source-qualification audit validated (no process tier inflated)")
