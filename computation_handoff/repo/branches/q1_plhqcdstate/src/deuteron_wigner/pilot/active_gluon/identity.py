"""Ordered two-adjoint-link active-gluon operator identity."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace

from ...formal.diagnostics import ArchitectureError
from ...formal.gauge_path import ColorRepresentation, StapleOrientation
from ..wilson_line.identity import BareWilsonSegment


@dataclass(frozen=True)
class OrderedAdjointLinkPair:
    left: BareWilsonSegment
    right: BareWilsonSegment
    trace_closure_identity: str
    stable_id: str = "C6:LINK_PAIR:ORDERED"

    def __post_init__(self) -> None:
        if self.left.representation != ColorRepresentation.ADJOINT or self.right.representation != ColorRepresentation.ADJOINT:
            raise ArchitectureError("C6.GLID.2", "both active-gluon Wilson legs must be adjoint", expected="ADJOINT,ADJOINT", received=(self.left.representation, self.right.representation))
        if self.left.start_fiber != self.right.start_fiber or self.left.end_or_infinity_class != self.right.end_or_infinity_class:
            raise ArchitectureError("C6.GLID.2", "ordered links have incompatible endpoint fibers", expected=(self.left.start_fiber, self.left.end_or_infinity_class), received=(self.right.start_fiber, self.right.end_or_infinity_class))
        if not self.trace_closure_identity:
            raise ArchitectureError("C6.GLID.1", "active-gluon link pair lacks trace closure", expected="explicit trace closure", received=self.trace_closure_identity)

    @property
    def orientation_word(self) -> tuple[str, str]:
        return (self.left.orientation.value, self.right.orientation.value)

    @property
    def ordered_pair_id(self) -> str:
        return f"{self.stable_id}:{self.left.stable_id}|{self.right.stable_id}"

    def swapped(self) -> "OrderedAdjointLinkPair":
        return OrderedAdjointLinkPair(self.right, self.left, self.trace_closure_identity, self.stable_id + ":SWAPPED")

    def reverse_one(self, side: str) -> "OrderedAdjointLinkPair":
        def reversed_orientation(segment: BareWilsonSegment) -> BareWilsonSegment:
            return replace(
                segment, path_id=segment.path_id.inverted(),
                tangent=tuple(-item for item in segment.tangent),
                orientation=(
                    StapleOrientation.PAST
                    if segment.orientation == StapleOrientation.FUTURE
                    else StapleOrientation.FUTURE
                ),
                stable_id=segment.stable_id + ":ONE_LEG_REVERSED",
            )
        if side == "left":
            return OrderedAdjointLinkPair(reversed_orientation(self.left), self.right, self.trace_closure_identity, self.stable_id + ":LEFT_REVERSED")
        if side == "right":
            return OrderedAdjointLinkPair(self.left, reversed_orientation(self.right), self.trace_closure_identity, self.stable_id + ":RIGHT_REVERSED")
        raise KeyError(side)

    def antiunitary_pair(self) -> "OrderedAdjointLinkPair":
        # The declared operator convention transforms each ordered leg in
        # place; it does not silently sort or identify the pair.
        return OrderedAdjointLinkPair(
            self.left.inverted(), self.right.inverted(),
            self.trace_closure_identity, self.stable_id + ":THETA",
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "left": self.left.to_dict(), "right": self.right.to_dict(),
            "trace_closure_identity": self.trace_closure_identity,
            "stable_id": self.stable_id,
            "ordered_pair_id": self.ordered_pair_id,
            "orientation_word": list(self.orientation_word),
        }


@dataclass(frozen=True)
class ActiveGluonOperatorId:
    link_pair: OrderedAdjointLinkPair
    source_state_member_id: str
    field_strength_left_index: str = "i"
    field_strength_right_index: str = "j"
    active_species: str = "GLUON"
    color_status: str = "DIAGONAL_ADJOINT"
    rapidity_regulator_id: str = "C6:REG:ANALYTIC_DELTA"
    soft_route_id: str = "BOUNDARY_ONLY_RESCATTERING"
    operator_scheme_status: str = "UNSUBTRACTED_ACTIVE_GLUON_PILOT"
    wilson_order: int = 1
    stable_id: str = "C6:OP:ACTIVE_GLUON_FF"

    def __post_init__(self) -> None:
        if self.active_species != "GLUON" or self.color_status != "DIAGONAL_ADJOINT":
            raise ArchitectureError("C6.GLID.1", "invalid active-gluon operator status", expected=("GLUON", "DIAGONAL_ADJOINT"), received=(self.active_species, self.color_status))
        if self.wilson_order != 1:
            raise ArchitectureError("C6.DYN.1", "C6 is restricted to first Wilson order", expected=1, received=self.wilson_order)

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["link_pair"] = self.link_pair.to_dict()
        return value
