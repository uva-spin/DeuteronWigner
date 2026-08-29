"""Explicit ordered-product SU(3) f/d color projections."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ..states import _su3_generators
from ..wilson_line.color_guard import structure_constants, symmetric_constants


class ColorChannel(str, Enum):
    F_TYPE = "F_TYPE"
    D_TYPE = "D_TYPE"


def ordered_trace_tensor(order: tuple[int, int, int] = (0, 1, 2)) -> np.ndarray:
    generators = _su3_generators()
    result = np.zeros((8, 8, 8), complex)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                items = (generators[a], generators[b], generators[c])
                result[a, b, c] = np.trace(items[order[0]] @ items[order[1]] @ items[order[2]])
    return result


def antisymmetric_ordered_coupler() -> np.ndarray:
    return 2 * (ordered_trace_tensor((0, 1, 2)) - ordered_trace_tensor((1, 0, 2)))


def symmetric_ordered_coupler() -> np.ndarray:
    return 2 * (ordered_trace_tensor((0, 1, 2)) + ordered_trace_tensor((1, 0, 2)))


@dataclass(frozen=True)
class ColorProjection:
    channel: ColorChannel
    amplitude: complex
    normalization: float
    stable_id: str


@dataclass(frozen=True)
class ThreeAdjointColorKernel:
    tensor: np.ndarray
    ordering_id: str
    stable_id: str = "C6:COLOR:THREE_ADJOINT_KERNEL"

    @classmethod
    def from_ordered_couplers(cls, antisymmetric_weight: complex, symmetric_weight: complex) -> "ThreeAdjointColorKernel":
        return cls(
            antisymmetric_weight * antisymmetric_ordered_coupler()
            + symmetric_weight * symmetric_ordered_coupler(),
            "TRACE(abc)_MINUS_PLUS_TRACE(bac)",
        )

    def project(self, channel: ColorChannel) -> ColorProjection:
        f = structure_constants()
        d = symmetric_constants()
        if channel == ColorChannel.F_TYPE:
            value = np.einsum("abc,abc->", -1j * f, self.tensor) / 24
            return ColorProjection(channel, complex(value), 24.0, "C6:RED:COLOR:F")
        value = np.einsum("abc,abc->", d, self.tensor) / (40 / 3)
        return ColorProjection(channel, complex(value), 40 / 3, "C6:RED:COLOR:D")

    def decompose(self) -> tuple[ColorProjection, ColorProjection, np.ndarray, float]:
        f_projection = self.project(ColorChannel.F_TYPE)
        d_projection = self.project(ColorChannel.D_TYPE)
        parallel = (
            1j * structure_constants() * f_projection.amplitude
            + symmetric_constants() * d_projection.amplitude
        )
        residual = self.tensor - parallel
        return f_projection, d_projection, parallel, float(np.linalg.norm(residual))

    def require_fd_subspace(self, tolerance: float = 1e-12) -> None:
        residual = self.decompose()[3]
        if residual > tolerance:
            raise ArchitectureError("C6.COLOR.4", "three-adjoint tensor has a nonzero orthogonal color residual", expected=f"<={tolerance}", received=residual)


def reject_default_mixture() -> None:
    raise ArchitectureError("C6.COLOR.6", "no default f+d active-gluon mixture exists", expected="explicit process-qualified color channel", received="F_PLUS_D")
