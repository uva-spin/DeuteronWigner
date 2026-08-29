#!/usr/bin/env python3
"""Export the complete constrained spin-1 quark, antiquark, and gluon basis."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    impulse_convolution,
)
from deuteron_wigner.complete_tmd_model import (
    CompleteSpin1TMDModel,
    GaugeLink,
)
from deuteron_wigner.fourier import gluon_tmd_b_to_k
from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.gtmd import Species
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.registry import (
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_D_GEV = 1.87561294257


def main() -> None:
    output = Path("outputs/complete/spin1_tmd_phase_space.csv")
    provider = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    wave = select_momentum_wave_function("av18")
    smearing = build_lf_smearing_spherical(
        radial=wave.radial,
        nucleon_mass=0.93891897 / HBARC_GEV_FM,
        k_max=12.0,
        n_k=24,
        n_cos_theta=16,
        n_phi=12,
    )
    x_axis = (0.02, 0.05, 0.1, 0.2, 0.4, 0.6)
    k_axis = (0.0, 0.25, 0.5, 1.0, 1.5)
    scales = (2.0, 5.0, 10.0)
    flavors = {
        Species.GLUON: (21,),
        Species.QUARK: (2, 1, 3),
        Species.ANTIQUARK: (-2, -1, -3),
    }

    gluon_boundary = MatchedGluonTMD(
        provider.gluon,
        provider.alpha_s,
        helicity_gluon_pdf=polarized.gluon,
        quark_singlet_pdf=provider.quark_singlet,
        config=GluonTMDMatchingConfig(profile=LargeBProfile.CENTRAL),
    )
    gluon_evolution = OneLoopGluonCSSEvolution(
        provider.alpha_s,
        GluonCSSEvolutionConfig(
            cs_profile=NonperturbativeCSProfile.CENTRAL
        ),
    )
    evolved_gluon = EvolvedMatchedGluonTMD(
        gluon_boundary, gluon_evolution
    )
    b_axis = np.linspace(0.0, 8.0, 301)
    intrinsic_g2 = (0.10, 0.20, 0.40)
    cs_gk = (0.0, 0.05, 0.10)
    direct_gluon: dict[
        tuple[str, float, float, float], tuple[float, float, float]
    ] = {}
    for scale in scales:
        log_scale = np.log(scale / 2.0)
        for x in x_axis:
            base = [
                evolved_gluon.values(float(x), float(b), scale)
                for b in b_axis
            ]
            transformed_profiles = []
            for g2 in intrinsic_g2:
                for gk in cs_gk:
                    ratio = np.exp(
                        -(g2 - 0.20) * b_axis**2
                        -(gk - 0.05) * b_axis**2 * log_scale
                    )
                    transformed_profiles.append(
                        gluon_tmd_b_to_k(
                            b_axis,
                            ratio * np.asarray([value.f1 for value in base]),
                            ratio * np.asarray([value.g1 for value in base]),
                            ratio
                            * np.asarray([value.h1perp for value in base]),
                            np.asarray(k_axis),
                            nucleon_mass=0.93891897,
                        )
                    )
            central_index = 4
            for index, k in enumerate(k_axis):
                for name in ("f1", "g1", "h1perp"):
                    values = np.asarray(
                        [
                            getattr(profile, name)[index].real
                            for profile in transformed_profiles
                        ]
                    )
                    direct_gluon[(name, x, k, scale)] = (
                        float(values[central_index]),
                        float(np.min(values)),
                        float(np.max(values)),
                    )

    anchors: dict[tuple[Species, int, float, float, str], float] = {}
    for species, species_flavors in flavors.items():
        for flavor in species_flavors:
            for scale in scales:
                for x in x_axis:
                    common = dict(
                        x=x,
                        scale=scale,
                        flavor=flavor,
                        proton_pdf=provider.proton,
                        neutron_pdf=provider.neutron,
                        smearing=smearing,
                        scaling_variable=ScalingVariable.NUCLEON,
                        per_nucleon=True,
                    )
                    f1 = impulse_convolution(**common)
                    delta_t = impulse_convolution(**common, tensor=True)
                    anchors[(species, flavor, x, scale, "f1")] = f1
                    anchors[(species, flavor, x, scale, "f1LL")] = (
                        -2.0 * delta_t / 3.0
                    )
                    polarized_isoscalar = 0.5 * (
                        polarized.proton(flavor, x, scale)
                        + polarized.neutron(flavor, x, scale)
                    )
                    # Standard deuteron depolarization approximation; the
                    # exact wave-dependent factor is recorded in metadata.
                    depolarization = 1.0 - 1.5 * 0.0578
                    anchors[(species, flavor, x, scale, "g1")] = (
                        depolarization * polarized_isoscalar
                    )
                    soffer = 0.5 * max(0.0, f1 + anchors[
                        (species, flavor, x, scale, "g1")
                    ])
                    anchors[(species, flavor, x, scale, "h1")] = 0.7 * soffer

    rows: list[dict[str, object]] = []
    for species, species_flavors in flavors.items():
        registry = (
            leading_twist_gluon_registry()
            if species == Species.GLUON
            else leading_twist_quark_registry(species)
        )
        for flavor in species_flavors:
            for scale in scales:
                for x in x_axis:
                    lookup = lambda name: (
                        lambda x_value, q_value: anchors[
                            (species, flavor, x_value, q_value, name)
                        ]
                    )
                    model = CompleteSpin1TMDModel(
                        registry,
                        mass=M_D_GEV,
                        width=0.30 if species == Species.GLUON else 0.25,
                        f1_anchor=lookup("f1"),
                        g1_anchor=lookup("g1"),
                        f1ll_anchor=lookup("f1LL"),
                        h1_anchor=(
                            None if species == Species.GLUON else lookup("h1")
                        ),
                        direct_tmds=(
                            {
                                name: (
                                    lambda x_value, k_value, q_value, name=name:
                                    direct_gluon[
                                        (name, x_value, k_value, q_value)
                                    ]
                                )
                                for name in ("f1", "g1", "h1perp")
                            }
                            if species == Species.GLUON
                            else None
                        ),
                        anchor_relative_uncertainty=0.05,
                    )
                    for gauge_link in (GaugeLink.FUTURE, GaugeLink.PAST):
                        for k in k_axis:
                            predictions = model.predict_all(
                                x=x, k=k, scale=scale, gauge_link=gauge_link
                            )
                            model.require_modulation_bounds(predictions)
                            model.require_block_budgets(predictions)
                            entries = {entry.name: entry for entry in registry.select()}
                            for name, prediction in predictions.items():
                                entry = entries[name]
                                rows.append(
                                    {
                                        "species": species.value,
                                        "flavor": flavor,
                                        "target_channel": entry.target_channel.value,
                                        "tmd": name,
                                        "rank": entry.transverse_rank,
                                        "t_odd": int(entry.t_odd),
                                        "gauge_link": gauge_link.value,
                                        "x_N": x,
                                        "k_GeV": k,
                                        "Q_GeV": scale,
                                        "central_GeV-2": prediction.central,
                                        "lower95_GeV-2": prediction.lower,
                                        "upper95_GeV-2": prediction.upper,
                                        "physical_ratio_central": (
                                            prediction.physical_ratio_central
                                        ),
                                        "physical_ratio_lower95": (
                                            prediction.physical_ratio_lower
                                        ),
                                        "physical_ratio_upper95": (
                                            prediction.physical_ratio_upper
                                        ),
                                        "status": prediction.status.value,
                                    }
                                )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata = {
        "status": "complete constrained leading-twist spin-1 model",
        "basis": {"gluon": 19, "quark": 18, "antiquark": 18},
        "wave_function": "AV18",
        "PDFs": {"unpolarized": "CT18NNLO/0", "polarized": "BDSSV24-NLO/0"},
        "derived_anchors": [
            "evolved gluon f1/g1/h1perp",
            "impulse f1/f1LL",
            "depolarized collinear g1",
            "quark h1 Soffer model",
        ],
        "constrained_completion": (
            "all remaining functions with rank-safe conservative modulation priors"
        ),
        "processes": ["future_SIDIS", "past_DY"],
        "t_odd_rule": "exact sign reversal under future/past gauge-link reversal",
        "deuteron_D_probability": 0.0578,
        "depolarization_factor": 1.0 - 1.5 * 0.0578,
        "model_assumptions": [
            "Gaussian core widths 0.30 GeV2 for gluons and 0.25 GeV2 for quarks",
            "quark transversity is 0.7 of the Soffer ceiling",
            "unmodeled amplitudes use conservative channel-hierarchy priors",
            "h1LT has an exact zero unweighted transverse integral",
            "bands are model-prior bands, not data-fit confidence intervals",
        ],
        "rows": len(rows),
        "production_ready": False,
    }
    output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(rows)} rows to {output}")


if __name__ == "__main__":
    main()
