"""C407 truthful completion boundary."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .authority import STATUS, scientific_boundary_record, source_hash_audit
from .axis import intermediate_axis_inventory
from .bindings import binding_update_summary
from .descendants import longitudinal_validation
from .jqjq_qg import jqjq_qg_conditioned_validation


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    binding = binding_update_summary()
    axes = intermediate_axis_inventory()
    longitudinal = longitudinal_validation()
    jqjq = jqjq_qg_conditioned_validation()
    payload = {
        "schema": "C407-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "source_hash_audit_pass": source_hash_audit()["all_pass"],
        "scientific_boundary": scientific_boundary_record(),
        "same_species_intermediate_axes_ready": axes["row_count"] == 154,
        "same_species_longitudinal_descendants_ready": longitudinal["pass"],
        "J_qJ_q_qg_caller_conditioned_composition_ready": jqjq["pass"],
        "J_qJ_q_qg_source_authorized_graph_weights_ready": False,
        "J_qJ_q_q_sector_ready": False,
        "J_gJ_g_qg_full_transverse_descendant_ready": False,
        "J_gJ_g_q_sector_ready": False,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding["current_complete_numerical_apply_paths"],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": binding[
            "smallest_missing_object_for_complete_C117_I2_action"
        ],
    }
    return {**payload, "root": content_root(payload)}


def apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C407 cannot apply a complete C117 I2 action; source-authorized J_qJ_q graph-member weights, "
        "the J_qJ_q q-sector I4 kernel, "
        "J_gJ_g derivative-density transverse descendant, q-sector gluon branches, common "
        "normalization, target aggregation, coupling, and coefficient remain unavailable"
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
