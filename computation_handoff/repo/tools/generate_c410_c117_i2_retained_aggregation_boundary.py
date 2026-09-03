#!/usr/bin/env python3
"""Generate deterministic C410 retained-aggregation evidence."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    STATUS,
    aggregation_authority,
    binding_update_summary,
    c396_binding_inventory_with_c410_aggregation,
    completion_record,
    count_once_aggregation_record,
    normalization_boundary_record,
    normalization_capsule_schema,
    q_sector_vacuum_projection_validation,
    retained_aggregation_validation,
    scientific_boundary_record,
    source_hash_audit,
    vacuum_pair_validation,
    vacuum_routing_authority,
)

BASELINE = "160eb887f393177170b4c3486cea27b41968dfce"
PHASE = "C410_C117_I2_RETAINED_AGGREGATION_BOUNDARY"
OUT_REL = "docs/phases/c410_c117_i2_retained_aggregation_boundary"

GENERATED_NAMES = (
    "input_freeze.json",
    "source_hash_audit.json",
    "vacuum_routing_authority.json",
    "vacuum_pair_validation.json",
    "q_sector_vacuum_projection_validation.json",
    "aggregation_authority.json",
    "count_once_aggregation.json",
    "retained_aggregation_validation.json",
    "normalization_boundary.json",
    "normalization_capsule_schema.json",
    "scientific_boundary.json",
    "c396_coordinate_binding_inventory.json",
    "binding_update_summary.json",
    "blocker_or_completion.json",
    "scientific_nonclaims.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)

STATIC_NAMES = (
    "C410_ACCEPTANCE_SPEC.json",
    "C410_C117_I2_RETAINED_AGGREGATION_BOUNDARY_SCIENCE_LOCK.md",
    "C410_EXPECTED_COMMIT_PATHS.json",
    "C410_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md",
    "C410_MERGE_READINESS_CHECKLIST.md",
    "C410_PYTHON39_COMPATIBILITY_AUDIT.json",
    "C410_SOURCE_EVIDENCE_HASHES.json",
    "C410_TWO_CLEAN_BUILDS.json",
    "CHATGPT_STAGE_IMPLEMENTATION_REPORT.md",
    "CHATGPT_STAGE_TEST_EXECUTION.json",
)


def plain(value: Any) -> Any:
    if isinstance(value, MappingProxyType):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator,
                "exact": str(value), "float": float(value)}
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


def file_record(path: Path, root: Path) -> dict:
    data = path.read_bytes()
    return {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def input_freeze() -> dict:
    return {
        "schema": "C410-INPUT-FREEZE-V1",
        "phase": PHASE,
        "baseline": BASELINE,
        "source_hash_audit": source_hash_audit(),
        "upstream": {
            "C409_merge_commit": BASELINE,
            "source_routed_product_block_primitive_paths": 12,
            "complete_C396_numerical_apply_paths": 6,
            "complete_C117_numerical_apply_paths": 0,
        },
        "physical_coupling": None,
        "C117_coefficient": None,
        "physical_targets": None,
        "rank_evaluation": False,
    }


def implementation_report() -> str:
    vacuum = vacuum_pair_validation()
    aggregate = retained_aggregation_validation()
    complete = completion_record()
    return """# C410 implementation report

## Result

`{status}`

C410 proves that the `J_gJ_g:q->q` pair/vacuum branch is source-present and can be nonzero, but factorizes as the external-quark identity times a gluon-vacuum c-number. The project scheme routes that disconnected contribution to the C129/C131/C136 nonmatrix vacuum direction. The retained connected q-sector block is therefore exactly zero without claiming that the full-source vacuum matrix element vanishes.

C410 also aggregates the four source-ordered product primitives exactly once, preserves the two mixed orders separately, and applies the common C114 `-1/2` coefficient once with `g_s^2` and `c_C117_1` unselected.

## Numerical checks

- Source authority rows: {sources}
- Vacuum-pair validation rows: {vrows}
- Unequal-momentum diagnostic pair norm: {vnorm:.16g}
- Retained q-sector zero paths: 3
- Source-routed product-block primitive paths: {paths}
- Retained connected aggregate shape paths: {shapes}
- Maximum sparse/matrix-free residual: {mres:.3e}
- Maximum Hermiticity residual: {hres:.3e}
- Complete C117 numerical apply paths: {c117}
- Complete C396 numerical apply paths: {c396}

## Remaining exact frontier

{missing}

The C410 aggregate is a source-coefficient-reduced retained connected shape, not the C260/C262-normalized `O_C117_1,R` operator. No physical coefficient, rank, fit, or activation is claimed.
""".format(
        status=STATUS,
        sources=source_hash_audit()["row_count"],
        vrows=vacuum["row_count"],
        vnorm=vacuum["summed_unequal_momentum_vacuum_pair_norm_squared"],
        paths=aggregate["source_routed_product_block_primitive_paths"],
        shapes=aggregate["retained_connected_aggregate_shape_paths"],
        mres=aggregate["maximum_sparse_matrix_free_residual"],
        hres=aggregate["maximum_hermiticity_residual"],
        c117=complete["complete_C117_numerical_apply_paths"],
        c396=complete["complete_C396_numerical_apply_paths"],
        missing=complete["smallest_missing_object"],
    )


def scientific_nonclaims() -> dict:
    return {
        "schema": "C410-SCIENTIFIC-NONCLAIMS-V1",
        "phase": PHASE,
        "not_established": (
            "the absolute full-source vacuum c-number",
            "a finite-C43 C260/C262 operator-normalization adapter",
            "complete field/state/M2 and normalized-wavepacket normalization",
            "a complete C117 I2 Hamiltonian-coordinate action",
            "a physical value of g_s or c_C117_1",
            "physical response rank",
            "physical fit",
            "Hamiltonian activation",
        ),
        "vacuum_branch_silently_dropped": False,
        "identity_shift_inserted": False,
        "mixed_order_factor_two_used": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
    }


def release() -> dict:
    complete = completion_record()
    return {
        "schema": "C410-RELEASE-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "q_sector_vacuum_routing_ready": complete["q_sector_vacuum_projection_validation_pass"],
        "retained_product_aggregation_ready": complete["retained_aggregation_validation_pass"],
        "retained_connected_aggregate_shape_paths": 3,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "next_frontier": complete["smallest_missing_object"],
    }


def generate(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_NAMES:
        path = output / name
        if path.exists():
            path.unlink()
    artifacts = {
        "input_freeze.json": input_freeze(),
        "source_hash_audit.json": source_hash_audit(),
        "vacuum_routing_authority.json": vacuum_routing_authority(),
        "vacuum_pair_validation.json": vacuum_pair_validation(),
        "q_sector_vacuum_projection_validation.json": q_sector_vacuum_projection_validation(),
        "aggregation_authority.json": aggregation_authority(),
        "count_once_aggregation.json": count_once_aggregation_record(),
        "retained_aggregation_validation.json": retained_aggregation_validation(),
        "normalization_boundary.json": normalization_boundary_record(),
        "normalization_capsule_schema.json": normalization_capsule_schema(),
        "scientific_boundary.json": scientific_boundary_record(),
        "c396_coordinate_binding_inventory.json": c396_binding_inventory_with_c410_aggregation(),
        "binding_update_summary.json": binding_update_summary(),
        "blocker_or_completion.json": completion_record(),
        "scientific_nonclaims.json": scientific_nonclaims(),
        "release.json": release(),
    }
    for name, value in artifacts.items():
        write_json(output / name, value)
    (output / "implementation_report.md").write_text(implementation_report(), encoding="utf-8")
    records = [file_record(path, output) for path in sorted(output.iterdir()) if path.is_file() and path.name != "generation_result.json"]
    result = {
        "schema": "C410-GENERATION-RESULT-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "output_directory": OUT_REL,
        "artifact_count_excluding_generation_result": len(records),
        "artifacts": records,
        "required_static_files_present": all((output / name).is_file() for name in STATIC_NAMES),
        "source_hash_rows": source_hash_audit()["row_count"],
        "vacuum_pair_validation_rows": vacuum_pair_validation()["row_count"],
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
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
    parser.add_argument("--output", default=OUT_REL)
    args = parser.parse_args()
    result = generate(Path(args.output))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
