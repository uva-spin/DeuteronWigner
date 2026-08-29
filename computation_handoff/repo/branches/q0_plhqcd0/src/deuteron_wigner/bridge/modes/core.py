"""Executable C45 finite-projection conventions, modes, and color modules.

Authorities: Vary et al., arXiv:0905.1411v1, Eqs. (1)--(6),(14), and Li et
al., arXiv:1311.2980v1, Eqs. (7)--(12), converted to the C43 convention
``x^±=(x^0±x^3)/sqrt(2)``.  No Hamiltonian, interaction, Wilson, or TMD
matrix is represented here.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial, pi, sqrt
from pathlib import Path
from typing import Any

import numpy as np
from scipy.special import eval_genlaguerre, roots_laguerre

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C45_SOURCE_DERIVED_MODE_PROJECTION_READY"
CONVENTION_MAP_ID = "C45-C43-SQRT2-LONGITUDINAL-MAP-V1"
SOURCE_IDS = ("0905.1411v1", "1311.2980v1", "hep-ph/0011372v2")


@dataclass(frozen=True)
class Resolution:
    K: Fraction
    Nmax: int
    b_GeV: float

    @property
    def label(self) -> str:
        return f"K{self.K.numerator}_{self.K.denominator}_N{self.Nmax}_b{self.b_GeV:.2f}"


RESOLUTIONS = (
    Resolution(Fraction(9, 2), 8, 0.40),
    Resolution(Fraction(11, 2), 10, 0.45),
    Resolution(Fraction(13, 2), 12, 0.50),
)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()


def array_hash(value: np.ndarray) -> str:
    a = np.ascontiguousarray(value)
    return sha256(a.dtype.str.encode() + str(a.shape).encode() + a.tobytes()).hexdigest()


def code_hash() -> str:
    return sha256(Path(__file__).read_bytes()).hexdigest()


def longitudinal_contract() -> dict[str, Any]:
    return {
        "source": "0905.1411v1 Eqs. (4)-(6); 1311.2980v1 Eqs. (9),(12)",
        "c43_conversion": CONVENTION_MAP_ID,
        "source_coordinates": "x_B^-=x^0-x^3=sqrt(2) x_C43^-",
        "source_length_map": "BPP Eq. (4): L_BPP=sqrt(2)L_C43. For the 1311 Eq. (9) p^+=2pi k/L_1311 notation, L_1311=2 L_BPP=2sqrt(2)L_C43; both give p_C43^+=pi k/L_C43.",
        "cell": "-L <= x_C43^- <= L; total length 2L; L remains symbolic",
        "measure": "integral_{-L}^{L} dx^-",
        "mode": "phi_k(x^-)=exp(+i*pi*k*x^-/L)/sqrt(2L)",
        "fermion_boundary": "phi(x^-+2L)=-phi(x^-); k=1/2,3/2,...",
        "gluon_boundary": "phi(x^-+2L)=+phi(x^-); k=0,1,2,...; k=0 excluded from ordinary dynamical modes",
        "momenta": "p_k^+=pi*k/L; P^+=pi*K/L; x=k/K",
        "one_particle_delta": "integral dx^- phi_k^* phi_l=delta_kl",
        "large_box": "L->infinity at fixed physical p^+; K->infinity resolves x",
        "absolute_L": "SYMBOLIC_REGULATOR_PARAMETER; it cancels from x and dimensionless overlaps",
        "x_min_reconciliation": {
            "C7_record": "x_min=1/18 is EndpointRegulator.minimum_fraction, not a longitudinal mode-support identity",
            "derived_mode_minimum": {r.label: str(Fraction(1, 2) / r.K) for r in RESOLUTIONS},
            "decision": "NO_REWRITE_OF_HISTORICAL_C7_ENDPOINT_REGULATOR; C45 labels it separately from x_mode_min",
        },
    }


def longitudinal_modes(resolution: Resolution, species: str) -> list[dict[str, Any]]:
    if species not in ("QUARK", "GLUON"):
        raise ValueError("species must be QUARK or GLUON")
    if species == "QUARK":
        labels = [Fraction(2 * i + 1, 2) for i in range(int(resolution.K) + 1)]
        boundary = "ANTIPERIODIC"
    else:
        labels = [Fraction(i, 1) for i in range(1, int(resolution.K) + 1)]
        boundary = "PERIODIC_NONZERO"
    out = []
    for k in labels:
        if k > resolution.K:
            continue
        out.append({
            "k": [k.numerator, k.denominator], "species": species, "boundary": boundary,
            "p_plus": f"pi*{k}/L", "x": [ (k / resolution.K).numerator, (k / resolution.K).denominator],
            "zero_mode": False, "normalization": "1/sqrt(2L)", "resolution": resolution.label,
        })
    return out


def longitudinal_values(labels: list[Fraction], points: np.ndarray, *, phase_sign: int = 1) -> np.ndarray:
    """C43-normalized modes on dimensionless y=x^-/L points."""
    if phase_sign not in (-1, 1):
        raise ValueError("phase_sign must be +/-1")
    return np.exp(1j * phase_sign * pi * np.asarray(labels, dtype=float)[:, None] * points[None, :]) / sqrt(2.0)


def zero_mode_projectors(max_gluon_k: int) -> tuple[np.ndarray, np.ndarray]:
    if max_gluon_k < 1:
        raise ValueError("positive nonzero gluon domain required")
    p0 = np.zeros((max_gluon_k + 1, max_gluon_k + 1), dtype=np.complex128)
    p0[0, 0] = 1.0
    return p0, np.eye(max_gluon_k + 1, dtype=np.complex128) - p0


def inverse_partial_plus(labels: np.ndarray, *, L_symbolic: bool = True) -> np.ndarray:
    """PV inverse derivative in units L/pi, acting only on k != 0."""
    labels = np.asarray(labels, dtype=float)
    if np.any(labels == 0):
        values = np.zeros(labels.size, dtype=np.complex128)
        keep = labels != 0
        values[keep] = 1.0 / (1j * labels[keep])
    else:
        values = 1.0 / (1j * labels)
    return np.diag(values)


def ho_labels(Nmax: int) -> list[tuple[int, int]]:
    return [(n, m) for n in range(Nmax) for m in range(-Nmax, Nmax + 1) if 2 * n + abs(m) + 1 <= Nmax]


def ho_momentum(n: int, m: int, px: np.ndarray, py: np.ndarray, b: float, *, azimuth_sign: int = 1) -> np.ndarray:
    """Eq. (1) radial normalization converted to d^2p/(2pi)^2 measure."""
    if b <= 0 or azimuth_sign not in (-1, 1):
        raise ValueError("invalid HO scale or azimuthal phase")
    p = np.hypot(px, py); theta = np.arctan2(py, px); a = abs(m); z = (p / b) ** 2
    norm = sqrt(4.0 * pi * factorial(n) / factorial(n + a)) / b
    return norm * (p / b) ** a * np.exp(-z / 2.0) * eval_genlaguerre(n, a, z) * np.exp(1j * azimuth_sign * m * theta)


def ho_coordinate(n: int, m: int, x: np.ndarray, y: np.ndarray, b: float, *, fourier_sign: int = 1) -> np.ndarray:
    """Fourier partner under f(x)=int d2p/(2pi)^2 exp(+ip.x) f(p)."""
    if b <= 0 or fourier_sign not in (-1, 1):
        raise ValueError("invalid HO scale or Fourier phase")
    r = np.hypot(x, y); theta = np.arctan2(y, x); a = abs(m); z = (b * r) ** 2
    norm = b / sqrt(pi) * sqrt(factorial(n) / factorial(n + a))
    phase = ((-1) ** n) * (1j * fourier_sign) ** a
    return phase * norm * (b * r) ** a * np.exp(-z / 2.0) * eval_genlaguerre(n, a, z) * np.exp(1j * m * theta)


def ho_overlap(left: list[tuple[int, int]], b_left: float, right: list[tuple[int, int]], b_right: float, nodes: int = 96) -> np.ndarray:
    """Independent radial Gauss--Laguerre implementation of one-particle overlaps."""
    t, w = roots_laguerre(nodes); p = b_left * np.sqrt(t)
    out = np.zeros((len(left), len(right)), dtype=np.complex128)
    for i, (n, m) in enumerate(left):
        phi_l = ho_momentum(n, m, p, np.zeros_like(p), b_left)
        for j, (nr, mr) in enumerate(right):
            if m != mr:
                continue
            phi_r = ho_momentum(nr, mr, p, np.zeros_like(p), b_right)
            # p dp = b_left^2 dt/2.  Laguerre weights integrate e^-t; undo it.
            out[i, j] = b_left ** 2 / (4 * pi) * np.sum(w * np.conjugate(phi_l) * phi_r * np.exp(t))
    return out


def gamma_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Bjørken--Drell matrices, with C43 light-front combinations."""
    z = np.zeros((2, 2), complex); ident = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex); sz = np.array([[1, 0], [0, -1]], complex)
    g0 = np.block([[ident, z], [z, -ident]])
    return (g0, np.block([[z, sx], [-sx, z]]), np.block([[z, sy], [-sy, z]]), np.block([[z, sz], [-sz, z]]))


GAMMA = gamma_matrices()
GAMMA_PLUS = (GAMMA[0] + GAMMA[3]) / sqrt(2.0)
GAMMA_MINUS = (GAMMA[0] - GAMMA[3]) / sqrt(2.0)
LAMBDA_PLUS = GAMMA_MINUS @ GAMMA_PLUS / 2.0
LAMBDA_MINUS = GAMMA_PLUS @ GAMMA_MINUS / 2.0


def cartesian_momentum(pplus: float, px: float, py: float, mass: float) -> np.ndarray:
    if pplus <= 0 or mass <= 0:
        raise ValueError("nonzero p+ and mass required")
    pminus = (mass * mass + px * px + py * py) / (2.0 * pplus)
    return np.array([(pplus + pminus) / sqrt(2.0), px, py, (pplus - pminus) / sqrt(2.0)], float)


def spinor(pplus: float, px: float, py: float, mass: float, helicity: int, particle: str = "u") -> np.ndarray:
    """BPP Appendix D Eqs. (4.2)-(4.3), with fixed spin phase and C43 p^+."""
    if helicity not in (-1, 1) or particle not in ("u", "v"):
        raise ValueError("helicity +/-1 and particle u/v required")
    p = cartesian_momentum(pplus, px, py, mass); E = p[0]; pvec = p[1:]
    chi = np.array([1.0, 0.0], complex) if helicity == 1 else np.array([0.0, 1.0], complex)
    sigp = pvec[0] * np.array([[0, 1], [1, 0]], complex) + pvec[1] * np.array([[0, -1j], [1j, 0]], complex) + pvec[2] * np.array([[1, 0], [0, -1]], complex)
    a = sqrt(E + mass)
    if particle == "u":
        return np.concatenate((a * chi, sigp @ chi / a))
    eta = np.array([0.0, 1.0], complex) if helicity == 1 else np.array([-1.0, 0.0], complex)
    return np.concatenate((sigp @ eta / a, a * eta))


def slash(p: np.ndarray) -> np.ndarray:
    return p[0] * GAMMA[0] - p[1] * GAMMA[1] - p[2] * GAMMA[2] - p[3] * GAMMA[3]


def polarization(kplus: float, kx: float, ky: float, helicity: int) -> np.ndarray:
    """C43 A^+=0 polarization (plus, minus, x, y); epsilon^- is constrained."""
    if kplus <= 0 or helicity not in (-1, 1):
        raise ValueError("nonzero k+ and helicity +/-1 required")
    eps_t = -np.array([helicity, 1j], dtype=complex) / sqrt(2.0)
    epsminus = (kx * eps_t[0] + ky * eps_t[1]) / kplus
    return np.array([0.0, epsminus, eps_t[0], eps_t[1]], dtype=complex)


def lf_dot(a: np.ndarray, b: np.ndarray) -> complex:
    return a[0] * b[1] + a[1] * b[0] - a[2] * b[2] - a[3] * b[3]


def polarization_cartesian(eps: np.ndarray) -> np.ndarray:
    return np.array([(eps[0] + eps[1]) / sqrt(2.0), eps[2], eps[3], (eps[0] - eps[1]) / sqrt(2.0)], complex)


def local_overlap_kernel(pout: tuple[float, float, float], pin: tuple[float, float, float], k: tuple[float, float, float], mass: float) -> np.ndarray:
    """Color-free, unconserved local source-to-basis numerator samples only."""
    uout = [spinor(*pout, mass, h, "u") for h in (-1, 1)]
    uin = [spinor(*pin, mass, h, "u") for h in (-1, 1)]
    eps = [polarization(*k, h) for h in (-1, 1)]
    result = np.empty((2, 2, 2), complex)
    for i, a in enumerate(uout):
        abar = np.conjugate(a) @ GAMMA[0]
        for j, b in enumerate(uin):
            for h, e in enumerate(eps):
                ec = polarization_cartesian(np.conjugate(e))
                result[i, j, h] = abar @ sum((GAMMA[mu] * (ec[mu] if mu == 0 else -ec[mu]) for mu in range(4))) @ b
    return result


def gell_mann() -> np.ndarray:
    r3 = sqrt(3.0)
    lam = [np.array([[0,1,0],[1,0,0],[0,0,0]],complex), np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex), np.diag([1,-1,0]), np.array([[0,0,1],[0,0,0],[1,0,0]],complex), np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex), np.array([[0,0,0],[0,0,1],[0,1,0]],complex), np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex), np.diag([1/r3,1/r3,-2/r3])]
    return np.asarray(lam, dtype=complex) / 2.0


def color_triplet_projector() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    T = gell_mann(); f = np.empty((8, 8, 8), float)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                f[a, b, c] = float((-2j * np.trace((T[a] @ T[b] - T[b] @ T[a]) @ T[c])).real)
    F = -1j * f
    total = np.empty((8, 24, 24), complex)
    for a in range(8):
        total[a] = np.kron(T[a], np.eye(8)) + np.kron(np.eye(3), F[a])
    c2 = sum(g @ g for g in total)
    # 3x8=3 + 6bar + 15, with C2=4/3,10/3,16/3.
    projector = (c2 - (10.0 / 3.0) * np.eye(24)) @ (c2 - (16.0 / 3.0) * np.eye(24)) / ((4.0 / 3.0 - 10.0 / 3.0) * (4.0 / 3.0 - 16.0 / 3.0))
    return projector, total, T


def projection_contract_matrix() -> list[dict[str, str]]:
    common = {"status": "SOURCE_COMPLETE_EXECUTABLE", "conversion": CONVENTION_MAP_ID, "holdout": "C46 may assemble action matrices; C45 may not"}
    return [
        {"row": "LONGITUDINAL_CELL_AND_MEASURE", "source_authority": "0905.1411v1 Eqs. (4)-(6); 1311.2980v1 Eq. (12)", "symbolic_implementation": "longitudinal_contract/longitudinal_modes", "numerical_validation": "orthogonality, Q0 inverse derivative, rational x", **common},
        {"row": "TRANSVERSE_2D_HO_AND_PHASE", "source_authority": "0905.1411v1 Eqs. (1)-(3),(14); 1311.2980v1 Eqs. (7),(10)", "symbolic_implementation": "ho_momentum/ho_coordinate/ho_overlap", "numerical_validation": "Gauss-Laguerre Gram and overlap singular values", **common},
        {"row": "SPINOR_POLARIZATION_OVERLAP", "source_authority": "hep-ph/9705477v1 Appendix A Eqs. (1.15)-(1.23), Appendix D Eqs. (4.2)-(4.3); C43 contract", "symbolic_implementation": "spinor/polarization/local_overlap_kernel", "numerical_validation": "Dirac, completeness, gamma-plus current, gauge, transversality", **common},
        {"row": "GLOBAL_COLOR_ZERO_MODE_PROJECTION", "source_authority": "hep-ph/0011372v2 Gauss law; 1311.2980v1 color-singlet discussion following Eq. (12)", "symbolic_implementation": "color_triplet_projector/zero_mode_projectors", "numerical_validation": "Casimir, covariance, P0Q0", **common},
    ]


def library_arrays() -> dict[str, np.ndarray]:
    arrays: dict[str, np.ndarray] = {}
    y = np.linspace(-1.0, 1.0, 33, endpoint=False)
    grid = np.linspace(-2.5, 2.5, 17)
    X, Y = np.meshgrid(grid, grid, indexing="ij")
    for r in RESOLUTIONS:
        q = longitudinal_modes(r, "QUARK"); g = longitudinal_modes(r, "GLUON")
        arrays[f"longitudinal_quark_{r.label}"] = np.array([[a["k"][0] / a["k"][1], a["x"][0] / a["x"][1]] for a in q], dtype=np.float64)
        arrays[f"longitudinal_gluon_{r.label}"] = np.array([[a["k"][0], a["x"][0] / a["x"][1]] for a in g], dtype=np.float64)
        arrays[f"longitudinal_quark_values_{r.label}"] = longitudinal_values([Fraction(*a["k"]) for a in q], y)
        labels = ho_labels(r.Nmax)
        arrays[f"ho_momentum_{r.label}"] = np.asarray([ho_momentum(n, m, X, Y, r.b_GeV) for n, m in labels])
        arrays[f"ho_coordinate_{r.label}"] = np.asarray([ho_coordinate(n, m, X, Y, r.b_GeV) for n, m in labels])
    for a, b in zip(RESOLUTIONS[:-1], RESOLUTIONS[1:]):
        arrays[f"ho_overlap_{b.label}_from_{a.label}"] = ho_overlap(ho_labels(b.Nmax), b.b_GeV, ho_labels(a.Nmax), a.b_GeV)
    p0, q0 = zero_mode_projectors(int(RESOLUTIONS[-1].K))
    arrays["zero_mode_P0"] = p0; arrays["zero_mode_Q0"] = q0
    samples = [(2.0, .21, -.11), (2.3, -.18, .16)]
    arrays["u_spinors"] = np.asarray([spinor(*p, 1.2, h, q) for p in samples for q in ("u", "v") for h in (-1, 1)])
    arrays["gluon_polarizations"] = np.asarray([polarization(1.1, .19, -.13, h) for h in (-1, 1)])
    arrays["spinor_polarization_kernel"] = local_overlap_kernel((2.3, -.18, .16), (2.0, .21, -.11), (1.1, .19, -.13), 1.2)
    P, _, _ = color_triplet_projector(); arrays["qg_triplet_projector"] = P
    return arrays


def validate_library(arrays: dict[str, np.ndarray] | None = None) -> dict[str, float | bool]:
    arrays = library_arrays() if arrays is None else arrays
    p0, q0 = arrays["zero_mode_P0"], arrays["zero_mode_Q0"]
    P, total, T = color_triplet_projector(); c2 = sum(g @ g for g in total)
    spin = arrays["u_spinors"]
    g0 = GAMMA[0]; spin_res = max(abs((np.conjugate(s) @ g0 @ s).real - (2.4 if i % 4 < 2 else -2.4)) for i, s in enumerate(spin))
    pplus, px, py, mass = 2.0, .21, -.11, 1.2
    pcart = cartesian_momentum(pplus, px, py, mass)
    us = [spinor(pplus, px, py, mass, h, "u") for h in (-1, 1)]
    vs = [spinor(pplus, px, py, mass, h, "v") for h in (-1, 1)]
    udirac = max(np.linalg.norm((slash(pcart) - mass * np.eye(4)) @ u) for u in us)
    vdirac = max(np.linalg.norm((slash(pcart) + mass * np.eye(4)) @ v) for v in vs)
    ucomplete = np.linalg.norm(sum(np.outer(u, np.conjugate(u) @ g0) for u in us) - (slash(pcart) + mass * np.eye(4)))
    vcomplete = np.linalg.norm(sum(np.outer(v, np.conjugate(v) @ g0) for v in vs) - (slash(pcart) - mass * np.eye(4)))
    current = max(abs(np.conjugate(u) @ g0 @ GAMMA_PLUS @ u - 2 * pplus) for u in us)
    projector = np.linalg.norm(LAMBDA_PLUS + LAMBDA_MINUS - np.eye(4))
    eps = arrays["gluon_polarizations"]; k = np.array([1.1, (.19**2 + (-.13)**2)/(2*1.1), .19, -.13])
    trans = max(abs(lf_dot(k, e)) for e in eps)
    pol_norm = max(abs(lf_dot(np.conjugate(e), e) + 1) for e in eps)
    gram_res = max(float(np.linalg.norm(ho_overlap(ho_labels(r.Nmax), r.b_GeV, ho_labels(r.Nmax), r.b_GeV) - np.eye(len(ho_labels(r.Nmax))))) for r in RESOLUTIONS)
    return {
        "p0_idempotence": float(np.linalg.norm(p0 @ p0 - p0)), "q0_idempotence": float(np.linalg.norm(q0 @ q0 - q0)), "p0q0": float(np.linalg.norm(p0 @ q0)),
        "triplet_idempotence": float(np.linalg.norm(P @ P - P)), "triplet_hermiticity": float(np.linalg.norm(P - P.conj().T)), "triplet_rank": int(np.linalg.matrix_rank(P, tol=1e-10)),
        "triplet_casimir": float(np.linalg.norm((c2 - 4.0/3.0*np.eye(24)) @ P)), "triplet_covariance": float(max(np.linalg.norm(g @ P - P @ g) for g in total)),
        "spinor_norm": float(spin_res), "spinor_dirac": float(max(udirac, vdirac)), "spinor_completeness": float(max(ucomplete, vcomplete)), "spinor_current": float(current), "good_projector": float(projector),
        "polarization_transversality": float(trans), "polarization_norm": float(pol_norm), "ho_gram": float(gram_res),
        "pass": bool(max(gram_res, trans, pol_norm, spin_res, udirac, vdirac, ucomplete, vcomplete, current, projector, np.linalg.norm(P@P-P), np.linalg.norm(P-P.conj().T), np.linalg.norm((c2-4/3*np.eye(24))@P)) < 2e-10 and np.linalg.matrix_rank(P, tol=1e-10) == 3),
    }


def build_library(runtime: Path | None = None) -> dict[str, dict[str, Any]]:
    runtime = ROOT / "data/runtime/c45_modes" if runtime is None else Path(runtime)
    runtime.mkdir(parents=True, exist_ok=True)
    out = {}
    for name, array in sorted(library_arrays().items()):
        path = runtime / f"{name}.npy"; np.save(path, array, allow_pickle=False)
        out[name] = {"runtime_path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path), "shape": list(array.shape), "dtype": array.dtype.str, "array_sha256": array_hash(array), "basis_order_hash": sha256(name.encode()).hexdigest(), "generator_code_sha256": code_hash(), "units": "dimensionless unless mode argument explicitly carries GeV"}
    return out
