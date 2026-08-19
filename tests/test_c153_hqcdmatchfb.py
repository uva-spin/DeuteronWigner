from deuteron_wigner.bridge.hqcdmatchfb import core as c

REC = {
    "schema": "C153-MATCHING-RECORD-V1", "matching_id": "m1", "quantity_id": "qg_vertex",
    "finite_basis_scheme": "PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1",
    "target_scheme_id": "PROJECT_LIGHT_FRONT_NONEXCEPTIONAL", "order": 1,
    "gauge": "C43 A_plus=0", "N_f": 3, "mu": "mu_match",
    "kinematics": "nonexceptional-symbolic", "common_ir_id": "C43_TARGET_COMMON_IR_V1",
    "no_default": True,
}


def test_matching_schema_and_sources():
    assert c.validate_matching_record(REC)["common_ir_id"] == "C43_TARGET_COMMON_IR_V1"
    assert len(c.primary_source_manifest()["rows"]) == 6
    assert len(c.target_scheme_registry()["rows"]) == 5
    assert c.matching_completeness_certificate()["positive_gate"] is True


def test_conversion_routes_and_scope():
    for route in ("derivative", "spectral", "owner", "holdout"):
        x = c.finite_basis_perturbative_coefficient("qg_vertex", REC, fixture_id="FIXTURE-FREE", route=route)
        assert x["physical"] is False
    conv = c.conversion_factor("qg_vertex", REC, fixture_id="FIXTURE-FREE")
    inv = c.inverse_conversion_factor("qg_vertex", REC, fixture_id="FIXTURE-FREE")
    assert conv["common_ir_cancelled"] is True
    assert inv["schema"] == "C153-INVERSE-CONVERSION-FACTOR-V1"
    assert c.regulator_trajectory_report()["continuum_extrapolation"] is False


def test_explicit_inputs_and_mutations():
    try: c.conversion_factor("qg_vertex", REC)
    except ValueError as exc: assert "exactly one" in str(exc)
    else: raise AssertionError("implicit input accepted")
    assert c.verify_hqcd_matching_authority()["positive_gate"] is True
    for i in range(384):
        m = c.mutate_live_hqcdmatchfb(i)
        assert m["positive_gate"] is False and m["must_fail_or_change_root"] is True
