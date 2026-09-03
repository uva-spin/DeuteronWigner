#!/usr/bin/env python3
"""Export evolved b-space and transformed k-space gluon-TMD fixtures."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.fourier import gluon_tmd_b_to_k
from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=0.1)
    parser.add_argument(
        "--b-output",
        type=Path,
        default=Path("outputs/stage0/gluon_tmd_evolved_bspace.csv"),
    )
    parser.add_argument(
        "--k-output",
        type=Path,
        default=Path("outputs/stage0/gluon_tmd_evolved_kspace.csv"),
    )
    args = parser.parse_args()

    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    helicity = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    boundary = MatchedGluonTMD(
        unpolarized.gluon,
        unpolarized.alpha_s,
        helicity_gluon_pdf=helicity.gluon,
        quark_singlet_pdf=unpolarized.quark_singlet,
        config=GluonTMDMatchingConfig(profile=LargeBProfile.CENTRAL),
    )
    b_axis = np.linspace(0.0, 8.0, 401)
    k_axis = np.linspace(0.0, 3.0, 61)
    scales = (2.0, 5.0, 10.0)
    profiles = (
        NonperturbativeCSProfile.NONE,
        NonperturbativeCSProfile.CENTRAL,
        NonperturbativeCSProfile.HIGH,
    )
    b_rows: list[dict[str, object]] = []
    k_rows: list[dict[str, object]] = []

    last_metadata: dict[str, object] | None = None
    for profile in profiles:
        evolution = OneLoopGluonCSSEvolution(
            unpolarized.alpha_s,
            GluonCSSEvolutionConfig(cs_profile=profile),
        )
        model = EvolvedMatchedGluonTMD(boundary, evolution)
        last_metadata = model.metadata
        for scale in scales:
            values = [model.values(args.x, float(b), scale) for b in b_axis]
            f1_b = np.asarray([value.f1 for value in values])
            g1_b = np.asarray([value.g1 for value in values])
            h1_b = np.asarray([value.h1perp for value in values])
            for value in values:
                b_rows.append(
                    {
                        "CS_profile": profile.value,
                        "x": args.x,
                        "Q_GeV": scale,
                        "b_GeV_inverse": value.b,
                        "b_star_GeV_inverse": value.b_star,
                        "mu_initial_GeV": value.initial_scale,
                        "intrinsic_factor": value.intrinsic_factor,
                        "evolution_factor": value.evolution_factor,
                        "f1g_b": value.f1,
                        "g1g_b": value.g1,
                        "h1perpg_b": value.h1perp,
                    }
                )
            transformed = gluon_tmd_b_to_k(
                b_axis,
                f1_b,
                g1_b,
                h1_b,
                k_axis,
                nucleon_mass=0.9389,
            )
            for index, k in enumerate(k_axis):
                k_rows.append(
                    {
                        "CS_profile": profile.value,
                        "x": args.x,
                        "Q_GeV": scale,
                        "k_GeV": k,
                        "f1g_k_GeV-2": transformed.f1[index].real,
                        "g1g_k_GeV-2": transformed.g1[index].real,
                        "h1perpg_project_GeV-2": (
                            transformed.h1perp[index].real
                        ),
                    }
                )

    write_rows(args.b_output, b_rows)
    write_rows(args.k_output, k_rows)
    metadata_path = args.k_output.with_suffix(".metadata.json")
    metadata_path.write_text(
        json.dumps(
            {
                **(last_metadata or {}),
                "evolution": {
                    **((last_metadata or {}).get("evolution", {})),
                    "nonperturbative_CS_profile": "family",
                    "gk_GeV2": {
                        profile.value: GluonCSSEvolutionConfig(
                            cs_profile=profile
                        ).gk
                        for profile in profiles
                    },
                },
                "CS_profiles": [profile.value for profile in profiles],
                "scales_GeV": list(scales),
                "x": args.x,
                "b_grid": {
                    "minimum_GeV_inverse": float(b_axis[0]),
                    "maximum_GeV_inverse": float(b_axis[-1]),
                    "points": len(b_axis),
                },
                "k_grid": {
                    "minimum_GeV": float(k_axis[0]),
                    "maximum_GeV": float(k_axis[-1]),
                    "points": len(k_axis),
                },
                "rank2_adapter": "arXiv:1907.03780 Eqs. (2.6)-(2.8)",
            },
            indent=2,
        )
        + "\n"
    )
    print(f"Wrote {len(b_rows)} rows to {args.b_output}")
    print(f"Wrote {len(k_rows)} rows to {args.k_output}")
    print(f"Wrote metadata to {metadata_path}")


if __name__ == "__main__":
    main()
