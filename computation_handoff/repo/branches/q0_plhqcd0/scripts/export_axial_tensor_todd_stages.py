#!/usr/bin/env python3
"""Export positivity-bounded and explicit-rescattering quark g1LT/g1TT."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from scipy.integrate import simpson

from deuteron_wigner.axial_tensor_todd import (
    EikonalAxialTensorModel,
    EikonalKernelParameters,
    add_axial_tensor_todd,
    axial_tensor_todd_scenarios,
)
from deuteron_wigner.correlator_io import quark_correlator_rows
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    compose_spin1_quark_correlator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.wavefunctions.av18 import load_av18_momentum

INPUT = Path("outputs/parent_tmds/quark_av18_rich_medium.csv")
OUTPUT = Path("outputs/parent_tmds/quark_axial_tensor_todd_stages.csv")
CORRELATORS = OUTPUT.with_name(f"{OUTPUT.stem}.correlators.csv")
M_D_GEV = 1.87561294257
FLAVOR_IDS = {"u": 2, "d": 1, "ubar": -2, "dbar": -1}
LINKS = {
    "[+,+]": GaugeLink("+", "+"),
    "[-,-]": GaugeLink("-", "-"),
}
EIKONAL_SCENARIOS = (
    EikonalKernelParameters(
        label="screened_soft", alpha_s=0.28,
        screening_mass_gev=0.38, dipole_scale_gev=1.00,
    ),
    EikonalKernelParameters(label="screened_central"),
    EikonalKernelParameters(
        label="screened_strong", alpha_s=0.42,
        screening_mass_gev=0.25, dipole_scale_gev=1.25,
    ),
)


def _interpolators(frame: pd.DataFrame) -> dict[str, PchipInterpolator]:
    result = {}
    for tmd in SPIN1_QUARK_TMD_NAMES:
        selected = frame.loc[frame.tmd.eq(tmd)].sort_values("k_GeV")
        result[tmd] = PchipInterpolator(
            selected.k_GeV.to_numpy(),
            selected["F_GeV-2"].to_numpy(),
            extrapolate=False,
        )
    return result


def _f1_width(interpolator: PchipInterpolator) -> float:
    k = np.linspace(0.0, 0.75, 17)
    values = np.asarray(interpolator(k), dtype=float)
    positive = values > max(values[0] * 1.0e-8, 0.0)
    slope = np.polyfit(k[positive] ** 2, np.log(values[positive]), 1)[0]
    return float(np.clip(-1.0 / slope, 0.15, 0.80))


def main() -> None:
    source = pd.read_csv(INPUT)
    source = source.loc[source.mechanism.eq("model_total")]
    azimuth = float(source.azimuth_rad.iloc[0])
    # Positive-rank coefficients are not identifiable at the exact origin;
    # start at a resolved nonzero knot instead of inserting an artificial
    # plotted zero between their finite radial limits.
    k_axis = np.linspace(0.015625, 0.9375, 60)
    av18 = load_av18_momentum("data/raw/av18/deut.wfk")
    s_probability, d_probability = av18.component_norms()
    sd_coherence = float(
        simpson(av18.grid**2 * av18.u * av18.w, x=av18.grid)
        / np.sqrt(s_probability * d_probability)
    )
    rows: list[dict[str, object]] = []
    correlator_rows: list[dict[str, object]] = []

    for flavor_label, flavor in FLAVOR_IDS.items():
        future_frame = source.loc[
            source.flavor_label.eq(flavor_label)
            & source.gauge_link.eq("[+,+]")
        ]
        future_interpolators = _interpolators(future_frame)
        width = _f1_width(future_interpolators["f1"])
        for link_label, link in LINKS.items():
            selected = source.loc[
                source.flavor_label.eq(flavor_label)
                & source.gauge_link.eq(link_label)
            ]
            interpolators = _interpolators(selected)
            for k in k_axis:
                kx = float(k * np.cos(azimuth))
                ky = float(k * np.sin(azimuth))
                values = {
                    name: float(interpolators[name](k))
                    for name in SPIN1_QUARK_TMD_NAMES
                }
                base = compose_spin1_quark_correlator(
                    (kx, ky), M_D_GEV, values
                )
                f1 = float(future_interpolators["f1"](k))

                stage_members = []
                for scenario in axial_tensor_todd_scenarios():
                    raw = scenario.future_values(
                        flavor, f1_gev2=f1, k_gev=float(k)
                    )
                    stage_members.append((
                        "positivity_bounded_phase",
                        scenario.label,
                        raw,
                        (
                            "independent flavor/operator axial gauge-link "
                            "phase constrained by the full 6x6 density"
                        ),
                        "model_coefficient_scenario",
                    ))
                for kernel in EIKONAL_SCENARIOS:
                    model = EikonalAxialTensorModel(
                        kernel=kernel,
                        d_state_probability=d_probability,
                        sd_radial_coherence=sd_coherence,
                    )
                    raw = model.future_values(
                        flavor,
                        f1_gev2=f1,
                        k_gev=float(k),
                        width_gev2=width,
                    )
                    stage_members.append((
                        "screened_one_gluon_rescattering",
                        kernel.label,
                        raw,
                        (
                            "screened one-gluon transverse convolution with "
                            "AV18 S-D and explicit S-P/S-D/P-P interference"
                        ),
                        "alpha_s_screening_dipole_scenario",
                    ))

                for stage, scenario, raw, provenance, uncertainty in stage_members:
                    corrected, cap, final_lt, final_tt = add_axial_tensor_todd(
                        base,
                        momentum=(kx, ky),
                        g1lt_future=raw[0],
                        g1tt_future=raw[1],
                        gauge_link=link,
                    )
                    projected = (
                        project_spin1_quark_correlator_at_origin(
                            corrected, M_D_GEV
                        )
                        if k == 0.0
                        else project_spin1_quark_correlator(
                            corrected, (kx, ky), M_D_GEV
                        )
                    )
                    common = {
                        "sector": "quark",
                        "species": (
                            "quark" if flavor > 0 else "antiquark"
                        ),
                        "flavor": flavor,
                        "flavor_label": flavor_label,
                        "wave_function": "av18",
                        "stage": stage,
                        "scenario": scenario,
                        "mechanism": "axial_tensor_gauge_link_rescattering",
                        "gauge_link": link_label,
                        "x_N": 0.1,
                        "Q_GeV": 5.0,
                        "k_GeV": float(k),
                        "azimuth_rad": azimuth,
                        "d_state_probability": d_probability,
                        "sd_radial_coherence": sd_coherence,
                        "f1_width_GeV2": width,
                        "positivity_scale": cap,
                        "minimum_density_eigenvalue": (
                            corrected.minimum_positivity_eigenvalue()
                        ),
                        "evidence_class": "model_dependent",
                        "uncertainty_axis": uncertainty,
                        "source": provenance,
                        "validity": (
                            "x_N=0.1,Q=5 GeV,0<k_T<=0.9375 GeV; "
                            "future/past simple staples"
                        ),
                        "combine_policy": (
                            "alternative_stage_and_scenario_not_additive"
                        ),
                    }
                    correlator_rows.extend(
                        quark_correlator_rows(corrected, common)
                    )
                    raw_sign = 1.0 if link_label == "[+,+]" else -1.0
                    for tmd, value in projected.items():
                        rows.append({
                            **common,
                            "tmd": tmd,
                            "F_GeV-2": float(value),
                            "raw_g1LT_GeV-2": raw_sign * raw[0],
                            "raw_g1TT_GeV-2": raw_sign * raw[1],
                            "added_g1LT_GeV-2": final_lt,
                            "added_g1TT_GeV-2": final_tt,
                        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)
    pd.DataFrame(correlator_rows).to_csv(CORRELATORS, index=False)
    print(
        f"Wrote {len(rows)} projections and {len(correlator_rows)} "
        f"correlator entries; AV18 P_D={d_probability:.8f}, "
        f"S-D coherence={sd_coherence:.8f}"
    )


if __name__ == "__main__":
    main()
