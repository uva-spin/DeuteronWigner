"""C173 residual-gauge source/finite-cell boundary tests."""

from deuteron_wigner.bridge import hqcdb0resgauge1 as c


def test_authority_and_prompt_only_chain():
    a = c.verify_hqcd_b0resgauge1_authority()
    assert a["baseline"] == "0db3440c42545d7a55df205c0d0180a556e869ad"
    assert a["expected_contract_present"] is False
    p = c.contract_provenance_report()
    assert p["retrospective_contract_invented"] is False
    assert p["historical_C170_missing_contract"]["prompt_only_authority"]
    assert p["historical_C171_missing_contract"]["prompt_only_authority"]
    assert p["historical_C172_missing_contract"]["prompt_only_authority"]


def test_source_and_geometry_are_separate():
    source = c.continuum_pv_subgauge_manifest()["row"]
    assert source["source_id"] == "ARXIV-1508.07962V1"
    assert source["pdf_page"] == source["printed_page"] == 9
    assert source["status"] == "AUTHENTICATED_CONTINUUM_CANDIDATE_FINITE_CELL_UNPROVED"
    adapter = c.infinite_to_finite_adapter_manifest()["rows"][0]
    assert adapter["finite_cell_identity"] is False
    assert adapter["route_mismatch"] is False
    assert c.pv_propagator_manifest()["pole_substitution"] is False


def test_domain_candidates_and_nonpromotion():
    assert c.residual_parameter_manifest()["global_not_HO"] is True
    assert c.subgauge_candidate_manifest()["selected"] is None
    assert c.project_subgauge_manifest()["selected"] is False
    fp = c.p0_fp_operator_manifest()
    assert fp["operator"] is None
    assert fp["Q0_not_promoted"] is True
    assert c.open_color_factorization_manifest()["singlet_projection"] is False
    assert c.residual_link_manifest()["link_unity"] is False


def test_b0_records_and_requests():
    assert len(c.p0_gauss_subgauge_manifest()["rows"]) == 4
    assert len(c.request_resolution_manifest()["rows"]) == 6
    assert sum(row["terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in c.request_resolution_manifest()["rows"]) == 2
    assert c.b0_release_manifest()["decision"] == "B0_NOT_RELEASED_FINITE_CELL_SUBGAUGE_ADAPTER_INCOMPLETE"
    assert c.target_gauge_separation_manifest()["target_ghost_imported"] is False
    assert c.brst_st_boundary_manifest()["BRST"] == "BRST_NOT_CONSTRUCTED"


def test_safe_loader_and_384_mutations():
    # Runtime manifest is intentionally required; no build-if-missing path exists.
    assert c.load_verified_hqcd_b0resgauge1_authority()["package_root"] == c.PACKAGE_ROOT
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        m = c.mutate_live_hqcdb0resgauge1(i)
        assert m["positive_gate"] is False
        assert m["must_fail_or_change_root"] is True
