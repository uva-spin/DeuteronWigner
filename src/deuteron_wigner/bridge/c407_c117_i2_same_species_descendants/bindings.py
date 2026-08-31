"""C407 overlay of the accepted C406 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant.bindings import (
    c396_binding_inventory_with_c406_descendant,
)

from .authority import STATUS, scientific_boundary_record
from .axis import intermediate_axis_inventory
from .descendants import descendant_inventory, longitudinal_validation
from .jqjq_qg import jqjq_qg_conditioned_validation

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "source-authorized C117 I2 graph-member weights for J_qJ_q; source-qualified J_qJ_q q-sector I4-local "
    "transverse kernel; J_gJ_g derivative-density transverse descendant with derivative-count reconciliation; "
    "J_gJ_g q-sector pair/vacuum branches; route-reconciled finite-cell/field/state/M2 normalization; "
    "C125 target count-once aggregation; g_s^2 and c_C117_1"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c407_descendants() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c406_descendant())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C407_role": "C117_I2_SAME_SPECIES_LONGITUDINAL_DESCENDANTS_AND_CALLER_CONDITIONED_JQJQ_QG_COMPOSITION_READY",
                "same_species_intermediate_axis_status": "SOURCE_DERIVED_FINITE_Q0_AXES_READY",
                "same_species_longitudinal_descendant_path": (
                    "deuteron_wigner.bridge.c407_c117_i2_same_species_descendants."
                    "descendants.longitudinal_diagonal_csr"
                ),
                "J_qJ_q_qg_status": "CALLER_CONDITIONED_NUMERICAL_COMPOSITION_READY_GRAPH_WEIGHTS_UNBOUND",
                "J_qJ_q_qg_path": (
                    "deuteron_wigner.bridge.c407_c117_i2_same_species_descendants."
                    "jqjq_qg.jqjq_qg_conditioned_csr"
                ),
                "J_qJ_q_q_sector_status": "I4_LOCAL_TRANSVERSE_KERNEL_UNAVAILABLE_NOT_ZERO",
                "J_gJ_g_qg_status": "LONGITUDINAL_DESCENDANT_READY_DERIVATIVE_DENSITY_TRANSVERSE_ACTION_UNAVAILABLE",
                "J_gJ_g_q_sector_status": "NUMBER_PRESERVING_BRANCH_NOT_APPLICABLE_PAIR_AND_VACUUM_BRANCHES_UNRESOLVED_NOT_ZERO",
                "complete_current_prefactor_status": "UNAVAILABLE_NOT_ZERO",
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_C407_PRIMITIVES_ONLY",
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
        "schema": "C407-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C407_C117_I2_descendant_rows": updated,
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
    inventory = c396_binding_inventory_with_c407_descendants()
    axes = intermediate_axis_inventory()
    descendants = descendant_inventory()
    longitudinal = longitudinal_validation()
    jqjq = jqjq_qg_conditioned_validation()
    boundary = scientific_boundary_record()
    payload = {
        "schema": "C407-C396-C117-I2-SAME-SPECIES-DESCENDANT-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_descendant_rows": inventory["C407_C117_I2_descendant_rows"],
        "intermediate_axis_rows": axes["row_count"],
        "same_species_weight_rows": descendants["row_count"],
        "longitudinal_validation_pass": longitudinal["pass"],
        "J_qJ_q_qg_conditioned_validation_pass": jqjq["pass"],
        "J_qJ_q_qg_conditioned_composition_rows": jqjq["row_count"],
        "source_authorized_graph_member_weight_sets": 0,
        "J_gJ_g_longitudinal_primitive_paths": 3,
        "complete_C117_numerical_apply_paths": 0,
        "smallest_missing_object_for_complete_C117_I2_action": _MISSING,
        "scientific_boundary_root": boundary["root"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "c396_binding_inventory_with_c407_descendants",
    "binding_update_summary",
]
