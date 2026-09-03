import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(n): return json.loads((D/n).read_text())
def test_c15_manifests_machine_readable():
 names=("requirement_coverage","injection_manifest","regression_report","normative_source_integration","nuclear_plan_manifest","nuclear_recoil_manifest","spin1_state_manifest","spectral_amplitude_manifest","deuteron_parent_manifest","spin1_projector_manifest","current_closure_report","b1_closure_report","tagged_closure_report","ttn_convergence_report","provenance_complex","readiness_manifest")
 for n in names: assert load(f"c15_{n}.json")["schema_version"]=="1.0.0"
def test_c15_counts_and_immutable_baseline():
 q=load("c15_requirement_coverage.json");i=load("c15_injection_manifest.json");r=load("c15_regression_report.json")
 assert q["count"]==462 and len(q["rows"])==462 and i["count"]>=200 and i["all_detected"]
 assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and r["c14_manifests_unchanged"]
def test_c15_readiness_and_parent_matrix_scope():
 r=load("c15_readiness_manifest.json");p=load("c15_deuteron_parent_manifest.json")
 assert not r["production_reachable"] and "NUCLEAR_WILSON_READY" in r["not_issued"]
 assert {(x["species"],x["wilson_order"]) for x in p["parents"]}=={(s,o) for s in ("u","d","ubar","dbar","g") for o in (0,1,2)}
