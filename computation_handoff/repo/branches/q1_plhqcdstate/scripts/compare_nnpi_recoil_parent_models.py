#!/usr/bin/env python3
"""Compare conditional and unchanged-shape NNpi recoil on LF parent tables."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    TabulatedQuarkCorrelatorProvider,
    deserialize_quark_correlator,
)
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
    NNPiLongitudinalRecoilConvolution,
    SpinAveragedPionConvolution,
    TensorPionConvolution,
    build_longitudinal_recoil_fock_component,
    build_minimal_fock_consistent_pion_component,
    build_tensor_pion_component,
)
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator_at_origin,
)

M_D_GEV = 1.87561294257
FLAVORS = ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar"))


def _add(*items: Spin1QuarkCorrelator) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        sum(item.vector for item in items),
        sum(item.axial for item in items),
        sum(item.transverse for item in items),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--x-points", type=int, default=31)
    parser.add_argument("--pion-member", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = pd.read_csv(args.parent)
    required_fixed = {
        "wave_function": "av18", "mechanism": "impulse_total",
        "gauge_link": "[collinear,T-even]", "k_GeV": 0.0,
    }
    selected = frame.copy()
    for column, value in required_fixed.items():
        selected = selected[selected[column] == value]
    if selected.empty:
        raise RuntimeError("parent table contains no requested AV18 impulse slice")
    scales = selected["Q_GeV"].unique()
    if scales.size != 1:
        raise RuntimeError("comparison requires one parent scale")
    scale = float(scales[0])
    raw = MillerTensorPionDistribution()
    fock = FockNormalizedMillerPionDistribution(raw)
    pion_pdf = JAM21IsoscalarPionPDF(args.pion_member)
    spin_average = SpinAveragedPionConvolution(fock, pion_pdf)
    tensor = TensorPionConvolution(fock, pion_pdf)
    recoil = NNPiLongitudinalRecoilConvolution(fock)
    x_axis = np.geomspace(0.005, 0.65, args.x_points)
    rows: list[dict[str, object]] = []
    max_hermiticity = 0.0
    flavor_curves: dict[str, list[float]] = {}
    for flavor, label in FLAVORS:
        flavor_frame = selected[selected["flavor"] == flavor]
        sector = "valence" if flavor > 0 else "sea"
        provider = TabulatedQuarkCorrelatorProvider.from_frame(
            flavor_frame, scale_gev=scale, parton_sector=sector
        )
        conditional_component = build_longitudinal_recoil_fock_component(
            flavor, spin_average, recoil, provider
        )
        minimal_component = build_minimal_fock_consistent_pion_component(
            flavor, spin_average, fock
        )
        tensor_component = build_tensor_pion_component(flavor, tensor)
        f1_conditional = []
        for x in x_axis:
            local = provider(float(x), scale, sector)
            # The serialized total is sufficient for the component comparison;
            # proton/neutron identity remains separately present in the source
            # table and is never reconstructed by an isoscalar flavor swap.
            zero = Spin1QuarkCorrelator(
                np.zeros((3, 3), complex), np.zeros((3, 3), complex),
                np.zeros((2, 3, 3), complex),
            )
            common_tensor = tensor_component.value(
                zero, zero, float(x), scale, sector
            )
            minimal = _add(
                local,
                minimal_component.value(local, zero, float(x), scale, sector),
                common_tensor,
            )
            conditional = _add(
                local,
                conditional_component.value(
                    zero, zero, float(x), scale, sector
                ),
                common_tensor,
            )
            max_hermiticity = max(
                max_hermiticity,
                float(np.max(np.abs(
                    conditional.vector - conditional.vector.conj().T
                ))),
            )
            base_projection = project_spin1_quark_correlator_at_origin(
                local, M_D_GEV
            )
            minimal_projection = project_spin1_quark_correlator_at_origin(
                minimal, M_D_GEV
            )
            conditional_projection = project_spin1_quark_correlator_at_origin(
                conditional, M_D_GEV
            )
            f1_conditional.append(conditional_projection["f1"])
            for name in ("f1", "g1", "h1", "f1LL", "h1LT"):
                rows.append({
                    "flavor": flavor,
                    "flavor_label": label,
                    "x_N": float(x),
                    "Q_GeV": scale,
                    "tmd": name,
                    "baseline": base_projection[name],
                    "minimal_unchanged_shape": minimal_projection[name],
                    "conditional_recoil": conditional_projection[name],
                    "conditional_minus_minimal": (
                        conditional_projection[name] - minimal_projection[name]
                    ),
                    "pion_member": args.pion_member,
                })
        flavor_curves[label] = f1_conditional
    output = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.output, index=False)
    flavor_distinct = {
        "u_vs_d": float(np.max(np.abs(
            np.asarray(flavor_curves["u"]) - np.asarray(flavor_curves["d"])
        ))),
        "ubar_vs_dbar": float(np.max(np.abs(
            np.asarray(flavor_curves["ubar"]) -
            np.asarray(flavor_curves["dbar"])
        ))),
    }
    def nucleon_flavor_distance(mechanism: str, left: int, right: int) -> float:
        lhs = frame[
            (frame["mechanism"] == mechanism) & (frame["flavor"] == left)
        ].sort_values([
            "x_N", "projection", "operator_index", "target_out", "target_in"
        ])
        rhs = frame[
            (frame["mechanism"] == mechanism) & (frame["flavor"] == right)
        ].sort_values([
            "x_N", "projection", "operator_index", "target_out", "target_in"
        ])
        if lhs.shape != rhs.shape:
            raise RuntimeError("nucleon flavor slices do not align")
        return float(np.max(np.abs(
            lhs["real"].to_numpy() + 1j * lhs["imag"].to_numpy()
            - rhs["real"].to_numpy() - 1j * rhs["imag"].to_numpy()
        )))

    nucleon_flavor_distinct = {
        "proton_u_vs_d": nucleon_flavor_distance("proton_impulse", 2, 1),
        "proton_ubar_vs_dbar": nucleon_flavor_distance(
            "proton_impulse", -2, -1
        ),
        "neutron_u_vs_d": nucleon_flavor_distance("neutron_impulse", 2, 1),
        "neutron_ubar_vs_dbar": nucleon_flavor_distance(
            "neutron_impulse", -2, -1
        ),
    }
    validation = {
        "status": "pass" if (
            max_hermiticity < 1.0e-10
            and nucleon_flavor_distinct["proton_u_vs_d"] > 1.0e-6
            and nucleon_flavor_distinct["proton_ubar_vs_dbar"] > 1.0e-8
        ) else "fail",
        "parent": str(args.parent),
        "scale_gev": scale,
        "pion_member": args.pion_member,
        "max_target_hermiticity_residual": max_hermiticity,
        "conditional_flavor_distinction": flavor_distinct,
        "nucleon_flavor_distinction": nucleon_flavor_distinct,
        "controlled_isoscalar_limit": (
            "The p+n deuteron total has u=d and ubar=dbar in the declared "
            "exact-isospin CT18 baseline. Proton and neutron flavor slices "
            "remain distinct; MSHT20QED CSB is a separate replaceable input."
        ),
        "temporary_input": (
            "JAM21 member selected explicitly; production central and PDF "
            "band require all 786 replicas"
        ),
    }
    args.output.with_suffix(".validation.json").write_text(
        json.dumps(validation, indent=2) + "\n"
    )
    if validation["status"] != "pass":
        raise RuntimeError(f"NNpi recoil comparison failed: {validation}")


if __name__ == "__main__":
    main()
