#!/usr/bin/env python3
"""Independent quasi-Monte-Carlo check of the Norfolk isoscalar OPE moment.

This intentionally does not import project current or wave-function routines.
"""

from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.special import sph_harm
from scipy.stats import qmc
from sympy.physics.wigner import clebsch_gordan


MODELS = {
    "nvia": (-0.06571, 1.2),
    "nvib": (-0.02384, 1.0),
    "nviia": (-0.04714, 1.2),
    "nviib": (-0.07947, 1.0),
}


def read_coordinate_table(path: Path):
    rows = []
    started = False
    for line in path.read_text().splitlines():
        if line.strip().startswith("r") and "du/dr" in line:
            started = True
            continue
        if not started:
            continue
        fields = line.split()
        if len(fields) != 5:
            if rows:
                break
            continue
        try:
            row = tuple(float(item.replace("D", "E")) for item in fields)
        except ValueError:
            if rows:
                break
            continue
        rows.append(row)
    array = np.asarray(rows)
    return array[:, 0], array[:, 1], array[:, 3]


def spin_matrices():
    one = np.eye(2, dtype=complex)
    pauli = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    return np.asarray([np.kron(s, one) + np.kron(one, s) for s in pauli])


def triplet_vectors():
    # Product basis: up-up, up-down, down-up, down-down.
    return {
        1: np.array([1, 0, 0, 0], complex),
        0: np.array([0, 1, 1, 0], complex) / np.sqrt(2),
        -1: np.array([0, 0, 0, 1], complex),
    }


def angular_samples(power: int):
    uv = qmc.Sobol(2, scramble=True, seed=20260724).random_base2(power)
    cosine = 2 * uv[:, 0] - 1
    phi = 2 * np.pi * uv[:, 1]
    theta = np.arccos(cosine)
    sine = np.sqrt(1 - cosine**2)
    direction = np.column_stack((sine * np.cos(phi), sine * np.sin(phi), cosine))

    triplet = triplet_vectors()
    s_part = np.broadcast_to(triplet[1] / np.sqrt(4 * np.pi), (len(uv), 4))
    d_part = np.zeros((len(uv), 4), complex)
    for ml in range(-2, 3):
        ms = 1 - ml
        if ms not in triplet:
            continue
        cg = complex(clebsch_gordan(2, 1, 1, ml, ms, 1))
        d_part += cg * sph_harm(ml, 2, phi, theta)[:, None] * triplet[ms]
    return direction, s_part, d_part


def angular_bilinears(power: int):
    direction, s_part, d_part = angular_samples(power)
    sigma = spin_matrices()
    sigma_z = sigma[2]
    sigma_r = np.einsum("ni,iab->nab", direction, sigma)
    tensor = direction[:, 2, None, None] * sigma_r

    def bilinear(left, operator, right):
        return 4 * np.pi * np.mean(
            np.einsum("na,nab,nb->n", left.conj(), operator, right).real
        )

    results = {}
    for name, operator in (("spin", sigma_z), ("tensor", tensor)):
        if operator.ndim == 2:
            operator = np.broadcast_to(operator, (len(direction), 4, 4))
        results[name] = np.array(
            [
                bilinear(s_part, operator, s_part),
                bilinear(s_part, operator, d_part)
                + bilinear(d_part, operator, s_part),
                bilinear(d_part, operator, d_part),
            ]
        )
    return results


def calculate(model: str, power: int):
    r, u, w = read_coordinate_table(Path(f"data/raw/norfolk/fdeut.{model}"))
    coefficients = angular_bilinears(power)
    d2, r_long = MODELS[model]
    hbarc = 197.3269804
    mpi = 138.039 / hbarc
    fpi = 92.4 / hbarc
    mu = mpi * r
    x = (r / r_long) ** 6 * np.exp(2 * (r - r_long) / r_long)
    cutoff = x / (1 + x)
    i1 = (
        1.29
        / (16 * np.pi)
        * mpi**2
        / fpi**2
        * d2
        * cutoff
        * (-(1 + mu) * np.exp(-mu) / mu**3)
    )
    i2 = (
        1.29
        / (16 * np.pi)
        * mpi**2
        / fpi**2
        * d2
        * cutoff
        * ((3 + 3 * mu + mu**2) * np.exp(-mu) / mu**3)
    )
    products = np.vstack((u * u, u * w, w * w))
    expectation = i1 * (coefficients["spin"] @ products)
    expectation += i2 * (coefficients["tensor"] @ products)
    # tau_1.tau_2=-3; -2 m_N/m_pi converts to nuclear magnetons.
    moment = (-2 * 938.9 / 138.039) * simpson(-3 * expectation, x=r)
    return moment, coefficients, len(r)


if __name__ == "__main__":
    for power in (10, 12, 14, 16, 18):
        values = [calculate(model, power)[0] for model in MODELS]
        print(power, *(f"{value:+.10f}" for value in values))
    moment, coefficients, points = calculate("nvia", 18)
    print("angular bilinears", coefficients, "radial points", points)
