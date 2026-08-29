#!/usr/bin/env python3
"""Build convergence summaries and wave-function bands for gluon TMD grids."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

ROOT = Path("outputs/stage0")
TMDS = ("f1g", "h1perpg", "f1LLg", "h1LLperpg")
BAND_TMDS = TMDS + (
    "g1g", "h1Lperpg",
    "f1Tperpg", "g1Tg", "h1Tg", "h1Tperpg",
    "f1LTg", "g1LTg", "h1LTg", "h1LTperpg",
)
WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")


def scalar(data: np.lib.npyio.NpzFile, name: str) -> float:
    return float(np.asarray(data[name]).item())


def write_convergence() -> None:
    cases = (
        ("external_n16", "convergence/gluon_tmd_av18_external_n16.npz", 16, 16, 12, 8),
        ("external_n24", "gluon_tmd_ia_av18.npz", 24, 16, 12, 8),
        ("external_n32", "convergence/gluon_tmd_av18_external_n32.npz", 32, 16, 12, 8),
        ("internal_12x8x8", "convergence/gluon_tmd_av18_internal_12x8x8.npz", 16, 12, 8, 8),
        ("internal_16x12x8", "convergence/gluon_tmd_av18_external_n16.npz", 16, 16, 12, 8),
        ("internal_24x16x12", "convergence/gluon_tmd_av18_internal_24x16x12.npz", 16, 24, 16, 12),
    )
    reference = np.load(ROOT / "convergence/gluon_tmd_av18_internal_24x16x12.npz")
    rows = []
    for label, relative, n_grid, n_internal, n_cos, n_phi in cases:
        data = np.load(ROOT / relative)
        row = {
            "case": label,
            "n_k_grid": n_grid,
            "n_internal_k": n_internal,
            "n_cos": n_cos,
            "n_phi": n_phi,
            "smearing_norm": scalar(data, "smearing_norm"),
            "f1g_relative_error": scalar(data, "f1g_relative_error"),
            "f1LLg_relative_error": scalar(data, "f1LLg_relative_error"),
        }
        if n_grid == 16:
            for name in TMDS:
                numerator = np.linalg.norm(data[name] - reference[name])
                denominator = np.linalg.norm(reference[name])
                row[f"{name}_relative_L2_vs_fine_internal"] = float(
                    numerator / denominator if denominator else np.nan
                )
        else:
            for name in TMDS:
                row[f"{name}_relative_L2_vs_fine_internal"] = float("nan")
        rows.append(row)
    output = ROOT / "convergence/gluon_tmd_av18_summary.csv"
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_band() -> None:
    datasets = [np.load(ROOT / f"gluon_tmd_ia_{wave}.npz") for wave in WAVES]
    axis = datasets[0]["k_x_GeV"]
    for data in datasets[1:]:
        np.testing.assert_array_equal(data["k_x_GeV"], axis)
        np.testing.assert_array_equal(data["k_y_GeV"], axis)
    normalizations = np.asarray(
        [scalar(data, "smearing_norm") for data in datasets]
    )
    arrays = {
        name: np.stack(
            [
                data[name] / normalization
                for data, normalization in zip(datasets, normalizations)
            ],
            axis=0,
        )
        for name in BAND_TMDS
    }
    payload: dict[str, np.ndarray] = {
        "wave_functions": np.asarray(WAVES),
        "input_smearing_norms": normalizations,
        "normalized_by_smearing_norm": np.asarray(1),
        "k_x_GeV": axis,
        "k_y_GeV": axis,
    }
    for name, values in arrays.items():
        payload[f"{name}_minimum"] = np.min(values, axis=0)
        payload[f"{name}_maximum"] = np.max(values, axis=0)
        payload[f"{name}_mean"] = np.mean(values, axis=0)
    (ROOT / "uncertainty").mkdir(parents=True, exist_ok=True)
    np.savez_compressed(ROOT / "uncertainty/gluon_tmd_wave_function_band.npz", **payload)

    near_zero = int(np.argmin(np.abs(axis)))
    rows = []
    for index, k_x in enumerate(axis):
        row = {"k_x_GeV": float(k_x), "k_y_GeV": float(axis[near_zero])}
        for name in BAND_TMDS:
            row[f"{name}_minimum"] = float(payload[f"{name}_minimum"][index, near_zero])
            row[f"{name}_maximum"] = float(payload[f"{name}_maximum"][index, near_zero])
            row[f"{name}_mean"] = float(payload[f"{name}_mean"][index, near_zero])
        rows.append(row)
    output = ROOT / "uncertainty/gluon_tmd_wave_function_band_slice.csv"
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_convergence()
    write_band()
