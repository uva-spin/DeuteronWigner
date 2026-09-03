"""Declared boundary models for exploratory nucleon GTMD inputs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

CollinearPDF = Callable[[int, float, float], float]


@dataclass(frozen=True)
class FactorizedGaussianGTMD:
    """Helicity-independent, rank-zero nucleon GTMD boundary model.

    The transverse-momentum dependence is normalized to unity and the
    transfer dependence is a Gaussian:

    ``W = q(x) exp(-k_T^2/width)/(pi*width) exp(-slope*Delta_T^2/2) I/2``.

    ``width`` and transverse momenta use the same squared units; ``slope``
    uses the inverse squared unit.  The identity divided by two makes the
    active-nucleon helicity trace equal to the scalar GTMD.
    """

    pdf: CollinearPDF
    width: float
    slope: float

    def __post_init__(self) -> None:
        if self.width <= 0.0:
            raise ValueError("Gaussian GTMD width must be positive")
        if self.slope < 0.0:
            raise ValueError("Gaussian GTMD slope cannot be negative")

    def scalar(
        self,
        flavor: int,
        x: float,
        k_x: np.ndarray | float,
        k_y: np.ndarray | float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        if not 0.0 < x <= 1.0:
            return np.zeros(np.broadcast(k_x, k_y).shape, dtype=np.float64)
        k2 = np.asarray(k_x) ** 2 + np.asarray(k_y) ** 2
        delta2 = delta_x**2 + delta_y**2
        return (
            self.pdf(flavor, x, scale)
            * np.exp(-k2 / self.width)
            / (np.pi * self.width)
            * np.exp(-0.5 * self.slope * delta2)
        )

    def collinear(
        self,
        flavor: int,
        x: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> float:
        if not 0.0 < x <= 1.0:
            return 0.0
        return float(
            self.pdf(flavor, x, scale)
            * np.exp(-0.5 * self.slope * (delta_x**2 + delta_y**2))
        )

    def __call__(
        self,
        flavor: int,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        return complex(
            self.scalar(flavor, x, k_x, k_y, delta_x, delta_y, scale)
        ) * np.eye(2) / 2.0
