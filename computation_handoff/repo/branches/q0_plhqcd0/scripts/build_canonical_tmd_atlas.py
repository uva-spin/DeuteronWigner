#!/usr/bin/env python3
"""Build smooth canonical quark/gluon spin-1 TMD atlases with theory bands."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

from deuteron_wigner.gluon_lfwf_todd import GluonWilsonLineKernel


QUARK = Path("outputs/parent_tmds/quark_av18_rich_medium.csv")
GLUON = Path("outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.csv")
QWAVE = Path("outputs/parent_tmds/rich_ensemble/quark_parent_tmd_ensemble.csv")
GWAVE = Path("outputs/parent_tmds/rich_ensemble/gluon_parent_tmd_ensemble.csv")
OUTPUT_DIR = Path("outputs/parent_tmds/canonical")
PDF_DIR = Path("output/pdf")
QPDF = PDF_DIR / "canonical_quark_spin1_tmd_atlas.pdf"
GPDF = PDF_DIR / "canonical_gluon_spin1_tmd_atlas.pdf"
QCSV = OUTPUT_DIR / "canonical_quark_spin1_tmd_bands.csv"
GCSV = OUTPUT_DIR / "canonical_gluon_spin1_tmd_bands.csv"

QUARK_LABELS = {
    "f1": r"$f_1$", "h1perp": r"$h_1^\perp$", "g1": r"$g_1$",
    "h1Lperp": r"$h_{1L}^\perp$", "f1Tperp": r"$f_{1T}^\perp$",
    "g1T": r"$g_{1T}$", "h1": r"$h_1$", "h1Tperp": r"$h_{1T}^\perp$",
    "f1LL": r"$f_{1LL}$", "h1LLperp": r"$h_{1LL}^\perp$",
    "f1LT": r"$f_{1LT}$", "g1LT": r"$g_{1LT}$",
    "h1LT": r"$h_{1LT}$", "h1LTperp": r"$h_{1LT}^\perp$",
    "f1TT": r"$f_{1TT}$", "g1TT": r"$g_{1TT}$",
    "h1TT": r"$h_{1TT}$", "h1TTperp": r"$h_{1TT}^\perp$",
}
GLUON_LABELS = dict(QUARK_LABELS)
GLUON_LABELS["h1perp"] = r"$h_1^{\perp g}$"
GLUON_LABELS["f1TT_minus_h1TTperp"] = (
    r"$f_{1TT}^g-h_{1TT}^{\perp g}$"
)
GLUON_LABELS["h1TTperpperp"] = r"$h_{1TT}^{\perp\perp g}$"


def pchip(frame: pd.DataFrame, column: str, grid: np.ndarray) -> np.ndarray:
    ordered = frame.sort_values("k_GeV")
    return np.asarray(PchipInterpolator(
        ordered.k_GeV.to_numpy(), ordered[column].to_numpy(),
        extrapolate=False,
    )(grid), dtype=float)


def relative_wave_halfwidth(
    ensemble: pd.DataFrame,
    *,
    tmd: str,
    flavor: int | None,
    grid: np.ndarray,
) -> np.ndarray:
    selected = ensemble.loc[ensemble.tmd.eq(tmd)]
    if flavor is not None and "flavor" in selected:
        selected = selected.loc[selected.flavor.eq(flavor)]
    if selected.empty:
        return np.zeros_like(grid)
    xname = "k_GeV" if "k_GeV" in selected else "k_T_GeV"
    selected = selected.sort_values(xname)
    central = np.asarray(PchipInterpolator(
        selected[xname], selected["F_central_GeV-2"],
        extrapolate=False,
    )(grid))
    low = np.asarray(PchipInterpolator(
        selected[xname], selected["F_wave_low_GeV-2"],
        extrapolate=False,
    )(grid))
    high = np.asarray(PchipInterpolator(
        selected[xname], selected["F_wave_high_GeV-2"],
        extrapolate=False,
    )(grid))
    scale = np.maximum(np.abs(central), 1.0e-12)
    return np.maximum(abs(low-central), abs(high-central)) / scale


def build_quark() -> pd.DataFrame:
    source = pd.read_csv(QUARK)
    wave = pd.read_csv(QWAVE)
    future = source.loc[source.gauge_link.eq("[+,+]")]
    grid = np.linspace(0.0, 1.5, 241)
    rows = []
    model_uncertain = {"h1perp", "g1T", "h1Tperp", "g1LT", "g1TT"}
    for flavor in (2, 1, -2, -1):
        flavor_frame = future.loc[future.flavor.eq(flavor)]
        for tmd in QUARK_LABELS:
            total = flavor_frame.loc[
                flavor_frame.mechanism.eq("model_total")
                & flavor_frame.tmd.eq(tmd)
            ]
            central = pchip(total, "F_GeV-2", grid)
            wave_rel = relative_wave_halfwidth(
                wave, tmd=tmd, flavor=flavor, grid=grid
            )
            wave_half = wave_rel * abs(central)
            nuclear_half = np.zeros_like(grid)
            for mechanism, weight in (
                ("coherent_shadowing", 0.20),
                ("antishadowing", 0.50),
                ("meson_exchange", 1.00),
                ("off_shell", 0.50),
            ):
                part = flavor_frame.loc[
                    flavor_frame.mechanism.eq(mechanism)
                    & flavor_frame.tmd.eq(tmd)
                ]
                nuclear_half += weight * abs(pchip(part, "F_GeV-2", grid))
            model_half = (
                0.50 * abs(central) if tmd in model_uncertain
                else np.zeros_like(grid)
            )
            if tmd == "h1perp":
                model_half = abs(central)
            half = wave_half + nuclear_half + model_half
            for k, c, h, hw, hn, hm in zip(
                grid, central, half, wave_half, nuclear_half, model_half
            ):
                rows.append({
                    "species": "q" if flavor > 0 else "qbar",
                    "flavor": flavor,
                    "flavor_label": {2: "u", 1: "d", -2: "ubar", -1: "dbar"}[flavor],
                    "tmd": tmd,
                    "x_N": 0.1, "Q_GeV": 5.0, "k_GeV": k,
                    "F_central_GeV-2": c,
                    "F_low_GeV-2": c-h,
                    "F_high_GeV-2": c+h,
                    "wave_halfwidth_GeV-2": hw,
                    "nuclear_halfwidth_GeV-2": hn,
                    "model_halfwidth_GeV-2": hm,
                    "band_semantics": "conservative named-axis theory envelope",
                })
    return pd.DataFrame(rows)


def build_gluon() -> pd.DataFrame:
    source = pd.read_csv(GLUON)
    wave = pd.read_csv(GWAVE)
    links = {
        "f_type_antisymmetric": "[+,+]",
        "d_type_symmetric": "[+,-]",
    }
    grid = np.linspace(0.05, 1.0, 241)
    central_kernel = GluonWilsonLineKernel(
        alpha_s=0.30, screening_mass_gev=0.36, remnant_scale_gev=0.90,
        n_q=48, n_phi=64,
    )
    soft_kernel = GluonWilsonLineKernel(
        alpha_s=0.24, screening_mass_gev=0.45, remnant_scale_gev=0.75,
        n_q=48, n_phi=64,
    )
    strong_kernel = GluonWilsonLineKernel(
        alpha_s=0.36, screening_mass_gev=0.28, remnant_scale_gev=1.05,
        n_q=48, n_phi=64,
    )
    rows = []
    for color, link in links.items():
        selected = source.loc[
            source.color_structure.eq(color) & source.gauge_link.eq(link)
        ]
        for tmd in sorted(source.tmd.unique()):
            total = selected.loc[
                selected.mechanism.eq("model_total") & selected.tmd.eq(tmd)
            ]
            central = pchip(total, "F_GeV-2", grid)
            wave_rel = relative_wave_halfwidth(
                wave, tmd=tmd, flavor=None, grid=grid
            )
            wave_half = wave_rel * abs(central)
            nuclear_half = np.zeros_like(grid)
            for mechanism, weight in (
                ("coherent_shadowing", 0.20),
                ("antishadowing", 0.50),
                ("meson_exchange", 1.00),
            ):
                part = selected.loc[
                    selected.mechanism.eq(mechanism)
                    & selected.tmd.eq(tmd)
                ]
                nuclear_half += weight * abs(pchip(part, "F_GeV-2", grid))
            rank = int(total["rank"].iloc[0])
            todd = bool(total["t_odd"].iloc[0])
            model_half = np.zeros_like(grid)
            if todd:
                harmonic_rank = max(1, min(rank, 3))
                ratios = []
                for k in grid:
                    center = central_kernel.harmonic(k, 0.30, harmonic_rank)
                    variants = (
                        soft_kernel.harmonic(k, 0.30, harmonic_rank),
                        strong_kernel.harmonic(k, 0.30, harmonic_rank),
                    )
                    ratios.append(
                        max(abs(value/center-1.0) for value in variants)
                        if center else 0.0
                    )
                model_half = np.asarray(ratios) * abs(central)
                if color == "d_type_symmetric":
                    model_half += 0.50 * abs(central)
            half = wave_half + nuclear_half + model_half
            for k, c, h, hw, hn, hm in zip(
                grid, central, half, wave_half, nuclear_half, model_half
            ):
                rows.append({
                    "species": "g", "flavor": 21,
                    "color_structure": color, "gauge_link": link,
                    "tmd": tmd, "rank": rank, "t_odd": int(todd),
                    "x_N": 0.1, "Q_GeV": 5.0, "k_GeV": k,
                    "F_central_GeV-2": c,
                    "F_low_GeV-2": c-h,
                    "F_high_GeV-2": c+h,
                    "wave_halfwidth_GeV-2": hw,
                    "nuclear_halfwidth_GeV-2": hn,
                    "model_halfwidth_GeV-2": hm,
                    "band_semantics": "conservative named-axis theory envelope",
                })
    return pd.DataFrame(rows)


def style_axis(axis, tmd: str) -> None:
    axis.axhline(0.0, color="#707070", linewidth=0.7, zorder=0)
    axis.grid(True, alpha=0.18, linewidth=0.6)
    axis.set_xlabel(r"$k_T$ [GeV]")
    axis.set_ylabel(r"$F(x,k_T;Q)$ [GeV$^{-2}$]")
    axis.ticklabel_format(axis="y", style="sci", scilimits=(-3, 3))
    axis.set_title(tmd, loc="left", fontsize=11, fontweight="semibold")


def plot_quark(frame: pd.DataFrame) -> None:
    flavors = ((2, "u"), (1, "d"), (-2, r"$\bar u$"), (-1, r"$\bar d$"))
    with PdfPages(QPDF) as pdf:
        for tmd, label in QUARK_LABELS.items():
            fig, axes = plt.subplots(2, 2, figsize=(10.2, 7.6), sharex=True)
            for axis, (flavor, flavor_label) in zip(axes.flat, flavors):
                block = frame.loc[
                    frame.tmd.eq(tmd) & frame.flavor.eq(flavor)
                ]
                axis.fill_between(
                    block.k_GeV, block["F_low_GeV-2"],
                    block["F_high_GeV-2"], color="#4C78A8", alpha=0.24,
                    linewidth=0.0, label="named-axis theory envelope",
                )
                axis.plot(
                    block.k_GeV, block["F_central_GeV-2"],
                    color="#174A7E", linewidth=2.0, label="canonical central",
                )
                style_axis(axis, flavor_label)
            axes[0, 0].legend(frameon=False, fontsize=8)
            fig.suptitle(
                f"Canonical spin-1 quark TMD {label}  |  "
                r"$x_N=0.1,\ Q=5$ GeV, future staple",
                fontsize=14, fontweight="bold",
            )
            fig.text(
                0.5, 0.015,
                "Band: wave-function + sourced nuclear + named model axes; "
                "not a statistical confidence interval.",
                ha="center", fontsize=8, color="#444444",
            )
            fig.tight_layout(rect=(0.02, 0.04, 0.98, 0.94))
            pdf.savefig(fig)
            plt.close(fig)


def plot_gluon(frame: pd.DataFrame) -> None:
    colors = (
        ("f_type_antisymmetric", r"$f^{abc}$ / [+,+]"),
        ("d_type_symmetric", r"$d^{abc}$ / [+,-]"),
    )
    for tmd in sorted(frame.tmd.unique()):
        GLUON_LABELS.setdefault(tmd, f"${tmd}^g$")
    with PdfPages(GPDF) as pdf:
        for tmd in sorted(frame.tmd.unique()):
            fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.4), sharex=True)
            for axis, (color, color_label) in zip(axes, colors):
                block = frame.loc[
                    frame.tmd.eq(tmd) & frame.color_structure.eq(color)
                ]
                axis.fill_between(
                    block.k_GeV, block["F_low_GeV-2"],
                    block["F_high_GeV-2"], color="#E07B39", alpha=0.25,
                    linewidth=0.0, label="named-axis theory envelope",
                )
                axis.plot(
                    block.k_GeV, block["F_central_GeV-2"],
                    color="#A34716", linewidth=2.0, label="canonical central",
                )
                style_axis(axis, color_label)
            axes[0].legend(frameon=False, fontsize=8)
            fig.suptitle(
                f"Canonical spin-1 gluon TMD {GLUON_LABELS[tmd]}  |  "
                r"$x_N=0.1,\ Q=5$ GeV",
                fontsize=14, fontweight="bold",
            )
            fig.text(
                0.5, 0.015,
                "f- and d-type color structures are independent. Band: "
                "wave + nuclear + Wilson-kernel/color axes.",
                ha="center", fontsize=8, color="#444444",
            )
            fig.tight_layout(rect=(0.02, 0.05, 0.98, 0.91))
            pdf.savefig(fig)
            plt.close(fig)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
    })
    quark = build_quark()
    gluon = build_gluon()
    quark.to_csv(QCSV, index=False)
    gluon.to_csv(GCSV, index=False)
    plot_quark(quark)
    plot_gluon(gluon)
    print(
        f"Wrote {len(quark)} quark and {len(gluon)} gluon band rows; "
        f"{QPDF}; {GPDF}"
    )


if __name__ == "__main__":
    main()
