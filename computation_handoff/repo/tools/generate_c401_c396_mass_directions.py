#!/usr/bin/env python3
"""Generate deterministic C401 evidence for the first numerical C396 directions.

The generator never rewrites C128, C47, C396, or C400.S2 history.  It records
source/formula authority, emits the six K-local quark/gluon mass-direction
bindings, and keeps physical fitting, rank, and activation explicitly closed.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys
from typing import Any, Mapping

import numpy as np
import scipy

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.free2 import core as c128
from deuteron_wigner.bridge.hqcdrimassc43hamiltonianacceptphase1 import core as c396
from deuteron_wigner.bridge.c400_s2_corrective.coordinate_bindings import (
    coordinate_binding_inventory as c400_binding_inventory,
)
from deuteron_wigner.bridge import c401_c396_mass_directions as c401

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/phases/c401_c396_mass_directions"
BASELINE = "ada80920fb51617333c9b87a40d6538a0b0de915"
STATUS = "C396_FIRST_SIX_K_LOCAL_NUMERICAL_BINDINGS_READY_DIAGNOSTIC_ONLY"

GENERATED_NAMES = (
    "input_freeze.json",
    "resolution_records.json",
    "basis_fraction_provenance.json",
    "historical_c128_partition_defect.json",
    "mass_direction_operator_inventory.json",
    "sparse_matrix_free_validation.json",
    "finite_difference_validation.json",
    "historical_c128_derivative_comparison.json",
    "c396_coordinate_binding_inventory.json",
    "coordinate_reduction.json",
    "binding_update_summary.json",
    "scientific_nonclaims.json",
    "blocker_or_completion.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)


def jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set)):
        return [jsonable(item) for item in value]
    if isinstance(value, Fraction):
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
            "exact": str(value),
            "float": float(value),
        }
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.integer, np.floating, np.bool_)):
        return value.item()
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, Path):
        try:
            return value.resolve().relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            return str(value)
    if isinstance(value, float) and not np.isfinite(value):
        return "NaN" if np.isnan(value) else "Infinity" if value > 0 else "-Infinity"
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_root(value: Any) -> str:
    payload = json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def write_json(out: Path, name: str, value: Any) -> Path:
    path = out / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(jsonable(value), indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    return path


def source_file_record(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(path)
    return {
        "path": relative,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def input_freeze() -> dict[str, Any]:
    source_paths = (
        "references/c43_light_front_qcd_gauge_action.tex",
        "src/deuteron_wigner/bridge/basis1/core.py",
        "src/deuteron_wigner/bridge/free2/core.py",
        "src/deuteron_wigner/bridge/hqcdid3/core.py",
        "src/deuteron_wigner/bridge/hqcdrenred/core.py",
        "src/deuteron_wigner/bridge/hqcdrimassc43hamiltonianacceptphase1/core.py",
        "src/deuteron_wigner/bridge/c400_s2_corrective/coordinate_bindings.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/basis.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/operators.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/bindings.py",
    )
    previous = c400_binding_inventory()
    payload = {
        "schema": "C401-C396-MASS-DIRECTION-INPUT-FREEZE-V1",
        "accepted_repository_baseline": BASELINE,
        "historical_packages_immutable": True,
        "source_files": tuple(source_file_record(path) for path in source_paths),
        "source_records": {
            "C47_status": c47.STATUS,
            "C128_status": c128.STATUS,
            "C128_package_root": c128.PACKAGE_ROOT,
            "C396_status": c396.STATUS,
            "C396_package_root": c396.PACKAGE_ROOT,
            "C400_S2_inventory_schema": previous["schema"],
            "C400_S2_inventory_rows": previous["total_rows"],
            "C400_S2_inventory_root": canonical_root(previous),
        },
        "science_constraints": {
            "C144_proxy_allowed": False,
            "physical_parameter_selection": False,
            "rank_status": "RANK_NOT_EVALUATED",
            "resolution_average": False,
            "activation_gate_status": "NOT_READY",
        },
    }
    return {**payload, "root": canonical_root(payload)}


def scientific_nonclaims() -> dict[str, Any]:
    payload = {
        "schema": "C401-C396-MASS-DIRECTION-SCIENTIFIC-NONCLAIMS-V1",
        "nonclaims": (
            "no complete C396 19-coordinate numerical Hamiltonian",
            "no numerical ct_sector apply path",
            "no numerical source-null apply path",
            "no numerical C117 apply path",
            "no sector-qualified physical deuteron state",
            "no production current selection",
            "no physical coordinate value or counterterm value",
            "no likelihood fit",
            "no physical response rank",
            "no K9/K11/K13 convergence claim",
            "no resolution averaging",
            "no Hamiltonian activation",
            "no claim that historical C128 qg kinetic terms are numerically source-correct",
        ),
        "historical_C128_modified": False,
        "physical_fit_authorized": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": canonical_root(payload)}


def implementation_report(
    *,
    resolutions: Mapping[str, Any],
    defect: Mapping[str, Any],
    operator_inventory: Mapping[str, Any],
    validation: Mapping[str, Any],
    binding_summary: Mapping[str, Any],
) -> str:
    lines = [
        "# C401 — first numerical C396 mass-direction implementation",
        "",
        f"Status: `{STATUS}`",
        f"Accepted baseline: `{BASELINE}`",
        "Physical fit: forbidden",
        "Physical rank: not evaluated",
        "Activation: not ready",
        "",
        "## Implemented numerical directions",
        "",
        "C401 implements two source-owned mass-squared derivative directions at each of K9, K11, and K13:",
        "",
        r"\[D_{q,K}=\partial H_K/\partial\mu_{q,K}^2,\qquad D_{g,K}=\partial H_K/\partial\delta\mu_{g,K}^2.\]",
        "",
        "On the q sector their exact values are 1 and 0.  On each qg longitudinal partition they are "
        r"\(1/x_q\) and \(1/x_g\), with fractions taken from the exact C45/C47 partition authority.",
        "",
        f"The operator inventory contains **{operator_inventory['row_count']}** complete K-local apply rows. "
        "Each direction has a serialized COO record, an actual SciPy CSR representation, a SciPy LinearOperator, "
        "and an independent matrix-free block action.",
        "",
        "## Resolution records",
        "",
        "| Label | Exact K | Nmax | bHO | q dim | qg dim | direct dim |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in resolutions["rows"]:
        lines.append(
            f"| {row['resolution_label']} | {row['K_fraction']} | {row['Nmax']} | "
            f"{row['b_HO']} {row['b_HO_unit']} | {row['q_dimension']} | "
            f"{row['qg_dimension']} | {row['direct_sum_dimension']} |"
        )
    lines.extend(
        [
            "",
            "## Historical C128 partition defect discovered",
            "",
            "The historical private C128 partition helper does not satisfy the C47 identities for the quark mode: "
            r"it shifts \(k_q\) by \(+1/2\), \(x_q\) by \(+1/K_2\), and gives "
            r"\(x_q+x_g=1+1/K_2\).  The gluon fraction is unchanged.",
            "",
            f"Affected resolutions: {', '.join(defect['affected_resolutions'])}.  The historical C128 files were "
            "not edited.  C401 uses a versioned source-corrected adapter and records the mismatch explicitly.",
            "",
            "This defect affects the historical qg quark-mass derivative and qg transverse kinetic denominator. "
            "It does not materially affect the historical gluon-mass derivative.",
            "",
            "## Validation",
            "",
            f"- Sparse/CSR/LinearOperator/matrix-free route agreement: `{validation['sparse_matrix_free_pass']}`.",
            f"- Independent source-formula finite differences: `{validation['finite_difference_pass']}`.",
            f"- Historical quark-fraction defect exposed: `{validation['historical_quark_fraction_defect_exposed']}`.",
            f"- Historical gluon fraction unchanged at material tolerance: `{validation['historical_gluon_fraction_unchanged']}`.",
            "",
            "## C396 frontier update",
            "",
            f"The C400.S2 inventory contained 57 symbolic K-local rows and zero complete numerical apply paths. "
            f"C401 now records **{binding_summary['current_complete_numerical_apply_paths']}** complete numerical "
            "apply paths.  The full C396 forward map remains unavailable.",
            "",
            "The next source-ordered operator frontier is `ct_sector`, followed by the four C117 insertions and "
            "then owner-by-owner classification of the nine source-null directions.",
            "",
            "## Scientific boundary",
            "",
            "No physical mass, counterterm, state, current, covariance, likelihood, rank, or activation decision "
            "is made in this implementation.",
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

    resolutions = {
        "schema": "C401-C396-RESOLUTION-RECORDS-V1",
        "rows": tuple(c401.resolution_record(r) for r in c401.RESOLUTION_LABELS),
        "exact_K_required": True,
        "K2_is_label_not_physical_K": True,
    }
    resolutions["root"] = canonical_root(resolutions)
    fractions = {
        "schema": "C401-C396-BASIS-FRACTION-PROVENANCE-SET-V1",
        "rows": tuple(c401.basis_fraction_provenance(r) for r in c401.RESOLUTION_LABELS),
    }
    fractions["root"] = canonical_root(fractions)
    defect = c401.historical_c128_partition_defect_audit()
    operator_inventory = c401.mass_direction_operator_inventory()
    sparse = {
        "schema": "C401-C396-SPARSE-MATRIX-FREE-VALIDATION-SET-V1",
        "rows": tuple(c401.sparse_matrix_free_validation(r) for r in c401.RESOLUTION_LABELS),
    }
    sparse["pass"] = all(row["pass"] for row in sparse["rows"])
    sparse["root"] = canonical_root(sparse)
    finite = {
        "schema": "C401-C396-SOURCE-FORMULA-FINITE-DIFFERENCE-SET-V1",
        "rows": tuple(c401.finite_difference_validation(r) for r in c401.RESOLUTION_LABELS),
    }
    finite["pass"] = all(row["pass"] for row in finite["rows"])
    finite["root"] = canonical_root(finite)
    historical = {
        "schema": "C401-HISTORICAL-C128-DERIVATIVE-COMPARISON-SET-V1",
        "rows": tuple(c401.historical_c128_derivative_comparison(r) for r in c401.RESOLUTION_LABELS),
    }
    historical["root"] = canonical_root(historical)
    validation = c401.all_validation_records()
    binding_inventory = c401.c396_binding_inventory_with_c401_mass_directions()
    reduction = c401.coordinate_reduction_record()
    binding_summary = c401.binding_update_summary()
    nonclaims = scientific_nonclaims()

    completion = {
        "schema": "C401-C396-MASS-DIRECTION-COMPLETION-V1",
        "status": STATUS,
        "phase_result": "PHASE_COMPLETE_AT_FIRST_NUMERICAL_OPERATOR_SLICE",
        "complete_K_local_numerical_apply_paths": binding_inventory[
            "complete_numerical_apply_paths"
        ],
        "expected_complete_K_local_numerical_apply_paths": 6,
        "full_C396_19_coordinate_forward_map_ready": False,
        "historical_C128_partition_defect_exposed": True,
        "historical_C128_modified": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "next_scientific_frontier": (
            "resolve and implement the source normalization of ct_sector, then bind the four "
            "C117 insertions and classify the nine source-null directions"
        ),
    }
    completion["root"] = canonical_root(completion)
    release = {
        "schema": "C401-C396-MASS-DIRECTION-RELEASE-V1",
        "status": STATUS,
        "accepted_repository_baseline": BASELINE,
        "source_module": "deuteron_wigner.bridge.c401_c396_mass_directions",
        "operator_rows": operator_inventory["row_count"],
        "binding_rows": binding_inventory["total_rows"],
        "complete_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "validation_pass": validation["pass"],
        "physical": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
    }
    release["root"] = canonical_root(release)

    artifacts: dict[str, Any] = {
        "input_freeze.json": input_freeze(),
        "resolution_records.json": resolutions,
        "basis_fraction_provenance.json": fractions,
        "historical_c128_partition_defect.json": defect,
        "mass_direction_operator_inventory.json": operator_inventory,
        "sparse_matrix_free_validation.json": sparse,
        "finite_difference_validation.json": finite,
        "historical_c128_derivative_comparison.json": historical,
        "c396_coordinate_binding_inventory.json": binding_inventory,
        "coordinate_reduction.json": reduction,
        "binding_update_summary.json": binding_summary,
        "scientific_nonclaims.json": nonclaims,
        "blocker_or_completion.json": completion,
        "release.json": release,
    }
    for name, value in artifacts.items():
        write_json(out, name, value)

    report = implementation_report(
        resolutions=resolutions,
        defect=defect,
        operator_inventory=operator_inventory,
        validation=validation,
        binding_summary=binding_summary,
    )
    (out / "implementation_report.md").write_text(report, encoding="utf-8")

    artifact_records = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name == "generation_result.json":
            continue
        artifact_records.append(
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    result = {
        "schema": "C401-C396-MASS-DIRECTION-GENERATION-RESULT-V1",
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
        "validation_pass": validation["pass"],
        "complete_numerical_apply_paths": binding_inventory["complete_numerical_apply_paths"],
        "full_C396_forward_map_ready": False,
        "physical_fit_authorized": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "activation_gate_status": "NOT_READY",
    }
    write_json(out, "generation_result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_OUT))
    args = parser.parse_args()
    output = Path(args.output_dir).expanduser()
    result = generate(output)
    print(json.dumps(jsonable(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
