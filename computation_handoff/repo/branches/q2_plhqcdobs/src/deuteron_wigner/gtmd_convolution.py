"""Callable one-body nuclear GTMD convolution with retained nucleon spin."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable

import numpy as np

from .light_front import (
    InternalMomentum,
    LFNormalization,
    SpinRotation,
    off_forward_active_component_densities,
    off_forward_active_nucleon_density,
)
from .gluon_correlator import (
    GluonCorrelatorObservation,
    GluonTargetPolarization,
    TraceLinearTMDs,
    project_ll_gluon_correlator,
    project_longitudinal_gluon_correlator,
    project_polarized_gluon_correlators,
    project_unpolarized_gluon_correlator,
)
from .registry import TargetChannel
from .spin import HelicityMatrix, project_matrix, spin_one_basis

TWO_PI = 2.0 * np.pi
NucleonGTMD = Callable[
    [int, float, float, float, float, float, float], np.ndarray
]
NucleonCurrent = Callable[[float, float, float], np.ndarray]
NucleonGluonGTMD = Callable[
    [float, float, float, float, float, float], np.ndarray
]


class TransferMapping(str, Enum):
    """Transverse transfer assigned to the active nucleon correlator."""

    IDENTITY = "delta_N=delta_D"
    ACTIVE_FRACTION = "delta_N=y*delta_D"

    def nucleon_transfer(self, y: float, delta_x: float, delta_y: float) -> tuple[float, float]:
        if self == TransferMapping.IDENTITY:
            return delta_x, delta_y
        if self == TransferMapping.ACTIVE_FRACTION:
            return y * delta_x, y * delta_y
        raise ValueError(f"unsupported transfer mapping {self}")


@dataclass(frozen=True)
class OffForwardSpinQuadrature:
    """A fixed-Delta nuclear spectral kernel.

    ``spectral`` has index order
    ``(node,target_out,target_in,nucleon_out,nucleon_in)``.
    """

    y: np.ndarray
    p_x: np.ndarray
    p_y: np.ndarray
    weights: np.ndarray
    delta_x: float
    delta_y: float
    spectral: np.ndarray
    virtuality: np.ndarray | None = None

    def __post_init__(self) -> None:
        vectors = tuple(
            np.asarray(value, dtype=np.float64)
            for value in (self.y, self.p_x, self.p_y, self.weights)
        )
        spectral = np.asarray(self.spectral, dtype=np.complex128)
        virtuality = (
            np.zeros(len(vectors[0]), dtype=np.float64)
            if self.virtuality is None
            else np.asarray(self.virtuality, dtype=np.float64)
        )
        if any(array.ndim != 1 for array in vectors):
            raise ValueError("GTMD quadrature node arrays must be one-dimensional")
        if len({len(array) for array in vectors}) != 1:
            raise ValueError("GTMD quadrature node arrays must have equal length")
        if spectral.shape != (len(vectors[0]), 3, 3, 2, 2):
            raise ValueError("spectral must have shape (n,3,3,2,2)")
        if virtuality.shape != (len(vectors[0]),):
            raise ValueError("virtuality must have shape (n,)")
        if not np.isfinite(virtuality).all():
            raise ValueError("virtuality must be finite")
        if np.any(vectors[3] <= 0.0):
            raise ValueError("quadrature weights must be positive")
        for name, array in zip(("y", "p_x", "p_y", "weights"), vectors):
            object.__setattr__(self, name, array)
        object.__setattr__(self, "spectral", spectral)
        object.__setattr__(self, "virtuality", virtuality)


def spectator_on_shell_virtuality(
    k_squared: float,
    *,
    nucleon_mass: float,
    deuteron_mass: float,
) -> float:
    """Return ``(p_active^2-m_N^2)/m_N^2`` with an on-shell spectator."""

    if k_squared < 0.0 or nucleon_mass <= 0.0 or deuteron_mass <= 0.0:
        raise ValueError("masses must be positive and k_squared nonnegative")
    spectator_energy = np.sqrt(nucleon_mass**2 + k_squared)
    active_energy = deuteron_mass - spectator_energy
    active_mass_squared = active_energy**2 - k_squared
    return float(
        (active_mass_squared - nucleon_mass**2) / nucleon_mass**2
    )


def build_off_forward_spin_quadrature(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    k_max: float,
    k_min: float = 0.0,
    delta_x: float,
    delta_y: float,
    n_k: int = 24,
    n_cos_theta: int = 16,
    n_phi: int = 12,
    deuteron_mass: float | None = None,
) -> OffForwardSpinQuadrature:
    """Build the off-forward spectral kernel using spherical internal nodes."""

    if nucleon_mass <= 0.0 or k_max <= 0.0:
        raise ValueError("nucleon_mass and k_max must be positive")
    if k_min < 0.0 or k_min >= k_max:
        raise ValueError("k_min must satisfy 0 <= k_min < k_max")
    if min(n_k, n_cos_theta, n_phi) < 2:
        raise ValueError("quadrature orders must be at least two")
    k_legendre, k_weights = np.polynomial.legendre.leggauss(n_k)
    k_nodes = 0.5 * (
        (k_max - k_min) * k_legendre + k_max + k_min
    )
    k_weights = 0.5 * (k_max - k_min) * k_weights
    cos_nodes, cos_weights = np.polynomial.legendre.leggauss(n_cos_theta)
    phi_nodes = TWO_PI * np.arange(n_phi, dtype=np.float64) / n_phi
    phi_weight = TWO_PI / n_phi
    y_values = []
    p_x_values = []
    p_y_values = []
    weights = []
    spectral = []
    virtuality = []
    target_mass = (
        float(deuteron_mass) if deuteron_mass is not None else 2.0 * nucleon_mass
    )
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
                overlap = off_forward_active_nucleon_density(
                    y=internal.y,
                    p_x=p_x,
                    p_y=p_y,
                    delta_x=delta_x,
                    delta_y=delta_y,
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                )
                y_values.append(internal.y)
                p_x_values.append(p_x)
                p_y_values.append(p_y)
                weights.append(node_weight)
                spectral.append(overlap / internal.dkz_dy)
                virtuality.append(spectator_on_shell_virtuality(
                    float(k**2),
                    nucleon_mass=nucleon_mass,
                    deuteron_mass=target_mass,
                ))
    return OffForwardSpinQuadrature(
        y=np.asarray(y_values),
        p_x=np.asarray(p_x_values),
        p_y=np.asarray(p_y_values),
        weights=np.asarray(weights),
        delta_x=delta_x,
        delta_y=delta_y,
        spectral=np.asarray(spectral),
        virtuality=np.asarray(virtuality),
    )


def build_off_forward_component_quadratures(
    *,
    radial: Callable[[float], tuple[float, float]],
    nucleon_mass: float,
    k_max: float,
    delta_x: float,
    delta_y: float,
    n_k: int = 24,
    n_cos_theta: int = 16,
    n_phi: int = 12,
    spin_rotation: SpinRotation = SpinRotation.MELOSH,
    deuteron_mass: float | None = None,
) -> dict[str, OffForwardSpinQuadrature]:
    """Build coherent SS, SD, DS, and DD versions of one quadrature."""

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
    spectral = {label: [] for label in ("SS", "SD", "DS", "DD")}
    virtuality = []
    target_mass = (
        float(deuteron_mass) if deuteron_mass is not None else 2.0 * nucleon_mass
    )
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
                components = off_forward_active_component_densities(
                    y=internal.y,
                    p_x=p_x,
                    p_y=p_y,
                    delta_x=delta_x,
                    delta_y=delta_y,
                    mass=nucleon_mass,
                    radial=radial,
                    normalization=LFNormalization.FLAT,
                    spin_rotation=spin_rotation,
                )
                y_values.append(internal.y)
                p_x_values.append(p_x)
                p_y_values.append(p_y)
                weights.append(node_weight)
                virtuality.append(spectator_on_shell_virtuality(
                    float(k**2),
                    nucleon_mass=nucleon_mass,
                    deuteron_mass=target_mass,
                ))
                for label in spectral:
                    spectral[label].append(components[label] / internal.dkz_dy)
    common = dict(
        y=np.asarray(y_values),
        p_x=np.asarray(p_x_values),
        p_y=np.asarray(p_y_values),
        weights=np.asarray(weights),
        delta_x=delta_x,
        delta_y=delta_y,
        virtuality=np.asarray(virtuality),
    )
    return {
        label: OffForwardSpinQuadrature(
            **common, spectral=np.asarray(component_spectral)
        )
        for label, component_spectral in spectral.items()
    }


def convolve_gtmd_point(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    flavor: int,
    proton_gtmd: NucleonGTMD,
    neutron_gtmd: NucleonGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> HelicityMatrix:
    """Evaluate Eq. (45)'s one-body term at one external phase-space point."""

    components = convolve_gtmd_components(
        x=x,
        k_x=k_x,
        k_y=k_y,
        scale=scale,
        flavor=flavor,
        proton_gtmd=proton_gtmd,
        neutron_gtmd=neutron_gtmd,
        quadrature=quadrature,
        transfer_mapping=transfer_mapping,
    )
    return HelicityMatrix(
        components["proton"].values + components["neutron"].values
    )


def convolve_gtmd_components(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    flavor: int,
    proton_gtmd: NucleonGTMD,
    neutron_gtmd: NucleonGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> dict[str, HelicityMatrix]:
    """Return proton and neutron one-body terms without early isoscalar collapse.

    Keeping the active-nucleon identity is essential for flavor tracing,
    tagged observables, controlled charge-symmetry breaking, and distinct
    proton/neutron off-shell corrections.
    """

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    result = {
        "proton": np.zeros((3, 3), dtype=np.complex128),
        "neutron": np.zeros((3, 3), dtype=np.complex128),
    }
    for y, p_x, p_y, weight, spectral in zip(
        quadrature.y,
        quadrature.p_x,
        quadrature.p_y,
        quadrature.weights,
        quadrature.spectral,
    ):
        if y < x:
            continue
        z = x / y
        parton_k_x = k_x - z * p_x
        parton_k_y = k_y - z * p_y
        delta_n_x, delta_n_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        correlators = {
            "proton": np.asarray(proton_gtmd(
                flavor,
                z,
                parton_k_x,
                parton_k_y,
                delta_n_x,
                delta_n_y,
                scale,
            ), dtype=np.complex128),
            "neutron": np.asarray(neutron_gtmd(
                flavor,
                z,
                parton_k_x,
                parton_k_y,
                delta_n_x,
                delta_n_y,
                scale,
            ), dtype=np.complex128),
        }
        for nucleon, correlator in correlators.items():
            if correlator.shape != (2, 2):
                raise ValueError("nucleon GTMD must return a 2x2 helicity matrix")
            result[nucleon] += (
                weight * np.einsum("IHca,ac->IH", spectral, correlator) / y
            )
    return {name: HelicityMatrix(values) for name, values in result.items()}


def convolve_local_current(
    *,
    scale: float,
    proton_current: NucleonCurrent,
    neutron_current: NucleonCurrent,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> HelicityMatrix:
    """The x- and k_T-integrated GTMD moment.

    The change of variables ``x=y z`` cancels the explicit ``1/y`` in
    Eq. (45), leaving the nuclear spectral overlap times the local nucleon
    current.
    """

    if scale <= 0.0:
        raise ValueError("scale must be positive")
    result = np.zeros((3, 3), dtype=np.complex128)
    for y, weight, spectral in zip(
        quadrature.y, quadrature.weights, quadrature.spectral
    ):
        delta_n_x, delta_n_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        current = np.asarray(
            proton_current(delta_n_x, delta_n_y, scale)
            + neutron_current(delta_n_x, delta_n_y, scale),
            dtype=np.complex128,
        )
        if current.shape != (2, 2):
            raise ValueError("nucleon current must return a 2x2 helicity matrix")
        result += weight * np.einsum("IHca,ac->IH", spectral, current)
    return HelicityMatrix(result)


def spin_half_collinear_gluon_correlator(
    unpolarized: float,
    helicity: float = 0.0,
) -> np.ndarray:
    """Collinear spin-1/2 nucleon gluon correlator.

    Index order is ``(nucleon_out,nucleon_in,gluon_i,gluon_j)``.  After
    transverse-momentum integration a spin-1/2 target has no
    symmetric-traceless gluon-index component and hence no collinear gluon
    double-helicity-flip distribution.
    """

    identity_h = np.eye(2, dtype=np.complex128)
    sigma_z = np.diag((1.0, -1.0)).astype(np.complex128)
    delta = np.eye(2, dtype=np.complex128)
    epsilon = np.asarray(((0.0, 1.0), (-1.0, 0.0)), dtype=np.complex128)
    return 0.5 * (
        float(unpolarized) * np.einsum("ac,ij->acij", identity_h, delta)
        + float(helicity)
        * np.einsum("ac,ij->acij", sigma_z, 1j * epsilon)
    )


def convolve_gluon_gtmd_point(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    proton_gtmd: NucleonGluonGTMD,
    neutron_gtmd: NucleonGluonGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> np.ndarray:
    """One-body convolution retaining target and gluon transverse indices.

    The returned index order is
    ``(deuteron_out,deuteron_in,gluon_i,gluon_j)``.
    """

    components = convolve_gluon_gtmd_components(
        x=x,
        k_x=k_x,
        k_y=k_y,
        scale=scale,
        proton_gtmd=proton_gtmd,
        neutron_gtmd=neutron_gtmd,
        quadrature=quadrature,
        transfer_mapping=transfer_mapping,
    )
    return components["proton"] + components["neutron"]


def convolve_gluon_gtmd_components(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    proton_gtmd: NucleonGluonGTMD,
    neutron_gtmd: NucleonGluonGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> dict[str, np.ndarray]:
    """Return proton and neutron gluon terms with both index pairs retained."""

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if scale <= 0.0:
        raise ValueError("scale must be positive")
    result = {
        "proton": np.zeros((3, 3, 2, 2), dtype=np.complex128),
        "neutron": np.zeros((3, 3, 2, 2), dtype=np.complex128),
    }
    for y, p_x, p_y, weight, spectral in zip(
        quadrature.y,
        quadrature.p_x,
        quadrature.p_y,
        quadrature.weights,
        quadrature.spectral,
    ):
        if y < x:
            continue
        z = x / y
        parton_k_x = k_x - z * p_x
        parton_k_y = k_y - z * p_y
        delta_n_x, delta_n_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        correlators = {
            "proton": np.asarray(proton_gtmd(
                z,
                parton_k_x,
                parton_k_y,
                delta_n_x,
                delta_n_y,
                scale,
            ), dtype=np.complex128),
            "neutron": np.asarray(neutron_gtmd(
                z,
                parton_k_x,
                parton_k_y,
                delta_n_x,
                delta_n_y,
                scale,
            ), dtype=np.complex128),
        }
        for nucleon, correlator in correlators.items():
            if correlator.shape != (2, 2, 2, 2):
                raise ValueError(
                    "nucleon gluon GTMD must have shape (2,2,2,2)"
                )
            result[nucleon] += weight * np.einsum(
                "IHca,acij->IHij", spectral, correlator
            ) / y
    return result


def convolve_gluon_gtmd_wave_components(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    proton_gtmd: NucleonGluonGTMD,
    neutron_gtmd: NucleonGluonGTMD,
    quadratures: dict[str, OffForwardSpinQuadrature],
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> dict[str, dict[str, np.ndarray]]:
    """Retain p/n and coherent SS, SD, DS, DD gluon contributions in one pass."""

    required = {"SS", "SD", "DS", "DD"}
    if set(quadratures) != required:
        raise ValueError(f"component quadratures must be exactly {sorted(required)}")
    reference = quadratures["SS"]
    for label, quadrature in quadratures.items():
        for name in ("y", "p_x", "p_y", "weights"):
            if not np.array_equal(getattr(reference, name), getattr(quadrature, name)):
                raise ValueError(f"{label} component does not share {name} nodes")
    result = {
        label: {
            nucleon: np.zeros((3, 3, 2, 2), dtype=np.complex128)
            for nucleon in ("proton", "neutron")
        }
        for label in required
    }
    for node, (y, p_x, p_y, weight) in enumerate(zip(
        reference.y, reference.p_x, reference.p_y, reference.weights
    )):
        if y < x:
            continue
        z = x / y
        parton_k_x = k_x - z * p_x
        parton_k_y = k_y - z * p_y
        delta_n_x, delta_n_y = transfer_mapping.nucleon_transfer(
            float(y), reference.delta_x, reference.delta_y
        )
        correlators = {
            "proton": np.asarray(proton_gtmd(
                z, parton_k_x, parton_k_y, delta_n_x, delta_n_y, scale
            ), dtype=np.complex128),
            "neutron": np.asarray(neutron_gtmd(
                z, parton_k_x, parton_k_y, delta_n_x, delta_n_y, scale
            ), dtype=np.complex128),
        }
        for nucleon, correlator in correlators.items():
            if correlator.shape != (2, 2, 2, 2):
                raise ValueError(
                    "nucleon gluon GTMD must have shape (2,2,2,2)"
                )
            for label, quadrature in quadratures.items():
                result[label][nucleon] += weight * np.einsum(
                    "IHca,acij->IHij",
                    quadrature.spectral[node],
                    correlator,
                ) / y
    return result


def project_deuteron_gluon_target_channel(
    correlator: np.ndarray,
    channel: str,
) -> np.ndarray:
    """Project a ``(3,3,2,2)`` correlator onto one spin-1 target channel."""

    values = np.asarray(correlator, dtype=np.complex128)
    if values.shape != (3, 3, 2, 2):
        raise ValueError("deuteron gluon correlator must have shape (3,3,2,2)")
    basis = spin_one_basis()
    if channel not in basis:
        raise ValueError(f"unknown spin-1 target channel {channel}")
    target_last = np.moveaxis(values, (0, 1), (-2, -1))
    return np.asarray(project_matrix(target_last, basis[channel]))


def project_deuteron_gluon_u_ll(
    correlator: np.ndarray,
    momentum: tuple[float, float] | np.ndarray,
    deuteron_mass: float,
) -> tuple[TraceLinearTMDs, TraceLinearTMDs]:
    """Project the U and physical LL gluon TMD pairs.

    The spin-one matrix basis coefficient obeys
    ``coefficient_LL=(2/3)*delta_T=-f1LL`` in the project's standard
    convention.  The explicit minus sign here is therefore the same
    convention adapter used by the collinear calculation.
    """

    unpolarized_matrix = project_deuteron_gluon_target_channel(
        correlator, "U"
    )
    ll_basis_coefficient = project_deuteron_gluon_target_channel(
        correlator, "LL"
    )
    unpolarized = project_unpolarized_gluon_correlator(
        unpolarized_matrix, momentum, deuteron_mass
    )
    ll = project_ll_gluon_correlator(
        -ll_basis_coefficient, momentum, deuteron_mass, 1.0
    )
    return unpolarized, ll


def project_deuteron_gluon_l_t_lt(
    correlator: np.ndarray,
    momentum: tuple[float, float] | np.ndarray,
    deuteron_mass: float,
) -> dict[str, dict[str, float]]:
    """Project the L, T, and LT target sectors from a deuteron correlator."""

    k = tuple(float(value) for value in np.asarray(momentum))
    phi_l = project_deuteron_gluon_target_channel(correlator, "L")
    g1, h1lperp = project_longitudinal_gluon_correlator(
        phi_l, k, deuteron_mass, 1.0
    )
    result: dict[str, dict[str, float]] = {
        "L": {"g1": g1, "h1Lperp": h1lperp}
    }
    for channel, prefix in (
        (TargetChannel.T, "T"),
        (TargetChannel.LT, "LT"),
    ):
        observations = []
        for suffix, vector in (("x", (1.0, 0.0)), ("y", (0.0, 1.0))):
            polarization = (
                GluonTargetPolarization(spin_transverse=vector)
                if channel == TargetChannel.T
                else GluonTargetPolarization(spin_lt=vector)
            )
            observations.append(
                GluonCorrelatorObservation(
                    momentum=k,
                    polarization=polarization,
                    correlator=project_deuteron_gluon_target_channel(
                        correlator, f"{prefix}_{suffix}"
                    ),
                )
            )
        result[channel.value] = project_polarized_gluon_correlators(
            channel, observations, deuteron_mass
        )
    return result


def project_deuteron_gluon_tt(
    correlator: np.ndarray,
    momentum: tuple[float, float] | np.ndarray,
    deuteron_mass: float,
) -> dict[str, float]:
    """Project the complete identifiable leading-twist TT gluon sector.

    A two-dimensional symmetric-traceless target tensor has two independent
    Cartesian components.  ``TT_x`` corresponds to
    ``diag(1,-1)`` and ``TT_y`` to the off-diagonal tensor with unit
    entries.  At fixed transverse momentum the correlator identifies
    ``f1TT-h1TTperp`` rather than the two functions separately; the returned
    name makes that exact two-dimensional degeneracy explicit.
    """

    k = tuple(float(value) for value in np.asarray(momentum))
    polarizations = {
        "TT_x": GluonTargetPolarization(
            spin_tt=((1.0, 0.0), (0.0, -1.0))
        ),
        "TT_y": GluonTargetPolarization(
            spin_tt=((0.0, 1.0), (1.0, 0.0))
        ),
    }
    observations = [
        GluonCorrelatorObservation(
            momentum=k,
            polarization=polarization,
            correlator=project_deuteron_gluon_target_channel(
                correlator, target_channel
            ),
        )
        for target_channel, polarization in polarizations.items()
    ]
    return project_polarized_gluon_correlators(
        TargetChannel.TT, observations, deuteron_mass
    )
