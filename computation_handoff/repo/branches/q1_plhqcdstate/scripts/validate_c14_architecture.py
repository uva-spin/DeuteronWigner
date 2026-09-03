#!/usr/bin/env python3
import json
from pathlib import Path

D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(n): return json.loads((D/n).read_text())

req=load("c14_requirement_coverage.json"); inj=load("c14_injection_manifest.json")
reg=load("c14_regression_report.json"); col=load("c14_color_permutation_manifest.json")
sup=load("c14_wilson_support_manifest.json"); pred=load("c14_prediction_plan_manifest.json")
assert req["count"]==len(req["rows"]) and all(x["status"]=="COVERED_H7_SCOPE" for x in req["rows"])
assert inj["count"]>=168 and inj["all_detected"]
assert [x["multiplicity"] for x in col["rows"]]==[22,28,28]
assert all(sup["table"][x]["2"]=="EXPLICIT_FOCK_SUPPORTED" for x in sup["table"])
assert all(sup["table"][x]["3"]=="UNAVAILABLE_AT_THIS_WILSON_ORDER" for x in sup["table"])
assert reg["all_artifacts_unchanged"] and reg["c13_manifests_unchanged"] and reg["production_registry"]==216
assert not pred["production_reachable"] and "FULL_SLAVNOV_TAYLOR_CLOSURE" in pred["not_issued"]
print("C14/H7 architecture manifests validated")
