from deuteron_wigner.bridge import hqcdfavor2 as c


def _mass():
    return {"scope":"ISOSYMMETRIC_MODEL_SUBSPACE","m_l":"m_ud","delta_m":"0","m_u":"m_ud","m_d":"m_ud","scheme":"MSbar","scale":"2 GeV","N_f":4,"QCD_QED":"PURE_QCD"}


def test_flavor_plan_and_crosswalk():
    assert c.STATUS == "C155_C154_SOURCE_DERIVED_ISOSYMMETRIC_UD_FLAVOR_LIFT_AND_MUD_ADAPTER_READY"
    assert c.PLAN == "FLAVOR2-B"
    assert c.available_external_flavors() == ("u", "d")
    assert c.mass_matrix_contract()["delta_m"] == "(m_d-m_u)/2"
    assert c.mud_adapter_status()["no_factor_two"] is True
    assert c.action_flavor_ledger()["count"] == 6


def test_lift_dimensions_and_round_trip():
    rows = c.flavor_lift_manifest()["rows"]
    assert [(r["lifted_q"], r["lifted_qg"], r["lifted_total"]) for r in rows] == [(12,2688,2700),(12,5400,5412),(12,9504,9516)]
    for f in ("u", "d"):
        x = c.lift_basis_id(f, "q:0")
        assert c.project_lifted_basis_id(x)["flavor_id"] == f
        assert c.project_lifted_basis_id(x)["original_basis_id"] == "q:0"
    op = c.lifted_sparse_operator("K9", _mass(), fixture_id="EXPLICIT_ISOSYMMETRIC_TEST")
    assert op["blocks"]["u_to_d"] == "EXACT_ZERO"
    assert op["matrix_materialized"] is False


def test_scope_separation_and_blocked_downstream():
    assert c.active_nf_separation_contract()["beta_function_changed"] is False
    assert c.qcd_qed_flavor_status()["charges_in_C131"] is False
    assert c.descendant_flavor_covariance_report()["full_QCD_flavor_loops"] is False
    assert c.quantum_flavor_handoff_contract()["single_flavor_Q0_unchanged"] is True


def test_isolation_mutations_and_reload():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        m = c.mutate_live_hqcdfavor2(i)
        assert m["positive_gate"] is False and m["must_fail_or_change_root"] is True
    a = c.load_verified_hqcd_flavor_authority()
    assert a["package_root"] == c.PACKAGE_ROOT
    assert a["next"] == "C156/HQCDMATCHGRID2"
