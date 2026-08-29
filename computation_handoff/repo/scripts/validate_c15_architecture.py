#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
r=load("c15_regression_report.json");q=load("c15_requirement_coverage.json");i=load("c15_injection_manifest.json");p=load("c15_deuteron_parent_manifest.json");s=load("c15_spin1_projector_manifest.json");ready=load("c15_readiness_manifest.json")
assert q["count"]==len(q["rows"]) and all(x["status"]=="COVERED_N0_SCOPE" for x in q["rows"])
assert i["count"]>=200 and i["all_detected"] and len({x["stable_id"] for x in i["rows"]})==i["count"]
assert len(p["parents"])==15 and all(x["shape"]==[6,6] for x in p["parents"])
assert s["gram_rank"]==9 and s["reconstruction_residual"]<1e-12
assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["c14_manifests_unchanged"]
assert not ready["production_reachable"] and "PHYSICAL_DEUTERON_GTMD" in ready["not_issued"]
print("C15/N0 architecture manifests validated")
