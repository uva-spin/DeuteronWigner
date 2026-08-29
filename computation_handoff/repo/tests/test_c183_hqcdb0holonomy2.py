from __future__ import annotations

import pytest

from deuteron_wigner.bridge import hqcdb0holonomy2 as c
from deuteron_wigner.bridge import hqcdb0reslink2 as c182


def test_contract_and_strict_capsules():
    loaded = c.load_verified_hqcd_b0holonomy2_authority()
    assert loaded["status"] == c.STATUS
    assert c.b0holonomy2_plan_manifest()["selected_plan"] == "HOLONOMY2-A"
    assert c.holonomy_fixture_manifest()["count"] == 5
    for fixture_id in c.FIXTURE_IDS:
        capsule = c.fixture_capsule(fixture_id)
        assert c.validate_holonomy_capsule(capsule)["valid"] is True
        assert c.su3_matrix_manifest(fixture_id)["rows"][0]["valid"] is True


def test_su3_cartan_conjugacy_and_center():
    for fixture_id in c.FIXTURE_IDS:
        assert c.representation_manifest(fixture_id)["rows"][0]["adjoint_unitarity_residual"] < 1e-12
        assert c.cartan_manifest(fixture_id)["rows"][0]["determinant_constraint"] == "sum eigenphases=0"
        assert c.conjugacy_manifest(fixture_id)["rows"][0]["class_not_frame"] is True
    centers = c.center_manifest()["rows"]
    assert len(centers) == 3
    assert all(row["adjoint_invisible"] for row in centers)
    assert c.center_manifest("NONTRIVIAL_CENTER_SECTOR")["rows"][0]["fermions_center_sensitive"] is True


def test_boundary_cut_gauge_ghost_and_frame_separation():
    assert all(row["longitudinal_mode_grid_changed"] is False for row in c.boundary_condition_manifest()["rows"])
    assert all(row["classification"] == "NONMATRIX_ZERO_MODE_INTERFACE" for row in c.transition_domain_manifest()["rows"])
    assert c.cut_pv_manifest()["PV_dropped"] is False
    assert all(row["Q0_inverse_changed"] is False for row in c.gauge_compatibility_manifest()["rows"])
    assert c.ghost_compatibility_manifest()["holonomy_in_local_ghost_determinant"] is False
    assert all(row["open_adjoint"] for row in c.global_frame_manifest()["rows"])


def test_conditional_full_link_and_no_physical_selection():
    local = c182.fixture_parameter_record("C182_FIXTURE_RETAINED_BOUNDARY_V1")
    capsule = c.fixture_capsule("CONJUGATED_NONDIAGONAL_GENERIC")
    full = c.apply_full_periodic_link(local, capsule, (1, 0, 0, 0, 0, 0, 0, 0), 2)
    assert full["state"] == "FULL_PERIODIC_LINK_WITH_EXPLICIT_CAPSULE"
    assert len(full["action"]) == 8
    assert c.physical_selection_manifest()["row"]["conjugacy_selected"] is False


def test_request_census_and_mutation_gate():
    assert len(c.request_resolution_manifest()["rows"]) == 6
    assert c.request_resolution_manifest()["active_count"] == 2
    assert len(c.missing_holonomy_object_manifest()["rows"]) == 2
    assert c.b0_release_manifest()["row"]["decision"] == "B0_CONDITIONAL_SU3_HOLONOMY_CAPSULE_AUTHORITY_READY_MATCHING_NEXT"
    for i in range(384):
        mutation = c.mutate_live_hqcd_b0holonomy2(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True


def test_invalid_matrix_never_silently_repairs():
    capsule = dict(c.fixture_capsule("GENERIC_CARTAN_INTERIOR"))
    capsule["fundamental_matrix"] = (([2, 0], [0, 0], [0, 0]), ([0, 0], [2, 0], [0, 0]), ([0, 0], [0, 0], [1, 0]))
    with pytest.raises(ValueError):
        c.validate_holonomy_capsule(capsule)
