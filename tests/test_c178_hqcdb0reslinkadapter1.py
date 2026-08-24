"""C178 periodic cut-side adapter and holonomy boundary tests."""

from deuteron_wigner.bridge import hqcdb0reslinkadapter1 as c


def test_contract_and_inherited_root_freeze():
    authority = c.verify_hqcd_b0reslinkadapter1_authority()
    assert authority["baseline"] == "ed5721329d15de326b382926603fdb3087177a0b"
    assert authority["contract_sha256"] == "e996e6c7113f9997d6ef1d4ccc20561bb58b36a185fdec4685d00f39fbe04683"
    assert authority["C177_package_root"] == "f65edb938e355b72e4bc950a1a20f84220ac18c6f980dae6005cb531f1614f90"
    assert authority["C177_package_root_verified"] is True
    assert authority["new_source_acquisitions"] == 0
    assert authority["C166_graph_nodes_added"] == 0
    assert authority["C166_graph_edges_added"] == 0


def test_circle_cut_sides_and_transition():
    circle = c.periodic_circle_manifest()["row"]
    assert circle["circle_id"] == "C178_LONGITUDINAL_CIRCLE_S_L_2L"
    assert circle["period"] == "2L"
    assert circle["cut_is_source_infinity"] is False
    sides = c.cut_side_manifest()
    assert sides["two_sides_retained"] is True
    assert {row["cut_side_id"] for row in sides["rows"]} == set(c.CUT_SIDE_IDS)
    transition = c.transition_function_manifest()["rows"][0]
    assert transition["identity_selected"] is False
    assert transition["A_plus_local_zero_implies_identity"] is False
    assert transition["kind"] == "nonmatrix zero-mode/global interface"
    assert c.holonomy_manifest()["rows"][0]["status"] == "HOLONOMY_INTERFACE_EXPLICIT"


def test_orientation_pv_projector_and_boundary_separation():
    source = c.source_to_cut_manifest()
    by_id = {row["path_class_id"]: row for row in source["rows"]}
    assert by_id["BJY_DIS_FUTURE_HALF_LINK"]["cut_side_frame"] == "C178_CUT_SIDE_PLUS"
    assert by_id["BJY_DY_PAST_HALF_LINK"]["cut_side_frame"] == "C178_CUT_SIDE_MINUS"
    assert by_id["JMY_OFFLIGHTCONE_STAPLE"]["status"] == "COMPARISON_ONLY_NOT_C43"
    assert source["future_past_merged"] is False
    assert c.pv_cut_manifest()["row"]["transition_inserted"] is True
    assert c.p0_q0_manifest()["Q0_antisymmetric_PV_inverse"] == "UNCHANGED"
    assert c.subgauge_compatibility_manifest()["row"]["status"] == "C174_SUBGAUGE_COMPATIBLE"
    assert c.ghost_boundary_manifest()["row"]["endpoint_orthogonality"] == "not promoted"


def test_covariance_color_and_path_gate():
    covariance = c.transition_covariance_manifest()
    assert len(covariance["rows"]) == 8
    assert all(row["direct_frame_residual"] == 0.0 for row in covariance["rows"])
    color = c.open_color_manifest()["row"]
    assert color["external_adjoint_coordinate"] == "retained"
    assert color["C171_gg_multiplicities"] == ("d", "f")
    assert c.global_volume_manifest()["row"]["holonomy_counted_as_volume"] is False
    assert c.trivial_holonomy_manifest()["row"]["selected"] is False
    gate = c.finite_ho_path_gate_manifest()
    assert [row["C176_leakage_entries"] for row in gate["rows"]] == [16, 20, 24]
    assert all(row["C176_leakage_threshold_pruned"] is False for row in gate["rows"])
    assert c.project_representative_manifest()["selected_representative"] is None


def test_requests_frontier_loading_and_mutations():
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert sum(row["C178_terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in requests["rows"]) == 2
    assert c.dependency_frontier_manifest()["C166_graph_nodes_added"] == 0
    assert c.dependency_frontier_manifest()["C166_graph_edges_added"] == 0
    assert c.load_verified_hqcd_b0reslinkadapter1_authority()["package_root"] == c.PACKAGE_ROOT
    for index in range(384):
        row = c.mutate_live_hqcdb0reslinkadapter1(index)
        assert row["positive_gate"] is False
        assert row["must_fail_or_change_root"] is True
