"""Strict readers for the authoritative Argonne v18 deuteron tables."""

from __future__ import annotations

from pathlib import Path
import re

import numpy as np
from scipy.integrate import quad

from .models import RadialWaveFunction

_FLOAT = re.compile(
    r"^[ ]*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[EeDd][+-]?\d+)?(?:[ ]+|$))+"
)


def _numeric_rows(path: Path, columns: int) -> np.ndarray:
    rows: list[list[float]] = []
    for line_number, line in enumerate(path.read_text(encoding="ascii").splitlines(), start=1):
        if not _FLOAT.match(line):
            continue
        fields = line.replace("D", "E").replace("d", "e").split()
        if len(fields) != columns:
            continue
        try:
            row = [float(field) for field in fields]
        except ValueError as exc:
            raise ValueError(f"{path}:{line_number}: malformed numeric row") from exc
        rows.append(row)
    if not rows:
        raise ValueError(f"{path}: no {columns}-column wave-function rows found")
    data = np.asarray(rows, dtype=np.float64)
    if not np.all(np.diff(data[:, 0]) > 0.0):
        raise ValueError(f"{path}: wave-function grid is not strictly increasing")
    return data


def load_av18_coordinate(path: str | Path) -> RadialWaveFunction:
    """Read ``deut.wf`` containing ``r,u,du/dr,w,dw/dr``."""

    source = Path(path)
    data = _numeric_rows(source, columns=5)
    if not (0.0 < data[0, 0] <= 0.01 and data[-1, 0] >= 15.0):
        raise ValueError(f"{source}: unexpected AV18 coordinate grid coverage")
    return RadialWaveFunction(
        name="AV18",
        representation="coordinate",
        grid=data[:, 0],
        u=data[:, 1],
        du=data[:, 2],
        w=data[:, 3],
        dw=data[:, 4],
        source=str(source),
    )


def load_av18_momentum(path: str | Path) -> RadialWaveFunction:
    """Read ``deut.wfk`` containing ``k,u(k),w(k)``."""

    source = Path(path)
    data = _numeric_rows(source, columns=3)
    if data[0, 0] != 0.0 or data[-1, 0] < 15.0:
        raise ValueError(f"{source}: unexpected AV18 momentum grid coverage")
    return RadialWaveFunction(
        name="AV18",
        representation="momentum",
        grid=data[:, 0],
        u=data[:, 1],
        w=data[:, 2],
        source=str(source),
    )


def av18_asymptotic_tail_norm(
    r_min: float,
    *,
    gamma: float = 0.2316,
    a_s: float = 0.885056,
    eta: float = 0.025045,
) -> tuple[float, float]:
    """Normalization beyond ``r_min`` using the table's asymptotic constants.

    The AV18 header supplies ``a_s`` and ``eta``. The decay constant 0.2316 fm^-1
    agrees with the logarithmic derivative at the end of the coordinate table.
    This function completes normalization diagnostics only; it does not append
    synthetic samples to the authoritative table.
    """

    if r_min <= 0.0:
        raise ValueError("r_min must be positive")

    def u_squared(radius: float) -> float:
        return (a_s * np.exp(-gamma * radius)) ** 2

    def w_squared(radius: float) -> float:
        gamma_r = gamma * radius
        w = a_s * eta * np.exp(-gamma_r) * (
            1.0 + 3.0 / gamma_r + 3.0 / gamma_r**2
        )
        return w**2

    return (
        quad(u_squared, r_min, np.inf, epsabs=1e-13)[0],
        quad(w_squared, r_min, np.inf, epsabs=1e-13)[0],
    )
