"""Small-b matching layer for leading-twist nucleon gluon TMDs.

The scalar functions in this module use the b-space convention of
Gutierrez-Reyes et al., arXiv:1907.03780.  In particular, ``h1perp`` is the
coefficient of the symmetric-traceless b-space tensor; it is not yet a
k-space function and must not be passed directly to the Cartesian correlator.

The first implementation is deliberately mixed-order and labels itself as
such: f1 and g1 use their tree-level collinear matching, while h1perp uses the
first nonzero (one-loop) finite matching coefficient in the zeta-prescription.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import Callable

import numpy as np

from .tmd_scheme import DELTA_COLLINS_ZETA_SCHEME, TMDScheme

GluonPDF = Callable[[float, float], float]
AlphaS = Callable[[float], float]

CA = 3.0
CF = 4.0 / 3.0


@lru_cache(maxsize=None)
def _legendre_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    return np.polynomial.legendre.leggauss(order)


class LargeBProfile(str, Enum):
    """Named nonperturbative profile members, not fitted central truths."""

    NONE = "none"
    NARROW = "narrow"
    CENTRAL = "central"
    BROAD = "broad"


@dataclass(frozen=True)
class GluonTMDMatchingConfig:
    """Scheme and transition choices for the initial matched layer.

    ``g2`` has units GeV^2 and multiplies b^2 in ``exp(-g2*b^2)`` when b is
    supplied in GeV^-1.  The named profile values are intentionally exposed
    as sensitivity parameters.
    """

    profile: LargeBProfile = LargeBProfile.CENTRAL
    b_max: float = 1.5
    g2_narrow: float = 0.10
    g2_central: float = 0.20
    g2_broad: float = 0.40
    convolution_order: int = 96
    scheme: TMDScheme = DELTA_COLLINS_ZETA_SCHEME

    def __post_init__(self) -> None:
        if self.b_max <= 0.0:
            raise ValueError("b_max must be positive")
        if min(self.g2_narrow, self.g2_central, self.g2_broad) < 0.0:
            raise ValueError("large-b profile coefficients cannot be negative")
        if not self.g2_narrow <= self.g2_central <= self.g2_broad:
            raise ValueError("profile coefficients must be ordered narrow-to-broad")
        if self.convolution_order < 16:
            raise ValueError("convolution_order must be at least 16")

    @property
    def g2(self) -> float:
        return {
            LargeBProfile.NONE: 0.0,
            LargeBProfile.NARROW: self.g2_narrow,
            LargeBProfile.CENTRAL: self.g2_central,
            LargeBProfile.BROAD: self.g2_broad,
        }[self.profile]


@dataclass(frozen=True)
class BSpaceGluonTMDValues:
    """Scalar b-space TMD values at a common (mu, zeta) boundary."""

    f1: float
    g1: float
    h1perp: float
    b: float
    b_star: float
    scale: float
    profile_factor: float


@dataclass(frozen=True)
class MatchedGluonTMD:
    """Initial QCD-matched b-space gluon TMD boundary.

    The one-loop linearly polarized matching is

      delta^L C[g<-g](z) = -(alpha_s/(4*pi)) CA/4 (1-z)/z
      delta^L C[g<-q](z) = -(alpha_s/(4*pi)) CF/4 (1-z)/z.

    ``quark_singlet_pdf`` must return sum_q [q(x,Q)+qbar(x,Q)].  If it is
    omitted, only the gluon channel is retained and metadata reports that
    approximation.
    """

    unpolarized_gluon_pdf: GluonPDF
    alpha_s: AlphaS
    helicity_gluon_pdf: GluonPDF | None = None
    quark_singlet_pdf: GluonPDF | None = None
    config: GluonTMDMatchingConfig = GluonTMDMatchingConfig()

    @staticmethod
    def _validate_point(x: float, b: float, scale: float) -> None:
        if not 0.0 < x <= 1.0:
            raise ValueError("x must lie in (0,1]")
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        if scale <= 0.0:
            raise ValueError("scale must be positive")

    def b_star(self, b: float) -> float:
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        return float(b / np.sqrt(1.0 + (b / self.config.b_max) ** 2))

    def profile_factor(self, b: float) -> float:
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        return float(np.exp(-self.config.g2 * b**2))

    def _linear_convolution(
        self, pdf: GluonPDF, color_factor: float, x: float, scale: float
    ) -> float:
        if x == 1.0:
            return 0.0

        nodes, weights = _legendre_rule(self.config.convolution_order)
        z = 0.5 * ((1.0 - x) * nodes + 1.0 + x)
        mapped_weights = 0.5 * (1.0 - x) * weights
        values = np.asarray(
            [(1.0 - point) * pdf(x / point, scale) / point**2 for point in z]
        )
        integral = float(np.dot(mapped_weights, values))
        return -color_factor * integral / 4.0

    def perturbative_values(
        self, x: float, b: float, scale: float
    ) -> BSpaceGluonTMDValues:
        """Return the small-b OPE boundary before the large-b profile."""

        self._validate_point(x, b, scale)
        f1 = float(self.unpolarized_gluon_pdf(x, scale))
        g1 = (
            0.0
            if self.helicity_gluon_pdf is None
            else float(self.helicity_gluon_pdf(x, scale))
        )
        linear = self._linear_convolution(
            self.unpolarized_gluon_pdf, CA, x, scale
        )
        if self.quark_singlet_pdf is not None:
            linear += self._linear_convolution(
                self.quark_singlet_pdf, CF, x, scale
            )
        h1perp = float(self.alpha_s(scale) * linear / (4.0 * np.pi))
        return BSpaceGluonTMDValues(
            f1=f1,
            g1=g1,
            h1perp=h1perp,
            b=float(b),
            b_star=self.b_star(b),
            scale=float(scale),
            profile_factor=1.0,
        )

    def values(self, x: float, b: float, scale: float) -> BSpaceGluonTMDValues:
        """Return the matched boundary times the selected large-b profile."""

        perturbative = self.perturbative_values(x, b, scale)
        factor = self.profile_factor(b)
        return BSpaceGluonTMDValues(
            f1=factor * perturbative.f1,
            g1=factor * perturbative.g1,
            h1perp=factor * perturbative.h1perp,
            b=perturbative.b,
            b_star=perturbative.b_star,
            scale=perturbative.scale,
            profile_factor=factor,
        )

    @property
    def metadata(self) -> dict[str, object]:
        """Machine-readable theory labels required on downstream outputs."""

        return {
            "space": "b_T",
            "b_unit": "GeV^-1",
            "scheme": self.config.scheme.metadata,
            "matching_accuracy": {
                "f1": "tree",
                "g1": "tree",
                "h1perp": "one-loop first nonzero",
            },
            "h1perp_coefficient_source": "arXiv:1907.03780 Eq. (3.20)-(3.21)",
            "quark_singlet_channel": self.quark_singlet_pdf is not None,
            "large_b_profile": self.config.profile.value,
            "b_max_GeV_inverse": self.config.b_max,
            "g2_GeV2": self.config.g2,
            "production_ready": False,
            "limitations": (
                "No Collins-Soper evolution yet; f1/g1 matching is tree level; "
                "large-b factor is an unfitted sensitivity profile."
            ),
        }
