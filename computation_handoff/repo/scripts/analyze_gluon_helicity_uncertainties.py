#!/usr/bin/env python3
"""Assemble separate PDF, wave-function, and width sensitivity components."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

ROOT = Path("outputs/stage0/uncertainty")
WIDTH_FILES = {
    0.15: ROOT / "gluon_helicity_bdssv24_width015.npz",
    0.25: ROOT / "gluon_helicity_bdssv24_full.npz",
    0.40: ROOT / "gluon_helicity_bdssv24_width040.npz",
}
QUANTITIES = ("g1g", "g1Tg")


def main() -> None:
    width_data = {width: np.load(path) for width, path in WIDTH_FILES.items()}
    baseline = width_data[0.25]
    wave = np.load(ROOT / "gluon_tmd_wave_function_band.npz")
    axis = baseline["k_x_GeV"]
    payload: dict[str, np.ndarray] = {
        "k_x_GeV": axis,
        "k_y_GeV": axis,
        "widths_GeV2": np.asarray(tuple(WIDTH_FILES)),
        "baseline_width_GeV2": np.asarray(0.25),
    }
    rows = []
    origin = int(np.argmin(np.abs(axis)))
    for name in QUANTITIES:
        central = baseline[f"{name}_central"]
        pdf_std = baseline[f"{name}_std"]
        width_stack = np.stack(
            [data[f"{name}_central"] for data in width_data.values()]
        )
        width_minimum = np.min(width_stack, axis=0)
        width_maximum = np.max(width_stack, axis=0)
        wave_minimum = wave[f"{name}_minimum"]
        wave_maximum = wave[f"{name}_maximum"]
        payload[f"{name}_central"] = central
        payload[f"{name}_pdf_std"] = pdf_std
        payload[f"{name}_pdf_p16"] = baseline[f"{name}_p16"]
        payload[f"{name}_pdf_p84"] = baseline[f"{name}_p84"]
        payload[f"{name}_width_minimum"] = width_minimum
        payload[f"{name}_width_maximum"] = width_maximum
        payload[f"{name}_wave_minimum"] = wave_minimum
        payload[f"{name}_wave_maximum"] = wave_maximum
        value = float(central[origin, origin])
        pdf = float(pdf_std[origin, origin])
        width_low = float(width_minimum[origin, origin])
        width_high = float(width_maximum[origin, origin])
        wave_low = float(wave_minimum[origin, origin])
        wave_high = float(wave_maximum[origin, origin])
        rows.append(
            {
                "quantity": name,
                "k_x_GeV": float(axis[origin]),
                "k_y_GeV": float(axis[origin]),
                "central_width025": value,
                "pdf_sigma": pdf,
                "pdf_relative_sigma": pdf / abs(value),
                "width_minimum": width_low,
                "width_maximum": width_high,
                "width_max_relative_excursion": max(
                    abs(width_low - value), abs(width_high - value)
                )
                / abs(value),
                "wave_minimum": wave_low,
                "wave_maximum": wave_high,
                "wave_full_relative_spread": (wave_high - wave_low) / abs(value),
                "components_combined": 0,
            }
        )
    np.savez_compressed(ROOT / "gluon_helicity_uncertainty_components.npz", **payload)
    with (ROOT / "gluon_helicity_uncertainty_components.csv").open(
        "w", newline=""
    ) as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
