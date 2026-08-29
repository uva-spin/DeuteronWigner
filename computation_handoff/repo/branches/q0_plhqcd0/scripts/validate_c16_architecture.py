#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
r=load("c16_regression_report.json");q=load("c16_requirement_coverage.json");i=load("c16_injection_manifest.json");s=load("c16_nnpi_state_manifest.json");p=load("c16_deuteron_parent_manifest.json");ready=load("c16_readiness_manifest.json")
assert q["count"]==len(q["rows"]) and all(x["status"]=="COVERED_N1_SCOPE" for x in q["rows"])
assert i["count"]>=280 and i["all_detected"] and len({x["stable_id"] for x in i["rows"]})==i["count"]
assert abs(s["Z_NN"]+s["Z_NNPI"]-1)<1e-13 and len(p["rows"])==15
assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["c15_manifests_unchanged"]
assert not ready["production_reachable"] and "PRODUCTION_READY" in ready["not_issued"]
print("C16/N1 architecture manifests validated")
