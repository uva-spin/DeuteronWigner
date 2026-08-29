#!/usr/bin/env python3
"""Independent fail-closed validator for the C35/S0C package.

This validator deliberately does not calculate a soft coefficient.  It checks
that the C35 package records the supported Branch-G result without weakening
the regulator, changing an inherited result, or leaking an unavailable object
into the proton, bridge, inference, or production graphs.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import is_dataclass
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path
from typing import Any, Iterable, Mapping

from deuteron_wigner.bridge import s0c as c35_arch
from deuteron_wigner.bridge.s0c import core as c35


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
PROMPT = DOCS / "c35_s0c_codex_prompt.md"
VOLUME_XXI = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"

PROMPT_SHA256 = "1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"
C34_REPORT_SHA256 = "aa66b448518dd493ae237822712c15ea160a73aa9cc5257df59fb83722f7ebe1"
C34_COVERAGE_SHA256 = "0a94dfd213bd67ea6f4da498ff0095f38136d5a68c89b0c0ae3d30febb610d5e"


JSON_DELIVERABLES = (
    "c35_requirement_coverage.json",
    "c35_normative_source_integration.json",
    "c35_volume_xxi_requirement_crosswalk.json",
    "c35_primary_source_manifest.json",
    "c35_derivation_authority_manifest.json",
    "c35_gauge_complete_plan_manifest.json",
    "c35_gauge_complete_plan_selection.json",
    "c35_light_front_convention.json",
    "c35_null_vector_regulator_rescaling.json",
    "c35_real_coordinate_chart.json",
    "c35_virtual_coordinate_chart.json",
    "c35_real_virtual_measure_report.json",
    "c35_soft_mode_collection_manifest.json",
    "c35_soft_mode_normalization_report.json",
    "c35_soft_partition_of_unity_report.json",
    "c35_refinement_map_manifest.json",
    "c35_factorized_regulator_grid.json",
    "c35_trajectory_identifiability_report.json",
    "c35_soft_free_action.json",
    "c35_soft_mode_metric.json",
    "c35_brst_constraint_or_instantaneous_report.json",
    "c35_wilson_segment_parameterization.json",
    "c35_transverse_infinity_segment.json",
    "c35_line_to_pole_derivation_report.json",
    "c35_modified_delta_operator.json",
    "c35_modified_delta_mode_action_report.json",
    "c35_pole_cell_partition.json",
    "c35_singular_cell_subtraction_report.json",
    "c35_virtual_contour_report.json",
    "c35_executable_eikonal_vertex.json",
    "c35_line_pair_kernel_library.json",
    "c35_vertex_ward_report.json",
    "c35_soft_diagram_results.json",
    "c35_soft_counterterm_results.json",
    "c35_contribution_closure_matrix.json",
    "c35_real_virtual_assembly.json",
    "c35_bare_soft_coefficient.json",
    "c35_bare_soft_validation_report.json",
    "c35_continuum_soft_reconstruction.json",
    "c35_continuum_oracle_two_route_report.json",
    "c35_soft_uv_counterterm_solution.json",
    "c35_soft_rapidity_counterterm_solution.json",
    "c35_soft_renormalization_closure.json",
    "c35_soft_regulator_conversion.json",
    "c35_soft_regulator_roundtrip.json",
    "c35_soft_trajectory_report.json",
    "c35_zero_mode_sector.json",
    "c35_zero_mode_closure_report.json",
    "c35_boundary_endpoint_report.json",
    "c35_soft_side_zero_bin_limit.json",
    "c35_soft_collinear_continuation_contract.json",
    "c35_c32_continuation_gate.json",
    "c35_soft_tensor_network_execution.json",
    "c35_soft_quantum_interface_update.json",
    "c35_soft_uncertainty_budget.json",
    "c35_soft_remainder_separation.json",
    "c35_source_sufficiency_decision.json",
    "c35_no_go_decision_tree.json",
    "c35_holdout_report.json",
    "c35_injection_manifest.json",
    "c35_regression_report.json",
)

MARKDOWN_DELIVERABLES = (
    "c35_implementation_report.md",
    "c35_api.md",
    "c35_missing_calculation_specification.md",
    "c35_unresolved_physics_gaps.md",
)

EXPECTED_ARCHITECTURE_NAMES = (
    "GaugeCompleteSoftPlan", "CovariantKreinPlan", "LightFrontPhysicalPlan",
    "GaugePlanSupersession", "LightFrontConvention", "NullVectorNormalization",
    "RapidityRegulatorRescaling", "SoftCoordinateChart", "RealSoftCoordinateChart",
    "VirtualSoftCoordinateChart", "SoftJacobian", "SoftCell", "SoftCellBoundary",
    "SoftCellShape", "SoftCellMeasure", "SoftCellQuadrature",
    "SoftPartitionOfUnity", "SoftRefinementMap", "SoftModeCollection",
    "SoftGaugeMode", "SoftPolarizationMetric", "SoftGhostMode", "SoftAuxiliaryMode",
    "SoftInstantaneousKernel", "SoftFreeAction", "SoftFreeHamiltonian",
    "RealCutMeasure", "VirtualLoopMeasure", "VirtualContourPlan", "PoleCellPartition",
    "SingularCellSubtraction", "WilsonSegmentParameterization",
    "LongitudinalWilsonSegment", "TransverseInfinitySegment",
    "ModifiedDeltaDampingOperator", "FiniteSegmentLimit", "ExecutableEikonalVertex",
    "ExecutableLinePairKernel", "ExecutableSelfKernel", "ExecutableCuspKernel",
    "ExecutableBoundaryKernel", "SoftZeroModeSector", "SoftBoundarySector",
    "SoftBRSTOrConstraintReport", "SoftBareOneLoopResult", "SoftCountertermSystem",
    "SoftRenormalizedOneLoopResult", "SoftTrajectoryFamily", "SoftTrajectoryAxis",
    "SoftTrajectoryResult", "SoftSideOverlapObject", "C35CapabilityMatrix",
    "C35ClosureReport",
)

EXPECTED_KIND_COUNTS = {
    "ACCEPTANCE_CRITERION": 52,
    "BENCHMARK_FAMILY": 18,
    "REQUIRED_ARCHITECTURE_OBJECT": 53,
    "ONE_LOOP_CONTRIBUTION_SLOT": 18,
    "FROZEN_HOLDOUT": 27,
    "VOLUME_XXI_REQUIREMENT": 65,
    "NEGATIVE_FAULT_MODE": 93,
}

FORBIDDEN_ISSUED_STATUSES = {
    "C35_MICROSCOPIC_PROTON_TMD_EXPORTED",
    "BRIDGE_DISTRIBUTION_COMPARISON_READY",
    "MICROSCOPIC_MODEL_CALIBRATED",
    "ART25_CONSTRAINED_MICROSCOPIC_POSTERIOR",
    "GLOBAL_LIKELIHOOD_READY",
    "GLOBAL_INFERENCE_READY",
    "REPLICA_REWEIGHTED",
    "PROCESS_PREDICTION_READY",
    "DEUTERON_PREDICTION_READY",
    "PRODUCTION_READY",
}


def load(name: str) -> dict[str, Any]:
    return json.loads((DOCS / name).read_text())


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def assert_content_address(name: str) -> None:
    payload = load(name)
    assert isinstance(payload.get("content_hash"), str), name
    recorded = payload.pop("content_hash")
    assert recorded == canonical_hash(payload), name


def prompt_acceptance_rows() -> list[tuple[int, str]]:
    text = PROMPT.read_text()
    section = text.split("# 33. Acceptance criteria", 1)[1].split(
        "# 34. Outcome branches", 1
    )[0]
    rows = [
        (int(match.group(1)), match.group(2))
        for line in section.splitlines()
        if (match := re.fullmatch(r"(\d+)\. (.+)", line.strip()))
    ]
    assert [index for index, _ in rows] == list(range(1, 53))
    return rows


def _git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(("git", "show", f"{commit}:{path}"), cwd=ROOT)


def _iter_scalar_values(value: Any) -> Iterable[Any]:
    if isinstance(value, Mapping):
        for item in value.values():
            yield from _iter_scalar_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_scalar_values(item)
    else:
        yield value


def _semantic_target(row: Mapping[str, Any]) -> tuple[str, str, str]:
    target = row.get("semantic_target")
    if isinstance(target, Mapping):
        kind = target.get("kind") or target.get("target_kind")
        identity = target.get("id") or target.get("target_id")
        field = target.get("field") or target.get("mutation_field")
    else:
        kind = row.get("semantic_target_kind") or row.get("target_kind")
        identity = row.get("semantic_target_id") or row.get("target_id")
        field = row.get("mutation_field")
    payload = row.get("mutation_payload", {})
    if not field and isinstance(payload, Mapping):
        field = payload.get("mutation_field")
    if not identity and isinstance(payload, Mapping):
        nested = payload.get("semantic_target")
        if isinstance(nested, Mapping):
            kind = kind or nested.get("kind")
            identity = nested.get("id")
            field = field or nested.get("field")
    assert isinstance(kind, str) and kind
    assert isinstance(identity, str) and identity
    assert isinstance(field, str) and field
    return kind, identity, field


def validate_architecture() -> None:
    assert len(c35_arch.ARCHITECTURE_TYPES) == 53
    assert all(isinstance(item, type) for item in c35_arch.ARCHITECTURE_TYPES)
    names = tuple(item.__name__ for item in c35_arch.ARCHITECTURE_TYPES)
    assert names == EXPECTED_ARCHITECTURE_NAMES
    assert all(
        is_dataclass(item) and item.__dataclass_params__.frozen
        for item in c35_arch.ARCHITECTURE_TYPES
    )
    examples = c35_arch.architecture_examples()
    assert tuple(examples) == EXPECTED_ARCHITECTURE_NAMES
    for object_type in c35_arch.ARCHITECTURE_TYPES:
        value = examples[object_type.__name__]
        assert isinstance(value, object_type)
        envelope = value.identity
        assert envelope.object_type == object_type.__name__
        assert envelope.c34_completion_commit == c35.C35_BASELINE_COMMIT
        assert envelope.c33_b0_root == c35.C33_SOFT_ROOT
        assert envelope.c32_b1_root == c35.C32_COLLINEAR_ROOT
        assert envelope.c35_descendant_root == c35.C35_DESCENDANT_ROOT
        assert envelope.baryon_number == 0
        assert envelope.gauge_plan_id in {item.value for item in c35.GaugePlanKind}
        assert envelope.state_independent and envelope.hadron_independent
        assert envelope.art25_independent
        assert not envelope.process_reachable and not envelope.bridge_reachable
        assert not envelope.inference_reachable and not envelope.production_reachable
        assert len(value.sha256) == 64
        assert value.sha256 == c35_arch.content_hash(value)
        assert json.loads(value.to_deterministic_json())


def validate_conventions_and_oracles() -> None:
    convention = c35.LightFrontConvention()
    assert convention.metric_signature == "+---"
    assert abs(convention.dot(convention.n, convention.n)) < 1.0e-15
    assert abs(convention.dot(convention.nbar, convention.nbar)) < 1.0e-15
    assert abs(convention.dot(convention.n, convention.nbar) - 1.0) < 1.0e-15
    vector = (2.1, -0.3, 0.7, -0.4)
    plus, minus = convention.plus_minus(vector)
    pole_plus, pole_minus = convention.pole_components(vector)
    assert math.isclose(pole_plus, plus, rel_tol=0.0, abs_tol=2.0e-15)
    assert math.isclose(pole_minus, minus, rel_tol=0.0, abs_tol=2.0e-15)
    rebuilt = convention.reconstruct(plus, minus, (vector[1], vector[2]))
    assert max(abs(a - b) for a, b in zip(vector, rebuilt)) < 2.0e-15

    rescaling = c35.RapidityRegulatorRescaling()
    transformed = rescaling.transform(3.25, 0.002, 0.007)
    assert math.isclose(transformed[0], 0.002 / 3.25)
    assert math.isclose(transformed[1], 0.007 * 3.25)
    assert math.isclose(rescaling.invariant_product(3.25, 0.002, 0.007), 0.002 * 0.007)
    assert math.isclose(rescaling.source_to_project_delta_scale, 1.0 / math.sqrt(2.0))

    real = c35.RealSoftCoordinateChart()
    momentum = real.map(1.7, -0.4, 0.8)
    assert abs(real.mass_shell_residual(momentum)) < 2.0e-14
    assert math.isclose(real.measure_density(1.7), 1.7 / (2.0 * (2.0 * math.pi) ** 3))
    virtual = c35.VirtualSoftCoordinateChart()
    assert math.isclose(virtual.invariant((1.2, -0.8, 0.3, -0.5)), -2.26)
    assert math.isclose(virtual.measure_density(), 1.0 / (2.0 * math.pi) ** 4)
    assert tuple(real.coordinates) != tuple(virtual.coordinates)

    prototype = c35.real_cell_prototype(
        "C35.VALIDATION.CELL", (0.2, 0.7), (-0.5, 0.4), (0.1, 1.1)
    )
    assert abs(prototype.measure_value * prototype.top_hat_normalization ** 2 - 1.0) < 2.0e-14

    damping = c35.ModifiedDeltaDampingOperator()
    assert not damping.gauge_property_at_finite_delta
    assert damping.gauge_property_restored_only_in_delta_limit
    assert damping.power_delta_terms_must_be_discarded
    finite = damping.finite_segment_factor(0.7, 0.2, 200.0)
    infinite = damping.infinite_segment_factor(0.7, 0.2)
    assert abs(finite - infinite) < 1.0e-12
    assert abs(damping.ward_bulk_defect(0.7, 0.2, 2.0)) > 1.0e-6

    singular = c35.SingularCellOracle()
    assert singular.center_sampling_forbidden and singular.physical_cells_executed == 0
    expected_pv = math.log(3.0) - math.log(2.0)
    assert math.isclose(singular.principal_value_constant(-2.0, 3.0), expected_pv)
    for sign in (-1, 1):
        distributional = singular.distributional_constant(-2.0, 3.0, pole_sign=sign)
        regulated = singular.finite_delta_constant(-2.0, 3.0, 1.0e-9, pole_sign=sign)
        assert abs(distributional - regulated) < 2.0e-9


def validate_branch_g() -> None:
    plan = c35.default_gauge_plan_selection()
    assert plan.selected is c35.GaugePlanKind.UNAVAILABLE
    assert plan.frozen_before_coefficient and not plan.coefficient_attempted
    assert plan.primary_no_go == c35.C35_PRIMARY_NO_GO
    assert plan.outcome_branch == "G"
    assert "C36/O4" in plan.exact_next_package
    assert len(plan.candidates) == 4
    direct = [candidate for candidate in plan.candidates if candidate.kind is not c35.GaugePlanKind.UNAVAILABLE]
    assert all(not row.supported and not row.coefficient_execution_allowed for row in direct)

    allowed_statuses = {item.value for item in c35.ContributionStatus}
    assert allowed_statuses == {
        "CALCULATED_NONZERO",
        "CALCULATED_ZERO_BY_EXACT_IDENTITY",
        "CANCELS_WITH_DECLARED_PARTNER",
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO",
        "NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF",
        "UNRESOLVED_BLOCKING",
    }
    ledger = c35.fail_closed_contribution_ledger()
    assert len(ledger) == len(c35.REQUIRED_ONE_LOOP_CONTRIBUTIONS) == 18
    assert tuple(row.contribution_class for row in ledger) == c35.REQUIRED_ONE_LOOP_CONTRIBUTIONS
    assert all(row.status is c35.ContributionStatus.UNRESOLVED_BLOCKING for row in ledger)
    assert all(row.expression == c35.NONZERO_UNKNOWN and row.blocking for row in ledger)
    assert all(row.exact_missing_calculation for row in ledger)

    closure = c35.default_closure_report()
    assert closure.gauge_plan_decided and closure.light_front_normalization_validated
    assert not closure.gauge_complete_regulator_validated
    assert not closure.executable_mode_basis_validated
    assert not closure.finite_basis_one_loop_validated
    assert not closure.uv_renormalization_validated
    assert not closure.rapidity_renormalization_validated
    assert not closure.soft_side_zero_bin_ready
    assert closure.primary_no_go == c35.C35_PRIMARY_NO_GO
    assert closure.secondary_no_go == c35.C35_SECONDARY_MODE_NO_GO


def validate_deliverables() -> None:
    assert len(JSON_DELIVERABLES) == 61
    assert len(MARKDOWN_DELIVERABLES) == 4
    assert all((DOCS / name).is_file() for name in JSON_DELIVERABLES)
    assert all((DOCS / name).is_file() for name in MARKDOWN_DELIVERABLES)
    for name in JSON_DELIVERABLES:
        assert_content_address(name)

    assert file_hash(PROMPT) == PROMPT_SHA256 == c35.C35_PROMPT_SHA256
    assert file_hash(VOLUME_XXI) == VOLUME_XXI_SHA256 == c35.VOLUME_XXI_SHA256
    assert file_hash(DOCS / "c34_implementation_report.md") == C34_REPORT_SHA256
    assert file_hash(DOCS / "c34_requirement_coverage.json") == C34_COVERAGE_SHA256

    coverage = load("c35_requirement_coverage.json")
    rows = coverage["rows"]
    assert coverage["count"] == coverage["c35_requirement_record_count"] == len(rows) == 326
    assert len({row["requirement_id"] for row in rows}) == 326
    assert Counter(row["kind"] for row in rows) == Counter(EXPECTED_KIND_COUNTS)
    assert all(row["description"] and row["evidence_paths"] for row in rows)
    assert not any(row.get("positive_one_loop_status_claimed") for row in rows)
    acceptance = [row for row in rows if row["kind"] == "ACCEPTANCE_CRITERION"]
    assert [row["requirement_id"] for row in acceptance] == [f"C35.ACC.{i:03d}" for i in range(1, 53)]
    assert [row["description"] for row in acceptance] == [description for _, description in prompt_acceptance_rows()]
    assert all(
        row["disposition"] in {"PASS", "FAIL_CLOSED_GUARD_SATISFIED", "NOT_CLAIMED_DUE_BRANCH_G"}
        for row in acceptance
    )

    plan = load("c35_gauge_complete_plan_selection.json")
    assert plan["selected"] == c35.GaugePlanKind.UNAVAILABLE.value
    assert not plan["coefficient_attempted"]
    assert plan["primary_no_go"] == c35.C35_PRIMARY_NO_GO
    assert plan["outcome_branch"] == "G"
    bare = load("c35_bare_soft_coefficient.json")
    assert bare["tree_value"] == 1.0
    assert bare["one_loop_value"] is None
    assert bare["one_loop_status"] == c35.NONZERO_UNKNOWN
    assert not bare["all_required_slots_resolved"] and not bare["continuum_substituted"]
    counterterms = load("c35_soft_counterterm_results.json")
    assert not counterterms["bare_coefficient_available"]
    assert not counterterms["counterterm_solved_before_bare"]
    assert all(
        row.get("value") is None
        and row.get("value_semantics") == c35.NONZERO_UNKNOWN
        and row.get("status") == "UNRESOLVED_BLOCKING"
        for row in counterterms["records"]
    )
    diagrams = load("c35_soft_diagram_results.json")
    assert diagrams["count"] == len(diagrams["records"]) == 18
    assert not diagrams["all_slots_resolved"] and diagrams["all_slots_nonzero_unknown"]
    assert all(
        row["status"] == "UNRESOLVED_BLOCKING"
        and row["expression"] == c35.NONZERO_UNKNOWN
        and row["blocking"]
        for row in diagrams["records"]
    )
    gate = load("c35_c32_continuation_gate.json")
    assert not gate["passes"] and not gate["ready_status_issued"]
    assert not gate["bridge_rerun_executed"]
    export = gate["microscopic_proton_export"]
    assert export["shape"] == [0] and export["values"] is None and export["status"] == c35.EMPTY_NOT_ZERO

    for name in JSON_DELIVERABLES:
        values = set(value for value in _iter_scalar_values(load(name)) if isinstance(value, str))
        assert not values & FORBIDDEN_ISSUED_STATUSES, name


def validate_injections() -> None:
    manifest = load("c35_injection_manifest.json")
    rows = manifest["rows"]
    assert manifest["count"] == len(rows) >= 2440
    assert manifest["minimum_required"] == 2440
    assert manifest["fault_mode_count"] == len(c35.FAULT_CATALOG) == 93
    assert len(set(c35.FAULT_CATALOG)) == 93
    assert manifest["semantic_target_count"] == 98
    assert manifest["semantic_target_counts"] == {
        "ARCHITECTURE_OBJECT": 53,
        "CONTRIBUTION_SLOT": 18,
        "HOLDOUT": 27,
    }
    assert manifest["semantic_pair_count"] == len(rows)
    assert manifest["rows_differ_only_by_instance_index"] is False
    assert manifest["all_executed"] and manifest["all_detected"] and manifest["payload_hash_verified"]
    assert [row["ordered_index"] for row in rows] == list(range(1, len(rows) + 1))
    assert len({row["injection_id"] for row in rows}) == len(rows)
    targets = []
    semantic_signatures = set()
    for row in rows:
        payload = row["mutation_payload"]
        assert c35.content_hash(payload) == row["mutation_payload_sha256"]
        assert c35.execute_injection_payload(payload, row["mutation_payload_sha256"]) == row["expected_diagnostic"]
        assert row["observed_diagnostic"] == row["expected_diagnostic"] and row["detected"]
        kind, identity, field = _semantic_target(row)
        targets.append((kind, identity))
        payload_without_order = dict(payload)
        payload_without_order.pop("instance_index", None)
        semantic_signatures.add((row["fault"], kind, identity, field, canonical_hash(payload_without_order)))
    assert len(semantic_signatures) == len(rows), "C35_INJECTIONS_DIFFER_ONLY_BY_ORDER_OR_INSTANCE_INDEX"

    target_ids = {identity for _, identity in targets}
    expected_target_ids = {target_id for _, target_id, _ in c35.SEMANTIC_INJECTION_TARGETS}
    assert expected_target_ids <= target_ids
    assert len(expected_target_ids) == 53 + 18 + 27


def validate_regression_isolation() -> None:
    regression = load("c35_regression_report.json")
    assert regression["baseline_commit"] == c35.C35_BASELINE_COMMIT
    assert regression["c33_baseline"] == c35.C35_C33_BASELINE
    assert regression["c32_ancestor"] == c35.C35_C32_ANCESTOR
    assert regression["c28_ancestor"] == c35.C35_C28_ANCESTOR
    assert regression["baseline_reproduced_before_edits"]
    assert regression["immutable_c33_path_count"] == 74
    assert regression["all_immutable_c33_paths_byte_identical"]
    for row in regression["immutable_c33_paths"]:
        path = ROOT / row["path"]
        expected = _git_bytes(c35.C35_C33_BASELINE, row["path"])
        assert path.read_bytes() == expected
        assert file_hash(path) == row["actual_sha256"] == row["expected_sha256"]
    assert regression["immutable_c34_path_count"] == 73
    assert not regression["all_immutable_c34_paths_byte_identical"]
    assert regression["strictly_byte_identical_c34_path_count"] == 72
    assert regression["controlled_c34_maintenance_path_count"] == 1
    assert regression["all_c34_audited_paths_preserved_or_controlled"]
    assert regression["all_c34_json_manifests_byte_identical"]
    controlled = []
    for row in regression["immutable_c34_paths"]:
        path = ROOT / row["path"]
        expected = _git_bytes(c35.C35_BASELINE_COMMIT, row["path"])
        assert file_hash(path) == row["actual_sha256"]
        assert hashlib.sha256(expected).hexdigest() == row["expected_sha256"]
        if row["controlled_descendant_maintenance"]:
            controlled.append(row["path"])
            assert row["path"] == "scripts/build_c34_manifests.py"
            assert not row["byte_identical"] and path.read_bytes() != expected
            assert row["maintenance_reason"] == (
                "DESCENDANT_RECONSTRUCTION_GUARD_PINS_C34_LIVING_INPUTS_TO_C34_COMPLETION_BYTES"
            )
            assert row["accepted_without_scientific_output_change"]
        else:
            assert path.read_bytes() == expected
            assert row["byte_identical"] and row["actual_sha256"] == row["expected_sha256"]
    assert controlled == ["scripts/build_c34_manifests.py"]
    for path in sorted(DOCS.glob("c34_*.json")):
        assert path.read_bytes() == _git_bytes(c35.C35_BASELINE_COMMIT, str(path.relative_to(ROOT)))

    assert json.loads((DOCS / "c2_reduction_registry.json").read_text())["count"] == 216
    assert regression["production_registry_count"] == 216
    artifacts = regression["authoritative_artifacts"]
    assert len(artifacts) == 8 and regression["authoritative_artifacts_unchanged"]
    for artifact in artifacts:
        assert artifact["byte_identical"]
        assert artifact["actual_sha256"] == artifact["expected_sha256"] == file_hash(ROOT / artifact["path"])

    ensemble = json.loads((DOCS / "c28_theory_ensemble_factor_manifest.json").read_text())
    assert ensemble["members"] == 642 and ensemble["shape"] == [642, 1209]
    assert len(ensemble["member_ids"]) == len(set(ensemble["member_ids"])) == 642
    cross_root = json.loads((DOCS / "c29_cross_root_member_relation.json").read_text())
    assert cross_root["external_members"] == 642 and cross_root["status"] == "NO_JOINT_MEASURE"
    assert regression["external_art25_members"] == 642
    assert regression["cross_root_relation"] == "NO_JOINT_MEASURE"
    assert regression["failed_bridge_projection"] == {"shape": [642, 0], "empty_not_zero": True}
    inherited_covariance = load("c34_regression_report.json")["source_covariance"]
    assert regression["source_covariance"] == inherited_covariance
    assert inherited_covariance == {
        "shape": [642, 11],
        "rank": 10,
        "nullity": 1,
        "sha256": "33de79398ef3d75657e715abf751b5a12634e7e65e53a95b9ee19b0fb8eea16a",
    }
    for key in (
        "art25_consumed", "art25_data_consumed", "art25_chi2_consumed",
        "bridge_rerun", "microscopic_proton_export",
    ):
        assert regression[key] is False


def main() -> None:
    validate_architecture()
    validate_conventions_and_oracles()
    validate_branch_g()
    validate_deliverables()
    validate_injections()
    validate_regression_isolation()
    print("C35_VALIDATION_PASS")


if __name__ == "__main__":
    main()
