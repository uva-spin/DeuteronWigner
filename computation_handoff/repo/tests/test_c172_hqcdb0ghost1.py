"""C172 Q0 ghost/P0 residual-gauge boundary tests."""

from deuteron_wigner.bridge import hqcdb0ghost1 as c


def test_authority_and_prompt_only_provenance():
    authority = c.verify_hqcd_b0ghost1_authority()
    assert authority["baseline"] == "754b69c8920b8ce36cc0efeeaf1988f005ce255f"
    assert authority["C171_package_root"] == c.C171_PACKAGE_ROOT
    assert authority["expected_contract_present"] is False
    provenance = c.contract_provenance_report()
    assert provenance["retrospective_contract_invented"] is False
    assert provenance["historical_C170_missing_contract"]["prompt_only_authority"] is True
    assert provenance["historical_C171_missing_contract"]["prompt_only_authority"] is True


def test_projectors_fp_and_q0_scope():
    p = c.p0_q0_projector_manifest()
    assert p["P0_squared_residual"] == 0.0
    assert p["Q0_squared_residual"] == 0.0
    assert p["PQ_residual"] == 0.0
    assert p["completeness_residual"] == 0.0
    fp = c.q0_fp_operator_manifest()
    assert len(fp["mode_eigenvalues"]) == 13 * 2 * 8
    assert fp["route_A_B_mismatch"] is False
    cert = c.q0_ghost_decoupling_certificate()
    assert cert["scope"] == "Q0_NONZERO_MODE_GHOST_DECOUPLING_ONLY"
    assert cert["full_P0_closure"] is False


def test_residual_classes_link_and_open_color():
    group = c.residual_gauge_group_manifest()
    assert group["count"] == 5
    assert group["global_color_separate"] is True
    assert group["open_adjoint_quotiented"] is False
    assert c.residual_subgauge_manifest()["decision"] == "NO_SOURCE_QUALIFIED_SUBGAUGE"
    assert c.residual_link_manifest()["link_unity"] is False
    assert c.gauge_volume_manifest()["singlet_projection"] is False


def test_covariance_release_and_request_visibility():
    assert len(c.p0_gauss_manifest()["rows"]) == 3
    assert all(row["generator_count"] == 8 for row in c.p0_gauss_manifest()["rows"])
    assert c.b0_kinematic_covariance_manifest()["rows"][0]["route_mismatch"] is False
    assert c.b0_interaction_covariance_manifest()["numerical_coefficients"] == 0
    assert c.target_ghost_separation_manifest()["cross_import"] is False
    assert c.brst_st_boundary_manifest()["BRST"] == "BRST_NOT_CONSTRUCTED"
    assert c.b0_release_manifest()["decision"] == "B0_SECTOR_RELEASED_FOR_Q0_NONZERO_MODE_CALCULATION_P0_INTERFACE_SEPARATE"
    assert c.request_resolution_manifest()["count"] == 6
    assert sum(row["active_B0"] for row in c.request_resolution_manifest()["rows"]) == 2


def test_safe_loader_and_mutations():
    assert c.load_verified_hqcd_b0ghost1_authority()["package_root"] == c.PACKAGE_ROOT
    assert c.static_isolation_guard()["pass"] is True
    for index in range(384):
        mutation = c.mutate_live_hqcdb0ghost1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
