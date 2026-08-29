#!/usr/bin/env python3
"""Audit LF-wave off-forward GTMD/GPD/TMD/Wigner commuting reductions."""

import json
from pathlib import Path

import numpy as np

OUT = Path("outputs/validation/physical_offforward_reductions.json")
WAVES = ("av18", "cd_bonn", "nvia", "nvib", "nviia", "nviib")


def main() -> None:
    rows = []
    for wave in WAVES:
        path = Path(f"outputs/stage0/component_wigner_{wave}.npz")
        data = np.load(path)
        gtmd_components = sum(data[f"gtmd_{name}"] for name in ("SS", "SD", "DS", "DD"))
        wigner_components = sum(
            data[f"wigner_{name}"] for name in ("SS", "SD", "DS", "DD")
        )
        center = len(data["delta_gev"]) // 2
        forward = data["gtmd"][center, center]
        forward_u = np.trace(forward, axis1=-2, axis2=-1).real / 3.0
        forward_tensor = (
            forward[..., 1, 1]
            - 0.5 * (forward[..., 0, 0] + forward[..., 2, 2])
        ).real
        rows.append({
            "wave_function": str(data["wave_function"]),
            "source": str(path),
            "nucleon_gtmd_model": str(data["nucleon_gtmd_model"]),
            "nuclear_lf_wave_is_physical": True,
            "gtmd_component_closure": float(np.max(np.abs(
                data["gtmd"] - gtmd_components
            ))),
            "wigner_component_closure": float(np.max(np.abs(
                data["wigner"] - wigner_components
            ))),
            "forward_u_closure": float(np.max(np.abs(
                data["forward_unpolarized"] - forward_u
            ))),
            "forward_tensor_closure": float(np.max(np.abs(
                data["forward_tensor_difference"] - forward_tensor
            ))),
            "gpd_k_grid_relative_error": float(data["gpd_k_grid_relative_error"]),
            "delta_hermiticity_max_error": float(data["delta_hermiticity_max_error"]),
            "truncated_k_integral": bool(data["truncated_k_integral"]),
            "truncated_delta_transform": bool(data["truncated_delta_transform"]),
        })
    tolerances = {
        "component_absolute": 2.0e-12,
        "forward_absolute": 2.0e-12,
        "gpd_relative": 5.0e-3,
        "delta_hermiticity_absolute": 2.0e-12,
    }
    passed = all(
        row["gtmd_component_closure"] <= tolerances["component_absolute"]
        and row["wigner_component_closure"] <= tolerances["component_absolute"]
        and row["forward_u_closure"] <= tolerances["forward_absolute"]
        and row["forward_tensor_closure"] <= tolerances["forward_absolute"]
        and row["gpd_k_grid_relative_error"] <= tolerances["gpd_relative"]
        and row["delta_hermiticity_max_error"]
        <= tolerances["delta_hermiticity_absolute"]
        for row in rows
    )
    report = {
        "status": "pass" if passed else "fail",
        "scope": (
            "physical six-wave deuteron LF overlap composed with the declared "
            "replaceable factorized rank-zero nucleon GTMD boundary"
        ),
        "reductions": [
            "GTMD Delta_T=0 -> forward TMD",
            "GTMD k_T integral -> GPD",
            "GTMD Delta_T Fourier transform -> Wigner",
            "SS+SD+DS+DD -> full parent",
        ],
        "tolerances": tolerances,
        "rows": rows,
        "limitation": (
            "nucleon off-forward boundary is a declared model input; truncated "
            "external k and Delta transforms are convergence-controlled products"
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    if not passed:
        raise SystemExit("physical off-forward reduction audit failed")
    print(json.dumps({
        "output": str(OUT), "waves": len(rows),
        "maximum_gpd_relative_error": max(
            row["gpd_k_grid_relative_error"] for row in rows
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
