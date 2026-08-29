"""Flavor-resolved leading-twist spin-half nucleon quark correlators."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping

import numpy as np

from .gluon_correlator import EPSILON_T
from .gtmd import GaugeLink
from .provenance import ComponentProvenance, EvidenceClass
from .transverse_tensors import symmetric_traceless_2d

ScalarInput = Callable[[int, float, float], float]
MomentumTMDInput = Callable[[int, float, float, float], float]

NUCLEON_QUARK_TMD_NAMES = (
    "f1",
    "g1",
    "h1",
    "h1perp",
    "f1Tperp",
    "g1T",
    "h1Lperp",
    "h1Tperp",
)


@dataclass(frozen=True)
class SpinHalfQuarkCorrelator:
    vector: np.ndarray
    axial: np.ndarray
    transverse: np.ndarray

    def __post_init__(self) -> None:
        vector = np.asarray(self.vector, dtype=np.complex128)
        axial = np.asarray(self.axial, dtype=np.complex128)
        transverse = np.asarray(self.transverse, dtype=np.complex128)
        if vector.shape != (2, 2) or axial.shape != (2, 2):
            raise ValueError("nucleon vector and axial projections must be 2x2")
        if transverse.shape != (2, 2, 2):
            raise ValueError("nucleon transversity projection must be (2,2,2)")
        object.__setattr__(self, "vector", vector)
        object.__setattr__(self, "axial", axial)
        object.__setattr__(self, "transverse", transverse)

    def require_hermitian(self, tolerance: float = 1.0e-12) -> None:
        for values in (self.vector, self.axial, *self.transverse):
            if not np.allclose(values, values.conj().T, atol=tolerance, rtol=0):
                raise ValueError("nucleon target-helicity correlator is not Hermitian")

    def quark_target_density_matrix(self) -> np.ndarray:
        """Return the joint target-helicity x quark-spin density matrix.

        The three stored Dirac projections are the coefficients of the quark
        Pauli basis. Positivity of this 4x4 matrix is the complete leading-
        twist spin-half positivity condition at a fixed phase-space point.
        """

        self.require_hermitian()
        identity = np.eye(2, dtype=np.complex128)
        pauli = (
            np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128),
            np.asarray(((0.0, -1j), (1j, 0.0)), dtype=np.complex128),
            np.asarray(((1.0, 0.0), (0.0, -1.0)), dtype=np.complex128),
        )
        density = np.kron(self.vector, identity)
        density += np.kron(self.axial, pauli[2])
        density += np.kron(self.transverse[0], pauli[0])
        density += np.kron(self.transverse[1], pauli[1])
        density *= 0.5
        return density

    def minimum_positivity_eigenvalue(self) -> float:
        """Smallest Hermitian eigenvalue of the joint spin density."""

        return float(np.linalg.eigvalsh(self.quark_target_density_matrix())[0])


@dataclass(frozen=True)
class NucleonTMDComponent:
    value: ScalarInput
    width_gev2: Mapping[int, float]
    provenance: ComponentProvenance
    momentum_value: MomentumTMDInput | None = None

    def width(self, flavor: int) -> float:
        try:
            width = float(self.width_gev2[flavor])
        except KeyError as exc:
            raise KeyError(f"no transverse width for flavor {flavor}") from exc
        if width <= 0.0:
            raise ValueError("transverse width must be positive")
        return width


@dataclass(frozen=True)
class FlavorResolvedNucleonQuarkModel:
    """Complete spin-half correlator with independently replaceable TMD inputs."""

    components: Mapping[str, NucleonTMDComponent]
    nucleon_mass_gev: float
    transfer_slope_gev2: float = 0.0
    auxiliary_provenance: tuple[ComponentProvenance, ...] = ()

    def __post_init__(self) -> None:
        missing = set(NUCLEON_QUARK_TMD_NAMES) - set(self.components)
        unknown = set(self.components) - set(NUCLEON_QUARK_TMD_NAMES)
        if missing or unknown:
            raise ValueError(
                f"complete nucleon basis required; missing={sorted(missing)}, "
                f"unknown={sorted(unknown)}"
            )
        if self.nucleon_mass_gev <= 0.0 or self.transfer_slope_gev2 < 0.0:
            raise ValueError("invalid nucleon mass or transfer slope")
        if any(
            not isinstance(item, ComponentProvenance)
            for item in self.auxiliary_provenance
        ):
            raise TypeError("auxiliary provenance entries must be ComponentProvenance")

    @staticmethod
    def _t_odd_sign(name: str, gauge_link: GaugeLink) -> float:
        if name not in ("h1perp", "f1Tperp"):
            return 1.0
        if gauge_link.incoming == "+" and gauge_link.outgoing == "+":
            return 1.0
        if gauge_link.incoming == "-" and gauge_link.outgoing == "-":
            return -1.0
        raise ValueError("mixed gauge links require an explicit process model")

    def tmd_values(
        self,
        *,
        flavor: int,
        x: float,
        k_x_gev: float,
        k_y_gev: float,
        scale_gev: float,
        gauge_link: GaugeLink,
    ) -> dict[str, float]:
        if not 0.0 < x <= 1.0 or scale_gev <= 0.0:
            raise ValueError("require 0<x<=1 and positive scale")
        k2 = k_x_gev**2 + k_y_gev**2
        result = {}
        for name, component in self.components.items():
            if component.momentum_value is None:
                width = component.width(flavor)
                profile_value = (
                    float(component.value(flavor, x, scale_gev))
                    * np.exp(-k2 / width)
                    / (np.pi * width)
                )
            else:
                profile_value = float(
                    component.momentum_value(
                        flavor, x, float(np.sqrt(k2)), scale_gev
                    )
                )
            result[name] = (
                self._t_odd_sign(name, gauge_link)
                * profile_value
            )
        return result

    def correlator(
        self,
        *,
        flavor: int,
        x: float,
        k_x_gev: float,
        k_y_gev: float,
        delta_x_gev: float,
        delta_y_gev: float,
        scale_gev: float,
        gauge_link: GaugeLink,
    ) -> SpinHalfQuarkCorrelator:
        values = self.tmd_values(
            flavor=flavor,
            x=x,
            k_x_gev=k_x_gev,
            k_y_gev=k_y_gev,
            scale_gev=scale_gev,
            gauge_link=gauge_link,
        )
        return compose_spin_half_quark_correlator(
            values=values,
            k_x_gev=k_x_gev,
            k_y_gev=k_y_gev,
            delta_x_gev=delta_x_gev,
            delta_y_gev=delta_y_gev,
            nucleon_mass_gev=self.nucleon_mass_gev,
            transfer_slope_gev2=self.transfer_slope_gev2,
        )
    def require_component_provenance(self) -> None:
        entries = [
            (name, component.provenance)
            for name, component in self.components.items()
        ]
        entries.extend(
            (component.name, component)
            for component in self.auxiliary_provenance
        )
        for name, provenance in entries:
            if provenance.evidence == EvidenceClass.UNCONSTRAINED:
                if "parameter" not in provenance.uncertainty_kind.lower():
                    raise ValueError(
                        f"{name} is unconstrained without parameter uncertainty"
                    )

    def projection_callable(
        self,
        projection: str,
        gauge_link: GaugeLink,
        momentum_unit_to_gev: float = 1.0,
    ) -> Callable[[int, float, float, float, float, float, float], np.ndarray]:
        """Adapt one Dirac projection to the nuclear convolution interface."""

        if projection not in ("gamma+", "gamma+gamma5", "transversity_x", "transversity_y"):
            raise ValueError("unknown quark operator projection")
        if momentum_unit_to_gev <= 0.0:
            raise ValueError("momentum unit conversion must be positive")

        def evaluate(
            flavor: int,
            x: float,
            k_x: float,
            k_y: float,
            delta_x: float,
            delta_y: float,
            scale: float,
        ) -> np.ndarray:
            correlator = self.correlator(
                flavor=flavor,
                x=x,
                k_x_gev=momentum_unit_to_gev * k_x,
                k_y_gev=momentum_unit_to_gev * k_y,
                delta_x_gev=momentum_unit_to_gev * delta_x,
                delta_y_gev=momentum_unit_to_gev * delta_y,
                scale_gev=scale,
                gauge_link=gauge_link,
            )
            if projection == "gamma+":
                return correlator.vector
            if projection == "gamma+gamma5":
                return correlator.axial
            index = 0 if projection.endswith("_x") else 1
            return correlator.transverse[index]

        return evaluate


def compose_spin_half_quark_correlator(
    *,
    values: Mapping[str, float],
    k_x_gev: float,
    k_y_gev: float,
    delta_x_gev: float,
    delta_y_gev: float,
    nucleon_mass_gev: float,
    transfer_slope_gev2: float = 0.0,
) -> SpinHalfQuarkCorrelator:
    """Compose operator matrices from a complete named TMD mapping."""

    missing = set(NUCLEON_QUARK_TMD_NAMES) - set(values)
    if missing:
        raise ValueError(f"missing nucleon TMD values: {sorted(missing)}")
    k = np.asarray((k_x_gev, k_y_gev), dtype=np.float64)
    k2 = symmetric_traceless_2d(k, 2)
    mass = nucleon_mass_gev
    identity = np.eye(2, dtype=np.complex128)
    sigma = (
        np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128),
        np.asarray(((0.0, 1j), (-1j, 0.0)), dtype=np.complex128),
        np.asarray(((1.0, 0.0), (0.0, -1.0)), dtype=np.complex128),
    )
    vector = values["f1"] * identity
    vector += values["f1Tperp"] * (
        k[1] * sigma[0] - k[0] * sigma[1]
    ) / mass
    axial = values["g1"] * sigma[2]
    axial += values["g1T"] * (
        k[0] * sigma[0] + k[1] * sigma[1]
    ) / mass
    transverse = np.zeros((2, 2, 2), dtype=np.complex128)
    epsilon_k = EPSILON_T @ k
    for operator_index in range(2):
        transverse[operator_index] += (
            values["h1perp"] * epsilon_k[operator_index] * identity / mass
        )
        transverse[operator_index] += values["h1"] * sigma[operator_index]
        transverse[operator_index] += (
            values["h1Lperp"] * k[operator_index] * sigma[2] / mass
        )
        for target_index in range(2):
            transverse[operator_index] -= (
                values["h1Tperp"]
                * k2[operator_index, target_index]
                * sigma[target_index]
                / mass**2
            )
    transfer = np.exp(
        -transfer_slope_gev2 * (delta_x_gev**2 + delta_y_gev**2)
    )
    result = SpinHalfQuarkCorrelator(
        transfer * vector, transfer * axial, transfer * transverse
    )
    result.require_hermitian()
    return result
