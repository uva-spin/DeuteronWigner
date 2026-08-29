"""Complete transverse sensitivity parents for non-nucleonic spin-1 sectors."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np

from .canonical_parent_enrichment import (
    FockAmplitude,
    NonNucleonicFockLedger,
    NonNucleonicSector,
    SharedFockOAMLedger,
)
from .gluon_correlator import Spin1GluonCorrelator, compose_spin1_gluon_correlator
from .quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    T_ODD_QUARK_TMDS,
    Spin1QuarkCorrelator,
    compose_spin1_quark_correlator,
)


GLUON_NAMES = (
    "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
    "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
    "h1LTperp", "f1TT_minus_h1TTperp", "g1TT", "h1TT",
    "h1TTperpperp",
)
GLUON_TODD = frozenset({
    "h1Lperp", "f1Tperp", "h1", "h1Tperp", "g1LT", "g1TT",
})


def default_nonnucleonic_ledger() -> NonNucleonicFockLedger:
    """Conservative sensitivity probabilities; generic sectors are zero-centred.

    The sourced Miller/JAM21/Vpion19 NNpi correlator is activated in the
    canonical exporters through its own amplitude identity. Enabling this
    generic NNpi interface as well would double count it.
    """

    probability = {
        NonNucleonicSector.NNPI: 0.020847851903810458,
        NonNucleonicSector.DELTADELTA: 0.004,
        NonNucleonicSector.HIDDEN_COLOR: 0.010,
        NonNucleonicSector.SRC: 0.060,
    }
    momentum = {
        NonNucleonicSector.NNPI: 0.020847851903810458,
        NonNucleonicSector.DELTADELTA: 0.004,
        NonNucleonicSector.HIDDEN_COLOR: 0.010,
        NonNucleonicSector.SRC: 0.060,
    }
    return NonNucleonicFockLedger(probability, momentum, {})


def _sector_ledger(sector: NonNucleonicSector) -> SharedFockOAMLedger:
    phases = {
        NonNucleonicSector.NNPI: (0.12j, -0.04 + 0.02j),
        NonNucleonicSector.DELTADELTA: (0.18 + 0.05j, 0.08j),
        NonNucleonicSector.HIDDEN_COLOR: (-0.14 + 0.10j, 0.12 - 0.04j),
        NonNucleonicSector.SRC: (0.22 - 0.06j, -0.09 + 0.03j),
    }[sector]
    return SharedFockOAMLedger((
        FockAmplitude(f"{sector.value}_L0", "axial", 0, 1.0, "sensitivity"),
        FockAmplitude(f"{sector.value}_L1", "axial", 1, phases[0], "sensitivity"),
        FockAmplitude(
            f"{sector.value}_L2",
            "quark_gluon" if sector == NonNucleonicSector.HIDDEN_COLOR else "axial",
            2, phases[1], "sensitivity",
        ),
    )).normalized()


@dataclass(frozen=True)
class NonNucleonicTransverseModel:
    ledger: NonNucleonicFockLedger = default_nonnucleonic_ledger()
    deuteron_mass_gev: float = 1.87561294257
    widths_gev2: Mapping[NonNucleonicSector, float] = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "widths_gev2", dict(self.widths_gev2 or {
            NonNucleonicSector.NNPI: 0.24,
            NonNucleonicSector.DELTADELTA: 0.38,
            NonNucleonicSector.HIDDEN_COLOR: 0.55,
            NonNucleonicSector.SRC: 0.65,
        }))
        if set(self.widths_gev2) != set(NonNucleonicSector):
            raise ValueError("all non-nucleonic widths are required")

    def _radial(self, sector: NonNucleonicSector, k: float) -> float:
        width = self.widths_gev2[sector]
        return float(np.exp(-k*k/width) / (np.pi*width))

    def _longitudinal(self, sector: NonNucleonicSector, x_n: float) -> float:
        """Model-dependent beta shape, normalized to unity at x_N=0.1."""
        if not 0.0 < x_n < 1.0:
            raise ValueError("non-nucleonic parent requires 0<x_N<1")
        alpha, beta = {
            NonNucleonicSector.NNPI: (-0.15, 4.5),
            NonNucleonicSector.DELTADELTA: (0.35, 5.0),
            NonNucleonicSector.HIDDEN_COLOR: (0.55, 6.0),
            NonNucleonicSector.SRC: (0.70, 3.5),
        }[sector]
        shape = x_n**alpha * (1.0-x_n)**beta
        reference = 0.1**alpha * 0.9**beta
        return float(shape/reference)

    def quark_tmds(
        self, sector: NonNucleonicSector, flavor: int,
        k_gev: float, staple_sign: int, x_n: float = 0.1,
    ) -> dict[str, float]:
        if flavor not in (2, 1, -2, -1) or staple_sign not in (-1, 1):
            raise ValueError("unsupported flavor or staple")
        c = _sector_ledger(sector).shared_tmd_coordinates()
        flavor_weight = {2: 0.38, 1: 0.34, -2: 0.13, -1: 0.15}[flavor]
        base = (
            flavor_weight * self._longitudinal(sector, x_n)
            * self._radial(sector, k_gev)
        )
        tensor = {
            NonNucleonicSector.NNPI: -0.08,
            NonNucleonicSector.DELTADELTA: 0.12,
            NonNucleonicSector.HIDDEN_COLOR: 0.18,
            NonNucleonicSector.SRC: -0.10,
        }[sector]
        result = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
        even = {
            "f1": 1.0, "g1": 0.08*c["rank0_density"],
            "h1": 0.06*c["rank0_density"],
            "g1T": 0.08*c["rank1_even"],
            "h1Lperp": -0.08*c["rank1_even"],
            "h1Tperp": 0.06*c["rank2_even"],
            "f1LL": tensor, "f1LT": 0.08*c["rank1_even"],
            "f1TT": 0.06*c["rank2_even"],
        }
        odd_coordinate = 0.05*c["rank1_odd"]
        for name in result:
            if name in even:
                result[name] = base * even[name]
            elif name in T_ODD_QUARK_TMDS:
                rank_factor = c["rank2_odd"] if "TT" in name else c["rank1_odd"]
                result[name] = staple_sign * base * 0.04 * rank_factor
        return result

    def quark_parent(
        self, sector: NonNucleonicSector, flavor: int,
        momentum_gev: tuple[float, float], staple_sign: int,
        x_n: float = 0.1,
    ) -> Spin1QuarkCorrelator:
        k = float(np.hypot(*momentum_gev))
        raw = self.quark_tmds(sector, flavor, k, staple_sign, x_n)
        return self._positive_quark(momentum_gev, raw)

    def _positive_quark(self, momentum, values) -> Spin1QuarkCorrelator:
        def candidate(scale):
            trial = {
                name: value if name == "f1" else scale*value
                for name, value in values.items()
            }
            return compose_spin1_quark_correlator(
                momentum, self.deuteron_mass_gev, trial
            )
        if candidate(1.0).minimum_positivity_eigenvalue() >= -1e-12:
            return candidate(1.0)
        low, high = 0.0, 1.0
        for _ in range(60):
            middle = (low+high)/2
            if candidate(middle).minimum_positivity_eigenvalue() >= 0:
                low = middle
            else:
                high = middle
        return candidate(0.95*low)

    def gluon_tmds(
        self, sector: NonNucleonicSector, k_gev: float, staple_sign: int,
        x_n: float = 0.1,
    ) -> dict[str, float]:
        if staple_sign not in (-1, 1):
            raise ValueError("staple sign must be +/-1")
        c = _sector_ledger(sector).shared_tmd_coordinates()
        base = self._longitudinal(sector, x_n) * self._radial(sector, k_gev)
        result = {name: 0.0 for name in GLUON_NAMES}
        result.update({
            "f1": base, "g1": 0.08*base*c["rank0_density"],
            "h1perp": 0.05*base*c["rank2_even"],
            "g1T": 0.05*base*c["rank1_even"],
            "f1LL": 0.10*base*c["rank0_density"],
            "f1LT": 0.05*base*c["rank1_even"],
            "f1TT_minus_h1TTperp": 0.04*base*c["rank2_even"],
        })
        for name in GLUON_TODD:
            coordinate = c["rank2_odd"] if "TT" in name else c["rank1_odd"]
            result[name] = staple_sign * 0.035*base*coordinate
        return result

    def gluon_parent(
        self, sector: NonNucleonicSector,
        momentum_gev: tuple[float, float], staple_sign: int,
        x_n: float = 0.1,
    ) -> Spin1GluonCorrelator:
        k = float(np.hypot(*momentum_gev))
        values = self.gluon_tmds(sector, k, staple_sign, x_n)
        def candidate(scale):
            trial = {
                name: value if name == "f1" else scale*value
                for name, value in values.items()
            }
            return compose_spin1_gluon_correlator(
                momentum_gev, self.deuteron_mass_gev, trial
            )
        if candidate(1).minimum_positivity_eigenvalue() >= -1e-12:
            return candidate(1)
        low, high = 0.0, 1.0
        for _ in range(60):
            middle = (low+high)/2
            if candidate(middle).minimum_positivity_eigenvalue() >= 0:
                low = middle
            else:
                high = middle
        return candidate(0.95*low)
