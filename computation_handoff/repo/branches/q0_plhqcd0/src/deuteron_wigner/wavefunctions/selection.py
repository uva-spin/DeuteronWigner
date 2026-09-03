"""Shared selection of production momentum-space deuteron wave functions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .av18 import load_av18_momentum
from .cd_bonn import cd_bonn_parameters
from .norfolk import load_norfolk_momentum, norfolk_radial_callable

WAVE_FUNCTION_CHOICES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")


@dataclass(frozen=True)
class MomentumWaveSelection:
    label: str
    radial: Callable[[float], tuple[float, float]]
    maximum_momentum_fm: float | None

    def validate_k_max(self, k_max: float) -> None:
        if k_max <= 0.0:
            raise ValueError("k-max must be positive")
        if self.maximum_momentum_fm is not None and k_max > self.maximum_momentum_fm:
            raise ValueError(
                f"{self.label} k-max cannot exceed "
                f"{self.maximum_momentum_fm} fm^-1"
            )


def select_momentum_wave_function(label: str) -> MomentumWaveSelection:
    """Load a named production radial function with its domain metadata."""

    key = label.lower()
    if key == "av18":
        table = load_av18_momentum("data/raw/av18/deut.wfk")
        return MomentumWaveSelection(
            key, table.radial_callable(), float(table.grid[-1])
        )
    if key == "cd-bonn":
        parameters = cd_bonn_parameters()

        def radial(momentum: float) -> tuple[float, float]:
            return tuple(float(value) for value in parameters.momentum(momentum))

        return MomentumWaveSelection(key, radial, None)
    if key in WAVE_FUNCTION_CHOICES[2:]:
        table = load_norfolk_momentum(f"data/raw/norfolk/fdeut.{key}")
        return MomentumWaveSelection(
            key, norfolk_radial_callable(table), float(table.grid[-1])
        )
    raise ValueError(
        f"unknown wave function {label!r}; expected one of {WAVE_FUNCTION_CHOICES}"
    )
