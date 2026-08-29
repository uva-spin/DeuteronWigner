"""Validated containers for reduced deuteron radial wave functions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Optional

import numpy as np
from scipy.integrate import simpson
from scipy.interpolate import PchipInterpolator

Representation = Literal["coordinate", "momentum"]


@dataclass(frozen=True)
class RadialWaveFunction:
    """Reduced S- and D-wave radial functions on a strictly increasing grid.

    Coordinate-space functions use ``grid=r`` in fm and ``u,w`` in
    fm**(-1/2), with normalization ``integral dr (u**2+w**2)=1``.

    Momentum-space functions use ``grid=k`` in fm**(-1) and ``u,w`` in
    fm**(3/2), with normalization ``integral dk k**2 (u**2+w**2)=1``.
    """

    name: str
    representation: Representation
    grid: np.ndarray
    u: np.ndarray
    w: np.ndarray
    du: Optional[np.ndarray] = None
    dw: Optional[np.ndarray] = None
    source: str = ""

    def __post_init__(self) -> None:
        grid = np.asarray(self.grid, dtype=np.float64)
        u = np.asarray(self.u, dtype=np.float64)
        w = np.asarray(self.w, dtype=np.float64)
        if grid.ndim != 1 or len(grid) < 2:
            raise ValueError("grid must be one-dimensional with at least two points")
        if u.shape != grid.shape or w.shape != grid.shape:
            raise ValueError("u and w must have the same one-dimensional shape as grid")
        if not np.all(np.isfinite(grid)) or not np.all(np.isfinite(u)) or not np.all(np.isfinite(w)):
            raise ValueError("wave-function arrays must contain only finite values")
        if not np.all(np.diff(grid) > 0.0):
            raise ValueError("grid must be strictly increasing")
        if grid[0] < 0.0:
            raise ValueError("radial and momentum grids cannot contain negative values")
        for label, values in (("du", self.du), ("dw", self.dw)):
            if values is not None:
                array = np.asarray(values, dtype=np.float64)
                if array.shape != grid.shape or not np.all(np.isfinite(array)):
                    raise ValueError(f"{label} must be finite and have the grid shape")
                object.__setattr__(self, label, array)
        object.__setattr__(self, "grid", grid)
        object.__setattr__(self, "u", u)
        object.__setattr__(self, "w", w)

    @property
    def grid_units(self) -> str:
        return "fm" if self.representation == "coordinate" else "fm^-1"

    @property
    def function_units(self) -> str:
        return "fm^-1/2" if self.representation == "coordinate" else "fm^3/2"

    def component_norms(self) -> tuple[float, float]:
        measure = np.ones_like(self.grid)
        if self.representation == "momentum":
            measure = self.grid**2
        s_norm = float(simpson(measure * self.u**2, x=self.grid))
        d_norm = float(simpson(measure * self.w**2, x=self.grid))
        return s_norm, d_norm

    def norm(self) -> float:
        s_norm, d_norm = self.component_norms()
        return s_norm + d_norm

    def d_state_probability(self) -> float:
        return self.component_norms()[1]

    def interpolate(self, points: np.ndarray | float) -> tuple[np.ndarray, np.ndarray]:
        """Shape-preserving interpolation with forbidden extrapolation."""

        query = np.asarray(points, dtype=np.float64)
        if np.any(query < self.grid[0]) or np.any(query > self.grid[-1]):
            raise ValueError(
                f"requested {self.representation}-space point outside "
                f"[{self.grid[0]}, {self.grid[-1]}] {self.grid_units}"
            )
        u_interp = PchipInterpolator(self.grid, self.u, extrapolate=False)
        w_interp = PchipInterpolator(self.grid, self.w, extrapolate=False)
        return np.asarray(u_interp(query)), np.asarray(w_interp(query))

    def radial_callable(self) -> Callable[[float], tuple[float, float]]:
        """Return a scalar callable for a momentum-space radial input."""

        if self.representation != "momentum":
            raise ValueError("light-front mapping requires a momentum-space radial function")
        u_interp = PchipInterpolator(self.grid, self.u, extrapolate=False)
        w_interp = PchipInterpolator(self.grid, self.w, extrapolate=False)
        lower, upper = float(self.grid[0]), float(self.grid[-1])

        def evaluate(momentum: float) -> tuple[float, float]:
            if momentum < lower or momentum > upper:
                raise ValueError(
                    f"momentum {momentum} outside tabulated range [{lower}, {upper}] fm^-1"
                )
            return float(u_interp(momentum)), float(w_interp(momentum))

        return evaluate
