"""C410 truthful completion boundary."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .aggregate import count_once_aggregation_record, retained_aggregation_validation
from .authority import (
    STATUS,
    aggregation_authority,
    scientific_boundary_record,
    source_hash_audit,
    vacuum_routing_authority,
)
from .bindings import binding_update_summary
from .normalization import (
    MISSING_NORMALIZATION_OBJECT,
    normalization_boundary_record,
    normalization_capsule_schema,
)
from .vacuum import vacuum_pair_validation, q_sector_vacuum_projection_validation


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    binding = binding_update_summary()
    payload = {
        "schema": "C410-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "source_hash_audit_pass": source_hash_audit()["all_pass"],
        "vacuum_routing_authority": vacuum_routing_authority(),
        "vacuum_pair_validation_pass": vacuum_pair_validation()["pass"],
        "q_sector_vacuum_projection_validation_pass": (
            q_sector_vacuum_projection_validation()["pass"]
        ),
        "aggregation_authority": aggregation_authority(),
        "count_once_aggregation_pass": count_once_aggregation_record()["pass"],
        "retained_aggregation_validation_pass": retained_aggregation_validation()[
            "pass"
        ],
        "normalization_boundary": normalization_boundary_record(),
        "normalization_capsule_schema": normalization_capsule_schema(),
        "scientific_boundary": scientific_boundary_record(),
        "J_gJ_g_q_sector_retained_connected_block_ready": True,
        "source_routed_product_block_primitive_paths": 12,
        "retained_connected_aggregate_shape_paths": 3,
        "complete_C117_numerical_apply_paths": 0,
        "complete_C396_numerical_apply_paths": binding[
            "current_complete_numerical_apply_paths"
        ],
        "full_C117_I2_action_ready": False,
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
        "smallest_missing_object": MISSING_NORMALIZATION_OBJECT,
    }
    return dict(payload, root=content_root(payload))


def apply_complete_c117_i2(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError(
        "C410 retains only a source-reduced aggregate shape; complete O_C117_1,R "
        "is unavailable because {}".format(MISSING_NORMALIZATION_OBJECT)
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
