from deuteron_wigner.bridge.hqcdg2pt import core as c

Z = {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True, "physical_width": False}
SUB = {"schema":"C149-OFFSHELL-SUBTRACTION-RECORD-V1","subtraction_id":"diag","mu":"mu_FB","units":"GeV","kinematics":Z,"state_selector":"q_source_image","projector_id":"mass","no_default":True}


def test_free_source_and_sector_scope():
    rows = c.one_gluon_source_manifest("K9")["rows"]
    assert len(rows) == 16
    free = c.free_gluon_two_point("K9", Z, rows[0]["source_mode_id"])
    assert free["B"] == 0
    assert free["masslessness"] == "not imposed"
    assert c.pure_gluon_sector_census()["free_only"] is True


def test_spectator_response_and_amputation():
    spectator = c.spectator_qg_source_manifest("K9")["rows"][0]["spectator_id"]
    gluon = c.one_gluon_source_manifest("K9")["rows"][0]["source_mode_id"]
    response = c.spectator_tagged_qg_response("K9", Z, spectator, gluon, fixture_id="FIXTURE-FREE")
    amputated = c.quark_leg_amputated_spectator_response("K9", Z, spectator, gluon, SUB, "K_MINUS", fixture_id="FIXTURE-FREE")
    assert response["B"] == 1
    assert amputated["spectator_factorized"] is True
    assert c.spectator_factorization_report()["no_averaging"] is True


def test_conditional_za_and_explicit_inputs():
    za = c.conditional_za("K9", SUB, "K_PERP", fixture_id="FIXTURE-FREE")
    assert za["physical"] is False
    assert c.gluon_mass_like_status()["masslessness_imposed"] is False
    try:
        c.conditional_za("K9", SUB, "K_PERP")
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit numerical input accepted")


def test_mutations_and_authority():
    assert c.verify_hqcd_gluon_two_point_authority()["positive_gate"] is True
    for i in range(384):
        m = c.mutate_live_hqcdg2pt(i)
        assert m["positive_gate"] is False
        assert m["must_fail_or_change_root"] is True
