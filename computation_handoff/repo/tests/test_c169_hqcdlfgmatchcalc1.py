"""C169 C43 perturbative-calculation authority tests."""
import pytest

from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c


def test_authority_capsules_and_plan():
    authority = c.load_verified_hqcd_lfgmatchcalc1_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGMATCHCALC1-H"
    assert authority["C168_capsule_count"] == 6
    assert len(c.calculation_capsule_freeze()["rows"]) == 6
    assert c.sixth_calculation_manifest()["exact_sixth"] is True
    assert c.request_resolution_manifest()["count"] == 6


def test_public_owner_and_explicit_missing_sectors():
    owners = c.operator_substrate_manifest()
    assert owners["owner_count"] == 21
    assert owners["rows"][0]["private_builder_called"] is False
    assert c.propagating_contribution_manifest()["missing_as_zero"] == 0
    assert c.direct_instantaneous_manifest()["rows"][0]["missing_as_zero"] == 0
    assert c.zero_boundary_residual_ledger()["missing_as_zero"] == 0
    assert c.count_once_report()["duplicate_semantic_owners"] == 0
    assert c.gluon_two_point_manifest()["rows"][0]["missing_as_zero"] is False
    assert c.qg_vertex_manifest()["rows"][0]["full_1PI"] is False
    assert c.coupling_manifest()["rows"][0]["restricted_Ward_promoted"] is False


def test_separation_and_fail_closed_diagnostics():
    assert c.signed_mass_manifest()["signed_mass_m2_conflation"] == 0
    assert c.quark_two_point_manifest()["K_resolution_count"] == 3
    assert c.diagnostic_manifest()["evaluations"] == 0
    assert c.c158_noncircularity_manifest()["C158_value_inputs"] == 0
    assert c.static_isolation_guard()["pass"] is True
    with pytest.raises(KeyError):
        c.calculation_capsule_freeze("unknown")
    with pytest.raises(KeyError):
        c.operator_substrate_manifest("unknown")
    with pytest.raises(ValueError):
        c.diagnostic_manifest(fixture_id="C144-FIXTURE-1")


def test_restart_query_and_384_live_mutations():
    assert c.dependency_frontier_manifest()["root"] == c.dependency_frontier_manifest()["root"]
    assert c.request_resolution_manifest()["root"] == c.request_resolution_manifest()["root"]
    assert c.graph_program_manifest()["root"] == c.graph_program_manifest()["root"]
    for index in range(384):
        mutation = c.mutate_live_hqcdlfgmatchcalc1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
