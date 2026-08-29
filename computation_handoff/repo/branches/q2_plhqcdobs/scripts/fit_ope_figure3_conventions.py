#!/usr/bin/env python3
"""Test simple operator conventions against digitized Schiavilla Fig. 3."""

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from deuteron_wigner.two_body_current import regulated_ope_radial_functions
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate


def main() -> None:
    source = Path("outputs/stage0/norfolk_ope_figure3_digitized.csv")
    rows = list(csv.DictReader(source.open(encoding="utf-8")))
    pion_mass_fm = 138.039 / 197.3269804
    prepared = {}
    for model in ("nvia", "nvib"):
        wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{model}")
        for term in ("i1", "i2"):
            selected = [row for row in rows if row["curve"] == f"{model}_{term}"]
            radius = np.asarray([float(row["radius_fm"]) for row in selected])
            density = np.asarray([float(row["density_fm^-1"]) for row in selected])
            keep = (radius > 0.25) & (radius < 4.7)
            radius, density = radius[keep], density[keep]
            u = np.interp(radius, wave.grid, wave.u)
            w = np.interp(radius, wave.grid, wave.w)
            shapes = regulated_ope_radial_functions(
                radius,
                pion_mass_fm=pion_mass_fm,
                r_long_fm=1.2 if model == "nvia" else 1.0,
            )
            prepared[model, term] = (density, u, w, shapes[term == "i2"])

    def evaluate(tensor_multiplier: float) -> tuple[float, dict[str, float]]:
        squared_error = 0.0
        count = 0
        scales = {}
        for model in ("nvia", "nvib"):
            predictions, observations = [], []
            for term, coefficients in (
                ("i1", np.asarray([2.0, 0.0, -1.0])),
                (
                    "i2",
                    tensor_multiplier
                    * np.asarray([2.0 / 3.0, 2.0 * np.sqrt(2.0) / 3.0, 1.0 / 3.0]),
                ),
            ):
                density, u, w, shape = prepared[model, term]
                radial = np.column_stack((u * u, u * w, w * w)) @ coefficients
                predictions.extend(shape * radial)
                observations.extend(density)
            prediction = np.asarray(predictions)
            observation = np.asarray(observations)
            scale = float(np.dot(prediction, observation) / np.dot(prediction, prediction))
            scales[model] = scale
            squared_error += np.sum((scale * prediction - observation) ** 2)
            count += len(observation)
        return float(np.sqrt(squared_error / count)), scales

    optimum = minimize_scalar(
        lambda multiplier: evaluate(multiplier)[0],
        bounds=(0.1, 1.5),
        method="bounded",
    )
    rms, scales = evaluate(float(optimum.x))
    result = {
        "best_tensor_multiplier": float(optimum.x),
        "density_rms_fm^-1": rms,
        "model_scales": scales,
        "interpretation": (
            "No simple tensor rescaling is accepted: the RMS is much larger "
            "than the raster digitization uncertainty."
        ),
    }
    destination = Path("outputs/stage0/norfolk_ope_figure3_convention_fit.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
