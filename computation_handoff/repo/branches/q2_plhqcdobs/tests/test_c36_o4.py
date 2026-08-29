from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

from deuteron_wigner.bridge import o4


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
sys.path.insert(0, str(ROOT / "scripts"))
import validate_c36 as validator  # noqa: E402


def load(name: str):
    return json.loads((DOCS / name).read_text())


def test_c36_independent_validator_passes():
    env = os.environ.copy(); env["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_c36.py")], cwd=ROOT, env=env, check=True, text=True, stdout=subprocess.PIPE)
    assert result.stdout.strip() == "C36_VALIDATION_PASS"


def test_exactly_one_physical_plan_is_selected_before_coefficients():
    selection = o4.default_selection()
    assert selection.selected_family.value == o4.C36_SELECTED_PLAN
    assert sum(item.selected for item in selection.plans) == 1
    with pytest.raises(ValueError):
        replace(selection.plans[1], selected=True)


def test_spacelike_pair_and_limit_order_are_explicit():
    pair = o4.default_pair()
    assert pair.v.norm_squared < 0 and pair.vbar.norm_squared < 0
    order = o4.RapidityLimitOrder(("renormalize_UV_and_rapidity_at_finite_v_vbar", "form_soft_subtracted_TMD", "take_lightlike_rapidity_limit"), "lightlike_before_renormalization")
    assert order.ordered_limits[0].startswith("renormalize")


def test_soft_and_hadron_roots_never_share_a_probability_tensor():
    soft = o4.ReplacementSoftRoot(o4.C36_SOFT_ROOT, 0, "vacuum", "soft", "R", o4.C36_COLLINEAR_ROOT, False)
    assert soft.baryon_number == 0
    with pytest.raises(ValueError):
        replace(soft, hadron_probability_tensor_member=True)


def test_c35_defect_is_retained_and_new_spacelike_path_closes_gauge_law():
    report = o4.default_gauge_report()
    assert report.ward_residual == 0.0
    assert report.inherited_c35_ward_defect == 0.2143273
    assert load("c36_ward_benchmark.json")["c35_defect_overwritten"] is False


def test_all_twelve_c11_parent_reductions_are_exact_and_nonmatching():
    reduction = o4.c11_tree_reduction()
    assert len(reduction.rows) == 12
    assert reduction.maximum_residual == reduction.link_odd_maximum == 0.0
    assert not reduction.one_loop_matching_claimed
    assert {row["flavor"] for row in reduction.rows} == {"u", "d", "ubar", "dbar"}


def test_conversion_is_continuum_only_and_art25_independent():
    conversion = load("c36_selected_to_project_conversion.json")["conversion"]
    assert conversion["direct_to_c11_forbidden"] and conversion["art25_independent"]
    assert load("c36_conversion_roundtrip_report.json")["round_trip_residual"] == 0.0


def test_injections_and_readiness_isolation_are_complete():
    assert load("c36_injection_manifest.json")["count"] >= 2640
    gate = load("c36_continuation_gate.json")["gate"]
    assert gate["status"] == "C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY"
    assert not gate["proton_tmd_exported"] and not gate["bridge_rerun"]
