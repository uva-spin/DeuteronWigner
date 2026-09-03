#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs/next_level";L=lambda n:json.loads((D/n).read_text())
r=L("c19_regression_report.json");q=L("c19_requirement_coverage.json");i=L("c19_injection_manifest.json");s=L("c19_scheme_manifest.json");e=L("c19_two_scale_evolution_report.json");a=L("c19_accuracy_manifest.json")
assert q["count"]==len(q["rows"]);assert i["count"]==480 and i["all_detected"];assert s["roundtrip_residual"]<1e-12;assert e["integrable_path_residual"]<1e-12 and e["finite_order_curl"]>0;assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not a["production_reachable"]
print("C19/M0 architecture manifests validated")
