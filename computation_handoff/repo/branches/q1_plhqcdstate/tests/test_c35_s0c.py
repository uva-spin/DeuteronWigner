from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys

import pytest

from deuteron_wigner.bridge import s0c as c35_arch
from deuteron_wigner.bridge.s0c import core as c35


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
sys.path.insert(0, str(ROOT / "scripts"))
import validate_c35 as validator  # noqa: E402


def load(name: str):
    return json.loads((DOCS / name).read_text())


def test_c35_independent_validator_passes():
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_c35.py")],
        cwd=ROOT,
        env=environment,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.stdout.strip() == "C35_VALIDATION_PASS"


def test_all_53_architecture_types_are_real_frozen_content_addressed_objects():
    validator.validate_architecture()
    examples = c35_arch.architecture_examples()
    first = examples[validator.EXPECTED_ARCHITECTURE_NAMES[0]]
    field = next(item.name for item in first.__dataclass_fields__.values())
    with pytest.raises(FrozenInstanceError):
        setattr(first, field, "MUTATED")


def test_identity_envelopes_reject_root_and_scope_leakage():
    envelope = next(iter(c35_arch.architecture_examples().values())).identity
    with pytest.raises(ValueError):
        replace(envelope, baryon_number=1)
    with pytest.raises(ValueError):
        replace(envelope, c33_b0_root=c35.C32_COLLINEAR_ROOT)
    for field, wrong_commit in (
        ("c34_completion_commit", "0" * 40),
        ("c33_completion_commit", "1" * 40),
        ("c32_completion_commit", "2" * 40),
        ("c28_scientific_ancestor", "3" * 40),
    ):
        with pytest.raises(ValueError):
            replace(envelope, **{field: wrong_commit})
    with pytest.raises(ValueError):
        replace(envelope, gauge_plan_id="UNDECLARED_GAUGE_PLAN")
    for field in (
        "process_reachable",
        "bridge_reachable",
        "inference_reachable",
        "production_reachable",
    ):
        with pytest.raises(ValueError):
            replace(envelope, **{field: True})


def test_general_types_represent_evidence_qualified_future_states():
    candidate = c35.GaugePlanCandidate(
        "C35.TEST.VALIDATED.COVARIANT",
        c35.GaugePlanKind.COVARIANT_KREIN,
        True,
        True,
        True,
        ("C35.TEST.REGULATOR_IDENTICAL_EVIDENCE",),
        (),
        True,
    )
    assert candidate.coefficient_execution_allowed and not candidate.blockers
    bare = c35.SoftBareOneLoopResult(
        "C35.TEST.BARE",
        1.0,
        0.125,
        "CALCULATED_NONZERO",
        "TEST_EVIDENCE_QUALIFIED_CONVENTION",
        True,
        False,
    )
    assert bare.all_required_slots_resolved and bare.one_loop_value == 0.125
    counterterms = c35.SoftCountertermSystem(
        "C35.TEST.COUNTERTERMS",
        True,
        -0.1,
        0.2,
        0.0,
        "EVIDENCE_QUALIFIED_TEST_STATE",
    )
    assert counterterms.bare_coefficient_available


def test_nonapplicability_requires_selected_gauge_action_proof():
    with pytest.raises(ValueError):
        c35.SoftContributionResult(
            "C35.TEST.NA",
            c35.REQUIRED_ONE_LOOP_CONTRIBUTIONS[0],
            c35.ContributionStatus.NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF,
            "NOT_APPLICABLE",
            False,
            "NO_MISSING_CALCULATION_AFTER_PROOF",
            None,
        )
    proved = c35.SoftContributionResult(
        "C35.TEST.NA.PROVED",
        c35.REQUIRED_ONE_LOOP_CONTRIBUTIONS[0],
        c35.ContributionStatus.NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF,
        "NOT_APPLICABLE",
        False,
        "NO_MISSING_CALCULATION_AFTER_PROOF",
        "C35.TEST.SELECTED_GAUGE_ACTION_PROOF",
    )
    assert not proved.blocking


def test_default_branch_is_unavailable_and_never_attempts_a_coefficient():
    validator.validate_branch_g()


def test_light_front_vectors_components_and_rescaling_are_exact():
    validator.validate_conventions_and_oracles()
    formal = c35_arch.architecture_examples()["LightFrontConvention"]
    root_two = math.sqrt(2.0)
    expected_n = (1.0 / root_two, 0.0, 0.0, 1.0 / root_two)
    expected_nbar = (1.0 / root_two, 0.0, 0.0, -1.0 / root_two)
    assert all(
        math.isclose(value, expected, rel_tol=0.0, abs_tol=1.0e-15)
        for value, expected in zip(formal.n_components, expected_n)
    )
    assert all(
        math.isclose(value, expected, rel_tol=0.0, abs_tol=1.0e-15)
        for value, expected in zip(formal.nbar_components, expected_nbar)
    )
    assert formal.k_plus_projection == "nbar.k"
    assert formal.k_minus_projection == "n.k"
    with pytest.raises(ValueError):
        replace(formal, n_components=formal.nbar_components)


def test_real_chart_is_on_shell_and_virtual_chart_remains_off_shell():
    real = c35.RealSoftCoordinateChart()
    virtual = c35.VirtualSoftCoordinateChart()
    point = real.map(2.3, 0.37, 1.2)
    assert abs(real.mass_shell_residual(point)) < 3.0e-14
    assert virtual.invariant((1.0, 1.0, 0.0, 0.0)) == 2.0
    assert virtual.contour_status.startswith("UNRESOLVED_BLOCKING")
    report = load("c35_real_virtual_measure_report.json")
    assert report["measures_aliased"] is False
    assert report["real_on_shell"] and report["virtual_off_shell"]


def test_modified_delta_is_not_misrepresented_as_finite_delta_gauge_complete():
    operator = c35.ModifiedDeltaDampingOperator()
    assert not operator.gauge_property_at_finite_delta
    assert operator.gauge_property_restored_only_in_delta_limit
    manifest = load("c35_modified_delta_operator.json")
    assert manifest["gauge_property_at_finite_delta"] is False
    assert manifest["gauge_property_restored_only_in_delta_limit"] is True
    selection = load("c35_gauge_complete_plan_selection.json")
    assert selection["selected"] == "S0C-UNAVAILABLE"


@pytest.mark.parametrize("pole_sign", (-1, 1))
def test_singular_cell_oracle_matches_the_controlled_distributional_limit(pole_sign):
    oracle = c35.SingularCellOracle()
    expected = oracle.distributional_constant(-2.0, 3.0, pole_sign=pole_sign)
    finite = oracle.finite_delta_constant(-2.0, 3.0, 1.0e-10, pole_sign=pole_sign)
    assert abs(expected - finite) < 2.0e-10
    assert math.isclose(expected.real, math.log(3.0 / 2.0))
    assert math.isclose(expected.imag, pole_sign * math.pi)


def test_cell_center_sampling_is_forbidden_and_no_physical_cell_was_executed():
    oracle = c35.SingularCellOracle()
    assert oracle.center_sampling_forbidden
    assert oracle.physical_cells_executed == 0
    report = load("c35_singular_cell_subtraction_report.json")
    assert report["center_sampling_used"] is False
    assert report["physical_singular_cell_executed"] is False


def test_all_18_contributions_remain_explicit_empty_not_zero_blockers():
    ledger = c35.fail_closed_contribution_ledger()
    assert tuple(row.contribution_class for row in ledger) == c35.REQUIRED_ONE_LOOP_CONTRIBUTIONS
    assert all(row.expression == c35.NONZERO_UNKNOWN for row in ledger)
    assert all(row.blocking for row in ledger)
    manifest = load("c35_soft_diagram_results.json")
    assert manifest["count"] == len(manifest["records"]) == 18
    assert manifest["all_slots_nonzero_unknown"] and not manifest["all_slots_resolved"]
    assert all(row["expression"] == c35.NONZERO_UNKNOWN for row in manifest["records"])


def test_counterterms_cannot_be_solved_before_the_bare_coefficient():
    with pytest.raises(ValueError, match="COUNTERTERM_SOLVED_BEFORE_BARE_COEFFICIENT"):
        c35.SoftCountertermSystem(
            "C35.TEST.ILLEGAL.CT",
            False,
            0.0,
            None,
            None,
            "ILLEGAL",
        )
    result = load("c35_soft_counterterm_results.json")
    assert not result["bare_coefficient_available"]
    assert not result["counterterm_solved_before_bare"]
    assert result["records"] and all(row["value"] is None for row in result["records"])


def test_no_continuum_coefficient_is_substituted_for_the_finite_basis_result():
    bare = load("c35_bare_soft_coefficient.json")
    assert bare["one_loop_value"] is None
    assert bare["one_loop_status"] == c35.NONZERO_UNKNOWN
    assert bare["continuum_substituted"] is False
    continuum = load("c35_continuum_soft_reconstruction.json")
    assert continuum["source_transcription_present"]
    assert not continuum["finite_basis_result"]
    assert not continuum["graph_level_reconstruction"]


def test_exact_61_json_and_four_markdown_deliverables_are_content_addressed():
    validator.validate_deliverables()


def test_exact_326_coverage_rows_and_kind_counts():
    coverage = load("c35_requirement_coverage.json")
    assert coverage["count"] == 326
    counts = {}
    for row in coverage["rows"]:
        counts[row["kind"]] = counts.get(row["kind"], 0) + 1
    assert counts == validator.EXPECTED_KIND_COUNTS


def test_all_93_fault_modes_have_semantically_targeted_executed_injections():
    validator.validate_injections()


def test_injection_payload_hash_and_target_tampering_fail_closed():
    row = load("c35_injection_manifest.json")["rows"][0]
    payload = dict(row["mutation_payload"])
    with pytest.raises(ValueError, match="PAYLOAD_HASH_MISMATCH"):
        c35.execute_injection_payload(payload, "0" * 64)
    payload["semantic_target_id"] = "C35.UNKNOWN.TARGET"
    with pytest.raises(ValueError):
        c35.execute_injection_payload(payload)


def test_27_holdouts_are_frozen_and_never_used_for_selection_or_fit():
    report = load("c35_holdout_report.json")
    assert report["count"] == len(c35.HOLDOUT_IDS) == 27
    assert [row["holdout_id"] for row in report["rows"]] == list(c35.HOLDOUT_IDS)
    assert report["all_frozen"] and not report["failed_holdout_moved_to_construction"]
    assert all(row["frozen_before_plan_selection"] for row in report["rows"])
    assert all(not row["used_in_selection"] and not row["used_in_fit"] for row in report["rows"])


def test_regression_locks_registry_artifacts_members_and_covariance():
    validator.validate_regression_isolation()


def test_no_joint_measure_and_empty_projection_are_preserved():
    contract = load("c35_soft_collinear_continuation_contract.json")
    assert contract["cross_root_relation"] == "NO_JOINT_MEASURE"
    assert contract["shared_state"] is False
    assert contract["exact_conversion"] is None
    gate = load("c35_c32_continuation_gate.json")
    assert gate["microscopic_proton_export"] == {
        "shape": [0], "values": None, "status": c35.EMPTY_NOT_ZERO,
    }
    assert gate["bridge_rerun_executed"] is False


def test_runtime_entrypoint_writes_only_an_ignored_content_addressed_no_go_bundle():
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_c35_soft_calculation.py")],
        cwd=ROOT,
        env=environment,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    prefix = "C35_BRANCH_G_RUNTIME_BUNDLE_PASS "
    assert result.stdout.startswith(prefix)
    relative = result.stdout.strip()[len(prefix):]
    path = ROOT / relative
    record = json.loads(path.read_text())
    digest = record.pop("content_hash")
    assert digest == path.parent.name == validator.canonical_hash(record)
    assert record["finite_basis_one_loop"] == {
        "value": None,
        "value_semantics": c35.NONZERO_UNKNOWN,
        "coefficient_issued": False,
        "continuum_coefficient_substituted": False,
    }
    assert len(record["contributions"]) == 18
    assert all(row["value"] is None for row in record["contributions"])
    ignored = subprocess.run(
        ("git", "check-ignore", "--quiet", "--", relative), cwd=ROOT, check=False
    )
    assert ignored.returncode == 0


def test_runtime_entrypoint_rejects_output_outside_the_ignored_runtime_root(tmp_path):
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "run_c35_soft_calculation.py"),
            "--runtime-root",
            str(tmp_path),
        ],
        cwd=ROOT,
        env=environment,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode != 0
    assert "C35_RUNTIME_OUTPUT_MUST_REMAIN_UNDER_DATA_RUNTIME" in result.stderr


def test_manifest_builder_regenerates_byte_identically():
    before = {name: hashlib.sha256((DOCS / name).read_bytes()).hexdigest() for name in validator.JSON_DELIVERABLES}
    final_tests = load("c35_regression_report.json")["final_tests"]
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_c35_manifests.py"),
            str(final_tests),
        ],
        cwd=ROOT,
        env=environment,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.stdout.strip() == "C35_MANIFEST_BUILD_PASS"
    after = {name: hashlib.sha256((DOCS / name).read_bytes()).hexdigest() for name in validator.JSON_DELIVERABLES}
    assert after == before


def test_msht20_rep_remains_untracked_and_outside_git():
    tracked = subprocess.check_output(("git", "ls-files", "MSHT20_REP"), cwd=ROOT, text=True)
    assert tracked.strip() == ""
