"""C405 overlay of the accepted C404 C396 binding inventory."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.bindings import (
    c396_binding_inventory_with_c404_primitives,
)

from .conditioned import conditional_kernel_validation
from .derivative_order import ordered_derivative_inventory
from .embedding import direct_sum_embedding_validation
from .normalization import normalization_closure_audit
from .topology import STATUS, topology_authority_audit

_COORDINATE_ID = "c_C117_1"
_MISSING = (
    "source-qualified product/sector normal-ordering descendant assigning both current matrix elements, "
    "the external BRA/KET image of each C192 source-ordered gluon derivative field, source phase and contraction sign, exact finite-cell/"
    "field/state normalization ownership, a C405 conditional-kernel-to-C125 witness/target aggregation map, "
    "target count-once multiplicity, and the q-sector diagonal block"
)


@lru_cache(maxsize=1)
def c396_binding_inventory_with_c405_boundary() -> Mapping[str, Any]:
    previous = deepcopy(c396_binding_inventory_with_c404_primitives())
    rows = [deepcopy(row) for row in previous["rows"]]
    updated = 0
    for row in rows:
        if row["coordinate_id"] != _COORDINATE_ID:
            continue
        row.update(
            {
                "C405_role": "C117_I2_CURRENT_ORDER_FAMILY_AND_DIRECT_SUM_EMBEDDING_BOUNDARY_READY",
                "current_pair_grammar_status": "TWO_CURRENT_IDENTITIES_EXPLICIT_FOR_ALL_PRODUCTS",
                "current_pair_grammar_path": (
                    "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding."
                    "topology.current_pair_grammar"
                ),
                "topology_authority_status": "HISTORICAL_CONFLICTS_AUDITED_SOURCE_DESCENDANT_REQUIRED",
                "topology_authority_path": (
                    "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding."
                    "topology.topology_authority_audit"
                ),
                "ordered_derivative_family_status": "BRA_KET_CANDIDATE_FAMILY_READY_NO_DEFAULT",
                "ordered_derivative_family_path": (
                    "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding."
                    "derivative_order.ordered_partition_kernel_csr"
                ),
                "conditional_qg_kernel_status": (
                    "CALLER_CONDITIONED_CURRENT_ORDER_STRESS_TEST_NOT_OPERATOR_BINDING"
                ),
                "conditional_qg_kernel_path": (
                    "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding."
                    "conditioned.conditional_qg_kernel_csr"
                ),
                "direct_sum_embedding_status": (
                    "EXACT_CROSS_SECTOR_ZERO_AND_EXPLICIT_TWO_DIAGONAL_BLOCK_ASSEMBLER_READY"
                ),
                "direct_sum_embedding_path": (
                    "deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding."
                    "embedding.assemble_explicit_direct_sum_csr"
                ),
                "qg_partial_block_available": True,
                "q_sector_diagonal_block_status": "UNAVAILABLE_NOT_ZERO",
                "complete_current_prefactor_status": "UNAVAILABLE_NOT_ZERO",
                "source_qualified_product_topology_bound": False,
                "numerical_apply_status": "FULL_C396_C117_APPLY_UNAVAILABLE_C405_BOUNDARY_ONLY",
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
        "schema": "C405-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": rows,
        "C405_C117_I2_boundary_rows": updated,
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
    inventory = c396_binding_inventory_with_c405_boundary()
    topology = topology_authority_audit()
    derivative = ordered_derivative_inventory()
    conditional = conditional_kernel_validation()
    embedding = direct_sum_embedding_validation()
    normalization = normalization_closure_audit()
    payload = {
        "schema": "C405-C396-C117-I2-CURRENT-BOUNDARY-SUMMARY-V1",
        "status": STATUS,
        "previous_complete_numerical_apply_paths": 6,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "complete_apply_count_changed": False,
        "C117_I2_boundary_rows": inventory["C405_C117_I2_boundary_rows"],
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
        "ordered_derivative_candidate_rows": derivative["row_count"],
        "conditional_qg_kernel_rows": conditional["row_count"],
        "conditional_qg_validation_pass": conditional["pass"],
        "direct_sum_embedding_validation_pass": embedding["pass"],
        "complete_numeric_prefactors": normalization["complete_numeric_prefactors"],
        "source_qualified_product_topology_rows": topology[
            "source_qualified_product_topology_rows"
        ],
        "smallest_missing_object_for_complete_C117_I2_action": _MISSING,
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = ["c396_binding_inventory_with_c405_boundary", "binding_update_summary"]
