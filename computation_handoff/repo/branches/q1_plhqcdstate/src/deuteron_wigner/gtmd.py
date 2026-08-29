"""Sampled zero-skewness spin-1 GTMD parent correlators and marginals."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np
from scipy.integrate import simpson

from .fourier import gtmd_to_wigner
from .kinematics import BDelta
from .spin import HelicityMatrix


class Species(str, Enum):
    QUARK = "q"
    ANTIQUARK = "qbar"
    GLUON = "g"


@dataclass(frozen=True)
class GaugeLink:
    """Minimal process/gauge-link label; no process equivalence is implied."""

    incoming: str
    outgoing: str

    def __post_init__(self) -> None:
        allowed = {"+", "-"}
        if self.incoming not in allowed or self.outgoing not in allowed:
            raise ValueError("gauge-link directions must be '+' or '-'")

    def label(self) -> str:
        return f"[{self.incoming},{self.outgoing}]"


@dataclass(frozen=True)
class SampledGTMD:
    """A sampled parent W(x,kx,ky,Delta_x,Delta_y) with target helicity indices.

    Array shape is ``(nx,nkx,nky,ndx,ndy,3,3)``. This dense reference
    representation is intended for algebra tests and small fixtures; production
    integrations may use lazy/callable backends behind the same marginal API.
    """

    species: Species
    projection: str
    gauge_link: GaugeLink
    x: np.ndarray
    k_x: np.ndarray
    k_y: np.ndarray
    delta_x: np.ndarray
    delta_y: np.ndarray
    values: np.ndarray

    def __post_init__(self) -> None:
        axes = tuple(np.asarray(axis, dtype=np.float64) for axis in (
            self.x, self.k_x, self.k_y, self.delta_x, self.delta_y
        ))
        for name, axis in zip(("x", "k_x", "k_y", "delta_x", "delta_y"), axes):
            if axis.ndim != 1 or len(axis) < 2 or not np.all(np.diff(axis) > 0.0):
                raise ValueError(f"{name} must be a strictly increasing one-dimensional axis")
        expected = tuple(len(axis) for axis in axes) + (3, 3)
        values = np.asarray(self.values, dtype=np.complex128)
        if values.shape != expected:
            raise ValueError(f"GTMD values have shape {values.shape}, expected {expected}")
        object.__setattr__(self, "x", axes[0])
        object.__setattr__(self, "k_x", axes[1])
        object.__setattr__(self, "k_y", axes[2])
        object.__setattr__(self, "delta_x", axes[3])
        object.__setattr__(self, "delta_y", axes[4])
        object.__setattr__(self, "values", values)

    @staticmethod
    def _zero_index(axis: np.ndarray, tolerance: float = 1e-14) -> int:
        candidates = np.flatnonzero(np.abs(axis) <= tolerance)
        if len(candidates) != 1:
            raise ValueError("forward-limit axis must contain exactly one zero")
        return int(candidates[0])

    def tmd(self) -> HelicityMatrix:
        dx0 = self._zero_index(self.delta_x)
        dy0 = self._zero_index(self.delta_y)
        return HelicityMatrix(self.values[:, :, :, dx0, dy0, :, :])

    def gpd(self) -> HelicityMatrix:
        integrated_ky = simpson(self.values, x=self.k_y, axis=2)
        integrated = simpson(integrated_ky, x=self.k_x, axis=1)
        return HelicityMatrix(integrated)

    def pdf_from_tmd(self) -> HelicityMatrix:
        tmd = self.tmd().values
        integrated_ky = simpson(tmd, x=self.k_y, axis=2)
        integrated = simpson(integrated_ky, x=self.k_x, axis=1)
        return HelicityMatrix(integrated)

    def pdf_from_gpd(self) -> HelicityMatrix:
        dx0 = self._zero_index(self.delta_x)
        dy0 = self._zero_index(self.delta_y)
        return HelicityMatrix(self.gpd().values[:, dx0, dy0, :, :])

    def wigner_at(
        self,
        *,
        x_index: int,
        k_x_index: int,
        k_y_index: int,
        points: list[BDelta],
    ) -> HelicityMatrix:
        delta_values = self.values[x_index, k_x_index, k_y_index, :, :, :, :]
        return HelicityMatrix(
            gtmd_to_wigner(self.delta_x, self.delta_y, delta_values, points)
        )

