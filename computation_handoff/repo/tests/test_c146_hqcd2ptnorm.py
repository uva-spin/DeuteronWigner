from deuteron_wigner.bridge.hqcd2ptnorm import core as c


def test_kinematic_relation_and_units():
    relation = c.kinematic_resolvent_relation()
    assert relation["relation"] == "R_Pminus = 2P_plus * R_M2"
    assert relation["units"]["R_M2"] == "GeV^-2"
    assert relation["units"]["R_Pminus"] == "GeV^-1"
    assert c.m2_to_pminus_resolvent_factor()["factor"] == "2P_plus"
    assert c.normalization_plan_manifest()["selected_plan"] == "NORM-C"


def test_symbolic_pminus_and_field_boundary():
    p = {"real": 0, "imaginary": 1, "units": "GeV", "analytic_query": True,
         "physical_width": False}
    out = c.source_projected_pminus_resolvent("K9", p, fixture_id="FIXTURE-FREE")
    assert out["R_Pminus_symbolic_factor"] == "2*pi*K/L"
    field = c.forward_good_component_two_point("K9", p, fixture_id="FIXTURE-FREE")
    assert field["status"] == "INCOMPLETE_SOURCE_NORMALIZATION"
    assert field["negative_frequency_antiquark"] is False
    assert c.m2_to_forward_good_component_factor()["final_net_factor"] == "UNRESOLVED_SOURCE_NORMALIZATION"


def test_c145_qualification_and_safe_report():
    q = c.c145_status_qualification()
    assert q["C145_M2_resolvent"] == "PRESERVED_POSITIVE"
    assert q["C145_good_component"] == "DESCENDANT_QUALIFIED_INCOMPLETE"
    report = c.verify_hqcd_two_point_normalization_authority()
    assert report["positive_gate"] is False
    assert report["R_M2_preserved"] is True
    assert report["physical_values"] == 0
