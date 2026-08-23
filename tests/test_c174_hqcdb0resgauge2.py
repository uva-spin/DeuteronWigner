"""C174 finite-cell scalar/vector residual-gauge tests."""

from deuteron_wigner.bridge import hqcdb0resgauge2 as c


def test_authority_and_prompt_only_provenance():
    a = c.verify_hqcd_b0resgauge2_authority()
    assert a["baseline"] == "dde187bc92e75ea54199bb79b54f170829992afb"
    assert a["expected_contract_present"] is False
    p = c.contract_provenance_report()
    assert p["retrospective_contract_invented"] is False
    assert all(p[k]["prompt_only_authority"] for k in ("historical_C170_missing_contract", "historical_C171_missing_contract", "historical_C172_missing_contract", "historical_C173_missing_contract"))


def test_scalar_vector_complex_and_leakage():
    assert c.global_color_parameter_manifest()["normalizable_HO"] is False
    assert c.p0_vector_field_manifest()["physical_source_space_distinct"] is True
    for row in c.gradient_manifest()["rows"]:
        assert row["route_A_B_residual"] == 0.0
        assert row["finite_shell_leakage"]["threshold_pruned"] is False
        assert row["finite_shell_leakage"]["norm"] > 0.0
    for row in c.transverse_complex_manifest()["rows"]:
        assert row["scalar_kernel_dimension"] == 0
        assert row["cokernel_dimension"] == 0
        assert row["vector_kernel_dimension"] == row["scalar_dimension"]


def test_project_scheme_fp_and_separation():
    assert c.functional_candidate_manifest()["selected"] == "ORBIT_MINIMUM_FUNCTIONAL"
    assert c.project_subgauge_manifest()["scheme_id"] == "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1"
    assert c.orbit_functional_manifest()["route_A_B_C_agree"] is True
    assert all(row["field_dependence"] == "FIELD_DEPENDENT_LOCAL_FP" for row in c.p0_fp_operator_manifest()["rows"])
    assert c.residual_ghost_decision()["decision"] == "EXPLICIT_P0_GHOST_SECTOR_REQUIRED_FIELD_DEPENDENT_FP"
    assert c.residual_ghost_decision()["loop_evaluated"] is False
    assert c.q0_pv_compatibility_manifest()["pole_substitution"] is False
    assert c.residual_link_manifest()["link_unity"] is False
    assert c.open_color_factorization_manifest()["singlet_projection"] is False


def test_gauss_requests_release_and_nonmutation():
    assert len(c.p0_gauss_manifest()["rows"]) == 4
    assert len(c.request_resolution_manifest()["rows"]) == 6
    assert sum(row["terminal_status"] != "PRESERVED_INHERITED_REQUEST" for row in c.request_resolution_manifest()["rows"]) == 2
    assert c.b0_release_manifest()["decision"] == "B0_GEOMETRY_READY_EXPLICIT_P0_GHOST_SECTOR_REQUIRED"
    assert c.static_isolation_guard()["pass"] is True


def test_route_candidate_and_covariance_order_holdouts():
    resolutions = ("K9", "K11", "K13")
    for resolution in resolutions:
        assert c.gradient_manifest(resolution)["rows"][0]["route_A_B_residual"] == 0.0
        assert c.divergence_manifest(resolution)["rows"][0]["adjoint_residual"] == 0.0
        assert c.p0_fp_operator_manifest(resolution)["rows"][0]["route_A_B_C_agree"] is True
    candidates = ("P0_TRANSVERSE_DIVERGENCE", "ORBIT_MINIMUM_FUNCTIONAL", "CELL_AVERAGED_DIVERGENCE", "RESIDUAL_LINK_ANCHOR", "GLOBAL_COLOR_ONLY", "UNAVAILABLE")
    forward = [c.functional_candidate_manifest(x)["rows"][0]["candidate_id"] for x in candidates]
    reverse = [c.functional_candidate_manifest(x)["rows"][0]["candidate_id"] for x in reversed(candidates)]
    assert set(forward) == set(reverse)
    sectors = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F")
    assert {c.p0_gauss_manifest(x)["rows"][0]["sector_id"] for x in sectors} == set(sectors)


def test_safe_loader_and_384_mutations():
    assert c.load_verified_hqcd_b0resgauge2_authority()["package_root"] == c.PACKAGE_ROOT
    for i in range(384):
        mutation = c.mutate_live_hqcdb0resgauge2(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
