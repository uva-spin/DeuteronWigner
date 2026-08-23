"""C177 source/path authority and finite-cell fail-closed tests."""

from deuteron_wigner.bridge import hqcdb0reslinksource1 as c


def test_baseline_contract_and_source_cache():
    authority = c.verify_hqcd_b0reslinksource1_authority()
    assert authority["baseline"] == "f10ffa776a274ae226b9640f9a9ebf896f736a48"
    assert authority["contract_sha256"] == "4cd0ebf313762ba7041a10b2fb5141e603a6e71cf530b951a59ef23deeec1033"
    assert authority["C176_package_root"] == "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5"
    assert c.source_audit_manifest()["all_hash_verified"] is True


def test_exact_source_objects_and_paths():
    objects = c.source_object_manifest()
    assert len(objects["rows"]) == 7
    assert objects["rows"][0]["pdf_page"] == 12
    assert {row["path_class_id"] for row in c.continuum_path_class_manifest()["rows"]} == {
        "BJY_DIS_FUTURE_HALF_LINK", "BJY_DIS_FUTURE_REDUCED_LINK",
        "BJY_DY_PAST_HALF_LINK", "BJY_DY_PAST_REDUCED_LINK",
        "JY_TRANSVERSE_INFINITY_CLASS", "JMY_OFFLIGHTCONE_STAPLE",
    }
    assert c.half_link_cancellation_manifest()["rows"][0]["non_Abelian_commutation"] is False
    assert c.pure_gauge_manifest()["rows"][0]["classification"] == "LINEARIZED_PATH_INDEPENDENT_ONLY"


def test_future_past_representation_and_cell_gate():
    fp = c.future_past_manifest()
    assert {row["process_class"] for row in fp["rows"]} == {"DIS_FUTURE", "DY_PAST", "JMY_OFFLIGHTCONE"}
    assert fp["merged"] is False
    rep = c.representation_lift_manifest()
    assert len(rep["rows"]) == 8
    assert rep["all_eight_generators"] is True
    assert rep["open_adjoint"] is True
    assert c.finite_cell_adapter_manifest()["rows"][0]["classification"] == "FINITE_CELL_ADAPTER_INCOMPLETE"
    assert c.project_path_manifest()["project_path_id"] == "NO_PROJECT_REPRESENTATIVE_SELECTED"


def test_ho_boundary_read_only_and_handoff():
    rows = c.finite_ho_path_manifest()["rows"]
    assert [row["C176_leakage_entries"] for row in rows] == [16, 20, 24]
    assert all(row["C176_leakage_threshold_pruned"] is False for row in rows)
    assert all(row["classification"] == "PATH_COMPARISON_NOT_EXECUTABLE_SOURCE_ONLY" for row in rows)
    handoff = c.executable_link_handoff_contract()
    assert handoff["boundary_values_constructed"] is False
    assert handoff["project_path_absence"] is True


def test_requests_frontier_loader_and_mutations():
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert sum(row["C177_terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in requests["rows"]) == 2
    assert c.dependency_frontier_manifest()["C166_graph_nodes_added"] == 0
    assert c.dependency_frontier_manifest()["C166_graph_edges_added"] == 0
    assert c.load_verified_hqcd_b0reslinksource1_authority()["package_root"] == c.PACKAGE_ROOT
    for index in range(384):
        row = c.mutate_live_hqcdb0reslinksource1(index)
        assert row["positive_gate"] is False
        assert row["must_fail_or_change_root"] is True
