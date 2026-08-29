"""C179 symbolic finite-HO path comparison tests."""

from deuteron_wigner.bridge import hqcdb0reslinkpath1 as c


def test_contract_and_c178_freeze():
    authority = c.verify_hqcd_b0reslinkpath1_authority()
    assert authority["baseline"] == "fea467e8b02340d84d5d83323c8d4a585981a3de"
    assert authority["contract_sha256"] == "feaeaf061c4e7b7bfdf98957c4f671ffae3f40c1d2b2934ea09cf473bb670978"
    assert authority["C178_package_root"] == "4a8768a8fa12406b99370fffe26886c149ba0acdc8ae3c7a843900a0504dd38b"
    assert authority["C178_package_root_verified"] is True
    assert authority["new_source_acquisitions"] == 0
    assert authority["C166_graph_nodes_added"] == 0
    assert authority["C166_graph_edges_added"] == 0


def test_endpoint_and_candidate_registry():
    endpoints = c.endpoint_domain_manifest()
    assert endpoints["symbolic_domain_complete"] is True
    assert endpoints["physical_endpoint_values"] is False
    assert len(endpoints["rows"]) == 2
    candidates = c.candidate_path_manifest()
    assert candidates["compiled_before_selection"] is True
    assert set(candidates["accepted_ids"]) == set(c.ACCEPTED_CANDIDATES)
    assert len(candidates["rows"]) == 7
    assert next(x for x in candidates["rows"] if x["candidate_id"] == "SOURCE_HALF_LINK_COMPOSITION")["admissibility"] == "REJECTED_NO_FINITE_COMMON_REFERENCE"


def test_degree_one_and_ordered_degree_two_geometry():
    degree1 = c.degree1_geometry_manifest()
    assert len(degree1["rows"]) == 36
    assert all(row["value"] == 1.0 for row in degree1["rows"])
    assert all(row["route_residual"] == 0.0 for row in degree1["rows"])
    degree2 = c.degree2_geometry_manifest()
    assert len(degree2["rows"]) == 72
    assert degree2["ordered"] is True
    assert all(row["symmetrized"] is False for row in degree2["rows"])
    assert all(row["g_s_factor"] is False for row in degree2["rows"])
    assert any(row["value"] == 0.0 for row in degree2["rows"])
    assert any(row["value"] == 1.0 for row in degree2["rows"])


def test_difference_scope_and_boundary_ownership():
    difference = c.path_difference_manifest()
    assert all(row["same_endpoints"] for row in difference["rows"])
    assert all(row["same_cut_side"] for row in difference["rows"])
    assert all(row["same_holonomy"] for row in difference["rows"])
    assert any(row["degree"] == 2 and row["difference"] != 0.0 for row in difference["rows"])
    assert all(row["difference"] == 0.0 for row in difference["rows"] if row["degree"] == 1)
    assert all(row["degree_two_promotion"] is False for row in c.linearized_path_manifest()["rows"])
    owners = c.ho_boundary_ownership_manifest()
    assert all(row["threshold_pruned"] is False for row in owners["rows"])
    assert all(row["unrestricted_omitted_space_materialized"] is False for row in owners["rows"])
    assert any(row["status"] == "PATH_DIFFERENCE_PARTIALLY_BOUNDARY_OWNED" for row in owners["rows"])


def test_representative_covariance_and_requests():
    rep = c.project_representative_manifest()["row"]
    assert rep["selected"] == "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
    assert rep["straight_is_unique_source_path"] is False
    assert rep["extra_scale"] == "none"
    assert c.orientation_covariance_manifest()["rows"][0]["future_past_merged"] is False
    assert all(row["forward_status"] == "closed" for row in c.cut_shift_path_manifest()["rows"])
    assert c.path_systematic_manifest()["rows"][0]["claim_tier"] == "FINITE_BASIS_PATH_SCHEME_VARIATION_ONLY"
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert sum(row["C179_terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in requests["rows"]) == 2
    assert c.b0_release_manifest()["row"]["decision"] == "B0_FINITE_HO_PATH_SCHEME_READY_NONZERO_DEGREE2_DEPENDENCE"


def test_loader_and_mutation_campaign():
    assert c.load_verified_hqcd_b0reslinkpath1_authority()["package_root"] == c.PACKAGE_ROOT
    assert c.static_isolation_guard()["pass"] is True
    for index in range(384):
        row = c.mutate_live_hqcdb0reslinkpath1(index)
        assert row["positive_gate"] is False
        assert row["must_fail_or_change_root"] is True
