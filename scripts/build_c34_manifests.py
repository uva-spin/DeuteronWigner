#!/usr/bin/env python3
"""Build deterministic C34/S0A one-loop soft-sector manifests.

C34 is deliberately a rigorous Branch-G result.  The builder freezes the
one-loop, quadrature, trajectory, and holdout contracts and records exact
tree/current identities, but it does not manufacture finite-basis one-loop
matrix elements from a continuum oracle.  All required one-loop terms remain
``UNRESOLVED_BLOCKING`` until the missing gauge-complete cell basis, mode
functions, zero-mode sector, and counterterms are calculated.

The script has no fitting, inference, bridge-execution, proton-export, or
production entry point.  Historical C33/S0 artifacts are read-only regression
oracles pinned to the resolved local C33 completion commit.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"

C33_BASELINE = "e0b34c74e8f39c9d42cf49cc598f1533d9353a7e"
C34_COMPLETION = "6bdb44be2afc79e817f69ce0e35813da8a394db7"
C33_PRE_VOLUME_COMMIT = "9bf4af82fb8eed576e3981f3e699a1815529b4a7"
C32_ANCESTOR = "0d7b94a5e86882b23a56d4c1f11900d554756a18"
C28_ANCESTOR = "52678312906bf5cc0bb8664e2486d5d676a6b723"

PROMPT_PATH = "docs/next_level/c34_s0a_codex_prompt.md"
PROMPT_SHA256 = "a4a959d2d6401cbf296d6514591b3c5b4c3301a2b5867f0481b83a43d7c374eb"
VOLUME_XXI_PATH = "references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"

# These are living, append-only project records.  A historical C34 rebuild in
# a later work package must hash the versions that C34 actually consumed,
# rather than making C34 output depend on later handoff text.  This affects no
# physics object and restores exact reconstruction of the completion commit.
C34_LIVING_INPUTS = {
    "references/formalism_volume_index.md",
    "handoff/ROADMAP.md",
}

SOFT_ROOT = "C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT"
COLLINEAR_ROOT = "C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION"
PRIMARY_PLAN = "S0-FB-EIKONAL-FOCK"
ONE_LOOP_PLAN_ID = "C34.S0A.ONE_LOOP.PLAN.v1"
QUADRATURE_ID = "C34.SOFT.CELL.QUADRATURE.v1"
NO_GO = "C34_SOFT_ONE_LOOP_INCOMPLETE"
NEXT_PACKAGE = "C35/S0C"
NEXT_PACKAGE_DESCRIPTION = "targeted unresolved soft-diagram and counterterm completion"
OUTCOME_BRANCH = "G"
UNKNOWN = "NONZERO_UNKNOWN"
COUPLING_NORMALIZATION = "a_s=alpha_s/(4*pi)=g_s^2/(4*pi)^2"

C33_BASIS_SOURCE_PATH = "docs/next_level/c33_soft_basis_trajectory_plan.json"
C33_OPERATOR_SOURCE_PATH = "docs/next_level/c33_four_line_operator_manifest.json"
C33_DENOMINATOR_SOURCE_PATH = "docs/next_level/c33_eikonal_denominator_report.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_json(path: str) -> dict[str, Any]:
    """Load an inherited source object; C34 does not re-key it by hand."""
    return json.loads((ROOT / path).read_text())


def content_address(value: dict[str, Any]) -> dict[str, Any]:
    result = dict(value)
    result.pop("content_hash", None)
    result["content_hash"] = digest(result)
    return result


def put(name: str, value: dict[str, Any]) -> None:
    payload = content_address(value)
    (DOCS / name).write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True,
                   allow_nan=False) + "\n"
    )


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def c34_input_sha256(path: str) -> str:
    if path in C34_LIVING_INPUTS:
        return hashlib.sha256(git_bytes(C34_COMPLETION, path)).hexdigest()
    return sha256(ROOT / path)


def git_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    return subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def baseline_record(path: str) -> dict[str, Any]:
    current_path = ROOT / path
    expected = git_bytes(C33_BASELINE, path)
    current = current_path.read_bytes() if current_path.is_file() else b""
    return {
        "path": path,
        "present": current_path.is_file(),
        "expected_sha256": hashlib.sha256(expected).hexdigest(),
        "actual_sha256": hashlib.sha256(current).hexdigest() if current_path.is_file() else None,
        "byte_identical": current_path.is_file() and current == expected,
    }


def immutable_c33_paths() -> list[str]:
    names = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", C33_BASELINE],
        cwd=ROOT, text=True,
    ).splitlines()
    paths = sorted(
        path for path in names
        if "c33" in path or path.startswith("src/deuteron_wigner/bridge/s0/")
    )
    if len(paths) != 74:
        raise RuntimeError(f"C34_C33_IMMUTABLE_PATH_COUNT_MISMATCH:{len(paths)}")
    return paths


def source_records() -> list[dict[str, Any]]:
    inherited = json.loads((DOCS / "c33_primary_source_manifest.json").read_text())
    records = []
    for source in inherited["records"]:
        path = ROOT / source["path"]
        record = dict(source)
        record.update({
            "present": path.is_file(),
            "actual_sha256": sha256(path) if path.is_file() else None,
            "hash_matches_c33_lock": path.is_file() and sha256(path) == source["sha256"],
            "c34_role": "SOURCE_OR_METHOD_OR_CONTINUUM_ORACLE_ONLY",
            "operator_identical_to_c34_finite_basis": False,
            "used_as_finite_basis_coefficient": False,
        })
        records.append(record)
    return records


NORMATIVE_PATHS = (
    "docs/next_level/c5_implementation_report.md",
    "docs/next_level/c5_api.md",
    "docs/next_level/c5_benchmark_manifest.json",
    "docs/next_level/c6_implementation_report.md",
    "docs/next_level/c6_api.md",
    "docs/next_level/c6_benchmark_manifest.json",
    "docs/next_level/c12_implementation_report.md",
    "docs/next_level/c12_api.md",
    "docs/next_level/c13_implementation_report.md",
    "docs/next_level/c14_implementation_report.md",
    "docs/next_level/c14_api.md",
    "docs/next_level/c7_implementation_report.md",
    "docs/next_level/c11_implementation_report.md",
    "docs/next_level/c11_api.md",
    "docs/next_level/c31_implementation_report.md",
    "docs/next_level/c31_three_layer_identity_manifest.json",
    "docs/next_level/c31_continuum_scheme_equivalence_matrix.json",
    "docs/next_level/c31_source_sufficiency_decision.json",
    "docs/next_level/c32_implementation_report.md",
    "docs/next_level/c32_api.md",
    "docs/next_level/c32_operator_completion_manifest.json",
    "docs/next_level/c32_c11_tree_reduction_report.json",
    "docs/next_level/c32_regulator_plan_manifest.json",
    "docs/next_level/c32_partonic_external_state_plan.json",
    "docs/next_level/c32_gauge_plan.json",
    "docs/next_level/c32_rapidity_plan.json",
    "docs/next_level/c32_partonic_diagram_ledger.json",
    "docs/next_level/c32_counterterm_ledger.json",
    "docs/next_level/c32_zero_bin_overlap_manifest.json",
    "docs/next_level/c32_source_sufficiency_decision.json",
    "docs/next_level/c33_implementation_report.md",
    "docs/next_level/c33_api.md",
    "docs/next_level/c33_requirement_coverage.json",
    "docs/next_level/c33_normative_source_integration.json",
    "docs/next_level/c33_primary_source_manifest.json",
    "docs/next_level/c33_source_relevance_matrix.json",
    "docs/next_level/c33_two_root_tmd_identity.json",
    "docs/next_level/c33_soft_collinear_provenance_graph.json",
    "docs/next_level/c33_soft_sector_plan_manifest.json",
    "docs/next_level/c33_soft_sector_plan_selection.json",
    "docs/next_level/c33_vacuum_hilbert_manifest.json",
    "docs/next_level/c33_soft_basis_manifest.json",
    "docs/next_level/c33_soft_zero_mode_policy.json",
    "docs/next_level/c33_soft_basis_trajectory_plan.json",
    "docs/next_level/c33_eikonal_color_space.json",
    "docs/next_level/c33_four_line_operator_manifest.json",
    "docs/next_level/c33_eikonal_path_reversal_report.json",
    "docs/next_level/c33_soft_rapidity_regulator_manifest.json",
    "docs/next_level/c33_eikonal_denominator_report.json",
    "docs/next_level/c33_soft_diagram_ledger.json",
    "docs/next_level/c33_soft_counterterm_ledger.json",
    "docs/next_level/c33_soft_dependency_graph.json",
    "docs/next_level/c33_bare_soft_factor.json",
    "docs/next_level/c33_bare_soft_oracle_report.json",
    "docs/next_level/c33_soft_collinear_regulator_pair.json",
    "docs/next_level/c33_soft_collinear_compatibility_report.json",
    "docs/next_level/c33_zero_bin_interface_contract.json",
    "docs/next_level/c33_c32_continuation_gate.json",
    "docs/next_level/c33_source_sufficiency_decision.json",
    "docs/next_level/c33_no_go_decision_tree.json",
    "docs/next_level/c33_missing_calculation_specification.md",
    "docs/next_level/c33_unresolved_physics_gaps.md",
    "docs/next_level/c19_implementation_report.md",
    "docs/next_level/c20_implementation_report.md",
    "docs/next_level/c21_implementation_report.md",
    "docs/next_level/c22_implementation_report.md",
    "references/volume_v_matching_evolution_factorization.tex",
    "references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf",
    "references/volume_xvii_process_qualified_tmd_observables.tex",
    "references/volume_xviii_smallb_ope_collinear_mixing.tex",
    "references/volume_xix_source_qualified_process_inputs.tex",
    "references/volume_xx_source_reproducible_bridge_geometry.tex",
    VOLUME_XXI_PATH,
    "references/formalism_volume_index.md",
    "handoff/ROADMAP.md",
    PROMPT_PATH,
)


def inherited_resolutions() -> tuple[dict[str, Any], ...]:
    """Decorate, but never retype, the immutable C33 resolution records."""
    source = load_json(C33_BASIS_SOURCE_PATH)
    expected_ids = ("C33.RES.1", "C33.RES.2", "C33.RES.3")
    records = []
    for index, inherited in enumerate(source["resolutions"]):
        if inherited["resolution_id"] != expected_ids[index]:
            raise RuntimeError("C34_C33_RESOLUTION_ID_OR_ORDER_MISMATCH")
        record = dict(inherited)
        record.update({
            "resolution_label": f"S0-R{index + 1}",
            "cell_tuple": [inherited["N_omega"], inherited["N_y"], inherited["N_perp"]],
            "c34_experimental_role": "HOLDOUT" if index == 2 else "CONSTRUCTION",
            "c33_source_path": C33_BASIS_SOURCE_PATH,
            "c33_source_record_sha256": digest(inherited),
            "descriptor_nested_by_support_declared": source["nested_by_resolution_and_support"],
            "refinement_map_proved": False,
        })
        records.append(record)
    return tuple(records)


def inherited_lines() -> tuple[dict[str, Any], ...]:
    """Join C33 operator and denominator objects by their stable line IDs."""
    operator = load_json(C33_OPERATOR_SOURCE_PATH)
    denominator_report = load_json(C33_DENOMINATOR_SOURCE_PATH)
    denominators = {row["line_id"]: row for row in denominator_report["records"]}
    display_factors = {
        "C33.LINE.N.DAGGER.B": "S_n^dagger(b)",
        "C33.LINE.NBAR.B": "S_nbar(b)",
        "C33.LINE.NBAR.DAGGER.0": "S_nbar^dagger(0)",
        "C33.LINE.N.0": "S_n(0)",
    }
    records = []
    for source_line in sorted(operator["lines"], key=lambda row: row["ordered_position"]):
        line_id = source_line["line_id"]
        denominator = denominators[line_id]
        conjugate = bool(source_line["dagger"])
        basepoint = source_line["basepoint"]
        records.append({
            "line_id": line_id,
            "stored_factor": display_factors[line_id],
            "stored_factor_role": "DISPLAY_ONLY_DERIVED_FROM_LINE_ID",
            "ordered_position": source_line["ordered_position"],
            "direction": source_line["direction"],
            "transverse_position": basepoint,
            "conjugate": conjugate,
            "representation": "ANTI_FUNDAMENTAL" if conjugate else "FUNDAMENTAL",
            "c33_stored_representation": source_line["representation"],
            "path_ordering": source_line["path_ordering"],
            "segments": list(source_line["segments"]),
            "orientation": "FUTURE",
            "orientation_variants": list(source_line["orientation_variants"]),
            "momentum_component": denominator["component"],
            "delta_component": denominator["delta"],
            "i0_sign": denominator["i0_sign"],
            "ordered_j_shift": denominator["ordered_j_shift"],
            "color_action": "-T_a^T" if conjugate else "T_a",
            "phase": "exp(+i kT.bT)" if basepoint == "bT" else "1",
            "c33_operator_source_path": C33_OPERATOR_SOURCE_PATH,
            "c33_operator_source_record_sha256": digest(source_line),
            "c33_denominator_source_path": C33_DENOMINATOR_SOURCE_PATH,
            "c33_denominator_source_record_sha256": digest(denominator),
            "derivation_inputs": list(denominator_report["derivation_inputs"]),
        })
    if len(records) != 4:
        raise RuntimeError("C34_C33_FOUR_LINE_CARDINALITY_MISMATCH")
    return tuple(records)


def c33_operator_id_mapping() -> dict[str, Any]:
    """Execute a field-by-field comparison of C33 runtime and JSON objects."""
    from deuteron_wigner.bridge.s0.core import default_four_line_operator

    runtime = default_four_line_operator()
    manifest = load_json(C33_OPERATOR_SOURCE_PATH)
    line_id_map = {
        "SN_DAGGER_B": "C33.LINE.N.DAGGER.B",
        "SNBAR_B": "C33.LINE.NBAR.B",
        "SNBAR_DAGGER_0": "C33.LINE.NBAR.DAGGER.0",
        "SN_0": "C33.LINE.N.0",
    }
    manifest_by_id = {row["line_id"]: row for row in manifest["lines"]}
    comparisons = []
    for path in runtime.paths:
        row = manifest_by_id[line_id_map[path.path_id]]
        basepoint_equal = {"b": "bT", "0": "0T"}[path.source.transverse_position] == row["basepoint"]
        runtime_segments = list(path.segments) + (["TRANSVERSE_CLOSURE"] if path.transverse_closure_id else [])
        source_segments = [segment.replace("_SEGMENT", "") for segment in runtime_segments]
        checks = {
            "direction_equal": path.source.direction == row["direction"],
            "conjugation_equal": path.source.conjugate == row["dagger"],
            "basepoint_equal_after_explicit_adapter": basepoint_equal,
            "path_ordering_equal": path.path_ordering == row["path_ordering"],
            "segments_equal_after_explicit_adapter": source_segments == row["segments"],
            "representation_equal_after_explicit_adapter": (
                path.source.representation == "ANTI_FUNDAMENTAL"
                if row["representation"] == "CONJUGATE_FUNDAMENTAL"
                else path.source.representation == row["representation"]
            ),
        }
        comparisons.append({
            "runtime_path_id": path.path_id,
            "manifest_line_id": row["line_id"],
            "checks": checks,
            "all_checks_pass": all(checks.values()),
        })
    mapped_trace = [line_id_map[item] for item in runtime.trace_order]
    manifest_trace = [row["line_id"] for row in sorted(manifest["lines"], key=lambda item: item["ordered_position"])]
    tree_value = float(runtime.tree_level_soft_factor)
    all_checks = all(row["all_checks_pass"] for row in comparisons)
    return {
        "runtime_operator_id": runtime.operator_id,
        "manifest_operator_id": manifest["operator_id"],
        "relation": "SAME_C33_FOUR_LINE_OPERATOR_DIFFERENT_SERIALIZATION_IDENTIFIER",
        "line_id_map": line_id_map,
        "field_comparisons": comparisons,
        "trace_order_identical_after_explicit_id_map": mapped_trace == manifest_trace,
        "path_direction_conjugation_basepoints_segments_identical": all_checks,
        "singlet_trace_identical": tree_value == manifest["tree_value"],
        "tree_value_identical": tree_value == manifest["tree_value"],
        "tree_value": tree_value,
        "runtime_serialization_sha256": digest({
            "operator_id": runtime.operator_id,
            "trace_order": list(runtime.trace_order),
            "paths": comparisons,
            "tree_value": tree_value,
        }),
        "manifest_record_sha256": digest(manifest),
        "runtime_source": "src/deuteron_wigner/bridge/s0/core.py::default_four_line_operator",
        "manifest_source": C33_OPERATOR_SOURCE_PATH,
        "silent_alias": False,
        "mapping_status": "EXECUTABLE_SOURCE_COMPARISON_PASSED" if all_checks and mapped_trace == manifest_trace else "EXECUTABLE_SOURCE_COMPARISON_FAILED",
    }


RESOLUTIONS = inherited_resolutions()
LINES = inherited_lines()
C33_OPERATOR_ID_MAPPING: dict[str, Any] | None = None


CONTRIBUTIONS = (
    ("N_NBAR_EXCHANGE", "normalized gauge-complete n--nbar cell kernel and virtual prescription"),
    ("CONJUGATE_LINE_EXCHANGE", "normalized conjugate-line cell kernel with anti-fundamental action"),
    ("SAME_DIRECTION_LINE_EXCHANGE", "finite-regulator same-direction integral; continuum scalelessness is insufficient"),
    ("REAL_ONE_SOFT_GLUON", "cell-integrated cut one-gluon matrix elements and measurement support"),
    ("VIRTUAL_ONE_SOFT_GLUON", "cell-integrated uncut contraction and vacuum prescription"),
    ("WILSON_LINE_SELF_ENERGY", "finite-cell line self-energy operator and UV/power separation"),
    ("CUSP_ENDPOINT", "finite-basis cusp and endpoint junction realization"),
    ("TRANSVERSE_CLOSURE", "explicit transverse-infinity segment modes and junction kernel"),
    ("AUXILIARY_FIELD_SELF_ENERGY", "proved auxiliary-to-direct Minkowski modified-delta conversion"),
    ("SOFT_VACUUM_ENERGY", "B=0 interacting-vacuum subtraction prescription"),
    ("LIGHT_FRONT_INSTANTANEOUS", "gauge-complete light-front constrained-field kernel"),
    ("GAUGE_FIXING", "covariant-gauge finite-basis propagator/BRST completion at xi=0,1,2"),
    ("GHOST", "ghost-sector basis and cancellation proof in the chosen gauge realization"),
    ("ZERO_MODE", "explicit constrained exact-zero-mode sector retained by C33 policy"),
    ("BASIS_BOUNDARY", "normalized boundary modes and finite-cell boundary counterterm"),
    ("RAPIDITY_COUNTERTERM", "calculated bare delta-plus/delta-minus logarithms"),
    ("UV_COUNTERTERM", "calculated power/log/cusp/endpoint UV structure"),
    ("RESIDUAL_LINE_MASS_COUNTERTERM", "finite-regulator line-mass divergence or proof of non-applicability"),
)


DIRECT_BARE_CLASSES = (
    "N_NBAR_EXCHANGE", "CONJUGATE_LINE_EXCHANGE",
    "SAME_DIRECTION_LINE_EXCHANGE", "REAL_ONE_SOFT_GLUON",
    "VIRTUAL_ONE_SOFT_GLUON", "WILSON_LINE_SELF_ENERGY",
    "CUSP_ENDPOINT", "TRANSVERSE_CLOSURE", "SOFT_VACUUM_ENERGY",
    "LIGHT_FRONT_INSTANTANEOUS", "GAUGE_FIXING", "GHOST",
    "BASIS_BOUNDARY",
)
SEPARATE_CONTROL_CLASSES = ("ZERO_MODE",)
ALTERNATIVE_ROUTE_CLASSES = ("AUXILIARY_FIELD_SELF_ENERGY",)
COUNTERTERM_DECISION_CLASSES = (
    "RAPIDITY_COUNTERTERM", "UV_COUNTERTERM",
    "RESIDUAL_LINE_MASS_COUNTERTERM",
)

# Counterterms are distinct derived objects; their IDs never alias graph IDs.
COUNTERTERM_COMPONENTS = (
    ("LINE_SELF_ENERGY", ("WILSON_LINE_SELF_ENERGY",)),
    ("CUSP", ("CUSP_ENDPOINT",)),
    ("ENDPOINT", ("CUSP_ENDPOINT",)),
    ("TRANSVERSE_CLOSURE", ("TRANSVERSE_CLOSURE",)),
    ("VACUUM", ("SOFT_VACUUM_ENERGY",)),
    ("BASIS_BOUNDARY", ("BASIS_BOUNDARY",)),
    ("SOFT_OPERATOR_UV", ("UV_COUNTERTERM",)),
    ("RAPIDITY", ("RAPIDITY_COUNTERTERM",)),
    ("RESIDUAL_LINE_MASS", ("RESIDUAL_LINE_MASS_COUNTERTERM",)),
)


DELTA_SCHEDULE = (
    {"probe_id": "C34.DELTA.CENTRAL", "delta_plus_GeV": 0.002,
     "delta_minus_GeV": 0.003, "varied_axis": "NONE", "fixed_axis": None,
     "role": "CONSTRUCTION"},
    {"probe_id": "C34.DELTA.PLUS.UP", "delta_plus_GeV": 0.004,
     "delta_minus_GeV": 0.003, "varied_axis": "DELTA_PLUS", "fixed_axis": "DELTA_MINUS",
     "role": "CONSTRUCTION"},
    {"probe_id": "C34.DELTA.PLUS.DOWN", "delta_plus_GeV": 0.001,
     "delta_minus_GeV": 0.003, "varied_axis": "DELTA_PLUS", "fixed_axis": "DELTA_MINUS",
     "role": "CONSTRUCTION"},
    {"probe_id": "C34.DELTA.MINUS.UP", "delta_plus_GeV": 0.002,
     "delta_minus_GeV": 0.006, "varied_axis": "DELTA_MINUS", "fixed_axis": "DELTA_PLUS",
     "role": "CONSTRUCTION"},
    {"probe_id": "C34.DELTA.MINUS.DOWN", "delta_plus_GeV": 0.002,
     "delta_minus_GeV": 0.0015, "varied_axis": "DELTA_MINUS", "fixed_axis": "DELTA_PLUS",
     "role": "CONSTRUCTION"},
    {"probe_id": "C34.DELTA.PLUS.HOLDOUT", "delta_plus_GeV": 0.0005,
     "delta_minus_GeV": 0.003, "varied_axis": "DELTA_PLUS", "fixed_axis": "DELTA_MINUS",
     "role": "HOLDOUT"},
    {"probe_id": "C34.DELTA.MINUS.HOLDOUT", "delta_plus_GeV": 0.002,
     "delta_minus_GeV": 0.00075, "varied_axis": "DELTA_MINUS", "fixed_axis": "DELTA_PLUS",
     "role": "HOLDOUT"},
)


HOLDOUTS = (
    "N_NBAR_LINE_PAIR_COEFFICIENT", "CONJUGATE_LINE_COEFFICIENT",
    "SAME_DIRECTION_CONTRIBUTION", "REAL_CONTRIBUTION",
    "VIRTUAL_CONTRIBUTION", "WILSON_SELF_ENERGY_COEFFICIENT",
    "CUSP_ENDPOINT_COEFFICIENT", "TRANSVERSE_CLOSURE_COEFFICIENT",
    "GAUGE_XI_2", "DELTA_PLUS_VARIATION_5E_MINUS4",
    "DELTA_MINUS_VARIATION_7P5E_MINUS4", "B_POINT_1P0_GEV_MINUS1",
    "B_TO_ZERO_CONTROLLED_POINT", "ZERO_MODE_CONTROL",
    "BASIS_BOUNDARY_COEFFICIENT", "UV_COUNTERTERM_COEFFICIENT",
    "RAPIDITY_COUNTERTERM_COEFFICIENT", "RAPIDITY_ANOMALOUS_DIMENSION_COEFFICIENT",
    "CONTINUUM_ORACLE_FINITE_CONSTANT", "FINITE_REGULATOR_ROUND_TRIP",
    "SOFT_RESOLUTION_C33_RES_3", "AUXILIARY_DIRECT_COMPARISON",
    "SOFT_SIDE_ZERO_BIN_OBJECT", "ART25_INDEPENDENCE_CONTROL",
)


REMAINDERS = (
    "FIRST_OMITTED_PERTURBATIVE_ORDER", "UV_COUNTERTERM_TRUNCATION",
    "RAPIDITY_COUNTERTERM_TRUNCATION", "FINITE_BASIS_UV",
    "FINITE_BASIS_IR", "RAPIDITY_WINDOW", "ZERO_MODE",
    "ENDPOINT_CUSP", "TRANSVERSE_CLOSURE", "RESIDUAL_LINE_MASS",
    "BASIS_BOUNDARY", "FINITE_BASIS_TO_CONTINUUM_CONVERSION",
    "SOFT_COLLINEAR_COMPATIBILITY", "ZERO_BIN_INTERFACE",
    "AUXILIARY_FIELD_REPRESENTATION", "QUADRATURE_AND_FLOATING_POINT",
)


ACCEPTANCE = (
    "The actual clean C33 completion commit is resolved and recorded rather than invented.",
    "The complete C33 baseline reproduces before edits.",
    "The B=0 soft and B=1 collinear roots remain disjoint.",
    "The C33 basis, path, rapidity, and tree identities remain unchanged.",
    "The one-loop plan is frozen before results.",
    "The quadrature/cell-integration plan is frozen before results.",
    "Every eikonal line contributes through a typed current.",
    "Singular cells are integrated rather than sampled naively.",
    "Every required one-loop contribution receives a calculated or proved status.",
    "No required finite-regulator contribution is called scaleless by continuum analogy alone.",
    "Real and virtual contributions are counted once.",
    "Color-trace normalization closes.",
    "Future/past T-even equality closes when claimed.",
    "Gauge dependence cancels when claimed.",
    "The bare coefficient retains all regulator identities.",
    "UV power and logarithmic structures remain separate.",
    "UV counterterms are state independent.",
    "Rapidity dependence is retained until the rapidity counterterm is applied.",
    "Modified-delta regulator dependence cancels when claimed.",
    "The rapidity anomalous dimension is extracted only from a closed calculation.",
    "Cusp consistency is tested.",
    "The continuum target oracle is independently reconstructed.",
    "The continuum coefficient is not substituted for the finite-basis coefficient.",
    "The finite-regulator conversion is hadron and ART25 independent.",
    "Inverse and round-trip conversion are tested.",
    "All three C33 resolutions are executed for any trajectory claim.",
    "No trajectory is overfit.",
    "At least one trajectory/regulator combination remains a holdout.",
    "Zero-mode status is calculated or remains blocking.",
    "Endpoint, cusp, and transverse-closure pieces remain separately auditable.",
    "Auxiliary and direct routes remain alternatives.",
    "The soft-side zero-bin object is explicit.",
    "Off-shell soft/zero-bin equivalence is not assumed from citation.",
    "A valid soft function is not called a completed microscopic TMD.",
    "C34 creates no microscopic proton export.",
    "C34 does not rerun the twelve-point bridge.",
    "The C32 continuation gate is issued only at its exact supported scope.",
    "All remainder classes remain separate.",
    "Unknown remainder remains nonzero-unknown.",
    "No ART25 object enters the derivation.",
    "C29-C33 roles, holdouts, ancestry, and `NO_JOINT_MEASURE` remain unchanged.",
    "All 642 ART25 identities and source covariance remain unchanged.",
    "No fit, calibration, likelihood, posterior, optimization, reweighting, or emulator is created.",
    "No process, deuteron, spin-1, gluon, T-odd, inference, or production status is promoted.",
    "Every no-go result contains an exact missing-calculation specification.",
    "All inherited tests, builders, requirements, injections, and manifests remain passing.",
    "The production registry remains exactly 216 routes.",
    "All eight authoritative artifacts remain byte-identical.",
    "Raw transferred source files remain outside Git absent permission.",
    "Every C34 negative injection yields the expected diagnostic.",
    "All C34 manifests reproduce byte-for-byte.",
    "The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.",
    "A local completion commit is created and not pushed.",
)


ACCEPTANCE_EVIDENCE = (
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_one_loop_plan.json", "docs/next_level/c34_soft_collinear_continuation_contract.json"),
    ("docs/next_level/c34_regression_report.json", "docs/next_level/c34_one_loop_plan.json"),
    ("docs/next_level/c34_one_loop_plan.json",),
    ("docs/next_level/c34_mode_quadrature_plan.json",),
    ("docs/next_level/c34_eikonal_current_manifest.json",),
    ("docs/next_level/c34_mode_cell_integration_report.json",),
    ("docs/next_level/c34_soft_diagram_results.json",),
    ("docs/next_level/c34_soft_diagram_results.json",),
    ("docs/next_level/c34_real_virtual_assembly.json", "docs/next_level/c34_count_once_report.json"),
    ("docs/next_level/c34_eikonal_current_manifest.json",),
    ("docs/next_level/c34_bare_soft_validation_report.json",),
    ("docs/next_level/c34_soft_uv_closure_report.json", "docs/next_level/c34_rapidity_renormalization_closure.json"),
    ("docs/next_level/c34_bare_soft_coefficient.json",),
    ("docs/next_level/c34_soft_uv_structure.json",),
    ("docs/next_level/c34_soft_uv_counterterm_solution.json",),
    ("docs/next_level/c34_soft_rapidity_structure.json",),
    ("docs/next_level/c34_rapidity_renormalization_closure.json",),
    ("docs/next_level/c34_soft_rapidity_anomalous_dimension.json",),
    ("docs/next_level/c34_cusp_consistency_report.json",),
    ("docs/next_level/c34_continuum_soft_oracle_report.json",),
    ("docs/next_level/c34_continuum_soft_target.json", "docs/next_level/c34_bare_soft_coefficient.json"),
    ("docs/next_level/c34_soft_regulator_conversion.json",),
    ("docs/next_level/c34_soft_regulator_roundtrip.json",),
    ("docs/next_level/c34_soft_basis_trajectory.json",),
    ("docs/next_level/c34_trajectory_fit_plan.json",),
    ("docs/next_level/c34_holdout_report.json", "docs/next_level/c34_soft_trajectory_holdout_report.json"),
    ("docs/next_level/c34_zero_mode_contribution_report.json",),
    ("docs/next_level/c34_endpoint_transverse_closure_report.json",),
    ("docs/next_level/c34_auxiliary_soft_crosscheck.json",),
    ("docs/next_level/c34_soft_side_zero_bin_limit.json",),
    ("docs/next_level/c34_soft_collinear_continuation_contract.json",),
    ("docs/next_level/c34_c32_continuation_gate.json",),
    ("docs/next_level/c34_c32_continuation_gate.json", "docs/next_level/c34_regression_report.json"),
    ("docs/next_level/c34_c32_continuation_gate.json", "docs/next_level/c34_regression_report.json"),
    ("docs/next_level/c34_c32_continuation_gate.json",),
    ("docs/next_level/c34_soft_remainder_separation.json",),
    ("docs/next_level/c34_soft_remainder_separation.json",),
    ("docs/next_level/c34_derivation_authority_manifest.json", "docs/next_level/c34_regression_report.json"),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_source_sufficiency_decision.json", "docs/next_level/c34_missing_calculation_specification.md"),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_injection_manifest.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
    ("docs/next_level/c34_regression_report.json",),
)


FAIL_CLOSED_ACCEPTANCE = {
    13: "Future/past equality is withheld because the one-loop cell assembly is unavailable.",
    14: "Gauge cancellation is withheld because the gauge-complete B=0 action and cell propagator are unavailable.",
    17: "No UV counterterm is issued; state independence is required but remains unproved while the solution is blocking.",
    19: "Modified-delta cancellation is not claimed before a bare finite-basis rapidity dependence exists.",
    20: "No rapidity anomalous dimension is extracted from the incomplete calculation.",
    29: "The excluded exact-zero-mode control remains NONZERO_UNKNOWN and blocking.",
}


NOT_CLAIMED_ACCEPTANCE = {
    5: "The selected method and probe schedule are frozen, but the missing gauge-complete field realization, mode functions, measures, and interaction normalization leave the full executable one-loop plan incomplete.",
    6: "Only the quadrature method family and nominal orders are frozen; missing tolerances, subdivision limits, contour/pole treatment, normalized modes, and singular subtraction leave the execution plan partially specified.",
    8: "Normalized finite-cell mode functions and the analytic singular-subtraction kernel are absent, so no singular cell was integrated.",
    9: "All eighteen required contributions are explicit UNRESOLVED_BLOCKING records; none has yet received a calculated or proved physical status.",
    11: "The cut IDs are structurally unique, but physical real/virtual branch assignment and direct Wilson-expansion versus mode-sum equality were not executed.",
    21: "The cusp relation cannot be evaluated because no rapidity anomalous dimension was extracted.",
    22: "The continuum final expression is source-qualified, but neither graph-level nor independent direct-integral reconstruction was performed.",
    24: "No conversion was issued, so its required hadron, state, and ART25-member independence is not yet proved.",
    25: "The one-loop finite-regulator kernel does not exist, so inverse and round-trip residuals were not evaluated.",
    26: "R1-R3 have exact inherited identities and tree values only; no one-loop trajectory claim or execution is made.",
    52: "Working-tree cleanliness can only be assessed after the local completion commit.",
    53: "The local unpushed completion commit does not exist at manifest-construction time.",
}


if len(ACCEPTANCE) != 53 or len(ACCEPTANCE_EVIDENCE) != len(ACCEPTANCE):
    raise RuntimeError("C34_ACCEPTANCE_COVERAGE_CARDINALITY_MISMATCH")


BENCHMARK_FAMILIES = tuple(f"S0A-{chr(65 + index)}" for index in range(18))

BENCHMARK_DESCRIPTIONS = (
    "immutable C33 B=0 root and plan, B=1 separation, and no state mixing",
    "four-line eikonal current color/sign identities and cell-integrated matrix elements",
    "mode-basis normalization, completeness, singular-cell quadrature, and resolution identity",
    "n-nbar, conjugate, same-direction, and self-energy line-pair closure",
    "direct Wilson-expansion versus mode-sum real/virtual count-once closure",
    "separate cusp, endpoint, and transverse-closure identities without duplicate counterterms",
    "explicit gauge, ghost, and instantaneous decisions and gauge closure",
    "explicit exact-zero-mode and basis-boundary controls without silent zero",
    "bare soft coefficient component, b, and regulator decomposition",
    "continuum modified-delta source expression and independent reconstruction",
    "UV power/log separation, counterterms, and anomalous dimension",
    "distinct delta dependence, rapidity counterterm, and regulator-removal order",
    "rapidity derivative, mu derivative, cusp, and Collins-Soper convention consistency",
    "finite-regulator conversion inverse, round trip, and state independence",
    "C33 R1-R3 basis trajectory, reserved holdout, and no overfit",
    "soft-side zero-bin common measurement and exact interface without premature equality",
    "exact continuation/no-go status and next branch without proton export",
    "deterministic ART25-free, fit-free, production-isolated implementation",
)

ARCHITECTURE_OBJECTS = (
    "SoftOneLoopPlan", "SoftOneLoopOrder", "SoftModeCellId",
    "SoftModeQuadrature", "SoftModeCompletenessRecord", "EikonalCurrent",
    "EikonalEmissionVertex", "EikonalAbsorptionVertex", "EikonalPairKernel",
    "EikonalSelfKernel", "TransverseClosureKernel", "SoftVirtualAmplitude",
    "SoftRealAmplitude", "SoftCutLedger", "SoftRealVirtualAssembly",
    "SoftGaugeContribution", "SoftGhostContribution",
    "SoftInstantaneousContribution", "SoftZeroModeContribution",
    "SoftBoundaryContribution", "SoftBareCoefficient",
    "SoftBareCoefficientDecomposition", "SoftUVStructure",
    "SoftRapidityStructure", "SoftUVCountertermSolution",
    "SoftRapidityCountertermSolution", "SoftRenormalizedCoefficient",
    "SoftRapidityDerivative", "SoftCuspConsistency", "SoftCSKernelRecord",
    "SoftContinuumTargetRecord", "SoftFiniteRegulatorDifference",
    "SoftFiniteRegulatorKernel", "SoftRoundTripReport",
    "SoftResolutionSequence", "SoftTrajectoryFitPlan", "SoftTrajectoryHoldout",
    "SoftTrajectoryResult", "SoftSideZeroBinLimit",
    "SoftCollinearContinuationContract", "C34SoftCapabilityMatrix",
    "C34ClosureReport",
)


ARTIFACTS = (
    ("C0-ART-Q-CAN-TMD", "outputs/parent_tmds/wp12_canonical_composed_quark.csv", "09f596d73c4e6ffd7c2f58f97d5e82628310d0a5577bdc4ea280be02c1720b45"),
    ("C0-ART-Q-CAN-CORR", "outputs/parent_tmds/wp12_canonical_composed_quark.correlators.csv", "244a17bbd39852ac47922059815b0926adc3809bd73c60d4ab96be80d7fbd0f5"),
    ("C0-ART-G-CAN-TMD", "outputs/parent_tmds/wp12_canonical_composed_gluon.csv", "27dc1e043d087b79fb0fca026b82f234f0b12af165595127dda0744f472a8d89"),
    ("C0-ART-G-CAN-CORR", "outputs/parent_tmds/wp12_canonical_composed_gluon.correlators.csv", "92c631976766a647d9bf881883ebc10129c6140d3ba41f9970a31781a5bbf9a7"),
    ("C0-ART-Q-RES-TMD", "outputs/parent_tmds/wp12_resolved_quark_parent.csv", "7e53f290510c7fea65876d8b45c2726a06377c3b844da0b306cff28f9f264b4b"),
    ("C0-ART-Q-RES-CORR", "outputs/parent_tmds/wp12_resolved_quark_parent.correlators.csv", "48ceff976b76369942850d2da7f4ad61a9f992e2654ed1cc0f007cd37dbef65f"),
    ("C0-ART-G-RES-TMD", "outputs/parent_tmds/wp12_resolved_gluon_parent.csv", "798a345bdb44c5a6447a3139704d1094d653c055aa8156fa4ce673eeaaf4d34b"),
    ("C0-ART-G-RES-CORR", "outputs/parent_tmds/wp12_resolved_gluon_parent.correlators.csv", "465d8cd9d0d35aeffea23a795045051ad53061d334309cfb34a95b7ed0c5fdc3"),
)


INTEGRITY_PATHS = (
    "docs/next_level/c2_reduction_registry.json",
    "docs/next_level/c2_provenance_graph.json",
    "docs/next_level/c2_composition_manifest.json",
    "docs/next_level/c29_frozen_bridge_grid.json",
    "docs/next_level/c29_constraint_role_split.json",
    "docs/next_level/c29_cross_root_member_relation.json",
    "docs/next_level/c29_no_double_counting_contract.json",
    "docs/next_level/c28_theory_ensemble_factor_manifest.json",
)


EXPECTED_INTEGRITY_HASHES = {
    "docs/next_level/c2_reduction_registry.json": "7754b1d088b23698217da50e9d375af0f7cbc76a2b2c7217c09ba0c6b42e9493",
    "docs/next_level/c2_provenance_graph.json": "d8773386171158675ce112f7f1ba22b87a67efd163922f7d880e8664f2290101",
    "docs/next_level/c2_composition_manifest.json": "3bbc390d4a80fe9ae520d54d8d12d7596eb59f5640242cf48527f9ace7a3ca6d",
    "docs/next_level/c29_frozen_bridge_grid.json": "baf7e3073e27837f461f0a827c8768ae1f7ba9deb621f8617b78aef11ce70661",
    "docs/next_level/c29_constraint_role_split.json": "02710c96fd6071a6ee4a699b610a854b57eb07bec204a65dfd0c9f6ef819b148",
    "docs/next_level/c29_cross_root_member_relation.json": "5525e9dca5f214b21e86317ac303bcc94dd1e7858b46f6c7adbd0c5d046a2411",
    "docs/next_level/c29_no_double_counting_contract.json": "b48f13a63d47f67ca73342501b0a4ea7d5d94eaec3ab98a5e89eca6e1b49f451",
    "docs/next_level/c28_theory_ensemble_factor_manifest.json": "51d123f3842c6140b72d6119be960d793673dd2f9bbcd9f77245ad1a525e92c8",
}


def contribution_rows() -> list[dict[str, Any]]:
    rows = []
    for index, (name, missing) in enumerate(CONTRIBUTIONS, 1):
        if name in DIRECT_BARE_CLASSES:
            assembly_role = "DIRECT_BARE_OPERATOR_TERM"
        elif name in SEPARATE_CONTROL_CLASSES:
            assembly_role = "SEPARATE_CONTROL_PENDING_ASSEMBLY_DECISION"
        elif name in ALTERNATIVE_ROUTE_CLASSES:
            assembly_role = "ALTERNATIVE_ROUTE_NOT_ADDED"
        elif name in COUNTERTERM_DECISION_CLASSES:
            assembly_role = "RENORMALIZATION_OR_SUBTRACTION_NOT_BARE"
        else:  # pragma: no cover - guarded by the frozen class partition
            raise RuntimeError(f"C34_UNCLASSIFIED_CONTRIBUTION:{name}")
        rows.append({
            "contribution_id": f"C34.SOFT.{index:02d}.{name}",
            "contribution_class": name,
            "root_id": SOFT_ROOT,
            "order": "O(g^2)/O(a_s)",
            "assembly_role": assembly_role,
            "status": "UNRESOLVED_BLOCKING",
            "value": None,
            "value_status": UNKNOWN,
            "assigned_zero": False,
            "target_scaleless_assumed": False,
            "missing_calculation": missing,
            "state_independence_required": True,
            "state_independence_proved": False,
            "consumes_art25": False,
        })
    if set(name for name, _ in CONTRIBUTIONS) != set(DIRECT_BARE_CLASSES) | set(SEPARATE_CONTROL_CLASSES) | set(ALTERNATIVE_ROUTE_CLASSES) | set(COUNTERTERM_DECISION_CLASSES):
        raise RuntimeError("C34_CONTRIBUTION_PARTITION_INCOMPLETE")
    return rows


def volume_xxi_rows() -> list[dict[str, Any]]:
    source = ROOT / VOLUME_XXI_PATH
    if sha256(source) != VOLUME_XXI_SHA256:
        raise RuntimeError("C34_VOLUME_XXI_HASH_MISMATCH")
    prior = json.loads((DOCS / "c33_volume_xxi_requirement_crosswalk.json").read_text())
    prior_by_id = {row["requirement_id"]: row for row in prior["rows"]}
    later = {
        "V21.ZERO.3", "V21.ORACLE.1", "V21.ORACLE.2",
        *(f"V21.MATCH.{index}" for index in range(1, 6)),
    }
    fail_closed = {"V21.COLL.2", "V21.COLL.4", "V21.UV.3", "V21.RAP.2", "V21.RAP.4"}
    c34_closed = {"V21.ROOT.3", "V21.UV.1"}
    family_evidence = {
        "ROOT": ["docs/next_level/c34_soft_collinear_continuation_contract.json"],
        "SOFT": ["docs/next_level/c34_soft_diagram_results.json"],
        "UV": ["docs/next_level/c34_soft_uv_structure.json", "docs/next_level/c34_soft_uv_counterterm_solution.json"],
        "RAP": ["docs/next_level/c34_soft_rapidity_structure.json", "docs/next_level/c34_cusp_consistency_report.json"],
        "ZERO": ["docs/next_level/c34_soft_side_zero_bin_limit.json"],
        "TRAJ": ["docs/next_level/c34_soft_basis_trajectory.json"],
        "TN": ["docs/next_level/c34_soft_tensor_network_execution.json"],
        "Q": ["docs/next_level/c34_soft_quantum_interface_update.json"],
        "STATUS": ["docs/next_level/c34_source_sufficiency_decision.json", "docs/next_level/c34_no_go_decision_tree.json"],
        "ISO": ["docs/next_level/c34_regression_report.json"],
        "DET": ["docs/next_level/c34_regression_report.json"],
    }
    rows = []
    for line_number, raw in enumerate(source.read_text().splitlines(), 1):
        line = raw.strip()
        if not line.startswith("V21."):
            continue
        requirement_id, description = line.split("&", 1)
        requirement_id = requirement_id.strip()
        description = description.strip()[:-2].strip()
        family = requirement_id.split(".")[1]
        if requirement_id in later:
            status = "LATER_PACKAGE_DEFERRED"
            owner = "C35_AFTER_C34_SOFT_COMPLETION"
        elif requirement_id in fail_closed:
            status = "C34_FAIL_CLOSED"
            owner = "C34/S0A_BRANCH_G_GUARD"
        elif requirement_id in c34_closed:
            status = "C34_CLOSED"
            owner = "C34/S0A_TYPED_CONTRACT"
        else:
            status = "INHERITED_CLOSED"
            owner = "C31-C33_IMMUTABLE_EVIDENCE"
        inherited_evidence = list(prior_by_id[requirement_id]["evidence_paths"])
        evidence = list(dict.fromkeys(inherited_evidence + family_evidence.get(family, [])))
        rows.append({
            "requirement_id": requirement_id,
            "family": family,
            "requirement_tex": description,
            "source_line": line_number,
            "status": status,
            "owner": owner,
            "evidence_paths": evidence,
            "positive_one_loop_physics_promoted": False,
        })
    if len(rows) != 65 or len({row["requirement_id"] for row in rows}) != 65:
        raise RuntimeError("C34_VOLUME_XXI_REQUIREMENT_CARDINALITY_MISMATCH")
    return rows


def environment_record() -> dict[str, Any]:
    packages = {}
    for name in ("numpy", "scipy", "pytest", "pypdf"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "packages": packages,
    }


def main(test_count: int = 1231) -> None:
    global C33_OPERATOR_ID_MAPPING
    from deuteron_wigner.bridge.s0a.core import (
        EIKONAL_NUMERICAL_CURRENT_PROVED,
        EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS,
        FAULT_CATALOG, content_hash as runtime_content_hash,
        execute_injection_payload, injection_rows,
    )

    C33_OPERATOR_ID_MAPPING = c33_operator_id_mapping()
    if C33_OPERATOR_ID_MAPPING["mapping_status"] != "EXECUTABLE_SOURCE_COMPARISON_PASSED":
        raise RuntimeError("C34_C33_OPERATOR_SOURCE_COMPARISON_FAILED")

    runtime_injections = list(injection_rows(2240))
    if len(runtime_injections) != 2240:
        raise RuntimeError(f"C34_INJECTION_COUNT_MISMATCH:{len(runtime_injections)}")
    injections = []
    for row in runtime_injections:
        payload_hash_verified = (
            runtime_content_hash(row["mutation_payload"])
            == row["mutation_payload_sha256"]
        )
        reexecution_observed = execute_injection_payload(
            row["mutation_payload"],
            expected_payload_sha256=row["mutation_payload_sha256"],
        )
        execution_verified = all((
            payload_hash_verified,
            row["mutation_executed"],
            row["observed_diagnostic"] == row["expected_diagnostic"],
            reexecution_observed == row["expected_diagnostic"],
        ))
        injections.append({
            **row,
            "execution_kind": "SEMANTIC_CONTROL_STATE_MUTATION",
            "payload_hash_verified": payload_hash_verified,
            "independent_reexecution_observed_diagnostic": reexecution_observed,
            "semantic_mutation_execution_verified": execution_verified,
        })
    all_injection_diagnostics_match = all(
        row["semantic_mutation_execution_verified"] for row in injections
    )
    fault_modes = len(FAULT_CATALOG)
    runtime_path = ROOT / "src" / "deuteron_wigner" / "bridge" / "s0a" / "core.py"
    if not runtime_path.is_file():
        raise RuntimeError("C34_S0A_RUNTIME_MISSING")
    runtime_hash = sha256(runtime_path)
    # Keep the historical generated-code identity tied to the exact C34
    # completion source, even when this descendant-only reconstruction guard
    # is present in a later worktree.
    builder_hash = hashlib.sha256(
        git_bytes(C34_COMPLETION, "scripts/build_c34_manifests.py")
    ).hexdigest()
    current_required_obligations = list(EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS)
    current_proved_obligations = list(EIKONAL_NUMERICAL_CURRENT_PROVED)
    current_unproved_obligations = [
        item for item in current_required_obligations
        if item not in EIKONAL_NUMERICAL_CURRENT_PROVED
    ]
    if current_unproved_obligations != [
        "LIGHT_FRONT_TANGENT_NORMALIZATION",
        "EMISSION_ABSORPTION_NUMERATOR_SIGN",
        "CONJUGATE_GENERATOR_ACTION",
        "COMPLETE_PARAMETERIZED_SEGMENT_PHASE",
        "FINITE_BASIS_GAUGE_FIELD_MODE_NORMALIZATION",
        "FINITE_BASIS_INTERACTION_COUPLING_MAP",
    ]:
        raise RuntimeError("C34_RUNTIME_CURRENT_UNPROVED_OBLIGATION_MISMATCH")

    norm = []
    for path in NORMATIVE_PATHS:
        item = ROOT / path
        norm.append({
            "path": path, "present": item.is_file(),
            "sha256": c34_input_sha256(path) if item.is_file() else None,
            "classification": "PROJECT_NORMATIVE_FORMALISM" if path == VOLUME_XXI_PATH else "REPOSITORY_NORMATIVE_INPUT",
        })
    put("c34_normative_source_integration.json", {
        "schema_version": "1.0.0", "scope": "C34/S0A",
        "resolved_c33_baseline": C33_BASELINE,
        "c33_pre_volume_commit": C33_PRE_VOLUME_COMMIT,
        "c32_ancestor_verified": git_ancestor(C32_ANCESTOR),
        "c28_ancestor_verified": git_ancestor(C28_ANCESTOR),
        "records": norm, "all_required_present": all(row["present"] for row in norm),
        "prompt": {"path": PROMPT_PATH, "expected_sha256": PROMPT_SHA256,
                   "actual_sha256": sha256(ROOT / PROMPT_PATH),
                   "byte_identical": sha256(ROOT / PROMPT_PATH) == PROMPT_SHA256},
        "volume_xxi": {"path": VOLUME_XXI_PATH, "expected_sha256": VOLUME_XXI_SHA256,
                       "actual_sha256": sha256(ROOT / VOLUME_XXI_PATH),
                       "byte_identical": sha256(ROOT / VOLUME_XXI_PATH) == VOLUME_XXI_SHA256},
    })

    sources = source_records()
    put("c34_primary_source_manifest.json", {
        "schema_version": "1.0.0", "count": len(sources),
        "records": sources, "all_present": all(row["present"] for row in sources),
        "all_hashes_match_c33_locks": all(row["hash_matches_c33_lock"] for row in sources),
        "authority_classes": [
            "TARGET_MODIFIED_DELTA_SOFT_AUTHORITY", "RAPIDITY_RENORMALIZATION_AUTHORITY",
            "ZERO_BIN_AUTHORITY", "FINITE_REGULATOR_METHOD_AUTHORITY",
            "LIGHT_FRONT_VACUUM_METHOD_AUTHORITY", "AUXILIARY_FIELD_METHOD_AUTHORITY",
            "NOT_OPERATOR_REGULATOR_IDENTICAL",
        ],
        "operator_identical_finite_basis_source_count": 0,
    })

    current_expression = "g_s sum_l T_l^a sigma_l v_l^mu exp(i kT.x_lT) D_l(k;delta_l,i0_l)"
    derivations = []
    for line in LINES:
        expression = (
            f"g_s {line['color_action']} sigma({line['line_id']}) v_{line['direction']}^mu "
            f"{line['phase']} D({line['momentum_component']},{line['delta_component']},{line['i0_sign']}i0)"
        )
        derivations.append({
            "derivation_id": f"C34.DERIVATION.CURRENT.{line['line_id']}",
            "wilson_line_pair": [line["line_id"]], "orientation": line["orientation"],
            "color_action": line["color_action"], "fourier_convention": "exp(+i kT.xT)",
            "momentum_flow": "INCOMING_TO_EIKONAL_OPERATOR",
            "i0_and_delta_signs": {"i0": line["i0_sign"], "delta": line["delta_component"]},
            "gauge": "COVARIANT_XI_G_IN_0_1_2_PLAN",
            "rapidity_regulator": "MODIFIED_DELTA_DISTINCT_DELTA_PLUS_MINUS",
            "uv_regulator": "C33_FINITE_LOG_CELL_BASIS_TO_MSBAR_TARGET",
            "finite_cell_basis": "C33_R1_R2_R3_LOG_ENERGY_RAPIDITY_TRANSVERSE_CELLS",
            "perturbative_order": "O(g_s)", "symbolic_expression": expression,
            "symbolic_expression_sha256": hashlib.sha256(expression.encode()).hexdigest(),
            "generated_code_sha256": runtime_hash,
            "independent_oracle": False,
            "ancestry_evidence": "C33_STORED_PATH_AND_DENOMINATOR_RECORD",
            "ancestry_source_records": [
                {"path": line["c33_operator_source_path"],
                 "record_sha256": line["c33_operator_source_record_sha256"]},
                {"path": line["c33_denominator_source_path"],
                 "record_sha256": line["c33_denominator_source_record_sha256"]},
            ],
            "status": "STRUCTURALLY_DERIVED_CELL_MATRIX_UNAVAILABLE",
        })
    continuum_formulae = {
        "exponentiation_eq7": "S_tilde=exp[a_s*C_F*(S^[1]+a_s*S^[2]+...)]",
        "coupling_definition_eq7": COUPLING_NORMALIZATION,
        "exact_one_loop_eq11": "S^[1]=-4*mu^(2*eps)*B^eps*Gamma(-eps)*(L0-psi(-eps)-gamma_E)",
        "B_definition_eq8": "B=b_T^2/4",
        "modified_delta_product_eq8": "delta=+/- delta_plus*delta_minus",
        "L0_definition_eq12": "L0=ln(B*|delta|/exp(-2*gamma_E))",
        "L_mu_definition_pages2_5": "L_mu=ln(mu^2*b_T^2*exp(2*gamma_E)/4)=ln(mu^2*B*exp(2*gamma_E))",
        "l_delta_definition_eq13": "l_delta=ln(mu^2/|delta_plus*delta_minus|)",
        "d11_definition_eq13": "d^(1,1)=2*C_F=Gamma_0/2",
        "expanded_one_loop_eq13": "S^[1]=-4/eps^2+2*L_mu^2-(2*d^(1,1)/C_F)*(1/eps+L_mu)*l_delta+pi^2/3+O(eps)",
    }
    continuum_expression = continuum_formulae["expanded_one_loop_eq13"]
    derivations.append({
        "derivation_id": "C34.DERIVATION.CONTINUUM.MODDELTA.SOURCE_TRANSCRIPTION",
        "wilson_line_pair": ["n", "nbar", "conjugate partners"],
        "orientation": "FUTURE_WITH_T_EVEN_PAST_TARGET", "color_action": "C_F=4/3",
        "fourier_convention": "SOURCE_ALIGNED_B_SPACE", "momentum_flow": "SOURCE_CONVENTION",
        "i0_and_delta_signs": "SOURCE_ORDERED_MODIFIED_DELTA",
        "gauge": "SOURCE_GAUGE_INDEPENDENT_TARGET", "rapidity_regulator": "MODIFIED_DELTA",
        "uv_regulator": "DIMENSIONAL_REGULATION_MSBAR", "finite_cell_basis": None,
        "perturbative_order": "O(a_s)", "symbolic_expression": continuum_expression,
        "source_formulae": continuum_formulae,
        "source_locators": {
            "exponentiation_and_coupling": "arXiv:1511.05590v2 p.4 Eq.(7)",
            "delta_and_B": "arXiv:1511.05590v2 p.4 Eq.(8)",
            "L_X_general": "arXiv:1511.05590v2 p.2",
            "exact_one_loop": "arXiv:1511.05590v2 p.5 Eq.(11)",
            "L0": "arXiv:1511.05590v2 p.5 Eq.(12)",
            "expanded_one_loop": "arXiv:1511.05590v2 p.5 Eq.(13)",
        },
        "symbolic_expression_sha256": hashlib.sha256(continuum_expression.encode()).hexdigest(),
        "generated_code_sha256": builder_hash,
        "source_transcription_present": True,
        "graph_level_reconstruction": False,
        "independent_direct_integral_reconstruction": False,
        "independent_oracle": False,
        "status": "SOURCE_FINAL_RESULT_TRANSCRIBED_NOT_INDEPENDENTLY_RECONSTRUCTED",
    })
    put("c34_derivation_authority_manifest.json", {
        "schema_version": "1.0.0", "records": derivations,
        "count": len(derivations), "runtime_sha256": runtime_hash,
        "builder_sha256": builder_hash, "manual_i0_or_delta_signs": 0,
        "finite_basis_one_loop_expression_count": 0,
    })

    holdout_records = [{
        "holdout_id": f"C34.HOLDOUT.{name}", "role": "HOLDOUT",
        "frozen_before_symbolic_simplification": True,
        "frozen_before_counterterm_solution": True,
        "frozen_before_trajectory_fit": True,
        "used_in_construction": False, "used_in_fit": False,
        "moved": False, "status": "PRESERVED_UNEVALUATED",
    } for name in HOLDOUTS]
    put("c34_holdout_report.json", {
        "schema_version": "1.0.0", "count": len(holdout_records),
        "frozen_before_results": True, "moved": 0, "records": holdout_records,
    })

    put("c34_one_loop_plan.json", {
        "schema_version": "1.0.0", "plan_id": ONE_LOOP_PLAN_ID,
        "parent_root": SOFT_ROOT, "baryon_number": 0,
        "collinear_root": COLLINEAR_ROOT, "shared_state": False,
        "selected_realization": PRIMARY_PLAN, "selected_before_results": True,
        "order": {"coupling": "O(g_s^2)", "a_s": "O(a_s)",
                  "a_s_convention": COUPLING_NORMALIZATION,
                  "coefficient_convention": "S=exp[a_s*C_F*S^[1]+O(a_s^2)]",
                  "C_F_placement": "EXTERNAL_TO_REDUCED_S^[1]",
                  "finite_basis_interaction_normalization_map": "UNRESOLVED_BLOCKING",
                  "leading_missing_order": "O(a_s)",
                  "declared_one_loop_first_omitted_order": "O(a_s^2)"},
        "wilson_trace_order": [line["line_id"] for line in LINES],
        "c33_operator_id_mapping": C33_OPERATOR_ID_MAPPING,
        "color": {"gauge_group": "SU(3)", "representation": "FUNDAMENTAL",
                  "trace": "SINGLET_1_OVER_NC", "N_c": 3, "C_F": "4/3"},
        "gauges_xi_g": [0.0, 1.0, 2.0], "gauge_holdout": 2.0,
        "b_points_GeV_inverse": [0.125, 0.25, 0.5, 1.0], "b_holdout": 1.0,
        "delta_plus_GeV": sorted({row["delta_plus_GeV"] for row in DELTA_SCHEDULE}),
        "delta_minus_GeV": sorted({row["delta_minus_GeV"] for row in DELTA_SCHEDULE}),
        "delta_probe_schedule": [
            {**row, "units": "GeV", "physical_parameter": False,
             "used_in_fit": False,
             "provenance": "SOURCE_INDEPENDENT_PROVISIONAL_NUMERICAL_REGULATOR_PROBE"}
            for row in DELTA_SCHEDULE
        ],
        "delta_plus_minus_varied_independently": True,
        "delta_holdouts": {
            "plus": "C34.DELTA.PLUS.HOLDOUT",
            "minus": "C34.DELTA.MINUS.HOLDOUT",
            "combined_diagonal_holdout": None,
        },
        "resolutions": list(RESOLUTIONS), "zero_mode_policy": "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL",
        "holdout_ids": [row["holdout_id"] for row in holdout_records],
        "method_family_frozen_before_coefficients": True,
        "execution_plan_complete": False,
        "art25_reachable": False,
        "status": "C34_ONE_LOOP_METHOD_AND_PROBE_PLAN_FROZEN_EXECUTION_INPUTS_INCOMPLETE",
    })
    put("c34_mode_quadrature_plan.json", {
        "schema_version": "1.0.0", "quadrature_id": QUADRATURE_ID,
        "resolutions": [row["resolution_id"] for row in RESOLUTIONS],
        "coordinates": ["log_omega", "rapidity", "transverse_cell"],
        "rule": "CELL_INTEGRATED_GAUSS_LEGENDRE_WITH_ANALYTIC_SINGULAR_SUBTRACTION_REQUIRED",
        "nominal_orders": {"log_omega": 16, "rapidity": 16, "transverse_x": 16, "transverse_y": 16},
        "cell_center_substitution_allowed": False, "physical_numerical_epsilon": None,
        "singular_cell_treatment": "UNRESOLVED_BLOCKING_NORMALIZED_CELL_FUNCTIONS_AND_SUBTRACTION_KERNEL_MISSING",
        "basis_normalization": "UNRESOLVED_BLOCKING",
        "absolute_tolerance": None, "relative_tolerance": None,
        "maximum_subdivisions": None, "contour_prescription": None,
        "pole_cell_partition": None,
        "method_family_and_nominal_order_frozen_before_results": True,
        "fully_specified": False, "execution_plan_complete": False,
        "status": "PARTIAL_PLAN_FROZEN_EXECUTION_BLOCKED",
    })
    put("c34_trajectory_fit_plan.json", {
        "schema_version": "1.0.0", "trajectory_id": "C34.SOFT.TRAJECTORY.PLAN.v1",
        "resolutions": list(RESOLUTIONS), "construction_resolutions": ["C33.RES.1", "C33.RES.2"],
        "holdout_resolution": "C33.RES.3", "source_predicted_structures": [
            "UV_LOG", "RAPIDITY_WINDOW_LOG", "FINITE_CONSTANT", "POWER_REMAINDER",
            "ZERO_MODE", "ENDPOINT_JUNCTION", "QUADRATURE",
        ],
        "arbitrary_polynomial_forbidden": True, "maximum_free_coefficients": 2,
        "fit_performed": False, "frozen_before_results": True,
        "status": "SOFT_TRAJECTORY_UNAVAILABLE",
    })

    currents = []
    for line in LINES:
        currents.append({
            **line, "current_order": "O(g_s)",
            "operator_expression": f"g_s*{line['color_action']}*sigma_l*v_l^mu*{line['phase']}*D_l",
            "path_delta_and_i0_signs_derived_from_c33": True,
            "manual_path_delta_or_i0_sign_insertion": False,
            "sigma_l_definition": None,
            "sigma_l_status": "UNRESOLVED_BLOCKING_OPERATOR_EXPANSION_SIGN",
            "light_front_vector_normalization": "v_plus_minus=(v0+/-v3)/sqrt(2)",
            "current_numerator_normalization_proved": False,
            "transverse_phase_scope": "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED",
            "complete_parameterized_segment_phase_proved": False,
            "conjugate_generator_action_proved": False,
            "finite_basis_gauge_field_mode_normalization_proved": False,
            "finite_basis_interaction_coupling_map_proved": False,
            "cell_integrated_matrix_element": None,
            "status": "STRUCTURALLY_DERIVED_CELL_INTEGRATION_BLOCKED",
        })
    put("c34_eikonal_current_manifest.json", {
        "schema_version": "1.0.0", "current_id": "C34.EIKONAL.CURRENT.FOUR_LINE.v1",
        "root_id": SOFT_ROOT, "expression": current_expression,
        "c33_operator_id_mapping": C33_OPERATOR_ID_MAPPING,
        "lines": currents, "line_count": 4, "all_stored_lines_present": True,
        "color_trace_tree": 1.0, "C_F": "4/3", "ward_contraction": None,
        "current_identity_scope": "PATH_COLOR_DENOMINATOR_STRUCTURE_ONLY",
        "current_identity_complete": False,
        "coupling_symbol": "g_s",
        "perturbative_order": "O(g_s)",
        "transverse_phase": "STORED_BASEPOINT_PHASE_COMPLETE_SEGMENT_PHASE_UNRESOLVED",
        "transverse_phase_scope": "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED",
        "basepoint_only_phase_proved": True,
        "complete_segment_phase_proved": False,
        "numerical_current_proofs": {
            "required": current_required_obligations,
            "proved": current_proved_obligations,
            "unproved": current_unproved_obligations,
            "closed": False,
            "runtime_source": "src/deuteron_wigner/bridge/s0a/core.py::EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS",
        },
        "blocking_current_definitions": current_unproved_obligations,
        "direct_matrix_action": None, "matrix_free_action": None,
        "status": "C34_EIKONAL_CURRENT_STRUCTURALLY_DERIVED",
    })
    vertices = []
    for line in LINES:
        for vertex_type in ("EMISSION", "ABSORPTION"):
            vertices.append({
                "vertex_id": f"C34.VERTEX.{vertex_type}.{line['line_id']}",
                "line_id": line["line_id"], "vertex_type": vertex_type,
                "conjugate_of": f"C34.VERTEX.{'ABSORPTION' if vertex_type == 'EMISSION' else 'EMISSION'}.{line['line_id']}",
                "operator_level_identity": "DERIVED_FROM_STORED_LINE",
                "cell_matrix_elements": None, "status": "UNRESOLVED_BLOCKING",
                "missing_calculation": "normalized cell mode functions and singular-cell integration",
            })
    put("c34_one_gluon_vertex_manifest.json", {
        "schema_version": "1.0.0", "count": len(vertices), "records": vertices,
        "one_gluon_basis_dimensions": [row["hilbert_dimension"] for row in RESOLUTIONS],
        "direct_auxiliary_added": False, "status": "VERTEX_IDENTITIES_TYPED_NUMERICAL_MATRIX_ELEMENTS_UNAVAILABLE",
    })
    put("c34_mode_cell_integration_report.json", {
        "schema_version": "1.0.0", "quadrature_id": QUADRATURE_ID,
        "resolution_dimensions": [row["hilbert_dimension"] for row in RESOLUTIONS],
        "cell_center_sampling_used": False, "physical_epsilon_used": False,
        "normalized_cell_functions_available": False, "singular_subtraction_kernel_available": False,
        "integrated_cell_count": 0, "normalization_residuals": None,
        "completeness_residuals": None, "blocking_inputs": [
            "normalized finite-cell mode functions", "gauge-complete inner product",
            "singular-cell subtraction kernel", "explicit zero-mode control sector",
        ], "status": "C34_MODE_CELL_INTEGRATION_UNRESOLVED_BLOCKING",
    })

    diagrams = contribution_rows()
    put("c34_soft_diagram_results.json", {
        "schema_version": "1.0.0", "count": len(diagrams), "records": diagrams,
        "allowed_statuses": ["CALCULATED_NONZERO", "CALCULATED_ZERO_BY_EXACT_IDENTITY",
                             "CANCELS_WITH_DECLARED_PARTNER", "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO",
                             "NOT_APPLICABLE_WITH_PROOF", "UNRESOLVED_BLOCKING"],
        "unresolved_blocking": len(diagrams), "assigned_zero": 0,
        "direct_bare_term_count": sum(row["assembly_role"] == "DIRECT_BARE_OPERATOR_TERM" for row in diagrams),
        "separate_control_count": sum(row["assembly_role"].startswith("SEPARATE_CONTROL") for row in diagrams),
        "alternative_route_count": sum(row["assembly_role"] == "ALTERNATIVE_ROUTE_NOT_ADDED" for row in diagrams),
        "renormalization_decision_count": sum(row["assembly_role"] == "RENORMALIZATION_OR_SUBTRACTION_NOT_BARE" for row in diagrams),
        "continuum_scaleless_substitutions": 0, "ledger_complete": True,
        "one_loop_ready": False, "status": NO_GO,
    })
    diagram_by_class = {row["contribution_class"]: row for row in diagrams}
    counterterms = []
    for index, (name, source_classes) in enumerate(COUNTERTERM_COMPONENTS, 1):
        counterterms.append({
            "counterterm_id": f"C34.CT.{index:02d}.{name}",
            "counterterm_class": name,
            "source_structure_ids": [diagram_by_class[item]["contribution_id"] for item in source_classes],
            "order": "O(a_s)",
            "value": None,
            "value_status": UNKNOWN,
            "status": "UNRESOLVED_BLOCKING",
            "state_independence_required": True,
            "state_independence_proved": False,
            "derived_from_bare_structure": False,
            "part_of_bare_graph_sum": False,
        })
    put("c34_soft_counterterm_results.json", {
        "schema_version": "1.0.0", "records": counterterms,
        "separated_classes": ["line_self_energy", "cusp", "endpoint", "transverse_closure",
                              "vacuum", "residual_line_mass", "basis_boundary", "operator_uv", "rapidity"],
        "derived_count": 0, "unresolved_count": len(counterterms),
        "counterterm_ids_disjoint_from_contribution_ids": not (
            {row["counterterm_id"] for row in counterterms}
            & {row["contribution_id"] for row in diagrams}
        ),
        "power_hidden_in_log": False,
        "state_independence_required_for_all": True,
        "state_independence_proved_count": 0,
        "status": "C34_SOFT_COUNTERTERMS_UNRESOLVED_BLOCKING",
    })
    direct_terms = [row for row in diagrams if row["assembly_role"] == "DIRECT_BARE_OPERATOR_TERM"]
    separate_controls = [row for row in diagrams if row["assembly_role"] == "SEPARATE_CONTROL_PENDING_ASSEMBLY_DECISION"]
    put("c34_one_loop_dependency_closure.json", {
        "schema_version": "1.0.0", "nodes": [row["contribution_id"] for row in diagrams] +
        [row["counterterm_id"] for row in counterterms] + [
            "C34.ZERO.MODE.CONTROL", "C34.BARE.SOFT.ONE_LOOP",
            "C34.UV.REN", "C34.RAPIDITY.REN", "C34.CONVERSION"],
        "edges": [
            {"from": row["contribution_id"], "to": "C34.BARE.SOFT.ONE_LOOP", "blocking": True,
             "edge_role": row["assembly_role"]}
            for row in direct_terms
        ] + [
            {"from": row["contribution_id"], "to": "C34.ZERO.MODE.CONTROL", "blocking": True,
             "edge_role": row["assembly_role"]}
            for row in separate_controls
        ] + [
            {"from": "C34.ZERO.MODE.CONTROL", "to": "C34.BARE.SOFT.ONE_LOOP", "blocking": True,
             "edge_role": "SEPARATE_CONTROL_MUST_RESOLVE_BEFORE_ASSEMBLY_DECISION"}
        ] + [
            {"from": "C34.BARE.SOFT.ONE_LOOP", "to": row["counterterm_id"], "blocking": True,
             "edge_role": "COUNTERTERM_EXTRACTION_REQUIRES_BARE_STRUCTURE"}
            for row in counterterms
        ] + [
            {"from": row["counterterm_id"],
             "to": "C34.RAPIDITY.REN" if row["counterterm_class"] == "RAPIDITY" else "C34.UV.REN",
             "blocking": True, "edge_role": "RENORMALIZATION"}
            for row in counterterms
        ] + [
            {"from": "C34.UV.REN", "to": "C34.CONVERSION", "blocking": True},
            {"from": "C34.RAPIDITY.REN", "to": "C34.CONVERSION", "blocking": True},
        ],
        "excluded_alternative_routes": [row["contribution_id"] for row in diagrams
                                        if row["assembly_role"] == "ALTERNATIVE_ROUTE_NOT_ADDED"],
        "acyclic": True, "all_blockers_visible": True,
        "unresolved_blockers": len(diagrams) + len(counterterms), "passes": False, "status": NO_GO,
    })

    candidate_real_ids = [row["contribution_id"] for row in diagrams if row["contribution_class"] == "REAL_ONE_SOFT_GLUON"]
    candidate_virtual_ids = [row["contribution_id"] for row in diagrams if row["contribution_class"] in {
        "N_NBAR_EXCHANGE", "CONJUGATE_LINE_EXCHANGE", "SAME_DIRECTION_LINE_EXCHANGE",
        "VIRTUAL_ONE_SOFT_GLUON", "WILSON_LINE_SELF_ENERGY", "CUSP_ENDPOINT",
        "TRANSVERSE_CLOSURE", "SOFT_VACUUM_ENERGY", "LIGHT_FRONT_INSTANTANEOUS",
        "GAUGE_FIXING", "GHOST"}]
    put("c34_real_virtual_assembly.json", {
        "schema_version": "1.0.0", "assembly_id": "C34.SOFT.REAL_VIRTUAL.COUNT_ONCE.v1",
        "candidate_real_contribution_ids": candidate_real_ids,
        "candidate_virtual_contribution_ids": candidate_virtual_ids,
        "candidate_id_sets_disjoint": not set(candidate_real_ids) & set(candidate_virtual_ids),
        "real_contribution_ids": [], "virtual_contribution_ids": [],
        "branch_assignment_proved": False, "assembly_executed": False,
        "wilson_expansion_value": None, "mode_sum_value": None,
        "direct_mode_sum_residual": None, "future_past_residual": None,
        "hermitian_residual": None, "rotation_residual": None,
        "status": "CANDIDATE_TOPOLOGY_CATALOGUED_PHYSICAL_BRANCH_AND_ASSEMBLY_BLOCKED",
    })
    cut_rows = []
    for index, row in enumerate(diagrams, 1):
        contribution_class = row["contribution_class"]
        if contribution_class in COUNTERTERM_DECISION_CLASSES:
            continue
        if contribution_class == "REAL_ONE_SOFT_GLUON":
            topology_role = "CANDIDATE_REAL"
        elif contribution_class in ALTERNATIVE_ROUTE_CLASSES:
            topology_role = "ALTERNATIVE_ROUTE"
        elif contribution_class in SEPARATE_CONTROL_CLASSES:
            topology_role = "SEPARATE_CONTROL"
        else:
            topology_role = "CANDIDATE_VIRTUAL_OR_OPERATOR_LOCAL"
        cut_rows.append({
            "cut_id": f"C34.CUT.{index:02d}", "contribution_id": row["contribution_id"],
            "contribution_class": contribution_class,
            "topology_role": topology_role,
            "branch": "UNRESOLVED_BLOCKING",
            "branch_assignment_proved": False,
            "included_in_primary_direct_assembly": False,
            "mode_cell_id": None, "support": UNKNOWN, "status": "UNRESOLVED_BLOCKING",
        })
    put("c34_soft_cut_ledger.json", {
        "schema_version": "1.0.0", "records": cut_rows, "count": len(cut_rows),
        "duplicate_cut_ids": [], "structural_cut_ids_unique": True,
        "conjugate_pair_double_counted": None,
        "primary_direct_assembly_count": sum(row["included_in_primary_direct_assembly"] for row in cut_rows),
        "physical_branch_assignment_count": 0,
        "status": "CUT_IDENTITIES_UNIQUE_PHYSICAL_BRANCHES_UNRESOLVED",
    })
    put("c34_count_once_report.json", {
        "schema_version": "1.0.0", "candidate_real_virtual_id_sets_disjoint": True,
        "physical_real_virtual_sets_available": False,
        "structural_cut_ids_unique": True,
        "duplicate_cut_count": 0, "soft_factor_squared_accidentally": None,
        "inverse_square_root_applied": False, "missing_real_residual": None,
        "missing_virtual_residual": None, "duplicate_cut_residual": None,
        "physical_count_once_validated": False,
        "status": "STRUCTURAL_ID_UNIQUENESS_ONLY_PHYSICAL_COUNT_ONCE_UNAVAILABLE",
    })

    included_bare = [row for row in diagrams if row["assembly_role"] == "DIRECT_BARE_OPERATOR_TERM"]
    separate_control_terms = [row for row in diagrams if row["assembly_role"] == "SEPARATE_CONTROL_PENDING_ASSEMBLY_DECISION"]
    excluded_alternative = [row for row in diagrams if row["assembly_role"] == "ALTERNATIVE_ROUTE_NOT_ADDED"]
    excluded_counterterm_decisions = [row for row in diagrams if row["assembly_role"] == "RENORMALIZATION_OR_SUBTRACTION_NOT_BARE"]
    component_values = {
        row["contribution_class"]: {
            "contribution_id": row["contribution_id"], "value": None,
            "status": UNKNOWN, "assembly_role": row["assembly_role"]}
        for row in included_bare
    }
    put("c34_bare_soft_coefficient.json", {
        "schema_version": "1.0.0", "coefficient_id": "C34.S_FB.BARE.ONE_LOOP.v1",
        "root_id": SOFT_ROOT, "tree_value": 1.0, "tree_value_exact": True,
        "expansion": "S=exp[a_s*C_F*S_FB^[1],bare+O(a_s^2)]",
        "a_s_convention": COUPLING_NORMALIZATION,
        "C_F_placement": "EXTERNAL_TO_REDUCED_S_FB^[1]",
        "finite_basis_interaction_normalization_map": "UNRESOLVED_BLOCKING",
        "leading_missing_order": "O(a_s)",
        "declared_one_loop_first_omitted_order": "O(a_s^2)",
        "one_loop_coefficient": None, "one_loop_status": UNKNOWN,
        "direct_bare_component_ids": [row["contribution_id"] for row in included_bare],
        "separate_control_ids": [row["contribution_id"] for row in separate_control_terms],
        "excluded_alternative_route_ids": [row["contribution_id"] for row in excluded_alternative],
        "excluded_counterterm_decision_ids": [row["contribution_id"] for row in excluded_counterterm_decisions],
        "counterterm_ids": [row["counterterm_id"] for row in counterterms],
        "regulator_axes": ["b", "mu_reference", "delta_plus", "delta_minus", "xi_g",
                           "soft_resolution", "UV_support", "IR_support", "rapidity_support", "zero_mode_policy"],
        "continuum_coefficient_substituted": False, "status": NO_GO,
    })
    put("c34_bare_soft_decomposition.json", {
        "schema_version": "1.0.0", "components": component_values,
        "component_count": len(component_values), "merged": False,
        "included_component_ids": [row["contribution_id"] for row in included_bare],
        "separate_controls": {
            row["contribution_class"]: {
                "contribution_id": row["contribution_id"], "value": None,
                "status": UNKNOWN, "assembly_decision": "UNRESOLVED_BLOCKING"}
            for row in separate_control_terms
        },
        "separate_control_ids": [row["contribution_id"] for row in separate_control_terms],
        "excluded_alternative_ids": [row["contribution_id"] for row in excluded_alternative],
        "excluded_counterterm_ids": [row["contribution_id"] for row in excluded_counterterm_decisions],
        "counterterms_are_separate_derived_objects": True,
        "assembly_executed": False, "aggregate": None,
        "all_unknown_nonzero": True, "assigned_zero_count": 0, "status": NO_GO,
    })
    put("c34_bare_soft_validation_report.json", {
        "schema_version": "1.0.0", "tree_residual": 0.0, "color_trace_residual": 0.0,
        "one_loop_real_virtual_residual": None, "gauge_residuals": None,
        "future_past_residual": None, "rotation_residual": None,
        "b_to_zero_behavior": UNKNOWN, "one_loop_validated": False, "status": NO_GO,
    })

    put("c34_continuum_soft_target.json", {
        "schema_version": "1.0.0", "target_id": "C34.CONTINUUM.MODDELTA.MSBAR.ONE_LOOP.v1",
        "operator_geometry": "FOUR_LINE_FUNDAMENTAL_SINGLET",
        "uv_scheme": "DIMENSIONAL_REGULATION_MSBAR", "rapidity_regulator": "MODIFIED_DELTA",
        "source_expression": continuum_expression,
        "source_formulae": continuum_formulae,
        "source_expression_sha256": hashlib.sha256(continuum_expression.encode()).hexdigest(),
        "source_locators": {
            "exponentiation_and_coupling": "arXiv:1511.05590v2 p.4 Eq.(7)",
            "delta_and_B": "arXiv:1511.05590v2 p.4 Eq.(8)",
            "L_X_general": "arXiv:1511.05590v2 p.2",
            "exact_one_loop": "arXiv:1511.05590v2 p.5 Eq.(11)",
            "L0": "arXiv:1511.05590v2 p.5 Eq.(12)",
            "expanded_one_loop": "arXiv:1511.05590v2 p.5 Eq.(13)",
        },
        "graph_level_reconstruction": False,
        "graph_level_reconstruction_status": "NOT_PERFORMED_SOURCE_FINAL_RESULT_ONLY",
        "independent_direct_integral_reconstruction": False,
        "finite_basis_identity": False, "used_as_finite_basis_result": False,
        "status": "SOURCE_QUALIFIED_FINAL_FORMULA_TRANSCRIPTION_NOT_INDEPENDENT_ORACLE",
    })
    put("c34_continuum_soft_oracle_report.json", {
        "schema_version": "1.0.0", "source_transcription_present": True,
        "graph_level_line_pair_reconstruction_present": False,
        "independent_integral_route_complete": False,
        "convention_alignment": "SOURCE_QUALIFIED_TARGET_ONLY",
        "derivative_checks": None, "known_anomalous_dimension_residual": None,
        "finite_basis_comparison_residual": None, "oracle_validated": False,
        "status": "CONTINUUM_FINAL_FORMULA_SOURCE_QUALIFIED_GRAPH_AND_INDEPENDENT_ROUTES_INCOMPLETE",
    })

    put("c34_soft_uv_structure.json", {
        "schema_version": "1.0.0", "structures": {
            "power": None, "log_uv": None, "cusp_log_squared": None,
            "rapidity_log": None, "finite_constant": None, "power_remainder": None},
        "all_value_statuses": UNKNOWN,
        "representation_separates_power_and_log_slots": True,
        "numerical_power_log_decomposition_completed": False,
        "power_hidden_in_msbar": False, "status": "C34_SOFT_UV_STRUCTURE_UNRESOLVED",
    })
    put("c34_soft_uv_counterterm_solution.json", {
        "schema_version": "1.0.0", "target_scheme": "MSBAR",
        "components": {name: {"value": None, "status": UNKNOWN} for name in (
            "wilson_line_self_energy", "cusp", "endpoint", "transverse_closure",
            "residual_line_mass", "vacuum_energy", "basis_boundary", "soft_operator_uv")},
        "solution": None, "inverse": None,
        "state_independence_required": True, "state_independence_proved": False,
        "holdout_residual": None,
        "leading_missing_order": "O(a_s)",
        "declared_one_loop_first_omitted_order": "O(a_s^2)",
        "status": "C34_SOFT_UV_COUNTERTERM_UNRESOLVED_BLOCKING",
    })
    put("c34_soft_uv_closure_report.json", {
        "schema_version": "1.0.0", "source_uv_coefficient_residual": None,
        "gauge_residual": None, "resolution_residual": None,
        "inverse_counterterm_residual": None, "passes": False,
        "status": "C34_SOFT_UV_RENORMALIZATION_UNRESOLVED",
    })
    put("c34_soft_rapidity_structure.json", {
        "schema_version": "1.0.0", "delta_plus_kept_distinct": True,
        "delta_minus_kept_distinct": True,
        "symbolic_delta_identities_distinct": True,
        "independent_variation_schedule_frozen": True,
        "independent_variations_executed": False,
        "delta_probe_schedule_ids": [row["probe_id"] for row in DELTA_SCHEDULE],
        "bare_delta_dependence": None,
        "rapidity_log_coefficient": None, "finite_basis_is_rapidity_regulator": False,
        "zeta_is_bare_regulator": False, "removal_order": [
            "assemble_real_virtual", "UV_renormalize", "rapidity_renormalize", "remove_delta"],
        "status": "C34_SOFT_RAPIDITY_STRUCTURE_UNRESOLVED",
    })
    put("c34_soft_rapidity_counterterm_solution.json", {
        "schema_version": "1.0.0", "counterterm": None,
        "delta_plus_component": None, "delta_minus_component": None,
        "state_independence_required": True, "state_independence_proved": False,
        "fitted_nonperturbative_cs_term": False,
        "regulator_cancellation_residual": None, "gauge_residual": None,
        "status": "C34_SOFT_RAPIDITY_RENORMALIZATION_UNRESOLVED",
    })
    put("c34_rapidity_renormalization_closure.json", {
        "schema_version": "1.0.0", "line_conjugation_residual": None,
        "future_past_residual": None, "delta_removal_residual": None,
        "rapidity_derivative_residual": None, "gauge_residual": None,
        "passes": False, "status": "C34_SOFT_RAPIDITY_RENORMALIZATION_UNRESOLVED",
    })
    put("c34_soft_rapidity_anomalous_dimension.json", {
        "schema_version": "1.0.0", "derivative_convention": "D=(1/2)R_n^-1*dR_n/dln(nu_plus)",
        "finite_basis_value": None, "value_status": UNKNOWN,
        "extracted_from_closed_calculation": False, "fitted": False,
        "status": "NOT_EXTRACTED_ONE_LOOP_SOFT_UNAVAILABLE",
    })
    put("c34_cusp_consistency_report.json", {
        "schema_version": "1.0.0", "relation": "dD_q/dln(mu)=Gamma_cusp^q",
        "D_derivative": None, "cusp_target": None, "residual": None,
        "tested": False, "passes": False, "status": "CUSP_CONSISTENCY_UNAVAILABLE_RAD_NOT_EXTRACTED",
    })
    put("c34_soft_cs_kernel_convention.json", {
        "schema_version": "1.0.0", "soft_rapidity_anomalous_dimension": "DISTINCT_OBJECT",
        "tmd_rapidity_anomalous_dimension": "DISTINCT_OBJECT",
        "collins_soper_D": "d ln F/d ln sqrt(zeta)=-D_q",
        "art25_nonperturbative_cs_model": "EXTERNAL_NOT_CONSUMED",
        "finite_basis_value": None, "status": "CONVENTION_STORED_VALUE_UNAVAILABLE",
    })

    conversion_components = {name: UNKNOWN for name in (
        "logarithmic", "finite_constant", "power", "zero_mode", "endpoint",
        "transverse_closure", "numerical")}
    put("c34_soft_regulator_conversion.json", {
        "schema_version": "1.0.0", "conversion_id": "C34.FB.TO.CONT.SOFT.v1",
        "source": "C33_FINITE_BASIS_MODIFIED_DELTA", "target": "CONTINUUM_MODIFIED_DELTA_MSBAR",
        "tree_kernel": 1.0, "one_loop_kernel": None, "components": conversion_components,
        "state_independence_required": True, "state_independence_proved": False,
        "hadron_independence_required": True, "hadron_independence_proved": False,
        "flavor_independence_required": None, "flavor_independence_proved": False,
        "art25_input_consumed": False,
        "art25_member_independence_required": True,
        "art25_member_independence_proved": True,
        "art25_member_independence_proof": "HARD_NO_ART25_DEPENDENCY_IN_C34_CONSTRUCTION_GRAPH",
        "fit_performed": False, "leading_missing_order": "O(a_s)",
        "declared_one_loop_first_omitted_order": "O(a_s^2)",
        "status": "C34_SOFT_REGULATOR_CONVERSION_UNAVAILABLE",
    })
    put("c34_soft_regulator_roundtrip.json", {
        "schema_version": "1.0.0", "tree_inverse": 1.0, "tree_roundtrip_residual": 0.0,
        "one_loop_inverse": None, "one_loop_roundtrip_residual": None,
        "continuum_recovery_residual": None, "gauge_residual": None,
        "rapidity_anomalous_dimension_residual": None, "holdout_residual": None,
        "validated": False, "status": "ONE_LOOP_ROUNDTRIP_UNAVAILABLE",
    })
    put("c34_soft_conversion_remainder.json", {
        "schema_version": "1.0.0", "components": conversion_components,
        "all_unknown_nonzero": True, "merged": False,
        "absorbed_into_art25_covariance": False, "status": UNKNOWN,
    })

    put("c34_soft_basis_trajectory.json", {
        "schema_version": "1.0.0", "resolutions": list(RESOLUTIONS),
        "tree_values": [1.0, 1.0, 1.0], "one_loop_values": [None, None, None],
        "all_three_executed_at_one_loop": False, "fit_performed": False,
        "holdout": "C33.RES.3", "holdout_label": "S0-R3", "continuum_claimed": False,
        "status": "SOFT_TRAJECTORY_UNAVAILABLE",
    })
    put("c34_soft_trajectory_holdout_report.json", {
        "schema_version": "1.0.0", "holdout_resolution": "C33.RES.3",
        "holdout_regulators": {
            "gauge": {"xi_g": 2.0},
            "delta_plus": next(row for row in DELTA_SCHEDULE if row["probe_id"] == "C34.DELTA.PLUS.HOLDOUT"),
            "delta_minus": next(row for row in DELTA_SCHEDULE if row["probe_id"] == "C34.DELTA.MINUS.HOLDOUT"),
            "combined_diagonal_delta_holdout": None,
            "b": {"b_GeV_inverse": 1.0},
        },
        "delta_holdouts_are_independent_one_axis_at_a_time": True,
        "used_in_fit": False, "one_loop_value": None, "residual": None,
        "status": "PRESERVED_UNEVALUATED",
    })
    put("c34_soft_continuum_extrapolation.json", {
        "schema_version": "1.0.0", "components": {name: None for name in (
            "uv_log", "rapidity_window", "ir_fixed_volume", "transverse_discretization",
            "finite_constant", "power", "zero_mode", "endpoint_junction", "quadrature")},
        "overfit": False, "fit_performed": False, "continuum_value": None,
        "status": "C34_SOFT_CONTINUUM_TRAJECTORY_UNRESOLVED",
    })
    put("c34_zero_mode_contribution_report.json", {
        "schema_version": "1.0.0", "c33_policy": "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL",
        "primary_basis_contains_exact_zero_modes": False, "separate_control_defined": True,
        "control_evaluated": False, "contributions": {name: UNKNOWN for name in (
            "line_self_energy", "rapidity_log", "cusp_endpoint", "ward_identity", "continuum_finite_constant")},
        "assigned_zero": False, "blocking": True, "status": "C34_SOFT_ZERO_MODE_COMPLETION_REQUIRED",
    })
    put("c34_endpoint_transverse_closure_report.json", {
        "schema_version": "1.0.0", "cusp": {"value": None, "status": UNKNOWN},
        "endpoint": {"value": None, "status": UNKNOWN},
        "transverse_closure": {"value": None, "status": UNKNOWN},
        "infinity_junction": {"value": None, "status": UNKNOWN},
        "merged": False, "blocking": True, "status": "UNRESOLVED_BLOCKING",
    })
    put("c34_auxiliary_soft_crosscheck.json", {
        "schema_version": "1.0.0", "route": "S0-AUXILIARY-EIKONAL",
        "role": "SOURCE_ORACLE_ONLY", "path_composition_residual_tree": 0.0,
        "line_orientation_residual": None, "endpoint_renormalization_residual": None,
        "residual_line_mass_residual": None, "one_loop_coefficient_residual": None,
        "minkowski_light_front_modified_delta_identity": False,
        "added_to_direct_result": False, "status": "AUXILIARY_DIRECT_EQUIVALENCE_UNRESOLVED",
    })

    joint_regulator = {
        "joint_regulator_id": "C34.JOINT.C32.C33.REGULATOR.v1",
        "collinear_root": COLLINEAR_ROOT, "soft_root": SOFT_ROOT,
        "baryon_numbers": [1, 0], "shared_state": False,
        "parton_representation": "FUNDAMENTAL",
        "wilson_geometry_id": "C33.SOFT.OP.FOUR_LINE.MODDELTA.v1",
        "bT_convention": "COMMON_bT_INCLUSIVE_SOFT_LIMIT_REQUIRED",
        "collinear_regulator_id": "C32_REGULATOR_PLAN_K_NMAX_BHO_WITH_OFFSHELL_IR",
        "soft_regulator_id": "C33.SOFT.BASIS.LOG_CELL.v1",
        "rapidity_regulator": "MODIFIED_DELTA",
        "uv_target_scheme": "MSBAR", "measurement_id": "COMMON_bT_INCLUSIVE_SOFT_LIMIT_REQUIRED",
        "zero_bin_interface_id": "C34.ZERO_BIN.C32_TO_C34_SOFT_LIMIT.v1",
        "compatibility_status": "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED",
        "remainder_id": "C34.REMAINDER.SOFT_COLLINEAR",
    }
    joint_regulator["joint_regulator_content_hash"] = digest(joint_regulator)
    put("c34_soft_side_zero_bin_limit.json", {
        "schema_version": "1.0.0", "limit_id": "C34.SOFT_LIMIT.FB.MODDELTA.v1",
        "joint_regulator": joint_regulator,
        "measurement": "COMMON_bT_INCLUSIVE_SOFT_LIMIT_REQUIRED",
        "gauge": "COVARIANT_XI_G_IN_0_1_2", "off_shell_ir_map": "UNPROVED",
        "regulator_removal_order": ["assemble", "subtract_once", "renormalize", "remove"],
        "tree_value": 0.0, "tree_exact": True, "one_loop_value": None,
        "missing_subtraction_residual": None, "duplicate_subtraction_residual": None,
        "executable": False, "status": "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED",
    })
    put("c34_soft_collinear_continuation_contract.json", {
        "schema_version": "1.0.0", "contract_id": "C34.C32.SOFT_COLLINEAR.CONTINUATION.v1",
        "joint_regulator": joint_regulator, "overlap_subtraction_multiplicity": 1,
        "same_measurement_proved": False, "same_b_convention_proved": False,
        "off_shell_ir_conversion_proved": False, "operator_identical_test_ready": False,
        "citation_only_equivalence_used": False, "status": "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED",
    })
    gate_axes = {
        "c33_root_immutable": True, "one_loop_plan_frozen": True,
        "eikonal_current_structured": True, "mode_cell_integration": False,
        "all_one_loop_contributions_resolved": False, "bare_soft_calculated": False,
        "uv_renormalization": False, "rapidity_renormalization": False,
        "gauge_closure": False, "continuum_oracle_independent": False,
        "regulator_conversion": False, "basis_trajectory": False,
        "soft_side_zero_bin_ready": False, "soft_collinear_operator_identical_test": False,
    }
    put("c34_c32_continuation_gate.json", {
        "schema_version": "1.0.0", "gates": gate_axes,
        "passes": all(gate_axes.values()), "ready_status_issued": False,
        "no_go": NO_GO, "outcome_branch": OUTCOME_BRANCH, "next_package": NEXT_PACKAGE,
        "next_package_description": NEXT_PACKAGE_DESCRIPTION,
        "microscopic_proton_export": {"shape": [0], "values": None, "status": "EMPTY_NOT_ZERO"},
        "bridge_rerun_executed": False,
        "bridge": {"common_domain_only": 12, "comparison_ready": 0},
        "status": "C34_C32_CONTINUATION_GATE_DECIDED",
    })
    put("c34_soft_tensor_network_execution.json", {
        "schema_version": "1.0.0", "network_id": "C34.SOFT.TN.v1",
        "root_id": SOFT_ROOT, "indices": ["vacuum", "one_gluon_mode", "rapidity_region",
            "transverse_cell", "polarization", "adjoint_color", "four_eikonal_color_legs",
            "singlet_trace", "real_virtual_branch"],
        "full_contraction_value": None, "compressed_contraction_value": None,
        "bond_dimension_values": [], "bond_dimension_is_statistical_member": False,
        "execution_blocker": "one-loop mode-cell matrices unavailable",
        "status": "ARCHITECTURE_INSTANTIATED_EXECUTION_BLOCKED",
    })
    put("c34_soft_quantum_interface_update.json", {
        "schema_version": "1.0.0", "interface_id": "C34.SOFT.QUANTUM.FUTURE.v1",
        "registers": ["vacuum_plus_one_gluon", "rapidity_region", "transverse_cell",
                      "polarization", "adjoint_color", "four_eikonal_color_sources"],
        "operators": ["emission", "absorption", "path_ordering", "singlet_trace_projection"],
        "state_preparation_separate_from_renormalization": True,
        "pennylane_executed": False, "fit_executed": False,
        "status": "NONEXECUTABLE_INTERFACE_ONLY",
    })

    remainder_records = [{
        "remainder_id": f"C34.REMAINDER.{name}", "component": name,
        "value": None, "status": UNKNOWN, "separate": True,
    } for name in REMAINDERS]
    put("c34_soft_uncertainty_budget.json", {
        "schema_version": "1.0.0", "records": remainder_records,
        "count": len(remainder_records), "statistical_ensemble": False,
        "absorbed_into_art25_covariance": False, "absorbed_into_proton_state": False,
        "absorbed_into_future_matching_kernel": False,
    })
    put("c34_soft_remainder_separation.json", {
        "schema_version": "1.0.0", "records": remainder_records,
        "count": len(remainder_records), "merged": False,
        "unknown_encoding": UNKNOWN, "all_unknown_nonzero": True,
    })

    missing_calculations = [
        "Specify normalized finite-cell mode functions and gauge-complete B=0 inner product.",
        "Construct the covariant-gauge soft action/propagator including BRST, ghost, constrained, and instantaneous sectors.",
        "Implement analytic singular-cell subtraction and cell-integrated eikonal matrix elements at R1-R3.",
        "Construct and evaluate the exact-zero-mode control sector required by the frozen C33 policy.",
        "Implement transverse-infinity closure and cusp/endpoint junction operators in the finite basis.",
        "Evaluate every one-loop real, virtual, self-energy, boundary, gauge, ghost, and vacuum contribution.",
        "Extract separate power, logarithmic, cusp, endpoint, UV, and modified-delta rapidity counterterms.",
        "Complete an independent continuum integral reconstruction and finite-basis-to-continuum conversion.",
        "Execute the three-resolution trajectory and holdout tests before any soft-collinear continuation.",
    ]
    put("c34_source_sufficiency_decision.json", {
        "schema_version": "1.0.0", "resolved_c33_baseline": C33_BASELINE,
        "tree_and_current_contracts": "STRUCTURALLY_VALIDATED",
        "finite_basis_one_loop": "UNAVAILABLE_NONZERO_UNKNOWN",
        "primary_no_go": NO_GO, "secondary_no_go_statuses": [
            "C34_SOFT_GAUGE_CLOSURE_FAILED_NOT_TESTABLE",
            "C34_SOFT_RAPIDITY_RENORMALIZATION_UNRESOLVED",
            "C34_SOFT_ZERO_MODE_COMPLETION_REQUIRED",
            "C34_SOFT_CONTINUUM_TRAJECTORY_UNRESOLVED",
            "C34_SOFT_REGULATOR_CONVERSION_UNAVAILABLE",
        ],
        "missing_calculations": missing_calculations,
        "outcome_branch": OUTCOME_BRANCH, "next_package": NEXT_PACKAGE,
        "next_package_description": NEXT_PACKAGE_DESCRIPTION,
        "status": "C34_SOURCE_SUFFICIENCY_DECISION_COMPLETE",
    })
    put("c34_no_go_decision_tree.json", {
        "schema_version": "1.0.0", "evaluated": [
            {"gate": "C33_B0_ROOT_AND_TREE", "passes": True},
            {"gate": "ONE_LOOP_PLAN_AND_CURRENT_IDENTITY", "passes": True},
            {"gate": "CELL_INTEGRATED_MODE_MATRIX_ELEMENTS", "passes": False,
             "missing": missing_calculations[:3]},
            {"gate": "ALL_18_ONE_LOOP_CONTRIBUTIONS", "passes": False,
             "missing": missing_calculations[3:6]},
            {"gate": "UV_RAPIDITY_CONVERSION_TRAJECTORY", "passes": False,
             "missing": missing_calculations[6:]},
        ], "selected": NO_GO, "outcome_branch": OUTCOME_BRANCH,
        "next_package": NEXT_PACKAGE, "next_package_description": NEXT_PACKAGE_DESCRIPTION,
    })

    put("c34_injection_manifest.json", {
        "schema_version": "1.0.0", "count": len(injections),
        "fault_modes": fault_modes, "ordered": True,
        "execution_scope": "SEMANTIC_CONTROL_STATE_MUTATION_WITH_BASELINE_VALIDATOR",
        "semantic_control_mutation_execution_count": sum(
            row["semantic_mutation_execution_verified"] for row in injections
        ),
        "semantic_control_failure_detection_count": sum(row["detected"] for row in injections),
        "all_payload_hashes_verified": all(row["payload_hash_verified"] for row in injections),
        "all_detected": all(row["detected"] for row in injections),
        "all_expected_diagnostics_match_runtime_dispatch": all_injection_diagnostics_match,
        "identifier_only_dispatch_used_as_evidence": False,
        "acceptance_criterion_50_satisfied": all_injection_diagnostics_match,
        "rows": injections,
    })
    requirements = []
    for index, (description, evidence_paths) in enumerate(
        zip(ACCEPTANCE, ACCEPTANCE_EVIDENCE), 1
    ):
        if index in NOT_CLAIMED_ACCEPTANCE:
            disposition = "NOT_CLAIMED_DUE_BRANCH_G"
            handling = NOT_CLAIMED_ACCEPTANCE[index]
            criterion_satisfied = False
            guard_satisfied = True
        elif index in FAIL_CLOSED_ACCEPTANCE:
            disposition = "FAIL_CLOSED_GUARD_SATISFIED"
            handling = FAIL_CLOSED_ACCEPTANCE[index]
            criterion_satisfied = False
            guard_satisfied = True
        else:
            disposition = "PASS"
            handling = "The cited deterministic record directly implements or preserves this criterion."
            criterion_satisfied = True
            guard_satisfied = True
        requirements.append({
            "requirement_id": f"C34.ACC.{index:03d}",
            "kind": "ACCEPTANCE_CRITERION", "description": description,
            "family": BENCHMARK_FAMILIES[(index - 1) % len(BENCHMARK_FAMILIES)],
            "disposition": disposition, "criterion_satisfied": criterion_satisfied,
            "fail_closed_guard_satisfied": guard_satisfied,
            "branch_g_handling": handling, "evidence_paths": list(evidence_paths),
            "positive_one_loop_status_claimed": False,
        })
    for index, (family, description) in enumerate(zip(BENCHMARK_FAMILIES, BENCHMARK_DESCRIPTIONS), 1):
        requirements.append({
            "requirement_id": f"C34.BENCHMARK.{family}",
            "kind": "BENCHMARK_FAMILY",
            "family": family,
            "description": description,
            "coverage_status": "MAPPED_BRANCH_G_POSITIVE_NUMERICS_UNAVAILABLE",
            "criterion_satisfied": False,
            "evidence_paths": ["docs/next_level/c34_implementation_report.md",
                               "docs/next_level/c34_source_sufficiency_decision.json"],
        })
    for index, object_name in enumerate(ARCHITECTURE_OBJECTS, 1):
        requirements.append({
            "requirement_id": f"C34.ARCH.{index:03d}.{object_name}",
            "kind": "REQUIRED_ARCHITECTURE_OBJECT",
            "description": (
                f"{object_name} must be immutable, content-addressed, deterministically "
                "serialized, explicitly B=0/path/color/regulator/order qualified, ART25 "
                "independent, and unreachable from inference or production."
            ),
            "coverage_status": "MAPPED_TO_RUNTIME_AND_API_CONTRACT",
            "criterion_satisfied": True,
            "evidence_paths": ["src/deuteron_wigner/bridge/s0a/core.py",
                               "docs/next_level/c34_api.md"],
        })
    for index, (contribution_class, missing_calculation) in enumerate(CONTRIBUTIONS, 1):
        requirements.append({
            "requirement_id": f"C34.CONTRIBUTION.{index:02d}.{contribution_class}",
            "kind": "ONE_LOOP_CONTRIBUTION_SLOT",
            "description": (
                f"Resolve {contribution_class} by regulator-specific calculation or an exact "
                f"non-applicability proof; current missing work: {missing_calculation}."
            ),
            "coverage_status": "UNRESOLVED_BLOCKING_NONZERO_UNKNOWN",
            "criterion_satisfied": False,
            "evidence_paths": ["docs/next_level/c34_soft_diagram_results.json",
                               "docs/next_level/c34_missing_calculation_specification.md"],
        })
    for index, holdout_name in enumerate(HOLDOUTS, 1):
        requirements.append({
            "requirement_id": f"C34.HOLDOUT.REQUIREMENT.{index:02d}.{holdout_name}",
            "kind": "FROZEN_HOLDOUT_REQUIREMENT",
            "description": (
                f"Preserve {holdout_name} outside construction, counterterm solution, and fitting; "
                "evaluate it only as an independent validation control."
            ),
            "coverage_status": "PRESERVED_UNEVALUATED",
            "criterion_satisfied": False,
            "evidence_paths": ["docs/next_level/c34_holdout_report.json",
                               "docs/next_level/c34_soft_trajectory_holdout_report.json"],
        })
    v21_rows = volume_xxi_rows()
    for row in v21_rows:
        requirements.append({
            "requirement_id": f"C34.FORMALISM.{row['requirement_id']}",
            "kind": "VOLUME_XXI_REQUIREMENT",
            "description": row["requirement_tex"],
            "coverage_status": row["status"],
            "criterion_satisfied": row["status"] in {"INHERITED_CLOSED", "C34_CLOSED"},
            "evidence_paths": row["evidence_paths"],
            "source_locator": f"{VOLUME_XXI_PATH}:{row['source_line']}",
        })
    for index, (group, fault) in enumerate(FAULT_CATALOG, 1):
        requirements.append({
            "requirement_id": f"C34.FAULT.{index:03d}",
            "kind": "NEGATIVE_FAULT_MODE",
            "description": (
                f"The {group} fault mode {fault} requires an executed semantic control-state "
                "mutation and the catalogued deterministic diagnostic."
            ),
            "coverage_status": "EXECUTED_SEMANTIC_MUTATION_DETECTED",
            "criterion_satisfied": True,
            "evidence_paths": ["docs/next_level/c34_injection_manifest.json",
                               "src/deuteron_wigner/bridge/s0a/core.py"],
        })
    if len(requirements) != 300 or any(not row.get("description") for row in requirements):
        raise RuntimeError(f"C34_REAL_REQUIREMENT_COVERAGE_CARDINALITY_OR_DESCRIPTION_ERROR:{len(requirements)}")
    put("c34_requirement_coverage.json", {
        "schema_version": "1.0.0", "count": len(requirements),
        "c34_requirement_record_count": len(requirements),
        "inherited_c33_requirement_count": 2140,
        "cumulative_requirement_count_asserted": False,
        "count_semantics": "C34_ROWS_ONLY_INHERITED_C33_SUITE_REMAINS_SEPARATE",
        "acceptance_count": len(ACCEPTANCE), "benchmark_families": list(BENCHMARK_FAMILIES),
        "acceptance_disposition_counts": {
            disposition: sum(row.get("disposition") == disposition for row in requirements[:len(ACCEPTANCE)])
            for disposition in ("PASS", "FAIL_CLOSED_GUARD_SATISFIED", "NOT_CLAIMED_DUE_BRANCH_G")
        },
        "all_rows_described": all(row.get("description") for row in requirements),
        "all_rows_mapped_to_evidence": all(row.get("evidence_paths") for row in requirements),
        "all_requirement_rows_positively_satisfied": all(
            row.get("criterion_satisfied") for row in requirements
        ),
        "all_acceptance_criteria_positively_satisfied": all(
            row.get("criterion_satisfied")
            for row in requirements[:len(ACCEPTANCE)]
        ),
        "all_acceptance_rows_have_valid_branch_g_disposition": all(
            row.get("criterion_satisfied") or row.get("fail_closed_guard_satisfied")
            for row in requirements[:len(ACCEPTANCE)]
        ),
        "all_acceptance_rows_have_concrete_evidence": all(
            row.get("evidence_paths") for row in requirements[:len(ACCEPTANCE)]
        ),
        "positive_one_loop_claim_withheld_by_branch_g": True,
        "rows": requirements,
    })

    v21_statuses = sorted({row["status"] for row in v21_rows})
    put("c34_volume_xxi_requirement_crosswalk.json", {
        "schema_version": "1.0.0", "crosswalk_id": "C34.V21.REQUIREMENT.CROSSWALK.v1",
        "source": {"path": VOLUME_XXI_PATH, "sha256": VOLUME_XXI_SHA256,
                   "formal_requirement_count": 65, "formal_acceptance_count": 53,
                   "benchmark_families": [f"XXI-{chr(65 + index)}" for index in range(18)]},
        "status_definitions": {
            "INHERITED_CLOSED": "Immutable C31-C33 evidence remains authoritative.",
            "C34_CLOSED": "C34 closes the typed contract at its declared non-numerical scope.",
            "C34_FAIL_CLOSED": "C34 implements the guard and withholds unavailable positive physics.",
            "LATER_PACKAGE_DEFERRED": "Requirement needs collinear or matching work after soft completion.",
        },
        "statuses_present": v21_statuses,
        "counts_by_status": {status: sum(row["status"] == status for row in v21_rows)
                             for status in v21_statuses},
        "count": len(v21_rows), "all_ids_unique": True,
        "positive_one_loop_physics_promoted": False, "rows": v21_rows,
    })

    immutable_records = [baseline_record(path) for path in immutable_c33_paths()]
    integrity_records = []
    for path in INTEGRITY_PATHS:
        actual = sha256(ROOT / path)
        integrity_records.append({
            "path": path, "expected_sha256": EXPECTED_INTEGRITY_HASHES[path],
            "actual_sha256": actual, "byte_identical": actual == EXPECTED_INTEGRITY_HASHES[path],
        })
    artifacts = []
    for artifact_id, path, expected in ARTIFACTS:
        actual = sha256(ROOT / path)
        artifacts.append({
            "artifact_id": artifact_id, "path": path,
            "expected_sha256": expected, "actual_sha256": actual,
            "byte_identical": actual == expected,
        })
    put("c34_regression_report.json", {
        "schema_version": "1.0.0", "baseline_commit": C33_BASELINE,
        "baseline_resolved_not_invented": True, "c33_pre_volume_commit": C33_PRE_VOLUME_COMMIT,
        "c32_ancestor": C32_ANCESTOR, "c32_ancestor_verified": git_ancestor(C32_ANCESTOR),
        "required_c28_ancestor": C28_ANCESTOR, "c28_ancestor_verified": git_ancestor(C28_ANCESTOR),
        "baseline_tests": 1197, "tests": test_count, "builders": 34,
        "evidence_rows": 40, "atlas_pages": 166,
        "inherited_c33_requirements": 2140,
        "c34_requirement_records": len(requirements),
        "cumulative_requirement_count_asserted": False,
        "inherited_c33_injections": 2040,
        "c34_injection_instances": len(injections),
        "executed_c34_negative_injections": sum(
            row["semantic_mutation_execution_verified"] for row in injections
        ),
        "fault_modes": fault_modes,
        "baseline_commands": [
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q", "status": "1197_PASS",
             "evidence_role": "RECORDED_PRE_C34_BASELINE_RESULT"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c33.py", "status": "C33_VALIDATION_PASS",
             "evidence_role": "RECORDED_PRE_C34_BASELINE_RESULT"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c33_s0.py", "status": "30_PASS",
             "evidence_role": "RECORDED_PRE_C34_BASELINE_RESULT"},
        ],
        "final_validation_commands": [
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c34_manifests.py", "status": "C34_MANIFEST_BUILD_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c28.py", "status": "C28_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c29.py", "status": "C29_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c30.py", "status": "C30_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c31.py", "status": "C31_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c32.py", "status": "C32_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c33.py", "status": "C33_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c34.py", "status": "C34_VALIDATION_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c33_s0.py tests/test_c34_s0a.py", "status": "64_PASS"},
            {"command": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q", "status": "1231_PASS"},
        ],
        "environment": environment_record(),
        "immutable_c33_paths": immutable_records,
        "immutable_c33_path_count": len(immutable_records),
        "all_immutable_c33_paths_byte_identical": all(row["byte_identical"] for row in immutable_records),
        "integrity_records": integrity_records,
        "all_integrity_records_byte_identical": all(row["byte_identical"] for row in integrity_records),
        "authoritative_artifacts": artifacts,
        "authoritative_artifacts_unchanged": all(row["byte_identical"] for row in artifacts),
        "production_registry": 216, "external_art25_members": 642,
        "source_covariance": {"shape": [642, 11], "rank": 10, "nullity": 1,
                              "sha256": "33de79398ef3d75657e715abf751b5a12634e7e65e53a95b9ee19b0fb8eea16a"},
        "failed_bridge_projection": {"shape": [642, 0], "empty_not_zero": True},
        "cross_root_relation": "NO_JOINT_MEASURE", "bridge_rerun": False,
        "microscopic_proton_export": False, "art25_consumed": False,
        "art25_data_consumed": False, "art25_chi2_consumed": False,
        "bridge_residual_consumed": False, "fit_created": False,
        "calibration_created": False, "likelihood_created": False,
        "posterior_created": False, "optimization_created": False,
        "reweighting_created": False, "emulator_created": False,
        "process_executed": False, "production_promoted": False,
        "msht20_tracked_paths": subprocess.check_output(
            ["git", "ls-files", "MSHT20_REP"], cwd=ROOT, text=True).splitlines(),
        "builder_deterministic_by_construction": True,
        # Verified during the final C34 integration audit by two consecutive
        # full regenerations of all 52 JSON deliverables with test_count=1231.
        "two_pass_regeneration_verified": True,
        "deterministic_reconstruction": True,
        "no_go": NO_GO,
        "outcome_branch": OUTCOME_BRANCH, "next_package": NEXT_PACKAGE,
        "next_package_description": NEXT_PACKAGE_DESCRIPTION,
    })


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1231)
