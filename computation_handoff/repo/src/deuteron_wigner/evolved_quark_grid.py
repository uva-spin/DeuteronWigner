"""Portable interpolated momentum grids for evolved T-even quark TMDs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.interpolate import RegularGridInterpolator

from .gtmd import GaugeLink
from .nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    SpinHalfQuarkCorrelator,
    compose_spin_half_quark_correlator,
)
from .nucleon_inputs import ChargeSymmetryBreakingInput

GRID_COMPONENTS = ("f1", "g1", "h1", "g1T", "h1Lperp", "h1Tperp")


def project_spin_half_quark_positivity(
    correlator: SpinHalfQuarkCorrelator,
    *,
    safety_fraction: float = 0.98,
    tolerance: float = 1.0e-12,
) -> tuple[SpinHalfQuarkCorrelator, float]:
    """Minimally scale the complete polarized density into the PSD cone.

    The unpolarized target/quark scalar is held fixed.  Every remaining
    spin, spin-orbit, and T-odd matrix component receives one common factor,
    so fitted flavor and operator relations are not independently clipped.
    """

    if not 0.0 < safety_fraction <= 1.0:
        raise ValueError("positivity safety fraction must lie in (0,1]")
    correlator.require_hermitian()
    if correlator.minimum_positivity_eigenvalue() >= -tolerance:
        return correlator, 1.0
    unpolarized = np.trace(correlator.vector).real / 2.0
    if unpolarized <= 0.0:
        raise ValueError("positive quark density requires positive f1 scalar")
    scalar = unpolarized * np.eye(2, dtype=np.complex128)
    polarized_vector = correlator.vector - scalar

    def candidate(scale: float) -> SpinHalfQuarkCorrelator:
        return SpinHalfQuarkCorrelator(
            scalar + scale * polarized_vector,
            scale * correlator.axial,
            scale * correlator.transverse,
        )

    low, high = 0.0, 1.0
    for _ in range(64):
        middle = 0.5 * (low + high)
        if candidate(middle).minimum_positivity_eigenvalue() >= 0.0:
            low = middle
        else:
            high = middle
    scale = safety_fraction * low
    result = candidate(scale)
    if result.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("spin-half quark positivity projection failed")
    return result, float(scale)


@dataclass
class EvolvedQuarkGridModel:
    """Complete correlator model replacing six T-even components from a grid."""

    baseline: FlavorResolvedNucleonQuarkModel
    grid_path: str | Path
    nucleon: str
    pretzelosity_scenario: str = "central"
    charge_symmetry_breaking: ChargeSymmetryBreakingInput | None = None
    enforce_positivity: bool = True
    positivity_safety_fraction: float = 0.98
    w_transition_start_gev: float = 1.0
    w_transition_end_gev: float = 1.5

    def __post_init__(self) -> None:
        if self.nucleon not in ("proton", "neutron"):
            raise ValueError("nucleon must be proton or neutron")
        payload = np.load(self.grid_path, allow_pickle=False)
        self.x_grid = np.asarray(payload["x"], dtype=float)
        self.k_grid = np.asarray(payload["k"], dtype=float)
        self.flavors = tuple(int(v) for v in payload["flavors"])
        self.components = tuple(str(v) for v in payload["components"])
        self.scenarios = tuple(str(v) for v in payload["scenarios"])
        if self.pretzelosity_scenario not in self.scenarios:
            raise ValueError("unknown pretzelosity scenario")
        if not (
            0.0 < self.w_transition_start_gev < self.w_transition_end_gev
        ):
            raise ValueError("invalid W-term transition interval")
        nucleon_index = 0 if self.nucleon == "proton" else 1
        values = np.asarray(payload["values"])[nucleon_index]
        scenario_index = self.scenarios.index(self.pretzelosity_scenario)
        self._interpolators = {}
        for flavor_index, flavor in enumerate(self.flavors):
            selected = []
            for component_index, name in enumerate(self.components):
                selected_scenario = (
                    scenario_index if name == "h1Tperp"
                    else self.scenarios.index("central")
                )
                selected.append(
                    values[flavor_index, component_index, selected_scenario]
                )
            component_last = np.moveaxis(np.asarray(selected), 0, -1)
            self._interpolators[flavor] = RegularGridInterpolator(
                (self.x_grid, self.k_grid), component_last,
                method="linear", bounds_error=True,
            )
        self.scale_gev = float(payload["scale_gev"])

    @property
    def nucleon_mass_gev(self) -> float:
        return self.baseline.nucleon_mass_gev

    @property
    def transfer_slope_gev2(self) -> float:
        return self.baseline.transfer_slope_gev2

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
        if not np.isclose(scale_gev, self.scale_gev, rtol=0.0, atol=1e-12):
            raise ValueError(
                f"grid fixed at Q={self.scale_gev} GeV, received {scale_gev}"
            )
        k = float(np.hypot(k_x_gev, k_y_gev))
        values = self.baseline.tmd_values(
            flavor=flavor, x=x, k_x_gev=k_x_gev, k_y_gev=k_y_gev,
            scale_gev=scale_gev, gauge_link=gauge_link,
        )
        intrinsic_tail = dict(values)
        interpolated = self._interpolators[flavor]((x, k))
        transition = np.clip(
            (k - self.w_transition_start_gev)
            / (self.w_transition_end_gev - self.w_transition_start_gev),
            0.0,
            1.0,
        )
        # C1-continuous smoothstep.  The grid is the low-k W term; the
        # positive intrinsic model supplies the unresolved W+Y tail.
        tail_weight = float(transition**2 * (3.0 - 2.0 * transition))
        for index, name in enumerate(GRID_COMPONENTS):
            values[name] = float(
                (1.0 - tail_weight) * interpolated[index]
                + tail_weight * intrinsic_tail[name]
            )
        # A W term without its perturbative Y partner is not a probability
        # density and can cross zero at large x or k.  Such nodes are outside
        # the canonical W-term domain; select the declared positive intrinsic
        # continuation for the entire six-component block rather than
        # clipping f1 alone and corrupting spin ratios.
        if values["f1"] <= 0.0:
            for name in GRID_COMPONENTS:
                values[name] = float(intrinsic_tail[name])
        if values["f1"] <= 0.0:
            # Fixed-order sea PDFs can be slightly negative at extreme
            # large-x nodes.  A density-matrix TMD model cannot represent
            # that scheme artifact as a probability.  Project the complete
            # flavor block to the zero-density boundary; no polarized or
            # T-odd remnant is retained without positive f1 support.
            for name in values:
                values[name] = 0.0
        if self.charge_symmetry_breaking is not None:
            values["f1"] *= (
                1.0
                + self.charge_symmetry_breaking.relative_correction(
                    self.nucleon, flavor, "f1", x, scale_gev
                )
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
        result = compose_spin_half_quark_correlator(
            values=self.tmd_values(
                flavor=flavor, x=x, k_x_gev=k_x_gev, k_y_gev=k_y_gev,
                scale_gev=scale_gev, gauge_link=gauge_link,
            ),
            k_x_gev=k_x_gev, k_y_gev=k_y_gev,
            delta_x_gev=delta_x_gev, delta_y_gev=delta_y_gev,
            nucleon_mass_gev=self.nucleon_mass_gev,
            transfer_slope_gev2=self.transfer_slope_gev2,
        )
        if self.enforce_positivity:
            result, _ = project_spin_half_quark_positivity(
                result, safety_fraction=self.positivity_safety_fraction
            )
        return result
