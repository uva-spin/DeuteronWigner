import json
from pathlib import Path

D=Path(__file__).resolve().parents[1]/"docs"/"next_level"


def test_c14_required_manifests_are_machine_readable():
    names=("requirement_coverage","injection_manifest","regression_report","normative_source_integration",
           "color_permutation_manifest","sector_tower_manifest","renormalization_trajectory","tensor_network_manifest",
           "wilson_support_manifest","dyson_magnus_manifest","spectral_cut_manifest","soft_overlap_manifest",
           "gauge_closure_report","explicit_induced_comparison","convergence_manifest","prediction_plan_manifest")
    for name in names:
        data=json.loads((D/f"c14_{name}.json").read_text()); assert data["schema_version"]=="1.0.0"


def test_c14_coverage_and_injections_complete():
    req=json.loads((D/"c14_requirement_coverage.json").read_text())
    inj=json.loads((D/"c14_injection_manifest.json").read_text())
    assert req["count"]==len(req["rows"]) and all(x["status"]=="COVERED_H7_SCOPE" for x in req["rows"])
    assert inj["count"]>=168 and inj["all_detected"] and len({x["stable_id"] for x in inj["rows"]})==inj["count"]


def test_c14_regression_and_support_gates():
    reg=json.loads((D/"c14_regression_report.json").read_text())
    sup=json.loads((D/"c14_wilson_support_manifest.json").read_text())
    assert reg["production_registry"]==216 and reg["all_artifacts_unchanged"] and reg["c13_manifests_unchanged"]
    assert all(sup["table"][x]["2"]=="EXPLICIT_FOCK_SUPPORTED" for x in sup["table"])
