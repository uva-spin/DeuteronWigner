#!/usr/bin/env python3
"""Inject BPV20 Sivers matrices into stored zero-T-odd quark parents.

The operation recomputes only the vector Sivers convolution, vectorized over
the existing LF quadrature nodes.  It replaces the prior exact-zero
``f1Tperp`` boundary without recomputing unrelated T-even parent sectors.
Run ``refresh_quark_nuclear_corrections.py`` afterwards so algebraic nuclear
mechanisms are reconstructed from the updated impulse matrices.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.bpv20_sivers import BPV20ArtemideSivers
from deuteron_wigner.correlator_io import (
    deserialize_quark_correlator,
    quark_correlator_rows,
    write_correlator_table,
)
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nuclear_mechanisms import default_off_shell_input
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
BASE_KEYS = (
    "wave_function", "species", "flavor", "flavor_label", "gauge_link",
    "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
)
UPDATED = (
    "proton_impulse", "neutron_impulse", "impulse_total",
    "wave_SS", "wave_SD", "wave_DS", "wave_DD", "off_shell",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("projections", type=Path)
    parser.add_argument("--correlators", type=Path, required=True)
    return parser.parse_args()


def zero_correlator(vector: np.ndarray) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        vector,
        np.zeros((3, 3), dtype=np.complex128),
        np.zeros((2, 3, 3), dtype=np.complex128),
    )


def add(left: Spin1QuarkCorrelator, right: Spin1QuarkCorrelator):
    return Spin1QuarkCorrelator(
        left.vector + right.vector,
        left.axial + right.axial,
        left.transverse + right.transverse,
    )


def project(correlator, k: float, angle: float):
    if np.isclose(k, 0.0):
        return project_spin1_quark_correlator_at_origin(correlator, M_D_GEV)
    momentum = (k * np.cos(angle), k * np.sin(angle))
    return project_spin1_quark_correlator(correlator, momentum, M_D_GEV)


def main() -> None:
    args = parse_args()
    projections = pd.read_csv(args.projections)
    serialized = pd.read_csv(args.correlators)
    prior_sivers = projections.loc[
        projections.tmd.eq("f1Tperp")
        & projections.mechanism.isin(("proton_impulse", "neutron_impulse")),
        "F_GeV-2",
    ]
    if float(np.max(np.abs(prior_sivers))) > 1.0e-10:
        raise RuntimeError(
            "stored parent already has a nonzero Sivers boundary; refusing "
            "a non-idempotent second injection"
        )
    metadata = pd.read_json(args.projections.with_suffix(".metadata.json"), typ="series")
    wave_name = str(projections.wave_function.iloc[0])
    wave = select_momentum_wave_function(wave_name)
    settings = metadata["internal_quadrature"]
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=float(settings["k_max_fm-1"]),
        delta_x=0.0,
        delta_y=0.0,
        n_k=int(settings["n_k"]),
        n_cos_theta=int(settings["n_cos"]),
        n_phi=int(settings["n_phi"]),
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    reference = quadratures["SS"]
    sivers = BPV20ArtemideSivers().fitted_input()
    off_shell = default_off_shell_input()
    sigma_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128)
    sigma_y = np.asarray(((0.0, 1j), (-1j, 0.0)), dtype=np.complex128)

    additions: dict[tuple[object, ...], dict[str, Spin1QuarkCorrelator]] = {}
    unique = projections[list(BASE_KEYS)].drop_duplicates()
    # Future-link values are computed once; time reversal gives the past link.
    unique = unique.loc[unique.gauge_link.eq("[+,+]")]
    for row in unique.itertuples(index=False):
        labels = tuple(getattr(row, key) for key in BASE_KEYS)
        x_d = float(row.x_D)
        k = float(row.k_GeV)
        angle = float(row.azimuth_rad)
        kx = k * np.cos(angle)
        ky = k * np.sin(angle)
        mask = reference.y >= x_d
        y = reference.y[mask]
        z = x_d / y
        parton_kx = kx - z * HBARC_GEV_FM * reference.p_x[mask]
        parton_ky = ky - z * HBARC_GEV_FM * reference.p_y[mask]
        parton_k = np.hypot(parton_kx, parton_ky)
        matrices: dict[str, np.ndarray] = {}
        for nucleon in ("proton", "neutron"):
            values = np.asarray([
                sivers.value(
                    nucleon, int(row.flavor), float(zz), float(kk),
                    float(row.Q_GeV),
                )
                for zz, kk in zip(z, parton_k)
            ])
            matrices[nucleon] = (
                values[:, None, None]
                * (
                    parton_ky[:, None, None] * sigma_x
                    - parton_kx[:, None, None] * sigma_y
                )
                / M_N_GEV
            )
        base_factors = reference.weights[mask] / y
        delta_response = (
            reference.virtuality[mask]
            * np.asarray([
                off_shell.value(
                    "valence" if int(row.flavor) > 0 else "sea",
                    float(zz),
                    float(row.Q_GeV),
                )
                for zz in z
            ])
        )
        wave_vectors: dict[str, dict[str, np.ndarray]] = {}
        for component, quadrature in quadratures.items():
            spectral = quadrature.spectral[mask]
            wave_vectors[component] = {
                nucleon: np.einsum(
                    "n,nIHca,nac->IH",
                    base_factors,
                    spectral,
                    matrices[nucleon],
                    optimize=True,
                )
                for nucleon in ("proton", "neutron")
            }
        proton = 0.25 * sum(
            values["proton"] for values in wave_vectors.values()
        )
        neutron = 0.25 * sum(
            values["neutron"] for values in wave_vectors.values()
        )
        off_vector = 0.25 * sum(
            np.einsum(
                "n,nIHca,nac->IH",
                base_factors * delta_response,
                quadratures[component].spectral[mask],
                matrices[nucleon],
                optimize=True,
            )
            for component in quadratures
            for nucleon in ("proton", "neutron")
        )
        future = {
            "proton_impulse": zero_correlator(proton),
            "neutron_impulse": zero_correlator(neutron),
            "impulse_total": zero_correlator(proton + neutron),
            **{
                f"wave_{component}": zero_correlator(
                    0.25 * (values["proton"] + values["neutron"])
                )
                for component, values in wave_vectors.items()
            },
            "off_shell": zero_correlator(off_vector),
        }
        additions[labels] = future
        past_labels = tuple(
            "[-,-]" if key == "gauge_link" else value
            for key, value in zip(BASE_KEYS, labels)
        )
        additions[past_labels] = {
            mechanism: zero_correlator(-value.vector)
            for mechanism, value in future.items()
        }

    output_rows = []
    projection_updates = []
    for labels, group in serialized.groupby(list(BASE_KEYS), sort=False):
        label_map = dict(zip(BASE_KEYS, labels))
        by_mechanism = additions[labels]
        for mechanism, mechanism_rows in group.groupby("mechanism", sort=False):
            correlator = deserialize_quark_correlator(mechanism_rows)
            if mechanism in UPDATED:
                correlator = add(correlator, by_mechanism[mechanism])
            output_rows.extend(
                quark_correlator_rows(correlator, {**label_map, "mechanism": mechanism})
            )
            if mechanism in UPDATED:
                for tmd, value in project(
                    correlator,
                    float(label_map["k_GeV"]),
                    float(label_map["azimuth_rad"]),
                ).items():
                    projection_updates.append({
                        **label_map,
                        "mechanism": mechanism,
                        "tmd": tmd,
                        "F_replacement": value,
                    })
    write_correlator_table(output_rows, args.correlators)

    update = pd.DataFrame(projection_updates)
    merge_keys = [*BASE_KEYS, "mechanism", "tmd"]
    merged = projections.merge(
        update, on=merge_keys, how="left", validate="one_to_one"
    )
    changed = merged.mechanism.isin(UPDATED)
    if bool(merged.loc[changed, "F_replacement"].isna().any()):
        raise AssertionError("missing BPV20 parent projection update")
    merged.loc[changed, "F_GeV-2"] = merged.loc[changed, "F_replacement"]
    merged.drop(columns="F_replacement").to_csv(args.projections, index=False)
    print(f"Injected BPV20 Sivers parent into {args.projections}")


if __name__ == "__main__":
    main()
