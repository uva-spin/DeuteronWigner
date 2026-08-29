import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
def test_c20_files():
 for n in ("coefficient_library","coefficient_source_audit","external_matrix_element_manifest","matching_plan_manifest","matching_fit_report","step_scaling_manifest","small_b_ope_manifest","scheme_roundtrip_report","holdout_report","uncertainty_ledger","unavailable_operator_matrix","injection_manifest","regression_report","normative_source_integration","requirement_coverage"):assert L("c20_"+n+".json")["schema_version"]=="1.0.0"
def test_c20_matrix():
 m=L("c20_unavailable_operator_matrix.json");assert len(m["entries"])==540 and m["executable"]==492 and m["unavailable"]==48
def test_c20_release():
 r=L("c20_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
