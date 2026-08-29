"""Light-front smearing functions and collinear impulse convolution."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Mapping

import numpy as np

from .light_front import (
    InternalMomentum,
    LFNormalization,
    light_front_wave_function,
    nucleon_momentum_density,
)

PDFCallable = Callable[[int, float, float], float]


class ScalingVariable(str, Enum):
    """Longitudinal fraction used by the observable."""

    DEUTERON = "x_D"
    NUCLEON = "x_N"


@dataclass(frozen=True)
class LFSmearingQuadrature:
    """Gauss-Legendre representation of the one-nucleon LF smearing.

    The stored density uses the flat convention

        integral_0^1 dy integral d2p_T rho_U(y,p_T) = 1

    for each active nucleon. This is equivalent to absorbing the explicit
    measure/flux factors of Eq. (61) into the nuclear kernel.
    """

    y: np.ndarray
    y_weights: np.ndarray
    unpolarized: np.ndarray
    tensor: np.ndarray
    p_max: float
    radial_units: str = "fm^-1"

    def __post_init__(self) -> None:
        arrays = tuple(
            np.asarray(value, dtype=np.float64)
            for value in (self.y, self.y_weights, self.unpolarized, self.tensor)
        )
        if any(array.ndim != 1 for array in arrays):
            raise ValueError("smearing arrays must be one-dimensional")
        if len({len(array) for array in arrays}) != 1:
            raise ValueError("smearing arrays must have equal length")
        if not np.all(np.diff(arrays[0]) > 0.0):
            raise ValueError("y nodes must be strictly increasing")
        if np.any(arrays[1] <= 0.0):
            raise ValueError("quadrature weights must be positive")
        for name, array in zip(
            ("y", "y_weights", "unpolarized", "tensor"), arrays
        ):
            object.__setattr__(self, name, array)

    def unpolarized_norm(self) -> float:
        return float(np.dot(self.y_weights, self.unpolarized))

    def tensor_norm(self) -> float:
        return float(np.dot(self.y_weights, self.tensor))


def build_lf_smearing(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    p_max: float,
    n_y: int = 32,
    n_p: int = 36,
    n_phi: int = 24,
) -> LFSmearingQuadrature:
    """Integrate the forward LF helicity density over transverse momentum.

    All masses and momenta must share units. For AV18/CD-Bonn functions in
    fm^-1, use a nucleon mass in fm^-1.
    """

    if nucleon_mass <= 0.0 or p_max <= 0.0:
        raise ValueError("nucleon_mass and p_max must be positive")
    if min(n_y, n_p, n_phi) < 2:
        raise ValueError("quadrature orders must be at least two")
    y_legendre, y_weights = np.polynomial.legendre.leggauss(n_y)
    y_nodes = 0.5 * (y_legendre + 1.0)
    y_weights = 0.5 * y_weights
    p_legendre, p_weights = np.polynomial.legendre.leggauss(n_p)
    p_nodes = 0.5 * p_max * (p_legendre + 1.0)
    p_weights = 0.5 * p_max * p_weights
    phi_nodes = TWO_PI * np.arange(n_phi, dtype=np.float64) / n_phi
    phi_weight = TWO_PI / n_phi

    unpolarized = np.zeros(n_y, dtype=np.float64)
    tensor = np.zeros(n_y, dtype=np.float64)
    for y_index, y in enumerate(y_nodes):
        for p_t, p_weight in zip(p_nodes, p_weights):
            radial_measure = p_weight * p_t
            for phi in phi_nodes:
                wave = light_front_wave_function(
                    y=float(y),
                    p_x=float(p_t * np.cos(phi)),
                    p_y=float(p_t * np.sin(phi)),
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                )
                density = nucleon_momentum_density(wave)
                weight = radial_measure * phi_weight
                unpolarized[y_index] += weight * float(density.unpolarized().real)
                tensor[y_index] += weight * float(density.tensor_difference().real)
    return LFSmearingQuadrature(
        y=y_nodes,
        y_weights=y_weights,
        unpolarized=unpolarized,
        tensor=tensor,
        p_max=p_max,
    )


def build_lf_smearing_spherical(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    k_max: float,
    n_k: int = 48,
    n_cos_theta: int = 32,
    n_phi: int = 16,
) -> LFSmearingQuadrature:
    """Preferred quadrature using the normalized instant-form d3k measure.

    Each spherical internal-momentum node is mapped to
    ``y=(E+k_z)/(2E)``. Dividing the flat-LF density by ``dk_z/dy`` exactly
    cancels the Jacobian already included in the LF amplitude. This avoids the
    slow endpoint convergence of direct y integration.
    """

    if nucleon_mass <= 0.0 or k_max <= 0.0:
        raise ValueError("nucleon_mass and k_max must be positive")
    if min(n_k, n_cos_theta, n_phi) < 2:
        raise ValueError("quadrature orders must be at least two")
    k_legendre, k_weights = np.polynomial.legendre.leggauss(n_k)
    k_nodes = 0.5 * k_max * (k_legendre + 1.0)
    k_weights = 0.5 * k_max * k_weights
    cos_nodes, cos_weights = np.polynomial.legendre.leggauss(n_cos_theta)
    phi_nodes = TWO_PI * np.arange(n_phi, dtype=np.float64) / n_phi
    phi_weight = TWO_PI / n_phi

    samples: list[tuple[float, float, float, float]] = []
    for k, k_weight in zip(k_nodes, k_weights):
        radial_weight = k_weight * k**2
        for cos_theta, cos_weight in zip(cos_nodes, cos_weights):
            sin_theta = np.sqrt(max(0.0, 1.0 - cos_theta**2))
            p_t = k * sin_theta
            k_z = k * cos_theta
            internal = InternalMomentum.from_cartesian(
                k_z=float(k_z), p_x=float(p_t), p_y=0.0, mass=nucleon_mass
            )
            unpolarized = 0.0
            tensor = 0.0
            for phi in phi_nodes:
                wave = light_front_wave_function(
                    y=internal.y,
                    p_x=float(p_t * np.cos(phi)),
                    p_y=float(p_t * np.sin(phi)),
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                )
                density = nucleon_momentum_density(wave)
                unpolarized += phi_weight * float(density.unpolarized().real)
                tensor += phi_weight * float(density.tensor_difference().real)
            inverse_jacobian = 1.0 / internal.dkz_dy
            samples.append(
                (
                    internal.y,
                    radial_weight * cos_weight,
                    unpolarized * inverse_jacobian,
                    tensor * inverse_jacobian,
                )
            )
    samples.sort(key=lambda item: item[0])
    array = np.asarray(samples, dtype=np.float64)
    return LFSmearingQuadrature(
        y=array[:, 0],
        y_weights=array[:, 1],
        unpolarized=array[:, 2],
        tensor=array[:, 3],
        p_max=k_max,
    )


def impulse_convolution(
    *,
    x: float,
    scale: float,
    flavor: int,
    proton_pdf: PDFCallable,
    neutron_pdf: PDFCallable,
    smearing: LFSmearingQuadrature,
    tensor: bool = False,
    scaling_variable: ScalingVariable = ScalingVariable.DEUTERON,
    per_nucleon: bool = False,
) -> float:
    """Collinear one-body convolution for proton plus neutron constituents."""

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    nuclear_density = smearing.tensor if tensor else smearing.unpolarized
    total = 0.0
    for y, weight, density in zip(smearing.y, smearing.y_weights, nuclear_density):
        constituent_fraction = y if scaling_variable == ScalingVariable.DEUTERON else 2.0 * y
        if constituent_fraction < x:
            continue
        z = x / constituent_fraction
        total += (
            weight
            * density
            / constituent_fraction
            * (proton_pdf(flavor, z, scale) + neutron_pdf(flavor, z, scale))
        )
    if per_nucleon:
        total *= 0.5
    return float(total)


def b1_leading_order(
    *,
    x: float,
    scale: float,
    flavors: tuple[int, ...],
    charges: Mapping[int, float],
    proton_pdf: PDFCallable,
    neutron_pdf: PDFCallable,
    smearing: LFSmearingQuadrature,
    scaling_variable: ScalingVariable = ScalingVariable.DEUTERON,
    per_nucleon: bool = False,
) -> float:
    """Equation (23) using positive flavor IDs and their negative antiparticles."""

    result = 0.0
    for flavor in flavors:
        if flavor <= 0:
            raise ValueError("flavors must contain positive quark PDG IDs")
        try:
            charge = charges[flavor]
        except KeyError as exc:
            raise KeyError(f"missing electric charge for flavor {flavor}") from exc
        quark = impulse_convolution(
            x=x,
            scale=scale,
            flavor=flavor,
            proton_pdf=proton_pdf,
            neutron_pdf=neutron_pdf,
            smearing=smearing,
            tensor=True,
            scaling_variable=scaling_variable,
            per_nucleon=per_nucleon,
        )
        antiquark = impulse_convolution(
            x=x,
            scale=scale,
            flavor=-flavor,
            proton_pdf=proton_pdf,
            neutron_pdf=neutron_pdf,
            smearing=smearing,
            tensor=True,
            scaling_variable=scaling_variable,
            per_nucleon=per_nucleon,
        )
        result += 0.5 * charge**2 * (quark + antiquark)
    return float(result)


# Imported late in the file to keep the mathematical convention visible above.
from .conventions import TWO_PI
