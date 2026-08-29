"""Distributional PV-plus-cut evaluation with a nonphysical epsilon oracle."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Callable

import numpy as np

from ...formal.diagnostics import ArchitectureError


@dataclass(frozen=True)
class PoleIntegral:
    pv: float
    cut: complex
    total: complex
    jacobian: float

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["cut"] = [self.cut.real, self.cut.imag]
        value["total"] = [self.total.real, self.total.imag]
        return value


@dataclass(frozen=True)
class EpsilonConvergence:
    epsilons: tuple[float, ...]
    values: tuple[complex, ...]
    target: complex
    final_residual: float
    epsilon_is_physical: bool = False

    def __post_init__(self) -> None:
        if self.epsilon_is_physical:
            raise ArchitectureError("C5.DIST.2", "epsilon cannot be stored as a physical phase width", expected=False, received=True)


class DistributionalPoleEvaluator:
    """One-dimensional reference realization of the coarea formula."""

    def pv_plus_cut(
        self, function: Callable[[np.ndarray], np.ndarray], *,
        eta: int, support: float, jacobian: float = 1.0, points: int = 200001,
    ) -> PoleIntegral:
        if eta not in (-1, 1) or jacobian <= 0 or points < 1001:
            raise ArchitectureError("C5.DIST.1", "invalid distributional integration metadata", expected="eta=+/-1,jacobian>0,points>=1001", received=(eta, jacobian, points))
        # Symmetric paired quadrature makes the principal value explicit.
        positive = np.linspace(support / (points // 2), support, points // 2)
        pv = float(np.trapz((function(positive) - function(-positive)) / positive, positive))
        f0 = float(np.asarray(function(np.asarray([0.0])))[0])
        cut = 1j * eta * np.pi * f0 / jacobian
        return PoleIntegral(pv, cut, pv + cut, jacobian)

    def epsilon_sequence(
        self, function: Callable[[np.ndarray], np.ndarray], *,
        eta: int, support: float, epsilons: tuple[float, ...],
        points_per_epsilon: int = 300001,
    ) -> EpsilonConvergence:
        target = self.pv_plus_cut(function, eta=eta, support=support).total
        values = []
        for epsilon in epsilons:
            if epsilon <= 0:
                raise ArchitectureError("C5.DIST.2", "epsilon oracle requires positive refinements", expected="epsilon>0", received=epsilon)
            # Direct complex integration of 1/(x-i eta epsilon).
            x = np.linspace(-support, support, points_per_epsilon)
            values.append(complex(np.trapz(function(x) / (x - 1j * eta * epsilon), x)))
        return EpsilonConvergence(epsilons, tuple(values), target, abs(values[-1] - target))


def compact_bump(x: np.ndarray, support: float = 1.0) -> np.ndarray:
    value = np.zeros_like(x, dtype=float)
    inside = np.abs(x) < support
    z = x[inside] / support
    value[inside] = (1 - z * z) ** 4
    return value
