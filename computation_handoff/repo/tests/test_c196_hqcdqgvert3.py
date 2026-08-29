from deuteron_wigner.bridge import hqcdqgvert3 as c


def test_authority_plan_and_frozen_imports():
    authority = c.load_verified_hqcd_qgvert3_authority()
    assert authority["package_root"] == c.PACKAGE_ROOT
    assert c.qgvert3_plan_manifest()["selected_plan"] == "QGVERT3-A"
    assert c.vertex_handoff_freeze()["C194_qgg_records"] == 54
    assert c.vertex_handoff_freeze()["C195_qqbarq_records"] == 18


def test_parameter_fixture_and_component_crosswalk():
    fixture = c.qg_vertex_fixture_manifest("C196-FIXTURE-K9-same_flavor-QQBARQ_COLOR_QQ_BAR3")["rows"][0]
    assert c.validate_qg_vertex_parameter_record(fixture)["physical"] is False
    assert c.qg_vertex_fixture_manifest()["count"] == 18
    assert c.qqbarq_crosswalk_manifest()["count"] == 18
    assert all(not row["counted_twice"] for row in c.qqbarq_crosswalk_manifest()["rows"])
    assert c.qgg_component_manifest()["count"] == 54
    assert c.qqbarq_component_manifest()["count"] == 18


def test_connected_owner_response_and_actions():
    fixture = c.qg_vertex_fixture_manifest("C196-FIXTURE-K11-different_flavor-QQBARQ_COLOR_QQ_6")["rows"][0]
    response = c.apply_connected_response(fixture, ("q",))
    assert response["connected"] and response["proper"] is False
    assert c.connected_response_manifest()["count"] == 18
    assert c.direct_owner_manifest()["count"] == 10
    assert c.connected_response_manifest()["rows"][0]["owner_order"] == ("TREE", "DIRECT", "QGG", "QQBARQ", "INTERFACE", "COUNTERTERM")


def test_subtraction_proper_amputation_projection_and_dressing():
    fixture = c.qg_vertex_fixture_manifest("C196-FIXTURE-K13-symbolic_active_flavor-QQBARQ_COLOR_QQ_BAR3")["rows"][0]
    assert c.leg_subtraction_manifest()["count"] == 9
    assert c.reducible_subtraction_manifest()["count"] == 6
    proper = c.apply_proper_kernel(fixture, ("q",))
    assert proper["proper_1PI"] and proper["physical_Z1F"] is False
    assert c.proper_kernel_manifest()["count"] == 18
    amp = c.apply_amputated_vertex(fixture, ("q",))
    assert amp["route_residual"] == "EXACT_SYMBOLIC_ZERO"
    assert c.amputation_manifest()["count"] == 108
    assert c.vertex_projection_manifest()["count"] == 144
    assert c.vertex_dressing_manifest()["count"] == 18
    assert c.z1f_boundary_manifest()["count"] == 144


def test_interfaces_sensitivities_release_and_handoff():
    assert c.interface_manifest()["count"] == 7
    assert c.counterterm_manifest()["count"] == 120
    assert c.analyticity_manifest()["count"] == 18
    assert c.qgvert3_release_manifest()["gates"]["z1f_boundary"]
    assert c.z1f_handoff_contract()["physical_Z1F"] is False
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] and requests["request4_frozen"]
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"]


def test_matrix_free_routes_and_mutations():
    fixture = c.qg_vertex_fixture_manifest("C196-FIXTURE-K9-same_flavor-QQBARQ_COLOR_QQ_BAR3")["rows"][0]
    connected = c.apply_connected_response(fixture, ("q",))
    proper = c.apply_proper_kernel(fixture, ("q",))
    amp = c.apply_amputated_vertex(fixture, ("q",))
    assert connected["sparse_route"] == connected["matrix_free_route"]
    assert proper["sparse_route"] == proper["matrix_free_route"]
    assert amp["sparse_route"] == amp["matrix_free_route"]
    assert all(c.mutate_live_hqcdqgvert3(i)["pass"] for i in range(384))
