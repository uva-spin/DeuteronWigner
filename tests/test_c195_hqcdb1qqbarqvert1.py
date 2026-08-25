from deuteron_wigner.bridge import hqcdb1qqbarqvert1 as c


def test_authority_blocker_and_freeze():
    authority = c.load_verified_hqcd_b1qqbarqvert1_authority()
    assert authority["package_root"] == c.PACKAGE_ROOT
    assert c.blocker_manifest()["not_zero"]
    assert c.blocker_manifest()["deduplicated"]
    assert c.qqbarq_handoff_freeze()["C194_record_count"] == 18


def test_owner_branch_flavor_color_denominator_routes():
    assert c.owner_manifest()["count"] == 8
    assert c.quark_branch_manifest()["count"] == 6
    assert {r["direction"] for r in c.qqbarq_branch_manifest()["rows"]} == {"Q_TO_QQBARQ", "QQBARQ_TO_Q"}
    assert c.flavor_pauli_manifest()["count"] == 9
    assert c.color_manifest()["count"] == 2
    assert c.denominator_manifest()["count"] == 6
    assert c.denominator_manifest()["rows"][0]["ordinary_zero_mode"] is False


def test_symbolic_fixtures_coefficients_and_actions():
    fixture = c.qqbarq_fixture_manifest("C195-K9-Q_TO_QQBARQ-same_flavor-QQBARQ_COLOR_QQ_BAR3")["rows"][0]
    assert c.validate_qqbarq_parameter_record(fixture)["physical"] is False
    assert c.qqbarq_fixture_manifest()["count"] == 36
    assert c.coefficient_manifest()["count"] == 36
    value = c.evaluate_qqbarq_coefficient(fixture)
    assert value["value_kind"] == "SYMBOLIC_NONPHYSICAL_FIXTURE"
    forward = c.apply_q_to_qqbarq(fixture, ("q",))
    reverse = c.apply_qqbarq_to_q(fixture, ("qqbarq",))
    assert forward["dense_matrix"] is False and reverse["hermitian_reverse"]


def test_transition_resolvent_component_and_crosswalk():
    assert c.transition_manifest()["count"] == 3
    assert c.qqbarq_vertex_manifest()["count"] == 18
    assert all(row["terminal"] for row in c.qqbarq_vertex_manifest()["rows"])
    fixture = c.qqbarq_fixture_manifest("C195-K11-QQBARQ_TO_Q-different_flavor-QQBARQ_COLOR_QQ_6")["rows"][0]
    action = c.apply_qqbarq_vertex_component(fixture, ("q",))
    assert action["proper_qg_vertex_assembled"] is False
    assert c.c194_crosswalk_manifest()["count"] == 18
    assert c.qgvert3_handoff_contract()["complete_qg_1PI"] is False


def test_paging_derivatives_holonomy_and_release():
    assert c.iter_sparse_coordinates("K13", "symbolic_active_flavor", "QQBARQ_COLOR_QQ_BAR3")
    assert c.sparse_manifest()["count"] == 18
    assert c.derivative_manifest()["count"] == 18
    assert c.hermitian_manifest()["count"] == 18
    assert c.holonomy_bc_manifest()["count"] > 0
    assert c.qqbarqvert1_release_manifest()["next"] == "C196/HQCDQGVERT3"
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.static_isolation_guard()["pass"]


def test_live_mutations_and_nonmutation():
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert all(c.mutate_live_hqcdb1qqbarqvert1(i)["pass"] for i in range(384))
