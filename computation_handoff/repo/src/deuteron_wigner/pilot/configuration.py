"""Intrinsic constituent configuration with support and closure gates."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ..formal.diagnostics import ArchitectureError
from ..formal.sector_space import SectorId
from ..gtmd import Species
from ..kinematics import PartonMomentum


class ColorLabel(str, Enum):
    RED = "r"
    GREEN = "g"
    BLUE = "b"
    SINGLET = "singlet"
    NONE = "none"


@dataclass(frozen=True)
class Constituent:
    stable_id: str
    x: float
    k_t: PartonMomentum
    species: Species
    flavor: str
    color: ColorLabel
    helicity: int
    lz: int
    basis_id: str

    def __post_init__(self) -> None:
        if not 0 < self.x <= 1:
            raise ArchitectureError("C3.CONFIG.SUPPORT", "invalid momentum fraction", expected="0<x<=1", received=self.x)
        if not self.stable_id or not self.flavor or not self.basis_id:
            raise ArchitectureError("C3.CONFIG", "constituent identity incomplete", expected="stable ID/flavor/basis", received=self)


@dataclass(frozen=True)
class IntrinsicConfiguration:
    constituents: tuple[Constituent, ...]
    active_index: int
    sector: SectorId
    member_id: str
    phase_id: str
    permutation_class: str
    version: int = 1

    def __post_init__(self) -> None:
        if not self.constituents or not 0 <= self.active_index < len(self.constituents):
            raise ArchitectureError("C3.CONFIG.ACTIVE", "invalid active index", expected=f"0..{len(self.constituents)-1}", received=self.active_index)
        ids = [item.stable_id for item in self.constituents]
        if len(ids) != len(set(ids)):
            raise ArchitectureError("C3.CONFIG.DUPLICATE", "duplicate constituent identity", expected="unique IDs", received=ids)
        if abs(sum(item.x for item in self.constituents) - 1) > 1e-13:
            raise ArchitectureError("C3.CONFIG.SUPPORT", "fractions do not sum to one", expected=1.0, received=sum(item.x for item in self.constituents))
        kx = sum(item.k_t.x for item in self.constituents)
        ky = sum(item.k_t.y for item in self.constituents)
        if abs(kx) > 1e-13 or abs(ky) > 1e-13:
            raise ArchitectureError("C3.CONFIG.CLOSURE", "intrinsic transverse momenta do not close", expected=(0.0, 0.0), received=(kx, ky))

    def with_active(self, index: int) -> "IntrinsicConfiguration":
        return type(self)(self.constituents, index, self.sector, self.member_id, self.phase_id, self.permutation_class, self.version)
