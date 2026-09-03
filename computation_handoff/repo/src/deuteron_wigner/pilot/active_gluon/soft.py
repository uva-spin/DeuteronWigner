"""Analytic first-order soft/rapidity overlap and exclusive route identity."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError
from ...formal.maps import MapClass


class SoftRoute(str, Enum):
    BOUNDARY_ONLY_RESCATTERING = "BOUNDARY_ONLY_RESCATTERING"
    JOINT_MICROSCOPIC_SOFT_SECTOR = "JOINT_MICROSCOPIC_SOFT_SECTOR"


@dataclass(frozen=True)
class RapidityRegulatorSpec:
    stable_id: str = "C6:REG:ANALYTIC_DELTA"
    logarithm_symbol: str = "L_RAP"
    physical_scheme: str = "NOT_ASSIGNED"


@dataclass(frozen=True)
class SoftOverlapRegion:
    stable_id: str
    collinear_ancestor: str
    soft_ancestor: str
    mode_region: str
    coefficient: complex


@dataclass(frozen=True)
class AnalyticSoftOverlap:
    finite_unsubtracted: complex
    overlap: SoftOverlapRegion
    color_channel: str
    polarization: str
    route: SoftRoute = SoftRoute.BOUNDARY_ONLY_RESCATTERING
    map_class: MapClass = MapClass.MATCH
    stable_id: str = "C6:MATCH:ANALYTIC_HALF_SOFT"

    def evaluated(self, rapidity_log: float, subtraction_count: int = 1) -> complex:
        if subtraction_count not in (0, 1, 2):
            raise ArchitectureError("C6.SOFT.2", "unsupported half-soft subtraction multiplicity", expected="0,1,2", received=subtraction_count)
        unsubtracted = self.finite_unsubtracted + self.overlap.coefficient * rapidity_log
        soft_first_order = 2 * self.overlap.coefficient * rapidity_log
        return unsubtracted - subtraction_count * 0.5 * soft_first_order

    def rapidity_derivative(self, subtraction_count: int = 1) -> complex:
        return (1 - subtraction_count) * self.overlap.coefficient

    def to_dict(self) -> dict[str, object]:
        return {
            "stable_id": self.stable_id,
            "finite_unsubtracted": [self.finite_unsubtracted.real, self.finite_unsubtracted.imag],
            "overlap": {
                **asdict(self.overlap),
                "coefficient": [self.overlap.coefficient.real, self.overlap.coefficient.imag],
            },
            "color_channel": self.color_channel,
            "polarization": self.polarization,
            "route": self.route.value,
            "map_class": self.map_class.value,
            "uv_finite_matching": "UNRESOLVED_NOT_ZERO",
        }


class SoftRouteSelector:
    @staticmethod
    def select(routes: tuple[SoftRoute, ...], *, overlap_matching_map: str | None = None) -> SoftRoute:
        if len(routes) != 1:
            raise ArchitectureError("C6.ROUTE.1", "boundary-only and joint-soft routes are mutually exclusive", expected="one route", received=tuple(item.value for item in routes))
        route = routes[0]
        if route == SoftRoute.JOINT_MICROSCOPIC_SOFT_SECTOR:
            raise ArchitectureError("C6.ROUTE.1", "joint microscopic soft route is not implemented in C6", expected=SoftRoute.BOUNDARY_ONLY_RESCATTERING.value, received=route.value)
        return route

    @staticmethod
    def transfer_to_cs_kernel(route: SoftRoute, overlap_matching_map: str | None = None) -> None:
        if route == SoftRoute.BOUNDARY_ONLY_RESCATTERING and not overlap_matching_map:
            raise ArchitectureError("C6.ROUTE.1", "boundary rescattering cannot enter a Collins-Soper kernel without overlap matching", expected="explicit overlap matching map", received=None)


def analytic_soft_benchmark(color_channel: str, polarization: str) -> AnalyticSoftOverlap:
    return AnalyticSoftOverlap(
        complex(0.3, 0.2),
        SoftOverlapRegion(
            "C6:OVERLAP:COLLINEAR_SOFT", "C6:UNSUB:ACTIVE_GLUON",
            "C6:SOFT:ONE_WILSON_ORDER", "SOFT_COLLINEAR_ZERO_BIN",
            complex(0.7, -0.1),
        ),
        color_channel, polarization,
    )
