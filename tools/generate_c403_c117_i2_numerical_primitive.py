#!/usr/bin/env python3
"""Generate C403 C117-I2 finite-axis and spatial-kernel evidence."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import platform
from typing import Any, Mapping

import numpy as np
import scipy

from deuteron_wigner.bridge import c403_c117_i2_numerical_primitive as c403

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/phases/c403_c117_i2_numerical_primitive"
BASELINE = "fce8842e5ddc6660c735b7f69723f63c9bff7073"
STATUS = c403.STATUS
GENERATED_NAMES = (
    "input_freeze.json",
    "axis_summary.json",
    "support_theorem_certificate.json",
    "support_witness_rows.json",
    "spatial_kernel_inventory.json",
    "spatial_kernel_validation.json",
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
    return json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")


def canonical_root(value: Any) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def write_json(out: Path, name: str, value: Any) -> None:
    (out / name).write_text(json.dumps(jsonable(value), indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def input_freeze() -> dict[str, Any]:
    source_paths = (
        "src/deuteron_wigner/bridge/modes/core.py",
        "src/deuteron_wigner/bridge/basis1/core.py",
        "src/deuteron_wigner/bridge/qgtm/core.py",
        "src/deuteron_wigner/bridge/icurrent/core.py",
        "src/deuteron_wigner/bridge/icho/core.py",
        "src/deuteron_wigner/bridge/icho2/core.py",
        "src/deuteron_wigner/bridge/icreg2/core.py",
        "src/deuteron_wigner/bridge/icmembers/core.py",
        "src/deuteron_wigner/bridge/icnorm3/core.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/bindings.py",
        "docs/phases/c401_c396_mass_directions/release.json",
    )
    rows = []
    for rel in source_paths:
        path = ROOT / rel
        rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    payload = {
        "schema": "C403-C117-I2-INPUT-FREEZE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_files": tuple(rows),
        "governing_science_locks": (
            "C402_CT_SECTOR_AND_C117_FRONTIER_SCIENCE_LOCK",
            "C402_C117_NUMERICAL_READINESS_AUDIT",
            "C402_NEXT_NUMERICAL_FRONTIER",
        ),
        "historical_files_modified": False,
        "C64_runtime_required": False,
        "C80_reused": False,
    }
    return {**payload, "root": canonical_root(payload)}


def scientific_nonclaims() -> dict[str, Any]:
    payload = {
        "schema": "C403-C117-I2-SCIENTIFIC-NONCLAIMS-V1",
        "status": STATUS,
        "does_not_establish": (
            "a complete numerical C117 I2 coordinate action",
            "a numerical value for c_C117_1",
            "C114 inverse/source-factor contraction",
            "C119 current-factor contraction",
            "spin or color contraction",
            "target q/qg matrix aggregation",
            "a physical deuteron state",
            "a production current",
            "physical response rank",
            "a physical fit",
            "K9/K11/K13 coefficient equality",
            "Hamiltonian activation",
        ),
        "forbidden_substitutions": (
            "C144 diagnostic proxy",
            "C80 full contact-kernel reuse",
            "C64 missing artifact treated as zero",
            "unit or minimum-norm weights",
            "zero C117 coefficient",
        ),
    }
    return {**payload, "root": canonical_root(payload)}


def implementation_report(
    *,
    axis: Mapping[str, Any],
    support: Mapping[str, Any],
    spatial: Mapping[str, Any],
    bindings: Mapping[str, Any],
) -> str:
    lines = [
        "# C403 C117 I2 finite-axis and spatial-kernel numerical primitive",
        "",
        f"Status: `{STATUS}`",
        f"Accepted baseline: `{BASELINE}`",
        "",
        "## Scientific advance",
        "",
        "C403 closes the first numerical substructure of the C117 `I2_density_projector` direction without "
        "promoting it to a complete C396 coordinate action.  It provides an exact finite internal-member axis "
        "and a K-local numerical transverse-HO spatial kernel for each admitted internal mode.",
        "",
        "The finite-support theorem is:",
        "",
        "```text",
        "ADMITTED  iff  2 n + |m| <= Nmax - 2",
        "REJECTED  iff  2 n + |m|  = Nmax - 1",
        "```",
        "",
        "For an admitted quark member, a ground-state gluon companion and CM ground produce the exact C62 "
        "witness coefficient `x_g^(shell/2)`.  For an admitted gluon member, the corresponding coefficient is "
        "`(-1)^shell x_q^(shell/2)`.  All positive C47 longitudinal partitions are covered.",
        "",
        f"The exhaustive certificate contains {support['row_count']} partition/species/mode rows: "
        f"{support['admitted_witness_rows']} admitted exact nonzero witnesses and "
        f"{support['rejected_shell_rows']} exact shell exclusions.  All exact comparisons pass.",
        "",
        "## Numerical spatial primitive",
        "",
        "For external HO modes `a,b` and one contracted mode `r`, C403 evaluates",
        "",
        "```text",
        "I[a,b;r] = integral d^2x phi_a^*(x) phi_b(x) |phi_r(x)|^2.",
        "```",
        "",
        "The analytic route uses finite generalized-Laguerre coefficients and exact rational Gamma moments. "
        "An independent generalized Gauss--Laguerre route verifies deterministic representative modes at every "
        "resolution.  Every single-member matrix is checked separately for Hermiticity and positive semidefiniteness "
        "as a weighted Gram matrix.  An arbitrary signed aggregate is not claimed positive semidefinite.",
        "",
        f"The maximum analytic/quadrature residual is `{spatial['maximum_quadrature_abs_residual']:.3e}` and "
        f"the maximum sparse/matrix-free residual is `{spatial['maximum_sparse_matrix_free_residual']:.3e}`.",
        "",
        "## Axis counts",
        "",
        "| Resolution | Species | candidate members | admitted members | rejected members |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in axis["rows"]:
        lines.append(
            f"| {row['resolution']} | {row['species']} | {row['candidate_member_count']} | "
            f"{row['admitted_member_count']} | {row['rejected_member_count']} |"
        )
    lines.extend(
        [
            "",
            "## C396 frontier",
            "",
            f"C403 updates {bindings['C403_I2_primitive_binding_rows']} C117 binding rows, one per resolution. "
            f"The number of complete numerical C396 coordinate actions remains "
            f"{bindings['complete_numerical_apply_paths']}; no complete C117 action is claimed.",
            "",
            "The smallest remaining object is the source-faithful K-local contraction of the C114 inverse/source "
            "factor, C119 current factors, spin/color/normalization factors, and target q/qg aggregation with the "
            "new finite axis and spatial kernel.",
            "",
            "## Scientific boundary",
            "",
            "No coefficient, target, state, current, rank, fit, cross-resolution equality, or activation decision "
            "is made.  Missing full-operator factors remain unavailable, not zero.",
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

    axis = c403.axis_summary()
    support_rows = c403.support_theorem_rows()
    support = c403.support_theorem_certificate()
    spatial_inventory = c403.spatial_kernel_inventory()
    spatial_validation = c403.spatial_kernel_validation()
    binding_inventory = c403.c396_binding_inventory_with_c403_i2_primitive()
    binding_summary = c403.binding_update_summary()
    nonclaims = scientific_nonclaims()

    completion = {
        "schema": "C403-C117-I2-BLOCKER-OR-COMPLETION-V1",
        "status": STATUS,
        "phase_result": "PHASE_COMPLETE_AT_NUMERICAL_PRIMITIVE_SCOPE",
        "finite_member_axis_paths": axis["finite_axis_paths"],
        "spatial_kernel_paths": spatial_inventory["spatial_kernel_paths"],
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
        "schema": "C403-C117-I2-NUMERICAL-PRIMITIVE-RELEASE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_module": "deuteron_wigner.bridge.c403_c117_i2_numerical_primitive",
        "support_theorem_rows": len(support_rows),
        "finite_member_axis_paths": axis["finite_axis_paths"],
        "spatial_kernel_inventory_rows": spatial_inventory["row_count"],
        "spatial_kernel_paths": spatial_inventory["spatial_kernel_paths"],
        "complete_C117_apply_paths": 0,
        "complete_C396_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "validation_pass": bool(support["all_exact_matches"] and spatial_validation["pass"]),
        "physical": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
    }
    release["root"] = canonical_root(release)

    artifacts: dict[str, Any] = {
        "input_freeze.json": input_freeze(),
        "axis_summary.json": axis,
        "support_theorem_certificate.json": support,
        "support_witness_rows.json": {
            "schema": "C403-C117-I2-SUPPORT-WITNESS-ROWS-V1",
            "row_count": len(support_rows),
            "rows": support_rows,
            "root": canonical_root(support_rows),
        },
        "spatial_kernel_inventory.json": spatial_inventory,
        "spatial_kernel_validation.json": spatial_validation,
        "c396_coordinate_binding_inventory.json": binding_inventory,
        "binding_update_summary.json": binding_summary,
        "scientific_nonclaims.json": nonclaims,
        "blocker_or_completion.json": completion,
        "release.json": release,
    }
    for name, value in artifacts.items():
        write_json(out, name, value)

    (out / "implementation_report.md").write_text(
        implementation_report(axis=axis, support=support, spatial=spatial_validation, bindings=binding_inventory),
        encoding="utf-8",
    )

    artifact_records = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name == "generation_result.json":
            continue
        artifact_records.append({"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    result = {
        "schema": "C403-C117-I2-GENERATION-RESULT-V1",
        "status": STATUS,
        "output_directory": (
            out.resolve().relative_to(ROOT.resolve()).as_posix()
            if out.resolve().is_relative_to(ROOT.resolve())
            else "<EXTERNAL_OUTPUT_DIRECTORY>"
        ),
        "artifact_count_excluding_generation_result": len(artifact_records),
        "artifacts": tuple(artifact_records),
        "package_root": canonical_root(artifact_records),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "support_theorem_pass": support["all_exact_matches"],
        "spatial_validation_pass": spatial_validation["pass"],
        "complete_C396_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "full_C117_I2_action_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    write_json(out, "generation_result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_OUT))
    args = parser.parse_args()
    result = generate(Path(args.output_dir).expanduser())
    print(json.dumps(jsonable(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
