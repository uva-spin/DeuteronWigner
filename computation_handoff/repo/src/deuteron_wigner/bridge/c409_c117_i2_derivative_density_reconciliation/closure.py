"""C409 truthful completion boundary."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .authority import (
    STATUS,
    derivative_count_authority,
    reduced_transverse_authority,
    scale_power_reconciliation,
    scientific_boundary_record,
    source_hash_audit,
)
from .bindings import binding_update_summary
from .derivative_count import derivative_count_validation
from .jgjg import jgjg_qg_validation


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    binding = binding_update_summary()
    payload = {
        "schema": "C409-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "source_hash_audit_pass": source_hash_audit()["all_pass"],
        "derivative_count_authority": derivative_count_authority(),
        "scale_power_reconciliation": scale_power_reconciliation(),
        "reduced_transverse_authority": reduced_transverse_authority(),
        "scientific_boundary": scientific_boundary_record(),
        "derivative_count_validation_pass": derivative_count_validation()["pass"],
        "J_gJ_g_number_preserving_qg_product_block_ready": jgjg_qg_validation()[
            "pass"
        ],
        "J_gJ_g_q_sector_complete": False,
        "source_routed_product_block_primitive_paths": 12,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding[
            "current_complete_numerical_apply_paths"
        ],
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
        "C409 cannot apply a complete C117 I2 action: J_gJ_g q-sector pair/vacuum "
        "branches, common finite-cell/field/state/M2 normalization, target count-once "
        "aggregation, g_s^2, and c_C117_1 remain unavailable"
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
