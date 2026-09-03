"""Deterministic one-gluon rescattering benchmark kernel."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import pi, sin

from ...formal.diagnostics import ArchitectureError
from ...formal.gauge_path import ColorRepresentation
from ..states import SpinorOAMState
from .cuts import CutLedger, LFResolventTerm
from .identity import BareWilsonSegment, derived_eikonal_pole


@dataclass(frozen=True)
class PilotKernelInput:
    state: SpinorOAMState
    path: BareWilsonSegment
    resolvent: LFResolventTerm
    cut_ledger: CutLedger
    coupling: float
    radial_kernel_01: float
    azimuth: float
    active_species: str
    flavor: str
    active_slot_id: str
    source_vertex_id: str = "C5:VERTEX:EIKONAL_ONE_GLUON"
    companion_ordering_id: str = "C5:ORDER:OPERATOR_THEN_RESCATTER"
    source_commit: str = "62125f0857e597e8f9548f279ae70b1634764a24"
    configuration_hash: str = "C5_ANALYTIC_V1"

    def __post_init__(self) -> None:
        if self.path.representation != ColorRepresentation.FUNDAMENTAL:
            raise ArchitectureError("C5.KERNEL.1", "quark pilot requires a fundamental Wilson path", expected=ColorRepresentation.FUNDAMENTAL, received=self.path.representation)
        if self.active_species not in ("QUARK", "ANTIQUARK") or not self.flavor:
            raise ArchitectureError("C5.KERNEL.2", "invalid positive-x quark/antiquark identity", expected="QUARK|ANTIQUARK with explicit flavor", received=(self.active_species, self.flavor))
        if self.resolvent.source_vertex_id != self.source_vertex_id:
            raise ArchitectureError("C5.KERNEL.1", "resolvent and kernel vertex identities disagree", expected=self.source_vertex_id, received=self.resolvent.source_vertex_id)


@dataclass(frozen=True)
class PilotAmplitude:
    stable_id: str
    orientation_eta: int
    principal_value: float
    absorptive: float
    oam_interference: float
    value: complex
    state_id: str
    operator_id: str
    path_id: str
    cut_weight: float

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["value"] = [self.value.real, self.value.imag]
        return value


class OneGluonPilotKernel:
    fundamental_color_factor = 4.0 / 3.0
    adjoint_color_factor = 3.0
    wilson_order = 1
    scientific_status = "VALIDATION_ONLY"

    def evaluate(self, item: PilotKernelInput, *, require_oam: bool = True) -> PilotAmplitude:
        pole = derived_eikonal_pole(item.path)
        a0, ap, am = item.state.normalized()
        oam1 = ap - am
        if require_oam and (abs(a0) == 0 or abs(oam1) == 0):
            interference = 0.0
        else:
            interference = float(2 * abs(a0) * abs(oam1) * item.radial_kernel_01 * sin(item.azimuth))
        cut_weight = item.cut_ledger.active_weight()
        pv = item.coupling * self.fundamental_color_factor * interference / (
            item.resolvent.energy_difference if item.resolvent.energy_difference else 1.0
        )
        absorptive = (
            item.coupling * self.fundamental_color_factor * pi
            * pole.eta * cut_weight * interference
        )
        if item.coupling == 0 or cut_weight == 0 or interference == 0:
            absorptive = 0.0
        return PilotAmplitude(
            f"C5:AMPLITUDE:{item.path.orientation.value}",
            pole.eta, pv, absorptive, interference, complex(pv, absorptive),
            item.state.stable_id, item.resolvent.target_operator_id,
            item.path.stable_id, cut_weight,
        )

    @staticmethod
    def ward_residual(
        active_attachment: complex, spectator_attachment: complex,
        eikonal_attachment: complex,
    ) -> float:
        """Restricted pilot Ward closure; all three declared attachments."""
        return abs(active_attachment + spectator_attachment + eikonal_attachment)
