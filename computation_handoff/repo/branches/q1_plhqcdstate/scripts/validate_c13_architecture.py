#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
assert [x["multiplicity"] for x in L("c13_color_multiplicity_manifest.json")["rows"]]==[6,8,8]
assert L("c13_dyson_magnus_manifest.json")["maximum_dyson_magnus"]<1e-13
assert L("c13_second_order_soft_manifest.json")["central"]["rapidity_residual"]==0
assert L("c13_gauge_closure_report.json")["residual"]==0
assert L("c13_injection_manifest.json")["count"]>=144
r=L("c13_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
print("C13/H6 architecture manifests validated")
