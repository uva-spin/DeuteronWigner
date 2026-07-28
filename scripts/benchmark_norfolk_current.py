#!/usr/bin/env python3
"""Benchmark matched Norfolk N3LO magnetic operators against Table III."""

import csv
from pathlib import Path

from deuteron_wigner.two_body_current import norfolk_n3lo_magnetic_moment
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate


PUBLISHED = {
    "nvia": (0.0002, 0.0093, 0.0042),
    "nvib": (0.0005, 0.0211, -0.0065),
    "nviia": (0.0002, 0.0110, 0.0026),
    "nviib": (0.0009, 0.0396, -0.0260),
}


def main() -> None:
    destination = Path("outputs/stage0/norfolk_n3lo_magnetic_moment.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for model, reference in PUBLISHED.items():
        wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{model}")
        result = norfolk_n3lo_magnetic_moment(wave, model=model)
        differentiated = norfolk_n3lo_magnetic_moment(
            wave,
            model=model,
            ope_regulator_ordering="differentiate_regulated_yukawa",
        )
        row = {"model": model}
        for label, published in zip(
            ("minimal_contact", "nonminimal_contact", "ope"), reference
        ):
            row[label] = result[label]
            row[f"{label}_published"] = published
            row[f"{label}_relative_error"] = (result[label] - published) / published
            row[f"{label}_validated"] = (
                abs(row[f"{label}_relative_error"]) < 0.02
                if label == "nonminimal_contact"
                else abs(result[label] - published) < 4.0e-5
                if label == "minimal_contact"
                else False
            )
        row["total"] = result["total"]
        row["ope_differentiate_regulated_yukawa"] = differentiated["ope"]
        rows.append(row)
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
