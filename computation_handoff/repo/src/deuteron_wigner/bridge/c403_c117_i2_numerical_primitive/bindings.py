"""C403 overlay of the C401 C396 coordinate-binding inventory.

C403 advances ``c_C117_1`` only to a finite-axis and spatial-kernel primitive.
The complete C396 coordinate action remains unavailable because C114 inverse/
source factors, C119 current factors, spin/color/normalization, and target-state
aggregation have not been numerically contracted.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c401_c396_mass_directions.bindings import (
    c396_binding_inventory_with_c401_mass_directions,
)

from .axis import STATUS, axis_summary, support_theorem_certificate
from .spatial import EXTERNAL_BASIS_SCOPE, spatial_kernel_inventory, spatial_kernel_validation

_COORDINATE_ID = "c_C117_1"
_OPERATOR_ID = "C117-DELTA-H-1"
_SMALLEST_MISSING_OBJECT = (
    "source-faithful K-local contraction of the C114 inverse/source factor, C119 current factors, "
    "spin/color/normalization factors, and target q/qg aggregation with the C403 finite axis and spatial kernel"
)


def c396_binding_inventory_with_c403_i2_primitive() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c401_mass_directions())
    rows = [deepcopy(row) for row in previous["rows"]]
    primitive_rows = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C403_role": "C117_I2_FINITE_AXIS_AND_SPATIAL_KERNEL_PRIMITIVE_READY",
                "finite_member_axis_status": "NUMERICAL_FINITE_AXIS_READY_WITH_EXACT_C62_SUPPORT_THEOREM",
                "finite_member_axis_path": (
                    "deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.axis.member_by_rank"
                ),
                "spatial_kernel_status": "K_LOCAL_ANALYTIC_SPARSE_AND_MATRIX_FREE_PRIMITIVE_READY",
                "spatial_kernel_path": (
                    "deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial.single_member_kernel_csr"
                ),
                "spatial_matrix_free_path": (
                    "deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial.apply_single_member_kernel"
                ),
                "spatial_external_basis_scope": EXTERNAL_BASIS_SCOPE,
                "q_sector_external_basis_assembled": False,
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_PRIMITIVE_ONLY",
                "numerical_apply_path": None,
                "derivative_status": "C274_SYMBOLIC_INSERTION_PLUS_C403_NUMERICAL_SPATIAL_PRIMITIVE",
                "smallest_missing_object": _SMALLEST_MISSING_OBJECT,
                "C64_runtime_required_for_finite_axis": False,
                "C80_reuse": False,
                "selected": False,
                "zeroed": False,
                "physical": False,
            }
        )
        primitive_rows += 1
    payload = {
        "schema": "C403-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": tuple(rows),
        "C403_I2_primitive_binding_rows": primitive_rows,
        "finite_member_axis_paths": axis_summary()["finite_axis_paths"],
        "spatial_kernel_paths": spatial_kernel_inventory()["spatial_kernel_paths"],
        "complete_numerical_apply_paths": previous["complete_numerical_apply_paths"],
        "expected_complete_numerical_apply_paths": 6,
        "complete_C117_numerical_apply_paths": 0,
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return {**payload, "root": content_root(payload)}


def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c403_i2_primitive()
    support = support_theorem_certificate()
    spatial = spatial_kernel_validation()
    payload = {
        "schema": "C403-C396-C117-I2-PRIMITIVE-BINDING-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_primitive_rows": inventory["C403_I2_primitive_binding_rows"],
        "finite_member_axis_paths": inventory["finite_member_axis_paths"],
        "spatial_kernel_paths": inventory["spatial_kernel_paths"],
        "support_theorem_pass": support["all_exact_matches"],
        "spatial_validation_pass": spatial["pass"],
        "first_numerical_C117_substructure": (
            "finite member identities and one-member transverse I2 kernels at K9/K11/K13"
        ),
        "smallest_missing_object_for_complete_C117_I2_action": _SMALLEST_MISSING_OBJECT,
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "c396_binding_inventory_with_c403_i2_primitive",
    "binding_update_summary",
]
