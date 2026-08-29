#!/usr/bin/env python3
"""Compare evolved and historical Gaussian nucleon inputs in AV18 IA."""

from __future__ import annotations

import csv
import json
from functools import lru_cache
from pathlib import Path

import numpy as np

from deuteron_wigner.fourier import gluon_tmd_b_to_k
from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    project_deuteron_gluon_l_t_lt,
    project_deuteron_gluon_u_ll,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)
from deuteron_wigner.tmd_models import (
    GaussianSpinHalfGluonGTMD,
    InterpolatedSpinHalfGluonGTMD,
)
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


def main() -> None:
    output = Path("outputs/stage0/gluon_tmd_evolved_vs_gaussian_av18.csv")
    provider = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    scale = 5.0
    x_n = 0.1
    x_d = x_n / 2.0

    boundary = MatchedGluonTMD(
        provider.gluon,
        provider.alpha_s,
        helicity_gluon_pdf=polarized.gluon,
        quark_singlet_pdf=provider.quark_singlet,
        config=GluonTMDMatchingConfig(profile=LargeBProfile.CENTRAL),
    )
    evolution = OneLoopGluonCSSEvolution(
        provider.alpha_s,
        GluonCSSEvolutionConfig(
            cs_profile=NonperturbativeCSProfile.CENTRAL
        ),
    )
    evolved_boundary = EvolvedMatchedGluonTMD(boundary, evolution)

    x_axis = np.concatenate((np.geomspace(0.05, 0.9, 15), (1.0,)))
    b_axis = np.linspace(0.0, 8.0, 201)
    k_axis = np.linspace(0.0, 3.5, 81)
    tables = {
        name: np.empty((len(x_axis), len(k_axis)))
        for name in ("f1", "g1", "h1perp")
    }
    for index, x in enumerate(x_axis):
        b_values = [
            evolved_boundary.values(float(x), float(b), scale) for b in b_axis
        ]
        transformed = gluon_tmd_b_to_k(
            b_axis,
            np.asarray([value.f1 for value in b_values]),
            np.asarray([value.g1 for value in b_values]),
            np.asarray([value.h1perp for value in b_values]),
            k_axis,
            nucleon_mass=M_N_GEV,
        )
        tables["f1"][index] = transformed.f1.real
        tables["g1"][index] = transformed.g1.real
        tables["h1perp"][index] = transformed.h1perp.real

    evolved_model = InterpolatedSpinHalfGluonGTMD(
        x_axis,
        k_axis,
        tables["f1"],
        tables["g1"],
        tables["h1perp"],
        nucleon_mass_GeV=M_N_GEV,
        momentum_unit_to_GeV=HBARC_GEV_FM,
    )

    @lru_cache(maxsize=None)
    def gluon_pdf(x: float, q: float) -> float:
        return provider.gluon(x, q)

    @lru_cache(maxsize=None)
    def helicity_pdf(x: float, q: float) -> float:
        return polarized.gluon(x, q)

    gaussian_model = GaussianSpinHalfGluonGTMD(
        gluon_pdf,
        width=0.25 / HBARC_GEV_FM**2,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        helicity_pdf=helicity_pdf,
        linear_fraction=0.5,
    )

    wave = select_momentum_wave_function("av18")
    quadrature = build_off_forward_spin_quadrature(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=8.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=8,
        n_cos_theta=6,
        n_phi=6,
    )
    k_external = np.linspace(0.05, 1.5, 20)
    rows: list[dict[str, object]] = []
    for k_gev in k_external:
        projections: dict[str, dict[str, float]] = {}
        for label, model, density_conversion in (
            ("evolved", evolved_model, 0.25),
            ("gaussian", gaussian_model, 0.25 / HBARC_GEV_FM**2),
        ):
            k_fm = float(k_gev / HBARC_GEV_FM)
            correlator = convolve_gluon_gtmd_point(
                x=x_d,
                k_x=k_fm,
                k_y=0.0,
                scale=scale,
                proton_gtmd=model,
                neutron_gtmd=model,
                quadrature=quadrature,
            )
            unpolarized, ll = project_deuteron_gluon_u_ll(
                correlator,
                (k_fm, 0.0),
                M_D_GEV / HBARC_GEV_FM,
            )
            longitudinal = project_deuteron_gluon_l_t_lt(
                correlator,
                (k_fm, 0.0),
                M_D_GEV / HBARC_GEV_FM,
            )["L"]
            projections[label] = {
                "f1g": density_conversion * unpolarized.trace,
                "h1perpg": density_conversion * unpolarized.linear,
                "f1LLg": density_conversion * ll.trace,
                "h1LLperpg": density_conversion * ll.linear,
                "g1g": density_conversion * longitudinal["g1"],
            }
        row: dict[str, object] = {"k_GeV": k_gev}
        for name in ("f1g", "g1g", "h1perpg", "f1LLg", "h1LLperpg"):
            evolved = projections["evolved"][name]
            gaussian = projections["gaussian"][name]
            row[f"{name}_evolved_GeV-2"] = evolved
            row[f"{name}_gaussian_GeV-2"] = gaussian
            row[f"{name}_evolved_over_gaussian"] = (
                evolved / gaussian if gaussian != 0.0 else np.nan
            )
        for label in ("evolved", "gaussian"):
            f1 = projections[label]["f1g"]
            h1perp = projections[label]["h1perpg"]
            row[f"linear_polarization_ratio_{label}"] = (
                k_gev**2 * h1perp / (2.0 * M_D_GEV**2 * f1)
                if f1 != 0.0
                else np.nan
            )
            row[f"helicity_ratio_{label}"] = (
                projections[label]["g1g"] / f1 if f1 != 0.0 else np.nan
            )
        rows.append(row)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata = {
        "wave_function": "AV18",
        "x_N": x_n,
        "x_D": x_d,
        "Q_GeV": scale,
        "evolved_model": evolved_boundary.metadata,
        "gaussian_model": {
            "width_GeV2": 0.25,
            "linear_fraction": 0.5,
            "status": "historical diagnostic only",
        },
        "interpolation": {
            "x_min": float(x_axis[0]),
            "x_max": float(x_axis[-1]),
            "x_points": len(x_axis),
            "k_max_GeV": float(k_axis[-1]),
            "k_points": len(k_axis),
            "strict_no_extrapolation": True,
        },
        "nuclear_quadrature": {
            "internal_k_max_fm_inverse": 8.0,
            "n_k": 8,
            "n_cos": 6,
            "n_phi": 6,
        },
    }
    output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(rows)} comparison points to {output}")


if __name__ == "__main__":
    main()
