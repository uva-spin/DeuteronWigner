#!/usr/bin/env python3
"""Audit LF-parent azimuth covariance at production and doubled phi order."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nucleon_quark_correlator import SpinHalfQuarkCorrelator
from deuteron_wigner.parent_quark_tmd import (
    ParentDerivedQuarkResult,
    convolve_spin1_quark_wave_components,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


class CovariantSyntheticNucleon:
    """Fast complete operator fixture with nontrivial radial momentum shape."""

    def correlator(
        self, *, k_x_gev: float, k_y_gev: float, **_: object
    ) -> SpinHalfQuarkCorrelator:
        kx, ky = float(k_x_gev), float(k_y_gev)
        profile = np.exp(-(kx**2 + ky**2) / 0.31) / (np.pi * 0.31)
        identity = np.eye(2, dtype=complex)
        sx = np.asarray(((0.0, 1.0), (1.0, 0.0)), complex)
        sy = np.asarray(((0.0, 1j), (-1j, 0.0)), complex)
        sz = np.asarray(((1.0, 0.0), (0.0, -1.0)), complex)
        vector = profile * identity + 0.04 * profile * (
            ky * sx - kx * sy
        ) / M_N_GEV
        axial = 0.18 * profile * sz + 0.06 * profile * (
            kx * sx + ky * sy
        ) / M_N_GEV
        transverse = np.empty((2, 2, 2), complex)
        for index, sigma in enumerate((sx, sy)):
            transverse[index] = 0.12 * profile * sigma
            transverse[index] += (
                -0.05 * profile * (kx, ky)[index] * sz / M_N_GEV
            )
        return SpinHalfQuarkCorrelator(vector, axial, transverse)


def sum_components(
    components: dict[str, ParentDerivedQuarkResult]
) -> ParentDerivedQuarkResult:
    def summed(nucleon: str) -> Spin1QuarkCorrelator:
        values = [getattr(item, nucleon) for item in components.values()]
        return Spin1QuarkCorrelator(
            sum(item.vector for item in values),
            sum(item.axial for item in values),
            sum(item.transverse for item in values),
        )
    return ParentDerivedQuarkResult(summed("proton"), summed("neutron"))


def evaluate(n_phi: int) -> dict[tuple[float, float, str], float]:
    wave = select_momentum_wave_function("av18")
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=10.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=24,
        n_cos_theta=16,
        n_phi=n_phi,
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    model = CovariantSyntheticNucleon()
    output = {}
    for k in (0.3, 0.7, 1.1):
        for angle in (0.37, 0.91):
            kx, ky = k * np.cos(angle), k * np.sin(angle)
            components = convolve_spin1_quark_wave_components(
                x=0.05,
                k_x=kx / HBARC_GEV_FM,
                k_y=ky / HBARC_GEV_FM,
                scale=5.0,
                flavor=2,
                proton=model,
                neutron=model,
                gauge_link=GaugeLink("+", "+"),
                quadratures=quadratures,
                momentum_unit_to_gev=HBARC_GEV_FM,
            )
            projected = project_parent_derived_quark_tmds(
                sum_components(components),
                k_x_gev=kx,
                k_y_gev=ky,
                deuteron_mass_gev=M_D_GEV,
            )["total"]
            for name, value in projected.items():
                output[(k, angle, name)] = value
    return output


def metric(values: dict[tuple[float, float, str], float]) -> dict[str, float]:
    absolute = []
    normalized = []
    for k in (0.3, 0.7, 1.1):
        for name in {key[2] for key in values}:
            left = values[(k, 0.37, name)]
            right = values[(k, 0.91, name)]
            difference = abs(left - right)
            size = max(abs(left), abs(right))
            absolute.append(difference)
            if size > 1.0e-8:
                normalized.append(difference / size)
    return {
        "maximum_absolute_GeV-2": max(absolute),
        "maximum_relative_resolved": max(normalized),
    }


def main() -> None:
    production = metric(evaluate(12))
    doubled = metric(evaluate(24))
    report = {
        "status": "pass",
        "wave_function": "AV18",
        "internal_orders": {
            "production": [24, 16, 12],
            "doubled_azimuth": [24, 16, 24],
        },
        "external_points": {
            "k_GeV": [0.3, 0.7, 1.1],
            "azimuth_rad": [0.37, 0.91],
        },
        "fixture": (
            "complete covariant synthetic spin-half correlator with radial "
            "momentum dependence, convolved through physical AV18 LF kernel"
        ),
        "production": production,
        "doubled_azimuth": doubled,
        "acceptance": {
            "production_relative_max": 0.01,
            "doubled_relative_max": 0.0025,
        },
    }
    if production["maximum_relative_resolved"] > 0.01:
        raise AssertionError(report)
    if doubled["maximum_relative_resolved"] > 0.0025:
        raise AssertionError(report)
    output = Path(
        "outputs/parent_tmds/quark_parent_azimuth_covariance.validation.json"
    )
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
