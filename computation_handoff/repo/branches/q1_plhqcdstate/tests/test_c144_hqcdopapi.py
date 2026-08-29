from deuteron_wigner.bridge.hqcdopapi import core as c


def test_coordinate_alternatives_and_fixture_isolation():
    a = c.load_diagnostic_fixture("FIXTURE-INTERACTING-A")
    b = c.load_diagnostic_fixture("FIXTURE-INTERACTING-B-NULL-SHIFT")
    assert a["coordinates"]["phi_mass"] == b["coordinates"]["phi_mass"]
    assert a["coordinates"]["phi_coupling"] == b["coordinates"]["phi_coupling"]
    assert any(a["coordinates"][x] != b["coordinates"][x] for x in c.NULLS)
    original = c.convert_parameter_coordinates(a, c.ORIGINAL_BASIS)
    assert c.convert_parameter_coordinates(original, c.IDENTIFIED_BASIS)["coordinates"] == a["coordinates"]
    try:
        c.validate_parameter_record({"basis_tag": c.IDENTIFIED_BASIS,
                                     "coordinates": {"phi_mass": 1, "phi_coupling": 1},
                                     "claim_tier": c.CLAIM_TIER, "no_default": True,
                                     "no_physical_claim": True})
    except ValueError:
        pass
    else:
        raise AssertionError("partial null vector accepted")


def test_three_routes_and_derivatives_for_all_fixtures():
    for fixture_id in c.FIXTURE_IDS:
        record = c.load_diagnostic_fixture(fixture_id)
        for resolution in c.RESOLUTIONS:
            sparse = c.parameterized_sparse_operator(resolution, parameter_record=record)
            vector = tuple(complex((i % 7) - 3, i % 5) for i in range(c.DIMS[resolution]))
            action = c.apply_parameterized_operator(resolution, vector, parameter_record=record)
            blocks = c.parameterized_operator_blocks(resolution, parameter_record=record)
            rebuilt = [0j] * c.DIMS[resolution]
            for entries in blocks["blocks"].values():
                for row, col, value in entries:
                    rebuilt[row] += value * vector[col]
            assert tuple(rebuilt) == action
            assert sparse["dense_materialized"] is False
            for direction in c.IDENTIFIED + c.NULLS:
                derivative = c.operator_derivative(resolution, direction, parameter_record=record)
                assert derivative["direction"] == direction


def test_c144_no_implicit_fixture_or_physical_route():
    report = c.verify_hqcd_operator_authority()
    assert report["positive_gate"] is True
    assert report["implicit_fixture_calls"] == 0
    assert report["physical_values"] == 0
    assert report["counterterms_solved"] == 0
    assert report["resolvents"] == 0
    assert c.load_verified_hqcd_operator_authority()["package_root"] == c.PACKAGE_ROOT
    try:
        c.parameterized_sparse_operator("K9", parameter_record=None)
    except (TypeError, ValueError):
        pass
    else:
        raise AssertionError("missing parameter record accepted")
