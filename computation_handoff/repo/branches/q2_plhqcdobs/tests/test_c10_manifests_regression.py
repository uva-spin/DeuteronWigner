import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def l(n):return json.loads((D/n).read_text())
def test_counts():assert l("c10_requirement_coverage.json")["count"]==210 and l("c10_injection_manifest.json")["count"]==90
def test_closure():assert l("c10_tolerance_manifest.json")["all_pass"] and l("c10_pcac_closure_report.json")["maximum_residual"]==0
def test_parents_and_wilson():
 assert all(all(r["positive_x_direct"] for r in p["rows"]) for p in l("c10_common_parent_manifest.json")["plans"])
 assert all(r["absorption"]==0 and not r["WILSON_READY"] for r in l("c10_antiquark_wilson_handoff.json")["rows"])
def test_regression():r=l("c10_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
