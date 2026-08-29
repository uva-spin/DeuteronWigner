#!/usr/bin/env python3
"""Build transparent AV18/CD-Bonn/Norfolk wave-function model bands."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

MODELS = ("av18", "cd_bonn", "nvia", "nvib", "nviia", "nviib")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def build_band(
    *,
    input_pattern: str,
    key: str,
    observables: tuple[str, ...],
    destination: Path,
) -> None:
    indexed = {}
    for model in MODELS:
        for row in read_rows(Path(input_pattern.format(model=model))):
            numeric_key = round(float(row[key]), 10)
            indexed.setdefault(numeric_key, {})[model] = row
    output = []
    for numeric_key, model_rows in sorted(indexed.items()):
        if len(model_rows) != len(MODELS):
            continue
        row = {key: numeric_key, "model_count": len(model_rows)}
        for observable in observables:
            values = {
                model: float(model_rows[model][observable]) for model in MODELS
            }
            minimum_model = min(values, key=values.get)
            maximum_model = max(values, key=values.get)
            array = np.asarray(tuple(values.values()))
            mean = float(array.mean())
            row.update(
                {
                    f"{observable}_mean": mean,
                    f"{observable}_min": float(array.min()),
                    f"{observable}_max": float(array.max()),
                    f"{observable}_half_range": float(
                        0.5 * (array.max() - array.min())
                    ),
                    f"{observable}_relative_half_range": float(
                        0.5 * (array.max() - array.min()) / abs(mean)
                    )
                    if mean != 0.0
                    else np.nan,
                    f"{observable}_min_model": minimum_model,
                    f"{observable}_max_model": maximum_model,
                }
            )
        output.append(row)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(output[0]))
        writer.writeheader()
        writer.writerows(output)


def main() -> None:
    build_band(
        input_pattern="outputs/stage1/b1_{model}_ct18nnlo.csv",
        key="x_table",
        observables=("b1_IA",),
        destination=Path("outputs/uncertainty/b1_wave_function_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage2/sidis_tensor_{model}.csv",
        key="P_hT_GeV",
        observables=("W_U", "W_deltaT", "deltaT_over_U"),
        destination=Path("outputs/uncertainty/sidis_wave_function_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage2/tmd_k_{model}.csv",
        key="kT_GeV",
        observables=("F_U", "F_deltaT"),
        destination=Path("outputs/uncertainty/tmd_wave_function_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/body_form_factor_{model}.csv",
        key="DeltaT_GeV",
        observables=("normalized_body_form_factor",),
        destination=Path("outputs/uncertainty/body_gtmd_marginal_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/body_impact_density_{model}.csv",
        key="bT_fm",
        observables=("rho_body_fm^-2",),
        destination=Path("outputs/uncertainty/body_impact_density_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/fixed_k_wigner_{model}.csv",
        key="kT_GeV",
        observables=(
            "gtmd_forward_U",
            "gtmd_forward_deltaT",
            "wigner_b0_U",
            "wigner_b0_deltaT",
        ),
        destination=Path("outputs/uncertainty/fixed_k_wigner_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/parent_x_scan_{model}.csv",
        key="x_N",
        observables=(
            "charge_weighted_pdf_U_parent",
            "charge_weighted_deltaT_pdf_parent",
            "b1_from_parent",
        ),
        destination=Path("outputs/uncertainty/parent_x_scan_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/component_wigner_{model}.csv",
        key="kT_GeV",
        observables=(
            "wigner_b0_U_SS",
            "wigner_b0_deltaT_SS",
            "wigner_b0_U_SD_plus_DS",
            "wigner_b0_deltaT_SD_plus_DS",
            "wigner_b0_U_DD",
            "wigner_b0_deltaT_DD",
        ),
        destination=Path("outputs/uncertainty/component_wigner_band.csv"),
    )
    build_band(
        input_pattern="outputs/stage0/lps_covariant_form_factors_{model}.csv",
        key="DeltaT_GeV",
        observables=("GC", "GM", "GQ", "A", "B", "t20_70deg"),
        destination=Path("outputs/uncertainty/lps_one_body_wave_function_band.csv"),
    )


if __name__ == "__main__":
    main()
