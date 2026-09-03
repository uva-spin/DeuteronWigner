"""Validation-only bridge to C2 native reductions."""

from __future__ import annotations

from dataclasses import dataclass

from ..formal.diagnostics import ArchitectureError
from ..formal.reduction import NativeReduction, ReductionRegistry
from .overlap import OverlapResult, PilotStatus


@dataclass(frozen=True)
class PilotReductionBridge:
    registry: ReductionRegistry
    stable_id: str = "C3:VALIDATION_RED_BRIDGE"

    def reduce(self, result: OverlapResult, reduction: NativeReduction):
        if result.status != PilotStatus.NOT_AUTHORIZED_FOR_PRODUCTION:
            raise ArchitectureError("C3.REDUCTION_BRIDGE", "unexpected pilot status", expected=PilotStatus.NOT_AUTHORIZED_FOR_PRODUCTION, received=result.status)
        if reduction.identity.stable_id not in {item.identity.stable_id for item in self.registry.entries()}:
            raise ArchitectureError("C3.REDUCTION_BRIDGE", "reduction is not in validation registry", expected="validation-only reduction", received=reduction.identity.stable_id)
        return reduction(result.value)

    def insert_into_production(self, production_registry: ReductionRegistry, reduction: NativeReduction) -> None:
        raise ArchitectureError("C3.ISOLATE.REGISTRY", "pilot reduction cannot enter accepted registry", expected="separate validation registry", received=reduction.identity.stable_id)
