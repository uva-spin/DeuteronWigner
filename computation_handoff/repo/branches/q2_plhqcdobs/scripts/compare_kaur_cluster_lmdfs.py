#!/usr/bin/env python3
"""Reproduce and validate the effective-cluster LMDF figure.

The uncertainty envelope is the extrema of six one-at-a-time parameter
variations quoted in arXiv:2507.09886.  It is a sensitivity envelope, not a
confidence interval: the source publishes no fit covariance.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from deuteron_wigner.hidden_color_cluster_lfwf import (
    EffectiveClusterParameters,
    EffectiveClusterScalarLFWF,
    EffectiveClusterVectorCurrentLFWF,
)


OUTPUT_DIRECTORY = Path("outputs/figures/hidden_color_cluster")
BENCHMARK = Path("data/benchmarks/kaur_2026_cluster_lmdf.csv")


def wave(parameters: EffectiveClusterParameters) -> EffectiveClusterVectorCurrentLFWF:
    return EffectiveClusterVectorCurrentLFWF(
        scalar=EffectiveClusterScalarLFWF(parameters),
        normalization_nodes=64,
    )


def curves(model: EffectiveClusterVectorCurrentLFWF, z_grid: np.ndarray) -> np.ndarray:
    values = []
    for z in z_grid:
        projected = model.collinear_lmdfs(float(z), quadrature_nodes=64)
        values.append([z * projected[name] for name in ("f1", "g1L", "f1LL")])
    return np.asarray(values)


def main() -> None:
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    z_grid = np.linspace(0.01, 0.99, 99)
    central_parameters = EffectiveClusterParameters()
    variants = (
        EffectiveClusterParameters(cluster_mass_gev=0.755),
        EffectiveClusterParameters(cluster_mass_gev=0.921),
        EffectiveClusterParameters(transverse_kappa_gev=0.117),
        EffectiveClusterParameters(transverse_kappa_gev=0.143),
        EffectiveClusterParameters(longitudinal_g_gev=0.45),
        EffectiveClusterParameters(longitudinal_g_gev=0.55),
    )
    central_model = wave(central_parameters)
    central = curves(central_model, z_grid)
    varied = np.asarray([curves(wave(parameters), z_grid) for parameters in variants])
    lower = np.min(varied, axis=0)
    upper = np.max(varied, axis=0)

    benchmark = np.genfromtxt(BENCHMARK, delimiter=",", names=True)
    benchmark_names = ("z_f1", "z_g1L", "z_f1LL")
    curve_names = ("z_f1", "z_g1L", "z_f1LL")
    plot_labels = (r"$z f_1$", r"$z g_{1L}$", r"$z f_{1LL}$")
    colors = ("#7b1fa2", "#c49a00", "#555555")
    line_styles = ("-", "--", "-.")
    figure, axis = plt.subplots(figsize=(8.0, 5.1), constrained_layout=True)
    for index, (name, label, color, style) in enumerate(
        zip(curve_names, plot_labels, colors, line_styles)
    ):
        axis.fill_between(
            z_grid,
            lower[:, index],
            upper[:, index],
            color=color,
            alpha=0.16,
            linewidth=0,
        )
        axis.plot(z_grid, central[:, index], style, color=color, lw=2.1, label=label)
        axis.plot(
            benchmark["z"],
            benchmark[benchmark_names[index]],
            color="black",
            lw=0,
            marker=".",
            markersize=1.8,
            alpha=0.5,
            label="official PDF paths" if index == 0 else None,
        )
    axis.axhline(0.0, color="#888888", lw=0.7)
    axis.set(xlabel=r"$z$", ylabel=r"$z\,F(z)$", xlim=(0.0, 1.0))
    axis.legend(frameon=False, ncol=3)
    axis.text(
        0.015,
        0.02,
        "bands: quoted-parameter one-at-a-time sensitivity (not fit CL)",
        transform=axis.transAxes,
        fontsize=8,
    )
    figure.savefig(OUTPUT_DIRECTORY / "kaur_2026_cluster_lmdf_comparison.pdf")
    figure.savefig(
        OUTPUT_DIRECTORY / "kaur_2026_cluster_lmdf_comparison.png", dpi=220
    )
    plt.close(figure)

    with (OUTPUT_DIRECTORY / "kaur_2026_cluster_lmdf_model.csv").open(
        "w", newline=""
    ) as stream:
        writer = csv.writer(stream)
        header = ["z"]
        for name in curve_names:
            header.extend((f"{name}_central", f"{name}_low", f"{name}_high"))
        writer.writerow(header)
        for row, z in enumerate(z_grid):
            output_row: list[float] = [float(z)]
            for column in range(3):
                output_row.extend(
                    (central[row, column], lower[row, column], upper[row, column])
                )
            writer.writerow(output_row)

    residuals = {}
    for index, name in enumerate(curve_names):
        interpolation = np.interp(
            benchmark["z"], z_grid, central[:, index], left=np.nan, right=np.nan
        )
        comparison = (benchmark["z"] >= 0.05) & (benchmark["z"] <= 0.90)
        residuals[name] = float(
            np.nanmax(
                np.abs(interpolation[comparison] - benchmark[benchmark_names[index]][comparison])
            )
        )
    report = {
        "source": "arXiv:2507.09886 official source vector figure pdfs.pdf",
        "classification": "deep-binding effective-cluster sensitivity model; not a hidden-color probability",
        "uncertainty": "extrema of six one-at-a-time quoted parameter variations; no source covariance available",
        "central_mass_gev": central_model.scalar.total_mass_gev,
        "normalizations": central_model._normalizations,
        "comparison_domain": [0.05, 0.90],
        "maximum_absolute_path_residual": residuals,
        "benchmark_extractor": "scripts/extract_kaur_cluster_lmdf_benchmark.py",
    }
    (OUTPUT_DIRECTORY / "kaur_2026_cluster_lmdf.validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
