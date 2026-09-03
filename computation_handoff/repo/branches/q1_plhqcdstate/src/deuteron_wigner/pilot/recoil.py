"""Single authoritative symmetric-xi=0 active/spectator recoil map."""

from __future__ import annotations

from dataclasses import dataclass

from ..formal.diagnostics import ArchitectureError
from ..kinematics import MomentumTransfer, PartonMomentum
from .configuration import Constituent, IntrinsicConfiguration
from .fibers import ZeroSkewnessFrame


@dataclass(frozen=True)
class RecoilResult:
    convention_id: str
    incoming: IntrinsicConfiguration
    outgoing: IntrinsicConfiguration
    frame: ZeroSkewnessFrame
    active_index: int
    jacobian: float
    version: int = 1

    def __post_init__(self) -> None:
        if self.jacobian != 1:
            raise ArchitectureError("C3.RECOIL.JACOBIAN", "symmetric affine recoil has unit Jacobian", expected=1.0, received=self.jacobian)


@dataclass(frozen=True)
class SymmetricXiZeroRecoil:
    stable_id: str = "SYMMETRIC_XI0"
    version: int = 1

    def apply(self, configuration: IntrinsicConfiguration, frame: ZeroSkewnessFrame, *, jacobian: float = 1.0) -> RecoilResult:
        delta = frame.delta_t
        active = configuration.active_index
        incoming, outgoing = [], []
        for index, item in enumerate(configuration.constituents):
            if index == active:
                in_shift = delta.scale(-0.5 * (1 - item.x))
                out_shift = delta.scale(0.5 * (1 - item.x))
            else:
                in_shift = delta.scale(0.5 * item.x)
                out_shift = delta.scale(-0.5 * item.x)
            incoming.append(_shift(item, in_shift))
            outgoing.append(_shift(item, out_shift))
        return RecoilResult(
            self.stable_id,
            IntrinsicConfiguration(tuple(incoming), active, configuration.sector, configuration.member_id, configuration.phase_id, configuration.permutation_class),
            IntrinsicConfiguration(tuple(outgoing), active, configuration.sector, configuration.member_id, configuration.phase_id, configuration.permutation_class),
            frame, active, jacobian,
        )

    def verify_physical_assignment(self, result: RecoilResult, tolerance: float = 1e-13) -> None:
        delta = result.frame.delta_t
        active = result.active_index
        for index, (before, after) in enumerate(zip(result.incoming.constituents, result.outgoing.constituents)):
            # Physical p_iT = kappa_iT + x_i P_T.
            p_in = PartonMomentum(before.k_t.x + before.x * result.frame.incoming.p_transverse.x, before.k_t.y + before.x * result.frame.incoming.p_transverse.y)
            p_out = PartonMomentum(after.k_t.x + after.x * result.frame.outgoing.p_transverse.x, after.k_t.y + after.x * result.frame.outgoing.p_transverse.y)
            expected = delta if index == active else MomentumTransfer(0, 0)
            received = MomentumTransfer(p_out.x - p_in.x, p_out.y - p_in.y)
            if abs(received.x - expected.x) > tolerance or abs(received.y - expected.y) > tolerance:
                raise ArchitectureError("C3.RECOIL.PHYSICAL", "active/spectator physical assignment failed", expected=expected, received=received)


def _shift(item: Constituent, shift) -> Constituent:
    return Constituent(item.stable_id, item.x, PartonMomentum(item.k_t.x + shift.x, item.k_t.y + shift.y), item.species, item.flavor, item.color, item.helicity, item.lz, item.basis_id)
