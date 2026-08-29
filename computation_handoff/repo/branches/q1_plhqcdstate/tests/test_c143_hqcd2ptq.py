from deuteron_wigner.bridge.hqcd2ptq import core as c


def test_c143_fail_closed_authority_and_source_shapes():
    report = c.verify_hqcd_two_pointq_authority()
    assert report["status"] == c.STATUS
    assert report["positive_gate"] is False
    assert report["parameter_records"] == 0
    assert report["null_coordinates_set_to_zero"] == 0
    for resolution, dimension in c.DIMS.items():
        embedding = c.source_embedding(resolution)
        assert embedding["shape"] == (dimension, 6)
        assert embedding["matrix"][:6] == ((1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0),
                                             (0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0),
                                             (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1))
        assert all(row == (0, 0, 0, 0, 0, 0) for row in embedding["matrix"][6:])


def test_c143_parameter_schema_has_no_defaults():
    schema = c.parameter_record_schema()
    assert schema["required_count"] == 19
    assert schema["no_defaults"] is True
    assert all(field["no_default"] is True for field in schema["fields"])
    try:
        c.validate_parameter_record({})
    except ValueError as exc:
        assert "missing" in str(exc)
    else:
        raise AssertionError("incomplete parameter record was accepted")


def test_c143_spectral_and_numerical_routes_fail_closed():
    z = {"real": "z", "imaginary": "eta", "units": "GeV^2",
         "analytic_query": True, "physical_width": False}
    try:
        c.source_projected_resolvent("K9", z)
    except ValueError as exc:
        assert "parameter record" in str(exc)
    else:
        raise AssertionError("resolvent route did not fail closed")
    try:
        c.spectral_variable({"real": 1, "imaginary": 0, "units": "GeV^2",
                             "analytic_query": True, "physical_width": True})
    except ValueError:
        pass
    else:
        raise AssertionError("physical-width interpretation was accepted")
    assert c.static_isolation_guard()["C80_calls"] == 0
    assert c.mutate_live_hqcd2ptq(383)["positive_gate"] is False
