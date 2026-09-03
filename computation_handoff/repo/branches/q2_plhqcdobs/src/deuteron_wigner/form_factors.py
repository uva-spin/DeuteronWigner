"""Provenance-preserving readers for deuteron electromagnetic benchmarks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import numpy as np
from scipy.interpolate import PchipInterpolator


def _numeric_block(lines: list[str], header: str, columns: int) -> np.ndarray:
    try:
        start = next(index for index, line in enumerate(lines) if line.strip() == header)
    except StopIteration as exc:
        raise ValueError(f"missing table header: {header}") from exc
    rows = []
    for line in lines[start + 1 :]:
        fields = line.split()
        if len(fields) != columns:
            if rows:
                break
            continue
        try:
            rows.append(tuple(float(field) for field in fields))
        except ValueError:
            if rows:
                break
    if not rows:
        raise ValueError(f"empty numeric table after header: {header}")
    return np.asarray(rows, dtype=np.float64)


@dataclass(frozen=True)
class AV18ElectromagneticTables:
    deuteron_mass_mev: float
    reduced_mass_mev: float
    q_nucleon: np.ndarray
    ges: np.ndarray
    gms: np.ndarray
    q_body: np.ndarray
    ce: np.ndarray
    cl: np.ndarray
    cs: np.ndarray
    cq: np.ndarray
    q_deuteron: np.ndarray
    gc: np.ndarray
    gm: np.ndarray
    gq: np.ndarray
    q_observable: np.ndarray
    structure_a: np.ndarray
    structure_b: np.ndarray
    t20_70deg: np.ndarray

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if name in ("deuteron_mass_mev", "reduced_mass_mev"):
                continue
            array = np.asarray(value, dtype=np.float64)
            if array.ndim != 1:
                raise ValueError(f"{name} must be one-dimensional")
            object.__setattr__(self, name, array)
        if not (
            len(self.q_nucleon) == len(self.ges) == len(self.gms)
            and len(self.q_body) == len(self.ce) == len(self.cl) == len(self.cs) == len(self.cq)
            and len(self.q_deuteron) == len(self.gc) == len(self.gm) == len(self.gq)
            and len(self.q_observable)
            == len(self.structure_a)
            == len(self.structure_b)
            == len(self.t20_70deg)
        ):
            raise ValueError("form-factor table lengths are inconsistent")

    @staticmethod
    def _interpolate(q: np.ndarray, values: np.ndarray, points: np.ndarray | float):
        requested = np.asarray(points, dtype=np.float64)
        if np.any(requested < q[0]) or np.any(requested > q[-1]):
            raise ValueError(f"requested q outside tabulated range [{q[0]}, {q[-1]}] fm^-1")
        result = PchipInterpolator(q, values, extrapolate=False)(requested)
        return float(result) if requested.ndim == 0 else result

    def isoscalar_electric(self, q_fm: np.ndarray | float):
        """Kelly \(G_E^s=(G_E^p+G_E^n)/2\) as tabulated by Wiringa."""

        return self._interpolate(self.q_nucleon, self.ges, q_fm)

    def isoscalar_magnetic(self, q_fm: np.ndarray | float):
        """Kelly \(G_M^s=(G_M^p+G_M^n)/2\) as tabulated by Wiringa."""

        return self._interpolate(self.q_nucleon, self.gms, q_fm)

    def body_charge(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_body, self.ce, q_fm)

    def charge_form_factor(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_deuteron, self.gc, q_fm)

    def magnetic_form_factor(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_deuteron, self.gm, q_fm)

    def quadrupole_form_factor(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_deuteron, self.gq, q_fm)

    def observable_a(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_observable, self.structure_a, q_fm)

    def observable_b(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_observable, self.structure_b, q_fm)

    def observable_t20(self, q_fm: np.ndarray | float):
        return self._interpolate(self.q_observable, self.t20_70deg, q_fm)


def load_av18_electromagnetic_tables(path: str | Path) -> AV18ElectromagneticTables:
    lines = Path(path).read_text().splitlines()
    mass_line = next((line for line in lines if "mdeut =" in line and "mr =" in line), None)
    if mass_line is None:
        raise ValueError("missing mdeut/mr line")
    masses = re.search(
        r"mdeut\s*=\s*([0-9.Ee+-]+)\s+mr\s*=\s*([0-9.Ee+-]+)", mass_line
    )
    if masses is None:
        raise ValueError("could not parse mdeut/mr values")
    nucleon = _numeric_block(lines, "k          ges                 gms", 3)
    body = _numeric_block(lines, "q       ce             cl             cs             cq", 5)
    deuteron = _numeric_block(lines, "q       gc                 gm                 gq", 4)
    observable = _numeric_block(lines, "q       A              B              t20", 4)
    return AV18ElectromagneticTables(
        deuteron_mass_mev=float(masses.group(1)),
        reduced_mass_mev=float(masses.group(2)),
        q_nucleon=nucleon[:, 0],
        ges=nucleon[:, 1],
        gms=nucleon[:, 2],
        q_body=body[:, 0],
        ce=body[:, 1],
        cl=body[:, 2],
        cs=body[:, 3],
        cq=body[:, 4],
        q_deuteron=deuteron[:, 0],
        gc=deuteron[:, 1],
        gm=deuteron[:, 2],
        gq=deuteron[:, 3],
        q_observable=observable[:, 0],
        structure_a=observable[:, 1],
        structure_b=observable[:, 2],
        t20_70deg=observable[:, 3],
    )


def charge_impulse_from_body(*, body_overlap: np.ndarray | float, ges: np.ndarray | float):
    """Wiringa's impulse relation \(G_C=2G_E^s C_E\)."""

    return 2.0 * np.asarray(ges) * np.asarray(body_overlap)


def deuteron_impulse_form_factors(
    *,
    ges,
    gms,
    ce,
    cl,
    cs,
    cq,
    deuteron_mass_mev: float,
    reduced_mass_mev: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Wiringa's nonrelativistic one-body \(G_C,G_M,G_Q\) combinations."""

    gc = 2.0 * np.asarray(ges) * np.asarray(ce)
    gm = (deuteron_mass_mev / reduced_mass_mev) * (
        np.asarray(ges) * np.asarray(cl) + 2.0 * np.asarray(gms) * np.asarray(cs)
    )
    gq = 2.0 * np.asarray(ges) * np.asarray(cq)
    return gc, gm, gq


def elastic_observables(
    *,
    q_fm,
    gc,
    gm,
    gq,
    deuteron_mass_mev: float,
    angle_degrees: float = 70.0,
    hbarc_mev_fm: float = 197.3269804,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute \(A,B,t_{20}\) using the convention of the AV18 table."""

    q = np.asarray(q_fm)
    gc = np.asarray(gc)
    gm = np.asarray(gm)
    gq = np.asarray(gq)
    tau = q**2 / (2.0 * deuteron_mass_mev / hbarc_mev_fm) ** 2
    structure_a = gc**2 + (8.0 / 9.0) * (tau * gq) ** 2 + (2.0 / 3.0) * tau * gm**2
    structure_b = (4.0 / 3.0) * tau * (1.0 + tau) * gm**2
    x = (2.0 / 3.0) * tau * gq / gc
    angle = np.deg2rad(angle_degrees)
    y = (
        (1.0 / 3.0)
        * tau
        * (gm / gc) ** 2
        * (1.0 + 2.0 * (1.0 + tau) * np.tan(angle / 2.0) ** 2)
    )
    t20 = -np.sqrt(2.0) * (x * (x + 2.0) + 0.5 * y) / (
        1.0 + 2.0 * (x**2 + y)
    )
    return structure_a, structure_b, t20
