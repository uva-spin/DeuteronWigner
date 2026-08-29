"""One common active-gluon tensor parent and downstream RED views."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ...formal.maps import MapClass
from ..color import structure_constants
from ..routes import GluonPolarizationProjector, project_gluon_polarization
from ..wilson_line.color_guard import symmetric_constants
from .color import ColorChannel, ThreeAdjointColorKernel
from .identity import ActiveGluonOperatorId


class GluonPolarizationView(str, Enum):
    TRACE = "GLUON_TRACE_LINK_ODD_PILOT"
    HELICITY_ANTISYMMETRIC = "GLUON_HELICITY_ANTISYMMETRIC_LINK_ODD_PILOT"
    SYMMETRIC_TRACELESS = "GLUON_SYMMETRIC_TRACELESS_LINK_ODD_PILOT"


_C4_PROJECTOR = {
    GluonPolarizationView.TRACE: GluonPolarizationProjector.TRACE_UNPOLARIZED,
    GluonPolarizationView.HELICITY_ANTISYMMETRIC: GluonPolarizationProjector.ANTISYMMETRIC_HELICITY,
    GluonPolarizationView.SYMMETRIC_TRACELESS: GluonPolarizationProjector.SYMMETRIC_TRACELESS_LINEAR,
}


@dataclass(frozen=True)
class ActiveGluonTensorParent:
    """Factorized tensor with explicit target/gluon helicity and color axes.

    Axis order is target final, target initial, active-gluon final,
    active-gluon initial, transverse i, transverse j, and three adjoint color
    indices.
    """

    tensor: np.ndarray
    operator_id: ActiveGluonOperatorId
    active_slot_id: str
    source_sector_id: str
    target_sector_id: str
    cut_ledger_id: str
    oam_block_ids: tuple[str, ...]
    phase_budget_id: str
    regulator_id: str
    stable_id: str = "C6:PARENT:ACTIVE_GLUON_COMMON_TENSOR"
    map_class: MapClass = MapClass.AMP

    def __post_init__(self) -> None:
        if self.tensor.shape != (2, 2, 2, 2, 2, 2, 8, 8, 8):
            raise ArchitectureError("C6.STATE.2", "common active-gluon tensor has wrong axes", expected=(2, 2, 2, 2, 2, 2, 8, 8, 8), received=self.tensor.shape)
        if self.map_class != MapClass.AMP:
            raise ArchitectureError("C6.STATE.2", "stored parent must precede RED projections", expected=MapClass.AMP, received=self.map_class)

    @classmethod
    def factorized(
        cls, helicity_kernel: np.ndarray, transverse: np.ndarray,
        color: ThreeAdjointColorKernel, operator_id: ActiveGluonOperatorId,
        active_slot_id: str,
    ) -> "ActiveGluonTensorParent":
        if helicity_kernel.shape != (2, 2, 2, 2) or transverse.shape != (2, 2):
            raise ArchitectureError("C6.STATE.3", "helicity/transverse fixture shape mismatch", expected=((2,2,2,2),(2,2)), received=(helicity_kernel.shape, transverse.shape))
        tensor = np.einsum("ABab,ij,cde->ABabijcde", helicity_kernel, transverse, color.tensor)
        return cls(
            tensor, operator_id, active_slot_id, "C4:SECTOR:QQQG",
            "C4:SECTOR:QQQG", "C6:CUT_LEDGER:ACTIVE_GLUON",
            ("LZ_0", "LZ_PLUS_1"), "C6:PHASE_BUDGET:ACTIVE_GLUON",
            operator_id.rapidity_regulator_id,
        )

    def color_projected_matrix(
        self, channel: ColorChannel, *,
        target_final: int = 0, target_initial: int = 0,
        gluon_final: int = 0, gluon_initial: int = 0,
    ) -> np.ndarray:
        # Project each transverse element with the same normalized color tensor.
        basis = (
            -1j * structure_constants() / 24
            if channel == ColorChannel.F_TYPE
            else symmetric_constants() / (40 / 3)
        )
        return np.einsum(
            "ijabc,abc->ij",
            self.tensor[target_final, target_initial, gluon_final, gluon_initial],
            basis,
        )

    def polarization_view(self, channel: ColorChannel, view: GluonPolarizationView):
        return project_gluon_polarization(self.color_projected_matrix(channel), _C4_PROJECTOR[view])

    def reconstruction_residual(self, channel: ColorChannel) -> float:
        matrix = self.color_projected_matrix(channel)
        trace = self.polarization_view(channel, GluonPolarizationView.TRACE)
        helicity = self.polarization_view(channel, GluonPolarizationView.HELICITY_ANTISYMMETRIC)
        st = self.polarization_view(channel, GluonPolarizationView.SYMMETRIC_TRACELESS)
        trace_matrix = 0.5 * trace * np.eye(2)
        asym_coefficient = helicity / (2j)
        asym = np.asarray(((0, asym_coefficient), (-asym_coefficient, 0)), complex)
        return float(np.max(np.abs(matrix - trace_matrix - asym - st)))

    def identity_record(self, channel: ColorChannel, view: GluonPolarizationView) -> dict[str, object]:
        return {
            "parent_id": self.stable_id, "operator_id": self.operator_id.stable_id,
            "ordered_pair_id": self.operator_id.link_pair.ordered_pair_id,
            "cut_ledger_id": self.cut_ledger_id, "color_channel": channel.value,
            "polarization_projector": view.value, "active_slot_id": self.active_slot_id,
            "state_member_id": self.operator_id.source_state_member_id,
            "phase_budget_id": self.phase_budget_id, "map_class": MapClass.RED.value,
        }
