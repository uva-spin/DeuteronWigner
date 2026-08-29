from deuteron_wigner.bridge import hqcdmatchir2 as c


def grid():
    record = {
        "schema": "C156-MATCHING-GRID-RECORD-V1",
        "matching_grid_id": "g-K9-mass",
        "resolution": "K9",
        "quantity_id": "SIGNED_QUARK_MASS",
        "perturbative_order": 0,
        "C153_matching_record_id": "m1",
        "C153_matching_record_root": "explicit-c153-root",
        "finite_basis_scheme": "PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1",
        "target_scheme_id": "MSBAR_C43_ADAPTED",
        "active_Nf_record": {"N_f": 4},
        "external_flavor_record": {"flavor": "u/d-external-copy-explicit"},
        "common_IR_record": {"common_ir_id": "C43_TARGET_COMMON_IR_V1"},
        "subtraction_kinematics": "spacelike-p2=-mu2",
        "candidate_domain_rule": "public-authority-only",
        "adaptive_refinement_rule": "log-scale-boundary-refinement",
        "thresholds": "C157_FROZEN_THRESHOLDS",
        "maximum_evaluations": 1024,
        "disconnected_interval_policy": "preserve-all-components",
        "endpoint_inclusion_policy": "explicit-open-closed-enclosures",
        "holdout_policy": "frozen-independent",
        "claim_tier": "DIAGNOSTIC_FIXTURE_WINDOW",
        "no_default": True,
        "no_physical_claim": True,
    }
    import hashlib
    import json
    record["grid_record_root"] = hashlib.sha256(
        json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()
    return record


def test_contract_and_fail_closed_gates():
    assert c.PLAN == "MATCHIR2-D"
    assert c.numerical_evidence_schema()["numeric_fields_are_required"] is True
    g = grid()
    common = c.common_ir_gate_report(g, 1.0, fixture_id="FIXTURE-FREE")
    remainder = c.perturbative_remainder_report(g, 1.0, fixture_id="FIXTURE-FREE")
    assert common["admitted"] is False
    assert remainder["admitted"] is False
    combined = c.evaluate_matching_ir_gates(g, 1.0, fixture_id="FIXTURE-FREE")
    assert combined["admitted"] is False
    assert combined["common_ir"]["common_ir_residual"] is None


def test_explicit_context_and_empty_windows():
    g = grid()
    try:
        c.evaluate_matching_ir_gates(g, 1.0)
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit matching context accepted")
    assert c.candidate_scale_domain(g)["intervals"] == ()
    window = c.componentwise_matching_window(g, fixture_id="FIXTURE-INTERACTING-A")
    assert window["intervals"] == ()
    cross = c.cross_resolution_window_report({x: "empty" for x in ("K9", "K11", "K13")})
    assert cross["intersection"] == ()


def test_isolation_mutations_and_reload():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        mutation = c.mutate_live_hqcdmatchir2(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
    authority = c.load_verified_hqcd_matching_ir_authority()
    assert authority["package_root"] == c.PACKAGE_ROOT
    assert authority["next"] == "C158/HQCDMATCHWINDOW2"

