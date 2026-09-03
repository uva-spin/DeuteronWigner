#!/usr/bin/env python3
"""Generate C404 C117-I2 longitudinal/color primitive evidence."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import platform
from typing import Any, Mapping

import numpy as np
import scipy

from deuteron_wigner.bridge import c404_c117_i2_longitudinal_color_primitive as c404

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/phases/c404_c117_i2_longitudinal_color_primitive"
BASELINE = "bd568280de5fb2846b4ec5cdaff36e7ec973b8f1"
STATUS = c404.STATUS
GENERATED_NAMES = (
    "input_freeze.json",
    "longitudinal_transfer_inventory.json",
    "triplet_color_spin_validation.json",
    "factorization_stress_validation.json",
    "c396_coordinate_binding_inventory.json",
    "binding_update_summary.json",
    "scientific_nonclaims.json",
    "blocker_or_completion.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)


def jsonable(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    return value


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")


def canonical_root(value: Any) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def write_json(out: Path, name: str, value: Any) -> None:
    (out / name).write_text(
        json.dumps(jsonable(value), indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def input_freeze() -> dict[str, Any]:
    paths = (
        "src/deuteron_wigner/bridge/modes/core.py",
        "src/deuteron_wigner/bridge/basis1/core.py",
        "src/deuteron_wigner/bridge/icurrent/core.py",
        "src/deuteron_wigner/bridge/icho/core.py",
        "src/deuteron_wigner/bridge/icnorm3/core.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/basis.py",
        "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/axis.py",
        "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
        "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/bindings.py",
        "docs/phases/c403_c117_i2_numerical_primitive/release.json",
    )
    rows = []
    for rel in paths:
        path = ROOT / rel
        rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    payload = {
        "schema": "C404-C117-I2-LONGITUDINAL-COLOR-INPUT-FREEZE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_files": tuple(rows),
        "historical_files_modified": False,
        "C144_proxy_used": False,
        "C117_coefficient_selected": False,
        "source_qualified_product_topology_claimed": False,
    }
    return {**payload, "root": canonical_root(payload)}


def scientific_nonclaims() -> dict[str, Any]:
    payload = {
        "schema": "C404-C117-I2-LONGITUDINAL-COLOR-NONCLAIMS-V1",
        "status": STATUS,
        "does_not_establish": (
            "a product-specific C114/C115/C119 normal-ordering contraction map",
            "a complete numerical C117 I2 coordinate action",
            "a numerical value for c_C117_1",
            "a physical value for g_s",
            "a q-sector current-current matrix or a proof that every q-sector contribution vanishes",
            "a source-qualified interpretation of the algebraic tensor-product stress tests",
            "a physical deuteron state",
            "a production current",
            "physical response rank",
            "a physical fit",
            "K9/K11/K13 coefficient equality",
            "Hamiltonian activation",
        ),
        "forbidden_substitutions": (
            "C144 diagnostic proxy",
            "zero or identity for unavailable current factors",
            "minimum-norm C117 representative",
            "unit weights for target aggregation",
            "post-hoc symmetrization in place of source-order Hermitian reversal",
        ),
    }
    return {**payload, "root": canonical_root(payload)}


def implementation_report(
    longitudinal: Mapping[str, Any],
    color: Mapping[str, Any],
    stress: Mapping[str, Any],
    bindings: Mapping[str, Any],
) -> str:
    lines = [
        "# C404 C117 I2 longitudinal, spin, and triplet-color numerical primitives",
        "",
        f"Status: `{STATUS}`",
        f"Accepted local baseline: `{BASELINE}`",
        "",
        "## Scientific advance",
        "",
        "C404 closes three independently source-owned factor classes needed by the first C117 direction: "
        "the exact dimensionless C114 Q0/nonzero-transfer kernel on the C47 qg partition axis, the C45/C47 "
        "triplet color-charge products, and the diagonal J+ helicity/polarization selection rule.",
        "",
        "The exact partition kernel is",
        "",
        "```text",
        "kappa(p',p) = 0                         if p'=p (Q0 exclusion)",
        "              1/[kq(p')-kq(p)]^2       otherwise.",
        "```",
        "",
        "It is K-local and preserves exact total-K transfer: `n_q+n_g=0`.",
        "",
        "## K-local axis and transfer counts",
        "",
        "| resolution | partitions | nonzero Q0 pairs | qg dimension |",
        "|---|---:|---:|---:|",
    ]
    for row in longitudinal["rows"]:
        lines.append(
            f"| {row['resolution']} | {row['partition_count']} | {row['nonzero_Q0_pairs']} | "
            f"{row['axis']['dimension']} |"
        )
    lines.extend(
        [
            "",
            "C404 explicitly verifies the C47 intrinsic-mode order and records the permutation needed to read "
            "the C403 spatial kernel in that order.",
            "",
            "## Triplet color algebra",
            "",
            "The four exact scalar products are `4/3`, `-3/2`, `-3/2`, and `3` for "
            "`J_qJ_q`, `J_qJ_g`, `J_gJ_q`, and `J_gJ_g`, respectively. Their sum gives the triplet Casimir "
            "`4/3`. The maximum color residual is "
            f"`{max(row['scalar_identity_residual'] for row in color['product_rows']):.3e}`.",
            "",
            "## Factorization stress test",
            "",
            "The closed longitudinal, C403 spatial, spin-selection, and color factors are composed in sparse and "
            "independent matrix-free routes. This is deliberately classified as:",
            "",
            "```text",
            "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING",
            "```",
            "",
            f"The maximum sparse/matrix-free residual is `{stress['maximum_sparse_matrix_free_residual']:.3e}` "
            f"and the maximum Hermiticity residual is `{stress['maximum_hermiticity_residual']:.3e}`.",
            "",
            "The missing product-specific normal-ordering and external-mode contraction map prevents these "
            "stress-test matrices from being interpreted as current-product matrix elements.",
            "",
            "## C396 frontier",
            "",
            f"C404 updates {bindings['C404_C117_I2_primitive_binding_rows']} K-local `c_C117_1` rows. "
            f"The complete numerical C396 path count remains {bindings['complete_numerical_apply_paths']} and "
            "the complete C117 path count remains zero.",
            "",
            "The smallest missing object is the source-qualified product topology and finite-cell/current-factor "
            "assembly, followed by count-once q/qg target embedding and an independently constructed Hermitian reverse.",
            "",
            "No coefficient, coupling, target, state, current, rank, fit, resolution average, merge, push, or "
            "activation decision is made.",
            "",
        ]
    )
    return "\n".join(lines)


def generate(out: Path) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_NAMES:
        path = out / name
        if path.exists():
            path.unlink()

    longitudinal = c404.longitudinal_inventory()
    color = c404.color_spin_validation()
    stress = c404.skeleton_validation()
    binding_inventory = c404.c396_binding_inventory_with_c404_primitives()
    binding_summary = c404.binding_update_summary()
    nonclaims = scientific_nonclaims()

    completion = {
        "schema": "C404-C117-I2-LONGITUDINAL-COLOR-COMPLETION-V1",
        "status": STATUS,
        "phase_result": "PHASE_COMPLETE_AT_NUMERICAL_PRIMITIVE_SCOPE",
        "longitudinal_Q0_paths": 3,
        "triplet_color_product_paths": 12,
        "spin_selection_paths": 3,
        "algebraic_factorization_stress_paths": 12,
        "source_qualified_factorization_operator_paths": 0,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "full_C117_I2_action_ready": False,
        "full_C396_19_coordinate_forward_map_ready": False,
        "smallest_missing_object": binding_summary["smallest_missing_object_for_complete_C117_I2_action"],
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    completion["root"] = canonical_root(completion)

    release = {
        "schema": "C404-C117-I2-LONGITUDINAL-COLOR-RELEASE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_module": "deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive",
        "longitudinal_validation_pass": all(
            row["symmetry_residual"] == 0 and row["diagonal_residual"] == 0
            for row in longitudinal["rows"]
        ),
        "color_spin_validation_pass": color["pass"],
        "factorization_stress_validation_pass": stress["pass"],
        "source_qualified_product_topology": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    release["root"] = canonical_root(release)

    write_json(out, "input_freeze.json", input_freeze())
    write_json(out, "longitudinal_transfer_inventory.json", longitudinal)
    write_json(out, "triplet_color_spin_validation.json", color)
    write_json(out, "factorization_stress_validation.json", stress)
    write_json(out, "c396_coordinate_binding_inventory.json", binding_inventory)
    write_json(out, "binding_update_summary.json", binding_summary)
    write_json(out, "scientific_nonclaims.json", nonclaims)
    write_json(out, "blocker_or_completion.json", completion)
    write_json(out, "release.json", release)
    (out / "implementation_report.md").write_text(
        implementation_report(longitudinal, color, stress, binding_inventory).rstrip() + "\n",
        encoding="utf-8",
    )

    artifacts = []
    for path in sorted(out.iterdir()):
        if path.is_file() and path.name != "generation_result.json":
            artifacts.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
            )
    package_root = canonical_root(artifacts)
    result = {
        "schema": "C404-C117-I2-LONGITUDINAL-COLOR-GENERATION-RESULT-V1",
        "status": STATUS,
        "output_directory": "docs/phases/c404_c117_i2_longitudinal_color_primitive",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "artifact_count_excluding_generation_result": len(artifacts),
        "artifacts": artifacts,
        "package_root": package_root,
        "partition_counts": {
            row["resolution"]: row["partition_count"] for row in longitudinal["rows"]
        },
        "qg_dimensions": {
            row["resolution"]: row["axis"]["dimension"] for row in longitudinal["rows"]
        },
        "maximum_longitudinal_symmetry_residual": max(
            row["symmetry_residual"] for row in longitudinal["rows"]
        ),
        "maximum_color_scalar_residual": max(
            row["scalar_identity_residual"] for row in color["product_rows"]
        ),
        "maximum_factorization_stress_residual": stress["maximum_sparse_matrix_free_residual"],
        "source_qualified_product_topology": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    write_json(out, "generation_result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    result = generate(args.out.resolve())
    print(json.dumps(jsonable(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
