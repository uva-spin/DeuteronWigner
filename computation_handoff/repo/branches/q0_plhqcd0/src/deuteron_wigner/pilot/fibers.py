"""Typed symmetric-frame zero-skewness momentum fibers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum

from ..formal.coordinates import CoordinateKind, CoordinateSpec, coordinate_spec
from ..formal.diagnostics import ArchitectureError
from ..kinematics import MomentumTransfer, TransverseVector


class FiberRole(str, Enum):
    INCOMING = "INCOMING"
    AVERAGE = "AVERAGE"
    OUTGOING = "OUTGOING"


@dataclass(frozen=True)
class MomentumFiber:
    stable_id: str
    role: FiberRole
    p_plus: float
    p_transverse: TransverseVector
    invariant_mass_gev: float
    light_front_convention: str
    normalization_id: str
    regulator_or_pilot_id: str
    hilbert_space_id: str
    sector_scope: str
    version: int = 1

    def __post_init__(self) -> None:
        if self.p_plus <= 0 or self.invariant_mass_gev < 0:
            raise ArchitectureError("C3.FIBER", "invalid LF fiber momentum/mass", expected="p+>0 and M>=0", received=(self.p_plus, self.invariant_mass_gev))
        if not all((self.stable_id, self.light_front_convention, self.normalization_id, self.regulator_or_pilot_id, self.hilbert_space_id, self.sector_scope)):
            raise ArchitectureError("C3.FIBER", "fiber identity incomplete", expected="all identity fields", received=self)

    def require_compatible(self, other: "MomentumFiber") -> None:
        fields = ("p_plus", "invariant_mass_gev", "light_front_convention", "normalization_id", "regulator_or_pilot_id", "hilbert_space_id", "sector_scope")
        mismatch = tuple(name for name in fields if getattr(self, name) != getattr(other, name))
        if mismatch:
            raise ArchitectureError("C3.FIBER", "incompatible momentum fibers", expected=f"equal {fields}", received=mismatch)

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["role"] = self.role.value
        return value


@dataclass(frozen=True)
class ZeroSkewnessFrame:
    average: MomentumFiber
    incoming: MomentumFiber
    outgoing: MomentumFiber
    delta_t: MomentumTransfer
    delta_coordinate: CoordinateSpec = coordinate_spec(CoordinateKind.DELTA_T)
    xi: float = 0.0
    delta_plus: float = 0.0
    version: int = 1

    def __post_init__(self) -> None:
        self.delta_coordinate.require_kind(CoordinateKind.DELTA_T)
        if self.xi != 0 or self.delta_plus != 0:
            raise ArchitectureError("C3.FIBER.XI", "C3 supports only xi=Delta+=0", expected=(0.0, 0.0), received=(self.xi, self.delta_plus))
        self.incoming.require_compatible(self.outgoing)
        self.average.require_compatible(self.incoming)
        if self.average.role != FiberRole.AVERAGE or self.incoming.role != FiberRole.INCOMING or self.outgoing.role != FiberRole.OUTGOING:
            raise ArchitectureError("C3.FIBER.ROLE", "fiber roles inconsistent", expected="AVERAGE/INCOMING/OUTGOING", received=(self.average.role, self.incoming.role, self.outgoing.role))
        expected_in = self.delta_t.scale(-0.5)
        expected_out = self.delta_t.scale(0.5)
        if self.average.p_transverse.norm_squared() != 0 or self.incoming.p_transverse != expected_in or self.outgoing.p_transverse != expected_out:
            raise ArchitectureError("C3.FIBER.FRAME", "not the symmetric xi=0 frame", expected=(expected_in, TransverseVector(0, 0), expected_out), received=(self.incoming.p_transverse, self.average.p_transverse, self.outgoing.p_transverse))

    @classmethod
    def symmetric(cls, *, p_plus: float, mass_gev: float, delta_t: MomentumTransfer, sector_scope: str, member: str = "C3_ANALYTIC") -> "ZeroSkewnessFrame":
        common = dict(p_plus=p_plus, invariant_mass_gev=mass_gev, light_front_convention="vpm=(v0+-v3)/sqrt2", normalization_id="LF_covariant_pilot_v1", regulator_or_pilot_id=member, hilbert_space_id="C3_ANALYTIC_HILBERT", sector_scope=sector_scope)
        return cls(
            MomentumFiber("fiber:average", FiberRole.AVERAGE, p_transverse=TransverseVector(0, 0), **common),
            MomentumFiber("fiber:incoming", FiberRole.INCOMING, p_transverse=delta_t.scale(-0.5), **common),
            MomentumFiber("fiber:outgoing", FiberRole.OUTGOING, p_transverse=delta_t.scale(0.5), **common),
            delta_t,
        )
