import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
def test_c13_counts():assert L("c13_requirement_coverage.json")["count"]>=330 and L("c13_injection_manifest.json")["count"]==148
def test_c13_science():assert L("c13_dyson_magnus_manifest.json")["maximum_dyson_magnus"]<1e-13 and L("c13_gauge_closure_report.json")["residual"]==0
def test_c13_isolation():
 r=L("c13_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
