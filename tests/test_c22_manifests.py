import json
from pathlib import Path

D = Path(__file__).resolve().parents[1] / "docs" / "next_level"


def load(name):
    return json.loads((D / f"c22_{name}.json").read_text())


def test_c22_manifest_shapes():
    for name in ("normative_source_integration", "primary_source_manifest", "distribution_algebra_manifest", "coefficient_library", "coefficient_source_audit", "gamma5_scheme_manifest", "splitting_function_library", "collinear_evolution_manifest", "ope_rg_consistency_report", "smallb_capability_matrix", "m3_multiq_capability_matrix", "nuclear_ope_manifest", "accuracy_manifest", "uncertainty_manifest", "holdout_report", "injection_manifest", "requirement_coverage", "regression_report"):
        assert load(name)["schema_version"] == "1.0.0"


def test_c22_manifest_counts_and_isolation():
    assert load("primary_source_manifest")["count"] == 15
    assert load("requirement_coverage")["count"] == 980
    assert load("injection_manifest")["count"] == 720
    assert len(load("m3_multiq_capability_matrix")["rows"]) == 540
    assert load("regression_report")["production_registry"] == 216
    assert not load("regression_report")["process_reachable"]
