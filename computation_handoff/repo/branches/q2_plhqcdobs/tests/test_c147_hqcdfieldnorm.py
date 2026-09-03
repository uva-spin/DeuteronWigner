from deuteron_wigner.bridge.hqcdfieldnorm import core as c

Z = {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True,
     "physical_width": False}


def test_authority_and_factorization_are_authenticated():
    report = c.verify_hqcd_field_normalization_authority()
    assert report["positive_gate"] is True
    assert report["route_mismatches"] == 0
    assert report["C146_package_root"] == c.C146_ROOT
    assert c.field_normalization_plan_manifest()["selected_plan"] == "FIELDNORM-A"
    assert c.field_normalization_completeness_certificate()["positive_gate"] is True


def test_symbolic_mode_and_coordinate_sources():
    for resolution in c.RESOLUTIONS:
        long = c.longitudinal_mode_manifest(resolution)
        trans = c.transverse_mode_manifest(resolution)
        src = c.coordinate_field_source(resolution, {"x_minus": "x", "x_perp": ("x1", "x2")})
        sink = c.coordinate_field_sink(resolution, {"x_minus": "y", "x_perp": ("y1", "y2")})
        assert "(2L)^(-1/2)" in long["rows"][0]["wave"]
        assert "b_HO" in trans["rows"][0]["coordinate"]
        assert src["orientation"] == "J_R(x)=B_R C_R(x)"
        assert sink["adjoint"] is True
        assert src["qg_direct_source"] is False


def test_mode_and_coordinate_correlators_require_explicit_fixture():
    mode = c.mode_space_positive_frequency_correlator("K9", Z, fixture_id="FIXTURE-FREE")
    coord = c.coordinate_good_component_correlator(
        "K9", {"x_minus": "x", "x_perp": ("x1", "x2")},
        {"x_minus": "y", "x_perp": ("y1", "y2")}, Z,
        fixture_id="FIXTURE-FREE")
    assert mode["R_Pminus_factor"] == "2*pi*K/L"
    assert mode["negative_frequency_antiquark"] is False
    assert coord["positive_frequency_only"] is True
    try:
        c.mode_space_positive_frequency_correlator("K9", Z)
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit diagnostic fixture accepted")


def test_mutations_fail_closed():
    for i in range(384):
        mutation = c.mutate_live_hqcdfieldnorm(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
