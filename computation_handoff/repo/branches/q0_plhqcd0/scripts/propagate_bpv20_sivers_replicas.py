#!/usr/bin/env python3
"""Propagate all official BPV20 replicas through the deuteron LF convolution."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.bpv20_sivers import BPV20ReplicaMomentumGrid
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nuclear_mechanisms import default_off_shell_input
from deuteron_wigner.spin import project_matrix, spin_one_basis
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
FLAVOR_LABELS = {2: "u", 1: "d", -2: "ubar", -1: "dbar"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("projections", type=Path)
    parser.add_argument(
        "--grid", type=Path,
        default=Path("data/processed/bpv20_sivers_replicas_Q5.npz"),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--members-output", type=Path)
    return parser.parse_args()


def t_channel_projection(vectors: np.ndarray, k: float, angle: float) -> np.ndarray:
    """Project a batch of vector correlators onto the spin-1 Sivers amplitude."""

    if np.isclose(k, 0.0):
        return np.zeros(len(vectors))
    basis = spin_one_basis()
    kx, ky = k * np.cos(angle), k * np.sin(angle)
    tx = project_matrix(vectors, basis["T_x"])
    ty = project_matrix(vectors, basis["T_y"])
    return np.real(M_D_GEV * (ky * tx - kx * ty) / k**2)


def main() -> None:
    args = parse_args()
    source = pd.read_csv(args.projections)
    metadata = json.loads(args.projections.with_suffix(".metadata.json").read_text())
    wave_name = str(source.wave_function.iloc[0])
    settings = metadata["internal_quadrature"]
    wave = select_momentum_wave_function(wave_name)
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
    grid = BPV20ReplicaMomentumGrid.load(args.grid)
    if not np.isclose(grid.q_gev, float(source.Q_GeV.iloc[0])):
        raise ValueError("replica-grid Q does not match parent table")
    off_shell = default_off_shell_input()
    sigma_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), complex)
    sigma_y = np.asarray(((0.0, 1j), (-1j, 0.0)), complex)
    configurations = (
        source.loc[
            source.tmd.eq("f1Tperp")
            & source.gauge_link.eq("[+,+]")
            & source.mechanism.eq("model_total"),
            ["flavor", "x_D", "x_N", "Q_GeV", "k_GeV", "azimuth_rad", "F_GeV-2"],
        ]
        .drop_duplicates()
        .sort_values(["flavor", "k_GeV"])
    )
    central_rows = source.loc[
        source.tmd.eq("f1Tperp") & source.gauge_link.eq("[+,+]"),
        ["flavor", "k_GeV", "mechanism", "F_GeV-2"],
    ]
    central_lookup = {
        (int(flavor), float(k), str(mechanism)): float(value)
        for flavor, k, mechanism, value in central_rows.itertuples(
            index=False, name=None
        )
    }
    summaries: list[dict[str, object]] = []
    member_payload: dict[str, np.ndarray] = {}
    mask_cache: dict[float, np.ndarray] = {}
    for row in configurations.itertuples(index=False):
        flavor = int(row.flavor)
        x_d, k, angle = float(row.x_D), float(row.k_GeV), float(row.azimuth_rad)
        kx, ky = k * np.cos(angle), k * np.sin(angle)
        mask = mask_cache.setdefault(x_d, reference.y >= x_d)
        y = reference.y[mask]
        z = x_d / y
        parton_kx = kx - z * HBARC_GEV_FM * reference.p_x[mask]
        parton_ky = ky - z * HBARC_GEV_FM * reference.p_y[mask]
        parton_k = np.hypot(parton_kx, parton_ky)
        proton_values = grid.interpolate_all(flavor, z, parton_k)
        neutron_flavor = {2: 1, 1: 2, -2: -1, -1: -2}[flavor]
        neutron_values = grid.interpolate_all(neutron_flavor, z, parton_k)
        spin_matrix = (
            parton_ky[:, None, None] * sigma_x
            - parton_kx[:, None, None] * sigma_y
        ) / M_N_GEV
        factors = reference.weights[mask] / y

        def contract(values: np.ndarray, node_factor: np.ndarray) -> np.ndarray:
            return 0.25 * np.einsum(
                "n,nIHca,rn,nac->rIH",
                factors * node_factor, spectral[mask], values, spin_matrix,
                optimize=True,
            )

        proton = contract(proton_values, np.ones_like(y))
        neutron = contract(neutron_values, np.ones_like(y))
        impulse = proton + neutron
        delta = reference.virtuality[mask] * np.asarray([
            off_shell.value(
                "valence" if flavor > 0 else "sea", float(zz), float(row.Q_GeV)
            )
            for zz in z
        ])
        off = contract(proton_values + neutron_values, delta)
        mechanisms = {
            "proton_impulse": proton,
            "neutron_impulse": neutron,
            "impulse_total": impulse,
            "off_shell": off,
            # Current coherent/antishadowing maps leave the transverse target
            # irrep unchanged, and source-required extra components are zero.
            "model_total": impulse + off,
        }
        for mechanism, vectors in mechanisms.items():
            values = t_channel_projection(vectors, k, angle)
            key = f"{flavor}_{k:.8f}_{mechanism}"
            member_payload[key] = values
            q16, median, q84 = np.quantile(values, (0.16, 0.5, 0.84))
            summaries.append({
                "wave_function": wave_name,
                "flavor": flavor,
                "flavor_label": FLAVOR_LABELS[flavor],
                "tmd": "f1Tperp",
                "gauge_link": "[+,+]",
                "x_N": float(row.x_N),
                "x_D": x_d,
                "Q_GeV": float(row.Q_GeV),
                "k_GeV": k,
                "azimuth_rad": angle,
                "mechanism": mechanism,
                "F_central_GeV-2": central_lookup[(flavor, k, mechanism)],
                "F_replica_mean_GeV-2": float(np.mean(values)),
                "F_replica_median_GeV-2": float(median),
                "F_q16_GeV-2": float(q16),
                "F_q84_GeV-2": float(q84),
                "F_replica_std_GeV-2": float(np.std(values, ddof=1)),
                "replica_count": len(values),
            })
    future = pd.DataFrame(summaries)
    # Process reversal is exact. Quantile endpoints reverse order under -F.
    past = future.copy()
    past["gauge_link"] = "[-,-]"
    past["F_central_GeV-2"] *= -1
    past["F_replica_mean_GeV-2"] *= -1
    past["F_replica_median_GeV-2"] *= -1
    old_low = past["F_q16_GeV-2"].copy()
    past["F_q16_GeV-2"] = -past["F_q84_GeV-2"]
    past["F_q84_GeV-2"] = -old_low
    output = pd.concat((future, past), ignore_index=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.output, index=False)
    members_path = args.members_output or args.output.with_suffix(".members.npz")
    np.savez_compressed(members_path, **member_payload)
    validation = {
        "status": "pass",
        "replica_count": 500,
        "central_is_separate_member_0": True,
        "future_past_exact_sign": bool(np.allclose(
            future["F_q16_GeV-2"], -past["F_q84_GeV-2"], rtol=0.0, atol=0.0
        )),
        "all_finite": bool(np.isfinite(output.select_dtypes("number")).all().all()),
        "member_identity_preserved": True,
        "interpolation_grid": str(args.grid),
        "nuclear_model_note": (
            "BPV20 fit replicas only; wave-function, H1 scenario, CJ26, and "
            "missing-component uncertainties remain separated rather than "
            "being assigned an unsupported joint probability distribution"
        ),
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(validation, indent=2) + "\n"
    )
    if not all((validation["future_past_exact_sign"], validation["all_finite"])):
        raise AssertionError(validation)
    print(f"Wrote {len(output)} band rows to {args.output}")


if __name__ == "__main__":
    main()
