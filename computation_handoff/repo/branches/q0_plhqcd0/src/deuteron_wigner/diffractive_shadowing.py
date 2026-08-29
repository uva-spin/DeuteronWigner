"""H1-DPDF implementation of leading-twist deuteron shadowing.

This module implements Eq. (4) of Frankfurt, Guzey and Strikman,
arXiv:hep-ph/0601123, using the official H1 2007 Jets DPDF grids and flux
convention.  The output is a fractional correction to a supplied proton plus
neutron inclusive parton density, suitable for the correlator-level nuclear
mechanism interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
from typing import Callable

import numpy as np

from .provenance import EvidenceClass

_FLOAT = re.compile(r"[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[Ee][+-]?\d+)?")


@dataclass(frozen=True)
class H1Grid:
    """Bilinear log(z)-log(Q2) interpolation of an official H1 grid."""

    log_z: np.ndarray
    log_q2: np.ndarray
    z_times_density: np.ndarray

    @staticmethod
    def load(path: str | Path) -> "H1Grid":
        values = np.asarray(
            [float(item) for item in _FLOAT.findall(Path(path).read_text())],
            dtype=float,
        )
        expected = 100 + 88 + 100 * 88
        if values.size != expected:
            raise ValueError(
                f"H1 grid {path} has {values.size} values; expected {expected}"
            )
        log_z = values[:100]
        q2 = values[100:188]
        table = values[188:].reshape(88, 100).T
        if not np.all(np.diff(log_z) > 0.0) or not np.all(np.diff(q2) > 0.0):
            raise ValueError("H1 grid axes must be strictly increasing")
        if np.any(~np.isfinite(table)):
            raise ValueError("H1 DPDF grid must contain finite densities")
        return H1Grid(log_z, np.log(q2), table)

    def value(self, z: float, q2_gev2: float) -> float:
        """Return z*f(z,Q2), with the official boundary-clamping convention."""

        if z <= 0.0 or q2_gev2 <= 0.0:
            raise ValueError("DPDF arguments must be positive")
        x = float(np.clip(np.log(z), self.log_z[0], self.log_z[-1]))
        y = float(np.clip(np.log(q2_gev2), self.log_q2[0], self.log_q2[-1]))
        i = int(np.clip(np.searchsorted(self.log_z, x) - 1, 0, 98))
        j = int(np.clip(np.searchsorted(self.log_q2, y) - 1, 0, 86))
        xd = (x - self.log_z[i]) / (self.log_z[i + 1] - self.log_z[i])
        yd = (y - self.log_q2[j]) / (self.log_q2[j + 1] - self.log_q2[j])
        f00 = self.z_times_density[i, j]
        f10 = self.z_times_density[i + 1, j]
        f01 = self.z_times_density[i, j + 1]
        f11 = self.z_times_density[i + 1, j + 1]
        return float(
            (1.0 - xd) * (1.0 - yd) * f00
            + xd * (1.0 - yd) * f10
            + (1.0 - xd) * yd * f01
            + xd * yd * f11
        )


@dataclass(frozen=True)
class H12007JetsDPDF:
    singlet: H1Grid
    gluon: H1Grid
    alpha_pomeron_0: float = 1.1037
    alpha_prime_gev2: float = 0.06
    flux_slope_gev2: float = 5.5
    flux_normalization_x: float = 0.003
    proton_mass_gev: float = 0.93827231

    @staticmethod
    def load(directory: str | Path) -> "H12007JetsDPDF":
        root = Path(directory)
        return H12007JetsDPDF(
            H1Grid.load(root / "h12007jetsdpdf_singlet.data"),
            H1Grid.load(root / "h12007jetsdpdf_gluon.data"),
        )

    def _unnormalized_flux_integral(
        self, x_pomeron: float, *, slope_shift_gev2: float = 0.0
    ) -> float:
        t_min = -(self.proton_mass_gev * x_pomeron) ** 2 / (1.0 - x_pomeron)
        slope = (
            self.flux_slope_gev2 + slope_shift_gev2
            + 2.0 * self.alpha_prime_gev2 * np.log(1.0 / x_pomeron)
        )
        return float(
            x_pomeron ** (1.0 - 2.0 * self.alpha_pomeron_0)
            * (np.exp(slope * t_min) - np.exp(-slope))
            / slope
        )

    @property
    def flux_normalization(self) -> float:
        x0 = self.flux_normalization_x
        return 1.0 / (x0 * self._unnormalized_flux_integral(x0))

    def varied_flux_normalization(self, slope_shift_gev2: float) -> float:
        x0 = self.flux_normalization_x
        return 1.0 / (
            x0
            * self._unnormalized_flux_integral(
                x0, slope_shift_gev2=slope_shift_gev2
            )
        )

    def differential_flux(
        self, x_pomeron: float, q_t2_gev2: float, *, slope_shift_gev2: float = 0.0
    ) -> float:
        """Return f_IP/p(x_IP,t), differential in positive qT^2=-t-qL^2."""

        if not 0.0 < x_pomeron < 1.0 or q_t2_gev2 < 0.0:
            raise ValueError("invalid Pomeron flux arguments")
        t = -q_t2_gev2 - (
            self.proton_mass_gev * x_pomeron
        ) ** 2 / (1.0 - x_pomeron)
        alpha_t = self.alpha_pomeron_0 + self.alpha_prime_gev2 * t
        slope = self.flux_slope_gev2 + slope_shift_gev2
        if slope <= 0.0:
            raise ValueError("Pomeron t slope must remain positive")
        return float(
            self.varied_flux_normalization(slope_shift_gev2)
            * x_pomeron ** (1.0 - 2.0 * alpha_t)
            * np.exp(slope * t)
        )

    def parton_density(self, sector: str, beta: float, q2_gev2: float) -> float:
        """Return f_i/IP, not beta*f_i/IP.

        The H1 singlet is divided equally among u,d,s and their antiquarks,
        as assumed by the H1 light-flavor singlet parameterization.
        """

        bounded_beta = max(float(beta), np.exp(self.singlet.log_z[0]))
        if sector == "gluon":
            return self.gluon.value(bounded_beta, q2_gev2) / bounded_beta
        if sector not in ("valence", "sea"):
            raise ValueError(f"unsupported diffractive sector {sector}")
        return self.singlet.value(bounded_beta, q2_gev2) / (6.0 * bounded_beta)


@dataclass(frozen=True)
class TabulatedBodyFormFactor:
    momentum_gev: np.ndarray
    value_array: np.ndarray

    @staticmethod
    def load(path: str | Path) -> "TabulatedBodyFormFactor":
        table = np.genfromtxt(path, delimiter=",", names=True)
        q = np.asarray(table["DeltaT_GeV"], dtype=float)
        values = np.asarray(table["normalized_body_form_factor"], dtype=float)
        if q[0] != 0.0 or not np.all(np.diff(q) > 0.0):
            raise ValueError("body-form-factor table requires a monotonic zero origin")
        if not np.isclose(values[0], 1.0, atol=1.0e-10):
            raise ValueError("body form factor must be normalized to one")
        return TabulatedBodyFormFactor(q, values)

    def value(self, momentum_gev: float) -> float:
        if momentum_gev < 0.0:
            raise ValueError("form-factor momentum cannot be negative")
        if momentum_gev > self.momentum_gev[-1]:
            return 0.0
        return float(np.interp(momentum_gev, self.momentum_gev, self.value_array))


InclusiveDensity = Callable[[float, float], float]


def build_h1_deuteron_shadowing_input(
    *,
    inclusive_density: InclusiveDensity,
    body_form_factor: TabulatedBodyFormFactor,
    dpdf: H12007JetsDPDF,
    integration_points: int = 48,
):
    """Build a `DiffractiveShadowingInput` from the FGS double-scattering term."""

    # Imported locally to keep the grid/parser layer independent of correlators.
    from .nuclear_mechanisms import DiffractiveShadowingInput

    if integration_points < 16:
        raise ValueError("DPDF shadowing requires at least 16-point quadrature")
    nodes, weights = np.polynomial.legendre.leggauss(integration_points)
    eta = 0.5 * np.pi * (dpdf.alpha_pomeron_0 - 1.0)
    # The factor 2 is the deuteron ordered-pair interference coefficient.
    # 16*pi converts the HERA differential diffractive-PDF normalization to
    # the forward rescattering normalization (FGS, PRD 71, 054001, Eq. (2)).
    diffraction_conversion = 16.0 * np.pi
    real_part_factor = (
        2.0
        * diffraction_conversion
        * (1.0 - eta**2)
        / (1.0 + eta**2)
    )
    q_t2_max = body_form_factor.momentum_gev[-1] ** 2 / 4.0

    def calculate(
        sector: str,
        x: float,
        q_gev: float,
        *,
        normalization: float = 1.0,
        slope_shift_gev2: float = 0.0,
    ) -> float:
        x_max = 0.03 if sector == "gluon" else 0.1
        if x >= x_max:
            return 0.0
        denominator = float(inclusive_density(x, q_gev))
        if denominator <= 0.0:
            raise ValueError("inclusive p+n density must be positive")
        xp = 0.5 * ((x_max - x) * nodes + x_max + x)
        xp_weights = 0.5 * (x_max - x) * weights
        qt2 = 0.5 * q_t2_max * (nodes + 1.0)
        qt2_weights = 0.5 * q_t2_max * weights
        integral = 0.0
        for x_pomeron, wx in zip(xp, xp_weights):
            beta = x / float(x_pomeron)
            pomeron_density = dpdf.parton_density(
                sector, beta, q_gev**2
            )
            for q_t2, wt in zip(qt2, qt2_weights):
                momentum = 2.0 * np.sqrt(
                    q_t2 + (float(x_pomeron) * dpdf.proton_mass_gev) ** 2
                )
                integral += (
                    wx
                    * wt
                    * dpdf.differential_flux(
                        float(x_pomeron),
                        float(q_t2),
                        slope_shift_gev2=slope_shift_gev2,
                    )
                    * pomeron_density
                    * body_form_factor.value(float(momentum))
                )
        return float(max(0.0, normalization * real_part_factor * integral / denominator))

    @lru_cache(maxsize=512)
    def central(sector: str, x: float, q_gev: float) -> float:
        return calculate(sector, x, q_gev)

    members = {
        "dpdf_norm_down": lambda sector, x, q: calculate(
            sector, x, q, normalization=0.8
        ),
        "dpdf_norm_up": lambda sector, x, q: calculate(
            sector, x, q, normalization=1.2
        ),
        "t_slope_down": lambda sector, x, q: calculate(
            sector, x, q, slope_shift_gev2=-1.1
        ),
        "t_slope_up": lambda sector, x, q: calculate(
            sector, x, q, slope_shift_gev2=1.1
        ),
    }
    return DiffractiveShadowingInput(
        fraction=central,
        source=(
            "H1 2007 Jets DPDF v1.0 official singlet/gluon grids and flux; "
            "FGS arXiv:hep-ph/0601123 Eq. (4); wave-specific LF body form factor"
        ),
        relative_uncertainty=0.2,
        classification=EvidenceClass.PHENOMENOLOGY,
        uncertainty_members=members,
        applies_longitudinal_coherence=False,
    )
