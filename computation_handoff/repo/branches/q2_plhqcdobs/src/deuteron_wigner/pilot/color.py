"""Exact finite SU(3) color tensors for C4 sea and gluon benchmarks."""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

import numpy as np

from ..formal.diagnostics import ArchitectureError
from .states import _su3_generators


def levi_civita3() -> np.ndarray:
    value = np.zeros((3, 3, 3), complex)
    for item in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        value[item] = 1
    for item in ((0, 2, 1), (2, 1, 0), (1, 0, 2)):
        value[item] = -1
    return value


def structure_constants() -> np.ndarray:
    generators = _su3_generators()
    values = np.zeros((8, 8, 8), float)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                commutator = generators[a] @ generators[b] - generators[b] @ generators[a]
                values[a, b, c] = float((-2j * np.trace(commutator @ generators[c])).real)
    return values


@dataclass(frozen=True)
class SeaColorSinglet:
    stable_id: str = "C4:COLOR:QQQQQBAR_CLUSTER_SINGLET"
    construction: str = "epsilon_abc/sqrt6 times delta_de/sqrt3"
    basis_status: str = "CLUSTER_BASIS_NOT_FULLY_ANTISYMMETRIZED"

    def tensor(self) -> np.ndarray:
        return np.einsum("abc,de->abcde", levi_civita3() / sqrt(6), np.eye(3) / sqrt(3))

    def norm(self) -> float:
        return float(np.vdot(self.tensor(), self.tensor()).real)

    def generator_residual(self, *, antiquark_sign: int = -1) -> float:
        tensor = self.tensor()
        maximum = 0.0
        for generator in _su3_generators():
            transformed = (
                np.einsum("Aa,abcde->Abcde", generator, tensor)
                + np.einsum("Bb,abcde->aBcde", generator, tensor)
                + np.einsum("Cc,abcde->abCde", generator, tensor)
                + np.einsum("Dd,abcde->abcDe", generator, tensor)
                + antiquark_sign * np.einsum("Ee,abcdE->abcde", generator, tensor)
            )
            maximum = max(maximum, float(np.max(np.abs(transformed))))
        return maximum

    def validate(self, tolerance: float = 1e-15) -> None:
        if abs(self.norm() - 1) > tolerance or self.generator_residual() > tolerance:
            raise ArchitectureError(
                "C4.SEA_COLOR.NONSINGLET", "five-parton tensor is not a normalized singlet",
                expected=f"norm=1,residual<={tolerance}",
                received=(self.norm(), self.generator_residual()),
            )


@dataclass(frozen=True)
class GluonColorSinglet:
    stable_id: str = "C4:COLOR:QQQG_OCTET_ADJOINT_SINGLET"
    multiplicity_channel: str = "rho-octet: antisymmetric first quark pair"
    construction: str = "N epsilon_ijm (t^a)_km"

    def tensor(self) -> np.ndarray:
        epsilon = levi_civita3()
        generators = _su3_generators()
        raw = np.stack(
            [np.einsum("ijm,km->ijk", epsilon, generator) for generator in generators],
            axis=-1,
        )
        return raw / sqrt(float(np.vdot(raw, raw).real))

    def norm(self) -> float:
        tensor = self.tensor()
        return float(np.vdot(tensor, tensor).real)

    def generator_residual(self, *, include_adjoint: bool = True) -> float:
        tensor = self.tensor()
        generators = _su3_generators()
        constants = structure_constants()
        maximum = 0.0
        for index, generator in enumerate(generators):
            transformed = (
                np.einsum("Ii,ijka->Ijka", generator, tensor)
                + np.einsum("Jj,ijka->iJka", generator, tensor)
                + np.einsum("Kk,ijka->ijKa", generator, tensor)
            )
            if include_adjoint:
                transformed += np.einsum(
                    "Aa,ijka->ijkA", -1j * constants[index], tensor
                )
            maximum = max(maximum, float(np.max(np.abs(transformed))))
        return maximum

    def validate(self, tolerance: float = 3e-16) -> None:
        if abs(self.norm() - 1) > tolerance or self.generator_residual() > tolerance:
            raise ArchitectureError(
                "C4.GLUON_COLOR.NONSINGLET", "qqqg tensor is not a normalized singlet",
                expected=f"norm=1,residual<={tolerance}",
                received=(self.norm(), self.generator_residual()),
            )


def reject_singlet_times_free_gluon() -> None:
    raise ArchitectureError(
        "C4.GLUON_COLOR.FREE_GLUON",
        "qqq singlet times a free adjoint gluon is not a total singlet",
        expected="qqq octet coupled to adjoint", received="singlet x adjoint",
    )
