"""Tracked C157 regression surface derived from committed authority records.

The similarly named untracked inherited file is retained as provenance only;
this file is the official corrected replacement for C160.
"""
import json
from pathlib import Path

from deuteron_wigner.bridge import hqcdmatchir2 as c157
from deuteron_wigner.bridge import hqcdfbnum as c158


ROOT = Path(__file__).resolve().parents[1]


def _json(name):
    return json.loads((ROOT / "docs/next_level" / name).read_text())


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
    record["grid_record_root"] = hashlib.sha256(
        json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()
    return record


def test_contract_and_fail_closed_gates():
    c157_plan = c157.matchir_plan_manifest()
    decision = _json("c157_matchir_plan_decision.json")
    continuation = _json("c157_matching_grid_rerun_contract.json")
    c158_contract = _json("c157_c158_hqcdfbnum_continuation_contract.json")
    assert c157_plan["selected_plan"] == decision["selected"] == "MATCHIR2-B"
    assert c157_plan["status"] == "C157_HQCDMATCHIR2_FINITE_BASIS_NUMERICAL_INCOMPLETE"
    assert c157_plan["first_remaining_object"] == "FINITE_BASIS_NUMERICAL_EVALUATOR"
    assert continuation["next"] == c158_contract["branch"] == "C158/HQCDFBNUM"
    assert c157_plan["selected_plan"] != "MATCHIR2-D"
    assert c158.verify_hqcd_fbnum_authority()["status"] == c158.STATUS
    assert c158.fbnum_completeness_certificate()["public_C144_polynomial_consumed"] is True
    g = grid()
    common = c157.common_ir_gate_report(g, 1.0, fixture_id="FIXTURE-FREE")
    remainder = c157.perturbative_remainder_report(g, 1.0, fixture_id="FIXTURE-FREE")
    assert common["admitted"] is False
    assert remainder["admitted"] is False
    combined = c157.evaluate_matching_ir_gates(g, 1.0, fixture_id="FIXTURE-FREE")
    assert combined["admitted"] is False
    assert combined["common_ir"]["common_ir_residual"] is None


def test_explicit_context_and_empty_windows():
    g = grid()
    try:
        c157.evaluate_matching_ir_gates(g, 1.0)
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("implicit matching context accepted")
    assert c157.candidate_scale_domain(g)["intervals"] == ()
    window = c157.componentwise_matching_window(g, fixture_id="FIXTURE-INTERACTING-A")
    assert window["intervals"] == ()
    cross = c157.cross_resolution_window_report({x: "empty" for x in ("K9", "K11", "K13")})
    assert cross["intersection"] == ()


def test_isolation_mutations_and_reload():
    assert c157.static_isolation_guard()["pass"] is True
    for i in range(384):
        mutation = c157.mutate_live_hqcdmatchir2(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
    authority = c157.load_verified_hqcd_matching_ir_authority()
    assert authority["package_root"] == c157.PACKAGE_ROOT
    assert authority["next"] == "C158/HQCDFBNUM"
    c159_report = _json("c159_regression_report.json")
    assert c159_report["next"] == "C160/HQCDFBTEST"
    assert "C158/HQCDMATCHWINDOW2" not in c159_report["next"]
