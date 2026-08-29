"""Explicit first Collins-Soper/CSS evolution layer for gluon TMDs.

This is an intermediate one-loop CSS implementation.  It makes the evolution
and nonperturbative Collins-Soper assumptions inspectable, but it is not a
replacement for a full order-consistent TMD evolution library.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable

import numpy as np
from scipy.integrate import quad

from .gluon_tmd_matching import (
    BSpaceGluonTMDValues,
    CA,
    CF,
    MatchedGluonTMD,
)
from .quark_tmd_matching import BSpaceQuarkTMDValue, MatchedRankZeroQuarkTMD
from .tmd_scheme import (
    DELTA_COLLINS_ZETA_SCHEME,
    TMDScheme,
    TMDScalePoint,
)

AlphaS = Callable[[float], float]
EULER_GAMMA = 0.5772156649015329
C0 = 2.0 * np.exp(-EULER_GAMMA)


class NonperturbativeCSProfile(str, Enum):
    """Named uncertainty members for the unknown gluon CS kernel."""

    NONE = "none"
    LOW = "low"
    CENTRAL = "central"
    HIGH = "high"


@dataclass(frozen=True)
class GluonCSSEvolutionConfig:
    """One-loop CSS and nonperturbative-kernel configuration."""

    n_flavors: int = 4
    mu_floor: float = 1.3
    reference_scale: float = 2.0
    cs_profile: NonperturbativeCSProfile = NonperturbativeCSProfile.NONE
    gk_low: float = 0.02
    gk_central: float = 0.05
    gk_high: float = 0.10
    quadrature_epsabs: float = 1.0e-9
    quadrature_epsrel: float = 1.0e-7
    scheme: TMDScheme = DELTA_COLLINS_ZETA_SCHEME

    def __post_init__(self) -> None:
        if not 1 <= self.n_flavors <= 6:
            raise ValueError("n_flavors must lie between one and six")
        if self.mu_floor <= 0.0 or self.reference_scale <= 0.0:
            raise ValueError("evolution scales must be positive")
        if min(self.gk_low, self.gk_central, self.gk_high) < 0.0:
            raise ValueError("nonperturbative CS coefficients cannot be negative")
        if not self.gk_low <= self.gk_central <= self.gk_high:
            raise ValueError("CS profile coefficients must be ordered")

    @property
    def beta0_css(self) -> float:
        """Coefficient entering B_g^(1)=-(11 CA-2 nf)/6."""

        return (11.0 * CA - 2.0 * self.n_flavors) / 6.0

    @property
    def gk(self) -> float:
        return {
            NonperturbativeCSProfile.NONE: 0.0,
            NonperturbativeCSProfile.LOW: self.gk_low,
            NonperturbativeCSProfile.CENTRAL: self.gk_central,
            NonperturbativeCSProfile.HIGH: self.gk_high,
        }[self.cs_profile]


@dataclass(frozen=True)
class OneLoopGluonCSSEvolution:
    """Spin-independent one-loop CSS Sudakov evolution."""

    alpha_s: AlphaS
    config: GluonCSSEvolutionConfig = GluonCSSEvolutionConfig()

    def canonical_scale(self, b_star: float, final_scale: float) -> float:
        if b_star < 0.0 or final_scale <= 0.0:
            raise ValueError("b_star must be nonnegative and scale positive")
        if b_star == 0.0:
            return float(final_scale)
        return float(
            min(final_scale, max(self.config.mu_floor, C0 / b_star))
        )

    def perturbative_sudakov(
        self, b_star: float, final_scale: float
    ) -> float:
        """Return S_pert with A_g^(1)=CA and B_g^(1)=-beta0_css."""

        initial_scale = self.canonical_scale(b_star, final_scale)
        if final_scale <= initial_scale:
            return 0.0

        def integrand(log_mu: float) -> float:
            mu = np.exp(log_mu)
            logarithm = np.log(final_scale**2 / mu**2)
            return (
                self.alpha_s(float(mu))
                / np.pi
                * (CA * logarithm - self.config.beta0_css)
            )

        value, _ = quad(
            integrand,
            np.log(initial_scale),
            np.log(final_scale),
            epsabs=self.config.quadrature_epsabs,
            epsrel=self.config.quadrature_epsrel,
            limit=100,
        )
        return float(value)

    def nonperturbative_exponent(self, b: float, final_scale: float) -> float:
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        if final_scale < self.config.reference_scale:
            raise ValueError("final scale cannot be below the reference scale")
        return float(
            self.config.gk
            * b**2
            * np.log(final_scale / self.config.reference_scale)
        )

    def factor(self, b: float, b_star: float, final_scale: float) -> float:
        initial_scale = self.canonical_scale(b_star, final_scale)
        self.config.scheme.require_supported_path(
            TMDScalePoint.canonical(initial_scale),
            TMDScalePoint.canonical(final_scale),
        )
        exponent = self.perturbative_sudakov(
            b_star, final_scale
        ) + self.nonperturbative_exponent(b, final_scale)
        return float(np.exp(-exponent))

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "evolution": "one-loop CSS Sudakov",
            "A_g_1": "C_A",
            "B_g_1": "-(11 C_A - 2 n_f)/6",
            "n_flavors": self.config.n_flavors,
            "mu_floor_GeV": self.config.mu_floor,
            "reference_scale_GeV": self.config.reference_scale,
            "nonperturbative_CS_profile": self.config.cs_profile.value,
            "gk_GeV2": self.config.gk,
            "spin_independent": True,
            "scheme": self.config.scheme.metadata,
            "production_ready": False,
        }


@dataclass(frozen=True)
class EvolvedBSpaceGluonTMDValues:
    f1: float
    g1: float
    h1perp: float
    b: float
    b_star: float
    initial_scale: float
    final_scale: float
    initial_zeta_gev2: float
    final_zeta_gev2: float
    intrinsic_factor: float
    evolution_factor: float


@dataclass(frozen=True)
class EvolvedMatchedGluonTMD:
    """Evaluate matching at the canonical scale and evolve to final Q."""

    boundary: MatchedGluonTMD
    evolution: OneLoopGluonCSSEvolution

    def __post_init__(self) -> None:
        self.boundary.config.scheme.require_compatible(
            self.evolution.config.scheme
        )

    def values(
        self, x: float, b: float, final_scale: float
    ) -> EvolvedBSpaceGluonTMDValues:
        if b < 0.0:
            raise ValueError("b must be nonnegative")
        b_star = self.boundary.b_star(b)
        initial_scale = self.evolution.canonical_scale(b_star, final_scale)
        initial_point = TMDScalePoint.canonical(initial_scale)
        final_point = TMDScalePoint.canonical(final_scale)
        self.evolution.config.scheme.require_supported_path(
            initial_point, final_point
        )
        small_b: BSpaceGluonTMDValues = self.boundary.perturbative_values(
            x, b_star, initial_scale
        )
        intrinsic = self.boundary.profile_factor(b)
        evolution = self.evolution.factor(b, b_star, final_scale)
        common = intrinsic * evolution
        return EvolvedBSpaceGluonTMDValues(
            f1=common * small_b.f1,
            g1=common * small_b.g1,
            h1perp=common * small_b.h1perp,
            b=float(b),
            b_star=b_star,
            initial_scale=initial_scale,
            final_scale=float(final_scale),
            initial_zeta_gev2=initial_point.zeta_gev2,
            final_zeta_gev2=final_point.zeta_gev2,
            intrinsic_factor=intrinsic,
            evolution_factor=evolution,
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "boundary": self.boundary.metadata,
            "evolution": self.evolution.metadata,
            "production_ready": False,
            "limitations": (
                "One-loop CSS evolution with an optional unfitted gluon CS "
                "kernel profile; fixed-order matching remains mixed accuracy."
            ),
        }


@dataclass(frozen=True)
class QuarkCSSEvolutionConfig:
    """One-loop quark CSS configuration for a rank-zero LO boundary."""

    n_flavors: int = 4
    # JAMDiFF's released grid begins at Q^2=2 GeV^2.  The common composed
    # boundary must not request any constituent below its source domain.
    mu_floor: float = float(np.sqrt(2.0))
    reference_scale: float = 2.0
    gk: float = 0.0
    quadrature_epsabs: float = 1.0e-9
    quadrature_epsrel: float = 1.0e-7
    scheme: TMDScheme = DELTA_COLLINS_ZETA_SCHEME

    def __post_init__(self) -> None:
        if not 1 <= self.n_flavors <= 6:
            raise ValueError("n_flavors must lie between one and six")
        if self.mu_floor <= 0.0 or self.reference_scale <= 0.0:
            raise ValueError("evolution scales must be positive")
        if self.gk < 0.0:
            raise ValueError("gk cannot be negative")


@dataclass(frozen=True)
class OneLoopQuarkCSSEvolution:
    """Spin-independent quark Sudakov with A_q=CF and B_q=-3 CF/2."""

    alpha_s: AlphaS
    config: QuarkCSSEvolutionConfig = QuarkCSSEvolutionConfig()

    def canonical_scale(self, b_star: float, final_scale: float) -> float:
        if b_star < 0.0 or final_scale <= 0.0:
            raise ValueError("b_star must be nonnegative and scale positive")
        if b_star == 0.0:
            return float(final_scale)
        return float(min(final_scale, max(self.config.mu_floor, C0 / b_star)))

    def factor(self, b: float, b_star: float, final_scale: float) -> float:
        if b < 0.0 or final_scale < self.config.reference_scale:
            raise ValueError(
                "require b>=0 and final scale not below the reference scale"
            )
        initial = self.canonical_scale(b_star, final_scale)
        self.config.scheme.require_supported_path(
            TMDScalePoint.canonical(initial),
            TMDScalePoint.canonical(final_scale),
        )
        perturbative = 0.0
        if final_scale > initial:
            def integrand(log_mu: float) -> float:
                mu = np.exp(log_mu)
                return (
                    self.alpha_s(float(mu)) / np.pi
                    * (
                        CF * np.log(final_scale**2 / mu**2)
                        - 1.5 * CF
                    )
                )

            perturbative = quad(
                integrand,
                np.log(initial),
                np.log(final_scale),
                epsabs=self.config.quadrature_epsabs,
                epsrel=self.config.quadrature_epsrel,
                limit=100,
            )[0]
        nonperturbative = (
            self.config.gk * b**2
            * np.log(final_scale / self.config.reference_scale)
        )
        return float(np.exp(-perturbative - nonperturbative))

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "evolution": "one-loop quark CSS Sudakov",
            "A_q_1": "C_F",
            "B_q_1": "-3 C_F/2",
            "spin_independent": True,
            "nonperturbative_gk_GeV2": self.config.gk,
            "scheme": self.config.scheme.metadata,
            "production_ready": False,
        }


@dataclass(frozen=True)
class EvolvedBSpaceQuarkTMDValue:
    boundary: BSpaceQuarkTMDValue
    value: float
    initial_scale: float
    final_scale: float
    initial_zeta_gev2: float
    final_zeta_gev2: float
    evolution_factor: float


@dataclass(frozen=True)
class EvolvedMatchedRankZeroQuarkTMD:
    boundary: MatchedRankZeroQuarkTMD
    evolution: OneLoopQuarkCSSEvolution

    def __post_init__(self) -> None:
        self.boundary.config.scheme.require_compatible(
            self.evolution.config.scheme
        )

    def value(
        self, name: str, flavor: int, x: float, b: float, final_scale: float
    ) -> EvolvedBSpaceQuarkTMDValue:
        b_star = self.boundary.b_star(b)
        initial_scale = self.evolution.canonical_scale(b_star, final_scale)
        initial_point = TMDScalePoint.canonical(initial_scale)
        final_point = TMDScalePoint.canonical(final_scale)
        self.evolution.config.scheme.require_supported_path(
            initial_point, final_point
        )
        boundary = self.boundary.value(name, flavor, x, b, initial_scale)
        factor = self.evolution.factor(b, b_star, final_scale)
        return EvolvedBSpaceQuarkTMDValue(
            boundary=boundary,
            value=boundary.value * factor,
            initial_scale=initial_scale,
            final_scale=float(final_scale),
            initial_zeta_gev2=initial_point.zeta_gev2,
            final_zeta_gev2=final_point.zeta_gev2,
            evolution_factor=factor,
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "boundary": self.boundary.metadata,
            "evolution": self.evolution.metadata,
            "production_ready": False,
            "limitations": (
                "LO rank-zero boundary and one-loop Sudakov only; a complete "
                "order-consistent quark TMD treatment remains required."
            ),
        }
