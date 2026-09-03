#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
r=L("c20_regression_report.json");q=L("c20_requirement_coverage.json");i=L("c20_injection_manifest.json");m=L("c20_unavailable_operator_matrix.json");f=L("c20_matching_fit_report.json")
assert q["count"]==len(q["rows"]);assert i["count"]==560 and i["all_detected"];assert len(m["entries"])==540 and m["executable"]==492 and m["unavailable"]==48;assert f["conditions"]>f["parameters"] and f["holdouts"]>=3;assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
print("C20/M1 architecture manifests validated")
