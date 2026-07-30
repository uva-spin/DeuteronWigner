"""Typed path dynamics and a convention-derived eikonal pole."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError
from ...formal.gauge_path import ColorRepresentation, StapleOrientation, WilsonPathId


class FourierConvention(str, Enum):
    EXP_MINUS_I_L_DOT_X = "EXP_MINUS_I_L_DOT_X"


class CouplingConvention(str, Enum):
    D_MU_PARTIAL_PLUS_IG_A = "D_MU_PARTIAL_PLUS_IG_A"


class MomentumFlowConvention(str, Enum):
    GLUON_INTO_EIKONAL = "GLUON_INTO_EIKONAL"


class PathOrdering(str, Enum):
    INCREASING_LAMBDA_RIGHT_TO_LEFT = "INCREASING_LAMBDA_RIGHT_TO_LEFT"


@dataclass(frozen=True)
class BareWilsonSegment:
    path_id: WilsonPathId
    start_fiber: str
    end_or_infinity_class: str
    tangent: tuple[float, float, float, float]
    orientation: StapleOrientation
    representation: ColorRepresentation
    path_ordering: PathOrdering
    transverse_closure_identity: str
    fourier_convention: FourierConvention
    coupling_convention: CouplingConvention
    momentum_flow: MomentumFlowConvention
    rapidity_regulator_identity: str
    wilson_order: int = 1
    stable_id: str = "C5:PATH:SEMI_INFINITE"

    def __post_init__(self) -> None:
        if self.orientation not in (StapleOrientation.FUTURE, StapleOrientation.PAST):
            raise ArchitectureError("C5.PATH.1", "pilot requires an oriented semi-infinite path", expected="FUTURE|PAST", received=self.orientation)
        if self.path_id.staple_orientation != self.orientation or self.path_id.color_representation != self.representation:
            raise ArchitectureError("C5.PATH.1", "dynamic path disagrees with authoritative path identity", expected=(self.path_id.staple_orientation, self.path_id.color_representation), received=(self.orientation, self.representation))
        if self.wilson_order != 1:
            raise ArchitectureError("C5.PATH.2", "C5 is restricted to first Wilson order", expected=1, received=self.wilson_order)
        if len(self.tangent) != 4 or not any(self.tangent):
            raise ArchitectureError("C5.PATH.1", "invalid eikonal tangent", expected="nonzero four-vector", received=self.tangent)

    @property
    def eta(self) -> int:
        return 1 if self.orientation == StapleOrientation.FUTURE else -1

    def inverted(self) -> "BareWilsonSegment":
        return BareWilsonSegment(
            self.path_id.inverted(), self.end_or_infinity_class, self.start_fiber,
            tuple(-x for x in self.tangent), StapleOrientation.PAST if self.eta == 1 else StapleOrientation.FUTURE,
            self.representation, self.path_ordering, self.transverse_closure_identity,
            self.fourier_convention, self.coupling_convention, self.momentum_flow,
            self.rapidity_regulator_identity, self.wilson_order,
            self.stable_id + ":INVERSE",
        )

    def compose(self, earlier: "BareWilsonSegment") -> tuple["BareWilsonSegment", "BareWilsonSegment"]:
        if earlier.end_or_infinity_class != self.start_fiber:
            raise ArchitectureError("C5.PATH.2", "path composition has incompatible endpoint fibers", expected=self.start_fiber, received=earlier.end_or_infinity_class)
        return (self, earlier)

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["path_id"] = self.path_id.to_dict()
        for key in ("orientation", "representation", "path_ordering", "fourier_convention", "coupling_convention", "momentum_flow"):
            value[key] = getattr(self, key).value
        return value


@dataclass(frozen=True)
class EikonalPole:
    stable_id: str
    eta: int
    denominator_form: str
    pv_coefficient: float
    delta_coefficient_imaginary: float

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def derived_eikonal_pole(path: BareWilsonSegment, *, manual_sign: int | None = None) -> EikonalPole:
    if manual_sign is not None:
        raise ArchitectureError("C5.POLE.1", "eikonal pole sign cannot be supplied independently", expected="derived from complete path conventions", received=manual_sign)
    expected = (
        FourierConvention.EXP_MINUS_I_L_DOT_X,
        CouplingConvention.D_MU_PARTIAL_PLUS_IG_A,
        MomentumFlowConvention.GLUON_INTO_EIKONAL,
    )
    received = (path.fourier_convention, path.coupling_convention, path.momentum_flow)
    if received != expected:
        raise ArchitectureError("C5.POLE.1", "unsupported convention tuple", expected=expected, received=received)
    eta = path.eta
    return EikonalPole(
        f"C5:POLE:{path.orientation.value}", eta,
        f"1/(v.l-i0*{eta:+d})", 1.0, eta,
    )
