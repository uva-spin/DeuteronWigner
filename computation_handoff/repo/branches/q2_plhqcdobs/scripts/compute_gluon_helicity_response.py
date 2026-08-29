#!/usr/bin/env python3
"""Fast linear-response propagation of polarized gluon PDF replicas."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.pdfs import PolarizedLHAPDFProvider
from deuteron_wigner.spin import project_matrix, spin_one_basis
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897
DEUTERON_MASS_GEV = 1.87561294257
X_N = 0.1
SCALE_GEV = 2.0
K_MAX_GEV = 1.6
N_K = 24
MEMBERS = tuple(range(1, 601))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width-gev2", type=float, default=0.25)
    parser.add_argument(
        "--output-stem",
        type=Path,
        default=Path(
            "outputs/stage0/uncertainty/gluon_helicity_bdssv24_full"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.width_gev2 <= 0.0:
        raise ValueError("width-gev2 must be positive")
    wave = select_momentum_wave_function("av18")
    mass_fm = AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM
    deuteron_mass_fm = DEUTERON_MASS_GEV / HBARC_GEV_FM
    quadrature = build_off_forward_spin_quadrature(
        radial=wave.radial,
        nucleon_mass=mass_fm,
        k_max=10.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=16,
        n_cos_theta=12,
        n_phi=8,
    )
    rounded_y = np.round(quadrature.y, decimals=14)
    y_unique, inverse = np.unique(rounded_y, return_inverse=True)
    z_unique = (X_N / 2.0) / y_unique
    valid_groups = y_unique >= X_N / 2.0
    basis = spin_one_basis()
    sigma_z = np.diag((1.0, -1.0))
    spin_scalar = np.einsum("nIHca,ac->nIH", quadrature.spectral, sigma_z)
    channel_node = {
        label: np.asarray(
            [
                project_matrix(spin_scalar[node], basis[label]).real
                for node in range(len(quadrature.y))
            ]
        )
        for label in ("L", "T_x", "T_y", "LT_x", "LT_y")
    }
    base = {
        label: quadrature.weights * values / quadrature.y
        for label, values in channel_node.items()
    }
    axis_gev = np.linspace(-K_MAX_GEV, K_MAX_GEV, N_K)
    axis_fm = axis_gev / HBARC_GEV_FM
    width_fm2 = args.width_gev2 / HBARC_GEV_FM**2
    density_conversion = 1.0 / (4.0 * HBARC_GEV_FM**2)
    response = {
        name: np.zeros((N_K, N_K, len(y_unique)), dtype=np.float64)
        for name in ("g1g", "g1Tg", "g1LTg")
    }
    z_node = (X_N / 2.0) / quadrature.y
    for ix, k_x in enumerate(axis_fm):
        for iy, k_y in enumerate(axis_fm):
            q_x = k_x - z_node * quadrature.p_x
            q_y = k_y - z_node * quadrature.p_y
            profile = np.exp(-(q_x**2 + q_y**2) / width_fm2) / (
                np.pi * width_fm2
            )
            grouped = {
                label: np.bincount(
                    inverse,
                    weights=values * profile,
                    minlength=len(y_unique),
                )
                for label, values in base.items()
            }
            response["g1g"][ix, iy] = 2.0 * grouped["L"]
            k_squared = k_x**2 + k_y**2
            response["g1Tg"][ix, iy] = (
                2.0
                * deuteron_mass_fm
                * (k_x * grouped["T_x"] + k_y * grouped["T_y"])
                / k_squared
            )
            epsilon_k = np.asarray((k_y, -k_x))
            response["g1LTg"][ix, iy] = (
                2.0
                * deuteron_mass_fm
                * (
                    epsilon_k[0] * grouped["LT_x"]
                    + epsilon_k[1] * grouped["LT_y"]
                )
                / k_squared
            )
    for values in response.values():
        values *= density_conversion
        values[..., ~valid_groups] = 0.0

    replica_pdfs = []
    for member in MEMBERS:
        provider = PolarizedLHAPDFProvider(member=member)
        replica_pdfs.append(
            np.asarray([provider.gluon(float(z), SCALE_GEV) for z in z_unique])
        )
    replica_pdfs = np.asarray(replica_pdfs)
    predictions = {
        name: np.einsum("xyg,rg->rxy", kernel, replica_pdfs)
        for name, kernel in response.items()
    }
    central_provider = PolarizedLHAPDFProvider(member=0)
    central_pdf = np.asarray(
        [central_provider.gluon(float(z), SCALE_GEV) for z in z_unique]
    )
    central = {
        name: np.einsum("xyg,g->xy", kernel, central_pdf)
        for name, kernel in response.items()
    }
    output = args.output_stem.with_suffix(".npz")
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "members": np.asarray(MEMBERS),
        "k_x_GeV": axis_gev,
        "k_y_GeV": axis_gev,
        "y_unique": y_unique,
        "z_unique": z_unique,
        "width_GeV2": np.asarray(args.width_gev2),
    }
    for name in response:
        payload[f"{name}_response"] = response[name]
        payload[f"{name}_central"] = central[name]
        payload[f"{name}_replicas"] = predictions[name]
        payload[f"{name}_mean"] = np.mean(predictions[name], axis=0)
        payload[f"{name}_std"] = np.std(predictions[name], axis=0, ddof=1)
        payload[f"{name}_p16"] = np.percentile(predictions[name], 16.0, axis=0)
        payload[f"{name}_p84"] = np.percentile(predictions[name], 84.0, axis=0)
    np.savez_compressed(output, **payload)

    near_zero = int(np.argmin(np.abs(axis_gev)))
    rows = []
    full_std = {
        name: np.std(predictions[name], axis=0, ddof=1) for name in response
    }
    replica_order = np.random.default_rng(240711635).permutation(len(MEMBERS))
    for count in (20, 50, 100, 200, 400, len(MEMBERS)):
        subset_indices = replica_order[:count]
        row = {"replica_count": count}
        for name in response:
            subset_std = np.std(
                predictions[name][subset_indices], axis=0, ddof=1
            )
            denominator = np.linalg.norm(full_std[name])
            row[f"{name}_std_L2_relative_to_full"] = float(
                np.linalg.norm(subset_std - full_std[name]) / denominator
                if denominator else np.nan
            )
            value = central[name][near_zero, near_zero]
            sigma = subset_std[near_zero, near_zero]
            row[f"{name}_central_near_origin"] = float(value)
            row[f"{name}_sigma_near_origin"] = float(sigma)
            row[f"{name}_relative_sigma_near_origin"] = float(
                sigma / abs(value) if value else np.nan
            )
        rows.append(row)
    summary = output.with_suffix(".csv")
    with summary.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"# wrote {output} and {summary}")


if __name__ == "__main__":
    main()
