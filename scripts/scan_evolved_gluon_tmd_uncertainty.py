#!/usr/bin/env python3
"""Convergence and separated uncertainty scan for evolved deuteron gluon TMDs."""

from __future__ import annotations

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
from deuteron_wigner.tmd_models import InterpolatedSpinHalfGluonGTMD
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
OBSERVABLES = ("f1g", "g1g", "h1perpg", "f1LLg", "h1LLperpg")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def project_point(model, quadrature, x_d: float, k_gev: float, scale: float):
    k_fm = k_gev / HBARC_GEV_FM
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
        correlator, (k_fm, 0.0), M_D_GEV / HBARC_GEV_FM
    )
    longitudinal = project_deuteron_gluon_l_t_lt(
        correlator, (k_fm, 0.0), M_D_GEV / HBARC_GEV_FM
    )["L"]
    per_nucleon_x_conversion = 0.25
    return {
        "f1g": per_nucleon_x_conversion * unpolarized.trace,
        "g1g": per_nucleon_x_conversion * longitudinal["g1"],
        "h1perpg": per_nucleon_x_conversion * unpolarized.linear,
        "f1LLg": per_nucleon_x_conversion * ll.trace,
        "h1LLperpg": per_nucleon_x_conversion * ll.linear,
    }


def main() -> None:
    root = Path("outputs/stage0/uncertainty")
    scale = 5.0
    x_n = 0.1
    x_d = x_n / 2.0
    provider = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
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
    central = EvolvedMatchedGluonTMD(boundary, evolution)

    x_axis = np.concatenate((np.geomspace(0.05, 0.9, 15), (1.0,)))
    b_axis = np.linspace(0.0, 8.0, 201)
    k_table = np.linspace(0.0, 3.5, 81)
    k_scan = np.asarray((0.1, 0.5, 1.0, 1.5))
    intrinsic_profiles = (
        LargeBProfile.NARROW,
        LargeBProfile.CENTRAL,
        LargeBProfile.BROAD,
    )
    cs_profiles = (
        NonperturbativeCSProfile.NONE,
        NonperturbativeCSProfile.CENTRAL,
        NonperturbativeCSProfile.HIGH,
    )
    intrinsic_g2 = {
        profile: GluonTMDMatchingConfig(profile=profile).g2
        for profile in intrinsic_profiles
    }
    cs_gk = {
        profile: GluonCSSEvolutionConfig(cs_profile=profile).gk
        for profile in cs_profiles
    }

    central_b_tables = []
    for x in x_axis:
        central_b_tables.append(
            [central.values(float(x), float(b), scale) for b in b_axis]
        )

    models: dict[
        tuple[LargeBProfile, NonperturbativeCSProfile],
        InterpolatedSpinHalfGluonGTMD,
    ] = {}
    log_scale = np.log(scale / evolution.config.reference_scale)
    for intrinsic in intrinsic_profiles:
        for cs_profile in cs_profiles:
            delta_exponent = (
                intrinsic_g2[intrinsic] - boundary.config.g2
            ) * b_axis**2 + (
                cs_gk[cs_profile] - evolution.config.gk
            ) * b_axis**2 * log_scale
            profile_ratio = np.exp(-delta_exponent)
            tables = {
                name: np.empty((len(x_axis), len(k_table)))
                for name in ("f1", "g1", "h1perp")
            }
            for index, values in enumerate(central_b_tables):
                transformed = gluon_tmd_b_to_k(
                    b_axis,
                    profile_ratio * np.asarray([value.f1 for value in values]),
                    profile_ratio * np.asarray([value.g1 for value in values]),
                    profile_ratio
                    * np.asarray([value.h1perp for value in values]),
                    k_table,
                    nucleon_mass=M_N_GEV,
                )
                tables["f1"][index] = transformed.f1.real
                tables["g1"][index] = transformed.g1.real
                tables["h1perp"][index] = transformed.h1perp.real
            models[(intrinsic, cs_profile)] = InterpolatedSpinHalfGluonGTMD(
                x_axis,
                k_table,
                tables["f1"],
                tables["g1"],
                tables["h1perp"],
                nucleon_mass_GeV=M_N_GEV,
                momentum_unit_to_GeV=HBARC_GEV_FM,
            )

    quadratures = {}
    for wave_name in WAVE_FUNCTION_CHOICES:
        wave = select_momentum_wave_function(wave_name)
        quadratures[wave_name] = build_off_forward_spin_quadrature(
            radial=wave.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=8.0,
            delta_x=0.0,
            delta_y=0.0,
            n_k=12,
            n_cos_theta=8,
            n_phi=8,
        )

    sample_rows: list[dict[str, object]] = []
    for wave_name in WAVE_FUNCTION_CHOICES:
        for intrinsic in intrinsic_profiles:
            for cs_profile in cs_profiles:
                model = models[(intrinsic, cs_profile)]
                for k_gev in k_scan:
                    values = project_point(
                        model, quadratures[wave_name], x_d, float(k_gev), scale
                    )
                    row: dict[str, object] = {
                        "wave_function": wave_name,
                        "intrinsic_profile": intrinsic.value,
                        "CS_profile": cs_profile.value,
                        "x_N": x_n,
                        "Q_GeV": scale,
                        "k_GeV": k_gev,
                        **values,
                    }
                    row["linear_polarization_ratio"] = (
                        k_gev**2
                        * values["h1perpg"]
                        / (2.0 * M_D_GEV**2 * values["f1g"])
                    )
                    row["helicity_ratio"] = values["g1g"] / values["f1g"]
                    sample_rows.append(row)
    write_csv(root / "gluon_tmd_evolved_samples.csv", sample_rows)

    band_rows: list[dict[str, object]] = []
    for k_gev in k_scan:
        at_k = [
            row for row in sample_rows if np.isclose(row["k_GeV"], k_gev)
        ]
        central_profiles = [
            row
            for row in at_k
            if row["intrinsic_profile"] == "central"
            and row["CS_profile"] == "central"
        ]
        av18_profiles = [
            row for row in at_k if row["wave_function"] == "av18"
        ]
        row: dict[str, object] = {"k_GeV": k_gev}
        for observable in (*OBSERVABLES, "linear_polarization_ratio", "helicity_ratio"):
            total = np.asarray([item[observable] for item in at_k])
            wave = np.asarray([item[observable] for item in central_profiles])
            profile = np.asarray([item[observable] for item in av18_profiles])
            for label, values in (
                ("total", total),
                ("wave_central_profiles", wave),
                ("profiles_av18", profile),
            ):
                row[f"{observable}_{label}_min"] = float(np.min(values))
                row[f"{observable}_{label}_max"] = float(np.max(values))
                row[f"{observable}_{label}_half_range"] = float(
                    0.5 * (np.max(values) - np.min(values))
                )
        band_rows.append(row)
    write_csv(root / "gluon_tmd_evolved_bands.csv", band_rows)

    av18 = select_momentum_wave_function("av18")
    convergence_specs = (
        ("coarse", 12, 8, 8),
        ("medium", 16, 12, 8),
        ("fine", 24, 16, 12),
    )
    convergence_k = k_scan
    convergence_values = {}
    central_model = models[
        (LargeBProfile.CENTRAL, NonperturbativeCSProfile.CENTRAL)
    ]
    for label, n_k, n_cos, n_phi in convergence_specs:
        quadrature = build_off_forward_spin_quadrature(
            radial=av18.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=8.0,
            delta_x=0.0,
            delta_y=0.0,
            n_k=n_k,
            n_cos_theta=n_cos,
            n_phi=n_phi,
        )
        convergence_values[label] = [
            project_point(central_model, quadrature, x_d, float(k), scale)
            for k in convergence_k
        ]
    convergence_rows = []
    fine = convergence_values["fine"]
    for label, n_k, n_cos, n_phi in convergence_specs:
        for index, k_gev in enumerate(convergence_k):
            row = {
                "case": label,
                "n_k": n_k,
                "n_cos": n_cos,
                "n_phi": n_phi,
                "k_GeV": k_gev,
            }
            for observable in OBSERVABLES:
                value = convergence_values[label][index][observable]
                reference = fine[index][observable]
                row[observable] = value
                row[f"{observable}_relative_to_fine"] = (
                    (value - reference) / reference
                    if reference != 0.0
                    else np.nan
                )
            convergence_rows.append(row)
    write_csv(root / "gluon_tmd_evolved_convergence.csv", convergence_rows)

    metadata = {
        "status": "diagnostic uncertainty and convergence scan",
        "x_N": x_n,
        "Q_GeV": scale,
        "wave_functions": list(WAVE_FUNCTION_CHOICES),
        "intrinsic_profiles_g2_GeV2": {
            key.value: value for key, value in intrinsic_g2.items()
        },
        "CS_profiles_gk_GeV2": {
            key.value: value for key, value in cs_gk.items()
        },
        "sample_rows": len(sample_rows),
        "nuclear_k_max_fm_inverse": 8.0,
        "sample_nuclear_quadrature": {"n_k": 12, "n_cos": 8, "n_phi": 8},
        "convergence_reference": {"n_k": 24, "n_cos": 16, "n_phi": 12},
        "production_ready": False,
    }
    (root / "gluon_tmd_evolved_scan.metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(sample_rows)} samples and {len(band_rows)} band rows")


if __name__ == "__main__":
    main()
