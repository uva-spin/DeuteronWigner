import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";load=lambda n:json.loads((D/n).read_text())
def test_c16_manifests_readable():
 names=("normative_source_integration","requirement_coverage","injection_manifest","regression_report","nnpi_state_manifest","nnpi_basis_manifest","three_body_recoil_manifest","hamiltonian_flow","pion_active_operator_manifest","transition_operator_manifest","pion_subtraction_manifest","two_body_current_closure","coherent_smallx_manifest","parton_nuclear_overlap_manifest","cp_reduction_manifest","deuteron_parent_manifest","tensor_network_manifest","provenance_complex","tolerance_manifest","readiness_manifest")
 for n in names:assert load("c16_"+n+".json")["schema_version"]=="1.0.0"
def test_c16_counts_and_regression():
 q=load("c16_requirement_coverage.json");i=load("c16_injection_manifest.json");r=load("c16_regression_report.json")
 assert q["count"]==len(q["rows"]) and i["count"]>=280 and i["all_detected"]
 assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["c15_manifests_unchanged"]
def test_c16_readiness_parent_scope():
 r=load("c16_readiness_manifest.json");p=load("c16_deuteron_parent_manifest.json")
 assert not r["production_reachable"] and "PHYSICAL_PION_TMD" in r["not_issued"] and len(p["rows"])==15
