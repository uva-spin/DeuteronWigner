#!/usr/bin/env python3
"""Build pre-evolution inspection plots from the composed WP12 boundary."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from scipy.ndimage import median_filter
from scipy.signal import savgol_filter


ROOT = Path(__file__).resolve().parents[1]
Q = ROOT / "outputs/parent_tmds/wp12_canonical_composed_quark.csv"
G = ROOT / "outputs/parent_tmds/wp12_canonical_composed_gluon.csv"
QBAND = ROOT / (
    "outputs/parent_tmds/canonical/canonical_quark_spin1_tmd_bands.csv"
)
GBAND = ROOT / (
    "outputs/parent_tmds/canonical/canonical_gluon_spin1_tmd_bands.csv"
)
QWAVE = ROOT / "outputs/parent_tmds/rich_ensemble/quark_parent_tmd_ensemble.csv"
GWAVE = ROOT / "outputs/parent_tmds/rich_ensemble/gluon_parent_tmd_ensemble.csv"
QF1PDF = ROOT / "outputs/parent_tmds/ensemble/ct18_quark_f1_hessian_x010.csv"
QG1PDF = ROOT / "outputs/parent_tmds/ensemble/bdssv24_quark_g1_bands_x010.csv"
GF1PDF = ROOT / "outputs/parent_tmds/ensemble/ct18_gluon_f1_hessian_response.csv"
CSB = ROOT / "outputs/parent_tmds/wp12_csb_power_counting_envelope.csv"
OUT = ROOT / "output/figures/wp12_inspection"
QOUT = OUT / "wp12_quark_inspection_bands.csv"
GOUT = OUT / "wp12_gluon_inspection_bands.csv"
MASS = 1.87561294257

QLABELS = {
    "f1": r"$f_1$", "h1perp": r"$h_1^\perp$", "g1": r"$g_1$",
    "h1Lperp": r"$h_{1L}^\perp$", "f1Tperp": r"$f_{1T}^\perp$",
    "g1T": r"$g_{1T}$", "h1": r"$h_1$",
    "h1Tperp": r"$h_{1T}^\perp$", "f1LL": r"$f_{1LL}$",
    "h1LLperp": r"$h_{1LL}^\perp$", "f1LT": r"$f_{1LT}$",
    "g1LT": r"$g_{1LT}$", "h1LT": r"$h_{1LT}$",
    "h1LTperp": r"$h_{1LT}^\perp$", "f1TT": r"$f_{1TT}$",
    "g1TT": r"$g_{1TT}$", "h1TT": r"$h_{1TT}$",
    "h1TTperp": r"$h_{1TT}^\perp$",
}
GLABELS = dict(QLABELS)
GLABELS.pop("f1TT")
GLABELS.pop("h1TTperp")
GLABELS.update({
    "h1perp": r"$h_1^{\perp g}$",
    "f1TT_minus_h1TTperp": r"$f_{1TT}^g-h_{1TT}^{\perp g}$",
    "h1TTperpperp": r"$h_{1TT}^{\perp\perp g}$",
})
QRANK = {
    "f1": 0, "h1perp": 1, "g1": 0, "h1Lperp": 1,
    "f1Tperp": 1, "g1T": 1, "h1": 0, "h1Tperp": 2,
    "f1LL": 0, "h1LLperp": 2, "f1LT": 1, "g1LT": 1,
    "h1LT": 0, "h1LTperp": 2, "f1TT": 2, "g1TT": 2,
    "h1TT": 1, "h1TTperp": 3,
}

FLAVORS = (
    (2, r"$u$", "#1464A0"), (1, r"$d$", "#C4473A"),
    (-2, r"$\bar u$", "#4D9221"), (-1, r"$\bar d$", "#7B4AB5"),
)
COLORS = (
    ("f_type_antisymmetric", r"$f^{abc}$, $[+,+]$", "#1464A0"),
    ("d_type_symmetric", r"$d^{abc}$, $[+,-]$", "#C4473A"),
)


def interpolate(block: pd.DataFrame, grid: np.ndarray) -> np.ndarray:
    block = block.sort_values("k_GeV")
    return np.asarray(PchipInterpolator(
        block.k_GeV.to_numpy(), block["F_GeV-2"].to_numpy(),
        extrapolate=False,
    )(grid))


def shifted_bands(
    central: pd.DataFrame, old: pd.DataFrame, wave: pd.DataFrame, *,
    gluon: bool,
) -> pd.DataFrame:
    group_keys = ["tmd", "color_structure"] if gluon else ["tmd", "flavor"]
    rows = []
    csb_table = pd.read_csv(CSB)
    qf1_pdf = pd.read_csv(QF1PDF) if not gluon else None
    qg1_pdf = pd.read_csv(QG1PDF) if not gluon else None
    gf1_pdf = pd.read_csv(GF1PDF) if gluon else None
    for key, old_block in old.groupby(group_keys, sort=False):
        if not isinstance(key, tuple):
            key = (key,)
        select = central.tmd.eq(key[0]) & np.isclose(central.x_N, 0.1)
        if gluon:
            select &= central.color_structure.eq(key[1])
            select &= central.gauge_link.eq(
                "[+,+]" if key[1] == "f_type_antisymmetric" else "[+,-]"
            )
        else:
            select &= central.flavor.eq(key[1])
            select &= central.gauge_link.eq("[+,+]")
        source = central[select]
        grid = old_block.k_GeV.to_numpy()
        new_central = interpolate(source, grid)
        old_central = old_block["F_central_GeV-2"].to_numpy()
        wave_select = wave.tmd.eq(key[0])
        if not gluon:
            wave_select &= wave.flavor.eq(key[1])
        wave_block = wave[wave_select].sort_values("k_GeV")
        wave_absolute = np.maximum(
            wave_block["F_central_GeV-2"].to_numpy()
            - wave_block["F_wave_low_GeV-2"].to_numpy(),
            wave_block["F_wave_high_GeV-2"].to_numpy()
            - wave_block["F_central_GeV-2"].to_numpy(),
        )
        wave_half = np.asarray(PchipInterpolator(
            wave_block.k_GeV.to_numpy(), wave_absolute,
            extrapolate=False,
        )(grid))
        wave_half = np.nan_to_num(wave_half, nan=0.0)
        inherited_raw = (
            wave_half
            + old_block["nuclear_halfwidth_GeV-2"].to_numpy()
            + old_block["model_halfwidth_GeV-2"].to_numpy()
        )
        # Earlier relative wave envelopes divide by central functions and
        # can acquire isolated spikes when a TMD crosses zero. Those spikes
        # are numerical band-construction artifacts, not physical
        # uncertainties. Smooth the non-negative halfwidth itself without
        # altering the composed central line.
        inherited = median_filter(
            inherited_raw, size=9, mode="nearest"
        )
        window = min(21, len(inherited) if len(inherited) % 2 else len(inherited)-1)
        if window >= 5:
            inherited = savgol_filter(
                inherited, window_length=window, polyorder=3, mode="interp"
            )
        inherited = np.maximum(inherited, 0.0)
        composition = np.abs(new_central-old_central)
        pdf_half = np.zeros_like(new_central)
        if not gluon and key[0] in ("f1", "g1"):
            source_pdf = qf1_pdf if key[0] == "f1" else qg1_pdf
            source_pdf = source_pdf[
                source_pdf.flavor.eq(key[1])
                & source_pdf.mechanism.eq("model_total")
                & source_pdf.gauge_link.eq("[+,+]")
            ].copy()
            source_pdf["pdf_half"] = (
                source_pdf["F_replica_std_GeV-2"]
                if key[0] == "f1" else
                np.maximum(
                    source_pdf["F_q84_GeV-2"]
                    - source_pdf["F_central_GeV-2"],
                    source_pdf["F_central_GeV-2"]
                    - source_pdf["F_q16_GeV-2"],
                )
            )
            pdf_half = np.nan_to_num(PchipInterpolator(
                source_pdf.k_GeV, source_pdf.pdf_half,
                extrapolate=False,
            )(grid), nan=0.0)
        elif gluon and key[0] == "f1":
            source_pdf = gf1_pdf[np.isclose(gf1_pdf.x_N, 0.1)]
            response = np.asarray(PchipInterpolator(
                source_pdf.k_GeV, source_pdf["response_central_GeV-2"],
                extrapolate=False,
            )(grid))
            sigma = np.asarray(PchipInterpolator(
                source_pdf.k_GeV, source_pdf["hessian_sigma_GeV-2"],
                extrapolate=False,
            )(grid))
            relative = sigma/np.maximum(np.abs(response), 1e-14)
            pdf_half = relative*np.abs(new_central)
        csb_select = (
            csb_table.species.eq("gluon" if gluon else "quark")
            & csb_table.tmd.eq(key[0])
            & np.isclose(csb_table.x_N, 0.1)
        )
        if gluon:
            csb_select &= csb_table.color_structure.eq(key[1])
            csb_select &= csb_table.gauge_link.eq(
                "[+,+]" if key[1] == "f_type_antisymmetric" else "[+,-]"
            )
        else:
            csb_select &= csb_table.flavor.eq(key[1])
            csb_select &= csb_table.gauge_link.eq("[+,+]")
        csb_source = csb_table[csb_select].sort_values("k_GeV")
        csb_half = np.nan_to_num(PchipInterpolator(
            csb_source.k_GeV, csb_source["csb_halfwidth_GeV-2"],
            extrapolate=False,
        )(grid), nan=0.0)
        half = inherited+composition+np.maximum(pdf_half, 0.0)+csb_half
        for (_, row), value, width, comp, raw_width, pdf_width, csb_width in zip(
            old_block.iterrows(), new_central, half, composition,
            inherited_raw, pdf_half, csb_half,
        ):
            item = row.to_dict()
            item.update({
                "F_central_GeV-2": value,
                "F_low_GeV-2": value-width,
                "F_high_GeV-2": value+width,
                "composition_halfwidth_GeV-2": comp,
                "pdf_halfwidth_GeV-2": float(pdf_width),
                "csb_halfwidth_GeV-2": float(csb_width),
                "inherited_raw_halfwidth_GeV-2": raw_width,
                "band_semantics": (
                    "conservative inherited named-axis envelope plus full "
                    "legacy-to-CP-composed central displacement; not a CI"
                ),
            })
            rows.append(item)
    return pd.DataFrame(rows)


def axis_style(axis, title: str, ratio: bool = False) -> None:
    axis.axhline(0, color="0.4", linewidth=0.6, alpha=0.7)
    axis.grid(True, linewidth=0.45, alpha=0.18)
    axis.set_title(title, loc="left", fontsize=10)
    axis.tick_params(labelsize=7)
    axis.ticklabel_format(axis="y", style="sci", scilimits=(-2, 2))


def overview(
    frame: pd.DataFrame, labels: dict[str, str], series, path: Path,
    *, gluon: bool, ratio: bool = False,
) -> None:
    names = list(labels)
    fig, axes = plt.subplots(6, 3, figsize=(14.2, 20.0), sharex=True)
    for axis, name in zip(axes.flat, names):
        for identity, label, color in series:
            block = frame[
                frame.tmd.eq(name)
                & (
                    frame.color_structure.eq(identity)
                    if gluon else frame.flavor.eq(identity)
                )
            ].sort_values("k_GeV")
            x = block.k_GeV.to_numpy()
            if ratio:
                f1 = frame[
                    frame.tmd.eq("f1")
                    & (
                        frame.color_structure.eq(identity)
                        if gluon else frame.flavor.eq(identity)
                    )
                ].sort_values("k_GeV")
                denominator = f1["F_central_GeV-2"].to_numpy()
                rank = int(block["rank"].iloc[0]) if gluon else QRANK[name]
                y = (
                    (x/MASS)**rank
                    * block["F_central_GeV-2"].to_numpy()
                    / np.maximum(np.abs(denominator), 1e-14)
                )
                axis.plot(x, y, color=color, linewidth=1.5, label=label)
            else:
                axis.fill_between(
                    x, block["F_low_GeV-2"], block["F_high_GeV-2"],
                    color=color, alpha=0.10, linewidth=0,
                )
                axis.plot(
                    x, block["F_central_GeV-2"], color=color,
                    linewidth=1.6, label=label,
                )
        axis_style(axis, labels[name], ratio)
    for axis in axes[-1]:
        axis.set_xlabel(r"$k_T$ [GeV]", fontsize=8)
    fig.supylabel(
        r"$(k_T/M)^r F/f_1$" if ratio
        else r"$F(x_N,k_T;Q)$ [GeV$^{-2}$]",
        fontsize=11,
    )
    axes[0, 0].legend(
        loc="best", frameon=False, fontsize=8, ncol=2,
    )
    fig.suptitle(
        ("Rank-weighted physical ratios" if ratio else "Canonical TMDs")
        + (" — flavor-resolved spin-1 deuteron gluons"
           if gluon else
           " — flavor-resolved spin-1 deuteron quarks and antiquarks")
        + r"  |  $x_N=0.1,\ Q=5$ GeV",
        fontsize=15,
    )
    if not ratio:
        fig.text(
            0.5, 0.012,
            "Shading: conservative named-axis envelope plus the complete "
            "legacy-to-CP-composed displacement; not a confidence interval.",
            ha="center", fontsize=9,
        )
    fig.tight_layout(rect=(0.035, 0.025, 0.995, 0.975))
    fig.savefig(path, dpi=180)
    plt.close(fig)


def multipage(
    frame: pd.DataFrame, labels: dict[str, str], series, path: Path,
    *, gluon: bool,
) -> None:
    with PdfPages(path) as pdf:
        for name, title in labels.items():
            n = len(series)
            fig, axes = plt.subplots(
                2, 2, figsize=(10.5, 7.6)
            ) if n == 4 else plt.subplots(1, 2, figsize=(10.5, 4.5))
            axes = np.asarray(axes).reshape(-1)
            for axis, (identity, label, color) in zip(axes, series):
                block = frame[
                    frame.tmd.eq(name)
                    & (
                        frame.color_structure.eq(identity)
                        if gluon else frame.flavor.eq(identity)
                    )
                ].sort_values("k_GeV")
                axis.fill_between(
                    block.k_GeV, block["F_low_GeV-2"],
                    block["F_high_GeV-2"], color=color, alpha=0.18,
                    linewidth=0, label="theory envelope",
                )
                axis.plot(
                    block.k_GeV, block["F_central_GeV-2"],
                    color=color, linewidth=2.0, label="canonical central",
                )
                axis_style(axis, label)
                axis.set_xlabel(r"$k_T$ [GeV]")
                axis.set_ylabel(r"$F$ [GeV$^{-2}$]")
            axes[0].legend(frameon=False, fontsize=8)
            fig.suptitle(
                f"{title}  |  " + r"$x_N=0.1,\ Q=5$ GeV",
                fontsize=14,
            )
            fig.tight_layout(rect=(0, 0, 1, 0.95))
            pdf.savefig(fig)
            plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    q = pd.read_csv(Q)
    g = pd.read_csv(G)
    qb = shifted_bands(
        q, pd.read_csv(QBAND), pd.read_csv(QWAVE), gluon=False
    )
    gb = shifted_bands(
        g, pd.read_csv(GBAND), pd.read_csv(GWAVE), gluon=True
    )
    qb.to_csv(QOUT, index=False)
    gb.to_csv(GOUT, index=False)
    overview(
        qb, QLABELS, FLAVORS, OUT / "wp12_quark_all_tmd_F_x010.png",
        gluon=False,
    )
    overview(
        gb, GLABELS, COLORS, OUT / "wp12_gluon_all_tmd_F_x010.png",
        gluon=True,
    )
    overview(
        qb, QLABELS, FLAVORS,
        OUT / "wp12_quark_all_tmd_rank_weighted_x010.png",
        gluon=False, ratio=True,
    )
    overview(
        gb, GLABELS, COLORS,
        OUT / "wp12_gluon_all_tmd_rank_weighted_x010.png",
        gluon=True, ratio=True,
    )
    multipage(
        qb, QLABELS, FLAVORS, OUT / "wp12_quark_tmd_inspection_atlas.pdf",
        gluon=False,
    )
    multipage(
        gb, GLABELS, COLORS, OUT / "wp12_gluon_tmd_inspection_atlas.pdf",
        gluon=True,
    )
    print(f"Wrote inspection figures and band tables to {OUT}")


if __name__ == "__main__":
    main()
