#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
r=load("c17_regression_report.json");q=load("c17_requirement_coverage.json");i=load("c17_injection_manifest.json");c=load("c17_continuity_closure_report.json");s=load("c17_separator_trajectory.json");ready=load("c17_readiness_manifest.json");b=load("c17_benchmark_manifest.json")
assert q["count"]==len(q["rows"]) and all(x["status"]=="COVERED_N2_SCOPE" for x in q["rows"])
assert i["count"]>=340 and i["all_detected"] and len({x["stable_id"] for x in i["rows"]})==i["count"]
assert abs(c["residual"])<1e-12 and c["max_block_residual"]<1e-12 and s["matched_variation"]<s["tolerance"]
assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["c16_manifests_unchanged"]
assert not ready["production_reachable"] and "PRODUCTION_READY" in ready["not_issued"]
assert len(b["rows"])==18 and all(x["status"]=="PASS" for x in b["rows"])
print("C17/N2 architecture manifests validated")
