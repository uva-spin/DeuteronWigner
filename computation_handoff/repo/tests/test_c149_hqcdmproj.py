from deuteron_wigner.bridge.hqcdmproj import core as c

SUB = {
    "schema": "C149-OFFSHELL-SUBTRACTION-RECORD-V1",
    "subtraction_id": "diagnostic-symbolic",
    "mu": "mu_FB",
    "units": "GeV",
    "kinematics": {"real": 0, "imaginary": 1, "units": "GeV^2",
                   "analytic_query": True, "physical_width": False},
    "state_selector": "q_source_image",
    "projector_id": "signed_mass",
    "no_default": True,
}


def test_schema_and_authority():
    assert c.validate_subtraction_record(SUB)["no_default"] is True
    report = c.verify_hqcd_mass_projector_authority()
    assert report["positive_gate"] is True
    assert report["tensor_rank"] == 8
    assert report["null_dimension"] == 9
    assert c.projector_completeness_certificate()["route_mismatches"] == 0


def test_inverse_routes_and_projectors():
    records = [c.inverse_two_point("K9", SUB, fixture_id="FIXTURE-FREE", route=r)
               for r in ("direct", "block", "matrix_free", "eom")]
    for rec in records:
        assert rec["schur_hamiltonian"] is False
        assert c.apply_mass_projector(rec)["mass_response"] == 1
        assert c.apply_kinetic_projector(rec, "pminus_kinetic")["response"] == 1
    assert c.tensor_gram_manifest("K9")["rows"][0]["rank"] == 8


def test_no_implicit_inputs_and_conditional_handoff():
    try:
        c.inverse_two_point("K9", SUB, fixture_id="FIXTURE-FREE", parameter_record={})
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("mixed parameter inputs accepted")
    assert c.conditional_renormalization_interface()["physical_Z_q"] is False
    assert c.mass_sign_projector_report()["physical_mass"] is False


def test_mutations():
    for i in range(384):
        m = c.mutate_live_hqcdmproj(i)
        assert m["positive_gate"] is False
        assert m["must_fail_or_change_root"] is True
