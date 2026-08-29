"""Forward rank-zero nuclear TMD convolution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from .light_front import (
    InternalMomentum,
    LFNormalization,
    active_nucleon_spin_density,
    light_front_wave_function,
    nucleon_momentum_density,
    project_active_nucleon_density,
)

TWO_PI = 2.0 * np.pi
BTMDCallable = Callable[[int, float, float, float], complex]
SpinBTMDCallable = Callable[[int, float, float, float], np.ndarray]


@dataclass(frozen=True)
class TransverseSmearingQuadrature:
    """Spherical-node representation retaining the nucleon transverse momentum."""

    y: np.ndarray
    p_x: np.ndarray
    p_y: np.ndarray
    weights: np.ndarray
    unpolarized: np.ndarray
    tensor: np.ndarray

    def __post_init__(self) -> None:
        arrays = tuple(
            np.asarray(value, dtype=np.float64)
            for value in (
                self.y,
                self.p_x,
                self.p_y,
                self.weights,
                self.unpolarized,
                self.tensor,
            )
        )
        if any(array.ndim != 1 for array in arrays):
            raise ValueError("transverse-smearing arrays must be one-dimensional")
        if len({len(array) for array in arrays}) != 1:
            raise ValueError("transverse-smearing arrays must have equal length")
        if np.any(arrays[3] <= 0.0):
            raise ValueError("quadrature weights must be positive")
        for name, array in zip(
            ("y", "p_x", "p_y", "weights", "unpolarized", "tensor"), arrays
        ):
            object.__setattr__(self, name, array)

    def norm(self, *, tensor: bool = False) -> float:
        density = self.tensor if tensor else self.unpolarized
        return float(np.dot(self.weights, density))


@dataclass(frozen=True)
class SpinTransverseSmearingQuadrature:
    """Forward nuclear kernel retaining the active nucleon's helicity matrix."""

    y: np.ndarray
    p_x: np.ndarray
    p_y: np.ndarray
    weights: np.ndarray
    unpolarized: np.ndarray
    tensor: np.ndarray

    def __post_init__(self) -> None:
        vectors = tuple(
            np.asarray(value, dtype=np.float64)
            for value in (self.y, self.p_x, self.p_y, self.weights)
        )
        matrices = tuple(
            np.asarray(value, dtype=np.complex128)
            for value in (self.unpolarized, self.tensor)
        )
        if any(array.ndim != 1 for array in vectors):
            raise ValueError("spin-smearing node arrays must be one-dimensional")
        if len({len(array) for array in vectors}) != 1:
            raise ValueError("spin-smearing node arrays must have equal length")
        if any(array.shape != (len(vectors[0]), 2, 2) for array in matrices):
            raise ValueError("spin densities must have shape (n,2,2)")
        if np.any(vectors[3] <= 0.0):
            raise ValueError("quadrature weights must be positive")
        for name, array in zip(("y", "p_x", "p_y", "weights"), vectors):
            object.__setattr__(self, name, array)
        for name, array in zip(("unpolarized", "tensor"), matrices):
            object.__setattr__(self, name, array)

    def scalar_view(self) -> TransverseSmearingQuadrature:
        """Trace active helicities to recover the earlier scalar kernel."""

        return TransverseSmearingQuadrature(
            y=self.y,
            p_x=self.p_x,
            p_y=self.p_y,
            weights=self.weights,
            unpolarized=np.trace(self.unpolarized, axis1=1, axis2=2).real,
            tensor=np.trace(self.tensor, axis1=1, axis2=2).real,
        )


def build_transverse_smearing_spherical(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    k_max: float,
    n_k: int = 36,
    n_cos_theta: int = 24,
    n_phi: int = 16,
) -> TransverseSmearingQuadrature:
    """Build the forward nuclear kernel with the normalized instant-form measure."""

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

    samples = []
    for k, k_weight in zip(k_nodes, k_weights):
        for cos_theta, cos_weight in zip(cos_nodes, cos_weights):
            sin_theta = np.sqrt(max(0.0, 1.0 - cos_theta**2))
            p_t = k * sin_theta
            internal = InternalMomentum.from_cartesian(
                k_z=float(k * cos_theta), p_x=float(p_t), p_y=0.0, mass=nucleon_mass
            )
            node_weight = k_weight * k**2 * cos_weight * phi_weight
            for phi in phi_nodes:
                p_x = float(p_t * np.cos(phi))
                p_y = float(p_t * np.sin(phi))
                wave = light_front_wave_function(
                    y=internal.y,
                    p_x=p_x,
                    p_y=p_y,
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                )
                density = nucleon_momentum_density(wave)
                samples.append(
                    (
                        internal.y,
                        p_x,
                        p_y,
                        node_weight,
                        float(density.unpolarized().real) / internal.dkz_dy,
                        float(density.tensor_difference().real) / internal.dkz_dy,
                    )
                )
    array = np.asarray(samples, dtype=np.float64)
    return TransverseSmearingQuadrature(
        y=array[:, 0],
        p_x=array[:, 1],
        p_y=array[:, 2],
        weights=array[:, 3],
        unpolarized=array[:, 4],
        tensor=array[:, 5],
    )


def build_spin_transverse_smearing_spherical(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    k_max: float,
    n_k: int = 36,
    n_cos_theta: int = 24,
    n_phi: int = 16,
) -> SpinTransverseSmearingQuadrature:
    """Build Eq. (82)'s active-nucleon spin-density kernel."""

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

    y_values = []
    p_x_values = []
    p_y_values = []
    weights = []
    unpolarized = []
    tensor = []
    for k, k_weight in zip(k_nodes, k_weights):
        for cos_theta, cos_weight in zip(cos_nodes, cos_weights):
            p_t = k * np.sqrt(max(0.0, 1.0 - cos_theta**2))
            internal = InternalMomentum.from_cartesian(
                k_z=float(k * cos_theta), p_x=float(p_t), p_y=0.0, mass=nucleon_mass
            )
            node_weight = k_weight * k**2 * cos_weight * phi_weight
            for phi in phi_nodes:
                p_x = float(p_t * np.cos(phi))
                p_y = float(p_t * np.sin(phi))
                wave = light_front_wave_function(
                    y=internal.y,
                    p_x=p_x,
                    p_y=p_y,
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                )
                active = active_nucleon_spin_density(wave)
                inverse_jacobian = 1.0 / internal.dkz_dy
                y_values.append(internal.y)
                p_x_values.append(p_x)
                p_y_values.append(p_y)
                weights.append(node_weight)
                unpolarized.append(
                    inverse_jacobian
                    * project_active_nucleon_density(active, target_channel="U")
                )
                tensor.append(
                    inverse_jacobian
                    * project_active_nucleon_density(active, target_channel="LL")
                )
    return SpinTransverseSmearingQuadrature(
        y=np.asarray(y_values),
        p_x=np.asarray(p_x_values),
        p_y=np.asarray(p_y_values),
        weights=np.asarray(weights),
        unpolarized=np.asarray(unpolarized),
        tensor=np.asarray(tensor),
    )


def rank_zero_tmd_bspace(
    *,
    x: float,
    scale: float,
    flavor: int,
    b_x: float,
    b_y: float,
    proton_tmd: BTMDCallable,
    neutron_tmd: BTMDCallable,
    smearing: TransverseSmearingQuadrature,
    tensor: bool = False,
) -> complex:
    """Equation (84), in the deuteron-target x convention.

    The nucleon input is the Fourier transform
    ``F_tilde(flavor, z, b, scale)`` with ``b=sqrt(b_x**2+b_y**2)``.
    """

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    density = smearing.tensor if tensor else smearing.unpolarized
    b = float(np.hypot(b_x, b_y))
    result = 0.0j
    nucleon_cache: dict[float, complex] = {}
    for y, p_x, p_y, weight, nuclear_density in zip(
        smearing.y,
        smearing.p_x,
        smearing.p_y,
        smearing.weights,
        density,
    ):
        if y < x:
            continue
        z = x / y
        cache_key = float(y)
        nucleon = nucleon_cache.get(cache_key)
        if nucleon is None:
            nucleon = proton_tmd(flavor, z, b, scale) + neutron_tmd(
                flavor, z, b, scale
            )
            nucleon_cache[cache_key] = nucleon
        phase = np.exp(1j * z * (b_x * p_x + b_y * p_y))
        result += (
            weight
            * nuclear_density
            * phase
            * nucleon
            / y
        )
    return complex(result)


def spin_density_tmd_bspace(
    *,
    x: float,
    scale: float,
    flavor: int,
    b_x: float,
    b_y: float,
    proton_tmd: SpinBTMDCallable,
    neutron_tmd: SpinBTMDCallable,
    smearing: SpinTransverseSmearingQuadrature,
    tensor: bool = False,
) -> complex:
    """Eq. (81)/(82) with the full active-nucleon helicity contraction."""

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    density = smearing.tensor if tensor else smearing.unpolarized
    b = float(np.hypot(b_x, b_y))
    result = 0.0j
    correlator_cache: dict[float, np.ndarray] = {}
    for y, p_x, p_y, weight, spin_density in zip(
        smearing.y,
        smearing.p_x,
        smearing.p_y,
        smearing.weights,
        density,
    ):
        if y < x:
            continue
        z = x / y
        cache_key = float(y)
        correlator = correlator_cache.get(cache_key)
        if correlator is None:
            correlator = np.asarray(
                proton_tmd(flavor, z, b, scale)
                + neutron_tmd(flavor, z, b, scale),
                dtype=np.complex128,
            )
            if correlator.shape != (2, 2):
                raise ValueError("nucleon spin TMD must return a 2x2 matrix")
            correlator_cache[cache_key] = correlator
        phase = np.exp(1j * z * (b_x * p_x + b_y * p_y))
        result += (
            weight
            * phase
            * np.einsum("ab,ba->", spin_density, correlator)
            / y
        )
    return complex(result)
