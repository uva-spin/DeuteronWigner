"""Explicitly model-dependent hidden-color six-quark contribution to b1.

This module implements Eq. (14) of Miller, Phys. Rev. C 89, 045203 (2014).
The publication fixes only the charge-weighted observable b1, not a unique
flavor-resolved quark correlator.  Consequently this object deliberately does
not implement the nuclear-correlator input protocol.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np
from scipy.integrate import quad


FM_TO_GEV_INV = 5.067730716156395


@dataclass(frozen=True)
class MillerSixQuarkParameters:
    """Published central model parameters and explicit fitted normalization."""

    nucleon_mass_gev: float = 0.93891897
    constituent_mass_gev: float = 0.338
    radius_fm: float = 1.2
    probability_amplitude_product: float = 0.0015

    @property
    def radius_gev_inv(self) -> float:
        return self.radius_fm * FM_TO_GEV_INV


class MillerSixQuarkB1:
    """Charge-weighted six-quark b1 scenario, valid on 0 < x < 2."""

    source = "G. A. Miller, Phys. Rev. C 89, 045203 (2014), Eq. (14)"
    classification = "model-dependent; probability fitted to HERMES x=0.452"

    def __init__(self, parameters: MillerSixQuarkParameters | None = None):
        self.parameters = parameters or MillerSixQuarkParameters()

    def b1(self, x: float) -> float:
        if not 0.0 < x < 2.0:
            return 0.0
        p = self.parameters
        mass, quark_mass, radius = (
            p.nucleon_mass_gev,
            p.constituent_mass_gev,
            p.radius_gev_inv,
        )
        u_min = (
            (x * x * mass * mass - quark_mass * quark_mass) ** 2
            * radius
            * radius
            / (4.0 * x * x * mass * mass)
        )

        def integrand(u: float) -> float:
            bracket = 3.0 * (
                (x * x * mass * mass + quark_mass * quark_mass) * radius**2
                + u
                - 2.0
                * x
                * mass
                * radius
                * np.sqrt(u + quark_mass * quark_mass * radius**2)
            ) - u
            return np.exp(-u) * bracket

        integral = quad(integrand, u_min, np.inf, epsabs=1.0e-13)[0]
        return float(
            6.0
            * mass
            * radius
            / np.sqrt(30.0 * np.pi)
            * integral
            * p.probability_amplitude_product
        )

    def parameter_variants(self) -> dict[str, "MillerSixQuarkB1"]:
        """Published ±10% radius/mass shape tests at fixed fitted probability."""
        p = self.parameters
        return {
            "radius_minus_10pct": MillerSixQuarkB1(replace(p, radius_fm=0.9 * p.radius_fm)),
            "radius_plus_10pct": MillerSixQuarkB1(replace(p, radius_fm=1.1 * p.radius_fm)),
            "mass_minus_10pct": MillerSixQuarkB1(
                replace(p, constituent_mass_gev=0.9 * p.constituent_mass_gev)
            ),
            "mass_plus_10pct": MillerSixQuarkB1(
                replace(p, constituent_mass_gev=1.1 * p.constituent_mass_gev)
            ),
        }

    def integral_sum_rule(self) -> float:
        """Numerical valence tensor sum rule over the six-quark support."""
        return float(quad(self.b1, 1.0e-6, 2.0, epsabs=1.0e-10, limit=300)[0])
