"""Exact and matrix-free Krylov eigenproblem oracles."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ...formal.diagnostics import ArchitectureError
from .hamiltonian import ValenceHamiltonian


@dataclass(frozen=True)
class EigenSolution:
    route: str
    hamiltonian_id: str
    basis_id: str
    eigenvalues: np.ndarray
    eigenvectors: np.ndarray
    residuals: tuple[float,...]


def _residual(matrix,value,vector):
    numerator=np.linalg.norm(matrix@vector-value*vector)
    denominator=np.linalg.norm(matrix)*np.linalg.norm(vector)+abs(value)*np.linalg.norm(vector)
    return float(numerator/denominator)


def exact_solve(hamiltonian: ValenceHamiltonian):
    values,vectors=np.linalg.eigh(hamiltonian.matrix)
    residuals=tuple(_residual(hamiltonian.matrix,v,vectors[:,i]) for i,v in enumerate(values))
    return EigenSolution("EXACT",hamiltonian.hamiltonian_id,hamiltonian.basis.basis_id,values,vectors,residuals)


def krylov_solve(hamiltonian: ValenceHamiltonian, count=3):
    try:
        from scipy.sparse.linalg import LinearOperator, eigsh
        n=hamiltonian.basis.dimension
        op=LinearOperator((n,n),matvec=hamiltonian.apply,dtype=complex)
        k=min(count,n-2)
        values,vectors=eigsh(op,k=k,which="SA",v0=np.ones(n))
        order=np.argsort(values); values=values[order]; vectors=vectors[:,order]
    except (ImportError,TypeError,ValueError):
        values,vectors=np.linalg.eigh(hamiltonian.matrix)
        values,vectors=values[:count],vectors[:,:count]
    residuals=tuple(_residual(hamiltonian.matrix,v,vectors[:,i]) for i,v in enumerate(values))
    return EigenSolution("KRYLOV",hamiltonian.hamiltonian_id,hamiltonian.basis.basis_id,values,vectors,residuals)


def require_compatible(left: EigenSolution,right: EigenSolution):
    if left.hamiltonian_id!=right.hamiltonian_id or left.basis_id!=right.basis_id:
        raise ArchitectureError("C8.SOLVER", "solver results belong to different operators", expected=(left.hamiltonian_id,left.basis_id), received=(right.hamiltonian_id,right.basis_id))
