"""Distinct RED-class validation projectors on one link-odd kernel."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError
from ...formal.maps import MapClass


class PilotProjection(str, Enum):
    SIVERS_LIKE_PILOT = "SIVERS_LIKE_PILOT"
    BOER_MULDERS_LIKE_PILOT = "BOER_MULDERS_LIKE_PILOT"


@dataclass(frozen=True)
class PilotSpinBlock:
    target_transverse: float
    active_quark_transverse: float
    momentum_pseudovector: float
    stable_id: str = "C5:SPIN_BLOCK:TRANSVERSE"


@dataclass(frozen=True)
class PilotProjector:
    stable_id: str
    projection: PilotProjection
    required_spin_block: str
    map_class: MapClass = MapClass.RED

    def project(self, link_odd: complex, block: PilotSpinBlock, *, route_projection: PilotProjection | None = None) -> float:
        if route_projection is not None and route_projection != self.projection:
            raise ArchitectureError("C5.QUARK.2", "route uses the wrong spin projector", expected=self.projection.value, received=route_projection.value)
        if self.projection == PilotProjection.SIVERS_LIKE_PILOT:
            spin = block.target_transverse
        else:
            spin = block.active_quark_transverse
        if spin == 0:
            raise ArchitectureError("C5.QUARK.1", "operator lacks required transverse spin block", expected=self.required_spin_block, received=block)
        return float(link_odd.imag * spin * block.momentum_pseudovector)


def sivers_like_projector() -> PilotProjector:
    return PilotProjector("C5:RED:SIVERS_LIKE", PilotProjection.SIVERS_LIKE_PILOT, "TARGET_TRANSVERSE_SPIN")


def boer_mulders_like_projector() -> PilotProjector:
    return PilotProjector("C5:RED:BOER_MULDERS_LIKE", PilotProjection.BOER_MULDERS_LIKE_PILOT, "ACTIVE_QUARK_TRANSVERSE_SPIN")


def reject_scalar_proportionality() -> None:
    raise ArchitectureError("C5.QUARK.2", "scalar proportionality between distinct projections is forbidden", expected="independent spin operators", received="C(x,kT)")
