"""Tensor-polarized Sullivan pion contribution in a spin-1 deuteron."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np
from scipy.integrate import quad, simpson
from scipy.interpolate import PchipInterpolator
from scipy.special import j0, spherical_jn
from numpy.polynomial.legendre import leggauss

from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)
from .nuclear_mechanisms import AdditionalNuclearComponentInput
from .quark_correlator import Spin1QuarkCorrelator
from .spin import diagonal_from_u_l_delta_t
from .wavefunctions.av18 import load_av18_coordinate

HBARC_GEV_FM = 0.1973269804
LIGHT_FLAVORS = (2, 1, -2, -1)


@dataclass(frozen=True)
class NucleonMesonMomentumAudit:
    """Hadronic plus-momentum ledger for activating a pion Fock component."""

    nucleon_fraction_before_pion: float
    pion_fraction: float

    @property
    def uncompensated_total(self) -> float:
        return self.nucleon_fraction_before_pion + self.pion_fraction

    @property
    def required_nucleon_fraction(self) -> float:
        return 1.0 - self.pion_fraction

    @property
    def required_nucleon_subtraction(self) -> float:
        return self.nucleon_fraction_before_pion - self.required_nucleon_fraction

    def passes(self, tolerance: float = 1.0e-8) -> bool:
        return abs(self.uncompensated_total - 1.0) <= tolerance


@dataclass(frozen=True)
class NNPiFockLedger:
    """Exact probability and plus-momentum ledger for NN plus NNπ sectors."""

    raw_pinn_norm: float
    raw_pion_momentum: float

    @property
    def z_factor(self) -> float:
        return 1.0 + self.raw_pinn_norm

    @property
    def nn_probability(self) -> float:
        return 1.0 / self.z_factor

    @property
    def pinn_probability(self) -> float:
        return self.raw_pinn_norm / self.z_factor

    @property
    def nn_sector_nucleon_momentum(self) -> float:
        return self.nn_probability

    @property
    def pinn_sector_pion_momentum(self) -> float:
        return self.raw_pion_momentum / self.z_factor

    @property
    def pinn_sector_nucleon_momentum(self) -> float:
        return (self.raw_pinn_norm - self.raw_pion_momentum) / self.z_factor

    @property
    def total_momentum(self) -> float:
        return (
            self.nn_sector_nucleon_momentum
            + self.pinn_sector_nucleon_momentum
            + self.pinn_sector_pion_momentum
        )


@dataclass(frozen=True)
class MillerPionExchangeParameters:
    """Parameters entering Eqs. (7), (19), and (20) of arXiv:1311.4561."""

    nucleon_mass_gev: float = 0.93891897
    pion_mass_gev: float = 0.13957039
    pion_nucleon_coupling: float = 13.5
    axial_mass_gev: float = 1.03
    q_max_gev: float = 5.0
    q_nodes: int = 1001
    transverse_nodes: int = 320

    def __post_init__(self) -> None:
        if min(
            self.nucleon_mass_gev,
            self.pion_mass_gev,
            self.pion_nucleon_coupling,
            self.axial_mass_gev,
            self.q_max_gev,
        ) <= 0.0:
            raise ValueError("pion-exchange parameters must be positive")
        if self.q_nodes < 101 or self.q_nodes % 2 == 0:
            raise ValueError("q_nodes must be an odd integer >=101")
        if self.transverse_nodes < 40:
            raise ValueError("transverse_nodes must be >=40")


class MillerTensorPionDistribution:
    """AV18 tensor pion light-cone distribution ``delta f_pi(y)``."""

    def __init__(
        self,
        wave_path: str | Path = "data/raw/av18/deut.wf",
        parameters: MillerPionExchangeParameters | None = None,
    ) -> None:
        self.parameters = parameters or MillerPionExchangeParameters()
        self.wave = load_av18_coordinate(wave_path)
        self._legendre_nodes, self._legendre_weights = leggauss(
            self.parameters.transverse_nodes
        )
        q = np.linspace(0.0, self.parameters.q_max_gev, self.parameters.q_nodes)
        r = self.wave.grid
        qr = np.outer(q / HBARC_GEV_FM, r)
        j0 = spherical_jn(0, qr)
        j2 = spherical_jn(2, qr)
        self._integrals = {
            "uu0": PchipInterpolator(
                q, simpson(j0 * self.wave.u[None, :] ** 2, x=r, axis=1)
            ),
            "uw2": PchipInterpolator(
                q,
                simpson(
                    j2 * self.wave.u[None, :] * self.wave.w[None, :],
                    x=r,
                    axis=1,
                ),
            ),
            "ww0": PchipInterpolator(
                q, simpson(j0 * self.wave.w[None, :] ** 2, x=r, axis=1)
            ),
            "ww2": PchipInterpolator(
                q, simpson(j2 * self.wave.w[None, :] ** 2, x=r, axis=1)
            ),
        }
        self.provenance = ComponentProvenance(
            name="AV18 Sullivan tensor pion distribution",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.MESON_EXCHANGE,
            sources=(
                "G. A. Miller, Phys. Rev. C 89, 045203 (2014), arXiv:1311.4561",
                "AV18 coordinate-space deuteron wave function",
                "axial dipole mass M_A=1.03+-0.04 GeV",
            ),
            assumptions=(
                "two-nucleon plus one-pion intermediate-state saturation",
                "nonrelativistic deuteron dynamics and neglected retardation",
                "generalized Goldberger-Treiman relation for the piNN form factor",
            ),
            validity=ValidityDomain(1.0e-4, 0.8, 1.14, 100.0),
            uncertainty_kind=(
                "axial-mass +/-0.04 GeV variants, pion-PDF replicas, "
                "and deuteron wave-function model dependence"
            ),
            replaceable_interface="MillerTensorPionDistribution",
        )

    def radial_integral(self, channel: str, q_gev: float) -> float:
        if channel not in self._integrals:
            raise KeyError(f"unknown pion radial channel {channel}")
        if not 0.0 <= q_gev <= self.parameters.q_max_gev:
            return 0.0
        return float(self._integrals[channel](q_gev))

    @lru_cache(maxsize=8192)
    def component(self, channel: str, y: float) -> float:
        """Return ``f_abL(y)`` from Eq. (19) of arXiv:1311.4561."""

        if y == 0.0:
            return 0.0
        if y < 0.0:
            return self.component(channel, -y)
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0

        q_perp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        q2 = q_perp2 + qz2
        q = np.sqrt(q2)
        propagator = (q2 + p.pion_mass_gev**2) ** -2
        axial = (1.0 + q2 / p.axial_mass_gev**2) ** -4
        tensor = q_perp2 - 2.0 * qz2
        radial = np.asarray(self._integrals[channel](q), dtype=float)
        integral = float(
            upper
            / 2.0
            * np.dot(
                self._legendre_weights,
                propagator * axial * tensor * radial,
            )
        )
        return float(
            -3.0
            * y
            * p.pion_nucleon_coupling**2
            / (8.0 * math.pi**2)
            * integral
        )

    @lru_cache(maxsize=4096)
    def delta_f(self, y: float) -> float:
        """Return ``f_pi^(0)-f_pi^(1)`` from Eq. (20)."""

        return float(
            self.component("uu0", y)
            + math.sqrt(2.0) / 2.0 * self.component("uw2", y)
            + self.component("ww0", y)
            - 0.25 * self.component("ww2", y)
        )

    @lru_cache(maxsize=4096)
    def spin_averaged_f(self, y: float) -> float:
        r"""Return ``(f_pi^(0)+2 f_pi^(1))/3`` from the published spin projections.

        Averaging the individual ``F_m`` expressions following Eq. (7) of
        arXiv:1311.4561 gives

        .. math::
           \bar F={q^2\over3}
           [I_{uu0}-4\sqrt2 I_{uw2}+I_{ww0}+2I_{ww2}].

        The printed ``F_0^{ww}`` line repeats ``I_ww2`` in its first term.
        Reading that term as ``I_ww0`` is required by the channel definition
        and exactly reproduces the paper's subsequent
        ``delta f = ... + f_ww0 - f_ww2/4`` identity.
        """

        if y == 0.0:
            return 0.0
        if y < 0.0:
            return self.spin_averaged_f(-y)
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0
        q_perp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        density = self._spin_averaged_differential_array(y, q_perp2)
        return float(upper / 2.0 * np.dot(self._legendre_weights, density))

    def _spin_averaged_differential_array(
        self, y: float, q_perp2_gev2: np.ndarray
    ) -> np.ndarray:
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        q2 = np.asarray(q_perp2_gev2, dtype=float) + qz2
        q = np.sqrt(q2)
        radial_average = (
            np.asarray(self._integrals["uu0"](q))
            - 4.0 * math.sqrt(2.0) * np.asarray(self._integrals["uw2"](q))
            + np.asarray(self._integrals["ww0"](q))
            + 2.0 * np.asarray(self._integrals["ww2"](q))
        ) / 3.0
        kernel = (
            (q2 + p.pion_mass_gev**2) ** -2
            * (1.0 + q2 / p.axial_mass_gev**2) ** -4
            * q2
            * radial_average
        )
        return (
            -3.0
            * y
            * p.pion_nucleon_coupling**2
            / (8.0 * math.pi**2)
            * kernel
        )

    def spin_averaged_differential(self, y: float, q_perp2_gev2: float) -> float:
        """Return d fbar_pi(y)/d q_perp² before transverse integration."""

        if y == 0.0:
            return 0.0
        if y < 0.0:
            return self.spin_averaged_differential(-y, q_perp2_gev2)
        if q_perp2_gev2 < 0.0:
            raise ValueError("q_perp squared must be nonnegative")
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        q2 = q_perp2_gev2 + qz2
        if q2 > p.q_max_gev**2:
            return 0.0
        return float(
            self._spin_averaged_differential_array(
                y, np.asarray([q_perp2_gev2])
            )[0]
        )

    @lru_cache(maxsize=32768)
    def spin_averaged_nn_recoil_b(
        self, y: float, alpha: float, b_gev_inv: float
    ) -> float:
        """Pion splitting with recoil assigned to an NN constituent.

        The NN subsystem has transverse momentum ``-qT``. A constituent with
        internal plus fraction ``alpha`` receives ``-alpha*qT``, producing
        ``J0(alpha*b*qT)`` in impact space. At b=0 (or alpha=0) this reduces
        exactly to the spin-averaged pion probability density.
        """

        if not 0.0 <= alpha <= 1.0:
            raise ValueError("NN internal momentum fraction must lie in [0,1]")
        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        if b_gev_inv == 0.0 or alpha == 0.0:
            return self.spin_averaged_f(y)
        if y <= 0.0:
            return (
                0.0
                if y == 0.0
                else self.spin_averaged_nn_recoil_b(-y, alpha, b_gev_inv)
            )
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0
        q_perp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        density = self._spin_averaged_differential_array(y, q_perp2)
        return float(
            upper
            / 2.0
            * np.dot(
                self._legendre_weights,
                density * j0(alpha * b_gev_inv * np.sqrt(q_perp2)),
            )
        )

    @lru_cache(maxsize=32768)
    def spin_averaged_f_b(self, y: float, z: float, b_gev_inv: float) -> float:
        """Spin-average splitting resolved in impact space.

        The Bessel factor follows from
        ``k_T(deuteron)=k_T(parton/pion)+z q_T(pion/deuteron)``. At ``b=0``
        this reduces exactly to :meth:`spin_averaged_f`.
        """

        if not 0.0 <= z <= 1.0:
            raise ValueError("parton-in-pion fraction z must lie in [0,1]")
        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        if b_gev_inv == 0.0:
            return self.spin_averaged_f(y)
        if y <= 0.0:
            return 0.0 if y == 0.0 else self.spin_averaged_f_b(-y, z, b_gev_inv)
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0
        qp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        q2 = qp2 + qz2
        q = np.sqrt(q2)
        radial_average = (
            np.asarray(self._integrals["uu0"](q))
            - 4.0 * math.sqrt(2.0) * np.asarray(self._integrals["uw2"](q))
            + np.asarray(self._integrals["ww0"](q))
            + 2.0 * np.asarray(self._integrals["ww2"](q))
        ) / 3.0
        kernel = (
            (q2 + p.pion_mass_gev**2) ** -2
            * (1.0 + q2 / p.axial_mass_gev**2) ** -4
            * q2
            * radial_average
            * j0(z * b_gev_inv * np.sqrt(qp2))
        )
        integral = float(upper / 2.0 * np.dot(self._legendre_weights, kernel))
        return float(
            -3.0
            * y
            * p.pion_nucleon_coupling**2
            / (8.0 * math.pi**2)
            * integral
        )

    def spin_projection_f(self, helicity: int, y: float) -> float:
        """Directly evaluate the published ``f_pi^(m)`` for ``m=0,±1``."""

        if helicity not in (-1, 0, 1):
            raise ValueError("deuteron helicity must be -1, 0, or 1")
        if y == 0.0:
            return 0.0
        if y < 0.0:
            return self.spin_projection_f(helicity, -y)
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0
        qp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        q2 = qp2 + qz2
        q = np.sqrt(q2)
        uu0 = np.asarray(self._integrals["uu0"](q))
        uw2 = np.asarray(self._integrals["uw2"](q))
        ww0 = np.asarray(self._integrals["ww0"](q))
        ww2 = np.asarray(self._integrals["ww2"](q))
        if helicity == 0:
            form = (
                (qp2 - qz2) * uu0
                - (2.0 * qp2 + 4.0 * qz2) / math.sqrt(2.0) * uw2
                + (qp2 - qz2) * ww0
                + (2.0 * qp2 + 4.0 * qz2) / 4.0 * ww2
            )
        else:
            form = (
                qz2 * uu0
                - (3.0 * qp2 + 2.0 * qz2) / math.sqrt(2.0) * uw2
                + qz2 * ww0
                + (3.0 * qp2 + 2.0 * qz2) / 4.0 * ww2
            )
        kernel = (
            (q2 + p.pion_mass_gev**2) ** -2
            * (1.0 + q2 / p.axial_mass_gev**2) ** -4
            * form
        )
        integral = float(upper / 2.0 * np.dot(self._legendre_weights, kernel))
        return float(
            -3.0
            * y
            * p.pion_nucleon_coupling**2
            / (8.0 * math.pi**2)
            * integral
        )

    @lru_cache(maxsize=65536)
    def spin_projection_f_b(
        self, helicity: int, y: float, z: float, b_gev_inv: float
    ) -> float:
        """Spin-resolved pion splitting with exact partonic recoil in b space."""

        if helicity not in (-1, 0, 1):
            raise ValueError("deuteron helicity must be -1, 0, or 1")
        if not 0.0 <= z <= 1.0:
            raise ValueError("parton-in-pion fraction z must lie in [0,1]")
        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        if b_gev_inv == 0.0:
            return self.spin_projection_f(helicity, y)
        if y == 0.0:
            return 0.0
        if y < 0.0:
            return self.spin_projection_f_b(helicity, -y, z, b_gev_inv)
        p = self.parameters
        qz2 = (p.nucleon_mass_gev * y) ** 2
        upper = max(0.0, p.q_max_gev**2 - qz2)
        if upper == 0.0:
            return 0.0
        qp2 = upper * (self._legendre_nodes + 1.0) / 2.0
        q2 = qp2 + qz2
        q = np.sqrt(q2)
        uu0 = np.asarray(self._integrals["uu0"](q))
        uw2 = np.asarray(self._integrals["uw2"](q))
        ww0 = np.asarray(self._integrals["ww0"](q))
        ww2 = np.asarray(self._integrals["ww2"](q))
        if helicity == 0:
            form = (
                (qp2 - qz2) * uu0
                - (2.0 * qp2 + 4.0 * qz2) / math.sqrt(2.0) * uw2
                + (qp2 - qz2) * ww0
                + (2.0 * qp2 + 4.0 * qz2) / 4.0 * ww2
            )
        else:
            form = (
                qz2 * uu0
                - (3.0 * qp2 + 2.0 * qz2) / math.sqrt(2.0) * uw2
                + qz2 * ww0
                + (3.0 * qp2 + 2.0 * qz2) / 4.0 * ww2
            )
        kernel = (
            (q2 + p.pion_mass_gev**2) ** -2
            * (1.0 + q2 / p.axial_mass_gev**2) ** -4
            * form
            * j0(z * b_gev_inv * np.sqrt(qp2))
        )
        integral = float(upper / 2.0 * np.dot(self._legendre_weights, kernel))
        return float(
            -3.0
            * y
            * p.pion_nucleon_coupling**2
            / (8.0 * math.pi**2)
            * integral
        )

    def spin_averaged_moments(self, y_max: float = 2.0) -> dict[str, float]:
        """Return pion number and deuteron plus-momentum moments.

        ``y`` is normalized to the nucleon mass in the source, while
        ``y_A M_D = y M``. The reported deuteron momentum fraction therefore
        retains the exact ``M/M_D`` conversion rather than replacing it by
        one half.
        """

        if y_max <= 0.0:
            raise ValueError("y_max must be positive")
        number = quad(
            self.spin_averaged_f, 0.0, y_max, epsabs=2.0e-8, limit=200
        )[0]
        deuteron_mass = 1.87561294257
        momentum = quad(
            lambda y: (
                y
                * self.parameters.nucleon_mass_gev
                / deuteron_mass
                * self.spin_averaged_f(y)
            ),
            0.0,
            y_max,
            epsabs=2.0e-8,
            limit=200,
        )[0]
        return {
            "pion_number_connected": float(number),
            "pion_deuteron_plus_momentum_fraction": float(momentum),
        }

    def momentum_audit(
        self, nucleon_fraction_before_pion: float = 1.0, y_max: float = 2.0
    ) -> NucleonMesonMomentumAudit:
        if not 0.0 <= nucleon_fraction_before_pion <= 1.0:
            raise ValueError("nucleon plus-momentum fraction must lie in [0,1]")
        pion_fraction = self.spin_averaged_moments(y_max)[
            "pion_deuteron_plus_momentum_fraction"
        ]
        return NucleonMesonMomentumAudit(
            nucleon_fraction_before_pion=nucleon_fraction_before_pion,
            pion_fraction=pion_fraction,
        )


class FockNormalizedMillerPionDistribution:
    """Apply the exact NN/NNπ normalization omitted in the source's Z≈1 plots.

    The wrapper normalizes all pion spin projections by the same Fock-space
    factor. It also exposes the momentum carried by nucleons inside the NNπ
    sector; their x, spin, and transverse distributions remain a required
    independent input.
    """

    def __init__(self, raw: MillerTensorPionDistribution):
        self.raw = raw
        moments = raw.spin_averaged_moments()
        self.ledger = NNPiFockLedger(
            raw_pinn_norm=moments["pion_number_connected"],
            raw_pion_momentum=moments["pion_deuteron_plus_momentum_fraction"],
        )
        if not (
            0.0 <= self.ledger.raw_pion_momentum <= self.ledger.raw_pinn_norm
        ):
            raise ValueError("NNπ Fock moments do not define a physical ledger")

    @property
    def normalization(self) -> float:
        return 1.0 / self.ledger.z_factor

    def delta_f(self, y: float) -> float:
        return self.normalization * self.raw.delta_f(y)

    def spin_averaged_f(self, y: float) -> float:
        return self.normalization * self.raw.spin_averaged_f(y)

    def spin_projection_f(self, helicity: int, y: float) -> float:
        return self.normalization * self.raw.spin_projection_f(helicity, y)

    def spin_projection_f_b(
        self, helicity: int, y: float, z: float, b_gev_inv: float
    ) -> float:
        return self.normalization * self.raw.spin_projection_f_b(
            helicity, y, z, b_gev_inv
        )

    def spin_averaged_f_b(self, y: float, z: float, b_gev_inv: float) -> float:
        return self.normalization * self.raw.spin_averaged_f_b(
            y, z, b_gev_inv
        )

    def spin_averaged_nn_recoil_b(
        self, y: float, recoil_fraction: float, b_gev_inv: float
    ) -> float:
        return self.normalization * self.raw.spin_averaged_nn_recoil_b(
            y, recoil_fraction, b_gev_inv
        )

    def spin_averaged_moments(self, y_max: float = 2.0) -> dict[str, float]:
        raw = self.raw.spin_averaged_moments(y_max)
        return {
            key: self.normalization * value for key, value in raw.items()
        }


@dataclass
class NNPiLongitudinalRecoilConvolution:
    """Conditional NNπ nucleon recoil derived from the pion splitting.

    In an NNπ state the pion carries deuteron fraction
    ``eta=y*M_N/M_D``. The residual NN subsystem carries ``1-eta`` and an
    active nucleon's internal fraction ``alpha`` maps to
    ``alpha'=(1-eta)*alpha``. Applying this map to a complete baseline
    correlator preserves its spin matrix while changing its x shape.

    This supersedes the unchanged-shape counterterm in longitudinal
    observables. It is not a full three-body spectral amplitude: transverse
    recoil, pion-spin entanglement, and NNπ off-shell response remain
    separate replacement tasks.
    """

    distribution: FockNormalizedMillerPionDistribution
    nodes: int = 72
    deuteron_mass_gev: float = 1.87561294257

    def __post_init__(self) -> None:
        if self.nodes < 32:
            raise ValueError("NNpi recoil quadrature requires at least 32 nodes")
        if self.deuteron_mass_gev <= 0.0:
            raise ValueError("deuteron mass must be positive")

    def pion_deuteron_fraction(self, y: float) -> float:
        return float(
            y
            * self.distribution.raw.parameters.nucleon_mass_gev
            / self.deuteron_mass_gev
        )

    @staticmethod
    def _zero() -> Spin1QuarkCorrelator:
        return Spin1QuarkCorrelator(
            vector=np.zeros((3, 3), dtype=np.complex128),
            axial=np.zeros((3, 3), dtype=np.complex128),
            transverse=np.zeros((2, 3, 3), dtype=np.complex128),
        )

    def nnpi_nucleon(
        self,
        baseline: Callable[[float], Spin1QuarkCorrelator],
        x: float,
    ) -> Spin1QuarkCorrelator:
        """Return the physical NNπ-sector nucleon correlator at x."""

        if not 0.0 < x < 1.0:
            return self._zero()
        mass_ratio = (
            self.distribution.raw.parameters.nucleon_mass_gev
            / self.deuteron_mass_gev
        )
        y_upper = min(2.0, (1.0 - x) / mass_ratio)
        if y_upper <= 0.0:
            return self._zero()
        nodes, weights = leggauss(self.nodes)
        y_values = y_upper * (nodes + 1.0) / 2.0
        weights = y_upper * weights / 2.0
        vector = np.zeros((3, 3), dtype=np.complex128)
        axial = np.zeros((3, 3), dtype=np.complex128)
        transverse = np.zeros((2, 3, 3), dtype=np.complex128)
        for y, weight in zip(y_values, weights):
            remaining = 1.0 - self.pion_deuteron_fraction(float(y))
            source = baseline(x / remaining)
            factor = (
                weight
                * self.distribution.spin_averaged_f(float(y))
                / remaining
            )
            vector += factor * source.vector
            axial += factor * source.axial
            transverse += factor * source.transverse
        return Spin1QuarkCorrelator(vector, axial, transverse)

    def nucleon_correction(
        self,
        baseline: Callable[[float], Spin1QuarkCorrelator],
        x: float,
    ) -> Spin1QuarkCorrelator:
        """Return (physical NN + NNπ nucleons) minus unit baseline."""

        if not 0.0 < x < 1.0:
            return self._zero()
        source = baseline(x)
        nn_weight_change = self.distribution.ledger.nn_probability - 1.0
        nnpi = self.nnpi_nucleon(baseline, x)
        return Spin1QuarkCorrelator(
            nn_weight_change * source.vector + nnpi.vector,
            nn_weight_change * source.axial + nnpi.axial,
            nn_weight_change * source.transverse + nnpi.transverse,
        )

    def nnpi_nucleon_b(
        self,
        baseline: Callable[[float, float], Spin1QuarkCorrelator],
        x: float,
        b_gev_inv: float,
    ) -> Spin1QuarkCorrelator:
        """Return the NNπ nucleon correlator including exact transverse recoil.

        The public API uses nucleon-scaled ``x_N``, while the LF parent uses
        ``x_D=x_N/2``. For a residual-NN nucleon fraction ``alpha`` and
        parton fraction ``z=x_D/[alpha*(1-eta_pi)]``, the recoil phase is
        ``z*alpha*b*qT=x_N*b*qT/[2*(1-eta_pi)]``. Thus the apparent alpha
        dependence cancels exactly at impulse level; no average-alpha
        approximation or access to a collinearly integrated alpha is needed.
        """

        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        if not 0.0 < x < 1.0:
            return self._zero()
        mass_ratio = (
            self.distribution.raw.parameters.nucleon_mass_gev
            / self.deuteron_mass_gev
        )
        y_upper = min(2.0, (1.0 - x) / mass_ratio)
        if y_upper <= 0.0:
            return self._zero()
        nodes, weights = leggauss(self.nodes)
        y_values = y_upper * (nodes + 1.0) / 2.0
        weights = y_upper * weights / 2.0
        vector = np.zeros((3, 3), dtype=np.complex128)
        axial = np.zeros((3, 3), dtype=np.complex128)
        transverse = np.zeros((2, 3, 3), dtype=np.complex128)
        for y, weight in zip(y_values, weights):
            remaining = 1.0 - self.pion_deuteron_fraction(float(y))
            shifted_x = x / remaining
            source = baseline(shifted_x, b_gev_inv)
            splitting_b = self.distribution.spin_averaged_nn_recoil_b(
                float(y), 0.5 * shifted_x, b_gev_inv
            )
            factor = weight * splitting_b / remaining
            vector += factor * source.vector
            axial += factor * source.axial
            transverse += factor * source.transverse
        return Spin1QuarkCorrelator(vector, axial, transverse)

    def nucleon_correction_b(
        self,
        baseline: Callable[[float, float], Spin1QuarkCorrelator],
        x: float,
        b_gev_inv: float,
    ) -> Spin1QuarkCorrelator:
        """Return the b-space NN+NNπ nucleon correction."""

        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        if not 0.0 < x < 1.0:
            return self._zero()
        source = baseline(x, b_gev_inv)
        nn_weight_change = self.distribution.ledger.nn_probability - 1.0
        nnpi = self.nnpi_nucleon_b(baseline, x, b_gev_inv)
        return Spin1QuarkCorrelator(
            nn_weight_change * source.vector + nnpi.vector,
            nn_weight_change * source.axial + nnpi.axial,
            nn_weight_change * source.transverse + nnpi.transverse,
        )


class JAM21IsoscalarPionPDF:
    """Charge-averaged light-flavor and gluon pion PDF from one JAM21 replica.

    All released members, including member 0, have ``PdfType: replica``.
    An ensemble central value must therefore be constructed from all members.
    """

    def __init__(
        self,
        member: int = 0,
        data_root: str | Path = "data/raw/lhapdf",
    ) -> None:
        if member < 0 or member >= 786:
            raise ValueError("JAM21 pion member must lie in [0,785]")
        try:
            import lhapdf
        except ImportError as exc:
            raise RuntimeError("LHAPDF is required for JAM21 pion PDFs") from exc
        root = str(Path(data_root).resolve())
        paths = list(lhapdf.paths())
        if root not in paths:
            lhapdf.setPaths([root, *paths])
        self.member = member
        self._pdf: Any = lhapdf.mkPDF("JAM21PionPDFnlo", member)

    def value(self, flavor: int, x: float, q_gev: float) -> float:
        if flavor not in (*LIGHT_FLAVORS, 21):
            raise ValueError("only u,d,ubar,dbar and gluon pion inputs are implemented")
        if not 0.0 < x <= 1.0 or q_gev <= 0.0:
            raise ValueError("invalid pion PDF kinematics")
        if flavor == 21:
            return float(self._pdf.xfxQ(21, x, q_gev) / x)
        # Equal pi+, pi-, pi0 populations in the deuteron isoscalar exchange
        # give 1/2 [q^{pi-}+qbar^{pi-}] for each fixed light flavor.
        return float(
            0.5
            * (
                self._pdf.xfxQ(flavor, x, q_gev)
                + self._pdf.xfxQ(-flavor, x, q_gev)
            )
            / x
        )


@dataclass
class TensorPionConvolution:
    """Flavor-resolved collinear tensor pion convolution."""

    splitting: MillerTensorPionDistribution
    pion_pdf: JAM21IsoscalarPionPDF
    y_max: float = 2.0
    strength: float = 1.0

    def __post_init__(self) -> None:
        if self.y_max <= 0.0:
            raise ValueError("pion y maximum must be positive")
        if self.strength < 0.0 or not math.isfinite(self.strength):
            raise ValueError("pion mechanism strength must be finite and nonnegative")

    def delta_t(self, flavor: int, x: float, q_gev: float) -> float:
        """Return ``q^(0)-q^(1)`` for a single quark or antiquark flavor."""

        if not 0.0 < x < self.y_max:
            return 0.0
        if self.strength == 0.0:
            return 0.0
        return float(
            self.strength
            *
            quad(
                lambda y: (
                    self.pion_pdf.value(flavor, x / y, q_gev)
                    * self.splitting.delta_f(y)
                    / y
                ),
                x,
                self.y_max,
                epsabs=2.0e-8,
                epsrel=3.0e-4,
                limit=180,
                points=tuple(
                    point for point in (0.05, 0.1, 0.2, 0.4, 0.8, 1.2)
                    if x < point < self.y_max
                ),
            )[0]
        )

    def f1ll(self, flavor: int, x: float, q_gev: float) -> float:
        """Standard spin-1 convention ``f1LL=-(2/3) delta_T f``."""

        return float(-2.0 / 3.0 * self.delta_t(flavor, x, q_gev))

    def b1(self, x: float, q_gev: float) -> float:
        """Leading-order charge-weighted pion contribution to deuteron b1."""

        charges2 = {2: 4.0 / 9.0, 1: 1.0 / 9.0}
        return float(
            0.5
            * sum(
                charges2[flavor]
                * (
                    self.delta_t(flavor, x, q_gev)
                    + self.delta_t(-flavor, x, q_gev)
                )
                for flavor in (2, 1)
            )
        )


@dataclass
class SpinAveragedPionConvolution:
    """Flavor-resolved collinear spin-averaged pion convolution."""

    splitting: MillerTensorPionDistribution
    pion_pdf: JAM21IsoscalarPionPDF
    y_max: float = 2.0
    strength: float = 1.0

    def __post_init__(self) -> None:
        if self.y_max <= 0.0:
            raise ValueError("pion y maximum must be positive")
        if self.strength < 0.0 or not math.isfinite(self.strength):
            raise ValueError("pion mechanism strength must be finite and nonnegative")

    def f1(self, flavor: int, x: float, q_gev: float) -> float:
        if flavor not in LIGHT_FLAVORS:
            raise ValueError("spin-averaged pion input requires a light flavor")
        if not 0.0 < x < self.y_max or self.strength == 0.0:
            return 0.0
        return float(
            self.strength
            * quad(
                lambda y: (
                    self.pion_pdf.value(flavor, x / y, q_gev)
                    * self.splitting.spin_averaged_f(y)
                    / y
                ),
                x,
                self.y_max,
                epsabs=2.0e-8,
                epsrel=3.0e-4,
                limit=180,
            )[0]
        )


def build_spin_averaged_pion_component(
    flavor: int,
    convolution: SpinAveragedPionConvolution,
    *,
    momentum_accounting_acknowledged: bool = False,
) -> AdditionalNuclearComponentInput:
    """Adapt the sourced spin average after explicit momentum-ledger review.

    Adding this component to a unit-normalized nucleonic parent without
    reducing the NN Fock-sector momentum would overcount plus momentum.
    The explicit acknowledgement prevents accidental production activation;
    it does not itself prescribe an unsupported universal nucleon rescaling.
    """

    if flavor not in LIGHT_FLAVORS:
        raise ValueError("spin-averaged pion component requires a light flavor")
    if not momentum_accounting_acknowledged:
        audit = convolution.splitting.momentum_audit()
        raise RuntimeError(
            "spin-averaged pion activation requires an explicit NN-sector "
            f"momentum policy; uncompensated total={audit.uncompensated_total:.8f}, "
            f"required nucleon fraction={audit.required_nucleon_fraction:.8f}"
        )

    def component(
        proton: Spin1QuarkCorrelator,
        neutron: Spin1QuarkCorrelator,
        x: float,
        scale_gev: float,
        parton_sector: str,
    ) -> Spin1QuarkCorrelator:
        del proton, neutron, parton_sector
        f1 = convolution.f1(flavor, x, scale_gev)
        vector = diagonal_from_u_l_delta_t(f1, 0.0, 0.0).values
        return Spin1QuarkCorrelator(
            vector=vector,
            axial=np.zeros((3, 3), dtype=np.complex128),
            transverse=np.zeros((2, 3, 3), dtype=np.complex128),
        )

    return AdditionalNuclearComponentInput(
        component=component,
        source=(
            "Miller spin-averaged Sullivan pion projection arXiv:1311.4561 "
            "+ JAM21PionPDFnlo 786 replicas arXiv:2108.05822"
        ),
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.MESON_EXCHANGE,
        relative_uncertainty=0.0,
        validity=ValidityDomain(1.0e-4, 0.8, 1.14, 100.0),
        uncertainty_description=(
            "x-correlated JAM21 replicas, M_A=1.03+-0.04 GeV variants, "
            "wave-function dependence, and connected-pion model dependence"
        ),
    )


def build_minimal_fock_consistent_pion_component(
    flavor: int,
    convolution: SpinAveragedPionConvolution,
    fock_distribution: FockNormalizedMillerPionDistribution,
) -> AdditionalNuclearComponentInput:
    """Combine the pion with a transparent minimal πNN-nucleon counterterm.

    The default closure scenario assigns the πNN nucleons the same normalized
    correlator shape as the NN sector and reduces its weight by the physical
    pion plus-momentum fraction. This is the leading ``unchanged nucleon
    distribution`` approximation used in pion-excess treatments, not an
    exact result. The pion and counterterm remain algebraically identifiable.
    """

    if flavor not in LIGHT_FLAVORS:
        raise ValueError("Fock-consistent pion component requires a light flavor")
    if convolution.splitting is not fock_distribution:
        raise ValueError("convolution must use the supplied Fock-normalized splitting")
    pion_momentum = fock_distribution.ledger.pinn_sector_pion_momentum

    def component(
        proton: Spin1QuarkCorrelator,
        neutron: Spin1QuarkCorrelator,
        x: float,
        scale_gev: float,
        parton_sector: str,
    ) -> Spin1QuarkCorrelator:
        del parton_sector
        pion_f1 = convolution.f1(flavor, x, scale_gev)
        pion_vector = diagonal_from_u_l_delta_t(pion_f1, 0.0, 0.0).values
        return Spin1QuarkCorrelator(
            vector=(
                pion_vector
                - pion_momentum * (proton.vector + neutron.vector)
            ),
            axial=-pion_momentum * (proton.axial + neutron.axial),
            transverse=-pion_momentum
            * (proton.transverse + neutron.transverse),
        )

    return AdditionalNuclearComponentInput(
        component=component,
        source=(
            "Miller NN+NNpi Fock normalization with Z=1+N_pi; "
            "minimal unchanged-shape piNN nucleon closure + JAM21 pion PDF"
        ),
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.MESON_EXCHANGE,
        relative_uncertainty=1.0,
        validity=ValidityDomain(1.0e-4, 0.8, 1.14, 100.0),
        uncertainty_description=(
            "temporary 100% model uncertainty on the unchanged-shape piNN "
            "nucleon counterterm; replace with a coupled NN/NNpi spectral input"
        ),
    )


def build_longitudinal_recoil_fock_component(
    flavor: int,
    convolution: SpinAveragedPionConvolution,
    recoil: NNPiLongitudinalRecoilConvolution,
    baseline_provider: Callable[[float, float, str], Spin1QuarkCorrelator],
) -> AdditionalNuclearComponentInput:
    """Build pion plus conditionally recoiling NNπ nucleons.

    ``baseline_provider(x,Q,sector)`` must return the complete proton+neutron
    impulse correlator at arbitrary x. This extra x dependence is precisely
    what the older local unchanged-shape component could not represent.
    """

    if flavor not in LIGHT_FLAVORS:
        raise ValueError("NNpi recoil component requires a light flavor")
    if convolution.splitting is not recoil.distribution:
        raise ValueError("pion convolution and NNpi recoil must share Fock normalization")

    def component(
        proton: Spin1QuarkCorrelator,
        neutron: Spin1QuarkCorrelator,
        x: float,
        scale_gev: float,
        parton_sector: str,
    ) -> Spin1QuarkCorrelator:
        del proton, neutron

        def baseline(shifted_x: float) -> Spin1QuarkCorrelator:
            return baseline_provider(shifted_x, scale_gev, parton_sector)

        nucleon = recoil.nucleon_correction(baseline, x)
        pion_f1 = convolution.f1(flavor, x, scale_gev)
        pion_vector = diagonal_from_u_l_delta_t(pion_f1, 0.0, 0.0).values
        return Spin1QuarkCorrelator(
            vector=nucleon.vector + pion_vector,
            axial=nucleon.axial,
            transverse=nucleon.transverse,
        )

    return AdditionalNuclearComponentInput(
        component=component,
        source=(
            "Miller NN+NNpi Fock normalization and pion splitting; "
            "conditional alpha_N'=(1-eta_pi)alpha_N longitudinal recoil "
            "+ JAM21 pion PDF"
        ),
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.MESON_EXCHANGE,
        relative_uncertainty=1.0,
        validity=ValidityDomain(1.0e-4, 0.8, 1.14, 100.0),
        uncertainty_description=(
            "longitudinal recoil and exact Fock moments implemented; 100% "
            "model uncertainty retained for unresolved transverse recoil, "
            "NNpi spin entanglement, and off-shell response"
        ),
    )

def build_tensor_pion_component(
    flavor: int,
    convolution: TensorPionConvolution,
) -> AdditionalNuclearComponentInput:
    """Adapt the sourced collinear pion tensor PDF to a correlator component."""

    if flavor not in LIGHT_FLAVORS:
        raise ValueError("tensor pion component requires a light flavor")

    def component(
        proton: Spin1QuarkCorrelator,
        neutron: Spin1QuarkCorrelator,
        x: float,
        scale_gev: float,
        parton_sector: str,
    ) -> Spin1QuarkCorrelator:
        del proton, neutron, parton_sector
        delta_t = convolution.delta_t(flavor, x, scale_gev)
        vector = diagonal_from_u_l_delta_t(0.0, 0.0, delta_t).values
        return Spin1QuarkCorrelator(
            vector=vector,
            axial=np.zeros((3, 3), dtype=np.complex128),
            transverse=np.zeros((2, 3, 3), dtype=np.complex128),
        )

    return AdditionalNuclearComponentInput(
        component=component,
        source=(
            "Miller Sullivan tensor pion distribution arXiv:1311.4561 "
            "+ JAM21PionPDFnlo 786 replicas arXiv:2108.05822"
        ),
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.MESON_EXCHANGE,
        relative_uncertainty=0.0,
        validity=ValidityDomain(1.0e-4, 0.8, 1.14, 100.0),
        uncertainty_description=(
            "x-correlated JAM21 786-replica ensemble, axial-mass "
            "M_A=1.03+-0.04 GeV variants, and wave-function model dependence"
        ),
    )
