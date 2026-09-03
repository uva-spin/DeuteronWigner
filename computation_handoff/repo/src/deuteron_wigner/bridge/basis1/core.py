"""Source-derived C47 BLFQ intrinsic/CM projection layer.

The implementation follows Du et al. 1911.10762v1 Eqs. (20)--(23),
(31)--(32), (46)--(54), (76)--(81), (96)--(100), and (111)--(113),
converted from their unnormalised light-front coordinates to C43's
``x^±=(x^0±x^3)/sqrt(2)`` convention.  It exposes basis maps/functionals,
never a Hamiltonian or QCD interaction matrix.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial, pi, sqrt
from pathlib import Path
from typing import Any
import json

import numpy as np
from scipy.special import eval_hermite, roots_hermite

from ..modes.core import (
    RESOLUTIONS, Resolution, array_hash, code_hash, color_triplet_projector,
    ho_labels, ho_momentum, local_overlap_kernel, zero_mode_projectors,
)

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY"
MASS_IR_GEV = 1.2


def resolutions() -> tuple[Resolution, ...]:
    return RESOLUTIONS


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def basis_hash(rows: list[tuple]) -> str:
    return sha256(canonical_json(rows).encode()).hexdigest()


def partitions(r: Resolution) -> list[tuple[Fraction, Fraction, Fraction, Fraction]]:
    """Exact qg partitions kq+kg=K, retaining only positive APBC/PBC modes."""
    out = []
    for kg_int in range(1, int(r.K) + 1):
        kg = Fraction(kg_int); kq = r.K - kg
        if kq <= 0 or kq.denominator != 2:
            continue
        out.append((kq, kg, kq / r.K, kg / r.K))
    return out


def x_map(xq: Fraction, xg: Fraction) -> dict[str, str]:
    if xq <= 0 or xg <= 0 or xq + xg != 1:
        raise ValueError("two-body fractions must be positive and sum to one")
    return {
        "q_i": "q_i=p_i/sqrt(x_i); s_i=sqrt(x_i) r_i; [s_i,q_j]=i delta_ij",
        "forward": "Q=sqrt(xq) qq+sqrt(xg) qg; qrel=sqrt(xg) qq-sqrt(xq) qg",
        "inverse": "qq=sqrt(xq) Q+sqrt(xg) qrel; qg=sqrt(xg) Q-sqrt(xq) qrel",
        "coordinate": "S=sqrt(xq) sq+sqrt(xg) sg; srel=sqrt(xg) sq-sqrt(xq) sg",
        "jacobian": "det= -1 per transverse Cartesian direction; absolute Jacobian=1",
        "fractions": f"xq={xq}; xg={xg}",
    }


def _single_cart_labels(N: int) -> list[tuple[int, int]]:
    return [(nx, N - nx) for nx in range(N + 1)]


def _polar_shell(N: int) -> list[tuple[int, int]]:
    return [(n, m) for n, m in ho_labels(N + 1) if 2 * n + abs(m) == N]


def _cart_mode(nx: int, ny: int, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Cartesian 2D-HO mode normalized under d2q/(2pi)^2 at b=1."""
    norm1 = sqrt(2.0 * sqrt(pi))
    fx = norm1 * eval_hermite(nx, x) * np.exp(-x * x / 2) / sqrt((2 ** nx) * factorial(nx))
    fy = norm1 * eval_hermite(ny, y) * np.exp(-y * y / 2) / sqrt((2 ** ny) * factorial(ny))
    return fx * fy


@lru_cache(maxsize=None)
def polar_to_cart_shell(N: int) -> np.ndarray:
    """C45-phase-aligned polar-to-Cartesian shell isometry by GH overlap."""
    polar = _polar_shell(N); cart = _single_cart_labels(N)
    nodes, weights = roots_hermite(max(28, N + 16))
    X, Y = np.meshgrid(nodes, nodes, indexing="ij")
    W = np.outer(weights, weights)
    result = np.empty((len(polar), len(cart)), dtype=np.complex128)
    for i, (n, m) in enumerate(polar):
        # GH weights carry exp(-x^2-y^2); remove that factor from the product.
        p = ho_momentum(n, m, X, Y, 1.0) * np.exp((X * X + Y * Y) / 2)
        for j, (nx, ny) in enumerate(cart):
            c = _cart_mode(nx, ny, X, Y) * np.exp((X * X + Y * Y) / 2)
            result[i, j] = np.sum(W * np.conjugate(p) * c) / (2 * pi) ** 2
    # Numerical quadrature fixes amplitudes but deterministic polar phases are
    # aligned to the largest Cartesian component.
    for i in range(len(polar)):
        j = int(np.argmax(np.abs(result[i])))
        result[i] *= np.exp(-1j * np.angle(result[i, j]))
    return result


def _one_dim_tm(n1: int, n2: int, N: int, c: float, s: float) -> float:
    """Exact binomial oscillator rotation coefficient for a1=cA+sa, a2=sA-ca."""
    n = n1 + n2 - N
    if n < 0:
        return 0.0
    total = 0.0
    for r in range(n1 + 1):
        t = N - r
        if 0 <= t <= n2:
            total += comb(n1, r) * comb(n2, t) * c ** r * s ** (n1-r+t) * (-c) ** (n2-t)
    return sqrt(factorial(N) * factorial(n) / (factorial(n1) * factorial(n2))) * total


def _cart_product_shell(Ntotal: int) -> list[tuple[int, int, int, int]]:
    out = []
    for n1x in range(Ntotal + 1):
        for n1y in range(Ntotal - n1x + 1):
            for n2x in range(Ntotal - n1x - n1y + 1):
                out.append((n1x, n1y, n2x, Ntotal - n1x - n1y - n2x))
    return out


def _polar_product_shell(Ntotal: int) -> list[tuple[int, int, int, int]]:
    out = []
    for Nq in range(Ntotal + 1):
        for nq, mq in _polar_shell(Nq):
            for ng, mg in _polar_shell(Ntotal - Nq):
                out.append((nq, mq, ng, mg))
    return out


@lru_cache(maxsize=None)
def tm_blocks(xq_num: int, xq_den: int, shell_max: int) -> tuple[tuple[tuple[int, int, int, int], np.ndarray], ...]:
    """Exact finite-shell 2D TM blocks, C47/1911 Eq. (96)."""
    xq = Fraction(xq_num, xq_den); xg = 1 - xq; c, s = sqrt(float(xq)), sqrt(float(xg))
    blocks = []
    for total in range(shell_max + 1):
        polar = _polar_product_shell(total); cart = _cart_product_shell(total)
        cprod = np.zeros((len(polar), len(cart)), dtype=np.complex128)
        for ip, (nq, mq, ng, mg) in enumerate(polar):
            Nq, Ng = 2*nq+abs(mq), 2*ng+abs(mg)
            cq = polar_to_cart_shell(Nq); cg = polar_to_cart_shell(Ng)
            qlabels, glabels = _single_cart_labels(Nq), _single_cart_labels(Ng)
            for iq, qlab in enumerate(qlabels):
                for ig, glab in enumerate(glabels):
                    try: jc = cart.index((qlab[0], qlab[1], glab[0], glab[1]))
                    except ValueError: continue
                    cprod[ip, jc] = cq[_polar_shell(Nq).index((nq,mq)), iq] * cg[_polar_shell(Ng).index((ng,mg)), ig]
        bcart = np.empty((len(cart), len(cart)), dtype=np.float64)
        for io, (Nx, Ny, nx, ny) in enumerate(cart):
            for ii, (qnx, qny, gnx, gny) in enumerate(cart):
                if qnx + gnx - Nx != nx or qny + gny - Ny != ny:
                    bcart[io, ii] = 0.0
                else:
                    bcart[io, ii] = _one_dim_tm(qnx, gnx, Nx, c, s) * _one_dim_tm(qny, gny, Ny, c, s)
        U = cprod.conj() @ bcart @ cprod.T
        blocks.append((tuple(polar), U))
    return tuple(blocks)


def tm_cm_ground_map(xq: Fraction, shell_max: int) -> tuple[list[tuple[int, int]], list[tuple[int, int, int, int]], np.ndarray]:
    """Rows of TM transformation with CM (N,M)=(0,0): product -> intrinsic."""
    rows: list[np.ndarray] = []; intrinsic: list[tuple[int,int]] = []; product: list[tuple[int,int,int,int]] = []
    blocks = tm_blocks(xq.numerator, xq.denominator, shell_max)
    offset = 0
    dimensions = [len(p) for p, _ in blocks]
    total_dim = sum(dimensions)
    for total, (labels, U) in enumerate(blocks):
        cm0_rows = [i for i, (N, M, n, m) in enumerate(labels) if N == 0 and M == 0]
        for i in cm0_rows:
            v = np.zeros(total_dim, dtype=np.complex128); v[offset:offset+len(labels)] = U[i]
            rows.append(v); intrinsic.append(labels[i][2:])
        product.extend(labels)
        offset += len(labels)
    return intrinsic, product, np.asarray(rows)


def q_basis(r: Resolution) -> list[tuple]:
    # A one-particle state carries only CM motion.  CM-ground projection leaves
    # its unique transverse ground mode; color and helicity remain open-module labels.
    return [(r.K, 0, 0, h, c, "CM_GROUND", r.label) for h in (-1, 1) for c in range(3)]


def triplet_isometry() -> np.ndarray:
    """Deterministic C45-compatible U_{3<-3x8}=T^b/sqrt(C_F)."""
    _, _, T = color_triplet_projector()
    emission = np.stack([T[b] for b in range(8)], axis=1).reshape(24, 3)
    return emission / sqrt(4.0 / 3.0)


def qg_basis(r: Resolution) -> tuple[list[tuple], list[np.ndarray], list[tuple]]:
    shell_max = r.Nmax - 2
    entries = []; maps = []; product_labels = []
    for part_id, (kq, kg, xq, xg) in enumerate(partitions(r)):
        intr, prod, u0 = tm_cm_ground_map(xq, shell_max)
        product_labels.extend([(part_id, *p) for p in prod])
        for rel_id, (n, m) in enumerate(intr):
            for hq in (-1, 1):
                for hg in (-1, 1):
                    for color in range(3):
                        entries.append((part_id, kq, kg, xq, xg, n, m, 0, 0, hq, hg, color, "CM_GROUND", r.label))
        maps.append(u0)
    return entries, maps, product_labels


def free_functional(r: Resolution, mass: float = MASS_IR_GEV) -> tuple[np.ndarray, list[tuple]]:
    """C43 invariant M^2=2P+P--Pperp^2; diagonal *functional*, not a matrix."""
    rows, _, _ = qg_basis(r); values = []
    for row in rows:
        xq, xg, n, m = row[3], row[4], row[5], row[6]
        q2_expect = r.b_GeV ** 2 * (2*n + abs(m) + 1)
        values.append(q2_expect + mass * mass / float(xq))
    return np.asarray(values, dtype=np.float64), rows


def canonical_kernel(r: Resolution, mass: float = MASS_IR_GEV) -> tuple[np.ndarray, list[tuple]]:
    """Exhaustive color/coupling-factored C47 tuple functional, not V_qg<-q."""
    qrows = q_basis(r); qgrows, _, _ = qg_basis(r); tuples = []
    for iq, (_, _, _, hp, _, _, _) in enumerate(qrows):
        for io, row in enumerate(qgrows):
            _, kq, kg, xq, xg, n, m, _, _, hq, hg, _, _, _ = row
            if Fraction(hp,2) != Fraction(hq,2) + hg + m:
                continue
            # Eq. (111) supplies m=0 contact overlap and (112)-(113) its
            # one-power transverse numerator partners. Higher |m| vanish at
            # this local one-gluon numerator scope.
            if abs(m) > 1:
                continue
            kern = local_overlap_kernel((float(kq), 0., 0.), (float(r.K), 0., 0.), (float(kg), 0., 0.), mass)
            ihq, ihp, ihg = ((0 if hq == -1 else 1), (0 if hp == -1 else 1), (0 if hg == -1 else 1))
            overlap = ((-1.)**n / sqrt(pi)) if m == 0 else ((-1.)**n * r.b_GeV * sqrt(n+1) / sqrt(pi))
            # finite-volume field normalization is retained symbolically as
            # L^(-1/2)/sqrt(2 kg); no numerical L is introduced.
            value = kern[ihq, ihp, ihg] * overlap / sqrt(2.0 * float(kg))
            tuples.append((iq, io, float(value.real), float(value.imag), "L^(-1/2)", "SB-C43-canonical;1911.10762v1-E111-E113"))
    arr = np.asarray([[a,b,c,d] for a,b,c,d,_,_ in tuples], dtype=np.float64)
    return arr, tuples


def inverse_derivative_functionals(max_k: int = 6) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Dimensionless coefficients with explicit factors L/pi and (L/pi)^2."""
    p0, q0 = zero_mode_projectors(max_k)
    k = np.arange(max_k + 1, dtype=float)
    d1 = np.zeros_like(k, dtype=np.complex128); d2 = np.zeros_like(k, dtype=np.complex128)
    d1[1:] = 1.0/(1j*k[1:]); d2[1:] = -1.0/(k[1:]**2)
    return p0, q0, np.diag(d1), np.diag(d2)


def comparison_map(source: Resolution, target: Resolution) -> tuple[np.ndarray, float]:
    """Exact common-fraction selector: nonnested qg grids have no common qg x."""
    a, _, _ = qg_basis(source); b, _, _ = qg_basis(target)
    # No nontrivial common longitudinal fraction exists for adjacent half-K
    # grids.  The exact map is therefore the zero common-support map; the
    # norm-one remainder is reported rather than interpolated away.
    return np.zeros((len(b), len(a)), dtype=np.complex128), 1.0


def validate_basis_contracts() -> dict[str, float | int | bool]:
    errs=[]; ranks=[]; dims=[]
    for r in RESOLUTIONS:
        for _, _, xq, xg in partitions(r):
            intr, _, u0 = tm_cm_ground_map(xq, r.Nmax-2)
            errs.append(float(np.linalg.norm(u0 @ u0.conj().T - np.eye(len(intr)))))
            ranks.append(int(np.linalg.matrix_rank(u0, tol=1e-10))); dims.append(len(intr))
        f, rows = free_functional(r); assert f.size == len(rows) and np.all(f > 0)
        k, tuples = canonical_kernel(r); assert k.shape[0] == len(tuples)
    p0,q0,d1,d2=inverse_derivative_functionals()
    return {"tm_cm_isometry": max(errs), "tm_cm_rank_min": min(ranks), "intrinsic_dimension_min": min(dims), "P0_idempotence": float(np.linalg.norm(p0@p0-p0)), "Q0_idempotence": float(np.linalg.norm(q0@q0-q0)), "P0Q0":float(np.linalg.norm(p0@q0)), "pv_antihermiticity":float(np.linalg.norm(d1+d1.conj().T)), "d2_hermiticity":float(np.linalg.norm(d2-d2.conj().T)), "pass": bool(max(errs)<2e-10)}


def build_runtime(runtime: Path | None = None) -> dict[str, dict[str, Any]]:
    runtime = ROOT / "data/runtime/c47_basis1" if runtime is None else Path(runtime)
    runtime.mkdir(parents=True, exist_ok=True); inventory={}
    def save(name: str, a: np.ndarray, units: str):
        p=runtime/f"{name}.npy"; np.save(p,a,allow_pickle=False); inventory[name]={"runtime_path":str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),"shape":list(a.shape),"dtype":a.dtype.str,"nnz":int(np.count_nonzero(a)),"units":units,"basis_order_hash":sha256(name.encode()).hexdigest(),"array_sha256":array_hash(a),"generator_code_sha256":code_hash()}
    for r in RESOLUTIONS:
        q=q_basis(r); qg,maps,prod=qg_basis(r); f,_=free_functional(r); k,_=canonical_kernel(r)
        save(f"q_basis_{r.label}",np.asarray([[float(x[0]),x[1],x[2],x[3],x[4]] for x in q],dtype=float),"dimensionless labels")
        save(f"qg_basis_{r.label}",np.asarray([[float(x[1]),float(x[2]),float(x[3]),float(x[4]),x[5],x[6],x[9],x[10],x[11]] for x in qg],dtype=float),"dimensionless labels")
        save(f"free_functional_{r.label}",f,"GeV^2")
        save(f"canonical_kernel_{r.label}",k,"L^(-1/2) GeV^(1+|m|)")
        for pid, m in enumerate(maps): save(f"cm_isometry_{r.label}_{pid}",m,"dimensionless")
        for pid, (_, _, xq, _) in enumerate(partitions(r)):
            for shell, (_, block) in enumerate(tm_blocks(xq.numerator, xq.denominator, r.Nmax-2)):
                save(f"tm_{r.label}_{pid}_shell{shell}", block, "dimensionless")
    p0,q0,d1,d2=inverse_derivative_functionals(); save("P0",p0,"dimensionless"); save("Q0",q0,"dimensionless"); save("inverse_d1",d1,"L/pi"); save("inverse_d2",d2,"(L/pi)^2")
    save("qg_triplet_isometry", triplet_isometry(), "dimensionless; product-color to triplet")
    for low,high in zip(RESOLUTIONS[:-1],RESOLUTIONS[1:]):
        m,rem=comparison_map(low,high); save(f"comparison_{high.label}_from_{low.label}",m,"dimensionless; exact common-support map")
    return inventory
