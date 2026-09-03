#!/usr/bin/env python3
"""Flavor-resolved effective-cluster b1 comparison with HERMES."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from deuteron_wigner.data import load_hermes_b1
from deuteron_wigner.hidden_color_cluster_lfwf import (
    EffectiveClusterCollinearConvolution,
    EffectiveClusterLMDFGrid,
    EffectiveClusterParameters,
    EffectiveClusterScalarLFWF,
    EffectiveClusterVectorCurrentLFWF,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider


OUTPUT = Path("outputs/figures/hidden_color_cluster")
HERMES = Path("data/processed/hermes_b1/table_ii.csv")
Q_GEV = np.sqrt(5.0)


def convolution(
    parameters: EffectiveClusterParameters,
    unpolarized: LHAPDFProvider,
    polarized: PolarizedLHAPDFProvider,
) -> EffectiveClusterCollinearConvolution:
    wave = EffectiveClusterVectorCurrentLFWF(
        scalar=EffectiveClusterScalarLFWF(parameters),
        normalization_nodes=48,
    )
    grid = EffectiveClusterLMDFGrid(wave=wave, z_nodes=121, transverse_nodes=48)
    return EffectiveClusterCollinearConvolution(
        unpolarized=unpolarized,
        polarized=polarized,
        lmdfs=grid,
        convolution_nodes=56,
    )


def b1_values(model: EffectiveClusterCollinearConvolution, x: np.ndarray) -> np.ndarray:
    return np.asarray(
        [
            model.structure_function("f1LL", float(value), Q_GEV) / value
            for value in x
        ]
    )


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    unpolarized = LHAPDFProvider("NNPDF31_nnlo_as_0118_1000", 0)
    polarized = PolarizedLHAPDFProvider(
        "BDSSV24-NLO", 0, data_root="data/raw/lhapdf"
    )
    central_parameters = EffectiveClusterParameters()
    variations = (
        EffectiveClusterParameters(cluster_mass_gev=0.755),
        EffectiveClusterParameters(cluster_mass_gev=0.921),
        EffectiveClusterParameters(transverse_kappa_gev=0.117),
        EffectiveClusterParameters(transverse_kappa_gev=0.143),
        EffectiveClusterParameters(longitudinal_g_gev=0.45),
        EffectiveClusterParameters(longitudinal_g_gev=0.55),
    )
    x_grid = np.geomspace(0.005, 0.85, 100)
    central_model = convolution(central_parameters, unpolarized, polarized)
    central = b1_values(central_model, x_grid)
    variant_models = [
        convolution(parameters, unpolarized, polarized) for parameters in variations
    ]
    varied = np.asarray(
        [b1_values(model, x_grid) for model in variant_models]
    )
    low, high = np.min(varied, axis=0), np.max(varied, axis=0)

    hermes = load_hermes_b1(HERMES)
    at_data = b1_values(central_model, hermes.x)
    experimental_sigma = hermes.b1_total_uncertainty
    chi2 = float(np.sum(((at_data - hermes.b1) / experimental_sigma) ** 2))

    moment_nodes, moment_weights = np.polynomial.legendre.leggauss(80)
    moment_x = 0.02 + (0.85 - 0.02) * (moment_nodes + 1.0) / 2.0
    moment_weights *= (0.85 - 0.02) / 2.0
    central_moment = float(np.dot(moment_weights, b1_values(central_model, moment_x)))
    variant_moments = [
        float(np.dot(moment_weights, b1_values(model, moment_x)))
        for model in variant_models
    ]

    with (OUTPUT / "kaur_2026_cluster_b1_vs_hermes.csv").open(
        "w", newline=""
    ) as stream:
        writer = csv.writer(stream)
        writer.writerow(("x", "b1_central", "b1_low", "b1_high"))
        writer.writerows(zip(x_grid, central, low, high))

    figure, axes = plt.subplots(1, 2, figsize=(10.2, 4.4), constrained_layout=True)
    for axis, multiply_x, ylabel in (
        (axes[0], False, r"$b_1(x)$"),
        (axes[1], True, r"$x\,b_1(x)$"),
    ):
        factor = x_grid if multiply_x else np.ones_like(x_grid)
        axis.fill_between(
            x_grid, factor * low, factor * high, color="#7b1fa2", alpha=0.22
        )
        axis.plot(
            x_grid,
            factor * central,
            color="#7b1fa2",
            lw=2.0,
            label="effective-cluster central",
        )
        data_factor = hermes.x if multiply_x else np.ones_like(hermes.x)
        axis.errorbar(
            hermes.x,
            data_factor * hermes.b1,
            yerr=data_factor * experimental_sigma,
            fmt="o",
            color="#6b4520",
            mfc="white",
            capsize=2,
            label="HERMES",
        )
        axis.axhline(0.0, color="#888888", lw=0.7)
        axis.set_xscale("log")
        axis.set(xlabel=r"$x$", ylabel=ylabel, xlim=(0.005, 0.9))
    axes[0].legend(frameon=False, fontsize=8)
    axes[1].text(
        0.02,
        0.03,
        r"$Q^2=5\ \mathrm{GeV}^2$; band is parameter sensitivity, not fit CL",
        transform=axes[1].transAxes,
        fontsize=7.5,
    )
    figure.savefig(OUTPUT / "kaur_2026_cluster_b1_vs_hermes.pdf")
    figure.savefig(OUTPUT / "kaur_2026_cluster_b1_vs_hermes.png", dpi=220)
    plt.close(figure)

    report = {
        "classification": "effective deep-binding cluster sensitivity; not hidden-color probability",
        "cluster_pdf": "NNPDF31_nnlo_as_0118_1000 member 0 with explicit proton/neutron isospin average",
        "scale_gev2": 5.0,
        "hard_prefactor": "b1 = 1/2 sum_q e_q^2 delta_T q",
        "moment_x_range": [0.02, 0.85],
        "central_b1_moment": central_moment,
        "sensitivity_moment_min": min(variant_moments),
        "sensitivity_moment_max": max(variant_moments),
        "source_quoted_moment": 0.0036,
        "source_quoted_uncertainty": 0.0003,
        "hermes_chi2_six_bins": chi2,
        "uncertainty_limitations": "one-at-a-time cluster parameter envelope only; no source covariance or NNPDF uncertainty propagated",
    }
    (OUTPUT / "kaur_2026_cluster_b1_vs_hermes.validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
