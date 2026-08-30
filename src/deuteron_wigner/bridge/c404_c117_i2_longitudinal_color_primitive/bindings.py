"""C404 overlay of the accepted C403 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.bindings import (
    c396_binding_inventory_with_c403_i2_primitive,
)

from .color_spin import color_spin_validation
from .factorized import skeleton_validation
from .longitudinal import STATUS, longitudinal_inventory

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "numerical C119 finite-cell normalization and ordered gluon-current derivative/source-phase factors, "
    "C114-to-M2 scale cancellation, exact C124/C125 target aggregation including q-sector contractions, "
    "complete Hermitian reverse, and unselected g_s^2/c_C117_1 coefficients"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c404_primitives() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c403_i2_primitive())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C404_role": "C117_I2_QG_LONGITUDINAL_SPIN_COLOR_SKELETON_READY",
                "longitudinal_Q0_status": "EXACT_K_LOCAL_NONZERO_TRANSFER_PRIMITIVE_READY",
                "longitudinal_Q0_path": (
                    "deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive."
                    "longitudinal.partition_transfer_matrix_csr"
                ),
                "triplet_color_status": "EXACT_C45_C47_CHARGE_GENERATOR_PRODUCTS_READY",
                "triplet_color_path": (
                    "deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive."
                    "color_spin.triplet_color_product_matrix"
                ),
                "spin_selection_status": "JPLUS_DIAGONAL_SELECTION_PRIMITIVE_READY",
                "qg_skeleton_status": "ALGEBRAIC_FACTORIZATION_STRESS_TEST_NOT_OPERATOR_BINDING",
                "qg_skeleton_path": (
                    "deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive."
                    "factorized.qg_skeleton_csr"
                ),
                "source_qualified_product_topology_bound": False,
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_PRIMITIVES_ONLY",
                "numerical_apply_path": None,
                "smallest_missing_object": _MISSING,
                "q_sector_external_basis_assembled": False,
                "C119_full_current_factor_bound": False,
                "complete_C117_action": False,
                "selected": False,
                "zeroed": False,
                "physical": False,
            }
        )
        updated += 1
    payload = {
        "schema": "C404-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C404_C117_I2_primitive_binding_rows": updated,
        "complete_numerical_apply_paths": previous["complete_numerical_apply_paths"],
        "expected_complete_numerical_apply_paths": 6,
        "complete_C117_numerical_apply_paths": 0,
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c404_primitives()
    longitudinal = longitudinal_inventory()
    color = color_spin_validation()
    skeleton = skeleton_validation()
    payload = {
        "schema": "C404-C396-C117-I2-PRIMITIVE-BINDING-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_primitive_rows": inventory["C404_C117_I2_primitive_binding_rows"],
        "longitudinal_validation_pass": all(row["symmetry_residual"] == 0 for row in longitudinal["rows"]),
        "color_spin_validation_pass": color["pass"],
        "skeleton_validation_pass": skeleton["pass"],
        "skeleton_is_operator_binding": False,
        "smallest_missing_object_for_complete_C117_I2_action": _MISSING,
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = ["c396_binding_inventory_with_c404_primitives", "binding_update_summary"]
