import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(name): return json.loads((D/name).read_text())
def test_c11_required_manifests_and_coverage():
 assert load("c11_requirement_coverage.json")["count"]>=250
 assert load("c11_injection_manifest.json")["count"]==104
 assert load("c11_gtmd_operator_registry.json")["count"]==20
def test_c11_projector_symmetry_and_closures():
 assert load("c11_quark_antiquark_projector_manifest.json")["generic_rank"]==16
 assert load("c11_gluon_projector_manifest.json")["generic_rank"]==16
 assert load("c11_current_emt_closure_report.json")["maximum_residual"]==0
 assert load("c11_wigner_oam_closure_report.json")["maximum_route_residual"]==0
def test_c11_regression_production_is_immutable():
 r=load("c11_regression_report.json")
 assert r["production_registry"]==216 and r["all_artifacts_unchanged"]
 assert not r["production_reachable"] and r["injections"]["C11"]>=100
