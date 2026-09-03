#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
r=L("c21_regression_report.json");q=L("c21_requirement_coverage.json");i=L("c21_injection_manifest.json");a=L("c21_anomalous_dimension_library.json");c=L("c21_evolution_capability_matrix.json");k=L("c21_cs_kernel_fit_manifest.json")
assert q["count"]==len(q["rows"]);assert i["count"]==640 and i["all_detected"];assert len(a["records"])==7 and a["quartic_casimir_visible"];assert len(c["rows"])==540 and c["matching_executable"]==492 and c["matching_unavailable"]==48;assert not k["one_kernel_per_tmd"] and r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
print("C21/M2 architecture manifests validated")
