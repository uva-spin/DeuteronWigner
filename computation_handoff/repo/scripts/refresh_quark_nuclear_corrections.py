#!/usr/bin/env python3
"""Refresh algebraic nuclear corrections from stored quark parent matrices."""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    deserialize_quark_correlator,
    quark_correlator_rows,
    write_correlator_table,
)
from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)
from deuteron_wigner.nuclear_mechanisms import (
    NuclearCorrectionParameters,
    apply_nuclear_corrections,
    build_momentum_sum_antishadowing_input,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)

M_D_GEV = 1.87561294257
BASE_KEYS = (
    "wave_function", "species", "flavor", "flavor_label", "gauge_link",
    "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
)
REPLACED = (
    "coherent_shadowing", "antishadowing",
    "meson_exchange", "non_nucleonic", "model_total",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("projections", type=Path)
    parser.add_argument("--correlators", type=Path, required=True)
    return parser.parse_args()


def summed(values) -> Spin1QuarkCorrelator:
    items = tuple(values)
    return Spin1QuarkCorrelator(
        sum(item.vector for item in items),
        sum(item.axial for item in items),
        sum(item.transverse for item in items),
    )


def project(correlator, k, angle):
    if np.isclose(k, 0.0):
        return project_spin1_quark_correlator_at_origin(correlator, M_D_GEV)
    momentum = (k * np.cos(angle), k * np.sin(angle))
    return project_spin1_quark_correlator(correlator, momentum, M_D_GEV)


def main() -> None:
    args = parse_args()
    projections = pd.read_csv(args.projections)
    serialized = pd.read_csv(args.correlators)
    pdf = LHAPDFProvider("CT18NNLO", 0)
    scale = float(projections.Q_GeV.iloc[0])
    wave_function = str(projections.wave_function.iloc[0])
    flavors = sorted(int(value) for value in projections.flavor.unique())
    dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")
    body_form_factor_path = (
        f"outputs/stage0/body_form_factor_{wave_function.replace('-', '_')}.csv"
    )
    body_form_factor = TabulatedBodyFormFactor.load(body_form_factor_path)
    diffractive = {
        flavor: build_h1_deuteron_shadowing_input(
            inclusive_density=lambda x, q, flavor=flavor: (
                pdf.proton(flavor, x, q) + pdf.neutron(flavor, x, q)
            ),
            body_form_factor=body_form_factor,
            dpdf=dpdf,
        )
        for flavor in flavors
    }
    antishadowing = {
        flavor: build_momentum_sum_antishadowing_input(
            lambda x, q, flavor=flavor: x * (
                pdf.proton(flavor, x, q) + pdf.neutron(flavor, x, q)
            ),
            scale_gev=scale,
            parton_sector="valence" if flavor > 0 else "sea",
            diffractive_input=diffractive[flavor],
        )
        for flavor in flavors
    }
    parameters = replace(
        NuclearCorrectionParameters(), average_nucleon_virtuality=0.0
    )

    retained = serialized.loc[~serialized.mechanism.isin(REPLACED)].copy()
    refreshed_rows = []
    projected_updates = []
    for labels, base_group in serialized.groupby(list(BASE_KEYS), sort=False):
        label_map = dict(zip(BASE_KEYS, labels))
        by_mechanism = {
            mechanism: deserialize_quark_correlator(group)
            for mechanism, group in base_group.groupby("mechanism", sort=False)
        }
        flavor = int(label_map["flavor"])
        resolved = apply_nuclear_corrections(
            proton_impulse=by_mechanism["proton_impulse"],
            neutron_impulse=by_mechanism["neutron_impulse"],
            x=float(label_map["x_N"]),
            scale_gev=float(label_map["Q_GeV"]),
            parton_sector="valence" if flavor > 0 else "sea",
            parameters=parameters,
            antishadowing_input=antishadowing[flavor],
            diffractive_input=diffractive[flavor],
        )
        updated = {
            "coherent_shadowing": resolved.corrections["coherent_shadowing"],
            "antishadowing": resolved.corrections["antishadowing"],
            "meson_exchange": resolved.corrections["meson_exchange"],
            "non_nucleonic": resolved.corrections["non_nucleonic"],
        }
        updated["model_total"] = summed((
            resolved.impulse,
            updated["coherent_shadowing"],
            updated["antishadowing"],
            updated["meson_exchange"],
            updated["non_nucleonic"],
            by_mechanism["off_shell"],
        ))
        for mechanism, correlator in updated.items():
            refreshed_rows.extend(quark_correlator_rows(
                correlator, {**label_map, "mechanism": mechanism}
            ))
            for tmd, value in project(
                correlator,
                float(label_map["k_GeV"]),
                float(label_map["azimuth_rad"]),
            ).items():
                projected_updates.append({
                    **label_map, "mechanism": mechanism, "tmd": tmd,
                    "F_replacement": value,
                })

    combined = pd.concat(
        (retained, pd.DataFrame(refreshed_rows)), ignore_index=True
    )
    write_correlator_table(combined.to_dict("records"), args.correlators)

    update = pd.DataFrame(projected_updates)
    merge_keys = [*BASE_KEYS, "mechanism", "tmd"]
    for mechanism in ("meson_exchange", "non_nucleonic"):
        if mechanism not in set(projections.mechanism):
            template = projections.loc[
                projections.mechanism.eq("coherent_shadowing")
            ].copy()
            template["mechanism"] = mechanism
            template["F_GeV-2"] = 0.0
            template["physical_ratio_to_total_f1"] = 0.0
            projections = pd.concat((projections, template), ignore_index=True)
    merged = projections.merge(
        update, on=merge_keys, how="left", validate="one_to_one"
    )
    replaced_mask = merged.mechanism.isin(REPLACED)
    if bool(merged.loc[replaced_mask, "F_replacement"].isna().any()):
        raise AssertionError("missing refreshed projection")
    merged.loc[replaced_mask, "F_GeV-2"] = merged.loc[
        replaced_mask, "F_replacement"
    ]
    merged = merged.drop(columns="F_replacement")
    model_f1 = (
        merged.loc[
            merged.mechanism.eq("model_total") & merged.tmd.eq("f1"),
            [*BASE_KEYS, "F_GeV-2"],
        ]
        .rename(columns={"F_GeV-2": "model_f1"})
    )
    merged = merged.drop(columns="physical_ratio_to_total_f1").merge(
        model_f1, on=list(BASE_KEYS), validate="many_to_one"
    )
    merged["physical_ratio_to_total_f1"] = (
        (merged.k_GeV / M_D_GEV) ** merged["rank"]
        * merged["F_GeV-2"]
        / merged.model_f1
    ).fillna(0.0)
    merged = merged.drop(columns="model_f1")
    merged.to_csv(args.projections, index=False)

    metadata_path = args.projections.with_suffix(".metadata.json")
    metadata = json.loads(metadata_path.read_text())
    has_fitted_sivers = float(np.max(np.abs(
        projections.loc[
            projections.tmd.eq("f1Tperp")
            & projections.mechanism.eq("impulse_total"),
            "F_GeV-2",
        ]
    ))) > 1.0e-10
    if has_fitted_sivers:
        metadata["t_odd_boundary"] = {
            "f1Tperp": (
                "BPV20 N3LO 500-replica fit central, evolved with released "
                "arTeMiDe v2.05; SIDIS is the future-link reference"
            ),
            "h1perp": "exact zero in the real one-body impulse baseline",
            "process_rule": "all T-odd structures reverse sign for past links",
            "replica_uncertainty_status": (
                "official 500 replicas ingested and validated at the nucleon "
                "boundary; run propagate_bpv20_sivers_replicas.py after this "
                "central-table refresh to regenerate nuclear fit bands"
            ),
        }
        limitations = list(metadata.get("limitations", []))
        obsolete = {
            "coherent shadowing, antishadowing, and off-shell terms remain transparent configurable sensitivity models rather than a joint fit",
        }
        limitations = [item for item in limitations if item not in obsolete]
        for item in (
            "BPV20 documents parton-model Sivers positivity-bound violations; constituent proton/neutron eigenvalues are reported without clipping, while physical deuteron total positivity remains a validation gate",
            "BPV20 ubar and dbar share a fitted sea shape; exact-isospin deuteron sums can therefore coincide even though proton u and d remain distinct",
            "BPV20 central tables do not embed replica columns; member-preserving nuclear bands are separate outputs generated by propagate_bpv20_sivers_replicas.py",
        ):
            if item not in limitations:
                limitations.append(item)
        metadata["limitations"] = limitations
    metadata["shadowing_input"] = {
        "source": diffractive[flavors[0]].source,
        "classification": diffractive[flavors[0]].classification.value,
        "relative_uncertainty": diffractive[flavors[0]].relative_uncertainty,
        "uncertainty_members": sorted(
            diffractive[flavors[0]].uncertainty_members or {}
        ),
        "h1_release": "H1 2007 Jets DPDF v1.0 (04/06/2009)",
        "h1_grid_directory": "data/raw/h1_2007_dpdf",
        "deuteron_body_form_factor": body_form_factor_path,
        "formula": "FGS arXiv:hep-ph/0601123 Eq. (4)",
        "x_pomeron_max": {"quark": 0.1, "gluon": 0.03},
        "real_part_eta": 0.5 * np.pi * (dpdf.alpha_pomeron_0 - 1.0),
        "separate_external_coherence_factor": False,
    }
    metadata["mechanisms"] = [
        "proton_impulse", "neutron_impulse", "impulse_total",
        "wave_SS", "wave_SD", "wave_DS", "wave_DD",
        "coherent_shadowing", "antishadowing", "off_shell",
        "meson_exchange", "non_nucleonic", "model_total",
    ]
    metadata["inactive_source_required_components"] = {
        "meson_exchange": (
            "zero baseline; configure AdditionalNuclearComponentInput with "
            "a deuteron meson splitting function and meson TMD/PDF"
        ),
        "non_nucleonic": (
            "zero baseline; configure AdditionalNuclearComponentInput with "
            "a sourced six-quark or Delta-Delta probability and correlator"
        ),
    }
    metadata["antishadowing_momentum_sum_audit"] = {
        str(flavor): {
            "lost_momentum": model.lost_momentum,
            "restored_momentum": model.restored_momentum,
            "compensation_fraction": model.compensation_fraction,
        }
        for flavor, model in antishadowing.items()
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"Refreshed nuclear corrections in {args.projections}")


if __name__ == "__main__":
    main()
