#!/usr/bin/env python3
"""Generate C406 one-gluon normal-order descendant evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import platform
from typing import Any, Mapping

import numpy as np
import scipy

from deuteron_wigner.bridge import c406_c117_i2_gluon_normal_order_descendant as c406

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/phases/c406_c117_i2_gluon_normal_order_descendant"
BASELINE = "4dbb0b8bbadc540f0da2337c46040afb971fffc1"
STATUS = c406.STATUS
GENERATED_NAMES = (
    "input_freeze.json",
    "source_hash_audit.json",
    "gluon_normal_order_authority.json",
    "one_gluon_descendant_inventory.json",
    "product_routing_audit.json",
    "mixed_current_collapse_validation.json",
    "mixed_q_sector_zero_certificates.json",
    "same_species_contraction_requirements.json",
    "mixed_kernel_validation.json",
    "c396_coordinate_binding_inventory.json",
    "binding_update_summary.json",
    "scientific_nonclaims.json",
    "blocker_or_completion.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)
STATIC_NAMES = (
    "C406_C117_I2_GLUON_NORMAL_ORDER_DESCENDANT_SCIENCE_LOCK.md",
    "C406_MATHEMATICAL_AND_ALGORITHMIC_DESIGN.md",
    "C406_ACCEPTANCE_SPEC.json",
    "C406_MERGE_READINESS_CHECKLIST.md",
)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
            "exact": str(value),
            "float": float(value),
        }
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
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


def source_paths() -> tuple[str, ...]:
    return (
        "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py",
        "src/deuteron_wigner/bridge/hqcdg2pt/core.py",
        "src/deuteron_wigner/bridge/modes/core.py",
        "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
        "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/longitudinal.py",
        "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/color_spin.py",
        "src/deuteron_wigner/bridge/c405_c117_i2_current_topology_embedding/derivative_order.py",
        "src/deuteron_wigner/bridge/c405_c117_i2_current_topology_embedding/embedding.py",
        "src/deuteron_wigner/bridge/c405_c117_i2_current_topology_embedding/bindings.py",
        "docs/phases/c405_c117_i2_current_topology_embedding/release.json",
        "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/normal_order.py",
        "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/routing.py",
        "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/mixed_kernel.py",
        "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/bindings.py",
        "src/deuteron_wigner/bridge/c406_c117_i2_gluon_normal_order_descendant/closure.py",
    )


def source_hash_audit() -> dict[str, Any]:
    rows = []
    for rel in source_paths():
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(path)
        rows.append(
            {
                "path": rel,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    payload = {
        "schema": "C406-C117-I2-SOURCE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": rows,
        "row_count": len(rows),
        "all_present": True,
        "historical_sources_modified": False,
    }
    return {**payload, "root": canonical_root(payload)}


def input_freeze() -> dict[str, Any]:
    hashes = source_hash_audit()
    payload = {
        "schema": "C406-C117-I2-INPUT-FREEZE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_hash_audit_root": hashes["root"],
        "source_files": hashes["rows"],
        "historical_files_modified": False,
        "C144_proxy_used": False,
        "C117_coefficient_selected": False,
        "same_species_external_pair_proxy_used": False,
        "mixed_current_orders_merged": False,
        "physical_rank_evaluated": False,
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": canonical_root(payload)}


def mixed_collapse_validation() -> dict[str, Any]:
    rows = []
    maximum_exact_residual = Fraction(0, 1)
    maximum_symmetry_residual = 0.0
    for resolution in ("K9", "K11", "K13"):
        for product in c406.MIXED_PRODUCTS:
            row = c406.mixed_c405_collapse_record(resolution, product)
            exact = row["maximum_exact_residual"]
            maximum_exact_residual = max(maximum_exact_residual, exact)
            maximum_symmetry_residual = max(
                maximum_symmetry_residual, float(row["matrix_symmetry_residual"])
            )
            rows.append(row)
    payload = {
        "schema": "C406-C117-I2-MIXED-CURRENT-COLLAPSE-VALIDATION-V1",
        "status": STATUS,
        "rows": rows,
        "row_count": len(rows),
        "maximum_exact_residual": maximum_exact_residual,
        "maximum_matrix_symmetry_residual": maximum_symmetry_residual,
        "identity": "C406 = -(C405_BRA + C405_KET)",
        "pass": maximum_exact_residual == 0 and maximum_symmetry_residual < 2e-14,
        "complete_C117_action": False,
    }
    return {**payload, "root": canonical_root(payload)}


def mixed_zero_certificates() -> dict[str, Any]:
    rows = [c406.mixed_q_sector_zero_certificate(product) for product in c406.MIXED_PRODUCTS]
    payload = {
        "schema": "C406-C117-I2-MIXED-Q-SECTOR-ZERO-CERTIFICATES-V1",
        "status": STATUS,
        "rows": rows,
        "row_count": len(rows),
        "all_exact_zero": all(
            row["status_value"] == "EXACT_ZERO_WITH_NORMAL_ORDERING_COLOR_TRACE_PROOF"
            for row in rows
        ),
        "zero_fill_used": False,
    }
    return {**payload, "root": canonical_root(payload)}


def same_species_requirements() -> dict[str, Any]:
    rows = [
        c406.same_species_intermediate_requirement(product)
        for product in c406.SAME_SPECIES_PRODUCTS
    ]
    payload = {
        "schema": "C406-C117-I2-SAME-SPECIES-REQUIREMENTS-V1",
        "status": STATUS,
        "rows": rows,
        "row_count": len(rows),
        "all_unavailable_not_zero": all(row["numerical_apply_path"] is None for row in rows),
        "external_pair_proxy_promoted": False,
    }
    return {**payload, "root": canonical_root(payload)}


def scientific_nonclaims() -> dict[str, Any]:
    payload = {
        "schema": "C406-C117-I2-SCIENTIFIC-NONCLAIMS-V1",
        "status": STATUS,
        "does_not_establish": (
            "a complete numerical C117 I2 coordinate action",
            "a complete J_qJ_q or J_gJ_g one-particle contraction descendant",
            "a complete finite-cell/current/field/state normalization",
            "a target-member aggregation or count-once multiplicity",
            "a numerical value for g_s or c_C117_1",
            "a complete C396 forward map",
            "physical response rank, identifiability, calibration, or activation",
        ),
        "forbidden_substitutions": (
            "C144 diagnostic proxy",
            "zero matrix for an unavailable same-species product",
            "external-pair transfer kernel in place of an internal contraction axis",
            "factor-two merge of J_qJ_g and J_gJ_q",
            "minimum-norm or zero C117 representative",
            "default product normalization",
        ),
    }
    return {**payload, "root": canonical_root(payload)}


def implementation_report(
    normal: Mapping[str, Any],
    descendants: Mapping[str, Any],
    routing: Mapping[str, Any],
    collapse: Mapping[str, Any],
    mixed: Mapping[str, Any],
    binding: Mapping[str, Any],
    completion: Mapping[str, Any],
) -> str:
    return "\n".join(
        (
            "# C406 C117 I2 gluon normal-order descendant",
            "",
            f"Status: `{STATUS}`",
            f"Accepted local baseline: `{BASELINE}`",
            "",
            "## Scientific advance",
            "",
            "C406 derives the one-gluon number-preserving descendant of the C192 ordered gluon current using the C45 longitudinal phase, C151 canonical one-gluon normalization, and the Hermitian adjoint-color convention. The two normal-order contributions add to `-(k_bra+k_ket) F^a`; the bosonic commutator vanishes exactly because `f^{abb}=0`.",
            "",
            "For the mixed products `J_qJ_g` and `J_gJ_q`, the result collapses C405's BRA/KET candidate family exactly. The mixed q-sector block is proved zero from the same color/normal-ordering algebra. Same-species `J_qJ_q` and `J_gJ_g` products remain unavailable because they require explicit intermediate one-particle contraction axes rather than the external-pair transfer kernel.",
            "",
            "## Numerical evidence",
            "",
            f"- one-gluon external mode-pair rows: {descendants['row_count']}",
            f"- normal-order validation: {normal['pass']}",
            f"- maximum color/mode Hermiticity residual: {normal['maximum_mode_color_hermiticity_residual']:.3e}",
            f"- routing rows: {routing['row_count']}",
            f"- mixed rows: {routing['mixed_product_rows']}",
            f"- same-species unresolved rows: {routing['same_species_rows']}",
            f"- exact C405-collapse rows: {collapse['row_count']}",
            f"- maximum exact collapse residual: {jsonable(collapse['maximum_exact_residual'])}",
            f"- mixed kernel rows: {mixed['row_count']}",
            f"- maximum sparse/matrix-free residual: {mixed['maximum_sparse_matrix_free_residual']:.3e}",
            f"- maximum adjoint residual: {mixed['maximum_adjoint_residual']:.3e}",
            "",
            "## Binding and completion boundary",
            "",
            f"- C406 K-local descendant binding rows: {binding['C117_I2_descendant_rows']}",
            f"- complete C117 numerical paths: {completion['complete_C117_numerical_apply_paths']}",
            f"- complete C396 numerical paths: {completion['complete_C396_numerical_apply_paths']}",
            f"- full C117 action ready: {completion['full_C117_I2_action_ready']}",
            f"- rank status: `{completion['rank_status']}`",
            f"- physical fit authorized: {completion['physical_fit_authorized']}",
            f"- activation: `{completion['activation_gate_status']}`",
            "",
            "## Smallest remaining object",
            "",
            completion["smallest_missing_object"],
            "",
            "No physical coefficient, rank, fit, activation, merge, or push is authorized by this phase.",
            "",
        )
    )


def release_record(completion: Mapping[str, Any], package_root: str) -> dict[str, Any]:
    payload = {
        "schema": "C406-C117-I2-RELEASE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "package_root": package_root,
        "one_gluon_normal_order_descendant_ready": completion[
            "one_gluon_normal_order_descendant_ready"
        ],
        "mixed_product_derivative_routing_ready": completion[
            "mixed_product_derivative_routing_ready"
        ],
        "same_species_contraction_axes_ready": completion[
            "same_species_contraction_axes_ready"
        ],
        "complete_C117_numerical_apply_paths": completion[
            "complete_C117_numerical_apply_paths"
        ],
        "complete_C396_numerical_apply_paths": completion[
            "complete_C396_numerical_apply_paths"
        ],
        "rank_status": completion["rank_status"],
        "physical_fit_authorized": completion["physical_fit_authorized"],
        "activation_gate_status": completion["activation_gate_status"],
        "next_frontier": "source-qualified J_qJ_q and J_gJ_g intermediate one-particle contraction axes",
        "merge_authorized_by_generator": False,
        "push": False,
    }
    return {**payload, "root": canonical_root(payload)}


def file_manifest(out: Path, *, exclude: tuple[str, ...] = ("generation_result.json",)) -> list[dict[str, Any]]:
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in exclude:
            continue
        rows.append(
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def generate(out: Path) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_NAMES:
        path = out / name
        if path.exists():
            path.unlink()

    hashes = source_hash_audit()
    freeze = input_freeze()
    normal = c406.normal_ordering_validation()
    descendants = c406.one_gluon_descendant_inventory()
    routing = c406.product_routing_audit()
    collapse = mixed_collapse_validation()
    zeros = mixed_zero_certificates()
    same = same_species_requirements()
    mixed = c406.mixed_kernel_validation()
    inventory = c406.c396_binding_inventory_with_c406_descendant()
    binding = c406.binding_update_summary()
    nonclaims = scientific_nonclaims()
    completion = c406.completion_record()

    records = {
        "input_freeze.json": freeze,
        "source_hash_audit.json": hashes,
        "gluon_normal_order_authority.json": normal,
        "one_gluon_descendant_inventory.json": descendants,
        "product_routing_audit.json": routing,
        "mixed_current_collapse_validation.json": collapse,
        "mixed_q_sector_zero_certificates.json": zeros,
        "same_species_contraction_requirements.json": same,
        "mixed_kernel_validation.json": mixed,
        "c396_coordinate_binding_inventory.json": inventory,
        "binding_update_summary.json": binding,
        "scientific_nonclaims.json": nonclaims,
        "blocker_or_completion.json": completion,
    }
    for name, value in records.items():
        write_json(out, name, value)

    (out / "implementation_report.md").write_text(
        implementation_report(normal, descendants, routing, collapse, mixed, binding, completion),
        encoding="utf-8",
    )

    preliminary = file_manifest(out)
    preliminary_root = canonical_root(preliminary)
    release = release_record(completion, preliminary_root)
    write_json(out, "release.json", release)

    artifacts = file_manifest(out)
    package_root = canonical_root(artifacts)
    result = {
        "schema": "C406-C117-I2-GENERATION-RESULT-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "output_directory": "docs/phases/c406_c117_i2_gluon_normal_order_descendant",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "artifact_count_excluding_generation_result": len(artifacts),
        "artifacts": artifacts,
        "package_root": package_root,
        "one_gluon_descendant_rows": descendants["row_count"],
        "product_routing_rows": routing["row_count"],
        "mixed_product_rows": routing["mixed_product_rows"],
        "same_species_rows": routing["same_species_rows"],
        "mixed_kernel_rows": mixed["row_count"],
        "normal_ordering_validation_pass": normal["pass"],
        "mixed_kernel_validation_pass": mixed["pass"],
        "complete_C117_numerical_apply_paths": completion[
            "complete_C117_numerical_apply_paths"
        ],
        "complete_C396_numerical_apply_paths": completion[
            "complete_C396_numerical_apply_paths"
        ],
        "full_C117_I2_action_ready": completion["full_C117_I2_action_ready"],
        "full_C396_forward_map_ready": completion["full_C396_forward_map_ready"],
        "rank_status": completion["rank_status"],
        "physical_fit_authorized": completion["physical_fit_authorized"],
        "activation_gate_status": completion["activation_gate_status"],
    }
    write_json(out, "generation_result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    result = generate(args.output_dir.resolve())
    print(json.dumps(jsonable(result), indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
