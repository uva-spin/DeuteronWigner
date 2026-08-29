import json
from pathlib import Path

import pytest

from deuteron_wigner.process.p1.core import (
    PHYSICAL_GATES,
    SOURCE_GATES,
    QualificationDecision,
    candidate_decisions,
    injection_rows,
    validate_no_tier_inflation,
)

DOCS = Path(__file__).resolve().parents[1] / "docs" / "next_level"


def load(name):
    return json.loads((DOCS / name).read_text())


def test_gate_schema_is_ordered_and_complete():
    assert len(SOURCE_GATES) == 13
    assert len(PHYSICAL_GATES) == 6


def test_all_audited_candidates_fail_closed_at_source_tier():
    decisions = candidate_decisions()
    assert len(decisions) == 10
    assert not any(x.source_eligible for x in decisions)
    assert not any(x.physical_eligible for x in decisions)


def test_physical_cannot_pass_without_source():
    source = dict.fromkeys(SOURCE_GATES, False)
    physical = dict.fromkeys(PHYSICAL_GATES, True)
    row = QualificationDecision("X", "U", "DY", 0, source, physical).record()
    with pytest.raises(ValueError, match="PHYSICAL_WITHOUT_SOURCE"):
        validate_no_tier_inflation([row | {"physical_eligible": True}])


def test_gate_schema_rejects_missing_field():
    source = dict.fromkeys(SOURCE_GATES[:-1], True)
    with pytest.raises(ValueError, match="SOURCE_GATE_SCHEMA"):
        QualificationDecision("X", "U", "DY", 0, source, dict.fromkeys(PHYSICAL_GATES, False))


def test_matched_total_rejected():
    with pytest.raises(ValueError, match="MATCHED_TOTAL_FORBIDDEN"):
        QualificationDecision("X", "U", "DY", 0, dict.fromkeys(SOURCE_GATES, True), dict.fromkeys(PHYSICAL_GATES, False), "MATCHED_TOTAL")


def test_injections_are_ordered_stable_and_large_enough():
    rows = injection_rows()
    assert len(rows) == 880
    assert [x["ordinal"] for x in rows] == list(range(1, 881))
    assert len({x["stable_id"] for x in rows}) == 880


def test_artemide_version_is_exact_and_not_substituted():
    lock = load("c24_source_package_lock_manifest.json")
    assert lock["artemide_paper_release"] == "3.01"
    assert lock["current_release_audited"] == "3.03"
    assert lock["current_release_substituted"] is False
    assert lock["art25_replicas_in_archive"] == 0


def test_source_physical_tiers_are_distinct():
    matrix = load("c24_source_process_eligibility_matrix.json")
    assert matrix["counts"] == {"analytic": 438, "not_process_eligible": 102, "source": 0, "physical": 0}


def test_todd_and_multiparton_fail_closed():
    assert load("c24_source_process_eligibility_matrix.json")["todd_multiparton_fail_closed"]


def test_quark_gluon_boundaries_are_separate():
    plans = load("c24_cs_largeb_source_manifest.json")["plans"]
    gluon = next(x for x in plans if x["stable_id"] == "P1-CS-GLUON")
    assert not gluon["quark_kernel_copied"]
    assert not gluon["nonperturbative_casimir_scaling_imposed"]


def test_collinear_ff_is_not_tmdff():
    ff = load("c24_fragmentation_source_manifest.json")
    assert not ff["collinear_ff_called_tmdff"]
    assert ff["source_qualified_tmdff_bundles"] == 0


def test_dy_and_sidis_not_executed_with_missing_sources():
    assert not load("c24_dy_source_validation_manifest.json")["source_executable"]
    assert not load("c24_sidis_source_validation_manifest.json")["source_executable"]


def test_source_wy_does_not_mutate_analytic_records():
    wy = load("c24_source_wy_manifest.json")
    assert wy["source_records_executed"] == 0
    assert wy["analytic_c23_records_immutable"]
    assert not wy["boundary_retuned"]


def test_spin1_scopes_remain_honest():
    data = load("c24_b1_tagged_prerequisite_manifest.json")
    assert data["inclusive_b1"]["status"] == "UNAVAILABLE"
    assert data["inclusive_b1"]["nn_only_not_complete_deuteron"]
    assert not data["tagged_dis"]["ordinary_tmdff"]


def test_heavy_pair_is_conditional_and_no_fd_default():
    data = load("c24_gluon_process_source_manifest.json")
    assert data["status"] == "CONDITIONAL_SOURCE_INTERFACE_ONLY"
    assert not data["default_f_plus_d"]


def test_regression_isolation():
    reg = load("c24_regression_report.json")
    assert reg["production_registry"] == 216
    assert reg["all_artifacts_unchanged"]
    assert reg["analytic_c23_plans_immutable"]
    assert not reg["likelihood_created"]
    assert not reg["inference_created"]
    assert not reg["production_reachable"]


def test_all_generated_json_is_parseable():
    for path in DOCS.glob("c24_*.json"):
        assert json.loads(path.read_text())["schema_version"] == "1.0.0"
