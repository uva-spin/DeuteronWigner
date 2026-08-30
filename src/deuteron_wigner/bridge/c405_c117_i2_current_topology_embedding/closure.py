"""C405 aggregate completion and fail-closed API."""
from __future__ import annotations

from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .bindings import binding_update_summary
from .conditioned import conditional_kernel_validation
from .derivative_order import ordered_derivative_inventory
from .embedding import direct_sum_embedding_validation
from .normalization import normalization_closure_audit
from .topology import STATUS, topology_authority_audit


def completion_record() -> Mapping[str, Any]:
    topology = topology_authority_audit()
    derivative = ordered_derivative_inventory()
    conditioned = conditional_kernel_validation()
    embedding = direct_sum_embedding_validation()
    normalization = normalization_closure_audit()
    bindings = binding_update_summary()
    payload = {
        "schema": "C405-C117-I2-CURRENT-TOPOLOGY-EMBEDDING-COMPLETION-V1",
        "status": STATUS,
        "phase_result": "PHASE_COMPLETE_AT_CONDITIONAL_PRIMITIVE_AND_SOURCE_AUDIT_SCOPE",
        "source_files_hash_verified": topology["source_hash_audit"]["all_match"],
        "current_product_rows": topology["product_count"],
        "historical_graph_mapping_conflicts": topology["graph_mapping_conflicts"],
        "historical_single_current_reference_defects": topology["single_current_reference_defects"],
        "historical_incomplete_C119_programs": topology["C119_incomplete_current_pair_programs"],
        "historical_derivative_overlap_programs": topology["C119_or_C126_derivative_overlap_programs"],
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
        "conditional_qg_kernel_rows": conditioned["row_count"],
        "conditional_qg_kernel_validation_pass": conditioned["pass"],
        "direct_sum_embedding_validation_pass": embedding["pass"],
        "complete_numeric_prefactors": normalization["complete_numeric_prefactors"],
        "source_qualified_product_topology_rows": topology["source_qualified_product_topology_rows"],
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": bindings["current_complete_numerical_apply_paths"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": bindings[
            "smallest_missing_object_for_complete_C117_I2_action"
        ],
    }
    return {**payload, "root": content_root(payload)}


def apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    missing = completion_record()["smallest_missing_object"]
    raise RuntimeError(
        "C405 cannot apply a complete C117 I2 action; " + str(missing)
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
