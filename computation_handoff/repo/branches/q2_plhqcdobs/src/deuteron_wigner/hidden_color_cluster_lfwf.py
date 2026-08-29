"""Effective two-cluster light-front state of arXiv:2507.09886.

This is a deep-binding cluster sensitivity model. It does not assign a
singlet-singlet/octet-octet probability.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import PchipInterpolator
from scipy.linalg import eigh


@dataclass(frozen=True)
class EffectiveClusterParameters:
    cluster_mass_gev: float = 0.838
    transverse_kappa_gev: float = 0.13
    longitudinal_g_gev: float = 0.50
    longitudinal_nodes: int = 320

    def __post_init__(self) -> None:
        if min(
            self.cluster_mass_gev,
            self.transverse_kappa_gev,
            self.longitudinal_g_gev,
        ) <= 0.0:
            raise ValueError("cluster parameters must be positive")
        if self.longitudinal_nodes < 40:
            raise ValueError("longitudinal_nodes must be at least 40")


@dataclass(frozen=True)
class LongitudinalTHooftSolution:
    z: np.ndarray
    weights: np.ndarray
    chi: np.ndarray
    mass_squared_gev2: float

    def __post_init__(self) -> None:
        if np.any(self.chi < 0.0):
            raise ValueError("ground-state longitudinal wave function must be positive")
        norm = float(np.dot(self.weights, self.chi**2))
        if abs(norm - 1.0) > 2.0e-10:
            raise ValueError("longitudinal solution is not normalized")

    def value(self, z: float | np.ndarray) -> float | np.ndarray:
        query = np.asarray(z, dtype=float)
        interpolator = PchipInterpolator(
            np.concatenate(([0.0], self.z, [1.0])),
            np.concatenate(([0.0], self.chi, [0.0])),
        )
        result = interpolator(query)
        result = np.where((query <= 0.0) | (query >= 1.0), 0.0, result)
        return float(result) if query.ndim == 0 else result


def solve_longitudinal_thooft(
    parameters: EffectiveClusterParameters = EffectiveClusterParameters(),
) -> LongitudinalTHooftSolution:
    """Solve the equal-mass principal-value 't Hooft equation.

    Gauss-Legendre collocation is transformed by ``sqrt(weight)`` so the
    discretized integral operator is explicitly self-adjoint.
    """

    nodes, weights = leggauss(parameters.longitudinal_nodes)
    z = (nodes + 1.0) / 2.0
    weights = weights / 2.0
    difference = z[:, None] - z[None, :]
    mask = ~np.eye(z.size, dtype=bool)
    coupling = parameters.longitudinal_g_gev**2 / np.pi
    hamiltonian = np.zeros((z.size, z.size), dtype=float)
    hamiltonian[mask] = (
        -coupling
        * np.sqrt(weights[:, None] * weights[None, :])[mask]
        / difference[mask] ** 2
    )
    diagonal_kernel = np.sum(
        np.where(mask, weights[None, :] / np.where(mask, difference**2, 1.0), 0.0),
        axis=1,
    )
    np.fill_diagonal(
        hamiltonian,
        parameters.cluster_mass_gev**2 / (z * (1.0 - z))
        + coupling * diagonal_kernel,
    )
    eigenvalues, eigenvectors = eigh(
        hamiltonian, subset_by_index=(0, 0), driver="evr"
    )
    weighted_wave = eigenvectors[:, 0]
    chi = weighted_wave / np.sqrt(weights)
    if np.dot(weights, chi) < 0.0:
        chi = -chi
    chi /= np.sqrt(np.dot(weights, chi**2))
    return LongitudinalTHooftSolution(
        z=z,
        weights=weights,
        chi=chi,
        mass_squared_gev2=float(eigenvalues[0]),
    )


@dataclass
class EffectiveClusterScalarLFWF:
    """Normalized L=0 holographic × 't Hooft scalar momentum wave function."""

    parameters: EffectiveClusterParameters = EffectiveClusterParameters()

    def __post_init__(self) -> None:
        self.longitudinal = solve_longitudinal_thooft(self.parameters)

    def amplitude(self, z: float, k_perp_gev: float) -> float:
        if not 0.0 < z < 1.0 or k_perp_gev < 0.0:
            return 0.0
        zbar = z * (1.0 - z)
        normalization = 4.0 * np.pi / self.parameters.transverse_kappa_gev
        return float(
            normalization
            * self.longitudinal.value(z)
            / np.sqrt(zbar)
            * np.exp(
                -k_perp_gev**2
                / (2.0 * self.parameters.transverse_kappa_gev**2 * zbar)
            )
        )

    @property
    def transverse_mass_squared_gev2(self) -> float:
        # Ground state n=L=0, J=1 of the source's holographic oscillator.
        return 2.0 * self.parameters.transverse_kappa_gev**2

    @property
    def total_mass_gev(self) -> float:
        return float(
            np.sqrt(
                self.longitudinal.mass_squared_gev2
                + self.transverse_mass_squared_gev2
            )
        )

    def analytic_norm(self) -> float:
        """Return ∫dz d²k/(16π³)|Psi|² using the Gaussian k integral."""

        longitudinal_norm = np.dot(
            self.longitudinal.weights, self.longitudinal.chi**2
        )
        return float(longitudinal_norm)


def melosh_rotation(
    momentum_fraction: float,
    kx_gev: float,
    ky_gev: float,
    constituent_mass_gev: float,
    free_mass_gev: float,
) -> np.ndarray:
    """Unitary canonical-spin to LF-helicity Melosh rotation.

    Rows are LF helicities ``(+,-)`` and columns are canonical spins
    ``(up,down)``.  The convention is
    ``R=(m+x M0-i sigma·(zhat×k_perp))/sqrt((m+x M0)^2+k_perp^2)``.
    """

    if not 0.0 < momentum_fraction < 1.0:
        raise ValueError("momentum fraction must lie in (0,1)")
    a = constituent_mass_gev + momentum_fraction * free_mass_gev
    k_right = kx_gev + 1j * ky_gev
    k_left = kx_gev - 1j * ky_gev
    denominator = np.sqrt(a * a + kx_gev**2 + ky_gev**2)
    return np.array([[a, -k_left], [k_right, a]], dtype=complex) / denominator


@dataclass
class EffectiveClusterSpinOneLFWF:
    """Canonical-triplet/Melosh diagnostic obtained from a scalar LF parent.

    The two equal-mass canonical cluster spins are coupled with exact
    spin-1 Clebsch--Gordan coefficients and independently transformed to LF
    helicity by unitary Melosh matrices.  Unlike the momentum-dependent
    vector-current vertex in arXiv:2507.09886, this unitary limiting case has
    equal pointwise total density for all target helicities and hence zero
    ``f1LL``.  It is retained as a diagnostic that a production spin vertex
    must distinguish, not as the paper's full spin construction.
    """

    scalar: EffectiveClusterScalarLFWF | None = None

    def __post_init__(self) -> None:
        if self.scalar is None:
            self.scalar = EffectiveClusterScalarLFWF()

    def free_mass_gev(self, z: float, k_perp_gev: float) -> float:
        m = self.scalar.parameters.cluster_mass_gev
        return float(np.sqrt((m * m + k_perp_gev**2) / (z * (1.0 - z))))

    @staticmethod
    def canonical_triplet(target_helicity: int) -> np.ndarray:
        """Return C[s1,s2] for |1,Lambda> in the up/down basis."""

        if target_helicity not in (-1, 0, 1):
            raise ValueError("target helicity must be -1, 0, or +1")
        coefficients = np.zeros((2, 2), dtype=complex)
        if target_helicity == 1:
            coefficients[0, 0] = 1.0
        elif target_helicity == -1:
            coefficients[1, 1] = 1.0
        else:
            coefficients[0, 1] = coefficients[1, 0] = 1.0 / np.sqrt(2.0)
        return coefficients

    def helicity_amplitudes(
        self, target_helicity: int, z: float, kx_gev: float, ky_gev: float
    ) -> np.ndarray:
        """Return Psi[active helicity,spectator helicity]."""

        k_perp = float(np.hypot(kx_gev, ky_gev))
        if not 0.0 < z < 1.0:
            return np.zeros((2, 2), dtype=complex)
        m = self.scalar.parameters.cluster_mass_gev
        m0 = self.free_mass_gev(z, k_perp)
        active = melosh_rotation(z, kx_gev, ky_gev, m, m0)
        spectator = melosh_rotation(1.0 - z, -kx_gev, -ky_gev, m, m0)
        canonical = self.canonical_triplet(target_helicity)
        return (
            active @ canonical @ spectator.T
            * self.scalar.amplitude(z, k_perp)
        )

    def helicity_density(
        self, target_helicity: int, active_helicity: int, z: float, k_perp_gev: float
    ) -> float:
        """Azimuth-independent density dP/(dz d²k) for active h=+1/-1."""

        if active_helicity not in (-1, 1):
            raise ValueError("active helicity must be -1 or +1")
        amplitudes = self.helicity_amplitudes(
            target_helicity, z, k_perp_gev, 0.0
        )
        row = 0 if active_helicity == 1 else 1
        return float(np.sum(np.abs(amplitudes[row, :]) ** 2) / (16.0 * np.pi**3))

    def leading_twist_tmds(self, z: float, k_perp_gev: float) -> dict[str, float]:
        """Project the diagnostic T-even subset f1, g1L, and f1LL.

        These are cluster momentum densities, not flavor PDFs.  Flavor enters
        only through a separately declared cluster-PDF convolution.
        """

        total = {}
        for lam in (-1, 0, 1):
            total[lam] = sum(
                self.helicity_density(lam, h, z, k_perp_gev) for h in (-1, 1)
            )
        p_plus_up = self.helicity_density(1, 1, z, k_perp_gev)
        p_plus_down = self.helicity_density(1, -1, z, k_perp_gev)
        return {
            "f1": (total[-1] + total[0] + total[1]) / 3.0,
            "g1L": p_plus_up - p_plus_down,
            "f1LL": total[0] - 0.5 * (total[1] + total[-1]),
        }


def _dirac_gamma_matrices() -> tuple[np.ndarray, ...]:
    """Return gamma^0,...,gamma^3 in the Dirac representation."""

    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex),
        np.array([[0.0, -1j], [1j, 0.0]], dtype=complex),
        np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
    )
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(np.block([[zero, sigma], [-sigma, zero]]) for sigma in pauli)
    return (gamma0, *spatial)


GAMMA = _dirac_gamma_matrices()
MINKOWSKI_METRIC = np.diag([1.0, -1.0, -1.0, -1.0])


def four_momentum_from_light_front(
    plus_gev: float, px_gev: float, py_gev: float, mass_gev: float
) -> np.ndarray:
    """Return contravariant (p0,px,py,p3), with p+ = p0+p3."""

    if plus_gev <= 0.0:
        raise ValueError("light-front plus momentum must be positive")
    minus = (mass_gev**2 + px_gev**2 + py_gev**2) / plus_gev
    return np.array(
        [(plus_gev + minus) / 2.0, px_gev, py_gev, (plus_gev - minus) / 2.0]
    )


def slash(vector: np.ndarray) -> np.ndarray:
    """Return gamma^mu vector_mu for a contravariant four-vector."""

    return (
        GAMMA[0] * vector[0]
        - GAMMA[1] * vector[1]
        - GAMMA[2] * vector[2]
        - GAMMA[3] * vector[3]
    )


def light_front_u_spinor(momentum: np.ndarray, helicity: int, mass_gev: float) -> np.ndarray:
    """Lepage--Brodsky on-shell u spinor, normalized to ubar u=2m."""

    if helicity not in (-1, 1):
        raise ValueError("helicity must be -1 or +1")
    plus = momentum[0] + momentum[3]
    right = momentum[1] + 1j * momentum[2]
    left = momentum[1] - 1j * momentum[2]
    if helicity == 1:
        components = [plus + mass_gev, right, plus - mass_gev, right]
    else:
        components = [-left, plus + mass_gev, left, -plus + mass_gev]
    return np.asarray(components, dtype=complex) / np.sqrt(2.0 * plus)


def light_front_v_spinor(momentum: np.ndarray, helicity: int, mass_gev: float) -> np.ndarray:
    """Charge-conjugate LF v basis, normalized to vbar v=-2m."""

    u = light_front_u_spinor(momentum, helicity, mass_gev)
    charge_conjugation = 1j * GAMMA[2] @ GAMMA[0]
    return charge_conjugation @ (u.conj().T @ GAMMA[0]).T


def spin_one_polarization(target_helicity: int) -> np.ndarray:
    """Rest-frame contravariant spin-1 polarization vector."""

    if target_helicity == 0:
        return np.array([0.0, 0.0, 0.0, 1.0], dtype=complex)
    if target_helicity == 1:
        return np.array([0.0, -1.0 / np.sqrt(2.0), -1j / np.sqrt(2.0), 0.0])
    if target_helicity == -1:
        return np.array([0.0, 1.0 / np.sqrt(2.0), -1j / np.sqrt(2.0), 0.0])
    raise ValueError("target helicity must be -1, 0, or +1")


@dataclass
class EffectiveClusterVectorCurrentLFWF:
    """Vector-current spin completion of the effective scalar cluster LFWF.

    Implements Eq. (8) of arXiv:2507.09886 literally as
    ``vbar/sqrt(1-z) gamma·epsilon u/sqrt(z) Psi_scalar``.  Longitudinal and
    transverse polarizations are normalized independently, as required when
    a phenomenological scalar radial state is dressed by the current vertex.
    """

    scalar: EffectiveClusterScalarLFWF | None = None
    normalization_nodes: int = 64

    def __post_init__(self) -> None:
        if self.scalar is None:
            self.scalar = EffectiveClusterScalarLFWF()
        if self.normalization_nodes < 32:
            raise ValueError("normalization_nodes must be at least 32")
        self._normalizations = {
            0: self._calculate_normalization(0),
            1: self._calculate_normalization(1),
        }

    def _raw_helicity_amplitudes(
        self, target_helicity: int, z: float, kx_gev: float, ky_gev: float
    ) -> np.ndarray:
        if not 0.0 < z < 1.0:
            return np.zeros((2, 2), dtype=complex)
        m = self.scalar.parameters.cluster_mass_gev
        target_mass = self.scalar.total_mass_gev
        active_momentum = four_momentum_from_light_front(
            z * target_mass, kx_gev, ky_gev, m
        )
        spectator_momentum = four_momentum_from_light_front(
            (1.0 - z) * target_mass, -kx_gev, -ky_gev, m
        )
        # The bound state is an incoming polarization ket, so the current
        # contraction carries epsilon*.  Omitting the conjugation swaps the
        # transverse helicity labels and reverses the source's g1L convention.
        vertex = slash(spin_one_polarization(target_helicity).conj())
        amplitudes = np.empty((2, 2), dtype=complex)
        for active_index, active_helicity in enumerate((1, -1)):
            u = light_front_u_spinor(active_momentum, active_helicity, m)
            for spectator_index, spectator_helicity in enumerate((1, -1)):
                v = light_front_v_spinor(spectator_momentum, spectator_helicity, m)
                vbar = v.conj().T @ GAMMA[0]
                amplitudes[active_index, spectator_index] = vbar @ vertex @ u
        return (
            amplitudes
            * self.scalar.amplitude(z, float(np.hypot(kx_gev, ky_gev)))
            / np.sqrt(z * (1.0 - z))
        )

    def _calculate_normalization(self, target_helicity: int) -> float:
        nodes, weights = leggauss(self.normalization_nodes)
        z_nodes = (nodes + 1.0) / 2.0
        z_weights = weights / 2.0
        # The scalar Gaussian is far below double precision at 1 GeV.
        k_nodes = (nodes + 1.0) / 2.0
        k_weights = weights / 2.0
        norm = 0.0
        for z, wz in zip(z_nodes, z_weights):
            for k, wk in zip(k_nodes, k_weights):
                amplitudes = self._raw_helicity_amplitudes(
                    target_helicity, float(z), float(k), 0.0
                )
                norm += (
                    wz
                    * wk
                    * 2.0
                    * np.pi
                    * k
                    * np.sum(np.abs(amplitudes) ** 2)
                    / (16.0 * np.pi**3)
                )
        return float(1.0 / np.sqrt(norm))

    def helicity_amplitudes(
        self, target_helicity: int, z: float, kx_gev: float, ky_gev: float
    ) -> np.ndarray:
        polarization_class = 0 if target_helicity == 0 else 1
        return (
            self._normalizations[polarization_class]
            * self._raw_helicity_amplitudes(
                target_helicity, z, kx_gev, ky_gev
            )
        )

    def helicity_density(
        self, target_helicity: int, active_helicity: int, z: float, k_perp_gev: float
    ) -> float:
        if active_helicity not in (-1, 1):
            raise ValueError("active helicity must be -1 or +1")
        amplitudes = self.helicity_amplitudes(
            target_helicity, z, k_perp_gev, 0.0
        )
        row = 0 if active_helicity == 1 else 1
        return float(np.sum(np.abs(amplitudes[row]) ** 2) / (16.0 * np.pi**3))

    def leading_twist_tmds(self, z: float, k_perp_gev: float) -> dict[str, float]:
        probabilities = {
            lam: {
                h: self.helicity_density(lam, h, z, k_perp_gev)
                for h in (-1, 1)
            }
            for lam in (-1, 0, 1)
        }
        totals = {
            lam: probabilities[lam][1] + probabilities[lam][-1]
            for lam in (-1, 0, 1)
        }
        return {
            "f1": sum(totals.values()) / 3.0,
            "g1L": probabilities[1][1] - probabilities[1][-1],
            "f1LL": totals[0] - 0.5 * (totals[1] + totals[-1]),
        }

    def collinear_lmdfs(
        self, z: float, quadrature_nodes: int = 80, k_max_gev: float = 1.0
    ) -> dict[str, float]:
        """Integrate the three source LMDFs over transverse momentum."""

        if quadrature_nodes < 24 or k_max_gev <= 0.0:
            raise ValueError("invalid transverse integration configuration")
        nodes, weights = leggauss(quadrature_nodes)
        momenta = k_max_gev * (nodes + 1.0) / 2.0
        radial_weights = k_max_gev * weights / 2.0
        result = {"f1": 0.0, "g1L": 0.0, "f1LL": 0.0}
        for momentum, weight in zip(momenta, radial_weights):
            projected = self.leading_twist_tmds(z, float(momentum))
            measure = weight * 2.0 * np.pi * momentum
            for name in result:
                result[name] += measure * projected[name]
        return result


class ClusterPDFProvider(Protocol):
    """Replaceable collinear parton input for the two effective clusters."""

    def proton(self, flavor: int, x: float, scale: float) -> float: ...

    def neutron(self, flavor: int, x: float, scale: float) -> float: ...


@dataclass
class EffectiveClusterLMDFGrid:
    """Cached interpolation of the three vector-current cluster LMDFs."""

    wave: EffectiveClusterVectorCurrentLFWF | None = None
    z_nodes: int = 161
    transverse_nodes: int = 64

    def __post_init__(self) -> None:
        if self.wave is None:
            self.wave = EffectiveClusterVectorCurrentLFWF(
                normalization_nodes=self.transverse_nodes
            )
        if self.z_nodes < 81:
            raise ValueError("z_nodes must be at least 81")
        self.z = np.linspace(0.002, 0.998, self.z_nodes)
        values = [
            self.wave.collinear_lmdfs(
                float(z), quadrature_nodes=self.transverse_nodes
            )
            for z in self.z
        ]
        self._interpolators = {
            name: PchipInterpolator(
                np.concatenate(([0.0], self.z, [1.0])),
                np.concatenate(
                    ([0.0], [entry[name] for entry in values], [0.0])
                ),
            )
            for name in ("f1", "g1L", "f1LL")
        }

    def value(self, name: str, z: float | np.ndarray) -> float | np.ndarray:
        if name not in self._interpolators:
            raise KeyError(f"unknown cluster LMDF {name}")
        query = np.asarray(z, dtype=float)
        result = self._interpolators[name](query)
        result = np.where((query <= 0.0) | (query >= 1.0), 0.0, result)
        return float(result) if query.ndim == 0 else result


@dataclass
class EffectiveClusterCollinearConvolution:
    """Flavor-resolved realization of Eq. (15) of arXiv:2507.09886.

    The source's factor one half and explicit proton-plus-neutron sum are
    retained.  ``f1`` and ``f1LL`` use the unpolarized cluster PDF input;
    ``g1L`` uses a separately supplied helicity PDF input.  No transverse
    cluster-parton profile is inferred by this collinear adapter.
    """

    unpolarized: ClusterPDFProvider
    polarized: ClusterPDFProvider
    lmdfs: EffectiveClusterLMDFGrid | None = None
    convolution_nodes: int = 72

    def __post_init__(self) -> None:
        if self.lmdfs is None:
            self.lmdfs = EffectiveClusterLMDFGrid()
        if self.convolution_nodes < 32:
            raise ValueError("convolution_nodes must be at least 32")

    def flavor_distribution(
        self, sector: str, flavor: int, x: float, scale_gev: float
    ) -> float:
        """Return F_flavor^D for sector ``f1``, ``g1L``, or ``f1LL``."""

        if sector not in ("f1", "g1L", "f1LL"):
            raise KeyError(f"unknown cluster convolution sector {sector}")
        if not 0.0 < x < 1.0:
            return 0.0
        if scale_gev <= 0.0:
            raise ValueError("scale must be positive")
        provider = self.polarized if sector == "g1L" else self.unpolarized
        lmdf_name = sector
        nodes, weights = leggauss(self.convolution_nodes)
        z = x + (1.0 - x) * (nodes + 1.0) / 2.0
        weights = weights * (1.0 - x) / 2.0
        result = 0.0
        for momentum_fraction, weight in zip(z, weights):
            cluster_x = x / momentum_fraction
            nucleon_average = 0.5 * (
                provider.proton(flavor, cluster_x, scale_gev)
                + provider.neutron(flavor, cluster_x, scale_gev)
            )
            result += (
                weight
                * self.lmdfs.value(lmdf_name, float(momentum_fraction))
                * nucleon_average
                / momentum_fraction
            )
        return float(result)

    @staticmethod
    def electric_charge_squared(flavor: int) -> float:
        absolute = abs(flavor)
        if absolute in (2, 4, 6):
            return 4.0 / 9.0
        if absolute in (1, 3, 5):
            return 1.0 / 9.0
        raise ValueError("flavor must be a quark or antiquark LHAPDF ID")

    def structure_function(
        self,
        sector: str,
        x: float,
        scale_gev: float,
        flavors: tuple[int, ...] = (2, 1, -2, -1, 3, -3),
    ) -> float:
        """Return the physical leading-order F2, x*g1, or x*b1.

        The unpolarized hard prefactor is one, while the helicity and tensor
        definitions carry one half.  The latter is required by the standard
        spin-1 convention and by the source's quoted b1 first moment, even
        though its compact Eq. (14) suppresses this sector distinction.
        """

        return float(
            x
            * (1.0 if sector == "f1" else 0.5)
            * sum(
                self.electric_charge_squared(flavor)
                * self.flavor_distribution(sector, flavor, x, scale_gev)
                for flavor in flavors
            )
        )


@dataclass
class EffectiveClusterTMDConvolution:
    """Flavor-resolved transverse cluster-motion correlator.

    This composes the source's vector-current LF wave function with the same
    proton/neutron collinear cluster PDFs as Eq. (15). It resolves transverse
    momentum generated by cluster motion while explicitly leaving intrinsic
    parton-in-cluster transverse momentum at its collinear boundary. That
    limitation is a replaceable convolution layer, not a Gaussian guess.
    """

    unpolarized: ClusterPDFProvider
    polarized: ClusterPDFProvider
    wave: EffectiveClusterVectorCurrentLFWF | None = None
    convolution_nodes: int = 72

    def __post_init__(self) -> None:
        if self.wave is None:
            self.wave = EffectiveClusterVectorCurrentLFWF()
        if self.convolution_nodes < 32:
            raise ValueError("cluster TMD convolution requires at least 32 nodes")

    def flavor_tmd(
        self,
        sector: str,
        flavor: int,
        x: float,
        k_perp_gev: float,
        scale_gev: float,
    ) -> float:
        if sector not in ("f1", "g1L", "f1LL"):
            raise KeyError(f"unknown cluster TMD sector {sector}")
        if not 0.0 < x < 1.0:
            return 0.0
        if k_perp_gev < 0.0 or scale_gev <= 0.0:
            raise ValueError("cluster TMD requires k>=0 and Q>0")
        provider = self.polarized if sector == "g1L" else self.unpolarized
        nodes, weights = leggauss(self.convolution_nodes)
        z_values = x + (1.0 - x) * (nodes + 1.0) / 2.0
        weights = weights * (1.0 - x) / 2.0
        result = 0.0
        for z, weight in zip(z_values, weights):
            cluster_x = x / z
            cluster_pdf = 0.5 * (
                provider.proton(flavor, cluster_x, scale_gev)
                + provider.neutron(flavor, cluster_x, scale_gev)
            )
            result += (
                weight
                * self.wave.leading_twist_tmds(
                    float(z), k_perp_gev
                )[sector]
                * cluster_pdf
                / z
            )
        return float(result)

    def correlator(
        self, flavor: int, x: float, k_perp_gev: float, scale_gev: float
    ):
        """Return the modeled non-nucleonic spin-1 quark correlator."""

        from .quark_correlator import Spin1QuarkCorrelator
        from .spin import diagonal_from_u_l_delta_t, spin_one_basis

        f1 = self.flavor_tmd("f1", flavor, x, k_perp_gev, scale_gev)
        g1 = self.flavor_tmd("g1L", flavor, x, k_perp_gev, scale_gev)
        f1ll = self.flavor_tmd("f1LL", flavor, x, k_perp_gev, scale_gev)
        return Spin1QuarkCorrelator(
            vector=diagonal_from_u_l_delta_t(f1, 0.0, f1ll).values,
            axial=g1 * spin_one_basis()["L"],
            transverse=np.zeros((2, 3, 3), dtype=np.complex128),
        )
