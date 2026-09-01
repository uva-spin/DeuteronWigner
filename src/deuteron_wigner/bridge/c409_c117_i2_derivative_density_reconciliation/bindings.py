"""C409 overlay of the accepted C408 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure.bindings import (
    c396_binding_inventory_with_c408_closure,
)

from .authority import STATUS, scientific_boundary_record
from .derivative_count import derivative_count_validation
from .jgjg import jgjg_qg_validation

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "J_gJ_g q-sector number-changing pair/vacuum descendants; route-reconciled finite-cell, "
    "field, external-state and M2 normalization for all four current products; complete target "
    "count-once aggregation; g_s^2 and c_C117_1"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c409_reconciliation() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c408_closure())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C409_role": (
                    "C117_I2_JGJG_DERIVATIVE_COUNT_RECONCILIATION_AND_"
                    "NUMBER_PRESERVING_QG_PRODUCT_BLOCK_PRIMITIVE_READY"
                ),
                "J_gJ_g_qg_status": (
                    "SOURCE_ROUTED_NUMBER_PRESERVING_DERIVATIVE_DENSITY_"
                    "PRODUCT_BLOCK_PRIMITIVE_READY"
                ),
                "J_gJ_g_qg_path": (
                    "deuteron_wigner.bridge."
                    "c409_c117_i2_derivative_density_reconciliation.jgjg.jgjg_qg_csr"
                ),
                "J_gJ_g_derivative_count_status": (
                    "EXACTLY_TWO_SOURCE_DERIVATIVES_COUNTED_ONCE_IN_C406_C407_DESCENDANT"
                ),
                "J_gJ_g_extra_C119_derivative_leaf_used": False,
                "J_gJ_g_extra_C124_derivative_density_weight_used": False,
                "J_gJ_g_color_C_A_counted_once": True,
                "J_gJ_g_q_sector_status": (
                    "NUMBER_PRESERVING_BRANCH_NOT_APPLICABLE_PAIR_AND_VACUUM_"
                    "BRANCHES_UNRESOLVED_NOT_ZERO"
                ),
                "complete_current_prefactor_status": "UNAVAILABLE_NOT_ZERO",
                "numerical_apply_status": (
                    "FULL_C396_C117_APPLY_UNAVAILABLE_C409_PRODUCT_BLOCK_PRIMITIVES_ONLY"
                ),
                "numerical_apply_path": None,
                "smallest_missing_object": _MISSING,
                "complete_C117_action": False,
                "selected": False,
                "zeroed": False,
                "physical": False,
            }
        )
        updated += 1
    payload = {
        "schema": "C409-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C409_C117_I2_reconciliation_rows": updated,
        "complete_numerical_apply_paths": previous["complete_numerical_apply_paths"],
        "expected_complete_numerical_apply_paths": 6,
        "complete_C117_numerical_apply_paths": 0,
        "source_routed_product_block_primitive_paths": 12,
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c409_reconciliation()
    derivative = derivative_count_validation()
    jgjg = jgjg_qg_validation()
    boundary = scientific_boundary_record()
    payload = {
        "schema": "C409-C396-C117-I2-DERIVATIVE-DENSITY-RECONCILIATION-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory[
            "complete_numerical_apply_paths"
        ],
        "complete_apply_count_changed": False,
        "C117_I2_reconciliation_rows": inventory[
            "C409_C117_I2_reconciliation_rows"
        ],
        "derivative_count_rows": derivative["row_count"],
        "derivative_count_validation_pass": derivative["pass"],
        "source_routed_J_qJ_q_direct_sum_paths": 3,
        "source_routed_mixed_direct_sum_paths": 6,
        "source_routed_J_gJ_g_qg_paths": 3,
        "source_routed_product_block_primitive_paths": 12,
        "J_gJ_g_qg_validation_pass": jgjg["pass"],
        "J_gJ_g_q_sector_ready": False,
        "complete_C117_numerical_apply_paths": 0,
        "smallest_missing_object_for_complete_C117_I2_action": _MISSING,
        "scientific_boundary_root": boundary["root"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "c396_binding_inventory_with_c409_reconciliation",
    "binding_update_summary",
]
