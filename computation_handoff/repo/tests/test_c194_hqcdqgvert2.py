from deuteron_wigner.bridge import hqcdqgvert2 as c


def test_authority_contract_absence_and_plan():
    a = c.load_verified_hqcd_qgvert2_authority()
    assert a["contract_present"] is False and a["contract_absence_fail_closed"]
    assert c.qgvert2_plan_manifest()["selected_plan"] == "QGVERT2-B"
    assert a["package_root"] == c.PACKAGE_ROOT
    assert c.qg_1pi_handoff_freeze()["C193_root"] == c.UPSTREAM["C193"]


def test_parameter_and_external_domain_records_are_explicit():
    f = c.qg_vertex_fixture_manifest("C194-FIXTURE-K9")["rows"][0]
    assert c.validate_qg_vertex_parameter_record(f)["no_defaults"] is True
    assert f["physical"] is False
    assert f["holonomy_capsule_id"] == "IDENTITY_DIAGNOSTIC_ONLY"
    assert c.qg_vertex_fixture_manifest()["count"] == 3
    assert c.external_domain_manifest()["count"] == 6
    assert c.external_domain_manifest(orientation="QG_TO_Q")["rows"][0]["orientation"] == "QG_TO_Q"


def test_qgg_owner_transition_contact_and_matrix_free_routes():
    f = c.qg_vertex_fixture_manifest("C194-FIXTURE-K11")["rows"][0]
    assert c.qgg_vertex_manifest()["count"] == 54
    action = c.apply_qgg_vertex_component(f, ("q",), "C185-QG-QGG-QUARK-EMISSION", "C112", "QGG_COLOR_8A")
    assert action["rows"][0]["matrix_free"] and action["rows"][0]["dense_inverse"] is False
    assert c.qgg_vertex_manifest(contact_owner_id="C127-JQ-K-JG")["count"] == 18
    assert c.qgg_vertex_manifest(transition_owner_id="C186-QG-QGG-CUBIC-GLUON")["count"] == 27


def test_qqbarq_fails_closed_without_qgg_inference():
    f = c.qg_vertex_fixture_manifest("C194-FIXTURE-K13")["rows"][0]
    q = c.qqbarq_vertex_manifest()
    assert q["count"] == 18 and q["not_zero"]
    assert all(r["inferred_from_qgg"] is False for r in q["rows"])
    result = c.apply_qqbarq_vertex_component(f, ("q",), "same_flavor", "QQBARQ_COLOR_QQ_BAR3")
    assert result["executable"] is False and result["not_zero"]


def test_connected_subtraction_proper_boundary_and_projection_ledgers():
    f = c.qg_vertex_fixture_manifest("C194-FIXTURE-K9")["rows"][0]
    connected = c.apply_connected_response(f, ("q",))
    assert connected["proper"] is False
    assert c.connected_response_manifest()["count"] == 3
    assert c.reducible_subtraction_manifest()["count"] == 12
    assert c.proper_kernel_manifest()["count"] == 3
    assert c.vertex_projection_manifest()["count"] == 24
    assert c.interface_manifest()["nonmatrix"]
    assert c.counterterm_manifest()["count"] == 120
    assert c.topology_manifest()["double_count"] == 0


def test_release_frontier_requests_and_mutations():
    assert c.qgvert2_release_manifest()["next"] == "C195/HQCDB1QQBARQVERT1"
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"]
    assert c.request_resolution_manifest()["all_six_visible"]
    assert c.missing_vertex_object_manifest()["count"] == 1
    assert all(c.mutate_live_hqcdqgvert2(i)["pass"] for i in range(384))
