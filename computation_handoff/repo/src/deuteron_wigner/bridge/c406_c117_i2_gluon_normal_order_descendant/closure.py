"""C406 truthful completion boundary."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root

from .bindings import binding_update_summary
from .mixed_kernel import mixed_kernel_validation
from .normal_order import STATUS, normal_ordering_validation
from .routing import product_routing_audit


@lru_cache(maxsize=1)
def completion_record() -> Mapping[str, Any]:
    binding = binding_update_summary()
    normal = normal_ordering_validation()
    routing = product_routing_audit()
    mixed = mixed_kernel_validation()
    payload = {
        "schema": "C406-C117-I2-COMPLETION-RECORD-V1",
        "status": STATUS,
        "one_gluon_normal_order_descendant_ready": normal["pass"],
        "mixed_product_derivative_routing_ready": routing["mixed_derivative_ambiguity_closed"],
        "mixed_qg_numerical_primitives_ready": mixed["pass"],
        "same_species_contraction_axes_ready": routing["same_species_contraction_axes_closed"],
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
        "C406 cannot apply a complete C117 I2 action; same-species contraction axes, "
        "normalization, target aggregation, coupling, and coefficient remain unavailable"
    )


__all__ = ["completion_record", "apply_complete_c117_i2"]
