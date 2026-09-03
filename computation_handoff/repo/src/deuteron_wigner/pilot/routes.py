"""Typed regulated common-parent routes for the C4 analytic pilot."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from math import exp, gamma, pi

import numpy as np

from ..formal.diagnostics import ArchitectureError
from ..formal.maps import MapClass
from ..gtmd import Species


class MatchingStatus(str, Enum):
    REGULATED_ANALYTIC = "REGULATED_ANALYTIC"
    IDENTITY_VALIDATION_ADAPTER = "IDENTITY_VALIDATION_ADAPTER"
    LINK_SHORTENING_REQUIRED = "LINK_SHORTENING_REQUIRED"
    UV_MATCHING_REQUIRED = "UV_MATCHING_REQUIRED"
    RAPIDITY_SOFT_MATCHING_REQUIRED = "RAPIDITY_SOFT_MATCHING_REQUIRED"
    NOT_PHYSICAL_QCD_OBJECT = "NOT_PHYSICAL_QCD_OBJECT"


class MellinConvention(str, Enum):
    QUARK_VECTOR_NET = "INT_DX_HQ_MINUS_HQBAR"
    QUARK_MOMENTUM = "INT_DX_X_HQ_PLUS_HQBAR"
    GLUON_EMT_XG = "INT_DX_HG_WHERE_HG_EQUALS_XG"


class GluonPolarizationProjector(str, Enum):
    TRACE_UNPOLARIZED = "TRACE_UNPOLARIZED"
    ANTISYMMETRIC_HELICITY = "ANTISYMMETRIC_HELICITY"
    SYMMETRIC_TRACELESS_LINEAR = "SYMMETRIC_TRACELESS_LINEAR"


def project_gluon_polarization(
    matrix: np.ndarray, projector: GluonPolarizationProjector,
):
    value = np.asarray(matrix, complex)
    if value.shape != (2, 2):
        raise ArchitectureError(
            "C4.GLUON.PROJECTOR", "gluon transverse matrix must be 2x2",
            expected=(2, 2), received=value.shape,
        )
    if projector == GluonPolarizationProjector.TRACE_UNPOLARIZED:
        return complex(np.trace(value))
    if projector == GluonPolarizationProjector.ANTISYMMETRIC_HELICITY:
        epsilon = np.asarray(((0, 1), (-1, 0)), complex)
        return complex(1j * np.einsum("ij,ij->", epsilon, value))
    symmetric = 0.5 * (value + value.T)
    return symmetric - 0.5 * np.eye(2) * np.trace(symmetric)


@dataclass(frozen=True)
class RouteResiduals:
    state_model: float = 0.0
    matching_status: float = 0.0
    quadrature: float = 0.0
    discretization_interpolation: float = 0.0
    floating_point: float = 0.0

    def maximum(self) -> float:
        return max(abs(value) for value in asdict(self).values())


@dataclass(frozen=True)
class RegulatedParent:
    """Factorized analytic overlap used solely to test reduction commutation."""

    stable_id: str
    species: Species
    flavor: str
    sector_id: str
    operator_id: str
    path_id: str
    active_slot_id: str
    coefficient: float
    alpha: float
    beta: float
    transverse_width_gev: float
    transfer_slope_gev2: float
    stored_scalar: str
    ordered_link_identity: tuple[str, ...] = (
        "0", "staple-infinity", "xi", "transverse-closure"
    )
    color_status: str = "NOT_APPLICABLE"
    overlap_evaluator_id: str = "C3:COMMON_DIAGONAL_OVERLAP"
    recoil_id: str = "SYMMETRIC_XI0"
    wilson_order: int = 0
    matching_status: MatchingStatus = MatchingStatus.REGULATED_ANALYTIC
    map_class: MapClass = MapClass.AMP
    status: str = "VALIDATION_ONLY"
    version: int = 1

    def __post_init__(self) -> None:
        if self.coefficient < 0 or self.alpha < 0 or self.beta < 0:
            raise ArchitectureError(
                "C4.OVERLAP.PARENT", "invalid analytic parent parameters",
                expected="nonnegative coefficient/powers",
                received=(self.coefficient, self.alpha, self.beta),
            )
        if self.transverse_width_gev <= 0 or self.transfer_slope_gev2 < 0:
            raise ArchitectureError(
                "C4.OVERLAP.PARENT", "invalid analytic transverse parameters",
                expected="width>0,slope>=0",
                received=(self.transverse_width_gev, self.transfer_slope_gev2),
            )
        if self.wilson_order != 0:
            raise ArchitectureError(
                "C4.ZERO.WILSON", "C4 core is zeroth rescattering only",
                expected=0, received=self.wilson_order,
            )
        if self.species == Species.GLUON and self.stored_scalar != "H_G_EQUALS_XG":
            raise ArchitectureError(
                "C4.GLUON_LEDGER.MELLIN", "gluon parent must store H^g=xg",
                expected="H_G_EQUALS_XG", received=self.stored_scalar,
            )
        if self.species == Species.GLUON and (
            len(self.ordered_link_identity) != 2
            or self.color_status != "DIAGONAL_ADJOINT"
        ):
            raise ArchitectureError(
                "C4.GLUON.OPERATOR_IDENTITY",
                "diagonal gluon parent needs an ordered link pair and color status",
                expected="two ordered links and DIAGONAL_ADJOINT",
                received=(self.ordered_link_identity, self.color_status),
            )

    def _longitudinal(self, x: float) -> float:
        if not 0 <= x <= 1 or self.coefficient == 0:
            return 0.0
        normalization = gamma(self.alpha + self.beta + 2) / (
            gamma(self.alpha + 1) * gamma(self.beta + 1)
        )
        return self.coefficient * normalization * x**self.alpha * (1 - x)**self.beta

    def value(self, x: float, kx: float, ky: float, dx: float, dy: float) -> float:
        width2 = self.transverse_width_gev**2
        transverse = exp(-(kx * kx + ky * ky) / width2) / (pi * width2)
        transfer = exp(-self.transfer_slope_gev2 * (dx * dx + dy * dy))
        return self._longitudinal(x) * transverse * transfer

    def promote_to_production(self):
        raise ArchitectureError(
            "C4.ISOLATE.PROMOTION", "C4 analytic parent cannot enter production",
            expected="VALIDATION_ONLY", received="production request",
        )


@dataclass(frozen=True)
class RouteResult:
    stable_id: str
    route: tuple[str, ...]
    parent_id: str
    species: Species
    flavor: str
    value: float
    transfer: tuple[float, float]
    matching_status: MatchingStatus
    required_matching: tuple[MatchingStatus, ...]
    operator_id: str
    path_id: str
    stored_scalar: str
    mellin_convention: MellinConvention | None
    residuals: RouteResiduals
    status: str = "VALIDATION_ONLY"
    version: int = 1


class CommonReductionRoutes:
    """One typed route authority for TMD, regulated GPD, PDF, and moments."""

    stable_id = "C4:COMMON_REGULATED_REDUCTION_ROUTES"
    combined_tolerance = 2e-12

    @staticmethod
    def _require_validation(parent: RegulatedParent) -> None:
        if parent.matching_status != MatchingStatus.REGULATED_ANALYTIC:
            raise ArchitectureError(
                "C4.MATCHING_STATUS", "route lacks regulated analytic status",
                expected=MatchingStatus.REGULATED_ANALYTIC.value,
                received=parent.matching_status.value,
            )

    def tmd(self, parent: RegulatedParent, x: float, kx: float, ky: float, *, delta=(0.0, 0.0)) -> RouteResult:
        self._require_validation(parent)
        if delta != (0.0, 0.0):
            raise ArchitectureError(
                "C4.TMD_ROUTE.TRANSFER", "TMD route requires forward limit",
                expected=(0.0, 0.0), received=delta,
            )
        return self._result(
            parent, ("GTMD", "TMD_REG"),
            parent.value(x, kx, ky, 0, 0), delta,
            required_matching=(
                MatchingStatus.UV_MATCHING_REQUIRED,
                MatchingStatus.RAPIDITY_SOFT_MATCHING_REQUIRED,
            ),
        )

    def gpd(self, parent: RegulatedParent, x: float, delta=(0.0, 0.0)) -> RouteResult:
        self._require_validation(parent)
        value = parent._longitudinal(x) * exp(
            -parent.transfer_slope_gev2 * (delta[0] ** 2 + delta[1] ** 2)
        )
        return self._result(
            parent, ("GTMD", "REGULATED_GPD"), value, delta,
            required_matching=(
                MatchingStatus.LINK_SHORTENING_REQUIRED,
                MatchingStatus.UV_MATCHING_REQUIRED,
            ),
        )

    def pdf_from_tmd(self, parent: RegulatedParent, x: float) -> RouteResult:
        value = parent._longitudinal(x)
        return self._result(
            parent, ("GTMD", "TMD_REG", "PDF_REG"), value, (0.0, 0.0),
            required_matching=(
                MatchingStatus.LINK_SHORTENING_REQUIRED,
                MatchingStatus.UV_MATCHING_REQUIRED,
            ),
        )

    def pdf_from_gpd(self, parent: RegulatedParent, x: float) -> RouteResult:
        value = self.gpd(parent, x, (0.0, 0.0)).value
        return self._result(
            parent, ("GTMD", "REGULATED_GPD", "PDF_REG"), value,
            (0.0, 0.0),
            required_matching=(
                MatchingStatus.LINK_SHORTENING_REQUIRED,
                MatchingStatus.UV_MATCHING_REQUIRED,
            ),
        )

    def direct_double_integral(self, parent: RegulatedParent, delta=(0.0, 0.0)) -> RouteResult:
        value = parent.coefficient * exp(
            -parent.transfer_slope_gev2 * (delta[0] ** 2 + delta[1] ** 2)
        )
        return self._result(parent, ("GTMD", "DIRECT_X_K_INTEGRAL"), value, delta)

    def moment(
        self, parent: RegulatedParent, convention: MellinConvention,
        delta=(0.0, 0.0),
    ) -> RouteResult:
        if parent.species == Species.GLUON:
            if convention != MellinConvention.GLUON_EMT_XG:
                raise ArchitectureError(
                    "C4.CURRENT_ROUTE.GLUON_NUMBER",
                    "gluon vector-number current is undefined in this route",
                    expected=MellinConvention.GLUON_EMT_XG.value,
                    received=convention.value,
                )
            value = self.direct_double_integral(parent, delta).value
        else:
            if convention == MellinConvention.GLUON_EMT_XG:
                raise ArchitectureError(
                    "C4.CURRENT_ROUTE.MELLIN",
                    "gluon H^g=xg convention applied to quark",
                    expected="quark convention", received=convention.value,
                )
            if convention == MellinConvention.QUARK_VECTOR_NET:
                value = self.direct_double_integral(parent, delta).value
            else:
                mean_x = (parent.alpha + 1) / (parent.alpha + parent.beta + 2)
                value = self.direct_double_integral(parent, delta).value * mean_x
        return self._result(
            parent, ("GTMD", "REGULATED_GPD", "LOCAL_MOMENT"), value, delta,
            convention,
            required_matching=(
                MatchingStatus.LINK_SHORTENING_REQUIRED,
                MatchingStatus.UV_MATCHING_REQUIRED,
            ),
        )

    def numerical_gpd(
        self, parent: RegulatedParent, x: float, delta=(0.0, 0.0),
        *, points: int = 401, extent_widths: float = 7.0,
    ) -> RouteResult:
        axis = np.linspace(
            -extent_widths * parent.transverse_width_gev,
            extent_widths * parent.transverse_width_gev, points,
        )
        kx, ky = np.meshgrid(axis, axis, indexing="ij")
        values = np.vectorize(parent.value)(x, kx, ky, delta[0], delta[1])
        numeric = float(np.trapz(np.trapz(values, axis, axis=1), axis, axis=0))
        analytic = self.gpd(parent, x, delta).value
        residual = abs(numeric - analytic)
        return self._result(
            parent, ("GTMD", "NUMERICAL_REGULATED_GPD"), numeric, delta,
            residuals=RouteResiduals(quadrature=residual),
        )

    def close(self, parent: RegulatedParent, delta=(0.0, 0.0)) -> RouteResiduals:
        direct = self.direct_double_integral(parent, delta).value
        sequential = self.moment(
            parent,
            MellinConvention.GLUON_EMT_XG if parent.species == Species.GLUON
            else MellinConvention.QUARK_VECTOR_NET,
            delta,
        ).value
        residuals = RouteResiduals(floating_point=abs(direct - sequential))
        if residuals.maximum() > self.combined_tolerance:
            raise ArchitectureError(
                "C4.ROUTE_CLOSURE", "common-parent routes do not commute",
                expected=f"<={self.combined_tolerance}", received=asdict(residuals),
            )
        return residuals

    @staticmethod
    def reject_physical_promotion(status: MatchingStatus) -> None:
        raise ArchitectureError(
            "C4.MATCHING_STATUS.PHYSICAL",
            "regulated staple identity is not a physical QCD object",
            expected="explicit UV/rapidity/soft/link matching",
            received=status.value,
        )

    @staticmethod
    def _result(
        parent: RegulatedParent, route: tuple[str, ...], value: float,
        delta: tuple[float, float],
        convention: MellinConvention | None = None,
        residuals: RouteResiduals = RouteResiduals(),
        required_matching: tuple[MatchingStatus, ...] = (),
    ) -> RouteResult:
        return RouteResult(
            ":".join((parent.stable_id, *route)), route, parent.stable_id,
            parent.species, parent.flavor, float(value), tuple(delta),
            parent.matching_status, required_matching,
            parent.operator_id, parent.path_id,
            parent.stored_scalar, convention, residuals,
        )
