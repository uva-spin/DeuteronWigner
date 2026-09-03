#!/usr/bin/env python3
"""Generate deterministic C407 evidence."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants import (
    STATUS,
    binding_update_summary,
    c396_binding_inventory_with_c407_descendants,
    completion_record,
    descendant_inventory,
    intermediate_axis_inventory,
    jqjq_qg_conditioned_validation,
    longitudinal_validation,
    scientific_boundary_record,
    source_hash_audit,
)

BASELINE = "4f932604483701d18158164288674cea82a07b3f"
PHASE = "C407_C117_I2_SAME_SPECIES_DESCENDANTS"

GENERATED_NAMES = (
    "C407_ACCEPTANCE_SPEC.json",
    "C407_SOURCE_EVIDENCE_HASHES.json",
    "input_freeze.json",
    "source_hash_audit.json",
    "intermediate_axis_inventory.json",
    "same_species_descendant_inventory.json",
    "longitudinal_validation.json",
    "jqjq_qg_conditioned_validation.json",
    "jqjq_qg_primitive_validation.json",  # obsolete pre-lock name, removed fail-closed
    "scientific_boundary.json",
    "c396_coordinate_binding_inventory.json",
    "binding_update_summary.json",
    "blocker_or_completion.json",
    "scientific_nonclaims.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)


def plain(value: Any) -> Any:
    if isinstance(value, MappingProxyType):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, dict):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    if isinstance(value, Fraction):
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
            "exact": str(value),
            "float": float(value),
        }
    if is_dataclass(value):
        return plain(asdict(value))
    if isinstance(value, complex):
        return [float(value.real), float(value.imag)]
    if hasattr(value, "item"):
        return plain(value.item())
    return value


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(plain(value), sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value))


def file_record(path: Path, root: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": len(data),
        "sha256": sha256(data).hexdigest(),
    }


def acceptance_spec() -> dict[str, Any]:
    return {
        "schema": "C407-ACCEPTANCE-SPEC-V1",
        "phase": PHASE,
        "baseline": BASELINE,
        "required": {
            "source_hash_rows": 12,
            "intermediate_axis_rows": 154,
            "same_species_weight_rows": 154,
            "J_qJ_q_qg_conditioned_composition_rows": 3,
            "source_authorized_graph_member_weight_sets": 0,
            "complete_C117_numerical_apply_paths": 0,
            "complete_C396_numerical_apply_paths": 6,
            "rank_status": "RANK_NOT_EVALUATED",
            "physical_fit_authorized": False,
            "activation_gate_status": "NOT_READY",
        },
        "forbidden": (
            "mixed-current kernel substitution for same-species products",
            "I2 substitution for the J_qJ_q q-sector I4-local graph",
            "I2 substitution for the J_gJ_g derivative-density graph",
            "zero-filling unresolved q-sector gluon branches",
            "unit-weight or minimum-norm graph-member defaults",
            "default normalization, physical coefficient, rank, fit, activation, merge, push",
        ),
    }


def input_freeze() -> dict[str, Any]:
    return {
        "schema": "C407-INPUT-FREEZE-V1",
        "phase": PHASE,
        "baseline": BASELINE,
        "source_hash_audit": source_hash_audit(),
        "upstream": {
            "C406_status": "ONE_GLUON_NORMAL_ORDER_DESCENDANT_READY_SAME_SPECIES_UNRESOLVED",
            "C406_merge_commit": BASELINE,
            "complete_C396_numerical_apply_paths": 6,
        },
        "physical_coupling": None,
        "C117_coefficient": None,
        "physical_targets": None,
        "rank_evaluation": False,
    }


def implementation_report() -> str:
    axes = intermediate_axis_inventory()
    descendants = descendant_inventory()
    jqjq = jqjq_qg_conditioned_validation()
    completion = completion_record()
    return f"""# C407 implementation report

## Result

`{STATUS}`

C407 closes {axes['row_count']} exact same-species longitudinal intermediate-mode rows and
{descendants['row_count']} exact one-body longitudinal weights across K9, K11 and K13.
It additionally implements three K-local caller-conditioned `J_qJ_q:qg->qg` I2 composition interfaces. The C117 graph-member weights remain source-unbound and no unit-weight default is used.

## Numerical checks

- Source authority rows: {source_hash_audit()['row_count']}
- Longitudinal sparse/matrix-free maximum residual: {longitudinal_validation()['maximum_sparse_matrix_free_residual']:.3e}
- Caller-conditioned J_qJ_q qg sparse/matrix-free maximum residual: {jqjq['maximum_sparse_matrix_free_residual']:.3e}
- Direct finite-Fock normal-order validation: {descendants['direct_Fock_validation']['pass']}
- Complete C117 numerical apply paths: {completion['complete_C117_numerical_apply_paths']}
- Complete C396 numerical apply paths: {completion['complete_C396_numerical_apply_paths']}

## Remaining exact frontier

{completion['smallest_missing_object']}

No physical coefficient, rank, fit or activation is claimed.
"""


def scientific_nonclaims() -> dict[str, Any]:
    return {
        "schema": "C407-SCIENTIFIC-NONCLAIMS-V1",
        "phase": PHASE,
        "not_established": (
            "source-authorized C117 I2 graph-member weights for J_qJ_q",
            "J_qJ_q q-sector I4-local numerical action",
            "J_gJ_g derivative-density transverse numerical action",
            "J_gJ_g q-sector pair/vacuum action",
            "complete C117 I2 Hamiltonian-coordinate action",
            "route-reconciled complete normalization",
            "physical value of g_s or c_C117_1",
            "physical response rank",
            "physical fit",
            "Hamiltonian activation",
        ),
        "unavailable_is_zero": False,
        "complete_C396_numerical_apply_paths": 6,
    }


def release() -> dict[str, Any]:
    completion = completion_record()
    return {
        "schema": "C407-RELEASE-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "same_species_intermediate_axes_ready": completion["same_species_intermediate_axes_ready"],
        "same_species_longitudinal_descendants_ready": completion["same_species_longitudinal_descendants_ready"],
        "J_qJ_q_qg_caller_conditioned_composition_ready": completion["J_qJ_q_qg_caller_conditioned_composition_ready"],
        "J_qJ_q_qg_source_authorized_graph_weights_ready": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "next_frontier": completion["smallest_missing_object"],
    }


def generate(output: Path) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_NAMES:
        path = output / name
        if path.exists():
            path.unlink()
    artifacts = {
        "C407_ACCEPTANCE_SPEC.json": acceptance_spec(),
        "C407_SOURCE_EVIDENCE_HASHES.json": source_hash_audit(),
        "input_freeze.json": input_freeze(),
        "source_hash_audit.json": source_hash_audit(),
        "intermediate_axis_inventory.json": intermediate_axis_inventory(),
        "same_species_descendant_inventory.json": descendant_inventory(),
        "longitudinal_validation.json": longitudinal_validation(),
        "jqjq_qg_conditioned_validation.json": jqjq_qg_conditioned_validation(),
        "scientific_boundary.json": scientific_boundary_record(),
        "c396_coordinate_binding_inventory.json": c396_binding_inventory_with_c407_descendants(),
        "binding_update_summary.json": binding_update_summary(),
        "blocker_or_completion.json": completion_record(),
        "scientific_nonclaims.json": scientific_nonclaims(),
        "release.json": release(),
    }
    for name, value in artifacts.items():
        write_json(output / name, value)
    (output / "implementation_report.md").write_text(implementation_report(), encoding="utf-8")

    static_names = (
        "C407_C117_I2_SAME_SPECIES_DESCENDANT_SCIENCE_LOCK.md",
        "C407_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md",
        "C407_MERGE_READINESS_CHECKLIST.md",
        "implementation_report.md",
    )
    records = []
    for path in sorted(output.iterdir()):
        if path.name == "generation_result.json" or not path.is_file():
            continue
        records.append(file_record(path, output))
    result = {
        "schema": "C407-GENERATION-RESULT-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "output_directory": "docs/phases/c407_c117_i2_same_species_descendants",
        "artifact_count_excluding_generation_result": len(records),
        "artifacts": records,
        "required_static_files_present": all((output / name).is_file() for name in static_names),
        "source_hash_rows": source_hash_audit()["row_count"],
        "intermediate_axis_rows": intermediate_axis_inventory()["row_count"],
        "same_species_weight_rows": descendant_inventory()["row_count"],
        "J_qJ_q_qg_conditioned_composition_rows": jqjq_qg_conditioned_validation()["row_count"],
        "source_authorized_graph_member_weight_sets": 0,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    result["package_root"] = sha256(canonical_bytes(records)).hexdigest()
    write_json(output / "generation_result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="docs/phases/c407_c117_i2_same_species_descendants",
    )
    args = parser.parse_args()
    result = generate(Path(args.output))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
