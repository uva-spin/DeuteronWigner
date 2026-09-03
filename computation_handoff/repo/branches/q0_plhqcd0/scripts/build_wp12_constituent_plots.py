#!/usr/bin/env python3
"""Plot the proton/neutron dynamics hidden by the final spin-1 projection."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from scipy.ndimage import median_filter
from scipy.signal import savgol_filter

from build_wp12_inspection_plots import QLABELS


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs/parent_tmds/wp12_resolved_quark_parent.csv"
BANDS = ROOT / "outputs/parent_tmds/canonical/canonical_quark_spin1_tmd_bands.csv"
WAVE = ROOT / "outputs/parent_tmds/rich_ensemble/quark_parent_tmd_ensemble.csv"
DIRECT_BANDS = {
    "f1Tperp": ROOT / "outputs/parent_tmds/ensemble/bpv20_sivers_bands.csv",
    "h1": ROOT / "outputs/parent_tmds/ensemble/jamdiff_transversity_bands.csv",
    "h1Lperp": ROOT / "outputs/parent_tmds/ensemble/jamdiff_h1Lperp_bands.csv",
}
OUT = ROOT / "output/figures/wp12_inspection"
DENSE = OUT / "wp12_quark_constituent_smooth_bands.csv"
GRID = np.linspace(0.0, 1.5, 241)


def style(axis, title):
    axis.axhline(0, color="0.4", linewidth=0.6)
    axis.grid(True, alpha=0.18, linewidth=0.45)
    axis.set_title(title, loc="left", fontsize=10)
    axis.tick_params(labelsize=7)
    axis.ticklabel_format(axis="y", style="sci", scilimits=(-2, 2))


def pchip(block, column, grid=GRID):
    block = block.sort_values("k_GeV")
    return np.asarray(PchipInterpolator(
        block.k_GeV.to_numpy(), block[column].to_numpy(),
        extrapolate=False,
    )(grid))


def smooth_halfwidth(values):
    values = median_filter(np.maximum(values, 0.0), size=9, mode="nearest")
    values = savgol_filter(values, 21, 3, mode="interp")
    return np.maximum(values, 0.0)


def build_smooth_bands(frame, bands, wave, direct_bands):
    """Propagate named parent axes onto resolved impulse components.

    The central lines are shape-preserving PCHIP interpolants through the
    calculated knots. Wave/model uncertainty is apportioned between proton
    and neutron using their local absolute-amplitude shares, regularized by
    the corresponding f1 shares at a TMD zero. Nuclear uncertainty remains
    assigned to the separate nuclear-correction component and is not folded
    into a constituent.
    """
    bands = bands[np.isclose(bands.x_N, 0.1)]
    rows = []
    for (tmd, flavor), group in frame.groupby(["tmd", "flavor"], sort=False):
        components = {}
        for component in ("proton_in_deuteron", "neutron_in_deuteron"):
            components[component] = pchip(
                group[group.component.eq(component)], "F_GeV-2"
            )
        f1_components = {}
        for component in components:
            source = frame[
                frame.tmd.eq("f1") & frame.flavor.eq(flavor)
                & frame.component.eq(component)
            ]
            f1_components[component] = np.abs(pchip(source, "F_GeV-2"))
        source_band = bands[
            bands.tmd.eq(tmd) & bands.flavor.eq(flavor)
        ].copy()
        source_wave = wave[
            wave.tmd.eq(tmd) & wave.flavor.eq(flavor)
            & np.isclose(wave.x_N, 0.1)
        ].copy()
        source_wave["absolute_wave_halfwidth"] = np.maximum(
            source_wave["F_central_GeV-2"]
            - source_wave["F_wave_low_GeV-2"],
            source_wave["F_wave_high_GeV-2"]
            - source_wave["F_central_GeV-2"],
        )
        parent_half = smooth_halfwidth(
            pchip(source_wave, "absolute_wave_halfwidth")
            + pchip(source_band, "model_halfwidth_GeV-2")
        )
        denominator = (
            np.abs(components["proton_in_deuteron"])
            + np.abs(components["neutron_in_deuteron"])
            + 0.05 * (
                f1_components["proton_in_deuteron"]
                + f1_components["neutron_in_deuteron"]
            )
        )
        for component, central in components.items():
            share = (
                np.abs(central) + 0.05*f1_components[component]
            ) / np.maximum(denominator, 1e-15)
            half = np.maximum(parent_half, 0.0)*share
            semantics = (
                "wave+model parent envelope apportioned by local resolved "
                "amplitude/f1 share; nuclear axis belongs to the separate "
                "nuclear-correction component; not CI"
            )
            if tmd in direct_bands:
                direct = direct_bands[tmd]
                mechanism = (
                    "proton_impulse" if component == "proton_in_deuteron"
                    else "neutron_impulse"
                )
                direct = direct[
                    direct.flavor.eq(flavor)
                    & direct.mechanism.eq(mechanism)
                    & direct.gauge_link.eq("[+,+]")
                    & np.isclose(direct.x_N, 0.1)
                ].copy()
                direct["fit_halfwidth"] = np.maximum(
                    np.abs(direct["F_q84_GeV-2"]
                           - direct["F_replica_median_GeV-2"]),
                    np.abs(direct["F_replica_median_GeV-2"]
                           - direct["F_q16_GeV-2"]),
                )
                direct["wave_halfwidth"] = np.maximum(
                    np.abs(direct["F_central_GeV-2"]
                           - direct["F_wave_low_GeV-2"]),
                    np.abs(direct["F_wave_high_GeV-2"]
                           - direct["F_central_GeV-2"]),
                )
                direct["combined_halfwidth"] = np.hypot(
                    direct["fit_halfwidth"], direct["wave_halfwidth"]
                )
                half = smooth_halfwidth(np.nan_to_num(
                    pchip(direct, "combined_halfwidth"), nan=0.0
                ))
                semantics = (
                    "direct 16-84% external-fit replica halfwidth combined "
                    "in quadrature with wave-function envelope; applied to "
                    "resolved central; nuclear axis remains separate; not a "
                    "joint confidence interval"
                )
            for k, value, width in zip(GRID, central, half):
                rows.append({
                    "species": "q", "flavor": int(flavor), "tmd": tmd,
                    "component": component, "x_N": 0.1, "Q_GeV": 5.0,
                    "k_GeV": k, "F_central_GeV-2": value,
                    "F_low_GeV-2": value-width,
                    "F_high_GeV-2": value+width,
                    "constituent_halfwidth_GeV-2": width,
                    "central_interpolation": (
                        "shape-preserving PCHIP through calculated knots"
                    ),
                    "band_semantics": semantics,
                })
    return pd.DataFrame(rows)


def overview(frame, flavors, path, heading):
    series = (
        ("proton_in_deuteron", flavors[0], "proton", "#1464A0", "-"),
        ("proton_in_deuteron", flavors[1], "proton", "#C4473A", "-"),
        ("neutron_in_deuteron", flavors[0], "neutron", "#1464A0", "--"),
        ("neutron_in_deuteron", flavors[1], "neutron", "#C4473A", "--"),
    )
    flavor_label = {
        2: "u", 1: "d", -2: r"$\bar u$", -1: r"$\bar d$"
    }
    fig, axes = plt.subplots(6, 3, figsize=(14.2, 20), sharex=True)
    for axis, (name, title) in zip(axes.flat, QLABELS.items()):
        for component, flavor, nucleon, color, line in series:
            block = frame[
                frame.tmd.eq(name) & frame.component.eq(component)
                & frame.flavor.eq(flavor)
            ].sort_values("k_GeV")
            axis.fill_between(
                block.k_GeV, block["F_low_GeV-2"],
                block["F_high_GeV-2"], color=color, alpha=0.10,
                linewidth=0,
            )
            axis.plot(
                block.k_GeV, block["F_central_GeV-2"], color=color,
                linestyle=line, linewidth=1.65,
                label=f"{nucleon} {flavor_label[flavor]}",
            )
        style(axis, title)
    for axis in axes[-1]:
        axis.set_xlabel(r"$k_T$ [GeV]", fontsize=8)
    axes[0, 0].legend(frameon=False, fontsize=7, ncol=2)
    fig.supylabel(r"constituent $F(x_N,k_T;Q)$ [GeV$^{-2}$]")
    fig.suptitle(
        "Constituent audit (not the deuteron observable): " + heading
        + r"  |  $x_N=0.1,\ Q=5$ GeV, future staple",
        fontsize=15,
    )
    fig.text(
        0.5, 0.009,
        "Shading: direct fit-replica bands where available, otherwise "
        "propagated wave + model envelope; nuclear uncertainty is retained "
        "in the separate nuclear-correction component; not a joint CI.",
        ha="center", fontsize=8,
    )
    fig.tight_layout(rect=(0.035, 0.025, 0.995, 0.97))
    fig.savefig(path, dpi=180)
    plt.close(fig)


def sivers(frame):
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4), sharex=True)
    colors = {2: "#1464A0", 1: "#C4473A"}
    for axis, component, title in (
        (axes[0], "proton_in_deuteron", "Proton constituent"),
        (axes[1], "neutron_in_deuteron", "Neutron constituent"),
    ):
        for flavor, label in ((2, r"$u$"), (1, r"$d$")):
            block = frame[
                frame.component.eq(component)
                & frame.flavor.eq(flavor) & frame.tmd.eq("f1Tperp")
            ].sort_values("k_GeV")
            axis.fill_between(
                block.k_GeV, block["F_low_GeV-2"],
                block["F_high_GeV-2"], color=colors[flavor],
                alpha=0.14, linewidth=0,
            )
            axis.plot(
                block.k_GeV, block["F_central_GeV-2"],
                color=colors[flavor],
                linewidth=2.2, label=label,
            )
        style(axis, title)
        axis.set_xlabel(r"$k_T$ [GeV]")
        axis.set_ylabel(r"$f_{1T}^{\perp}$ [GeV$^{-2}$]")
        axis.legend(frameon=False)
    fig.suptitle(
        r"Opposite flavor-orbital dynamics before the spin-1 sum  |  "
        r"$x_N=0.1,\ Q=5$ GeV",
        fontsize=14,
    )
    fig.text(
        0.5, 0.01,
        "Shading: BPV20 replica (16–84%) and wave-function envelope; "
        "not a joint CI.",
        ha="center", fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.035, 1, 0.93))
    fig.savefig(OUT / "wp12_sivers_proton_neutron_decomposition.png", dpi=200)
    plt.close(fig)


def main():
    frame = pd.read_csv(SOURCE)
    frame = frame[
        np.isclose(frame.x_N, 0.1) & frame.gauge_link.eq("[+,+]")
    ]
    OUT.mkdir(parents=True, exist_ok=True)
    direct_bands = {
        name: pd.read_csv(path) for name, path in DIRECT_BANDS.items()
    }
    frame = build_smooth_bands(
        frame, pd.read_csv(BANDS), pd.read_csv(WAVE), direct_bands
    )
    frame.to_csv(DENSE, index=False)
    overview(
        frame, (2, 1),
        OUT / "wp12_quark_valence_constituent_all_tmd.png",
        "Resolved proton/neutron valence-sector TMDs",
    )
    overview(
        frame, (-2, -1),
        OUT / "wp12_quark_sea_constituent_all_tmd.png",
        "Resolved proton/neutron antiquark-sector TMDs",
    )
    sivers(frame)
    print(f"Wrote constituent-resolved plots to {OUT}")


if __name__ == "__main__":
    main()
