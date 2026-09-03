"""Momentum-space and parent adapter for evolved rank-zero quark TMDs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
from scipy.integrate import simpson
from scipy.special import j0
from scipy.special import j1
from scipy.special import jv

from .gtmd import GaugeLink
from .nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    SpinHalfQuarkCorrelator,
    compose_spin_half_quark_correlator,
)
from .tmd_evolution import EvolvedMatchedRankZeroQuarkTMD


@dataclass
class EvolvedRankZeroQuarkModel:
    """Replace f1/g1/h1 in a complete model by their evolved J0 transforms.

    All other components remain supplied by ``baseline`` in their native
    momentum-space conventions.  This makes the partial scope explicit while
    providing the same ``correlator`` interface consumed by the LF parent.
    """

    baseline: FlavorResolvedNucleonQuarkModel
    evolved: EvolvedMatchedRankZeroQuarkTMD
    b_max_gev_inverse: float = 12.0
    n_b: int = 401
    n_rank_one_scales: int = 25
    evolve_rank_one: bool = True
    evolve_rank_two: bool = True
    _cache: dict[tuple[str, int, float, float], np.ndarray] = field(
        default_factory=dict, init=False, repr=False
    )
    _evolution_cache: dict[float, tuple[np.ndarray, np.ndarray]] = field(
        default_factory=dict, init=False, repr=False
    )
    _rank_one_cache: dict[tuple[str, int, float, float], np.ndarray] = field(
        default_factory=dict, init=False, repr=False
    )
    _rank_two_cache: dict[tuple[int, float, float], np.ndarray] = field(
        default_factory=dict, init=False, repr=False
    )

    def __post_init__(self) -> None:
        if self.evolved.boundary.nucleon is not self.baseline:
            raise ValueError("evolved boundary and baseline must share one nucleon model")
        if self.b_max_gev_inverse <= 0.0 or self.n_b < 101 or self.n_b % 2 == 0:
            raise ValueError("require positive b_max and odd n_b >= 101")
        if self.n_rank_one_scales < 9 or self.n_rank_one_scales % 2 == 0:
            raise ValueError("n_rank_one_scales must be odd and at least 9")
        self._b = np.linspace(0.0, self.b_max_gev_inverse, self.n_b)

    @property
    def nucleon_mass_gev(self) -> float:
        return self.baseline.nucleon_mass_gev

    @property
    def transfer_slope_gev2(self) -> float:
        return self.baseline.transfer_slope_gev2

    def _b_values(
        self, name: str, flavor: int, x: float, scale: float
    ) -> np.ndarray:
        key = (name, flavor, float(x), float(scale))
        if key not in self._cache:
            if scale not in self._evolution_cache:
                b_star = np.asarray([
                    self.evolved.boundary.b_star(float(b)) for b in self._b
                ])
                initial = np.asarray([
                    self.evolved.evolution.canonical_scale(float(bs), scale)
                    for bs in b_star
                ])
                factors = np.asarray([
                    self.evolved.evolution.factor(
                        float(b), float(bs), scale
                    )
                    for b, bs in zip(self._b, b_star)
                ])
                self._evolution_cache[scale] = initial, factors
            initial, factors = self._evolution_cache[scale]
            boundary_values = np.asarray([
                self.evolved.boundary.value(
                    name, flavor, x, float(b), float(mu)
                ).value
                for b, mu in zip(self._b, initial)
            ])
            self._cache[key] = boundary_values * factors
        return self._cache[key]

    def _momentum_value(
        self, name: str, flavor: int, x: float, k: float, scale: float
    ) -> float:
        values = self._b_values(name, flavor, x, scale)
        integrand = self._b * j0(self._b * k) * values / (2.0 * np.pi)
        return float(simpson(integrand, x=self._b))

    def _rank_one_b_values(
        self, name: str, flavor: int, x: float, scale: float
    ) -> np.ndarray:
        if name not in ("g1T", "h1Lperp"):
            raise ValueError("rank-one adapter supports g1T and h1Lperp")
        key = (name, flavor, float(x), float(scale))
        if key not in self._rank_one_cache:
            # Populate the common canonical scales and Sudakov factors.
            self._b_values("f1", flavor, x, scale)
            initial, factors = self._evolution_cache[scale]
            component = self.baseline.components[name]
            width = component.width(flavor)
            scale_nodes = np.geomspace(float(np.min(initial)), scale,
                                       self.n_rank_one_scales)
            node_values = np.asarray([
                component.value(flavor, x, float(mu)) for mu in scale_nodes
            ])
            collinear = np.interp(
                np.log(initial), np.log(scale_nodes), node_values
            )
            intrinsic = np.exp(-width * self._b**2 / 4.0)
            # For F_i(k)=k_i F(k)/M and the project Fourier convention,
            # F~_i(b)=i b_hat_i R(b), with
            # R(b)=F_collinear*width*b*exp(-width*b^2/4)/(2M).
            self._rank_one_cache[key] = (
                collinear
                * width
                * self._b
                * intrinsic
                * factors
                / (2.0 * self.nucleon_mass_gev)
            )
        return self._rank_one_cache[key]

    def _rank_one_momentum_value(
        self, name: str, flavor: int, x: float, k: float, scale: float
    ) -> float:
        radial = self._rank_one_b_values(name, flavor, x, scale)
        if k == 0.0:
            return float(
                self.nucleon_mass_gev
                * simpson(self._b**2 * radial, x=self._b)
                / (4.0 * np.pi)
            )
        return float(
            self.nucleon_mass_gev
            * simpson(
                self._b * j1(self._b * k) * radial, x=self._b
            )
            / (2.0 * np.pi * k)
        )

    def _rank_two_b_values(
        self, flavor: int, x: float, scale: float
    ) -> np.ndarray:
        key = (flavor, float(x), float(scale))
        if key not in self._rank_two_cache:
            self._b_values("f1", flavor, x, scale)
            initial, factors = self._evolution_cache[scale]
            component = self.baseline.components["h1Tperp"]
            width = component.width(flavor)
            scale_nodes = np.geomspace(
                float(np.min(initial)), scale, self.n_rank_one_scales
            )
            node_values = np.asarray([
                component.value(flavor, x, float(mu)) for mu in scale_nodes
            ])
            collinear = np.interp(
                np.log(initial), np.log(scale_nodes), node_values
            )
            intrinsic = np.exp(-width * self._b**2 / 4.0)
            # The project correlator contains
            # -k_ST^{ij} h1Tperp/M^2. Its forward transform is
            # (bhat_i bhat_j-delta_ij/2) R2(b), with the Gaussian
            # R2=A*width^2*b^2*exp(-width*b^2/4)/(4M^2).
            self._rank_two_cache[key] = (
                collinear
                * width**2
                * self._b**2
                * intrinsic
                * factors
                / (4.0 * self.nucleon_mass_gev**2)
            )
        return self._rank_two_cache[key]

    def _rank_two_momentum_value(
        self, flavor: int, x: float, k: float, scale: float
    ) -> float:
        radial = self._rank_two_b_values(flavor, x, scale)
        if k == 0.0:
            return float(
                self.nucleon_mass_gev**2
                * simpson(self._b**3 * radial, x=self._b)
                / (16.0 * np.pi)
            )
        return float(
            self.nucleon_mass_gev**2
            * simpson(
                self._b * jv(2, self._b * k) * radial, x=self._b
            )
            / (2.0 * np.pi * k**2)
        )

    def tmd_values(
        self,
        *,
        flavor: int,
        x: float,
        k_x_gev: float,
        k_y_gev: float,
        scale_gev: float,
        gauge_link: GaugeLink,
    ) -> dict[str, float]:
        values = self.baseline.tmd_values(
            flavor=flavor,
            x=x,
            k_x_gev=k_x_gev,
            k_y_gev=k_y_gev,
            scale_gev=scale_gev,
            gauge_link=gauge_link,
        )
        k = float(np.hypot(k_x_gev, k_y_gev))
        for name in ("f1", "g1", "h1"):
            values[name] = self._momentum_value(
                name, flavor, x, k, scale_gev
            )
        if self.evolve_rank_one:
            for name in ("g1T", "h1Lperp"):
                values[name] = self._rank_one_momentum_value(
                    name, flavor, x, k, scale_gev
                )
        if self.evolve_rank_two:
            values["h1Tperp"] = self._rank_two_momentum_value(
                flavor, x, k, scale_gev
            )
        return values

    def correlator(
        self,
        *,
        flavor: int,
        x: float,
        k_x_gev: float,
        k_y_gev: float,
        delta_x_gev: float,
        delta_y_gev: float,
        scale_gev: float,
        gauge_link: GaugeLink,
    ) -> SpinHalfQuarkCorrelator:
        values = self.tmd_values(
            flavor=flavor,
            x=x,
            k_x_gev=k_x_gev,
            k_y_gev=k_y_gev,
            scale_gev=scale_gev,
            gauge_link=gauge_link,
        )
        return compose_spin_half_quark_correlator(
            values=values,
            k_x_gev=k_x_gev,
            k_y_gev=k_y_gev,
            delta_x_gev=delta_x_gev,
            delta_y_gev=delta_y_gev,
            nucleon_mass_gev=self.nucleon_mass_gev,
            transfer_slope_gev2=self.transfer_slope_gev2,
        )

    @property
    def metadata(self) -> dict[str, Any]:
        return {
            "adapter": "rank-zero evolved b-space to momentum-space LF parent",
            "replaced_components": ["f1", "g1", "h1"],
            "native_components": ["h1perp", "f1Tperp"],
            "rank_one_components": ["g1T", "h1Lperp"],
            "rank_one_evolution_enabled": self.evolve_rank_one,
            "rank_one_scale_nodes": self.n_rank_one_scales,
            "rank_two_components": ["h1Tperp"],
            "rank_two_evolution_enabled": self.evolve_rank_two,
            "b_max_GeV_inverse": self.b_max_gev_inverse,
            "n_b": self.n_b,
            "evolution": self.evolved.metadata,
            "production_ready": False,
        }
