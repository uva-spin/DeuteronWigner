#!/usr/bin/env python3
"""Generate deterministic C408 evidence."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure import (
    STATUS,
    binding_update_summary,
    c396_binding_inventory_with_c408_closure,
    completion_record,
    derivative_density_conflict_record,
    i2_member_weight_authority,
    i2_source_weight_validation,
    jqjq_product_block_validation,
    q_sector_i4_inventory,
    q_sector_i4_validation,
    routing_authority_record,
    scientific_boundary_record,
    source_hash_audit,
    source_i2_unit_weight_record,
)

BASELINE = "6da320adf775956e26e860e294c08e047c66c024"
PHASE = "C408_C117_I2_WEIGHT_ROUTING_CLOSURE"

GENERATED_NAMES = (
    "input_freeze.json",
    "source_hash_audit.json",
    "routing_authority.json",
    "i2_member_weight_authority.json",
    "i2_unit_member_weights.json",
    "i2_source_weight_validation.json",
    "q_sector_i4_inventory.json",
    "q_sector_i4_validation.json",
    "jqjq_product_block_validation.json",
    "derivative_density_conflict.json",
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
    return {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def input_freeze() -> dict[str, Any]:
    return {
        "schema": "C408-INPUT-FREEZE-V1",
        "phase": PHASE,
        "baseline": BASELINE,
        "source_hash_audit": source_hash_audit(),
        "upstream": {
            "C407_hotfix_commit": BASELINE,
            "complete_C396_numerical_apply_paths": 6,
            "complete_C117_numerical_apply_paths": 0,
        },
        "physical_coupling": None,
        "C117_coefficient": None,
        "physical_targets": None,
        "rank_evaluation": False,
    }


def implementation_report() -> str:
    q = q_sector_i4_inventory()
    weights = i2_source_weight_validation()
    jq = jqjq_product_block_validation()
    complete = completion_record()
    return """# C408 implementation report

## Result

`{status}`

C408 closes the C116/C126 I4 route for `J_qJ_q:q->q`, evaluates {qrows} exact finite q-sector I4 members, and closes the C124/C126 unit I2 member multiplier at K9/K11/K13. It assembles three source-routed JqJq direct-sum product-block primitives and six source-routed mixed-current direct-sum primitives.

## Numerical checks

- Source authority rows: {sources}
- q-sector I4 analytic/quadrature maximum residual: {qres:.3e} GeV^2
- I2/mixed sparse-matrix-free maximum residual: {wres:.3e}
- JqJq direct-sum sparse-matrix-free maximum residual: {jres:.3e}
- Complete C117 numerical apply paths: {c117}
- Complete C396 numerical apply paths: {c396}

## Remaining exact frontier

{missing}

No physical coefficient, rank, fit or activation is claimed.
""".format(
        status=STATUS,
        qrows=q["row_count"],
        sources=source_hash_audit()["row_count"],
        qres=q["maximum_analytic_quadrature_abs_residual_GeV2"],
        wres=weights["maximum_sparse_matrix_free_residual"],
        jres=jq["maximum_sparse_matrix_free_residual"],
        c117=complete["complete_C117_numerical_apply_paths"],
        c396=complete["complete_C396_numerical_apply_paths"],
        missing=complete["smallest_missing_object"],
    )


def scientific_nonclaims() -> dict[str, Any]:
    return {
        "schema": "C408-SCIENTIFIC-NONCLAIMS-V1",
        "phase": PHASE,
        "not_established": (
            "J_gJ_g derivative-density numerical action",
            "J_gJ_g q-sector number-changing branches",
            "complete route-reconciled product normalization",
            "complete target count-once aggregation",
            "complete C117 I2 Hamiltonian-coordinate action",
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
        "schema": "C408-RELEASE-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "J_qJ_q_q_sector_I4_ready": completion["J_qJ_q_q_sector_I4_ready"],
        "I2_source_descendant_member_weights_ready": completion["I2_source_descendant_member_weights_ready"],
        "J_qJ_q_direct_sum_product_block_ready": completion["J_qJ_q_direct_sum_product_block_ready"],
        "mixed_current_source_weighted_product_blocks_ready": completion["mixed_current_source_weighted_product_blocks_ready"],
        "J_gJ_g_derivative_density_ready": False,
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
    unit = {resolution: source_i2_unit_weight_record(resolution) for resolution in ("K9", "K11", "K13")}
    artifacts = {
        "input_freeze.json": input_freeze(),
        "source_hash_audit.json": source_hash_audit(),
        "routing_authority.json": routing_authority_record(),
        "i2_member_weight_authority.json": i2_member_weight_authority(),
        "i2_unit_member_weights.json": unit,
        "i2_source_weight_validation.json": i2_source_weight_validation(),
        "q_sector_i4_inventory.json": q_sector_i4_inventory(),
        "q_sector_i4_validation.json": q_sector_i4_validation(),
        "jqjq_product_block_validation.json": jqjq_product_block_validation(),
        "derivative_density_conflict.json": derivative_density_conflict_record(),
        "scientific_boundary.json": scientific_boundary_record(),
        "c396_coordinate_binding_inventory.json": c396_binding_inventory_with_c408_closure(),
        "binding_update_summary.json": binding_update_summary(),
        "blocker_or_completion.json": completion_record(),
        "scientific_nonclaims.json": scientific_nonclaims(),
        "release.json": release(),
    }
    for name, value in artifacts.items():
        write_json(output / name, value)
    (output / "implementation_report.md").write_text(implementation_report(), encoding="utf-8")
    static_names = (
        "C408_ACCEPTANCE_SPEC.json",
        "C408_C117_I2_WEIGHT_ROUTING_CLOSURE_SCIENCE_LOCK.md",
        "C408_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md",
        "C408_MERGE_READINESS_CHECKLIST.md",
        "C408_SOURCE_EVIDENCE_HASHES.json",
        "C408_TWO_CLEAN_BUILDS.json",
        "C408_PYTHON39_COMPATIBILITY_AUDIT.json",
        "CHATGPT_STAGE_IMPLEMENTATION_REPORT.md",
        "CHATGPT_STAGE_TEST_EXECUTION.json",
    )
    records = []
    for path in sorted(output.iterdir()):
        if path.name == "generation_result.json" or not path.is_file():
            continue
        records.append(file_record(path, output))
    result = {
        "schema": "C408-GENERATION-RESULT-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "output_directory": "docs/phases/c408_c117_i2_weight_routing_closure",
        "artifact_count_excluding_generation_result": len(records),
        "artifacts": records,
        "required_static_files_present": all((output / name).is_file() for name in static_names),
        "source_hash_rows": source_hash_audit()["row_count"],
        "I2_unit_member_counts": {r: unit[r]["member_count"] for r in unit},
        "q_sector_I4_mode_counts": {row["resolution"]: row["mode_count"] for row in q_sector_i4_inventory()["summaries"]},
        "source_routed_product_block_primitive_paths": 9,
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
    parser.add_argument("--output", default="docs/phases/c408_c117_i2_weight_routing_closure")
    args = parser.parse_args()
    result = generate(Path(args.output))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
