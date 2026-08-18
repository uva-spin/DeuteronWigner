from deuteron_wigner.bridge.hqcd2ptq2 import core as c


Z = {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True,
     "physical_width": False}


def test_fixture_scoped_three_route_resolvent():
    for fixture_id in c.FIXTURES:
        direct = c.source_projected_m2_resolvent("K9", Z, fixture_id=fixture_id, route="direct")
        block = c.source_projected_m2_resolvent("K9", Z, fixture_id=fixture_id, route="block")
        free = c.source_projected_m2_resolvent("K9", Z, fixture_id=fixture_id, route="matrix_free")
        assert max(abs(direct["matrix"][i][j] - block["matrix"][i][j]) for i in range(6) for j in range(6)) < 1e-8
        assert max(abs(direct["matrix"][i][j] - free["matrix"][i][j]) for i in range(6) for j in range(6)) < 1e-8
        assert direct["diagnostics"]["dense_full_inverse"] is False


def test_fixture_argument_is_exactly_one_and_identities():
    try:
        c.source_projected_m2_resolvent("K9", Z)
    except ValueError:
        pass
    else:
        raise AssertionError("missing fixture/record accepted")
    record = c.op.load_diagnostic_fixture("FIXTURE-INTERACTING-A")
    try:
        c.source_projected_m2_resolvent("K9", Z, parameter_record=record, fixture_id="FIXTURE-FREE")
    except ValueError:
        pass
    else:
        raise AssertionError("both fixture and record accepted")
    assert c.null_shift_diagnostic()["identified_coordinates_equal"] is True
    assert c.mass_sign_diagnostic()["signed_short_distance_mass_inferred"] is False
    assert c.mass_projector_status()["constructed"] is False


def test_conversion_self_energy_and_safe_authority():
    out = c.forward_good_component_two_point("K9", Z, fixture_id="FIXTURE-INTERACTING-A")
    assert out["P_plus"] == "pi*K/L"
    assert out["negative_frequency_antiquark"] is False
    assert c.retained_qg_self_energy("K9", Z, fixture_id="FIXTURE-INTERACTING-A")["omitted_interfaces_excluded"] is True
    report = c.verify_hqcd_forward_two_point_authority()
    assert report["positive_gate"] is True
    assert report["physical_poles"] == 0
