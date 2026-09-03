#!/usr/bin/env python3
"""Independent Cartesian/FFT benchmark of the Norfolk OPE magnetic moment."""

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator

from deuteron_wigner.two_body_current import (
    _spin_operators,
    norfolk_n3lo_magnetic_moment,
    regulated_ope_radial_functions,
)
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate


def full_spin_wave(
    wave, x: np.ndarray, y: np.ndarray, z: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return stretched-deuteron ``psi`` and unit radial vectors."""

    radius = np.sqrt(x * x + y * y + z * z)
    safe_radius = np.where(radius > 0.0, radius, 1.0)
    direction = np.stack((x, y, z), axis=-1) / safe_radius[..., None]
    cosine = direction[..., 2]
    sine2 = np.maximum(0.0, 1.0 - cosine * cosine)
    phi = np.arctan2(y, x)
    y20 = np.sqrt(5.0 / (16.0 * np.pi)) * (3.0 * cosine**2 - 1.0)
    y21 = (
        -np.sqrt(15.0 / (8.0 * np.pi))
        * np.sqrt(sine2)
        * cosine
        * np.exp(1j * phi)
    )
    y22 = (
        np.sqrt(15.0 / (32.0 * np.pi))
        * sine2
        * np.exp(2j * phi)
    )

    u_interp = PchipInterpolator(wave.grid, wave.u, extrapolate=False)
    w_interp = PchipInterpolator(wave.grid, wave.w, extrapolate=False)
    query = np.clip(radius, wave.grid[0], wave.grid[-1])
    u = np.asarray(u_interp(query)) / safe_radius
    w = np.asarray(w_interp(query)) / safe_radius
    origin = radius < wave.grid[0]
    u[origin] = wave.u[0] / wave.grid[0]
    w[origin] = 0.0

    psi = np.zeros(radius.shape + (4,), dtype=np.complex128)
    psi[..., 0] = u / np.sqrt(4.0 * np.pi) + w * np.sqrt(10.0) / 10.0 * y20
    mixed = -w * np.sqrt(30.0) / 10.0 * y21 / np.sqrt(2.0)
    psi[..., 1] = mixed
    psi[..., 2] = mixed
    psi[..., 3] = w * np.sqrt(15.0) / 5.0 * y22
    return psi, direction


def fft_ope_moment(model: str, points: int, box_fm: float) -> dict[str, float]:
    wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{model}")
    spacing = box_fm / points
    axis = (np.arange(points) - points // 2) * spacing
    x, y, z = np.meshgrid(axis, axis, axis, indexing="ij")
    psi, direction = full_spin_wave(wave, x, y, z)
    radius = np.sqrt(x * x + y * y + z * z)

    pion_mass_fm = 138.039 / 197.3269804
    d2 = {
        "nvia": -0.06571,
        "nvib": -0.02384,
        "nviia": -0.04714,
        "nviib": -0.07947,
    }[model]
    shapes = [np.zeros_like(radius), np.zeros_like(radius)]
    nonzero = radius > 0.0
    evaluated = regulated_ope_radial_functions(
        radius[nonzero],
        pion_mass_fm=pion_mass_fm,
        r_long_fm=1.2 if model.endswith("a") else 1.0,
    )
    shapes[0][nonzero], shapes[1][nonzero] = evaluated
    prefactor = (
        1.29
        / (16.0 * np.pi)
        * pion_mass_fm**2
        / (92.4 / 197.3269804) ** 2
        * d2
    )
    i1, i2 = prefactor * shapes[0], prefactor * shapes[1]

    sigma_1, sigma_2 = _spin_operators()
    sigma_sum = sigma_1 + sigma_2
    spin_z_psi = np.einsum("ab,...b->...a", sigma_sum[2], psi)
    sigma_r_psi = np.einsum(
        "...i,iab,...b->...a", direction, sigma_sum, psi
    )
    operated = i1[..., None] * spin_z_psi + (
        i2 * direction[..., 2]
    )[..., None] * sigma_r_psi

    coordinate_inner = spacing**3 * np.vdot(psi, operated).real
    momentum_inner = 0.0
    for spin in range(4):
        psi_k = np.fft.fftn(psi[..., spin])
        operated_k = np.fft.fftn(operated[..., spin])
        momentum_inner += np.vdot(psi_k, operated_k).real
    momentum_inner *= spacing**3 / points**3
    conversion = (-2.0 * 938.9 / 138.039) * (-3.0)
    partial_wave = norfolk_n3lo_magnetic_moment(wave, model=model)["ope"]
    return {
        "model": model,
        "points": points,
        "box_fm": box_fm,
        "coordinate_cartesian": conversion * coordinate_inner,
        "momentum_fft": conversion * momentum_inner,
        "partial_wave": partial_wave,
        "fft_parseval_difference": conversion
        * (momentum_inner - coordinate_inner),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=("nvia", "nvib", "nviia", "nviib"), default="nvia")
    parser.add_argument("--points", type=int, default=96)
    parser.add_argument("--box-fm", type=float, default=24.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/stage0/norfolk_ope_fft_benchmark.json"),
    )
    arguments = parser.parse_args()
    result = fft_ope_moment(arguments.model, arguments.points, arguments.box_fm)
    arguments.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
