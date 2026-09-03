import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
def test_c18_manifests_readable():
 names=("normative_source_integration","requirement_coverage","injection_manifest","regression_report","assumption_plans","delta_delta_manifest","six_quark_color_manifest","hidden_color_basis_manifest","cluster_matching_manifest","hamiltonian_manifest","current_completeness_certificate","continuity_report","partonic_parent_manifest","tensor_b1_manifest","coherent_manifest","cp_reduction_manifest","ttn_convergence_manifest","provenance_complex","benchmark_manifest")
 for n in names:assert load("c18_"+n+".json")["schema_version"]=="1.0.0"
def test_c18_regression_and_counts():
 r=load("c18_regression_report.json");q=load("c18_requirement_coverage.json");i=load("c18_injection_manifest.json")
 assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and q["count"]==len(q["rows"]) and i["count"]==400
def test_c18_readiness_isolation():
 r=load("c18_provenance_complex.json");b=load("c18_benchmark_manifest.json")
 assert not r["production_reachable"] and "PRODUCTION_READY" in r["not_issued"] and len(b["rows"])==18
