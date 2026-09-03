import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())


def test_c23_manifest_set_and_counts():
    names=("normative_source_integration","primary_source_manifest","process_basis_manifest","spin1_structure_function_basis","hard_factor_library","fragmentation_interface_manifest","factorization_glauber_manifest","fixed_order_reference_manifest","wy_matching_manifest","process_capability_matrix","process_accuracy_manifest","uncertainty_manifest","holdout_report","injection_manifest","requirement_coverage","regression_report")
    assert all(L(f"c23_{n}.json")["schema_version"]=="1.0.0" for n in names)
    assert L("c23_injection_manifest.json")["count"]==720
    assert L("c23_requirement_coverage.json")["count"]==580


def test_c23_isolation_and_tiers():
    reg=L("c23_regression_report.json");cap=L("c23_process_capability_matrix.json")
    assert cap["input_eligibility"]=={"analytic":438,"not_eligible":102,"physical":0,"source":0}
    assert not cap["matched_total_executable"]
    assert not reg["source_process_executed"] and not reg["physical_process_executed"]
    assert not reg["likelihood_created"] and not reg["inference_created"] and not reg["production_reachable"]
    assert reg["production_registry"]==216 and reg["all_artifacts_unchanged"]
