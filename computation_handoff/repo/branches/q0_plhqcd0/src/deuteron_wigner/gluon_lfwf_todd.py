"""Nucleon-level gluon T-odd correlator from LF overlap and eikonal phases.

This is the canonical in-project construction.  It does not import the
normalization of an external spectator model.  The real T-even nucleon
correlator supplies the helicity populations and linear-polarization
coherence.  A screened Wilson-line kernel supplies rank-n absorptive
harmonics.  Their interference is composed at the nucleon level *before*
the deuteron LF convolution.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.linalg import expm
from scipy.special import ive

from .gluon_correlator import (
    GluonTargetPolarization,
    compose_longitudinal_gluon_correlator,
    compose_polarized_gluon_correlator,
    project_longitudinal_gluon_correlator,
    project_unpolarized_gluon_correlator,
)
from .gluon_todd import GluonColorStructure, gluon_link_sign
from .gtmd import GaugeLink
from .registry import TargetChannel
from .spin import spin_one_basis


def _joint_matrix(values: np.ndarray) -> np.ndarray:
    return np.asarray(values).transpose(0, 2, 1, 3).reshape(4, 4)


def _tensor_from_joint(values: np.ndarray) -> np.ndarray:
    return np.asarray(values).reshape(2, 2, 2, 2).transpose(0, 2, 1, 3)


def project_spin_half_gluon_density_psd(
    values: np.ndarray, *, tolerance: float = 1.0e-12
) -> tuple[np.ndarray, float]:
    """Project a complete spin-half gluon parent to the positive cone.

    This is the explicit pre-W+Y completion for W-term nodes outside their
    probability-density domain. It clips negative *joint-density
    eigenvalues*, never individual TMD coefficients.
    """

    joint = _joint_matrix(values)
    if not np.allclose(joint, joint.conj().T, atol=tolerance, rtol=0):
        raise ValueError("cannot positivity-project a non-Hermitian gluon parent")
    eigenvalues, eigenvectors = np.linalg.eigh(joint)
    if eigenvalues[0] >= -tolerance:
        return np.asarray(values).copy(), 0.0
    removed = float(-np.sum(eigenvalues[eigenvalues < 0.0]))
    clipped = np.maximum(eigenvalues, 0.0)
    positive_trace = float(np.trace(joint).real)
    if positive_trace <= 0.0 or clipped.sum() <= 0.0:
        return np.zeros_like(values), removed
    clipped *= positive_trace / clipped.sum()
    projected = (eigenvectors * clipped) @ eigenvectors.conj().T
    return _tensor_from_joint(projected), removed


@dataclass(frozen=True)
class GluonWilsonLineKernel:
    """Screened adjoint eikonal harmonics with no TMD normalization knobs."""

    alpha_s: float = 0.30
    screening_mass_gev: float = 0.36
    remnant_scale_gev: float = 0.90
    q_max_gev: float = 3.5
    n_q: int = 48
    n_phi: int = 64

    def __post_init__(self) -> None:
        if min(
            self.alpha_s, self.screening_mass_gev,
            self.remnant_scale_gev, self.q_max_gev,
        ) <= 0.0:
            raise ValueError("Wilson-line kernel scales must be positive")
        if self.n_q < 20 or self.n_phi < 24:
            raise ValueError("Wilson-line quadrature is under-resolved")

    def harmonic(self, k_gev: float, width_gev2: float, rank: int) -> float:
        """Return the dimensionless absorptive rank-n overlap."""

        if k_gev < 0.0 or width_gev2 <= 0.0 or rank not in (1, 2, 3):
            raise ValueError("invalid Wilson-line harmonic request")
        if k_gev == 0.0:
            return 0.0
        nodes, weights = np.polynomial.legendre.leggauss(self.n_q)
        q = 0.5 * self.q_max_gev * (nodes + 1.0)
        wq = 0.5 * self.q_max_gev * weights
        argument = k_gev * q / width_gev2
        # exp(-(k²+q²)/2w) I_n(kq/w), evaluated with exponentially scaled
        # I_n to remain stable in the large-argument tail.
        angular = (
            np.exp(-((k_gev-q)**2) / (2.0*width_gev2))
            * ive(rank, argument)
        )
        propagator = 1.0 / (q*q + self.screening_mass_gev**2)
        remnant = (
            self.remnant_scale_gev**2
            / (self.remnant_scale_gev**2 + q*q)
        ) ** 2
        total = float(np.sum(wq * q * propagator * remnant * angular))
        # C_A=3.  The Fourier measure fixes the absolute model phase.
        return float(3.0 * self.alpha_s * total / (2.0 * np.pi))


@dataclass(frozen=True)
class LFWFGaugeLinkSpinHalfGluonGTMD:
    """Add four gluon T-odd structures to an existing nucleon LF parent.

    ``f1Tperp`` comes from the interference of aligned and anti-aligned
    target--gluon helicity populations. ``h1`` is the independent rank-one
    linear-gluon interference allowed already by the minimal helicity
    vertex. The rank-two and rank-three structures additionally require
    Pauli/spin-orbit coherence, represented by the T-even linear-polarization
    overlap. Consequently only those two disappear in the minimal-vertex
    controlled limit, matching the external spectator benchmark.
    """

    t_even_gtmd: object
    color: GluonColorStructure
    gauge_link: GaugeLink
    nucleon_mass_gev: float
    transverse_width_gev2: float
    momentum_unit_to_gev: float = 1.0
    kernel: GluonWilsonLineKernel = GluonWilsonLineKernel()
    d_type_vertex_ratio: float = 5.0 / 9.0
    transfer_tolerance: float = 1.0e-14
    positivity_safety: float = 0.95

    def __post_init__(self) -> None:
        if min(
            self.nucleon_mass_gev, self.transverse_width_gev2,
            self.momentum_unit_to_gev, self.d_type_vertex_ratio,
            self.positivity_safety,
        ) <= 0.0 or self.positivity_safety > 1.0:
            raise ValueError("invalid nucleon LF gluon T-odd configuration")
        gluon_link_sign(self.color, self.gauge_link)

    def _radial_values(
        self, base: np.ndarray, momentum_input: tuple[float, float]
    ) -> dict[str, float]:
        identity = np.eye(2, dtype=np.complex128)
        sigma_z = np.diag((1.0, -1.0)).astype(np.complex128)
        unpolarized = 0.5 * np.einsum("ac,acij->ij", identity, base)
        longitudinal = 0.5 * np.einsum("ac,acij->ij", sigma_z, base)
        mass_input = self.nucleon_mass_gev / self.momentum_unit_to_gev
        u = project_unpolarized_gluon_correlator(
            unpolarized, momentum_input, mass_input
        )
        l = project_longitudinal_gluon_correlator(
            longitudinal, momentum_input, mass_input, spin_longitudinal=1.0
        )
        f1 = max(0.0, float(u.trace))
        if f1 == 0.0:
            return {name: 0.0 for name in (
                "f1Tperp", "h1", "h1Lperp", "h1Tperp"
            )}
        g1 = float(l[0])
        h1perp = float(u.linear)
        # Overlap visibilities are bounded consequences of the density,
        # not adjustable TMD fractions.
        aligned = max(0.0, 0.5 * (f1 + g1))
        anti = max(0.0, 0.5 * (f1 - g1))
        helicity_visibility = (
            2.0 * math.sqrt(aligned * anti) / f1
        )
        k_gev = self.momentum_unit_to_gev * float(
            np.hypot(*momentum_input)
        )
        linear_visibility = min(
            1.0,
            abs(h1perp) * k_gev**2
            / (2.0 * self.nucleon_mass_gev**2 * f1 + 1.0e-300),
        )
        phase = {
            rank: self.kernel.harmonic(
                k_gev, self.transverse_width_gev2, rank
            )
            for rank in (1, 2, 3)
        }
        color = (
            1.0 if self.color == GluonColorStructure.F_TYPE
            else self.d_type_vertex_ratio
        )
        sign = gluon_link_sign(self.color, self.gauge_link)
        common = sign * color * f1
        return {
            "f1Tperp": common * helicity_visibility * phase[1],
            "h1": common * helicity_visibility * phase[1],
            "h1Lperp": (
                common * helicity_visibility * linear_visibility
                * phase[2]
            ),
            "h1Tperp": (
                common * np.sign(h1perp) * helicity_visibility
                * linear_visibility * phase[3]
            ),
        }

    def __call__(
        self,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        if np.hypot(delta_x, delta_y) > self.transfer_tolerance:
            raise ValueError(
                "forward Wilson-line model cannot be promoted to an "
                "off-forward GTMD without a staple-link transfer kernel"
            )
        base = np.asarray(
            self.t_even_gtmd(
                x, k_x, k_y, delta_x, delta_y, scale
            ),
            dtype=np.complex128,
        )
        if base.shape != (2, 2, 2, 2):
            raise ValueError("nucleon gluon parent must have shape (2,2,2,2)")
        base, _ = project_spin_half_gluon_density_psd(base)
        momentum = (float(k_x), float(k_y))
        radial = self._radial_values(base, momentum)
        mass_input = self.nucleon_mass_gev / self.momentum_unit_to_gev
        correction = np.zeros_like(base)
        sigma_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), complex)
        sigma_y = np.asarray(((0.0, -1j), (1j, 0.0)), complex)
        for sigma, spin in (
            (sigma_x, (1.0, 0.0)), (sigma_y, (0.0, 1.0))
        ):
            matrix = compose_polarized_gluon_correlator(
                TargetChannel.T,
                momentum,
                mass_input,
                GluonTargetPolarization(spin_transverse=spin),
                {
                    "f1Tperp": radial["f1Tperp"],
                    "g1T": 0.0,
                    "h1": radial["h1"],
                    "h1Tperp": radial["h1Tperp"],
                },
            )
            correction += np.einsum("ac,ij->acij", sigma, matrix)
        longitudinal = compose_longitudinal_gluon_correlator(
            momentum, mass_input, 1.0, g1=0.0,
            h1Lperp=radial["h1Lperp"],
        )
        correction += np.einsum(
            "ac,ij->acij", np.diag((1.0, -1.0)), longitudinal
        )

        def candidate(scale_value: float) -> np.ndarray:
            return base + scale_value * correction

        if np.linalg.eigvalsh(_joint_matrix(candidate(1.0)))[0] >= -1e-12:
            scale_value = 1.0
        else:
            low, high = 0.0, 1.0
            for _ in range(64):
                middle = 0.5 * (low + high)
                if np.linalg.eigvalsh(_joint_matrix(candidate(middle)))[0] >= 0.0:
                    low = middle
                else:
                    high = middle
            scale_value = self.positivity_safety * low
        result = candidate(scale_value)
        if not np.allclose(
            result, result.transpose(1, 0, 3, 2).conj(),
            atol=1e-11, rtol=0,
        ):
            raise ValueError("nucleon gluon LF correlator is not Hermitian")
        if np.linalg.eigvalsh(_joint_matrix(result))[0] < -1e-10:
            raise ValueError("nucleon gluon LF correlator violates positivity")
        return result


@dataclass(frozen=True)
class Spin1NuclearWilsonLine:
    """Apply the spin-1 nuclear part of the staple-link phase.

    The rank-one generator is the LT irrep contracted with k-hat; the
    rank-two generator is the TT irrep contracted with the rank-two
    direction of k. Their coefficients are the screened eikonal harmonics
    multiplied by the actual S--D coherence and D probability.  The
    transformation acts on retained target-helicity amplitudes and therefore
    preserves Hermiticity, trace, and full joint-density positivity.
    """

    color: GluonColorStructure
    gauge_link: GaugeLink
    d_state_probability: float
    sd_coherence: float
    kernel: GluonWilsonLineKernel = GluonWilsonLineKernel()
    transverse_width_gev2: float = 0.30
    d_type_vertex_ratio: float = 5.0 / 9.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.d_state_probability < 1.0:
            raise ValueError("D-state probability must lie in [0,1)")
        if not -1.0 <= self.sd_coherence <= 1.0:
            raise ValueError("S-D coherence must lie in [-1,1]")
        if self.transverse_width_gev2 <= 0.0 or self.d_type_vertex_ratio <= 0.0:
            raise ValueError("nuclear Wilson-line scales must be positive")
        gluon_link_sign(self.color, self.gauge_link)

    def phases(self, k_gev: float) -> tuple[float, float]:
        if k_gev < 0.0:
            raise ValueError("transverse momentum cannot be negative")
        channels = self.channel_phases(k_gev)
        return channels["S_D_rank1"], channels["D_D_rank2"]

    def channel_phases(self, k_gev: float) -> dict[str, float]:
        """Return non-overlapping nuclear orbital exponent channels."""

        if k_gev < 0.0:
            raise ValueError("transverse momentum cannot be negative")
        tensor_mix = (
            math.sqrt(
                self.d_state_probability*(1.0-self.d_state_probability)
            ) * self.sd_coherence
        )
        color = (
            1.0 if self.color == GluonColorStructure.F_TYPE
            else self.d_type_vertex_ratio
        )
        sign = gluon_link_sign(self.color, self.gauge_link)
        return {
            "S_D_rank1": sign*color*tensor_mix*self.kernel.harmonic(
                k_gev, self.transverse_width_gev2, 1
            ),
            "D_D_rank2": sign*color*self.d_state_probability*self.kernel.harmonic(
                k_gev, self.transverse_width_gev2, 2
            ),
        }

    def apply(
        self, correlator: np.ndarray, momentum_gev: tuple[float, float]
    ) -> np.ndarray:
        values = np.asarray(correlator, dtype=np.complex128)
        if values.shape != (3, 3, 2, 2):
            raise ValueError("spin-1 gluon parent must have shape (3,3,2,2)")
        k = float(np.hypot(*momentum_gev))
        if k == 0.0 or self.d_state_probability == 0.0:
            return values.copy()
        phi = math.atan2(momentum_gev[1], momentum_gev[0])
        target = spin_one_basis()
        generator_lt = (
            math.cos(phi)*target["LT_x"] + math.sin(phi)*target["LT_y"]
        )
        generator_tt = (
            math.cos(2.0*phi)*target["TT_x"]
            + math.sin(2.0*phi)*target["TT_y"]
        )
        phase_lt, phase_tt = self.phases(k)
        unitary = expm(1j*(phase_lt*generator_lt + phase_tt*generator_tt))
        result = np.einsum(
            "Aa,abij,Bb->ABij", unitary, values, unitary.conj()
        )
        input_is_hermitian = np.allclose(
            values, values.transpose(1, 0, 3, 2).conj(),
            atol=1e-11, rtol=0,
        )
        # Individual SD and DS interference ledgers are conjugate partners,
        # not separately Hermitian densities.  Their unitary images remain
        # valid linear components and are checked after SD+DS closure.
        if input_is_hermitian:
            if not np.allclose(
                result, result.transpose(1, 0, 3, 2).conj(),
                atol=1e-11, rtol=0,
            ):
                raise ValueError("nuclear Wilson-line result is not Hermitian")
            original_eigenvalues = np.linalg.eigvalsh(
                values.transpose(0, 2, 1, 3).reshape(6, 6)
            )
            result_eigenvalues = np.linalg.eigvalsh(
                result.transpose(0, 2, 1, 3).reshape(6, 6)
            )
            if not np.allclose(
                original_eigenvalues, result_eigenvalues,
                atol=1e-10, rtol=1e-10,
            ):
                raise ValueError(
                    "unitary nuclear phase did not preserve positivity spectrum"
                )
        return result
