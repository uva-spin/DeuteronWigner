"""C408 truthful completion boundary."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .authority import (
    STATUS,
    derivative_density_conflict_record,
    i2_member_weight_authority,
    routing_authority_record,
    scientific_boundary_record,
    source_hash_audit,
)
from .bindings import binding_update_summary
from .i4_q import q_sector_i4_validation
from .jqjq import jqjq_product_block_validation
from .weights import i2_source_weight_validation


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    binding = binding_update_summary()
    payload = {
        "schema": "C408-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "source_hash_audit_pass": source_hash_audit()["all_pass"],
        "routing_authority": routing_authority_record(),
        "i2_member_weight_authority": i2_member_weight_authority(),
        "derivative_density_conflict": derivative_density_conflict_record(),
        "scientific_boundary": scientific_boundary_record(),
        "J_qJ_q_q_sector_I4_ready": q_sector_i4_validation()["pass"],
        "I2_source_descendant_member_weights_ready": i2_source_weight_validation()["pass"],
        "J_qJ_q_direct_sum_product_block_ready": jqjq_product_block_validation()["pass"],
        "mixed_current_source_weighted_product_blocks_ready": True,
        "J_gJ_g_derivative_density_ready": False,
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
    return dict(payload, root=content_root(payload))


def apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C408 cannot apply a complete C117 I2 action; J_gJ_g derivative-density derivative-count "
        "reconciliation, q-sector gluon branches, common normalization, target aggregation, coupling, "
        "and c_C117_1 remain unavailable"
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
