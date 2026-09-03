"""C408 overlay of the accepted C407 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.bindings import (
    c396_binding_inventory_with_c407_descendants,
)

from .authority import STATUS, derivative_density_conflict_record, scientific_boundary_record
from .i4_q import q_sector_i4_validation
from .jqjq import jqjq_product_block_validation
from .weights import i2_source_weight_validation

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "J_gJ_g derivative-density product-level derivative-count and normalization descendant; "
    "J_gJ_g q-sector number-changing branches; route-reconciled finite-cell/field/state/M2 normalization; "
    "complete C125 target aggregation/count-once multiplicity; g_s^2 and c_C117_1"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c408_closure() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c407_descendants())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C408_role": "C117_I2_MEMBER_WEIGHT_ROUTING_AND_JQJQ_TRANSVERSE_CLOSURE_READY",
                "J_qJ_q_q_sector_status": "SOURCE_ROUTED_I4_LOCAL_PRODUCT_BLOCK_PRIMITIVE_READY",
                "J_qJ_q_q_sector_path": (
                    "deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure."
                    "i4_q.q_sector_jqjq_csr"
                ),
                "J_qJ_q_qg_status": "C124_C126_UNIT_MEMBER_WEIGHT_SOURCE_ROUTED_PRIMITIVE_READY",
                "J_qJ_q_qg_path": (
                    "deuteron_wigner.bridge.c408_c117_i2_weight_routing_closure."
                    "weights.source_weighted_jqjq_qg_csr"
                ),
                "J_qJ_g_qg_status": "C124_C126_UNIT_MEMBER_WEIGHT_SOURCE_ROUTED_PRIMITIVE_READY",
                "J_gJ_q_qg_status": "C124_C126_UNIT_MEMBER_WEIGHT_SOURCE_ROUTED_PRIMITIVE_READY",
                "J_gJ_g_qg_status": "LONGITUDINAL_DESCENDANT_READY_DERIVATIVE_COUNT_CONFLICT_UNRESOLVED",
                "complete_current_prefactor_status": "UNAVAILABLE_NOT_ZERO",
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_C408_PRODUCT_BLOCK_PRIMITIVES_ONLY",
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
        "schema": "C408-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C408_C117_I2_closure_rows": updated,
        "complete_numerical_apply_paths": previous["complete_numerical_apply_paths"],
        "expected_complete_numerical_apply_paths": 6,
        "complete_C117_numerical_apply_paths": 0,
        "source_routed_product_block_primitive_paths": 9,
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return dict(payload, root=content_root(payload))


@lru_cache(maxsize=1)
def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c408_closure()
    weights = i2_source_weight_validation()
    q_sector = q_sector_i4_validation()
    jqjq = jqjq_product_block_validation()
    derivative = derivative_density_conflict_record()
    boundary = scientific_boundary_record()
    payload = {
        "schema": "C408-C396-C117-I2-WEIGHT-ROUTING-CLOSURE-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_closure_rows": inventory["C408_C117_I2_closure_rows"],
        "source_descendant_I2_weight_sets": 3,
        "source_routed_J_qJ_q_direct_sum_paths": 3,
        "source_routed_mixed_direct_sum_paths": 6,
        "source_routed_product_block_primitive_paths": 9,
        "J_qJ_q_q_sector_I4_validation_pass": q_sector["pass"],
        "I2_source_weight_validation_pass": weights["pass"],
        "J_qJ_q_product_block_validation_pass": jqjq["pass"],
        "J_gJ_g_derivative_density_ready": False,
        "J_gJ_g_derivative_conflict_root": derivative["root"],
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


__all__ = ["c396_binding_inventory_with_c408_closure", "binding_update_summary"]
