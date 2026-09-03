from deuteron_wigner.bridge import hqcdst2 as c
from deuteron_wigner.bridge import hqcdz1f2 as c197


def test_authority_plan_and_boundary_freeze():
    authority = c.load_verified_hqcd_st2_authority()
    assert authority["package_root"] == c.PACKAGE_ROOT
    assert c.st2_plan_manifest()["selected_plan"] == "ST2-A"
    assert c.st_handoff_freeze()["C197_Z1F_records"] == 54
    assert c.st_handoff_freeze()["C197_coupling_records"] == 54


def test_exact_missing_objects_and_variables():
    missing = c.missing_st_object_manifest()
    assert missing["count"] == 10
    assert tuple(x["object_id"] for x in missing["rows"]) == tuple(f"C197-ST-{i}" for i in range(1, 11))
    assert c.variable_manifest()["counterterms"] == 6
    assert c.variable_manifest()["nulls"] == 9
    assert c.variable_manifest()["count"] == 41


def test_identity_and_channel_boundaries():
    roles = c.identity_row_manifest()["status_census"]
    assert roles["EXACT_PROJECT_IDENTITY"] == 54
    assert roles["MISSING_OBJECT_BLOCKED"] == 10
    assert roles["BOUNDARY_OR_LINK_DIAGNOSTIC"] == 5
    assert c.qg_identity_manifest()["count"] == 324
    assert c.ghost_manifest()["count"] == 7
    assert c.pure_gluon_manifest()["count"] == 5
    assert c.brst_manifest()["count"] == 1
    assert c.boundary_identity_manifest()["count"] == 7


def test_residual_jacobian_compatibility_and_solution_family():
    fixture_id = c197.z1f_fixture_manifest()["rows"][0]["fixture_id"]
    parameter = c197.z1f_parameter_fixture(fixture_id)
    residual = c.evaluate_st_residuals(parameter, "C198-ST-SYSTEM-K9")
    assert residual["physical"] is False
    jac = c.evaluate_st_jacobian(parameter, "C198-ST-SYSTEM-K9")
    assert jac["variable_order"] == c.FIFTEEN
    assert jac["nullity"] == 14
    assert c.jacobian_manifest()["count"] == 3
    assert c.compatibility_manifest()["inconsistent_systems"] == 0
    family = c.solution_family_manifest()["rows"][0]
    assert family["family"].startswith("delta theta =")
    assert family["free_coordinates_default_zero"] is False
    assert family["selected_representative"] is False


def test_frontier_release_and_nonmutation():
    assert c.st_frontier_manifest()["first_object"] == "C197-ST-1"
    assert c.st_frontier_manifest()["rows"][0]["selected_first"]
    assert c.st2_release_manifest()["gates"]["solution_family"]
    assert c.st2_release_manifest()["gates"]["full_ST"] is False
    assert c.request_resolution_manifest()["all_six_visible"]
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"]


def test_focused_mutations():
    assert all(c.mutate_live_hqcdst2(i)["pass"] for i in range(384))
