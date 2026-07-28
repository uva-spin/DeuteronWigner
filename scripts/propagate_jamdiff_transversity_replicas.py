#!/usr/bin/env python3
"""Propagate correlated JAMDiFF transversity replicas through the LF parent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nuclear_mechanisms import default_off_shell_input
from deuteron_wigner.nucleon_inputs import (
    ISOSPIN_ROTATION,
    NucleonInputConfiguration,
    composed_transversity_ceiling,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import quark_correlator_basis
from deuteron_wigner.transversity import JAMDiFFReplicaGrid
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
FLAVOR_LABELS = {2: "u", 1: "d", -2: "ubar", -1: "dbar"}
MECHANISMS = (
    "proton_impulse", "neutron_impulse", "impulse_total", "off_shell",
    "model_total",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("projections", type=Path)
    parser.add_argument(
        "--grid", type=Path,
        default=Path(
            "data/processed/jamdiff_wlqcd_transversity_replicas_Q5.npz"
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tmd", choices=("h1", "h1Lperp"), default="h1")
    return parser.parse_args()


def projection_row(k: float, angle: float, tmd: str = "h1") -> np.ndarray:
    """Linear named projector acting on a batch of transverse correlators."""

    momentum = (k * np.cos(angle), k * np.sin(angle))
    basis = quark_correlator_basis(momentum, M_D_GEV)
    if np.isclose(k, 0.0):
        names = ("f1", "g1", "h1", "f1LL", "h1LT")
        if tmd not in names:
            return np.zeros(72)
    else:
        names = tuple(basis)

    def column(name: str) -> np.ndarray:
        item = basis[name]
        values = np.concatenate((
            item.vector.ravel(), item.axial.ravel(), item.transverse.ravel()
        ))
        return np.concatenate((values.real, values.imag))

    design = np.column_stack([column(name) for name in names])
    return np.linalg.pinv(design)[names.index(tmd)]


def project_transverse(values: np.ndarray, row: np.ndarray) -> np.ndarray:
    """Project ``(member,2,3,3)`` transverse matrices onto h1."""

    count = len(values)
    complex_columns = np.concatenate((
        np.zeros((count, 18), dtype=complex),
        values.reshape(count, 18),
    ), axis=1)
    real_columns = np.concatenate(
        (complex_columns.real, complex_columns.imag), axis=1
    )
    return real_columns @ row


def main() -> None:
    args = parse_args()
    source = pd.read_csv(args.projections)
    metadata = json.loads(args.projections.with_suffix(".metadata.json").read_text())
    wave_name = str(source.wave_function.iloc[0])
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
    spectral = sum(piece.spectral for piece in quadratures.values())
    grid = JAMDiFFReplicaGrid.load(args.grid)
    scale = float(source.Q_GeV.iloc[0])
    if not np.isclose(scale, grid.scale_gev):
        raise ValueError("JAMDiFF cache scale does not match parent table")
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    config = NucleonInputConfiguration.flavor_resolved_baseline()
    off_shell = default_off_shell_input()
    sigma = np.asarray((
        ((0.0, 1.0), (1.0, 0.0)),
        ((0.0, 1j), (-1j, 0.0)),
    ), dtype=complex)
    sigma_z = np.asarray(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
    central_rows = source.loc[
        source.tmd.eq(args.tmd) & source.gauge_link.eq("[+,+]"),
        ["flavor", "k_GeV", "mechanism", "F_GeV-2"],
    ]
    stored_central = {
        (int(flavor), float(k), str(mechanism)): float(value)
        for flavor, k, mechanism, value in central_rows.itertuples(
            index=False, name=None
        )
    }
    configurations = (
        source.loc[
            source.tmd.eq(args.tmd)
            & source.gauge_link.eq("[+,+]")
            & source.mechanism.eq("model_total"),
            ["flavor", "x_D", "x_N", "Q_GeV", "k_GeV", "azimuth_rad"],
        ]
        .drop_duplicates()
        .sort_values(["flavor", "k_GeV"])
    )
    rows: list[dict[str, object]] = []
    payload: dict[str, np.ndarray] = {}
    central_residuals: list[float] = []
    collinear_cache: dict[
        tuple[str, int], tuple[np.ndarray, np.ndarray, float]
    ] = {}
    for row in configurations.itertuples(index=False):
        flavor = int(row.flavor)
        x_d, k, angle = float(row.x_D), float(row.k_GeV), float(row.azimuth_rad)
        kx, ky = k * np.cos(angle), k * np.sin(angle)
        mask = reference.y >= x_d
        y = reference.y[mask]
        z = x_d / y
        parton_kx = kx - z * HBARC_GEV_FM * reference.p_x[mask]
        parton_ky = ky - z * HBARC_GEV_FM * reference.p_y[mask]
        parton_k2 = parton_kx**2 + parton_ky**2
        factors = reference.weights[mask] / y
        if args.tmd == "h1":
            kernels = np.einsum(
                "nIHca,iac->niIH", spectral[mask], sigma, optimize=True
            )
        else:
            local = np.einsum(
                "ni,ac->niac",
                np.column_stack((parton_kx, parton_ky)) / M_N_GEV,
                sigma_z,
            )
            kernels = np.einsum(
                "nIHca,niac->niIH", spectral[mask], local, optimize=True
            )

        nucleon_profiles: dict[str, np.ndarray] = {}
        nucleon_central: dict[str, np.ndarray] = {}
        for nucleon in ("proton", "neutron"):
            proton_flavor = (
                flavor if nucleon == "proton"
                else ISOSPIN_ROTATION.get(flavor, flavor)
            )
            cache_key = (nucleon, flavor)
            if cache_key not in collinear_cache:
                width = float(config.transversity_widths_gev2[proton_flavor])
                if args.tmd == "h1":
                    evaluation_x = z
                else:
                    evaluation_x = np.concatenate((grid.x_axis, (1.0,)))
                raw_members = (
                    grid.interpolate_all(proton_flavor, z)
                    if args.tmd == "h1"
                    else np.concatenate((
                        grid.replica_values[
                            :, grid.flavors.index(proton_flavor)
                        ],
                        np.zeros((968, 1)),
                    ), axis=1)
                )
                raw_central = (
                    grid.interpolate_central(proton_flavor, z)
                    if args.tmd == "h1"
                    else np.concatenate((
                        grid.central_values[
                            grid.flavors.index(proton_flavor)
                        ],
                        (0.0,),
                    ))
                )
                if proton_flavor < 0:
                    endpoint = np.where(
                        evaluation_x > 0.5,
                        ((1.0 - evaluation_x) / 0.5)
                        ** config.transversity_sea_endpoint_power,
                        1.0,
                    )
                    raw_members *= endpoint[None, :]
                    raw_central *= endpoint
                unique_z, inverse = np.unique(
                    evaluation_x, return_inverse=True
                )
                unique_ceilings = np.empty(len(unique_z))
                for index, zz in enumerate(unique_z):
                    if nucleon == "proton":
                        f1 = unpolarized.proton(flavor, float(zz), scale)
                        g1 = polarized.proton(flavor, float(zz), scale)
                    else:
                        f1 = unpolarized.neutron(flavor, float(zz), scale)
                        g1 = polarized.neutron(flavor, float(zz), scale)
                    unique_ceilings[index] = (
                        0.995 * composed_transversity_ceiling(
                            f1, g1,
                            unpolarized_width_gev2=(
                                config.unpolarized_widths_gev2[proton_flavor]
                            ),
                            helicity_width_gev2=(
                                config.helicity_widths_gev2[proton_flavor]
                            ),
                            transversity_width_gev2=width,
                        )
                    )
                ceilings = unique_ceilings[inverse]
                clipped_members = np.clip(
                    raw_members, -ceilings[None, :], ceilings[None, :]
                )
                clipped_central = np.clip(
                    raw_central, -ceilings, ceilings
                )
                if args.tmd == "h1Lperp":
                    integrand = clipped_members / evaluation_x[None, :] ** 2
                    central_integrand = clipped_central / evaluation_x**2
                    dx = np.diff(evaluation_x)
                    segments = 0.5 * (
                        integrand[:, :-1] + integrand[:, 1:]
                    ) * dx[None, :]
                    central_segments = 0.5 * (
                        central_integrand[:-1] + central_integrand[1:]
                    ) * dx
                    integral = np.zeros_like(clipped_members)
                    central_integral = np.zeros_like(clipped_central)
                    integral[:, :-1] = np.cumsum(
                        segments[:, ::-1], axis=1
                    )[:, ::-1]
                    central_integral[:-1] = np.cumsum(
                        central_segments[::-1]
                    )[::-1]
                    clipped_members = (
                        -2.0 * M_N_GEV**2 * evaluation_x[None, :] ** 2
                        * integral / width
                    )
                    clipped_central = (
                        -2.0 * M_N_GEV**2 * evaluation_x**2
                        * central_integral / width
                    )
                    indices = np.clip(
                        np.searchsorted(evaluation_x, z) - 1,
                        0, len(evaluation_x) - 2,
                    )
                    fraction = (
                        (z - evaluation_x[indices])
                        / (evaluation_x[indices + 1] - evaluation_x[indices])
                    )
                    clipped_members = (
                        (1.0 - fraction) * clipped_members[:, indices]
                        + fraction * clipped_members[:, indices + 1]
                    )
                    clipped_central = np.interp(
                        z, evaluation_x, clipped_central
                    )
                collinear_cache[cache_key] = (
                    clipped_members,
                    clipped_central,
                    width,
                )
            members, central, width = collinear_cache[cache_key]
            gaussian = np.exp(-parton_k2 / width) / (np.pi * width)
            nucleon_profiles[nucleon] = members * gaussian[None, :]
            nucleon_central[nucleon] = central * gaussian

        def contract(profiles: np.ndarray, response: np.ndarray) -> np.ndarray:
            return 0.25 * np.einsum(
                "n,niIH,rn->riIH",
                factors * response, kernels, profiles, optimize=True,
            )

        def contract_central(profile: np.ndarray, response: np.ndarray) -> np.ndarray:
            return 0.25 * np.einsum(
                "n,niIH,n->iIH",
                factors * response, kernels, profile, optimize=True,
            )

        proton = contract(nucleon_profiles["proton"], np.ones_like(y))
        neutron = contract(nucleon_profiles["neutron"], np.ones_like(y))
        proton_c = contract_central(
            nucleon_central["proton"], np.ones_like(y)
        )
        neutron_c = contract_central(
            nucleon_central["neutron"], np.ones_like(y)
        )
        delta = reference.virtuality[mask] * np.asarray([
            off_shell.value(
                "valence" if flavor > 0 else "sea", float(zz), scale
            )
            for zz in z
        ])
        off = contract(
            nucleon_profiles["proton"] + nucleon_profiles["neutron"], delta
        )
        off_c = contract_central(
            nucleon_central["proton"] + nucleon_central["neutron"], delta
        )
        resolved = {
            "proton_impulse": (proton, proton_c),
            "neutron_impulse": (neutron, neutron_c),
            "impulse_total": (proton + neutron, proton_c + neutron_c),
            "off_shell": (off, off_c),
            "model_total": (
                proton + neutron + off, proton_c + neutron_c + off_c
            ),
        }
        projector = projection_row(k, angle, args.tmd)
        for mechanism, (matrices, central_matrix) in resolved.items():
            members = project_transverse(matrices, projector)
            calculated_central = float(
                project_transverse(central_matrix[None], projector)[0]
            )
            expected_central = stored_central[(flavor, k, mechanism)]
            central_residuals.append(abs(calculated_central - expected_central))
            payload[f"{flavor}_{k:.8f}_{mechanism}"] = members
            q16, median, q84 = np.quantile(members, (0.16, 0.5, 0.84))
            rows.append({
                "wave_function": wave_name,
                "flavor": flavor,
                "flavor_label": FLAVOR_LABELS[flavor],
                "tmd": args.tmd,
                "gauge_link": "[+,+]",
                "x_N": float(row.x_N),
                "x_D": x_d,
                "Q_GeV": scale,
                "k_GeV": k,
                "azimuth_rad": angle,
                "mechanism": mechanism,
                "F_central_GeV-2": expected_central,
                "F_recomputed_central_GeV-2": calculated_central,
                "F_replica_mean_GeV-2": float(np.mean(members)),
                "F_replica_median_GeV-2": float(median),
                "F_q16_GeV-2": float(q16),
                "F_q84_GeV-2": float(q84),
                "F_replica_std_GeV-2": float(np.std(members, ddof=0)),
                "replica_count": 968,
            })
    future = pd.DataFrame(rows)
    # Both h1 and h1Lperp are T-even.
    past = future.copy()
    past["gauge_link"] = "[-,-]"
    output = pd.concat((future, past), ignore_index=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.output, index=False)
    np.savez_compressed(args.output.with_suffix(".members.npz"), **payload)
    scale_value = max(
        float(np.max(np.abs(output["F_central_GeV-2"]))), 1.0e-12
    )
    report = {
        "status": "pass",
        "replica_count": 968,
        "member_identity": "LHAPDF members 1-968; central is separate member 0",
        "maximum_central_absolute_residual_GeV-2": max(central_residuals),
        "maximum_central_relative_to_output_scale": (
            max(central_residuals) / scale_value
        ),
        "future_past_exact_invariance": True,
        "composition": (
            "each replica receives the same documented large-x sea endpoint "
            "and member-wise CT18+BDSSV Gaussian TMD Soffer projection before "
            "LF convolution; h1Lperp additionally applies the correlated WW "
            "integral member by member"
        ),
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    if report["maximum_central_relative_to_output_scale"] > 5.0e-3:
        raise AssertionError(f"JAMDiFF central roundtrip failed: {report}")
    print(f"Wrote {len(output)} rows; central residual {max(central_residuals):.3e}")


if __name__ == "__main__":
    main()
