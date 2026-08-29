"""C162 source-artifact inventory and fail-closed target boundary tests."""
import pytest

from deuteron_wigner.bridge import hqcdlfgnum3 as c


def numeric_record():
    return {
        "descriptor_id": "TGT-QUARK_FIELD-C43_ADAPTED_MSBAR",
        "target_scheme_id": "C43_ADAPTED_MSBAR",
        "mu": 1.2,
        "mu_units": "GeV",
        "rho": 0.2,
        "rho_units": "GeV",
        "rho_mu_relation": "independent",
        "external_state": {"state_id": "C162-STATE-EXPLICIT"},
        "active_Nf": 4,
        "external_flavor": "u",
        "gauge_pole_record": {"gauge": "C43", "pole": "antisymmetric-PV"},
        "projector": "C43_PROJECTOR",
        "perturbative_coordinate": "g_s^0",
        "precision_record": {"digits": 80},
        "branch_record": {"branch": "real-spacelike"},
        "no_default": True,
        "record_root": "explicit-test-record-root",
    }


def test_roots_and_source_inventory():
    authority = c.load_verified_hqcd_lfgnum3_authority()
    assert authority["status"] == c.STATUS
    assert authority["C161_package_root"] == "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
    inventory = c.source_artifact_inventory()
    assert inventory["count"] == 8
    assert inventory["hashes_verified"] is True
    assert all(row["complete_for_expression_binding"] is False for row in inventory["rows"])
    assert c.source_availability_audit()["exact_equation_locators"] == 0


def test_all_descriptors_have_terminal_status():
    ledger = c.descriptor_execution_ledger()
    assert ledger["descriptor_count"] == 25
    assert ledger["terminal_status_counts"] == {"SOURCE_LOCATOR_INCOMPLETE": 25}
    assert all(row["exact_first_missing_object"] for row in ledger["rows"])
    assert c.lfgnum3_plan_manifest()["selected_plan"] == "LFGNUM3-B"


def test_target_boundary_requires_explicit_record_and_fails_closed():
    rec = numeric_record()
    result = c.target_numeric_coefficient(rec["descriptor_id"], rec)
    assert result["value"] is None
    assert result["positive_gate"] is False
    assert c.target_program_manifest()["program_count"] == 0
    with pytest.raises(ValueError):
        c.validate_target_numeric_record({"descriptor_id": rec["descriptor_id"]})
    with pytest.raises(ValueError):
        c.validate_target_program({"schema": "TARGET_COEFFICIENT_PROGRAM_DAG_V2", "nodes": [{"op": "UNKNOWN"}]})


def test_isolation_and_mutation_controls():
    assert c.static_isolation_guard()["pass"] is True
    assert c.c158_target_crosswalk()["differences_evaluated"] == 0
    for i in range(384):
        mutation = c.mutate_live_hqcdlfgnum3(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
