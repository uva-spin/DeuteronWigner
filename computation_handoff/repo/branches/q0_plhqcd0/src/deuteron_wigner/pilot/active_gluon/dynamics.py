"""First-order active-gluon rescattering from C4 state and C5 cuts/poles."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sin

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ...gtmd import Species
from ..active import PositiveXActiveSelector
from ..color import GluonColorSinglet
from ..sectors import gluon_state
from ..wilson_line.cuts import CutLedger, LFResolventTerm
from ..wilson_line.identity import derived_eikonal_pole
from .color import ThreeAdjointColorKernel
from .identity import ActiveGluonOperatorId
from .parent import ActiveGluonTensorParent


@dataclass(frozen=True)
class ActiveGluonKernelInput:
    operator_id: ActiveGluonOperatorId
    cut_ledger: CutLedger
    resolvent: LFResolventTerm
    coupling: float
    radial_kernel_01: float
    azimuth: float
    oam0: complex
    oam1: complex
    antisymmetric_color_weight: float = 1.0
    symmetric_color_weight: float = 0.6
    attachment_set: tuple[str, ...] = (
        "ACTIVE_FIELD", "LEFT_LINK", "RIGHT_LINK", "SPECTATOR_COLOR",
    )
    exchanged_gluon_id: str = "C6:EXCHANGED_GLUON:ONE"
    stable_id: str = "C6:KERNEL_INPUT:ACTIVE_GLUON"

    def __post_init__(self) -> None:
        required = {"ACTIVE_FIELD", "LEFT_LINK", "RIGHT_LINK", "SPECTATOR_COLOR"}
        if set(self.attachment_set) != required:
            raise ArchitectureError("C6.DYN.4", "incomplete active-gluon Ward attachment set", expected=sorted(required), received=sorted(self.attachment_set))


class ActiveGluonRescatteringKernel:
    stable_id = "C6:AMP:ACTIVE_GLUON_ONE_EXCHANGE"
    wilson_order = 1
    status = "VALIDATION_ONLY"

    @staticmethod
    def active_slot() -> tuple[str, float]:
        state = gluon_state(0.3)
        higher = state.sectors[-1]
        selected = PositiveXActiveSelector().select(higher.configuration, Species.GLUON)
        if len(selected) != 1:
            raise ArchitectureError("C6.STATE.1", "active-gluon slot is not unique", expected=1, received=len(selected))
        item = higher.configuration.constituents[selected[0].slot_index]
        if item.x <= 0:
            raise ArchitectureError("C6.STATE.1", "active-gluon slot must have positive x", expected=">0", received=item.x)
        return selected[0].slot_id, item.x

    def evaluate(self, item: ActiveGluonKernelInput) -> ActiveGluonTensorParent:
        slot_id, _ = self.active_slot()
        left_pole = derived_eikonal_pole(item.operator_id.link_pair.left)
        right_pole = derived_eikonal_pole(item.operator_id.link_pair.right)
        cut = item.cut_ledger.active_weight()
        oam = 2 * abs(item.oam0) * abs(item.oam1) * item.radial_kernel_01 * sin(item.azimuth)
        orientation = 0.5 * (left_pole.eta + right_pole.eta)
        absorptive = item.coupling * pi * cut * oam * orientation
        if item.coupling == 0 or cut == 0 or oam == 0:
            absorptive = 0.0
        color = ThreeAdjointColorKernel.from_ordered_couplers(
            1j * absorptive * item.antisymmetric_color_weight,
            1j * absorptive * item.symmetric_color_weight,
        )
        helicity = np.zeros((2, 2, 2, 2), complex)
        helicity[0, 0, 0, 0] = 1
        helicity[1, 1, 1, 1] = 0.8
        helicity[0, 1, 0, 1] = helicity[1, 0, 1, 0] = 0.2
        transverse = np.asarray(((1.2, 0.3 + 0.25j), (0.3 - 0.25j, 0.8)), complex)
        return ActiveGluonTensorParent.factorized(
            helicity, transverse, color, item.operator_id, slot_id,
        )

    @staticmethod
    def ward_residual(attachments: dict[str, complex], channel: str) -> float:
        required = {"ACTIVE_FIELD", "LEFT_LINK", "RIGHT_LINK", "SPECTATOR_COLOR"}
        if set(attachments) != required:
            raise ArchitectureError("C6.WARD.2", "missing active-gluon Ward attachment", expected=sorted(required), received=sorted(attachments))
        if channel not in ("F_TYPE", "D_TYPE"):
            raise ArchitectureError("C6.WARD.4", "Ward channel must retain f/d identity", expected="F_TYPE|D_TYPE", received=channel)
        return abs(sum(attachments.values()))

    @staticmethod
    def color_singlet_residual() -> float:
        return GluonColorSinglet().generator_residual()
