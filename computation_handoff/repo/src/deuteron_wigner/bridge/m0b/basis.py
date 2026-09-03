"""Deterministic, color-fundamental q and qg coefficient bases for C40."""
from dataclasses import dataclass
from hashlib import sha256
import json
import numpy as np

REGULATOR = "O4-SPACELIKE-COLLINS-JMY"
IR_MASS = 0.37
RESOLUTIONS = ((17, 4, 8), (23, 6, 12), (31, 8, 16))  # K, Nq, Nqg

def array_hash(a):
    a = np.ascontiguousarray(a)
    return sha256(a.tobytes()).hexdigest()

def order_hash(table):
    return sha256(json.dumps(table, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

@dataclass(frozen=True)
class Basis:
    K: int
    q_table: tuple
    qg_table: tuple
    q_vectors: np.ndarray
    qg_vectors: np.ndarray
    Gq: np.ndarray
    Gqg: np.ndarray
    q_mass2: np.ndarray
    qg_mass2: np.ndarray

def _q_table(K, nq):
    return tuple({"flavor":"u", "color":i % 3, "helicity":-1 if i % 2 else 1,
                  "longitudinal_mode":i + 1, "radial":i % 2, "oam":(i % 3)-1,
                  "probe":"C40_COLOR_FUNDAMENTAL", "ir_mass":IR_MASS,
                  "resolution_K":K} for i in range(nq))

def _qg_table(K, nqg):
    rows=[]
    for a in range(nqg):
        qmode = a % min(4, K - 1) + 1
        gmode = K - qmode
        rows.append({"quark_mode":qmode, "gluon_mode":gmode, "quark_helicity":1 if a%2 else -1,
                     "gluon_helicity":-1 if (a//2)%2 else 1, "quark_color":a%3,
                     "adjoint_color":(2*a+1)%8, "partition":(qmode,gmode), "radial":a%2,
                     "oam":(a%3)-1, "transverse_node":a//6, "total_momentum":K, "zero_mode":False, "resolution_K":K})
    return tuple(rows)

def build_basis(K: int):
    try: nq, nqg = next((q, qg) for k,q,qg in RESOLUTIONS if k == K)
    except StopIteration: raise ValueError("C40 resolution is not declared")
    qtable, qgtable = _q_table(K,nq), _qg_table(K,nqg)
    # Coordinate arrays are the normalized coefficient-space state vectors.
    qv, qgv = np.eye(nq, dtype=np.complex128), np.eye(nqg, dtype=np.complex128)
    # Positive, explicitly mass-regulated invariant masses.
    # Nested retained modes make the free-operator refinement pilot exact;
    # resolution dependence is in the declared truncation and added modes.
    qm = IR_MASS**2 + (np.arange(nq)+1.0)**2 / 17.0
    qgm = IR_MASS**2 + (np.arange(nqg)+1.0)**2 / 17.0 + 0.21
    return Basis(K,qtable,qgtable,qv,qgv,qv.conj().T@qv,qgv.conj().T@qgv,qm,qgm)
