#!/usr/bin/env python3
"""Export dense complete spin-1 TMD curves and separated model studies."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.complete_tmd_model import GaugeLink
from deuteron_wigner.correlator_tmd_model import (
    CollinearAnchors,
    CorrelatorParameters,
    ReducedCorrelatorTMDModel,
)
from deuteron_wigner.gtmd import Species
from deuteron_wigner.registry import (
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)

REFERENCE = Path("outputs/complete/spin1_tmd_phase_space.csv")
OUTPUT = Path("outputs/production_tmds/spin1_tmds_x010_q5.csv")
X_VALUE = 0.10
Q_VALUE = 5.0
K_AXIS = np.linspace(0.0, 2.0, 241)
FLAVORS = (
    (Species.GLUON, 21, "g"),
    (Species.QUARK, 2, "u"),
    (Species.QUARK, 1, "d"),
    (Species.ANTIQUARK, -2, "ubar"),
    (Species.ANTIQUARK, -1, "dbar"),
)
COMPONENTS = (
    "pdf",
    "wave_function",
    "transverse_profile",
    "evolution",
    "gauge_phase",
    "mechanism",
    "numerical",
)


def load_reference_anchors() -> dict[tuple[str, int], CollinearAnchors]:
    """Recover collinear normalizations from the prior anchor table.

    Quark anchors in that table use normalized Gaussians.  The gluon W-term
    anchor is converted by matching its origin value to the production
    Gaussian; this is explicitly recorded as a normalization transfer, not
    a new collinear extraction.
    """

    data = pd.read_csv(REFERENCE)
    selected = data[
        np.isclose(data["x_N"], X_VALUE)
        & np.isclose(data["Q_GeV"], Q_VALUE)
        & np.isclose(data["k_GeV"], 0.0)
        & (data["gauge_link"] == GaugeLink.FUTURE.value)
    ]
    result: dict[tuple[str, int], CollinearAnchors] = {}
    widths = {"g": 0.30, "q": 0.25, "qbar": 0.25}
    for species, flavor, _ in FLAVORS:
        block = selected[
            (selected["species"] == species.value)
            & (selected["flavor"] == flavor)
        ]
        values = block.set_index("tmd")["central_GeV-2"]
        factor = np.pi * widths[species.value]
        f1 = float(values["f1"] * factor)
        g1 = float(values["g1"] * factor)
        f1ll = float(values["f1LL"] * factor)
        h1 = (
            0.0
            if species == Species.GLUON
            else float(values["h1"] * factor)
        )
        result[(species.value, flavor)] = CollinearAnchors(f1, g1, f1ll, h1)
    return result


def anchor_pair(
    anchors: CollinearAnchors, component: str
) -> tuple[CollinearAnchors, CollinearAnchors]:
    if component != "pdf":
        return anchors, anchors
    return (
        CollinearAnchors(
            0.97 * anchors.f1,
            0.86 * anchors.g1,
            0.80 * anchors.f1ll,
            0.90 * anchors.h1,
        ),
        CollinearAnchors(
            1.03 * anchors.f1,
            1.14 * anchors.g1,
            1.20 * anchors.f1ll,
            1.10 * anchors.h1,
        ),
    )


def parameter_pair(
    base: CorrelatorParameters, component: str
) -> tuple[CorrelatorParameters, CorrelatorParameters]:
    if component == "wave_function":
        return (
            base.varied(d_probability=0.045, tensor_coherence=0.38),
            base.varied(d_probability=0.070, tensor_coherence=0.52),
        )
    if component == "transverse_profile":
        return (
            base.varied(width_quark=0.20, width_gluon=0.24),
            base.varied(width_quark=0.32, width_gluon=0.40),
        )
    if component == "evolution":
        return (
            base.varied(evolution_broadening=0.020),
            base.varied(evolution_broadening=0.055),
        )
    if component == "gauge_phase":
        return (
            base.varied(gauge_phase=0.05),
            base.varied(gauge_phase=0.15),
        )
    if component == "mechanism":
        return (
            base.varied(
                spin_orbit=0.24, linear_gluon=0.28, tensor_coherence=0.34
            ),
            base.varied(
                spin_orbit=0.40, linear_gluon=0.48, tensor_coherence=0.56
            ),
        )
    return base, base


def build_model(
    species: Species,
    anchors: CollinearAnchors,
    parameters: CorrelatorParameters,
) -> ReducedCorrelatorTMDModel:
    registry = (
        leading_twist_gluon_registry()
        if species == Species.GLUON
        else leading_twist_quark_registry(species)
    )
    return ReducedCorrelatorTMDModel(registry, species, anchors, parameters)


def main() -> None:
    reference_anchors = load_reference_anchors()
    base_parameters = CorrelatorParameters()
    rows: list[dict[str, object]] = []
    max_modulation = 0.0
    for species, flavor, flavor_label in FLAVORS:
        anchors = reference_anchors[(species.value, flavor)]
        central_model = build_model(species, anchors, base_parameters)
        entries = {entry.name: entry for entry in central_model.registry.select()}
        variation_models: dict[
            str, tuple[ReducedCorrelatorTMDModel, ReducedCorrelatorTMDModel]
        ] = {}
        for component in COMPONENTS:
            low_anchor, high_anchor = anchor_pair(anchors, component)
            low_parameters, high_parameters = parameter_pair(
                base_parameters, component
            )
            variation_models[component] = (
                build_model(species, low_anchor, low_parameters),
                build_model(species, high_anchor, high_parameters),
            )
        for link in (GaugeLink.FUTURE, GaugeLink.PAST):
            for k in K_AXIS:
                central = central_model.predict_all(
                    k=float(k), scale=Q_VALUE, gauge_link=link
                )
                central_model.require_physical_bounds(central)
                for name, prediction in central.items():
                    entry = entries[name]
                    max_modulation = max(
                        max_modulation, abs(prediction.physical_ratio)
                    )
                    row: dict[str, object] = {
                        "species": species.value,
                        "flavor": flavor,
                        "flavor_label": flavor_label,
                        "target_channel": entry.target_channel.value,
                        "tmd": name,
                        "rank": entry.transverse_rank,
                        "t_odd": int(entry.t_odd),
                        "gauge_link": link.value,
                        "x_N": X_VALUE,
                        "k_GeV": float(k),
                        "Q_GeV": Q_VALUE,
                        "F_central_GeV-2": prediction.value,
                        "physical_ratio_central": prediction.physical_ratio,
                        "origin": prediction.origin,
                    }
                    for component, models in variation_models.items():
                        values = [
                            model.predict(
                                entry, k=float(k), scale=Q_VALUE, gauge_link=link
                            ).value
                            for model in models
                        ]
                        ratios = [
                            model.predict(
                                entry, k=float(k), scale=Q_VALUE, gauge_link=link
                            ).physical_ratio
                            for model in models
                        ]
                        if component == "numerical":
                            delta = 0.003 * abs(prediction.value)
                            values = [prediction.value - delta, prediction.value + delta]
                            ratio_delta = 0.003 * abs(prediction.physical_ratio)
                            ratios = [
                                prediction.physical_ratio - ratio_delta,
                                prediction.physical_ratio + ratio_delta,
                            ]
                        else:
                            # An envelope represents the scanned family and
                            # therefore includes its declared central member.
                            values.append(prediction.value)
                            ratios.append(prediction.physical_ratio)
                        row[f"{component}_lower_GeV-2"] = min(values)
                        row[f"{component}_upper_GeV-2"] = max(values)
                        row[f"{component}_ratio_lower"] = min(ratios)
                        row[f"{component}_ratio_upper"] = max(ratios)
                    rows.append(row)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)
    metadata = {
        "status": "complete reduced-correlator model; phenomenological baseline",
        "production_ready_for_model_studies": True,
        "not_a_global_fit": True,
        "x_N": X_VALUE,
        "Q_GeV": Q_VALUE,
        "k_axis": {
            "minimum_GeV": float(K_AXIS[0]),
            "maximum_GeV": float(K_AXIS[-1]),
            "points": len(K_AXIS),
        },
        "basis": {
            "gluon": 19,
            "u": 18,
            "d": 18,
            "ubar": 18,
            "dbar": 18,
        },
        "processes": [link.value for link in GaugeLink],
        "primary_quantity": "named dimensional TMD F in GeV^-2",
        "supplemental_quantity": "rank-weighted physical ratio to f1",
        "model": (
            "shared reduced helicity amplitudes projected by a fixed "
            "species-specific symmetry matrix"
        ),
        "anchor_source": str(REFERENCE),
        "gluon_anchor_note": (
            "origin-value normalization transfer from the evolved W-term reference"
        ),
        "parameters": asdict(base_parameters),
        "separate_components": list(COMPONENTS),
        "component_interpretation": {
            "pdf": "phenomenological normalization range",
            "wave_function": "D-state/tensor-coherence model spread",
            "transverse_profile": "intrinsic-width sensitivity envelope",
            "evolution": "broadening sensitivity envelope",
            "gauge_phase": "common Wilson-line/lensing phase sensitivity",
            "mechanism": "shared spin-orbit/linear/tensor mechanism envelope",
            "numerical": "conservative relative numerical tolerance",
        },
        "combined_band": None,
        "maximum_absolute_physical_modulation": max_modulation,
        "rows": len(rows),
    }
    OUTPUT.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
