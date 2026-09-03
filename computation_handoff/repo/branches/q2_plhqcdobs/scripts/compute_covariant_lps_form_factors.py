#!/usr/bin/env python3
"""Compute the Lev-Pace-Salme longitudinal-Breit one-body current."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from deuteron_wigner.covariant_current import (
    extract_lps_form_factors,
    hermitian_lps_current,
    lps_longitudinal_kinematics,
    lps_nucleon_current_kernels,
)
from deuteron_wigner.form_factors import (
    elastic_observables,
    load_av18_electromagnetic_tables,
)
from deuteron_wigner.light_front import (
    InternalMomentum,
    LFNormalization,
    light_front_wave_function,
)
from deuteron_wigner.wavefunctions.av18 import load_av18_momentum
from deuteron_wigner.wavefunctions.cd_bonn import cd_bonn_parameters
from deuteron_wigner.wavefunctions.norfolk import (
    load_norfolk_momentum,
    norfolk_radial_callable,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wave-function",
        choices=("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib"),
        default="av18",
    )
    parser.add_argument("--delta-gev", type=float, nargs="+", default=(0.01, 0.1, 0.3, 0.5))
    parser.add_argument("--k-max", type=float, default=10.0)
    parser.add_argument("--n-k", type=int, default=36)
    parser.add_argument("--n-cos", type=int, default=24)
    parser.add_argument("--n-phi", type=int, default=16)
    parser.add_argument(
        "--nucleon-transfer",
        choices=("node", "external"),
        default="node",
        help="evaluate nucleon form factors at exact constituent q_N or external Q",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.wave_function == "av18":
        table = load_av18_momentum("data/raw/av18/deut.wfk")
        radial = table.radial_callable()
        radial_max = float(table.grid[-1])
    elif args.wave_function == "cd-bonn":
        parameters = cd_bonn_parameters()
        radial = lambda k: tuple(float(value) for value in parameters.momentum(k))
        radial_max = np.inf
    else:
        table = load_norfolk_momentum(
            f"data/raw/norfolk/fdeut.{args.wave_function}"
        )
        radial = norfolk_radial_callable(table)
        radial_max = float(table.grid[-1])
    reference = load_av18_electromagnetic_tables("data/raw/av18/fdeut.av18")
    nucleon_mass = AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM
    deuteron_mass = (reference.deuteron_mass_mev / 1000.0) / HBARC_GEV_FM

    k_legendre, k_weights = np.polynomial.legendre.leggauss(args.n_k)
    k_nodes = 0.5 * args.k_max * (k_legendre + 1.0)
    k_weights = 0.5 * args.k_max * k_weights
    cos_nodes, cos_weights = np.polynomial.legendre.leggauss(args.n_cos)
    phi_nodes = 2.0 * np.pi * np.arange(args.n_phi) / args.n_phi
    phi_weight = 2.0 * np.pi / args.n_phi
    rows = []
    for delta_gev in args.delta_gev:
        delta = delta_gev / HBARC_GEV_FM
        free_components = {
            "electric": np.zeros((4, 3, 3), dtype=np.complex128),
            "magnetic": np.zeros((4, 3, 3), dtype=np.complex128),
        }
        for k_prime, wk in zip(k_nodes, k_weights):
            for cosine, wc in zip(cos_nodes, cos_weights):
                k_perp = k_prime * np.sqrt(max(0.0, 1.0 - cosine**2))
                k_z_prime = k_prime * cosine
                final_reference = InternalMomentum.from_cartesian(
                    k_z=float(k_z_prime),
                    p_x=float(k_perp),
                    p_y=0.0,
                    mass=nucleon_mass,
                )
                _, k_plus, k_prime_plus, _ = lps_longitudinal_kinematics(
                    fraction=final_reference.y,
                    momentum_transfer=delta,
                    deuteron_mass=deuteron_mass,
                )
                initial_fraction = 1.0 + (
                    final_reference.y - 1.0
                ) * k_prime_plus / k_plus
                if not 0.0 < initial_fraction < 1.0:
                    continue
                weight = wk * k_prime**2 * wc * phi_weight
                for phi in phi_nodes:
                    k_x = float(k_perp * np.cos(phi))
                    k_y = float(k_perp * np.sin(phi))
                    initial = InternalMomentum(
                        y=initial_fraction,
                        p_x=k_x,
                        p_y=k_y,
                        mass=nucleon_mass,
                    )
                    if initial.k_magnitude > radial_max:
                        continue
                    final = InternalMomentum(
                        y=final_reference.y,
                        p_x=k_x,
                        p_y=k_y,
                        mass=nucleon_mass,
                    )
                    incoming = light_front_wave_function(
                        y=initial.y,
                        p_x=k_x,
                        p_y=k_y,
                        mass=nucleon_mass,
                        radial=radial,
                        normalization=LFNormalization.FLAT,
                    ) / np.sqrt(initial.dkz_dy)
                    outgoing = light_front_wave_function(
                        y=final.y,
                        p_x=k_x,
                        p_y=k_y,
                        mass=nucleon_mass,
                        radial=radial,
                        normalization=LFNormalization.FLAT,
                    ) / np.sqrt(final.dkz_dy)
                    _, _, q_n_squared = lps_nucleon_current_kernels(
                        fraction=initial.y,
                        k_x=k_x,
                        k_y=k_y,
                        momentum_transfer=delta,
                        nucleon_mass=nucleon_mass,
                        deuteron_mass=deuteron_mass,
                        electric=0.0,
                        magnetic=0.0,
                    )
                    q_n = np.sqrt(q_n_squared)
                    form_factor_q = q_n if args.nucleon_transfer == "node" else delta
                    if form_factor_q > reference.q_nucleon[-1]:
                        continue
                    # fdeut.av18 stores half-isoscalar form factors, whereas
                    # LPS Eqs. (40)-(43) use proton-plus-neutron sums.
                    electric = 2.0 * reference.isoscalar_electric(form_factor_q)
                    magnetic = 2.0 * reference.isoscalar_magnetic(form_factor_q)
                    wave_factor = np.sqrt(
                        initial.energy
                        * final.y
                        / (final.energy * initial.y)
                    )
                    for label, electric_piece, magnetic_piece in (
                        ("electric", electric, 0.0),
                        ("magnetic", 0.0, magnetic),
                    ):
                        plus_kernel, x_kernel, _ = lps_nucleon_current_kernels(
                            fraction=initial.y,
                            k_x=k_x,
                            k_y=k_y,
                            momentum_transfer=delta,
                            nucleon_mass=nucleon_mass,
                            deuteron_mass=deuteron_mass,
                            electric=electric_piece,
                            magnetic=magnetic_piece,
                        )
                        plus_overlap = np.einsum(
                            "Hab,ac,Icb->HI", outgoing.conj(), plus_kernel, incoming
                        )
                        x_overlap = np.einsum(
                            "Hab,ac,Icb->HI", outgoing.conj(), x_kernel, incoming
                        )
                        free_components[label][0] += (
                            weight
                            * np.sqrt(2.0)
                            * deuteron_mass
                            * wave_factor
                            * plus_overlap
                        )
                        free_components[label][2] += weight * x_overlap
        free = free_components["electric"] + free_components["magnetic"]
        completed = hermitian_lps_current(free)
        gc, magnetic_moment_units, gq = extract_lps_form_factors(
            free,
            momentum_transfer=delta,
            deuteron_mass=deuteron_mass,
        )
        # The transverse constituent kernel is normalized in nucleon-magneton
        # units. The project convention is G_M(0)=(M_D/m_N)*mu_D.
        gm = magnetic_moment_units * deuteron_mass / nucleon_mass
        component_form_factors = {}
        for label, component in free_components.items():
            component_gc, component_mu, component_gq = extract_lps_form_factors(
                component,
                momentum_transfer=delta,
                deuteron_mass=deuteron_mass,
            )
            component_form_factors[label] = (
                component_gc,
                component_mu * deuteron_mass / nucleon_mass,
                component_gq,
            )
        q_fm = delta
        structure_a, structure_b, t20 = elastic_observables(
            q_fm=q_fm,
            gc=gc.real,
            gm=gm.real,
            gq=gq.real,
            deuteron_mass_mev=reference.deuteron_mass_mev,
        )
        rows.append(
            {
                "wave_function": args.wave_function,
                "DeltaT_GeV": delta_gev,
                "k_max_fm_inverse": args.k_max,
                "nucleon_transfer": args.nucleon_transfer,
                "GC": gc.real,
                "GM": gm.real,
                "muD_kernel_units": magnetic_moment_units.real,
                "GQ": gq.real,
                "GC_electric": component_form_factors["electric"][0].real,
                "GM_electric": component_form_factors["electric"][1].real,
                "GQ_electric": component_form_factors["electric"][2].real,
                "GC_magnetic": component_form_factors["magnetic"][0].real,
                "GM_magnetic": component_form_factors["magnetic"][1].real,
                "GQ_magnetic": component_form_factors["magnetic"][2].real,
                "GC_imag": gc.imag,
                "GM_imag": gm.imag,
                "GQ_imag": gq.imag,
                "hermiticity_residual": float(
                    np.max(np.abs(completed - hermitian_lps_current(completed)))
                ),
                "Jx_10_real": float(free[2, 0, 1].real),
                "Jx_01_real": float(free[2, 1, 0].real),
                "GC_AV18_reference": reference.charge_form_factor(q_fm),
                "GM_AV18_reference": reference.magnetic_form_factor(q_fm),
                "GQ_AV18_reference": reference.quadrupole_form_factor(q_fm),
                "A": float(structure_a),
                "B": float(structure_b),
                "t20_70deg": float(t20),
                "A_AV18_reference": float(reference.observable_a(q_fm)),
                "B_AV18_reference": float(reference.observable_b(q_fm)),
                "t20_AV18_reference": float(reference.observable_t20(q_fm)),
            }
        )
        print(
            f"{args.wave_function} Q={delta_gev:.3f} "
            f"GC={gc.real:.8g} GM={gm.real:.8g} GQ={gq.real:.8g}"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
