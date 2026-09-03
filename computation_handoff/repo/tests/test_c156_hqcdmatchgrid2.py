from deuteron_wigner.bridge import hqcdmatchgrid2 as c


def grid():
    r = {
        "schema":"C156-MATCHING-GRID-RECORD-V1", "matching_grid_id":"g-K9-mass",
        "resolution":"K9", "quantity_id":"SIGNED_QUARK_MASS", "perturbative_order":0,
        "C153_matching_record_id":"m1", "C153_matching_record_root":"explicit-c153-root",
        "finite_basis_scheme":"PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1",
        "target_scheme_id":"MSBAR_C43_ADAPTED", "active_Nf_record":{"N_f":4},
        "external_flavor_record":{"flavor":"u/d-external-copy-explicit"},
        "common_IR_record":{"common_ir_id":"C43_TARGET_COMMON_IR_V1"},
        "subtraction_kinematics":"spacelike-p2=-mu2", "candidate_domain_rule":"public-authority-only",
        "adaptive_refinement_rule":"log-scale-boundary-refinement", "thresholds":"C156_FROZEN_THRESHOLDS",
        "maximum_evaluations":1024, "disconnected_interval_policy":"preserve-all-components",
        "endpoint_inclusion_policy":"explicit-open-closed-enclosures", "holdout_policy":"frozen-independent",
        "claim_tier":"DIAGNOSTIC_FIXTURE_WINDOW", "no_default":True, "no_physical_claim":True,
    }
    import json, hashlib
    r["grid_record_root"] = hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
    return r


def test_schema_thresholds_and_explicit_fixture():
    g = grid()
    assert c.validate_matching_grid_record(g)["matching_grid_id"] == "g-K9-mass"
    assert len(c.gate_threshold_manifest()["rows"]) == 5
    assert c.candidate_scale_domain(g)["intervals"] == ()
    x = c.evaluate_matching_gates(g, 1.0, fixture_id="FIXTURE-FREE")
    assert x["admitted"] is False
    assert "COMMON_IR_NUMERICAL_AUTHORITY_MISSING" in x["failure_reasons"]


def test_parameter_fixture_exclusivity_and_empty_window():
    g = grid()
    try:
        c.evaluate_matching_gates(g, 1.0)
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit context accepted")
    w = c.componentwise_matching_windows(g, fixture_id="FIXTURE-INTERACTING-A")
    assert w["intervals"] == ()
    inter = c.mass_coupling_intersection(g, g, fixture_id="FIXTURE-INTERACTING-A")
    assert inter["intervals"] == ()
    assert c.flavor_window_covariance_report()["u_window_equals_d_window"] is True


def test_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        m = c.mutate_live_hqcdmatchgrid2(i)
        assert m["positive_gate"] is False and m["must_fail_or_change_root"] is True


def test_clean_reload_and_blocked_scale():
    a = c.load_verified_hqcd_matching_grid_authority()
    assert a["package_root"] == c.PACKAGE_ROOT
    assert a["next"] == "C157/HQCDMATCHIR2"
    try:
        c.validate_caller_scale("missing-window", 2.0)
    except ValueError:
        pass
    else:
        raise AssertionError("unadmitted caller scale accepted")
