"""Normalized analytic states for C3 Benchmarks A--D."""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, pi, sqrt

import numpy as np

from ..formal.diagnostics import ArchitectureError
from ..formal.sector_space import ResolutionLayer, SectorId
from ..gtmd import Species
from .configuration import ColorLabel, Constituent, IntrinsicConfiguration


def pilot_sector(name: str, quarks=()) -> SectorId:
    occupations = tuple(sorted((flavor, quarks.count(flavor)) for flavor in set(quarks)))
    charge = sum({"u": 2, "d": -1}.get(flavor, 0) for flavor in quarks)
    return SectorId(ResolutionLayer.MICROSCOPIC_FOCK, occupations, (), 0, charge, "pilot", "positive", "singlet", name, "validation_only")


@dataclass(frozen=True)
class PointState:
    stable_id: str = "C3:A:POINT"
    member_id: str = "analytic_exact"
    production_authorized: bool = False

    def amplitude(self, configuration: IntrinsicConfiguration) -> complex:
        if len(configuration.constituents) != 1:
            raise ArchitectureError("C3.STATE", "point state requires one body", expected=1, received=len(configuration.constituents))
        return 1 + 0j


@dataclass(frozen=True)
class GaussianScalarState:
    beta_gev: float
    stable_id: str = "C3:B:GAUSSIAN"
    member_id: str = "analytic_validation_width"
    production_authorized: bool = False

    def __post_init__(self) -> None:
        if self.beta_gev <= 0:
            raise ArchitectureError("C3.STATE", "Gaussian beta must be positive", expected=">0", received=self.beta_gev)

    def normalization(self, x: float) -> float:
        return 1 / sqrt(pi * self.beta_gev**2 * x * (1 - x))

    def amplitude(self, configuration: IntrinsicConfiguration) -> complex:
        item = configuration.constituents[configuration.active_index]
        if len(configuration.constituents) != 2 or not 0 < item.x < 1:
            raise ArchitectureError("C3.STATE", "scalar spectator state requires 0<x<1 and two bodies", expected="two-body support", received=(len(configuration.constituents), item.x))
        width = self.beta_gev**2 * item.x * (1 - item.x)
        return self.normalization(item.x) * exp(-item.k_t.norm_squared() / (2 * width))

    def analytic_overlap(self, x: float, k2: float, delta2: float) -> float:
        width = self.beta_gev**2 * x * (1 - x)
        return self.normalization(x) ** 2 * exp(-(k2 + (1 - x) ** 2 * delta2 / 4) / width)

    def promote_width_to_production(self):
        raise ArchitectureError("C3.ISOLATE.WIDTH", "analytic Gaussian width cannot become accepted model configuration", expected="validation-only beta", received=self.beta_gev)


@dataclass(frozen=True)
class SpinorOAMState:
    amplitudes: tuple[complex, complex, complex]  # Lz=0,+1,-1
    reference_mass_gev: float
    stable_id: str = "C3:C:SPINOR_OAM"
    member_id: str = "controlled_algebraic_interference"
    production_authorized: bool = False

    def __post_init__(self) -> None:
        if self.reference_mass_gev <= 0 or sum(abs(x) ** 2 for x in self.amplitudes) == 0:
            raise ArchitectureError("C3.STATE", "invalid spinor/OAM amplitudes", expected="positive mass and nonzero norm", received=(self.reference_mass_gev, self.amplitudes))

    def normalized(self) -> np.ndarray:
        values = np.asarray(self.amplitudes, complex)
        return values / np.linalg.norm(values)

    def helicity_matrix(self) -> np.ndarray:
        a0, ap, am = self.normalized()
        vector = np.asarray((a0, ap, am, (ap + am) / sqrt(2)), complex)
        return np.outer(vector, vector.conj()) / np.vdot(vector, vector).real

    def rank_one_interference(self) -> complex:
        a0, ap, am = self.normalized()
        return a0.conjugate() * (ap - am)

    def phase_odd(self) -> float:
        return float(self.rank_one_interference().imag)

    def amplitude(self, configuration: IntrinsicConfiguration) -> complex:
        item = configuration.constituents[configuration.active_index]
        a0, ap, am = self.normalized()
        return a0 + ap * (item.k_t.x + 1j * item.k_t.y) / self.reference_mass_gev + am * (item.k_t.x - 1j * item.k_t.y) / self.reference_mass_gev


@dataclass(frozen=True)
class ThreeQuarkColorState:
    flavors: tuple[str, str, str] = ("u", "u", "d")
    stable_id: str = "C3:D:PROTON_COLOR_SINGLET"
    member_id: str = "epsilon_abc_over_sqrt6"
    production_authorized: bool = False

    def __post_init__(self) -> None:
        if sorted(self.flavors) != ["d", "u", "u"]:
            raise ArchitectureError("C3.COLOR.FLAVOR", "proton benchmark requires uud, not flavor equality", expected=("u", "u", "d"), received=self.flavors)

    def color_tensor(self) -> np.ndarray:
        tensor = np.zeros((3, 3, 3), complex)
        for permutation in ((0,1,2),(1,2,0),(2,0,1)):
            tensor[permutation] = 1 / sqrt(6)
        for permutation in ((0,2,1),(2,1,0),(1,0,2)):
            tensor[permutation] = -1 / sqrt(6)
        return tensor

    def color_norm(self) -> float:
        return float(np.vdot(self.color_tensor(), self.color_tensor()).real)

    def amplitude(self, configuration: IntrinsicConfiguration) -> complex:
        if len(configuration.constituents) != 3:
            raise ArchitectureError("C3.STATE", "color benchmark requires three constituents", expected=3, received=len(configuration.constituents))
        color_index = {ColorLabel.RED: 0, ColorLabel.GREEN: 1, ColorLabel.BLUE: 2}
        try:
            indices = tuple(color_index[item.color] for item in configuration.constituents)
        except KeyError as exc:
            raise ArchitectureError("C3.COLOR.NONSINGLET", "invalid color basis for singlet", expected="r,g,b", received=tuple(item.color for item in configuration.constituents)) from exc
        return complex(self.color_tensor()[indices])

    def counts(self) -> dict[str, int]:
        return {flavor: self.flavors.count(flavor) for flavor in sorted(set(self.flavors))}

    def total_color_generator_residual(self) -> float:
        tensor = self.color_tensor()
        generators = _su3_generators()
        maximum = 0.0
        for generator in generators:
            transformed = (
                np.einsum("ia,ajk->ijk", generator, tensor)
                + np.einsum("ja,iak->ijk", generator, tensor)
                + np.einsum("ka,ija->ijk", generator, tensor)
            )
            maximum = max(maximum, float(np.max(np.abs(transformed))))
        return maximum


def neutron_from_proton(state: ThreeQuarkColorState) -> ThreeQuarkColorState:
    mapped = tuple({"u": "d", "d": "u"}[flavor] for flavor in state.flavors)
    result = object.__new__(ThreeQuarkColorState)
    object.__setattr__(result, "flavors", mapped)
    object.__setattr__(result, "stable_id", "C3:D:NEUTRON_COLOR_SINGLET")
    object.__setattr__(result, "member_id", state.member_id)
    object.__setattr__(result, "production_authorized", False)
    return result


def _su3_generators() -> tuple[np.ndarray, ...]:
    zero = 0j
    matrices = (
        ((0,1,0),(1,0,0),(0,0,0)),
        ((0,-1j,0),(1j,0,0),(0,0,0)),
        ((1,0,0),(0,-1,0),(0,0,0)),
        ((0,0,1),(0,0,0),(1,0,0)),
        ((0,0,-1j),(0,0,0),(1j,0,0)),
        ((0,0,0),(0,0,1),(0,1,0)),
        ((0,0,0),(0,0,-1j),(0,1j,0)),
        ((1/sqrt(3),0,0),(0,1/sqrt(3),0),(0,0,-2/sqrt(3))),
    )
    return tuple(0.5 * np.asarray(item, complex) for item in matrices)
