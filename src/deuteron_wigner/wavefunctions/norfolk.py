"""Strict readers for Argonne's Norfolk chiral deuteron tables."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np

from .models import RadialWaveFunction


@dataclass(frozen=True)
class NorfolkModel:
    label: str
    fit_class: int
    r_short_fm: float
    r_long_fm: float


NORFOLK_MODELS = {
    "nvia": NorfolkModel("NV2-Ia", 1, 0.8, 1.2),
    "nvib": NorfolkModel("NV2-Ib", 1, 0.7, 1.0),
    "nviia": NorfolkModel("NV2-IIa", 2, 0.8, 1.2),
    "nviib": NorfolkModel("NV2-IIb", 2, 0.7, 1.0),
}


def _model_from_path(path: Path) -> NorfolkModel:
    suffix = path.name.rsplit(".", 1)[-1].lower()
    if suffix not in NORFOLK_MODELS:
        raise ValueError(f"{path}: expected Norfolk suffix {tuple(NORFOLK_MODELS)}")
    return NORFOLK_MODELS[suffix]


def _section(path: Path, header: str, columns: int) -> np.ndarray:
    lines = path.read_text(encoding="ascii").splitlines()
    matches = [index for index, line in enumerate(lines) if line.strip() == header]
    if len(matches) != 1:
        raise ValueError(f"{path}: expected one section header {header!r}")
    rows = []
    for line_number, line in enumerate(lines[matches[0] + 1 :], start=matches[0] + 2):
        fields = line.replace("D", "E").replace("d", "e").split()
        if len(fields) != columns:
            if rows:
                break
            continue
        try:
            rows.append([float(field) for field in fields])
        except ValueError:
            if rows:
                break
            continue
    if not rows:
        raise ValueError(f"{path}: no data after section {header!r}")
    values = np.asarray(rows, dtype=np.float64)
    if not np.all(np.diff(values[:, 0]) > 0.0):
        raise ValueError(f"{path}: non-increasing grid in section {header!r}")
    return values


def load_norfolk_momentum(path: str | Path) -> RadialWaveFunction:
    source = Path(path)
    model = _model_from_path(source)
    values = _section(source, "k          u(k)                w(k)", 3)
    if values[0, 0] != 0.0 or values[-1, 0] < 20.0:
        raise ValueError(f"{source}: unexpected Norfolk momentum coverage")
    return RadialWaveFunction(
        name=model.label,
        representation="momentum",
        grid=values[:, 0],
        u=values[:, 1],
        w=values[:, 2],
        source=str(source),
    )


def load_norfolk_coordinate(path: str | Path) -> RadialWaveFunction:
    source = Path(path)
    model = _model_from_path(source)
    values = _section(
        source,
        "r          u              du/dr          w              dw/dr",
        5,
    )
    if values[0, 0] > 0.01 or values[-1, 0] < 99.0:
        raise ValueError(f"{source}: unexpected Norfolk coordinate coverage")
    return RadialWaveFunction(
        name=model.label,
        representation="coordinate",
        grid=values[:, 0],
        u=values[:, 1],
        du=values[:, 2],
        w=values[:, 3],
        dw=values[:, 4],
        source=str(source),
    )


def norfolk_radial_callable(
    wave: RadialWaveFunction,
) -> Callable[[float], tuple[float, float]]:
    """Return a continuously normalized shape-preserving Norfolk interpolant.

    The source table is normalized under its discrete trapezoidal convention.
    Off-grid convolution requires a continuous interpolant, so a single common
    factor normalizes the PCHIP amplitudes without changing their S/D ratio.
    """

    if wave.representation != "momentum" or not wave.name.startswith("NV2-"):
        raise ValueError("require a Norfolk momentum-space wave function")
    base = wave.radial_callable()
    lower, upper = float(wave.grid[0]), float(wave.grid[-1])
    nodes, weights = np.polynomial.legendre.leggauss(240)
    momenta = 0.5 * upper * (nodes + 1.0)
    weights = 0.5 * upper * weights
    continuous_norm = sum(
        weight * momentum**2 * sum(value**2 for value in base(float(momentum)))
        for momentum, weight in zip(momenta, weights)
    )
    normalization = 1.0 / np.sqrt(continuous_norm)

    def evaluate(momentum: float) -> tuple[float, float]:
        if momentum < lower or momentum > upper:
            raise ValueError(
                f"momentum {momentum} outside tabulated range [{lower}, {upper}] fm^-1"
            )
        u, w = base(momentum)
        return normalization * u, normalization * w

    return evaluate
