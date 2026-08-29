"""Common diagonal zeroth-rescattering overlap kernel and evaluator."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ..formal.diagnostics import ArchitectureError
from ..formal.maps import MapClass
from ..formal.operator_identity import DecoratedOperatorId, OperationKind
from .configuration import IntrinsicConfiguration
from .fibers import MomentumFiber
from .recoil import RecoilResult


class PilotStatus(str, Enum):
    VALIDATION_ONLY = "VALIDATION_ONLY"
    ANALYTIC_PILOT = "ANALYTIC_PILOT"
    NOT_AUTHORIZED_FOR_PRODUCTION = "NOT_AUTHORIZED_FOR_PRODUCTION"


@dataclass(frozen=True)
class OverlapKernel:
    stable_id: str
    active_species: str
    active_flavor: str
    active_index: int
    source_sector_id: str
    target_sector_id: str
    active_spin_operator: str
    color_operator: str
    spectator_matching_rule: str
    current_normalization: float
    source_fiber: MomentumFiber
    target_fiber: MomentumFiber
    recoil_convention: str
    operator_identity: DecoratedOperatorId
    wilson_order: int = 0
    map_class: MapClass = MapClass.AMP
    version: int = 1

    def __post_init__(self) -> None:
        if self.map_class != MapClass.AMP:
            raise ArchitectureError("C3.KERNEL.CLASS", "overlap kernel is an amplitude map", expected=MapClass.AMP, received=self.map_class)
        if self.wilson_order != 0:
            raise ArchitectureError("C3.KERNEL.WILSON", "C3 permits zeroth Wilson/rescattering order only", expected=0, received=self.wilson_order)
        if self.source_sector_id != self.target_sector_id:
            raise ArchitectureError("C3.KERNEL.SECTOR", "off-diagonal Fock block has no C3 source", expected=self.source_sector_id, received=self.target_sector_id)
        self.source_fiber.require_compatible(self.target_fiber)
        self.operator_identity.require_complete(OperationKind.BARE_GTMD)
        if self.current_normalization <= 0:
            raise ArchitectureError("C3.KERNEL.NORMALIZATION", "current normalization must be fixed and positive", expected=">0", received=self.current_normalization)

    def adjoint(self) -> "OverlapKernel":
        return type(self)(
            self.stable_id + ":adjoint", self.active_species, self.active_flavor,
            self.active_index, self.target_sector_id, self.source_sector_id,
            self.active_spin_operator + ":adjoint", self.color_operator,
            self.spectator_matching_rule, self.current_normalization,
            self.target_fiber, self.source_fiber, self.recoil_convention,
            self.operator_identity, self.wilson_order, self.map_class, self.version,
        )


@dataclass(frozen=True)
class OverlapResult:
    stable_id: str
    operator_identity: DecoratedOperatorId
    source_fiber: MomentumFiber
    target_fiber: MomentumFiber
    sector_id: str
    active_slot: int
    value: complex
    evaluation_mode: str
    normalization_ledger: tuple[tuple[str, float], ...]
    hermiticity_partner_id: str
    residuals: tuple[tuple[str, float], ...]
    provenance_trace: tuple[str, ...]
    status: PilotStatus = PilotStatus.NOT_AUTHORIZED_FOR_PRODUCTION
    version: int = 1

    def authorize_production(self):
        raise ArchitectureError("C3.ISOLATE.PROMOTION", "analytic pilot cannot enter production", expected=PilotStatus.NOT_AUTHORIZED_FOR_PRODUCTION.value, received="production request")


class AnalyticOverlapEvaluator:
    stable_id = "C3:COMMON_DIAGONAL_OVERLAP"

    def evaluate(self, state, configuration: IntrinsicConfiguration, recoil: RecoilResult, kernel: OverlapKernel) -> OverlapResult:
        if kernel.active_index != configuration.active_index or recoil.active_index != configuration.active_index:
            raise ArchitectureError("C3.OVERLAP.ACTIVE", "active-slot identity mismatch", expected=configuration.active_index, received=(kernel.active_index, recoil.active_index))
        if kernel.source_sector_id != configuration.sector.basis_id:
            raise ArchitectureError("C3.OVERLAP.SECTOR", "kernel/configuration sector mismatch", expected=kernel.source_sector_id, received=configuration.sector.basis_id)
        for index, (incoming, outgoing) in enumerate(zip(recoil.incoming.constituents, recoil.outgoing.constituents)):
            if index != configuration.active_index and (
                incoming.species != outgoing.species or incoming.flavor != outgoing.flavor
                or incoming.color != outgoing.color or incoming.helicity != outgoing.helicity
            ):
                raise ArchitectureError("C3.OVERLAP.SPECTATOR", "spectator quantum numbers mismatch", expected=incoming, received=outgoing)
        active = configuration.constituents[configuration.active_index]
        if kernel.active_species != active.species.value:
            raise ArchitectureError(
                "C4.ACTIVE.SPECIES", "kernel selects the wrong active species",
                expected=active.species.value, received=kernel.active_species,
            )
        expected_flavor = (
            "NOT_APPLICABLE"
            if active.species.value == "g" else active.flavor
        )
        if kernel.active_flavor != expected_flavor:
            raise ArchitectureError(
                "C4.ACTIVE.FLAVOR", "kernel selects the wrong active flavor",
                expected=expected_flavor, received=kernel.active_flavor,
            )
        psi_in = state.amplitude(recoil.incoming)
        psi_out = state.amplitude(recoil.outgoing)
        value = kernel.current_normalization * psi_out.conjugate() * psi_in
        return OverlapResult(
            f"overlap:{state.stable_id}:{configuration.active_index}",
            kernel.operator_identity, kernel.source_fiber, kernel.target_fiber,
            configuration.sector.basis_id, configuration.active_index, value,
            "analytic", (("state_norm", 1.0), ("current_norm", kernel.current_normalization)),
            f"overlap:{state.stable_id}:{configuration.active_index}:adjoint",
            (("algebra", 0.0), ("floating", 0.0)),
            (state.stable_id, recoil.convention_id, kernel.stable_id),
        )
