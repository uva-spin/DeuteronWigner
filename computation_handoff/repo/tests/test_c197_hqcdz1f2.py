from deuteron_wigner.bridge import hqcdz1f2 as c


def test_authority_and_frozen_upstream_roots():
    a = c.load_verified_hqcd_z1f2_authority()
    assert a["package_root"] == c.PACKAGE_ROOT
    assert c.z1f2_plan_manifest()["selected_plan"] == "Z1F2-A"
    assert c.z1f_handoff_freeze()["C196_projected_coordinates"] == 144
    assert c.static_isolation_guard()["pass"]


def test_projector_roles_and_strict_parameter_guards():
    assert c.projector_role_manifest()["count"] == 8
    assert c.projector_role_manifest()["eligible_multiplicative_count"] == 1
    fixture = c.z1f_fixture_manifest()["rows"][0]["fixture_id"]
    p = c.z1f_parameter_fixture(fixture)
    assert c.validate_z1f_parameter_record(p)["physical"] is False
    assert c.evaluate_z1f(p)["physical_Z1F"] is False
    bad = dict(p)
    bad["projector_id"] = "C152-RANK8-PROJECTOR-8"
    try:
        c.evaluate_z1f(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("boundary nuisance projector must not divide")


def test_imported_vertex_tree_fields_and_field_schemes():
    assert c.complete_vertex_manifest()["count"] == 144
    assert c.tree_normalization_manifest()["count"] == 144
    assert c.zq_manifest()["count"] == 9
    assert c.za_manifest()["count"] == 3
    assert c.z1f_manifest()["count"] == 54
    assert c.z1f_manifest()["rows"][0]["physical"] is False


def test_coupling_branches_jacobian_and_st_boundary():
    fixture = c.z1f_fixture_manifest()["rows"][0]["fixture_id"]
    p = c.z1f_parameter_fixture(fixture)
    assert c.evaluate_qg_coupling_response(p)["full_ST"] is False
    assert c.coupling_manifest()["count"] == 54
    assert c.branch_manifest()["count"] == 3
    assert c.jacobian_manifest()["count"] == 120
    assert c.st_boundary_manifest()["count"] == 10
    assert c.st_boundary_manifest()["full_ST_claim"] is False


def test_crosswalk_request_and_release_boundaries():
    assert c.retained_complete_manifest()["count"] == 144
    assert c.scheme_resolution_manifest()["count"] == 9
    assert c.topology_manifest()["count"] == 14
    assert c.count_once_manifest()["duplicates"] == 0
    assert c.z1f2_release_manifest()["gates"]["Z1F"]
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] and requests["request4_frozen"]
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False


def test_focused_mutations():
    assert all(c.mutate_live_hqcdz1f2(i)["pass"] for i in range(384))
