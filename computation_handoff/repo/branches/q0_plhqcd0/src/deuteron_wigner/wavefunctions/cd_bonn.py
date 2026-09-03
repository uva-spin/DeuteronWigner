"""CD-Bonn analytic deuteron wave function from Machleidt Appendix D."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import quad

from .models import RadialWaveFunction


@dataclass(frozen=True)
class CDBonnParameters:
    """Appendix D exponential coefficients in double precision."""

    gamma: float
    m0: float
    masses: np.ndarray
    c: np.ndarray
    d: np.ndarray

    def coordinate(self, r: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        radius = np.asarray(r, dtype=np.float64)
        if np.any(radius < 0.0):
            raise ValueError("r must be nonnegative")
        scalar = radius.ndim == 0
        flat = np.atleast_1d(radius)
        at_origin = flat == 0.0
        safe_radius = np.where(at_origin, 1.0, flat)
        mr = self.masses[:, None] * safe_radius[None, :]
        exponential = np.exp(-mr)
        u = self.c @ exponential
        with np.errstate(divide="ignore", invalid="ignore"):
            d_kernel = exponential * (1.0 + 3.0 / mr + 3.0 / mr**2)
        w = self.d @ d_kernel
        if np.any(at_origin):
            # The coefficient constraints make both limits zero, but the individual
            # D-wave terms are singular at r=0 and must not be evaluated separately.
            u = np.where(at_origin, 0.0, u)
            w = np.where(at_origin, 0.0, w)
        if scalar:
            return np.asarray(u[0]), np.asarray(w[0])
        return u, w

    def momentum(self, k: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        momentum = np.asarray(k, dtype=np.float64)
        if np.any(momentum < 0.0):
            raise ValueError("k must be nonnegative")
        scalar = momentum.ndim == 0
        flat = np.atleast_1d(momentum)
        denominators = flat[None, :] ** 2 + self.masses[:, None] ** 2
        factor = np.sqrt(2.0 / np.pi)
        u = factor * np.sum(self.c[:, None] / denominators, axis=0)
        # The relative minus sign is the i**L Fourier phase for L=2. It is
        # required for Eq. (D13) to reproduce the positive-r CD-Bonn D wave.
        w = -factor * np.sum(self.d[:, None] / denominators, axis=0)
        if scalar:
            return np.asarray(u[0]), np.asarray(w[0])
        return u, w

    def coordinate_norms(self) -> tuple[float, float]:
        u_norm = quad(lambda r: float(self.coordinate(r)[0]) ** 2, 0.0, np.inf, epsabs=1e-11)[0]
        w_norm = quad(lambda r: float(self.coordinate(r)[1]) ** 2, 0.0, np.inf, epsabs=1e-11)[0]
        return u_norm, w_norm

    def momentum_norms(self) -> tuple[float, float]:
        u_norm = quad(
            lambda k: k**2 * float(self.momentum(k)[0]) ** 2,
            0.0,
            np.inf,
            epsabs=1e-11,
        )[0]
        w_norm = quad(
            lambda k: k**2 * float(self.momentum(k)[1]) ** 2,
            0.0,
            np.inf,
            epsabs=1e-11,
        )[0]
        return u_norm, w_norm

    def on_coordinate_grid(self, grid: np.ndarray) -> RadialWaveFunction:
        u, w = self.coordinate(grid)
        return RadialWaveFunction(
            name="CD-Bonn",
            representation="coordinate",
            grid=grid,
            u=u,
            w=w,
            source="Machleidt, Phys. Rev. C 63, 024001 (2001), Appendix D",
        )

    def on_momentum_grid(self, grid: np.ndarray) -> RadialWaveFunction:
        u, w = self.momentum(grid)
        return RadialWaveFunction(
            name="CD-Bonn",
            representation="momentum",
            grid=grid,
            u=u,
            w=w,
            source="Machleidt, Phys. Rev. C 63, 024001 (2001), Appendix D",
        )


def _complete_d_coefficients(masses: np.ndarray, known: np.ndarray) -> np.ndarray:
    """Enforce the three Appendix D origin constraints for the D wave.

    The conditions are sum(D_j)=sum(D_j*m_j**2)=sum(D_j/m_j**2)=0.
    They are algebraically equivalent to Eq. (D24) and its cyclic permutations.
    """

    if known.shape != (8,):
        raise ValueError("CD-Bonn requires the first eight D coefficients")
    unknown_masses = masses[8:]
    matrix = np.vstack(
        (
            np.ones(3),
            unknown_masses**2,
            1.0 / unknown_masses**2,
        )
    )
    rhs = -np.array(
        (
            np.sum(known),
            np.sum(known * masses[:8] ** 2),
            np.sum(known / masses[:8] ** 2),
        )
    )
    return np.concatenate((known, np.linalg.solve(matrix, rhs)))


def cd_bonn_parameters() -> CDBonnParameters:
    """Return the CD-Bonn n=11 analytic parameterization.

    Coefficients are Table XX; gamma, m0, and constraints are Eqs. (D6), (D23)-(D25).
    """

    gamma = 0.2315380
    m0 = 0.9
    masses = gamma + np.arange(11, dtype=np.float64) * m0
    c_known = np.array(
        [
            0.88472985,
            -0.26408759,
            -0.044114404,
            -14.397512,
            85.591256,
            -318.76761,
            703.36701,
            -900.49586,
            661.45441,
            -259.58894,
        ],
        dtype=np.float64,
    )
    c = np.concatenate((c_known, [-np.sum(c_known)]))
    d_known = np.array(
        [
            0.022623762,
            -0.50471056,
            0.56278897,
            -16.079764,
            111.26803,
            -446.67490,
            1098.5907,
            -1611.4995,
        ],
        dtype=np.float64,
    )
    d = _complete_d_coefficients(masses, d_known)
    return CDBonnParameters(gamma=gamma, m0=m0, masses=masses, c=c, d=d)
