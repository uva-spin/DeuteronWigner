#!/usr/bin/env python3
"""Propagate collinear-PDF uncertainties through one LF deuteron parent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nuclear_mechanisms import default_off_shell_input
from deuteron_wigner.nucleon_inputs import ISOSPIN_ROTATION, NucleonInputConfiguration
from deuteron_wigner.quark_correlator import quark_correlator_basis
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC = 0.1973269804
M_N = 0.93891897
M_D = 1.87561294257
LABELS = {2: "u", 1: "d", -2: "ubar", -1: "dbar"}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("projections", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tmd", choices=("g1", "f1"), default="g1")
    return parser.parse_args()


def projector(k: float, angle: float, tmd: str) -> np.ndarray:
    basis = quark_correlator_basis(
        (k*np.cos(angle), k*np.sin(angle)), M_D
    )
    names = ("f1", "g1", "h1", "f1LL", "h1LT") if np.isclose(k, 0) else tuple(basis)

    def column(name: str) -> np.ndarray:
        item = basis[name]
        values = np.concatenate((
            item.vector.ravel(), item.axial.ravel(), item.transverse.ravel()
        ))
        return np.concatenate((values.real, values.imag))

    design = np.column_stack([column(name) for name in names])
    return np.linalg.pinv(design)[names.index(tmd)]


def project_operator(
    values: np.ndarray, row: np.ndarray, tmd: str,
) -> np.ndarray:
    count = len(values)
    if tmd == "g1":
        columns = np.concatenate((
            np.zeros((count, 9), complex), values.reshape(count, 9),
            np.zeros((count, 18), complex),
        ), axis=1)
    else:
        columns = np.concatenate((
            values.reshape(count, 9), np.zeros((count, 27), complex),
        ), axis=1)
    return np.concatenate((columns.real, columns.imag), axis=1) @ row


def main() -> None:
    args = arguments()
    source = pd.read_csv(args.projections)
    metadata = json.loads(args.projections.with_suffix(".metadata.json").read_text())
    wave_name = str(source.wave_function.iloc[0])
    wave = select_momentum_wave_function(wave_name)
    settings = metadata["internal_quadrature"]
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial, nucleon_mass=M_N/HBARC,
        k_max=float(settings["k_max_fm-1"]), delta_x=0.0, delta_y=0.0,
        n_k=int(settings["n_k"]), n_cos_theta=int(settings["n_cos"]),
        n_phi=int(settings["n_phi"]), deuteron_mass=M_D/HBARC,
    )
    reference = quadratures["SS"]
    spectral = sum(piece.spectral for piece in quadratures.values())
    operator = (
        np.asarray(((1.0, 0.0), (0.0, -1.0)), complex)
        if args.tmd == "g1" else np.eye(2, dtype=complex)
    )
    kernel_all = np.einsum("nIHca,ac->nIH", spectral, operator, optimize=True)
    config = NucleonInputConfiguration.flavor_resolved_baseline()
    off_shell = default_off_shell_input()

    import lhapdf
    local = str((Path("data/raw/lhapdf")).resolve())
    if local not in lhapdf.paths():
        lhapdf.setPaths([local, *lhapdf.paths()])
    set_name = "BDSSV24-NLO" if args.tmd == "g1" else "CT18NNLO"
    pdf_set = lhapdf.getPDFSet(set_name)
    expected_size = 601 if args.tmd == "g1" else 59
    expected_error = "replicas" if args.tmd == "g1" else "hessian"
    if int(pdf_set.size) != expected_size or str(pdf_set.errorType) != expected_error:
        raise RuntimeError(f"unexpected {set_name} member convention")
    pdfs = pdf_set.mkPDFs()
    replicas = pdfs[1:]
    central_pdf = pdfs[0]

    central_table = source[
        source.tmd.eq(args.tmd) & source.gauge_link.eq("[+,+]")
    ]
    stored = {
        (int(r.flavor), float(r.k_GeV), str(r.mechanism)): float(r["F_GeV-2"])
        for _, r in central_table.iterrows()
    }
    configurations = (
        central_table[central_table.mechanism.eq("model_total")][
            ["flavor", "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad"]
        ].drop_duplicates().sort_values(["flavor", "k_GeV"])
    )
    rows, payload, residuals = [], {}, []
    density_cache = {}
    for point in configurations.itertuples(index=False):
        flavor, x_d = int(point.flavor), float(point.x_D)
        k, angle, scale = float(point.k_GeV), float(point.azimuth_rad), float(point.Q_GeV)
        mask = reference.y >= x_d
        y, z = reference.y[mask], x_d/reference.y[mask]
        factors = reference.weights[mask]/y
        kx, ky = k*np.cos(angle), k*np.sin(angle)
        parton_k2 = (
            kx-z*HBARC*reference.p_x[mask]
        )**2 + (
            ky-z*HBARC*reference.p_y[mask]
        )**2
        kernel = kernel_all[mask]
        values = {}
        central_values = {}
        for nucleon in ("proton", "neutron"):
            pdf_flavor = flavor if nucleon == "proton" else ISOSPIN_ROTATION.get(flavor, flavor)
            key = (nucleon, flavor, x_d)
            if key not in density_cache:
                member_density = np.asarray([
                    [pdf.xfxQ(pdf_flavor, float(zz), scale)/zz for zz in z]
                    for pdf in replicas
                ])
                central_density = np.asarray([
                    central_pdf.xfxQ(pdf_flavor, float(zz), scale)/zz
                    for zz in z
                ])
                density_cache[key] = member_density, central_density
            member_density, central_density = density_cache[key]
            widths = (
                config.helicity_widths_gev2 if args.tmd == "g1"
                else config.unpolarized_widths_gev2
            )
            width = float(widths[pdf_flavor])
            gaussian = np.exp(-parton_k2/width)/(np.pi*width)
            profiles = member_density*gaussian[None, :]
            profile_c = central_density*gaussian
            values[nucleon] = 0.25*np.einsum(
                "n,nIH,rn->rIH", factors, kernel, profiles, optimize=True
            )
            central_values[nucleon] = 0.25*np.einsum(
                "n,nIH,n->IH", factors, kernel, profile_c, optimize=True
            )
        response = reference.virtuality[mask]*np.asarray([
            off_shell.value("valence" if flavor > 0 else "sea", float(zz), scale)
            for zz in z
        ])
        total_profiles = (
            (density_cache[("proton", flavor, x_d)][0]
             * np.exp(-parton_k2/widths[flavor])
             /(np.pi*widths[flavor]))
            + (density_cache[("neutron", flavor, x_d)][0]
               * np.exp(-parton_k2/widths[
                   ISOSPIN_ROTATION.get(flavor, flavor)])
               /(np.pi*widths[
                   ISOSPIN_ROTATION.get(flavor, flavor)]))
        )
        off = 0.25*np.einsum(
            "n,nIH,rn->rIH", factors*response, kernel, total_profiles,
            optimize=True,
        )
        resolved = {
            "proton_impulse": values["proton"],
            "neutron_impulse": values["neutron"],
            "impulse_total": values["proton"]+values["neutron"],
            "off_shell": off,
        }
        row_projector = projector(k, angle, args.tmd)
        projected_raw = {
            name: project_operator(matrix, row_projector, args.tmd)
            for name, matrix in resolved.items()
        }
        central_projected = {
            "proton_impulse": project_operator(
                central_values["proton"][None], row_projector, args.tmd
            )[0],
            "neutron_impulse": project_operator(
                central_values["neutron"][None], row_projector, args.tmd
            )[0],
        }
        central_projected["impulse_total"] = (
            central_projected["proton_impulse"]
            + central_projected["neutron_impulse"]
        )
        # The production central has already traversed the common evolved
        # Q=5 grid. Propagate the replica response as a deviation about
        # BDSSV member 0, then anchor that deviation to the stored evolved
        # central. This preserves the released member covariance without
        # silently replacing the production evolution scheme.
        projected = {
            name: (
                stored[(flavor, k, name)]
                + members-central_projected[name]
            )
            for name, members in projected_raw.items()
            if name in central_projected
        }
        projected["off_shell"] = projected_raw["off_shell"]
        projected["model_total"] = (
            stored[(flavor, k, "model_total")]
            + projected_raw["impulse_total"]
            - central_projected["impulse_total"]
            + projected_raw["off_shell"]
            - np.mean(projected_raw["off_shell"])
        )
        for mechanism, members in projected.items():
            expected = stored.get((flavor, k, mechanism))
            if expected is not None:
                if mechanism in ("proton_impulse", "neutron_impulse", "impulse_total"):
                    central_matrix = (
                        central_values["proton"] if mechanism == "proton_impulse"
                        else central_values["neutron"] if mechanism == "neutron_impulse"
                        else central_values["proton"]+central_values["neutron"]
                    )
                    residuals.append(abs(
                        project_operator(
                            central_matrix[None], row_projector, args.tmd
                        )[0]
                        - expected
                    ))
            if expected_error == "replicas":
                q16, median, q84 = np.quantile(members, (0.16, 0.5, 0.84))
                sigma = float(np.std(members, ddof=1))
            else:
                sigma = float(np.sqrt(np.sum(
                    ((members[0::2]-members[1::2])/2.0)**2
                )))
                median = stored.get(
                    (flavor, k, mechanism), float(np.mean(members))
                )
                q16, q84 = median-sigma, median+sigma
            rows.append({
                "wave_function": wave_name, "flavor": flavor,
                "flavor_label": LABELS[flavor], "tmd": args.tmd,
                "gauge_link": "[+,+]", "x_N": float(point.x_N), "x_D": x_d,
                "Q_GeV": scale, "k_GeV": k, "azimuth_rad": angle,
                "mechanism": mechanism,
                "F_central_GeV-2": stored.get((flavor, k, mechanism), float(np.mean(members))),
                "F_replica_mean_GeV-2": float(np.mean(members)),
                "F_replica_median_GeV-2": float(median),
                "F_q16_GeV-2": float(q16), "F_q84_GeV-2": float(q84),
                "F_replica_std_GeV-2": sigma,
                "replica_count": len(replicas),
            })
            payload[f"{flavor}_{k:.8f}_{mechanism}"] = members
    future = pd.DataFrame(rows)
    past = future.copy()
    past["gauge_link"] = "[-,-]"
    output = pd.concat((future, past), ignore_index=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.output, index=False)
    np.savez_compressed(args.output.with_suffix(".members.npz"), **payload)
    report = {
        "status": "pass",
        "tmd": args.tmd,
        "pdf_set": set_name,
        "replica_count": len(replicas),
        "member_identity": (
            "BDSSV24-NLO LHAPDF members 1-600"
            if args.tmd == "g1" else
            "CT18NNLO 29 paired Hessian eigenvectors (members 1-58)"
        ),
        "maximum_impulse_central_residual_GeV-2": max(residuals, default=0.0),
        "central_response_treatment": (
            f"{set_name} member deviations are anchored to the stored evolved "
            "production central; the reported direct residual measures the "
            "member-0 Gaussian versus evolved-grid scheme difference and is "
            "not discarded"
        ),
        "fixed_nuclear_terms": (
            "model_total members vary impulse plus off-shell response; other "
            "central nuclear mechanisms are retained without replica variation"
        ),
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(report, indent=2)+"\n"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
