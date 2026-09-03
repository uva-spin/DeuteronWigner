#!/usr/bin/env python3
"""Generate deterministic C409 evidence."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from deuteron_wigner.bridge.c409_c117_i2_derivative_density_reconciliation import (
    STATUS,
    binding_update_summary,
    c396_binding_inventory_with_c409_reconciliation,
    completion_record,
    derivative_count_authority,
    derivative_count_validation,
    jgjg_qg_validation,
    reduced_transverse_authority,
    scale_power_reconciliation,
    scientific_boundary_record,
    source_hash_audit,
)

BASELINE = "ab0af6587131a2846425e9bb19cfdc784b9f0bdb"
PHASE = "C409_C117_I2_DERIVATIVE_DENSITY_RECONCILIATION"

GENERATED_NAMES = (
    "input_freeze.json",
    "source_hash_audit.json",
    "derivative_count_authority.json",
    "scale_power_reconciliation.json",
    "reduced_transverse_authority.json",
    "derivative_count_validation.json",
    "jgjg_qg_validation.json",
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
    "C409_ACCEPTANCE_SPEC.json",
    "C409_C117_I2_DERIVATIVE_DENSITY_RECONCILIATION_SCIENCE_LOCK.md",
    "C409_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md",
    "C409_MERGE_READINESS_CHECKLIST.md",
    "C409_SOURCE_EVIDENCE_HASHES.json",
    "C409_TWO_CLEAN_BUILDS.json",
    "C409_PYTHON39_COMPATIBILITY_AUDIT.json",
    "C409_EXPECTED_COMMIT_PATHS.json",
    "CHATGPT_STAGE_IMPLEMENTATION_REPORT.md",
    "CHATGPT_STAGE_TEST_EXECUTION.json",
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
    return (
        json.dumps(plain(value), sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value))


def file_record(path: Path, root: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": len(data),
        "sha256": sha256(data).hexdigest(),
    }


def input_freeze() -> dict[str, Any]:
    return {
        "schema": "C409-INPUT-FREEZE-V1",
        "phase": PHASE,
        "baseline": BASELINE,
        "source_hash_audit": source_hash_audit(),
        "upstream": {
            "C408_merge_commit": BASELINE,
            "source_routed_product_block_primitive_paths": 9,
            "complete_C396_numerical_apply_paths": 6,
            "complete_C117_numerical_apply_paths": 0,
        },
        "physical_coupling": None,
        "C117_coefficient": None,
        "physical_targets": None,
        "rank_evaluation": False,
    }


def implementation_report() -> str:
    derivative = derivative_count_validation()
    product = jgjg_qg_validation()
    complete = completion_record()
    return """# C409 implementation report

## Result

`{status}`

C409 reconciles the derivative count for the number-preserving `J_gJ_g:qg->qg` route. The C114/C192 source contains exactly two longitudinal derivatives, one in each gluon current. C406 evaluates each complete one-gluon current descendant and C407 evaluates their product with the inverse-square kernel. C409 therefore excludes the additional C119 derivative leaf and C124/C126 `pi*k/L` member factor on this reduced route.

## Numerical checks

- Source authority rows: {sources}
- Exact derivative-reconstruction rows: {drows}
- Source-routed JgJg qg paths: {jpaths}
- Maximum sparse/matrix-free residual: {mres:.3e}
- Maximum Hermiticity residual: {hres:.3e}
- Maximum single-counted C_A equivalence residual: {cres:.3e}
- Source-routed product-block primitive paths after C409: {paths}
- Complete C117 numerical apply paths: {c117}
- Complete C396 numerical apply paths: {c396}

## Remaining exact frontier

{missing}

No physical coefficient, rank, fit, complete C117 action, or activation is claimed.
""".format(
        status=STATUS,
        sources=source_hash_audit()["row_count"],
        drows=derivative["row_count"],
        jpaths=product["source_routed_J_gJ_g_qg_paths"],
        mres=product["maximum_sparse_matrix_free_residual"],
        hres=product["maximum_hermiticity_residual"],
        cres=product["maximum_single_counted_C_A_equivalence_residual"],
        paths=complete["source_routed_product_block_primitive_paths"],
        c117=complete["complete_C117_numerical_apply_paths"],
        c396=complete["complete_C396_numerical_apply_paths"],
        missing=complete["smallest_missing_object"],
    )


def scientific_nonclaims() -> dict[str, Any]:
    return {
        "schema": "C409-SCIENTIFIC-NONCLAIMS-V1",
        "phase": PHASE,
        "not_established": (
            "J_gJ_g q-sector pair or vacuum branches",
            "complete route-reconciled finite-cell/field/state/M2 normalization",
            "complete target count-once aggregation",
            "complete C117 I2 Hamiltonian-coordinate action",
            "physical value of g_s or c_C117_1",
            "physical response rank",
            "physical fit",
            "Hamiltonian activation",
        ),
        "C124_generic_derivative_density_semantics_replaced": False,
        "unavailable_is_zero": False,
        "source_routed_product_block_primitive_paths": 12,
        "complete_C396_numerical_apply_paths": 6,
    }


def release() -> dict[str, Any]:
    completion = completion_record()
    return {
        "schema": "C409-RELEASE-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "derivative_count_reconciled": completion[
            "derivative_count_validation_pass"
        ],
        "J_gJ_g_number_preserving_qg_product_block_ready": completion[
            "J_gJ_g_number_preserving_qg_product_block_ready"
        ],
        "J_gJ_g_q_sector_complete": False,
        "source_routed_product_block_primitive_paths": 12,
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
        "input_freeze.json": input_freeze(),
        "source_hash_audit.json": source_hash_audit(),
        "derivative_count_authority.json": derivative_count_authority(),
        "scale_power_reconciliation.json": scale_power_reconciliation(),
        "reduced_transverse_authority.json": reduced_transverse_authority(),
        "derivative_count_validation.json": derivative_count_validation(),
        "jgjg_qg_validation.json": jgjg_qg_validation(),
        "scientific_boundary.json": scientific_boundary_record(),
        "c396_coordinate_binding_inventory.json": (
            c396_binding_inventory_with_c409_reconciliation()
        ),
        "binding_update_summary.json": binding_update_summary(),
        "blocker_or_completion.json": completion_record(),
        "scientific_nonclaims.json": scientific_nonclaims(),
        "release.json": release(),
    }
    for name, value in artifacts.items():
        write_json(output / name, value)
    (output / "implementation_report.md").write_text(
        implementation_report(), encoding="utf-8"
    )
    records = []
    for path in sorted(output.iterdir()):
        if path.name == "generation_result.json" or not path.is_file():
            continue
        records.append(file_record(path, output))
    result = {
        "schema": "C409-GENERATION-RESULT-V1",
        "phase": PHASE,
        "status": STATUS,
        "baseline": BASELINE,
        "output_directory": (
            "docs/phases/c409_c117_i2_derivative_density_reconciliation"
        ),
        "artifact_count_excluding_generation_result": len(records),
        "artifacts": records,
        "required_static_files_present": all(
            (output / name).is_file() for name in STATIC_NAMES
        ),
        "source_hash_rows": source_hash_audit()["row_count"],
        "derivative_count_rows": derivative_count_validation()["row_count"],
        "source_routed_J_gJ_g_qg_paths": 3,
        "source_routed_product_block_primitive_paths": 12,
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
        default="docs/phases/c409_c117_i2_derivative_density_reconciliation",
    )
    args = parser.parse_args()
    result = generate(Path(args.output))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
