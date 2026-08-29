"""Nucleon PDF provider interfaces, including the existing LHAPDF installation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class LHAPDFProvider:
    """Return number densities f_i(x,Q), converting LHAPDF's x*f_i."""

    set_name: str = "CT18NNLO"
    member: int = 0
    data_root: str | Path | None = "data/raw/lhapdf"

    def __post_init__(self) -> None:
        try:
            import lhapdf
        except ImportError as exc:
            raise RuntimeError(
                "LHAPDF Python bindings are unavailable; run in the configured conda base"
            ) from exc
        if self.data_root is not None:
            root = str(Path(self.data_root).resolve())
            paths = list(lhapdf.paths())
            if root not in paths:
                lhapdf.setPaths([root, *paths])
        self._pdf: Any = lhapdf.mkPDF(self.set_name, self.member)

    def proton(self, flavor: int, x: float, scale: float) -> float:
        if not 0.0 < x <= 1.0:
            raise ValueError("x must lie in (0,1]")
        if scale <= 0.0:
            raise ValueError("scale must be positive")
        return float(self._pdf.xfxQ(flavor, x, scale) / x)

    def neutron(self, flavor: int, x: float, scale: float) -> float:
        """Isospin rotation u<->d and ubar<->dbar; other flavors unchanged."""

        mapping = {2: 1, 1: 2, -2: -1, -1: -2}
        return self.proton(mapping.get(flavor, flavor), x, scale)

    def gluon(self, x: float, scale: float) -> float:
        """Return the unpolarized gluon number density."""

        return self.proton(21, x, scale)

    def quark_singlet(
        self, x: float, scale: float, flavors: tuple[int, ...] = (1, 2, 3)
    ) -> float:
        """Return sum_q [q+qbar] for the requested active flavors."""

        if not flavors or any(flavor <= 0 or flavor > 6 for flavor in flavors):
            raise ValueError("flavors must contain positive LHAPDF quark IDs")
        return float(
            sum(
                self.proton(flavor, x, scale)
                + self.proton(-flavor, x, scale)
                for flavor in flavors
            )
        )

    def alpha_s(self, scale: float) -> float:
        """Return the PDF-set running coupling at Q=scale."""

        if scale <= 0.0:
            raise ValueError("scale must be positive")
        return float(self._pdf.alphasQ(scale))

    @property
    def q_min(self) -> float:
        return float(self._pdf.q2Min) ** 0.5

    @property
    def q_max(self) -> float:
        return float(self._pdf.q2Max) ** 0.5


@dataclass
class PolarizedLHAPDFProvider:
    """Polarized proton PDF provider with an optional project-local data root."""

    set_name: str = "BDSSV24-NLO"
    member: int = 0
    data_root: str | Path | None = "data/raw/lhapdf"

    def __post_init__(self) -> None:
        try:
            import lhapdf
        except ImportError as exc:
            raise RuntimeError(
                "LHAPDF Python bindings are unavailable; run in the configured conda base"
            ) from exc
        if self.data_root is not None:
            root = str(Path(self.data_root).resolve())
            paths = list(lhapdf.paths())
            if root not in paths:
                lhapdf.setPaths([root, *paths])
        self._pdf: Any = lhapdf.mkPDF(self.set_name, self.member)

    def proton(self, flavor: int, x: float, scale: float) -> float:
        """Return the helicity number density Delta f_i(x,Q)."""

        if not 0.0 < x <= 1.0:
            raise ValueError("x must lie in (0,1]")
        if scale <= 0.0:
            raise ValueError("scale must be positive")
        return float(self._pdf.xfxQ(flavor, x, scale) / x)

    def gluon(self, x: float, scale: float) -> float:
        return self.proton(21, x, scale)

    def neutron(self, flavor: int, x: float, scale: float) -> float:
        """Isospin rotation of polarized u/d and antiquark densities."""

        mapping = {2: 1, 1: 2, -2: -1, -1: -2}
        return self.proton(mapping.get(flavor, flavor), x, scale)

    @property
    def q_min(self) -> float:
        return float(self._pdf.q2Min) ** 0.5

    @property
    def q_max(self) -> float:
        return float(self._pdf.q2Max) ** 0.5
