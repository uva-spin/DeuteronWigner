#!/usr/bin/env python3
"""Export the initial CT18/BDSSV24 matched b-space gluon-TMD fixture."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/stage0/gluon_tmd_matched_bspace.csv"),
    )
    parser.add_argument("--scale", type=float, default=2.0)
    args = parser.parse_args()

    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    helicity = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    x_values = (0.01, 0.05, 0.1, 0.2, 0.4)
    b_values = np.linspace(0.0, 4.0, 17)
    profiles = (
        LargeBProfile.NARROW,
        LargeBProfile.CENTRAL,
        LargeBProfile.BROAD,
    )

    rows: list[dict[str, object]] = []
    metadata: dict[str, object] | None = None
    for profile in profiles:
        model = MatchedGluonTMD(
            unpolarized.gluon,
            unpolarized.alpha_s,
            helicity_gluon_pdf=helicity.gluon,
            quark_singlet_pdf=unpolarized.quark_singlet,
            config=GluonTMDMatchingConfig(profile=profile),
        )
        metadata = model.metadata
        for x in x_values:
            for b in b_values:
                values = model.values(x, float(b), args.scale)
                rows.append(
                    {
                        "profile": profile.value,
                        "x": x,
                        "b_GeV_inverse": b,
                        "b_star_GeV_inverse": values.b_star,
                        "Q_GeV": args.scale,
                        "profile_factor": values.profile_factor,
                        "f1g_b": values.f1,
                        "g1g_b": values.g1,
                        "h1perpg_b": values.h1perp,
                    }
                )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata_path = args.output.with_suffix(".metadata.json")
    metadata_path.write_text(
        json.dumps(
            {
                **(metadata or {}),
                "large_b_profile": "family",
                "profiles": [profile.value for profile in profiles],
                "profile_g2_GeV2": {
                    "narrow": GluonTMDMatchingConfig(
                        profile=LargeBProfile.NARROW
                    ).g2,
                    "central": GluonTMDMatchingConfig(
                        profile=LargeBProfile.CENTRAL
                    ).g2,
                    "broad": GluonTMDMatchingConfig(
                        profile=LargeBProfile.BROAD
                    ).g2,
                },
                "x_grid": list(x_values),
                "b_grid_GeV_inverse": list(map(float, b_values)),
                "scale_GeV": args.scale,
                "unpolarized_pdf": "CT18NNLO/0",
                "helicity_pdf": "BDSSV24-NLO/0",
            },
            indent=2,
        )
        + "\n"
    )
    print(f"Wrote {len(rows)} rows to {args.output}")
    print(f"Wrote metadata to {metadata_path}")


if __name__ == "__main__":
    main()
