from deuteron_wigner.bridge.hqcd2ptfull import core as c

Z = {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True,
     "physical_width": False}
COORD = {"x_minus": "x", "x_perp": ("x1", "x2")}


def test_authority_and_constraint_manifests():
    report = c.verify_hqcd_full_spinor_authority()
    assert report["positive_gate"] is True
    assert report["route_A_mismatches"] == report["route_D_mismatches"] == 0
    assert c.constraint_factorization_manifest()["root"]
    assert c.inverse_partial_plus_manifest()["rows"]
    assert c.full_spinor_completeness_certificate()["positive_gate"] is True


def test_four_blocks_and_all_routes():
    for route in ("direct", "block", "matrix_free", "constraint"):
        out = c.full_spinor_blocks("K9", COORD, COORD, Z,
                                   fixture_id="FIXTURE-FREE", route=route)
        assert tuple(out["blocks"]) == ("++", "-+", "+-", "--")
        assert out["S_plus_plus_reproduces_C147"] is True
        assert all(v["status"] == "AVAILABLE_SOURCE_QUALIFIED" for v in out["blocks"].values())


def test_explicit_fixture_and_mass_linear_scope():
    block = c.full_spinor_block("-", "+", "K9", COORD, COORD, Z,
                                fixture_id="FIXTURE-INTERACTING-A")
    assert block["component"] == "-+"
    assert c.mass_linear_structure_manifest()["signed_mass"] == "m_q (not m_q^2)"
    assert c.mass_projector_readiness_report()["mass_projector_created"] is False
    try:
        c.constraint_residual_report("K9")
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit fixture accepted")


def test_scope_and_mutations():
    assert c.mass_sign_sensitivity_report()["physical_mass_inferred"] is False
    assert c.instantaneous_contact_ledger()["double_counting"] == 0
    assert c.spinor_tensor_decomposition()["components"] == ("++", "-+", "+-", "--")
    for i in range(384):
        m = c.mutate_live_hqcd2ptfull(i)
        assert m["positive_gate"] is False
        assert m["must_fail_or_change_root"] is True
