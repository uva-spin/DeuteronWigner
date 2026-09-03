#!/usr/bin/env python3
"""Generate C405 current-topology and embedding-boundary evidence."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import platform
from typing import Any, Mapping

import numpy as np
import scipy

from deuteron_wigner.bridge import c405_c117_i2_current_topology_embedding as c405

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/phases/c405_c117_i2_current_topology_embedding"
BASELINE = "6e7601881256d17fe14767d203cb4742143051c2"
STATUS = c405.STATUS
GENERATED_NAMES = (
    "input_freeze.json",
    "source_hash_audit.json",
    "gluon_source_slot_authority.json",
    "topology_authority_audit.json",
    "current_pair_grammar.json",
    "ordered_derivative_inventory.json",
    "normalization_closure_audit.json",
    "conditional_kernel_validation.json",
    "direct_sum_embedding_validation.json",
    "cross_sector_zero_certificates.json",
    "c396_coordinate_binding_inventory.json",
    "binding_update_summary.json",
    "scientific_nonclaims.json",
    "blocker_or_completion.json",
    "release.json",
    "implementation_report.md",
    "generation_result.json",
)
STALE_GENERATED_NAMES = (
    "source_file_hashes.json",
    "conditional_qg_kernel_validation.json",
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
        "src/deuteron_wigner/bridge/icurrent/core.py",
        "src/deuteron_wigner/bridge/icho/core.py",
        "src/deuteron_wigner/bridge/icreg2/core.py",
        "src/deuteron_wigner/bridge/icnorm3/core.py",
        "src/deuteron_wigner/bridge/icmembers/core.py",
        "src/deuteron_wigner/bridge/icdomain2/core.py",
        "src/deuteron_wigner/bridge/icsum3/core.py",
        "src/deuteron_wigner/bridge/icagg3/core.py",
        "src/deuteron_wigner/bridge/hqcdb1qggsource2/core.py",
        "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py",
        "src/deuteron_wigner/bridge/hqcdb1qggcontact2/core.py",
        "src/deuteron_wigner/bridge/hqcdriquarkfixedkv2currentmap1/core.py",
        "src/deuteron_wigner/bridge/hqcdriquarkfixedkv2currenteval1/core.py",
        "src/deuteron_wigner/bridge/c401_c396_mass_directions/basis.py",
        "src/deuteron_wigner/bridge/c403_c117_i2_numerical_primitive/spatial.py",
        "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/longitudinal.py",
        "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/color_spin.py",
        "src/deuteron_wigner/bridge/c404_c117_i2_longitudinal_color_primitive/bindings.py",
        "docs/phases/c404_c117_i2_longitudinal_color_primitive/release.json",
    )
    rows = []
    for rel in paths:
        path = ROOT / rel
        rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    payload = {
        "schema": "C405-C117-I2-CURRENT-TOPOLOGY-EMBEDDING-INPUT-FREEZE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_files": tuple(rows),
        "historical_files_modified": False,
        "C144_proxy_used": False,
        "C117_coefficient_selected": False,
        "normal_ordering_descendant_invented": False,
        "q_sector_diagonal_block_zero_filled": False,
    }
    return {**payload, "root": canonical_root(payload)}


def scientific_nonclaims() -> dict[str, Any]:
    payload = {
        "schema": "C405-C117-I2-CURRENT-TOPOLOGY-EMBEDDING-NONCLAIMS-V1",
        "status": STATUS,
        "does_not_establish": (
            "a source-qualified product/sector normal-ordering descendant",
            "a unique external BRA/KET assignment for the source-ordered gluon c field",
            "a complete numerical finite-cell/current prefactor",
            "a numerical q-sector diagonal current-current block",
            "a C405 conditional-kernel to C125 witness/target aggregation map",
            "a complete numerical C117 I2 coordinate action",
            "a numerical or physical value for c_C117_1 or g_s",
            "a physical deuteron state or production current",
            "physical response rank or identifiability",
            "a physical fit or Hamiltonian activation",
        ),
        "forbidden_substitutions": (
            "C144 diagnostic proxy",
            "zero q-sector block for an unavailable diagonal action",
            "minimum-norm or zero C117 representative",
            "a default gluon-derivative leg",
            "post-hoc averaging in place of source-order adjoint reversal",
            "historical C119/C126 single-current leaf program as a complete current pair",
            "historical C126 zero-scale assertion as a numerical normalization proof",
        ),
    }
    return {**payload, "root": canonical_root(payload)}


def implementation_report(
    topology: Mapping[str, Any],
    derivative: Mapping[str, Any],
    normalization: Mapping[str, Any],
    conditional: Mapping[str, Any],
    embedding: Mapping[str, Any],
    bindings: Mapping[str, Any],
) -> str:
    scale_rows = {
        row["product"]: row["literal_scale_ledger"]["known_post_exponents"]
        for row in normalization["rows"]
    }
    lines = [
        "# C405 C117 I2 current topology, derivative family, and embedding boundary",
        "",
        f"Status: `{STATUS}`",
        f"Accepted local baseline: `{BASELINE}`",
        "",
        "## Scientific advance",
        "",
        "C405 reconciles the source-owned instantaneous-current records before any complete C117 matrix is assembled. "
        "It authenticates the four ordered current products, exposes three historical graph-class conflicts, shows "
        "that all eight historical C119 program rows contain only one of the two required current identities, and "
        "records four program rows in which derivative ownership can overlap between C119 and C126.",
        "",
        "The later C190/C192 source chain closes an important part of that ambiguity: C192 derives "
        "`- f_abc A_perp^b partial_- A_perp^c` from the authenticated Gauss equation, fixes the derivative "
        "on the second ordered source field, and retains `J_q K J_g` and `J_g K J_q` separately without a "
        "factor-two merge. It remains symbolic and does not map that second source field to an external qg BRA "
        "or KET gluon after product-specific normal ordering.",
        "",
        "C250 supplies the corrected two-current identity grammar, but neither C192, C250, nor any earlier record "
        "supplies the product-specific normal-ordering descendant that maps the source-ordered gluon derivative "
        "field to an external BRA or KET leg.",
        "",
        "## Source reconciliation",
        "",
        f"- hash-verified source files: {len(topology['source_hash_audit']['rows'])}",
        f"- ordered products: {topology['product_count']}",
        f"- product/sector programs: {topology['program_count']}",
        f"- C115/C125 graph-class conflicts: {topology['graph_mapping_conflicts']}",
        f"- incomplete C119 current-pair programs: {topology['C119_incomplete_current_pair_programs']}",
        f"- derivative-overlap-risk programs: {topology['C119_or_C126_derivative_overlap_programs']}",
        f"- C126 program-level single-current references: {topology['C126_program_level_single_current_reference_defects']}",
        f"- C126 program rows with an extra derivative reference: {topology['C126_programs_with_extra_derivative_reference']}",
        "- C192 derivative source field: second ordered gluon field, source-qualified",
        "- C192 external BRA/KET derivative leg: unresolved after normal ordering",
        "- C192/C193 mixed current owners: retained separately; no factor-two merge",
        "- C250 two-current identity repair: retained as grammar, not normal-ordering authority",
        "- C125 one-member/one-target identity: source bound",
        "- C405 conditional-kernel to C125 witness map: unbound",
        "",
        "## Ordered derivative family",
        "",
        "C192 fixes the derivative on the second source-ordered gluon field. Because the normal-ordering descendant "
        "that identifies this field with an external qg leg is absent, C405 retains the complete explicit candidate "
        "set in which that fixed source field is assigned to BRA or KET. No default assignment is selected. Under Hermitian conjugation, "
        "the current order reverses, the derivative-order tuple reverses, and BRA/KET labels flip.",
        "",
        f"The resulting inventory contains {derivative['row_count']} rows: nine assignments per resolution across "
        "K9, K11, and K13. Its maximum exact adjoint residual is "
        f"`{derivative['maximum_adjoint_residual']:.3e}`.",
        "",
        "## Literal normalization ledger",
        "",
        "The exact C114/C119 expressions imply product-dependent residual powers before the unresolved normal-ordering "
        "and field/state factors are supplied:",
        "",
        "| product | L exponent | pi exponent | K exponent |",
        "|---|---:|---:|---:|",
    ]
    for product in c405.PRODUCTS:
        exponents = scale_rows[product]
        lines.append(
            f"| `{product}` | {exponents['L']} | {exponents['pi']} | {exponents['K']} |"
        )
    lines.extend(
        [
            "",
            "These product-dependent exponents demonstrate that the historical C126 zero-exponent claim is not a "
            "numerically verified normalization for the complete operator. C405 compiles the complete symbolic "
            "requirement program and refuses to evaluate a prefactor.",
            "",
            "## Conditional qg kernels",
            "",
            "For every explicit derivative assignment, C405 composes the accepted C404 nonzero-transfer kernel, "
            "C403 single-member spatial kernel, C404 spin-selection matrix, and C404 triplet-color product. The "
            "result is a caller-conditioned qg stress-test kernel, not a source-qualified operator binding.",
            "",
            f"Validation rows: {conditional['row_count']}; maximum sparse/matrix-free residual: "
            f"`{conditional['maximum_sparse_matrix_free_residual']:.3e}`; maximum adjoint residual: "
            f"`{conditional['maximum_adjoint_residual']:.3e}`.",
            "",
            "## Direct-sum embedding",
            "",
            "C114 proves the q-to-qg and qg-to-q cross-sector blocks vanish by even-gluon-number parity. C405 provides "
            "an exact block-diagonal assembler only when both surviving diagonal blocks are explicitly supplied. The "
            "q-sector diagonal block remains unavailable and is never zero-filled.",
            "",
            f"Direct-sum validation pass: `{embedding['pass']}`; maximum sparse/action residual: "
            f"`{embedding['maximum_sparse_direct_residual']:.3e}`.",
            "",
            "## C396 frontier",
            "",
            f"C405 updates {bindings['C405_C117_I2_boundary_rows']} K-local `c_C117_1` records with source-audit, "
            "ordered-derivative-family, conditional-qg-kernel, and embedding-boundary paths. The complete numerical "
            f"C396 apply count remains {bindings['complete_numerical_apply_paths']}; complete C117 actions remain zero.",
            "",
            "The smallest missing object is a source-qualified product/sector normal-ordering descendant assigning "
            "both current matrix elements, contracted member species, the external BRA/KET image of each C192 "
            "source-ordered derivative field, source phase, "
            "finite-cell/field/state normalization ownership, the C405-to-C125 witness/target map, target aggregation "
            "multiplicity, and the q-sector diagonal action.",
            "",
            "No coefficient, target, state, current prescription, rank, fit, resolution average, merge, push, or "
            "activation decision is made.",
            "",
        ]
    )
    return "\n".join(lines)


def generate(out: Path) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    for name in (*GENERATED_NAMES, *STALE_GENERATED_NAMES):
        path = out / name
        if path.exists():
            path.unlink()

    source_hashes = c405.source_file_hashes()
    source_slot = c405.gluon_source_slot_authority()
    topology = c405.topology_authority_audit()
    grammar = c405.current_pair_grammar()
    derivative = c405.ordered_derivative_inventory()
    normalization = c405.normalization_closure_audit()
    conditional = c405.conditional_kernel_validation()
    embedding = c405.direct_sum_embedding_validation()
    zero_certificates = tuple(
        c405.exact_cross_sector_zero_certificate(resolution)
        for resolution in ("K9", "K11", "K13")
    )
    inventory = c405.c396_binding_inventory_with_c405_boundary()
    binding_summary = c405.binding_update_summary()
    completion = c405.completion_record()
    nonclaims = scientific_nonclaims()
    release = {
        "schema": "C405-C117-I2-CURRENT-TOPOLOGY-EMBEDDING-RELEASE-V1",
        "status": STATUS,
        "accepted_local_baseline": BASELINE,
        "source_module": (
            "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding"
        ),
        "source_hash_audit_pass": source_hashes["all_match"],
        "C192_source_gluon_derivative_field_slot_bound": (
            source_slot["derivative_source_field_slot"] == 2
        ),
        "C192_external_BRA_KET_leg_mapping_bound": False,
        "topology_conflicts_exposed": topology["graph_mapping_conflicts"],
        "ordered_derivative_inventory_complete": derivative["row_count"] == 27,
        "conditional_qg_validation_pass": conditional["pass"],
        "direct_sum_embedding_validation_pass": embedding["pass"],
        "complete_numeric_prefactors": normalization["complete_numeric_prefactors"],
        "source_qualified_product_topology_rows": topology[
            "source_qualified_product_topology_rows"
        ],
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": inventory[
            "complete_numerical_apply_paths"
        ],
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    release["root"] = canonical_root(release)

    write_json(out, "input_freeze.json", input_freeze())
    write_json(out, "source_hash_audit.json", source_hashes)
    write_json(out, "gluon_source_slot_authority.json", source_slot)
    write_json(out, "topology_authority_audit.json", topology)
    write_json(out, "current_pair_grammar.json", grammar)
    write_json(out, "ordered_derivative_inventory.json", derivative)
    write_json(out, "normalization_closure_audit.json", normalization)
    write_json(out, "conditional_kernel_validation.json", conditional)
    write_json(out, "direct_sum_embedding_validation.json", embedding)
    write_json(
        out,
        "cross_sector_zero_certificates.json",
        {
            "schema": "C405-C117-I2-CROSS-SECTOR-ZERO-CERTIFICATES-V1",
            "status": STATUS,
            "rows": zero_certificates,
            "certificate_count": len(zero_certificates),
            "cross_sector_zero_blocks": sum(
                row["cross_sector_zero_blocks"] for row in zero_certificates
            ),
            "q_diagonal_block_inferred_zero": False,
        },
    )
    write_json(out, "c396_coordinate_binding_inventory.json", inventory)
    write_json(out, "binding_update_summary.json", binding_summary)
    write_json(out, "scientific_nonclaims.json", nonclaims)
    write_json(out, "blocker_or_completion.json", completion)
    write_json(out, "release.json", release)
    (out / "implementation_report.md").write_text(
        implementation_report(
            topology, derivative, normalization, conditional, embedding, inventory
        ).rstrip()
        + "\n",
        encoding="utf-8",
    )

    artifacts = []
    for path in sorted(out.iterdir()):
        if path.is_file() and path.name != "generation_result.json":
            artifacts.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
            )
    result = {
        "schema": "C405-C117-I2-CURRENT-TOPOLOGY-EMBEDDING-GENERATION-RESULT-V1",
        "status": STATUS,
        "output_directory": "docs/phases/c405_c117_i2_current_topology_embedding",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "artifact_count_excluding_generation_result": len(artifacts),
        "artifacts": artifacts,
        "package_root": canonical_root(artifacts),
        "source_files_hash_verified": source_hashes["all_match"],
        "C192_source_gluon_derivative_field_slot_bound": True,
        "C192_derivative_source_field_slot": source_slot["derivative_source_field_slot"],
        "C192_external_BRA_KET_leg_mapping_bound": False,
        "C192_mixed_current_orders_kept_separate": True,
        "historical_graph_mapping_conflicts": topology["graph_mapping_conflicts"],
        "historical_incomplete_C119_programs": topology[
            "C119_incomplete_current_pair_programs"
        ],
        "historical_derivative_overlap_programs": topology[
            "C119_or_C126_derivative_overlap_programs"
        ],
        "C126_program_level_single_current_reference_defects": topology[
            "C126_program_level_single_current_reference_defects"
        ],
        "C126_programs_with_extra_derivative_reference": topology[
            "C126_programs_with_extra_derivative_reference"
        ],
        "C250_two_current_reference_repairs_pair_identity": topology[
            "C250_two_current_reference_repairs_pair_identity"
        ],
        "ordered_derivative_assignment_rows": derivative["row_count"],
        "conditional_qg_kernel_rows": conditional["row_count"],
        "conditional_qg_validation_pass": conditional["pass"],
        "direct_sum_embedding_validation_pass": embedding["pass"],
        "complete_numeric_prefactors": normalization["complete_numeric_prefactors"],
        "source_qualified_product_topology_rows": topology[
            "source_qualified_product_topology_rows"
        ],
        "C405_C117_I2_boundary_rows": inventory["C405_C117_I2_boundary_rows"],
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": inventory[
            "complete_numerical_apply_paths"
        ],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": completion["smallest_missing_object"],
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
