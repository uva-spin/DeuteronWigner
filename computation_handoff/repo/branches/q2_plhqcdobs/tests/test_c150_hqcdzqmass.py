from deuteron_wigner.bridge.hqcdzqmass import core as c

SUB = {
    "schema": "C149-OFFSHELL-SUBTRACTION-RECORD-V1",
    "subtraction_id": "diagnostic-symbolic",
    "mu": "mu_FB",
    "units": "GeV",
    "kinematics": {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True, "physical_width": False},
    "state_selector": "q_source_image",
    "projector_id": "signed_mass",
    "no_default": True,
}


def test_scheme_registry_and_authority():
    assert c.kinetic_scheme_registry()["order"] == ("K_MINUS", "K_PLUS", "K_PERP")
    assert c.field_renormalization_convention()["Z_q_orientation"] == "Z_q=A_k in this declared convention"
    report = c.verify_hqcd_zq_mass_authority()
    assert report["positive_gate"] is True
    assert report["null_dimension"] == 9


def test_conditional_maps_require_all_explicit_inputs():
    for scheme in c.SCHEMES:
        zq = c.conditional_zq("K9", SUB, scheme, fixture_id="FIXTURE-FREE")
        mass = c.conditional_renormalized_mass("K9", SUB, scheme, fixture_id="FIXTURE-FREE")
        zm = c.conditional_zm("K9", SUB, scheme, fixture_id="FIXTURE-FREE")
        assert zq["value_status"] == "CONDITIONAL_NONPHYSICAL"
        assert mass["signed"] is True
        assert "UNDEFINED_NOT_0_OVER_0" in zm["chiral_point"]
    try:
        c.conditional_zq("K9", SUB, "K_MINUS")
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit numerical input accepted")


def test_restoration_conversion_and_mutations():
    rest = c.kinetic_restoration_report("K9", SUB, fixture_id="FIXTURE-FREE")
    assert rest["A_minus_A_plus_A_perp_averaged"] is False
    conv = c.internal_scheme_conversion("K9", SUB, "K_MINUS", "K_PERP", fixture_id="FIXTURE-FREE")
    assert conv["MSbar"] is False
    for i in range(384):
        m = c.mutate_live_hqcdzqmass(i)
        assert m["positive_gate"] is False
        assert m["must_fail_or_change_root"] is True
