"""Complete SU(3) invariant subspaces for H0 retained sectors."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from functools import lru_cache

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ...pilot.color import structure_constants
from ...pilot.states import _su3_generators


_REPS={
    "qqq":("3","3","3"),
    "qqqg":("3","3","3","8"),
    "qqqq-qbar":("3","3","3","3","3bar"),
}
_EXPECTED={"qqq":1,"qqqg":2,"qqqq-qbar":3}


def representation_generators(rep: str) -> tuple[np.ndarray,...]:
    fundamental=_su3_generators()
    if rep=="3": return fundamental
    if rep=="3bar": return tuple(-item.T for item in fundamental)
    f=structure_constants()
    return tuple(-1j*f[a] for a in range(8))


def _total_generators(reps: tuple[str,...]) -> tuple[np.ndarray,...]:
    dimensions=tuple(8 if rep=="8" else 3 for rep in reps)
    result=[]
    for a in range(8):
        total=np.zeros((int(np.prod(dimensions)),)*2,dtype=complex)
        for slot,rep in enumerate(reps):
            factors=[]
            for index,(label,dim) in enumerate(zip(reps,dimensions)):
                factors.append(representation_generators(label)[a] if index==slot else np.eye(dim))
            term=factors[0]
            for factor in factors[1:]: term=np.kron(term,factor)
            total+=term
        result.append(total)
    return tuple(result)


def _canonical_nullspace(matrix: np.ndarray, tolerance=2e-12) -> np.ndarray:
    _,singular,vh=np.linalg.svd(matrix,full_matrices=False)
    raw=vh[singular<tolerance].conj().T
    projector=raw@raw.conj().T
    basis=[]
    for index in range(projector.shape[0]):
        vector=projector[:,index].copy()
        for prior in basis: vector-=prior*np.vdot(prior,vector)
        norm=np.linalg.norm(vector)
        if norm>1e-9:
            vector/=norm
            pivot=np.flatnonzero(np.abs(vector)>1e-10)[0]
            vector*=np.exp(-1j*np.angle(vector[pivot]))
            basis.append(vector)
        if len(basis)==raw.shape[1]: break
    return np.column_stack(basis)


@dataclass(frozen=True)
class ColorSingletBasis:
    sector_id: str
    tensors: np.ndarray
    representation_rank: int
    deterministic_phase_convention: str = "PROJECTOR_PIVOT_POSITIVE_REAL"

    @classmethod
    @lru_cache(maxsize=None)
    def construct(cls,sector_id: str) -> "ColorSingletBasis":
        reps=_REPS[sector_id]
        total=_total_generators(reps)
        stacked=np.vstack(total)
        tensors=_canonical_nullspace(stacked)
        rank=np.linalg.matrix_rank(stacked,tol=2e-12)
        result=cls(sector_id,tensors,rank)
        result.require_complete()
        return result

    @property
    def multiplicity(self): return self.tensors.shape[1]
    @property
    def hilbert_dimension(self): return self.tensors.shape[0]

    def generator_residual(self) -> float:
        return max(float(np.max(np.abs(generator@self.tensors))) for generator in _total_generators(_REPS[self.sector_id]))

    def orthonormality_residual(self) -> float:
        return float(np.max(np.abs(self.tensors.conj().T@self.tensors-np.eye(self.multiplicity))))

    def invariant_dimension_from_rank(self) -> int:
        return self.hilbert_dimension-self.representation_rank

    def require_complete(self) -> None:
        observed=self.multiplicity
        rank_count=self.invariant_dimension_from_rank()
        if observed!=_EXPECTED[self.sector_id] or rank_count!=observed:
            raise ArchitectureError("C7.COLOR", "incomplete SU(3) invariant subspace", expected=_EXPECTED[self.sector_id], received=(observed,rank_count))

    def recoupling_matrix(self) -> np.ndarray:
        count=self.multiplicity
        omega=np.exp(2j*np.pi/count)
        return np.asarray([[omega**(i*j)/np.sqrt(count) for j in range(count)] for i in range(count)],complex)

    def recoupling_unitarity_residual(self) -> float:
        matrix=self.recoupling_matrix()
        return float(np.max(np.abs(matrix.conj().T@matrix-np.eye(self.multiplicity))))

    def content_hashes(self) -> tuple[str,...]:
        return tuple(hashlib.sha256(np.round(self.tensors[:,i],14).tobytes()).hexdigest() for i in range(self.multiplicity))

    def shaped_tensor(self,index: int) -> np.ndarray:
        dims=tuple(8 if rep=="8" else 3 for rep in _REPS[self.sector_id])
        return self.tensors[:,index].reshape(dims)


def emitted_gluon_color_amplitudes(emitter: int) -> np.ndarray:
    """Overlap t^a acting on the qqq singlet with both qqqg singlets."""
    source=ColorSingletBasis.construct("qqq").shaped_tensor(0)
    target=ColorSingletBasis.construct("qqqg")
    generators=_su3_generators()
    emitted=np.zeros((3,3,3,8),complex)
    if emitter==0:
        emitted=np.einsum("aIi,ijk->Ijka",np.asarray(generators),source)
    elif emitter==1:
        emitted=np.einsum("aJj,ijk->iJka",np.asarray(generators),source)
    elif emitter==2:
        emitted=np.einsum("aKk,ijk->ijKa",np.asarray(generators),source)
    else:
        raise IndexError(emitter)
    vector=emitted.reshape(-1)
    return target.tensors.conj().T@vector
