"""C406 overlay of the accepted C405 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.bindings import (
    c396_binding_inventory_with_c405_boundary,
)

from .mixed_kernel import mixed_kernel_validation
from .normal_order import STATUS, normal_ordering_validation, one_gluon_descendant_inventory
from .routing import product_routing_audit

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "source-qualified J_qJ_q and J_gJ_g one-particle contraction descendants with explicit intermediate "
    "mode/current-transfer axes; route-reconciled field/state and finite-cell normalization; C406-to-C125 "
    "witness/target aggregation and count-once multiplicity; complete product prefactors; g_s^2 and c_C117_1"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c406_descendant() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c405_boundary())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C406_role": "C117_I2_ONE_GLUON_NORMAL_ORDER_DESCENDANT_AND_MIXED_ROUTING_READY",
                "one_gluon_descendant_status": "SOURCE_DERIVED_NUMERICAL_PRIMITIVE_READY",
                "one_gluon_descendant_path": (
                    "deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant."
                    "normal_order.dimensionless_descendant_factor_exact"
                ),
                "mixed_product_routing_status": "JQJG_AND_JGJQ_SOURCE_DERIVED_NUMERICAL_PRIMITIVES_READY",
                "mixed_product_qg_path": (
                    "deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant."
                    "mixed_kernel.mixed_qg_kernel_csr"
                ),
                "mixed_product_q_sector_status": "EXACT_ZERO_WITH_NORMAL_ORDERING_COLOR_TRACE_PROOF",
                "same_species_product_status": "JQJQ_AND_JGJG_INTERMEDIATE_CONTRACTION_AXES_UNAVAILABLE_NOT_ZERO",
                "C405_BRA_KET_ambiguity_status": "CLOSED_FOR_MIXED_PRODUCTS_ONLY",
                "complete_current_prefactor_status": "UNAVAILABLE_NOT_ZERO",
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_C406_PRIMITIVES_ONLY",
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
        "schema": "C406-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C406_C117_I2_descendant_rows": updated,
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
    inventory = c396_binding_inventory_with_c406_descendant()
    normal = normal_ordering_validation()
    descendants = one_gluon_descendant_inventory()
    routing = product_routing_audit()
    mixed = mixed_kernel_validation()
    payload = {
        "schema": "C406-C396-C117-I2-NORMAL-ORDER-DESCENDANT-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_descendant_rows": inventory["C406_C117_I2_descendant_rows"],
        "one_gluon_descendant_inventory_rows": descendants["row_count"],
        "normal_ordering_validation_pass": normal["pass"],
        "product_routing_rows": routing["row_count"],
        "mixed_product_rows_ready": routing["mixed_product_rows"],
        "same_species_rows_unresolved": routing["same_species_rows"],
        "mixed_kernel_rows": mixed["row_count"],
        "mixed_kernel_validation_pass": mixed["pass"],
        "smallest_missing_object_for_complete_C117_I2_action": _MISSING,
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "c396_binding_inventory_with_c406_descendant",
    "binding_update_summary",
]
