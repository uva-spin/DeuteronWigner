"""Declared boundary models for rank-zero nucleon TMD fixtures."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.interpolate import RegularGridInterpolator

CollinearPDF = Callable[[int, float, float], float]
GluonPDF = Callable[[float, float], float]


@dataclass(frozen=True)
class GaussianRankZeroTMD:
    """Normalized Gaussian transverse profile.

    ``width`` is ``<k_T^2>`` in the square of the transverse-momentum unit.
    With the project's Fourier convention,

    F(k) = f(x) exp(-k^2/width) / (pi width),
    F_tilde(b) = f(x) exp(-width b^2/4).
    """

    pdf: CollinearPDF
    width: float

    def __post_init__(self) -> None:
        if self.width <= 0.0:
            raise ValueError("Gaussian width must be positive")

    def b_space(self, flavor: int, x: float, b: float, scale: float) -> complex:
        return complex(
            self.pdf(flavor, x, scale) * np.exp(-0.25 * self.width * b**2)
        )

    def k_space(self, flavor: int, x: float, k: float, scale: float) -> float:
        return float(
            self.pdf(flavor, x, scale)
            * np.exp(-(k**2) / self.width)
            / (np.pi * self.width)
        )


@dataclass(frozen=True)
class GaussianSpinHalfGluonGTMD:
    """Declared spin-1/2 nucleon gluon-TMD boundary model.

    ``unpolarized_pdf`` and the optional ``helicity_pdf`` return collinear
    number densities.  The Gaussian width and all momenta use one consistent
    unit.  ``linear_fraction`` controls a bounded linearly polarized gluon
    component and is not inferred from the collinear PDF.
    """

    unpolarized_pdf: GluonPDF
    width: float
    nucleon_mass: float
    helicity_pdf: GluonPDF | None = None
    linear_fraction: float = 0.0
    transfer_slope: float = 0.0

    def __post_init__(self) -> None:
        if self.width <= 0.0:
            raise ValueError("Gaussian width must be positive")
        if self.nucleon_mass <= 0.0:
            raise ValueError("nucleon mass must be positive")
        if abs(self.linear_fraction) > 1.0:
            raise ValueError("linear gluon fraction must lie in [-1,1]")
        if self.transfer_slope < 0.0:
            raise ValueError("transfer slope cannot be negative")

    def tmd_values(
        self, x: float, k_x: float, k_y: float, scale: float
    ) -> dict[str, float]:
        k_squared = float(k_x**2 + k_y**2)
        profile = np.exp(-k_squared / self.width) / (np.pi * self.width)
        f1 = float(self.unpolarized_pdf(x, scale) * profile)
        g1 = (
            0.0
            if self.helicity_pdf is None
            else float(self.helicity_pdf(x, scale) * profile)
        )
        # This maps to a linear-polarization matrix whose magnitude relative
        # to the trace is |rho| k_T^2/(width+k_T^2), hence is bounded by
        # |rho| and regular at k_T=0.
        h1perp = (
            2.0
            * self.linear_fraction
            * self.nucleon_mass**2
            * f1
            / (self.width + k_squared)
        )
        return {"f1": f1, "g1": g1, "h1perp": h1perp}

    def __call__(
        self,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        from .gluon_correlator import (
            compose_longitudinal_gluon_correlator,
            compose_unpolarized_gluon_correlator,
        )

        values = self.tmd_values(x, k_x, k_y, scale)
        transfer = np.exp(
            -self.transfer_slope * (delta_x**2 + delta_y**2)
        )
        unpolarized = compose_unpolarized_gluon_correlator(
            (k_x, k_y),
            self.nucleon_mass,
            f1=values["f1"],
            h1perp=values["h1perp"],
        )
        longitudinal = compose_longitudinal_gluon_correlator(
            (k_x, k_y),
            self.nucleon_mass,
            1.0,
            g1=values["g1"],
            h1Lperp=0.0,
        )
        identity = np.eye(2, dtype=np.complex128)
        sigma_z = np.diag((1.0, -1.0)).astype(np.complex128)
        return transfer * (
            np.einsum("ac,ij->acij", identity, unpolarized)
            + np.einsum("ac,ij->acij", sigma_z, longitudinal)
        )


@dataclass(frozen=True)
class InterpolatedSpinHalfGluonGTMD:
    """Strict radial interpolation of a tabulated nucleon gluon TMD.

    The tables are functions of ``(x,k_T)`` in GeV units. The callable
    interface accepts the momentum unit used by the nuclear convolution and
    converts it with ``momentum_unit_to_GeV``. No extrapolation is allowed.
    """

    x_axis: np.ndarray
    k_axis_GeV: np.ndarray
    f1: np.ndarray
    g1: np.ndarray
    h1perp: np.ndarray
    nucleon_mass_GeV: float
    momentum_unit_to_GeV: float = 1.0
    transfer_slope_per_input_unit2: float = 0.0

    def __post_init__(self) -> None:
        x = np.asarray(self.x_axis, dtype=np.float64)
        k = np.asarray(self.k_axis_GeV, dtype=np.float64)
        if (
            x.ndim != 1
            or k.ndim != 1
            or len(x) < 2
            or len(k) < 2
            or not np.all(np.diff(x) > 0.0)
            or not np.all(np.diff(k) > 0.0)
        ):
            raise ValueError("x and k axes must be strictly increasing")
        if x[0] <= 0.0 or x[-1] > 1.0 or k[0] != 0.0:
            raise ValueError("tables require 0<x<=1 and a k axis starting at zero")
        expected = (len(x), len(k))
        for name in ("f1", "g1", "h1perp"):
            values = np.asarray(getattr(self, name), dtype=np.float64)
            if values.shape != expected or not np.all(np.isfinite(values)):
                raise ValueError(f"{name} must be a finite (nx,nk) table")
            object.__setattr__(self, name, values)
        if self.nucleon_mass_GeV <= 0.0 or self.momentum_unit_to_GeV <= 0.0:
            raise ValueError("mass and momentum-unit conversion must be positive")
        if self.transfer_slope_per_input_unit2 < 0.0:
            raise ValueError("transfer slope cannot be negative")
        object.__setattr__(self, "x_axis", x)
        object.__setattr__(self, "k_axis_GeV", k)
        for name in ("f1", "g1", "h1perp"):
            object.__setattr__(
                self,
                f"_{name}_interpolator",
                RegularGridInterpolator(
                    (x, k),
                    getattr(self, name),
                    method="linear",
                    bounds_error=True,
                ),
            )

    def tmd_values(
        self, x: float, k_x: float, k_y: float, scale: float
    ) -> dict[str, float]:
        del scale  # The table scale is fixed and recorded by its producer.
        k_GeV = self.momentum_unit_to_GeV * float(np.hypot(k_x, k_y))
        point = np.asarray((x, k_GeV), dtype=np.float64)
        return {
            name: float(
                np.asarray(
                    getattr(self, f"_{name}_interpolator")(point)
                ).item()
            )
            for name in ("f1", "g1", "h1perp")
        }

    def __call__(
        self,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        from .gluon_correlator import (
            compose_longitudinal_gluon_correlator,
            compose_unpolarized_gluon_correlator,
        )

        values = self.tmd_values(x, k_x, k_y, scale)
        k_gev = self.momentum_unit_to_GeV * np.asarray((k_x, k_y))
        unpolarized = compose_unpolarized_gluon_correlator(
            k_gev,
            self.nucleon_mass_GeV,
            f1=values["f1"],
            h1perp=values["h1perp"],
        )
        longitudinal = compose_longitudinal_gluon_correlator(
            k_gev,
            self.nucleon_mass_GeV,
            1.0,
            g1=values["g1"],
            h1Lperp=0.0,
        )
        identity = np.eye(2, dtype=np.complex128)
        sigma_z = np.diag((1.0, -1.0)).astype(np.complex128)
        transfer = np.exp(
            -self.transfer_slope_per_input_unit2
            * (delta_x**2 + delta_y**2)
        )
        return transfer * (
            np.einsum("ac,ij->acij", identity, unpolarized)
            + np.einsum("ac,ij->acij", sigma_z, longitudinal)
        )
