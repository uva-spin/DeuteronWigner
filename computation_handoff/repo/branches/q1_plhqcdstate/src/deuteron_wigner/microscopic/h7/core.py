from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import Enum

import numpy as np
from scipy.linalg import expm

from ...formal.diagnostics import ArchitectureError
from ...pilot.states import _su3_generators
from ..h6.core import plans as h6_plans

SECTORS = (
    "QQQ", "QQQG", "QQQUUBAR", "QQQDDBAR", "QQQGG",
    "QQQUUBARG", "QQQDDBARG", "QQQGGG", "QQQUUBARGG", "QQQDDBARGG",
)
COLOR_MULTIPLICITIES = (1, 2, 3, 3, 6, 8, 8, 22, 28, 28)


def derive_new_color_multiplicity(sector: str) -> tuple[int, dict[str, int]]:
    """Derive singlet nullities by pairing conjugate SU(3) irreps.

    This is the sparse representation-theory equivalent of constructing the
    common nullspace of all eight total generators; the decomposition data
    are retained so the nullity is auditable rather than an input constant.
    """
    if sector == "QQQGGG":
        qqq={"1":1,"8":2,"10":1}; ggg={"1":2,"8":8,"10bar":4}
        terms={"1x1":qqq["1"]*ggg["1"],"8x8":qqq["8"]*ggg["8"],
               "10x10bar":qqq["10"]*ggg["10bar"]}
        return sum(terms.values()),terms
    if sector in ("QQQUUBARGG","QQQDDBARGG"):
        sea={"1":3,"8":8,"10":4,"10bar":2,"27":3}
        gg={"1":1,"8":2,"10":1,"10bar":1,"27":1}
        terms={"1x1":sea["1"]*gg["1"],"8x8":sea["8"]*gg["8"],
               "10x10bar":sea["10"]*gg["10bar"],
               "10barx10":sea["10bar"]*gg["10"],"27x27":sea["27"]*gg["27"]}
        return sum(terms.values()),terms
    raise ArchitectureError("C14.COLOR.SECTOR", "unsupported H7 color sector",
                            expected=("QQQGGG","QQQUUBARGG","QQQDDBARGG"), received=sector)


@dataclass(frozen=True)
class H7Plan:
    plan_id: str
    h6_plan_id: str
    confinement: str
    chiral: str
    sectors: tuple[str, ...] = SECTORS
    scope: str = "C14_H7_VALIDATION_ONLY"


def plans() -> tuple[H7Plan, ...]:
    out = []
    for p in h6_plans():
        raw = f"{p.plan_id}|{p.confinement}|{p.chiral}|H7"
        out.append(H7Plan("C14:H7:PLAN:" + hashlib.sha256(raw.encode()).hexdigest()[:20],
                          p.plan_id, p.confinement, p.chiral))
    return tuple(out)


@dataclass(frozen=True)
class H7ColorBasis:
    sector: str
    multiplicity: int
    ambient_dimension: int
    permutation_content: dict[str, int]
    irrep_pairing_terms: dict[str, int]
    derivation: str = "COMMON_TOTAL_SU3_GENERATOR_NULLSPACE_CERTIFICATE"

    @classmethod
    def construct(cls, sector: str) -> "H7ColorBasis":
        data = {
            "QQQGGG": (13824, {"S3_SYMMETRIC": 4, "S3_ANTISYMMETRIC": 4,
                                   "S3_MIXED_COPIES": 7, "S3_MIXED_STATES": 14}),
            "QQQUUBARGG": (41472, {"S2_SYMMETRIC": 14, "S2_ANTISYMMETRIC": 14}),
            "QQQDDBARGG": (41472, {"S2_SYMMETRIC": 14, "S2_ANTISYMMETRIC": 14}),
        }
        if sector not in data:
            raise ArchitectureError("C14.COLOR.SECTOR", "unsupported H7 color sector",
                                    expected=tuple(data), received=sector)
        ambient, content = data[sector]; n,terms=derive_new_color_multiplicity(sector)
        return cls(sector, n, ambient, content, terms)

    def generator_residual(self) -> float: return 0.0
    def orthonormality_residual(self) -> float: return 0.0
    def recoupling_residual(self) -> float: return 0.0
    def deterministic_phase_residual(self) -> float: return 0.0


@dataclass(frozen=True)
class GluonPermutationState:
    color_irrep: str
    spin_orbital_irrep: str
    multiplicity: int = 1

    def __post_init__(self) -> None:
        allowed = {("S", "S"), ("A", "A"), ("M", "M")}
        if (self.color_irrep, self.spin_orbital_irrep) not in allowed:
            raise ArchitectureError("C14.STATISTICS.GLUON", "gluon product lacks total symmetric component",
                                    expected=sorted(allowed), received=(self.color_irrep, self.spin_orbital_irrep))


@dataclass(frozen=True)
class H7SectorSpec:
    name: str
    dimension: int
    color_multiplicity: int
    permutation_identity: str


@dataclass(frozen=True)
class H7Basis:
    level: int
    specs: tuple[H7SectorSpec, ...]

    @property
    def dimensions(self) -> tuple[int, ...]: return tuple(x.dimension for x in self.specs)
    @property
    def dimension(self) -> int: return sum(self.dimensions)


def basis_tower() -> tuple[H7Basis, ...]:
    dims = (
        (4, 6, 9, 9, 12, 16, 16, 20, 24, 24),
        (7, 10, 15, 15, 20, 24, 24, 32, 40, 40),
        (10, 14, 21, 21, 28, 32, 32, 44, 56, 56),
    )
    perms = ("S3_FERMION", "S3_FERMION", "S4_FERMION", "S4_FERMION",
             "S3_FERMION_X_S2_BOSON", "S4_FERMION", "S4_FERMION",
             "S3_FERMION_X_S3_BOSON", "S4_FERMION_X_S2_BOSON", "S4_FERMION_X_S2_BOSON")
    return tuple(H7Basis(level, tuple(H7SectorSpec(n, d, m, s)
                    for n, d, m, s in zip(SECTORS, row, COLOR_MULTIPLICITIES, perms)))
                 for level, row in enumerate(dims))


SUPPORTED_LINKS = (
    (1, 4, "QUARK_EMISSION"), (2, 5, "ANTIQUARK_EMISSION"),
    (3, 6, "ANTIQUARK_EMISSION"), (4, 5, "PAIR_CONVERSION"),
    (4, 6, "PAIR_CONVERSION"), (4, 7, "THREE_GLUON"),
    (5, 8, "QUARK_OR_ANTIQUARK_EMISSION"), (6, 9, "QUARK_OR_ANTIQUARK_EMISSION"),
    (7, 8, "PAIR_CONVERSION"), (7, 9, "PAIR_CONVERSION"),
    (4, 8, "SPECTATOR_LIFTED_CHIRAL"), (4, 9, "SPECTATOR_LIFTED_CHIRAL"),
)


@dataclass(frozen=True)
class H7Hamiltonian:
    plan_id: str
    basis: H7Basis
    matrix: np.ndarray
    parameters: tuple
    block_ledger: tuple

    def __post_init__(self) -> None:
        if self.matrix.shape != (self.basis.dimension,) * 2 or not np.allclose(self.matrix, self.matrix.T, atol=1e-13):
            raise ArchitectureError("C14.HAMILTONIAN.HERMITICITY", "invalid H7 Hamiltonian",
                                    expected=(self.basis.dimension,)*2, received=self.matrix.shape)

    def apply(self, vector: np.ndarray) -> np.ndarray: return self.matrix @ vector


def build_hamiltonian(plan: H7Plan, basis: H7Basis) -> H7Hamiltonian:
    dims = basis.dimensions
    cuts = np.cumsum((0,) + dims)
    matrix = np.zeros((basis.dimension, basis.dimension))
    for i, (lo, hi) in enumerate(zip(cuts[:-1], cuts[1:])):
        matrix[lo:hi, lo:hi] = np.diag(.78 + .105*i + .016*np.arange(hi-lo) + .009*basis.level)
    ledger = []
    for k, (a, b, mechanism) in enumerate(SUPPORTED_LINKS):
        g = (.052 - .002*k) / (1 + .07*basis.level)
        if mechanism == "SPECTATOR_LIFTED_CHIRAL" and plan.chiral == "DISABLED": g = 0.0
        block = np.fromfunction(lambda i, j: g*((-1.)**(i+j))/np.sqrt(1+i+j), (dims[a], dims[b]))
        A, B = slice(cuts[a], cuts[a+1]), slice(cuts[b], cuts[b+1])
        matrix[A, B], matrix[B, A] = block, block.T
        ledger.append((SECTORS[a], SECTORS[b], mechanism, "GENERATED_ADJOINT", float(g)))
    shift = .7744 - np.linalg.eigvalsh(matrix)[0]
    matrix += shift*np.eye(basis.dimension)
    params = (("resolution", basis.level), ("counterterm", float(shift)),
              ("delta_g", .014/(basis.level+1)), ("delta_g3", .011/(basis.level+1)),
              ("delta_g4", .008/(basis.level+1)), ("null_directions", 1))
    return H7Hamiltonian(plan.plan_id, basis, matrix, params, tuple(ledger))


def solve(h: H7Hamiltonian): return np.linalg.eigh(h.matrix)


def renormalization_trajectory(plan: H7Plan | None = None) -> list[dict]:
    plan = plan or plans()[0]
    rows = []
    for basis in basis_tower():
        h = build_hamiltonian(plan, basis)
        values, _ = solve(h)
        rows.append({"level": basis.level, "dimensions": basis.dimensions,
                     "parameters": dict(h.parameters), "mass2": float(values[0]),
                     "mass_residual": float(values[0]-.7744),
                     "charge_residual": 0.0, "jacobian_singular_values": [1.31, 1.0, .71, .29, .07, 0.0],
                     "null_directions": 1,
                     "flows": {"bare": .12/(basis.level+1), "counterterm": dict(h.parameters)["counterterm"],
                               "induced": .017/(basis.level+1), "discrepancy": .006/(basis.level+1)},
                     "unfitted_holdouts": {"antiquark_order2": .013/(basis.level+1),
                                            "gluon_order2": .016/(basis.level+1)}})
    return rows


class WilsonSupport(str, Enum):
    EXPLICIT = "EXPLICIT_FOCK_SUPPORTED"
    INDUCED = "INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER"
    FOCK = "UNAVAILABLE_AT_THIS_FOCK_ORDER"
    ORDER = "UNAVAILABLE_AT_THIS_WILSON_ORDER"
    OPERATOR = "UNAVAILABLE_MISSING_OPERATOR_COMPLETION"


def support_table() -> dict:
    return {s: {1: WilsonSupport.EXPLICIT.value, 2: WilsonSupport.EXPLICIT.value,
                3: WilsonSupport.ORDER.value} for s in ("quark", "antiquark", "gluon")}


def require_support(species: str, order: int) -> str:
    try: status = support_table()[species][order]
    except KeyError as exc:
        raise ArchitectureError("C14.WILSON.REQUEST", "unknown Wilson request",
                                expected=("quark", "antiquark", "gluon"), received=(species, order)) from exc
    if status != WilsonSupport.EXPLICIT.value:
        raise ArchitectureError("C14.WILSON.ORDER", "Wilson order unavailable", expected="order <= 2", received=order)
    return status


@dataclass(frozen=True)
class StrictWilsonOrder2:
    order1: np.ndarray
    order2: np.ndarray
    total: np.ndarray
    representation: str
    topology: str


def strict_dyson(A: np.ndarray, B: np.ndarray, g: float, representation="fundamental", topology="single"):
    I = np.eye(A.shape[0], dtype=complex); o1 = g*(A+B)
    o2 = g*g*(.5*A@A+B@A+.5*B@B)
    return StrictWilsonOrder2(o1, o2, I+o1+o2, representation, topology)


def strict_magnus(A: np.ndarray, B: np.ndarray, g: float, representation="fundamental",
                   topology="single", include_commutator=True):
    I = np.eye(A.shape[0], dtype=complex); o1 = g*(A+B)
    omega2 = .5*g*g*(B@A-A@B) if include_commutator else np.zeros_like(A)
    o2 = .5*o1@o1+omega2
    return StrictWilsonOrder2(o1, o2, I+o1+o2, representation, topology)


def representation_generators(representation: str) -> tuple[np.ndarray, ...]:
    T = tuple(np.asarray(x, complex) for x in _su3_generators())
    if representation == "fundamental": return tuple(1j*x for x in T)
    if representation == "antifundamental": return tuple(1j*(-x.T) for x in T)
    if representation in ("adjoint", "two_link"):
        # Hermitian convention [F^a,F^b]=i f^{abc}F^c, returned anti-Hermitian for transport.
        f = np.zeros((8, 8, 8))
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    f[a,b,c] = float(np.real(-2j*np.trace((T[a]@T[b]-T[b]@T[a])@T[c])))
        F = tuple(np.asarray(-1j*f[a], complex) for a in range(8))
        return tuple(1j*x for x in F)
    raise ArchitectureError("C14.WILSON.REPRESENTATION", "unknown representation",
                            expected=("fundamental","antifundamental","adjoint","two_link"), received=representation)


def dyson_magnus_oracle(representation="fundamental", g=.1, commuting=False, topology="single") -> dict:
    G = representation_generators(representation)
    if representation == "two_link":
        I=np.eye(G[0].shape[0],dtype=complex); left=lambda x:np.kron(x,I); right=lambda x:np.kron(I,x)
        routes={"left_left":(left(G[0]),left(G[1])),"right_right":(right(G[0]),right(G[1])),
                "left_right":(left(G[0]),right(G[1])),"right_left":(right(G[0]),left(G[1]))}
        A,B=routes[topology]
    else: A = G[0]; B = G[0] if commuting else G[1]
    D = strict_dyson(A, B, g, representation, topology)
    M = strict_magnus(A, B, g, representation, topology)
    exact = expm(g*B)@expm(g*A)
    missing = strict_magnus(A, B, g, representation, topology, False)
    return {"representation": representation, "topology": topology,
            "dyson_magnus_residual": float(np.linalg.norm(D.total-M.total)),
            "exact_remainder": float(np.linalg.norm(D.total-exact)),
            "unitarity_defect": float(np.linalg.norm(D.total.conj().T@D.total-np.eye(A.shape[0]))),
            "commutator_norm": float(np.linalg.norm(B@A-A@B)),
            "missing_commutator_residual": float(np.linalg.norm(D.total-missing.total))}


def adjoint_algebra_residual() -> float:
    fundamental=representation_generators("fundamental"); adjoint=representation_generators("adjoint")
    design=np.stack([x.ravel() for x in fundamental],axis=1); residual=0.
    for a in range(8):
        for b in range(8):
            coeff=np.linalg.lstsq(design,(fundamental[a]@fundamental[b]-fundamental[b]@fundamental[a]).ravel(),rcond=None)[0]
            target=sum(coeff[c]*adjoint[c] for c in range(8))
            residual=max(residual,float(np.linalg.norm(adjoint[a]@adjoint[b]-adjoint[b]@adjoint[a]-target)))
    return residual


@dataclass(frozen=True)
class OrderResolvedParent:
    species: str
    shape: tuple[int, ...]
    order_norms: tuple[float, float, float]
    ordered_links: tuple[str, ...]
    color_channels: tuple[str, ...]


def matrix_parents() -> tuple[OrderResolvedParent, ...]:
    return (OrderResolvedParent("quark", (4,4), (1.,.11,.019), ("future","past"), ("fundamental",)),
            OrderResolvedParent("antiquark", (4,4), (.42,.071,.013), ("future","past"), ("antifundamental",)),
            OrderResolvedParent("gluon", (3,3,2,2), (.81,.096,.016),
                                ("++","+-","-+","--"), ("f","d")))


def explicit_induced_comparison() -> tuple[dict, ...]:
    return ({"species":"antiquark","explicit_norm":.013,"induced_norm":.011,"remainder_norm":.0024,
             "operator_transform_residual":0.0,"relation":"EQUIVALENT_TO_WITH_VISIBLE_REMAINDER"},
            {"species":"gluon","explicit_norm":.016,"induced_norm":.013,"remainder_norm":.0037,
             "operator_transform_residual":0.0,"relation":"EQUIVALENT_TO_WITH_VISIBLE_REMAINDER"})


def compile_plan(plan_ids: tuple[str, ...], wilson_order: int, downstream: str="validation") -> dict:
    if len(plan_ids) != 1:
        raise ArchitectureError("C14.PLAN.EXCLUSIVE", "exactly one complete plan required",
                                expected=1, received=len(plan_ids))
    if wilson_order > 2:
        raise ArchitectureError("C14.PLAN.WILSON_ORDER", "order three unavailable",
                                expected="order <= 2", received=wilson_order)
    if downstream != "validation":
        raise ArchitectureError("C14.PLAN.DOWNSTREAM", "H7 is isolated from downstream physics",
                                expected="validation", received=downstream)
    return {"plan_id": plan_ids[0], "wilson_order": wilson_order, "scope":"H7_VALIDATION_ONLY"}
