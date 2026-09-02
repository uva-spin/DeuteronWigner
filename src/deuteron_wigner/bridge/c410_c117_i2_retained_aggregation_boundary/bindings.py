"""C410 overlay of the C409 C396 coordinate-binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c409_c117_i2_derivative_density_reconciliation.bindings import (
    c396_binding_inventory_with_c409_reconciliation,
)

from .aggregate import retained_aggregation_validation
from .authority import STATUS, scientific_boundary_record
from .normalization import MISSING_NORMALIZATION_OBJECT, normalization_boundary_record
from .vacuum import q_sector_vacuum_projection_validation

_COORDINATE_ID = "c_C117_1"


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c410_aggregation() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c409_reconciliation())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C410_role": (
                    "C117_I2_RETAINED_CONNECTED_CURRENT_SQUARE_AGGREGATION_"
                    "AND_Q_SECTOR_VACUUM_ROUTING_READY"
                ),
                "J_gJ_g_q_sector_status": (
                    "SOURCE_NONZERO_DISCONNECTED_VACUUM_CNUMBER_ROUTED_TO_"
                    "NONMATRIX_VACUUM_OWNER_RETAINED_CONNECTED_BLOCK_EXACT_ZERO"
                ),
                "retained_connected_aggregate_status": (
                    "SOURCE_COEFFICIENT_NORMALIZED_SHAPE_PRIMITIVE_READY"
                ),
                "retained_connected_aggregate_path": (
                    "deuteron_wigner.bridge."
                    "c410_c117_i2_retained_aggregation_boundary.aggregate."
                    "source_reduced_c117_i2_shape_csr"
                ),
                "source_routed_product_block_primitive_paths": 12,
                "retained_connected_aggregate_shape_paths": 3,
                "source_product_count_once_aggregation_status": "CLOSED_FOR_RETAINED_SHAPE",
                "complete_target_aggregation_status": "C260_C262_ADAPTER_UNAVAILABLE_NOT_ZERO",
                "g_s_squared_required_for_derivative_shape": False,
                "c_C117_1_value_required_for_derivative_shape": False,
                "C260_operator_normalization_status": "UNAVAILABLE_NOT_ZERO",
                "complete_current_prefactor_status": "C260_ADAPTER_UNAVAILABLE_NOT_ZERO",
                "numerical_apply_status": (
                    "FULL_C396_C117_APPLY_UNAVAILABLE_C410_RETAINED_AGGREGATE_SHAPE_ONLY"
                ),
                "numerical_apply_path": None,
                "smallest_missing_object": MISSING_NORMALIZATION_OBJECT,
                "complete_C117_action": False,
                "selected": False,
                "zeroed": False,
                "physical": False,
            }
        )
        updated += 1
    payload = {
        "schema": "C410-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C410_C117_I2_aggregation_rows": updated,
        "complete_numerical_apply_paths": previous["complete_numerical_apply_paths"],
        "expected_complete_numerical_apply_paths": 6,
        "complete_C117_numerical_apply_paths": 0,
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c410_aggregation()
    aggregate = retained_aggregation_validation()
    vacuum = q_sector_vacuum_projection_validation()
    normalization = normalization_boundary_record()
    boundary = scientific_boundary_record()
    payload = {
        "schema": "C410-C396-C117-I2-RETAINED-AGGREGATION-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory[
            "complete_numerical_apply_paths"
        ],
        "complete_apply_count_changed": False,
        "C117_I2_aggregation_rows": inventory["C410_C117_I2_aggregation_rows"],
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
        "retained_aggregation_validation_pass": aggregate["pass"],
        "q_sector_vacuum_projection_validation_pass": vacuum["pass"],
        "source_product_count_once_aggregation_closed": True,
        "complete_target_aggregation_closed": False,
        "g_s_squared_required_for_derivative_shape": False,
        "c_C117_1_value_required_for_derivative_shape": False,
        "C260_operator_normalization_closed": False,
        "complete_C117_numerical_apply_paths": 0,
        "smallest_missing_object_for_complete_C117_I2_action": (
            MISSING_NORMALIZATION_OBJECT
        ),
        "normalization_boundary_root": normalization["root"],
        "scientific_boundary_root": boundary["root"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return dict(payload, root=content_root(payload))


__all__ = [
    "c396_binding_inventory_with_c410_aggregation",
    "binding_update_summary",
]
