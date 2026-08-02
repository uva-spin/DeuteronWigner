#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"
load = lambda name: json.loads((D / name).read_text())
cap = load("c22q_capability_reconciliation.json")
proc = load("c22q_process_eligibility_matrix.json")
contract = load("c23_p0_prerequisite_contract.json")
reg = load("c22q_regression_report.json")
assert len(cap["rows"]) == 540
assert cap["qualification_tier_counts"] == {"M3_UNAVAILABLE": 102, "M3_VALIDATION_QUALIFIED": 438}
assert proc["counts"] == {"ANALYTIC_PROCESS_ORACLE_ELIGIBLE": 438, "NOT_PROCESS_ELIGIBLE": 102}
assert contract["analytic_plan_nonempty"] and not contract["source_plan_nonempty"] and not contract["physical_plan_nonempty"]
assert hashlib.sha256((D / "c23_p0_codex_prompt.md").read_bytes()).hexdigest() == contract["original_prompt_sha256"]
assert reg["production_registry"] == 216 and not reg["process_executed"] and not reg["production_reachable"]
print("C22Q/M3Q architecture manifests validated")
