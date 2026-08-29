"""Reduced-helicity correlator model for the complete spin-1 TMD basis.

The model is deliberately organized at correlator level.  A small set of
shared reduced amplitudes is projected onto the named definite-rank TMD
basis.  It is not a fit, but unlike the legacy completion model it never
assigns independent priors to individual missing TMDs.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Mapping

import numpy as np

from .complete_tmd_model import GaugeLink
from .gtmd import Species
from .registry import TMDEntry, TMDRegistry

M_DEUTERON_GEV = 1.87561294257


@dataclass(frozen=True)
class CorrelatorParameters:
    """Shared dynamical parameters of the reduced correlator."""

    width_quark: float = 0.25
    width_gluon: float = 0.30
    d_probability: float = 0.0578
    spin_orbit: float = 0.32
    linear_gluon: float = 0.38
    tensor_coherence: float = 0.45
    gauge_phase: float = 0.10
    sea_spin_dilution: float = 0.55
    evolution_broadening: float = 0.035

    def varied(self, **changes: float) -> "CorrelatorParameters":
        return replace(self, **changes)

    def width(self, species: Species, scale: float) -> float:
        intrinsic = (
            self.width_gluon if species == Species.GLUON else self.width_quark
        )
        return intrinsic + self.evolution_broadening * np.log(max(scale, 1.0) / 2.0)


@dataclass(frozen=True)
class CollinearAnchors:
    """Collinear normalizations entering the reduced amplitudes."""

    f1: float
    g1: float
    f1ll: float
    h1: float = 0.0


@dataclass(frozen=True)
class CorrelatorPrediction:
    value: float
    physical_ratio: float
    origin: str


# Rows of the symmetry projector.  Columns are reduced helicity structures:
# helicity, transversity/linear polarization, spin-orbit, tensor,
# tensor-spin-orbit, and double-helicity coherence.  The numerical factors
# are fixed Clebsch-like convention coefficients, not fitted TMD amplitudes.
_QUARK_PROJECTOR: Mapping[str, tuple[float, ...]] = {
    "h1perp": (0, 0, 1, 0, 0, 0),
    "h1Lperp": (1, -1, 0, 0, 0, 0),
    "f1Tperp": (0, 0, 1, 0, 0, 0),
    "g1T": (1, 0, 1, 0, 0, 0),
    "h1Tperp": (0, 1, -1, 0, 0, 0),
    "h1LLperp": (0, 0, 0, 1, 1, 0),
    "f1LT": (0, 0, 0, 1, 1, 0),
    "g1LT": (1, 0, 0, 1, -1, 0),
    "h1LT": (0, 1, 0, 1, 0, 0),
    "h1LTperp": (0, 1, 0, 1, -1, 0),
    "f1TT": (0, 0, 0, 1, 0, 1),
    "g1TT": (1, 0, 0, 1, 0, -1),
    "h1TT": (0, 1, 0, 1, 0, 1),
    "h1TTperp": (0, 1, 0, 1, 0, -1),
}

_GLUON_PROJECTOR: Mapping[str, tuple[float, ...]] = {
    "h1perp": (0, 1, 0, 0, 0, 0),
    "h1Lperp": (1, 1, 0, 0, 0, 0),
    "f1Tperp": (0, 0, 1, 0, 0, 0),
    "g1T": (1, 0, 1, 0, 0, 0),
    "h1": (0, 1, 1, 0, 0, 0),
    "h1Tperp": (0, 1, -1, 0, 0, 0),
    "h1LLperp": (0, 1, 0, 1, 0, 0),
    "f1LT": (0, 0, 0, 1, 1, 0),
    "g1LT": (1, 0, 0, 1, -1, 0),
    "h1LT": (0, 1, 0, 1, 1, 0),
    "h1LTperp": (0, 1, 0, 1, -1, 0),
    "f1TT": (0, 0, 0, 1, 0, 1),
    "g1TT": (1, 0, 0, 1, 0, -1),
    "h1TT": (0, 1, 0, 1, 0, 1),
    "h1TTperp": (0, 1, 0, 1, 0, -1),
    "h1TTperpperp": (0, 1, 0, 1, 0, 0.5),
}


class ReducedCorrelatorTMDModel:
    """Project a common reduced correlator onto every registry entry."""

    def __init__(
        self,
        registry: TMDRegistry,
        species: Species,
        anchors: CollinearAnchors,
        parameters: CorrelatorParameters = CorrelatorParameters(),
    ) -> None:
        self.registry = registry
        self.species = species
        self.anchors = anchors
        self.parameters = parameters
        expected = Species.GLUON if species == Species.GLUON else species
        if any(entry.species != expected for entry in registry.select()):
            raise ValueError("registry species does not match correlator model")
        if anchors.f1 <= 0:
            raise ValueError("the unpolarized collinear anchor must be positive")

    def _gaussian(self, k: float, scale: float) -> float:
        width = self.parameters.width(self.species, scale)
        return float(np.exp(-(k * k) / width) / (np.pi * width))

    def _reduced_amplitudes(self) -> np.ndarray:
        p = self.parameters
        orbital = np.sqrt(max(p.d_probability * (1.0 - p.d_probability), 0.0))
        helicity = np.clip(self.anchors.g1 / self.anchors.f1, -0.85, 0.85)
        if self.species == Species.ANTIQUARK:
            helicity *= p.sea_spin_dilution
        transverse = (
            p.linear_gluon
            if self.species == Species.GLUON
            else np.clip(self.anchors.h1 / self.anchors.f1, -0.75, 0.75)
        )
        tensor = np.clip(self.anchors.f1ll / self.anchors.f1, -0.25, 0.25)
        spin_orbit = p.spin_orbit * orbital
        tensor_orbit = p.tensor_coherence * orbital * np.sign(tensor or -1.0)
        double_flip = p.tensor_coherence * p.d_probability
        return np.asarray(
            (helicity, transverse, spin_orbit, tensor, tensor_orbit, double_flip)
        )

    def _coefficient(self, entry: TMDEntry) -> float:
        projector = (
            _GLUON_PROJECTOR if self.species == Species.GLUON else _QUARK_PROJECTOR
        )
        row = projector.get(entry.name)
        if row is None:
            raise KeyError(f"no correlator projector for {self.species.value}:{entry.name}")
        reduced = self._reduced_amplitudes()
        # The common normalization keeps the complete spin correction in a
        # conservative positive-density domain.
        coefficient = 0.32 * float(np.dot(np.asarray(row), reduced))
        if entry.t_odd:
            coefficient *= self.parameters.gauge_phase
        return coefficient

    def predict(
        self,
        entry: TMDEntry,
        *,
        k: float,
        scale: float,
        gauge_link: GaugeLink,
    ) -> CorrelatorPrediction:
        if k < 0 or scale <= 0:
            raise ValueError("require k>=0 and scale>0")
        width = self.parameters.width(self.species, scale)
        profile = self._gaussian(k, scale)
        base = self.anchors.f1 * profile
        direct = {
            "f1": self.anchors.f1,
            "g1": self.anchors.g1,
            "f1LL": self.anchors.f1ll,
            "h1": self.anchors.h1,
        }
        if entry.name in direct and not (
            self.species == Species.GLUON and entry.name == "h1"
        ):
            value = direct[entry.name] * profile
            return CorrelatorPrediction(
                float(value),
                float(value / base),
                "collinear_anchor",
            )

        coefficient = self._coefficient(entry)
        if entry.t_odd:
            coefficient *= gauge_link.t_odd_sign
        rank_shape = (M_DEUTERON_GEV / np.sqrt(width)) ** entry.transverse_rank
        rank_shape *= np.exp(-0.5 * entry.transverse_rank * k * k / width)
        if entry.name == "h1LT" and entry.transverse_rank == 0:
            # The full radial factor is exp(-2u)(1-2u), whose 2-D integral
            # vanishes exactly.
            u = k * k / width
            rank_shape *= (1.0 - 2.0 * u) * np.exp(-u)
        value = coefficient * base * rank_shape
        physical = (k / M_DEUTERON_GEV) ** entry.transverse_rank
        return CorrelatorPrediction(
            float(value),
            float(physical * value / base),
            "reduced_correlator_projection",
        )

    def predict_all(
        self, *, k: float, scale: float, gauge_link: GaugeLink
    ) -> dict[str, CorrelatorPrediction]:
        return {
            entry.name: self.predict(
                entry, k=k, scale=scale, gauge_link=gauge_link
            )
            for entry in self.registry.select()
        }

    def require_physical_bounds(
        self, predictions: Mapping[str, CorrelatorPrediction], limit: float = 1.0
    ) -> None:
        for name, prediction in predictions.items():
            if abs(prediction.physical_ratio) > limit + 1.0e-12:
                raise ValueError(
                    f"{self.species.value}:{name} physical modulation "
                    f"{prediction.physical_ratio:g} exceeds {limit:g}"
                )
