#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
r=load("c18_regression_report.json");q=load("c18_requirement_coverage.json");i=load("c18_injection_manifest.json");d=load("c18_delta_delta_manifest.json");s=load("c18_six_quark_color_manifest.json");h=load("c18_hidden_color_basis_manifest.json");c=load("c18_cluster_matching_manifest.json");cur=load("c18_current_completeness_certificate.json");ready=load("c18_provenance_complex.json")
assert q["count"]==len(q["rows"]) and all(x["status"]=="COVERED_N3_SCOPE" for x in q["rows"])
assert i["count"]>=400 and i["all_detected"] and len({x["stable_id"] for x in i["rows"]})==i["count"]
assert d["antisymmetry_residual"]==0 and s["singlet_multiplicity"]==5 and s["transposition_residual"]==0
assert h["invariance_residual"]<1e-12 and c["subtraction_equivalence_residual"]<1e-12 and cur["complete"]
assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["prior_manifests_unchanged"] and not ready["production_reachable"]
print("C18/N3 architecture manifests validated")
