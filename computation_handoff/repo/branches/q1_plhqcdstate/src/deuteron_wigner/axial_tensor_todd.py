"""Quark ``g1LT`` and ``g1TT`` gauge-link and rescattering models.

Both functions are leading-twist, chiral-even, T-odd spin-1 structures in
the axial quark projection.  A real one-body impulse correlator cannot
generate them.  This module provides two deliberately separated layers:

1. independent positivity-bounded phenomenological amplitudes;
2. a screened one-gluon/eikonal rescattering moment acting on explicit
   S--P and S--D light-front interference channels.

Neither layer is described as a fit.  The second is a calculational model of
the phase rather than a free downstream TMD profile.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping

import numpy as np
from scipy.linalg import expm

from .gtmd import GaugeLink
from .quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    Spin1QuarkCorrelator,
    compose_spin1_quark_correlator,
)
from .spin import spin_one_basis

M_DEUTERON_GEV = 1.87561294257
LIGHT_FLAVORS = (2, 1, -2, -1)


def _staple_sign(link: GaugeLink) -> float:
    if link.incoming == link.outgoing == "+":
        return 1.0
    if link.incoming == link.outgoing == "-":
        return -1.0
    raise ValueError("mixed links require a process-specific axial rescattering model")


def _sum(
    left: Spin1QuarkCorrelator, right: Spin1QuarkCorrelator
) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        left.vector + right.vector,
        left.axial + right.axial,
        left.transverse + right.transverse,
    )


@dataclass(frozen=True)
class AxialTensorTOddScenario:
    """Independent flavor coefficients for the two axial tensor structures."""

    label: str
    g1lt_fractions: Mapping[int, float]
    g1tt_fractions: Mapping[int, float]
    width_gev2: float = 0.34

    def __post_init__(self) -> None:
        if (
            set(self.g1lt_fractions) != set(LIGHT_FLAVORS)
            or set(self.g1tt_fractions) != set(LIGHT_FLAVORS)
        ):
            raise ValueError("g1LT/g1TT scenarios require u,d,ubar,dbar")
        values = (*self.g1lt_fractions.values(), *self.g1tt_fractions.values())
        if not self.label or self.width_gev2 <= 0.0:
            raise ValueError("axial tensor scenario requires label and width")
        if any(not np.isfinite(value) or abs(value) > 1.0 for value in values):
            raise ValueError("axial tensor fractions must be finite and bounded")

    def future_values(
        self, flavor: int, *, f1_gev2: float, k_gev: float
    ) -> tuple[float, float]:
        """Return model coefficients before the full-density positivity cap."""

        if flavor not in LIGHT_FLAVORS or k_gev < 0.0:
            raise ValueError("unsupported flavor or transverse momentum")
        if k_gev == 0.0:
            return 0.0, 0.0
        shape = math.exp(-0.35 * k_gev**2 / self.width_gev2)
        scale = max(0.0, float(f1_gev2)) * shape
        return (
            float(self.g1lt_fractions[flavor] * scale),
            float(self.g1tt_fractions[flavor] * scale),
        )


def axial_tensor_todd_scenarios() -> tuple[AxialTensorTOddScenario, ...]:
    """Conservative independent low/central/high model scenarios."""

    return (
        AxialTensorTOddScenario(
            "phase_low",
            {2: 0.025, 1: -0.035, -2: 0.010, -1: -0.014},
            {2: -0.018, 1: 0.026, -2: -0.007, -1: 0.010},
        ),
        AxialTensorTOddScenario(
            "phase_central",
            {2: 0.060, 1: -0.085, -2: 0.024, -1: -0.034},
            {2: -0.043, 1: 0.062, -2: -0.017, -1: 0.025},
        ),
        AxialTensorTOddScenario(
            "phase_high",
            {2: 0.110, 1: -0.155, -2: 0.044, -1: -0.062},
            {2: -0.078, 1: 0.112, -2: -0.031, -1: 0.045},
        ),
    )


@dataclass(frozen=True)
class EikonalKernelParameters:
    """Screened one-gluon transverse rescattering kernel."""

    label: str = "screened_central"
    alpha_s: float = 0.34
    screening_mass_gev: float = 0.32
    dipole_scale_gev: float = 1.10
    q_max_gev: float = 3.0
    n_q: int = 56
    n_phi: int = 64

    def __post_init__(self) -> None:
        if not self.label:
            raise ValueError("eikonal kernel requires a label")
        if min(
            self.alpha_s,
            self.screening_mass_gev,
            self.dipole_scale_gev,
            self.q_max_gev,
        ) <= 0.0:
            raise ValueError("eikonal scales and coupling must be positive")
        if self.n_q < 20 or self.n_phi < 24:
            raise ValueError("eikonal angular/radial quadrature is under-resolved")


@dataclass(frozen=True)
class EikonalAxialTensorModel:
    """Generate axial tensor phases from screened transverse rescattering.

    The rank-one moment is paired with S--P interference and the rank-two
    moment with S--D plus P-even--P-odd interference.  The deuteron D-state
    probability is an explicit input rather than a universal tensor factor.
    """

    kernel: EikonalKernelParameters = EikonalKernelParameters()
    d_state_probability: float = 0.0578
    sd_radial_coherence: float = 1.0
    p_even: Mapping[int, float] = None
    p_odd: Mapping[int, float] = None
    tensor_coupling: Mapping[int, float] = None

    def __post_init__(self) -> None:
        default_p_even = {2: 0.22, 1: -0.16, -2: 0.06, -1: -0.05}
        default_p_odd = {2: -0.10, 1: 0.14, -2: -0.03, -1: 0.04}
        default_tensor = {2: 0.80, 1: -0.92, -2: 0.34, -1: -0.40}
        object.__setattr__(self, "p_even", dict(self.p_even or default_p_even))
        object.__setattr__(self, "p_odd", dict(self.p_odd or default_p_odd))
        object.__setattr__(
            self, "tensor_coupling", dict(self.tensor_coupling or default_tensor)
        )
        if any(
            set(values) != set(LIGHT_FLAVORS)
            for values in (self.p_even, self.p_odd, self.tensor_coupling)
        ):
            raise ValueError("eikonal model requires four flavor maps")
        if not 0.0 <= self.d_state_probability < 1.0:
            raise ValueError("D-state probability must lie in [0,1)")
        if not -1.0 <= self.sd_radial_coherence <= 1.0:
            raise ValueError("normalized S-D radial coherence must lie in [-1,1]")

    def _moment(self, k_gev: float, width_gev2: float, rank: int) -> float:
        """Numerically evaluate a screened harmonic one-gluon moment."""

        if k_gev < 0.0 or width_gev2 <= 0.0 or rank not in (1, 2):
            raise ValueError("invalid eikonal moment request")
        if k_gev == 0.0:
            return 0.0
        nodes, weights = np.polynomial.legendre.leggauss(self.kernel.n_q)
        q = 0.5 * self.kernel.q_max_gev * (nodes + 1.0)
        wq = 0.5 * self.kernel.q_max_gev * weights
        phi = 2.0 * np.pi * np.arange(self.kernel.n_phi) / self.kernel.n_phi
        cos_phi = np.cos(phi)
        harmonic = np.cos(rank * phi)
        total = 0.0
        color_factor = 4.0 / 3.0
        for q_value, q_weight in zip(q, wq):
            shifted2 = (
                k_gev**2 + q_value**2
                - 2.0 * k_gev * q_value * cos_phi
            )
            amplitude = np.exp(-shifted2 / (2.0 * width_gev2))
            angular = float(np.mean(harmonic * amplitude))
            propagator = 1.0 / (
                q_value**2 + self.kernel.screening_mass_gev**2
            )
            dipole = (
                self.kernel.dipole_scale_gev**2
                / (self.kernel.dipole_scale_gev**2 + q_value**2)
            ) ** 2
            total += (
                q_weight
                * q_value
                * propagator
                * dipole
                * (q_value / M_DEUTERON_GEV) ** rank
                * angular
            )
        return float(
            color_factor * self.kernel.alpha_s * total / (2.0 * np.pi)
        )

    def future_values(
        self,
        flavor: int,
        *,
        f1_gev2: float,
        k_gev: float,
        width_gev2: float,
    ) -> tuple[float, float]:
        """Return explicit S--P and S--D/P--P imaginary interferences."""

        if flavor not in LIGHT_FLAVORS:
            raise ValueError("unsupported eikonal flavor")
        if k_gev == 0.0 or f1_gev2 <= 0.0:
            return 0.0, 0.0
        p_d = self.d_state_probability
        tensor_mix = (
            math.sqrt(p_d * (1.0 - p_d)) * self.sd_radial_coherence
        )
        m1 = self._moment(float(k_gev), float(width_gev2), 1)
        m2 = self._moment(float(k_gev), float(width_gev2), 2)
        flavor_tensor = self.tensor_coupling[flavor]
        g1lt = (
            2.0 * f1_gev2 * tensor_mix * flavor_tensor
            * self.p_odd[flavor] * m1
        )
        sd_odd = tensor_mix * self.p_odd[flavor] * m2
        pp_odd = (
            p_d * self.p_even[flavor] * self.p_odd[flavor] * m1**2
        )
        g1tt = 2.0 * f1_gev2 * flavor_tensor * (sd_odd + pp_odd)
        return float(g1lt), float(g1tt)


@dataclass(frozen=True)
class Spin1QuarkNuclearWilsonLine:
    """Unitary flavor-resolved axial tensor phase on a spin-1 quark parent.

    Unlike the historical coefficient-level stage, this operator acts on
    every retained target-helicity projection before TMD projection.  Its LT
    and TT phase coefficients use the same explicit S--P, S--D, and P--P
    hierarchy as :class:`EikonalAxialTensorModel`.  Unitarity preserves the
    complete target x quark-spin positivity spectrum for Hermitian parents.
    """

    model: EikonalAxialTensorModel
    flavor: int
    gauge_link: GaugeLink

    def __post_init__(self) -> None:
        if self.flavor not in LIGHT_FLAVORS:
            raise ValueError("unsupported axial tensor flavor")
        _staple_sign(self.gauge_link)

    def phases(
        self, k_gev: float, width_gev2: float
    ) -> tuple[float, float]:
        if k_gev < 0.0 or width_gev2 <= 0.0:
            raise ValueError("invalid nuclear Wilson-line phase request")
        if k_gev == 0.0:
            return 0.0, 0.0
        channels = self.channel_phases(k_gev, width_gev2)
        return channels["S_P"], channels["S_D"] + channels["P_P"]

    def channel_phases(
        self, k_gev: float, width_gev2: float
    ) -> dict[str, float]:
        """Return non-overlapping S-P, S-D, and P-P exponent channels."""

        if k_gev < 0.0 or width_gev2 <= 0.0:
            raise ValueError("invalid nuclear Wilson-line phase request")
        if k_gev == 0.0:
            return {"S_P": 0.0, "S_D": 0.0, "P_P": 0.0}
        sign = _staple_sign(self.gauge_link)
        p_d = self.model.d_state_probability
        tensor_mix = (
            math.sqrt(p_d * (1.0 - p_d))
            * self.model.sd_radial_coherence
        )
        m1 = self.model._moment(k_gev, width_gev2, 1)
        m2 = self.model._moment(k_gev, width_gev2, 2)
        tensor = self.model.tensor_coupling[self.flavor]
        odd = self.model.p_odd[self.flavor]
        even = self.model.p_even[self.flavor]
        return {
            "S_P": sign * 2.0 * tensor_mix * tensor * odd * m1,
            "S_D": sign * 2.0 * tensor * tensor_mix * odd * m2,
            "P_P": sign * 2.0 * tensor * p_d * even * odd * m1**2,
        }

    def unitary(
        self, momentum_gev: tuple[float, float], width_gev2: float
    ) -> np.ndarray:
        k = float(np.hypot(*momentum_gev))
        if k == 0.0 or self.model.d_state_probability == 0.0:
            return np.eye(3, dtype=np.complex128)
        phi = math.atan2(momentum_gev[1], momentum_gev[0])
        target = spin_one_basis()
        generator_lt = (
            math.cos(phi) * target["LT_x"]
            + math.sin(phi) * target["LT_y"]
        )
        generator_tt = (
            math.cos(2.0 * phi) * target["TT_x"]
            + math.sin(2.0 * phi) * target["TT_y"]
        )
        phase_lt, phase_tt = self.phases(k, width_gev2)
        return expm(1j * (phase_lt * generator_lt + phase_tt * generator_tt))

    @staticmethod
    def apply_unitary(
        correlator: Spin1QuarkCorrelator, unitary: np.ndarray
    ) -> Spin1QuarkCorrelator:
        u = np.asarray(unitary, dtype=np.complex128)
        if u.shape != (3, 3):
            raise ValueError("spin-one Wilson unitary must be 3x3")

        def rotate(values: np.ndarray) -> np.ndarray:
            return u @ values @ u.conj().T

        result = Spin1QuarkCorrelator(
            rotate(correlator.vector),
            rotate(correlator.axial),
            np.asarray([rotate(value) for value in correlator.transverse]),
        )
        if correlator.is_target_hermitian():
            before = np.linalg.eigvalsh(correlator.quark_target_density_matrix())
            after = np.linalg.eigvalsh(result.quark_target_density_matrix())
            if not np.allclose(before, after, atol=1.0e-10, rtol=1.0e-10):
                raise ValueError("quark nuclear Wilson line changed density spectrum")
        return result


def add_axial_tensor_todd(
    base: Spin1QuarkCorrelator,
    *,
    momentum: tuple[float, float],
    g1lt_future: float,
    g1tt_future: float,
    gauge_link: GaugeLink,
    safety_fraction: float = 0.90,
    tolerance: float = 1.0e-12,
) -> tuple[Spin1QuarkCorrelator, float, float, float]:
    """Add both structures with a common full-density positivity cap.

    Returns ``(correlator, scale, final_g1LT, final_g1TT)``.  The common
    scale preserves the model-predicted relation between the two amplitudes.
    """

    if not 0.0 < safety_fraction <= 1.0:
        raise ValueError("positivity safety fraction must lie in (0,1]")
    if base.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("base correlator is outside the positivity domain")
    k = float(np.hypot(*momentum))
    if k == 0.0:
        return base, 0.0, 0.0, 0.0
    sign = _staple_sign(gauge_link)
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values["g1LT"] = sign * float(g1lt_future)
    values["g1TT"] = sign * float(g1tt_future)
    correction = compose_spin1_quark_correlator(
        momentum, M_DEUTERON_GEV, values
    )

    def candidate(scale: float) -> Spin1QuarkCorrelator:
        return _sum(
            base,
            Spin1QuarkCorrelator(
                scale * correction.vector,
                scale * correction.axial,
                scale * correction.transverse,
            ),
        )

    if candidate(1.0).minimum_positivity_eigenvalue() >= -tolerance:
        scale = 1.0
    else:
        low, high = 0.0, 1.0
        for _ in range(64):
            middle = 0.5 * (low + high)
            if candidate(middle).minimum_positivity_eigenvalue() >= tolerance:
                low = middle
            else:
                high = middle
        scale = safety_fraction * low
    result = candidate(scale)
    if result.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("positivity cap failed")
    return (
        result,
        float(scale),
        float(scale * sign * g1lt_future),
        float(scale * sign * g1tt_future),
    )
