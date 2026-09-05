"""Truthful diagnostic eigenstate and sector-projection interfaces for C400.S2."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Mapping, Optional, Sequence, Tuple

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh

from .derivative_integrity import (
    corrected_derivative,
    diagnostic_record,
    operator_matrix,
    shifted_record,
)
from .tracking import StateRecord, StateTracker, TrackingPolicy


class StateIdentityError(ValueError):
    """Raised when a diagnostic state or projector violates explicit invariants."""


UNPROJECTED_STATUS = "UNPROJECTED_DIAGNOSTIC_EIGENPAIR"
PROJECTED_STATUS = "PROJECTED_SECTOR_EIGENPAIR_VERIFIED"
PROJECTED_RITZ_STATUS = "PROJECTED_SUBSPACE_RITZ_PAIR_ONLY"


@dataclass(frozen=True)
class SectorProjector:
    owner: str
    requested_sector: Tuple[Tuple[str, str], ...]
    matrix: np.ndarray
    tolerance: float = 1.0e-10
    hamiltonian_invariance_tolerance: float = 1.0e-8

    def __post_init__(self) -> None:
        if not self.owner.strip() or not self.requested_sector:
            raise StateIdentityError("projector owner and requested sector are required")
        matrix = np.asarray(self.matrix, dtype=np.complex128)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            raise StateIdentityError("sector projector must be square")
        if not np.all(np.isfinite(matrix)):
            raise StateIdentityError("sector projector must be finite")
        if self.tolerance <= 0.0 or self.hamiltonian_invariance_tolerance <= 0.0:
            raise StateIdentityError(
                "projector and Hamiltonian-invariance tolerances must be positive"
            )
        hermitian = float(np.linalg.norm(matrix - matrix.conj().T))
        idempotent = float(np.linalg.norm(matrix @ matrix - matrix))
        if hermitian > self.tolerance or idempotent > self.tolerance:
            raise StateIdentityError(
                f"invalid sector projector: Hermiticity residual={hermitian}, idempotence residual={idempotent}"
            )
        frozen = np.array(matrix, copy=True)
        frozen.setflags(write=False)
        object.__setattr__(self, "matrix", frozen)
        object.__setattr__(self, "requested_sector", tuple(sorted(tuple(self.requested_sector))))


@dataclass(frozen=True)
class DiagnosticEigenpair:
    state: StateRecord
    identity_status: str
    requested_sector: Tuple[Tuple[str, str], ...] | None
    projector_owner: str | None
    quantum_number_evidence: str
    projection_norm: float | None
    projection_leakage: float | None
    projector_residual: float | None
    eigenvalue_residual: float
    relative_eigenvalue_residual: float
    spectral_status: str
    projector_membership_verified: bool | None
    full_eigenstate_verified: bool
    phase_convention: str
    degeneracy_gap: float
    degeneracy_status: str
    vector_sha256_incidental: str


@dataclass(frozen=True)
class DiagnosticSpectrum:
    resolution: str
    parameter_root: str
    matrix_shape: Tuple[int, int]
    matrix_nnz: int
    hermiticity_residual: float
    solver_tolerance: float
    eigenpairs: Tuple[DiagnosticEigenpair, ...]
    projected: bool
    projector_invariance_residual: float | None
    projector_relative_invariance_residual: float | None
    projector_invariant_subspace: bool | None
    physical_state_selected: bool = False
    C396_19_coordinate_state: bool = False


def _phase_fix(vector: np.ndarray) -> np.ndarray:
    index = int(np.argmax(np.abs(vector)))
    phase = vector[index] / abs(vector[index]) if abs(vector[index]) else 1.0 + 0.0j
    fixed = np.asarray(vector * np.conjugate(phase), dtype=np.complex128)
    fixed /= np.linalg.norm(fixed)
    fixed = np.array(fixed, copy=True)
    fixed.setflags(write=False)
    return fixed


def _eigensolve(matrix: csr_matrix | np.ndarray, *, k: int, tolerance: float) -> tuple[np.ndarray, np.ndarray]:
    dimension = matrix.shape[0]
    if k <= 0 or k > dimension:
        raise StateIdentityError("require 0 < k <= matrix dimension")
    if tolerance <= 0.0:
        raise StateIdentityError("solver tolerance must be positive")
    if isinstance(matrix, np.ndarray) or k == dimension or dimension <= max(32, 4 * k):
        values, vectors = eigh(np.asarray(matrix, dtype=np.complex128))
        return values[:k], vectors[:, :k]
    start = np.ones(dimension, dtype=np.complex128)
    start /= np.linalg.norm(start)
    values, vectors = eigsh(
        matrix,
        k=k,
        which="SA",
        tol=tolerance,
        maxiter=20_000,
        ncv=min(dimension - 1, max(4 * k + 1, 100)),
        v0=start,
    )
    order = np.argsort(values)
    return values[order], vectors[:, order]


def _projector_basis(projector: SectorProjector) -> np.ndarray:
    values, vectors = eigh(projector.matrix)
    mask = values > 0.5
    basis = vectors[:, mask]
    if basis.shape[1] == 0:
        raise StateIdentityError("sector projector has zero-dimensional range")
    return basis


def solve_c144_diagnostic(
    resolution: str = "K9",
    *,
    parameter_record: Mapping[str, Any] | None = None,
    k: int = 2,
    solver_tolerance: float = 1.0e-9,
    projector: SectorProjector | None = None,
) -> DiagnosticSpectrum:
    """Solve the nonphysical C144 fixture without inventing sector identity."""

    record = diagnostic_record(resolution) if parameter_record is None else parameter_record
    hamiltonian = operator_matrix(resolution, record)
    hermitian_delta = hamiltonian - hamiltonian.getH()
    hermiticity = float(np.max(np.abs(hermitian_delta.data))) if hermitian_delta.nnz else 0.0

    projected = projector is not None
    projector_invariance_residual: float | None = None
    projector_relative_invariance_residual: float | None = None
    projector_invariant_subspace: bool | None = None
    if projector is None:
        values, vectors = _eigensolve(hamiltonian, k=k, tolerance=solver_tolerance)
        basis = None
    else:
        if projector.matrix.shape != hamiltonian.shape:
            raise StateIdentityError("sector projector dimension does not match Hamiltonian")
        basis = _projector_basis(projector)
        h_basis = np.asarray(hamiltonian @ basis, dtype=np.complex128)
        in_range = basis @ (basis.conj().T @ h_basis)
        projector_invariance_residual = float(np.linalg.norm(h_basis - in_range))
        projector_invariance_scale = max(
            float(np.linalg.norm(h_basis)), np.finfo(float).tiny
        )
        projector_relative_invariance_residual = (
            projector_invariance_residual / projector_invariance_scale
        )
        projector_invariant_subspace = bool(
            projector_relative_invariance_residual
            <= projector.hamiltonian_invariance_tolerance
        )
        restricted = basis.conj().T @ h_basis
        values, subspace_vectors = _eigensolve(
            np.asarray(restricted, dtype=np.complex128),
            k=min(k, restricted.shape[0]),
            tolerance=solver_tolerance,
        )
        vectors = basis @ subspace_vectors

    pairs: list[DiagnosticEigenpair] = []
    for index in range(vectors.shape[1]):
        vector = _phase_fix(vectors[:, index])
        eigenvalue = float(np.real_if_close(values[index]))
        h_vector = np.asarray(hamiltonian @ vector, dtype=np.complex128)
        residual = float(np.linalg.norm(h_vector - eigenvalue * vector))
        residual_scale = max(
            float(np.linalg.norm(h_vector)),
            abs(eigenvalue) * float(np.linalg.norm(vector)),
            np.finfo(float).tiny,
        )
        relative_residual = residual / residual_scale
        residual_verified = bool(
            relative_residual <= max(100.0 * solver_tolerance, 1.0e-10)
        )
        gaps = [abs(eigenvalue - float(np.real_if_close(other))) for j, other in enumerate(values) if j != index]
        gap = min(gaps, default=float("inf"))
        if projector is None:
            sector = (("basis_scope", "C144_UNPROJECTED_FIXTURE"),)
            identity_status = UNPROJECTED_STATUS
            projection_norm = projection_leakage = projector_residual = None
            projector_membership_verified = None
            requested_sector = None
            owner = None
            quantum_number_evidence = "none; unprojected C144 fixture basis only"
            spectral_status = (
                "FULL_SPACE_EIGENPAIR_VERIFIED"
                if residual_verified
                else "FULL_SPACE_EIGENPAIR_RESIDUAL_FAILED"
            )
            full_eigenstate_verified = residual_verified
        else:
            projected_vector = projector.matrix @ vector
            projection_norm = float(np.linalg.norm(projected_vector))
            projection_leakage = float(np.linalg.norm(vector - projected_vector))
            projector_residual = float(
                np.linalg.norm(projector.matrix @ projected_vector - projected_vector)
            )
            projector_membership_verified = bool(
                projection_leakage <= projector.tolerance
                and projector_residual <= projector.tolerance
            )
            sector = projector.requested_sector
            requested_sector = projector.requested_sector
            owner = projector.owner
            full_eigenstate_verified = bool(
                projector_membership_verified
                and projector_invariant_subspace
                and residual_verified
            )
            if full_eigenstate_verified:
                identity_status = PROJECTED_STATUS
                spectral_status = PROJECTED_STATUS
                quantum_number_evidence = (
                    "numerical Hermitian idempotent projector; Hamiltonian-invariant "
                    "projected range; full-space eigenresidual verified"
                )
            else:
                identity_status = PROJECTED_RITZ_STATUS
                spectral_status = PROJECTED_RITZ_STATUS
                quantum_number_evidence = (
                    "numerical Hermitian idempotent projector establishes projected-range "
                    "membership only; Hamiltonian-invariant sector/full eigenpair not verified"
                )
        state = StateRecord(f"{resolution}-diagnostic-{index}", sector, eigenvalue, vector)
        pairs.append(
            DiagnosticEigenpair(
                state=state,
                identity_status=identity_status,
                requested_sector=requested_sector,
                projector_owner=owner,
                quantum_number_evidence=quantum_number_evidence,
                projection_norm=projection_norm,
                projection_leakage=projection_leakage,
                projector_residual=projector_residual,
                eigenvalue_residual=residual,
                relative_eigenvalue_residual=relative_residual,
                spectral_status=spectral_status,
                projector_membership_verified=projector_membership_verified,
                full_eigenstate_verified=full_eigenstate_verified,
                phase_convention="largest-magnitude component real positive",
                degeneracy_gap=float(gap),
                degeneracy_status=(
                    "ISOLATED_WITHIN_SOLVED_SUBSPACE"
                    if gap > max(10.0 * solver_tolerance, 1.0e-10)
                    else "NEAR_DEGENERATE_WITHIN_SOLVED_SUBSPACE"
                ),
                vector_sha256_incidental=sha256(vector.tobytes()).hexdigest(),
            )
        )

    return DiagnosticSpectrum(
        resolution=resolution,
        parameter_root=str(record["root"]),
        matrix_shape=tuple(hamiltonian.shape),
        matrix_nnz=int(hamiltonian.nnz),
        hermiticity_residual=hermiticity,
        solver_tolerance=solver_tolerance,
        eigenpairs=tuple(pairs),
        projected=projected,
        projector_invariance_residual=projector_invariance_residual,
        projector_relative_invariance_residual=projector_relative_invariance_residual,
        projector_invariant_subspace=projector_invariant_subspace,
    )


def derivative_step_tolerance_scan(
    *,
    resolution: str = "K9",
    coordinate_id: str = "phi_mass",
    steps: Sequence[float] = (1.0e-3, 1.0e-4, 1.0e-5),
    solver_tolerances: Sequence[float] = (1.0e-8, 1.0e-10),
) -> Mapping[str, Any]:
    """Compare tracked eigenvalue responses over step and solver tolerances."""

    base = diagnostic_record(resolution)
    derivative = corrected_derivative(resolution, coordinate_id, record=base)
    rows: list[Mapping[str, Any]] = []
    for tolerance in solver_tolerances:
        center = solve_c144_diagnostic(
            resolution, parameter_record=base, solver_tolerance=float(tolerance), k=1
        )
        selected = center.eigenpairs[0]
        for step in steps:
            if not np.isfinite(step) or step <= 0.0:
                raise StateIdentityError("all derivative steps must be finite and positive")
            plus = solve_c144_diagnostic(
                resolution,
                parameter_record=shifted_record(base, coordinate_id, float(step)),
                solver_tolerance=float(tolerance),
                k=1,
            )
            minus = solve_c144_diagnostic(
                resolution,
                parameter_record=shifted_record(base, coordinate_id, -float(step)),
                solver_tolerance=float(tolerance),
                k=1,
            )
            tracker = StateTracker(
                TrackingPolicy(
                    overlap_minimum=0.8,
                    degeneracy_gap=max(1.0e-10, 10.0 * float(tolerance)),
                    assignment_tie_tolerance=max(1.0e-12, float(tolerance)),
                    norm_tolerance=1.0e-7,
                )
            )
            plus_match = tracker.match(
                tuple(pair.state for pair in center.eigenpairs), tuple(pair.state for pair in plus.eigenpairs)
            )
            minus_match = tracker.match(
                tuple(pair.state for pair in center.eigenpairs), tuple(pair.state for pair in minus.eigenpairs)
            )
            plus_id = dict(plus_match.assignments)[selected.state.state_id]
            minus_id = dict(minus_match.assignments)[selected.state.state_id]
            plus_energy = next(pair.state.eigenvalue for pair in plus.eigenpairs if pair.state.state_id == plus_id)
            minus_energy = next(pair.state.eigenvalue for pair in minus.eigenpairs if pair.state.state_id == minus_id)
            central = (plus_energy - minus_energy) / (2.0 * float(step))
            hf = float(np.real(np.vdot(selected.state.vector, derivative @ selected.state.vector)))
            rows.append(
                {
                    "solver_tolerance": float(tolerance),
                    "step": float(step),
                    "Hellmann_Feynman": hf,
                    "central_finite_difference": central,
                    "difference": hf - central,
                    "center_residual": selected.eigenvalue_residual,
                    "plus_min_overlap": min(row.overlap_magnitude for row in plus_match.tracked_states),
                    "minus_min_overlap": min(row.overlap_magnitude for row in minus_match.tracked_states),
                    "same_state_verified": True,
                }
            )
    return {
        "schema": "C400-S2-C144-EIGENVALUE-DERIVATIVE-SCAN-V1",
        "resolution": resolution,
        "coordinate_id": coordinate_id,
        "rows": tuple(rows),
        "single_step_certification": False,
        "physical_derivative_claim": False,
        "C396_derivative_claim": False,
    }


__all__ = [
    "StateIdentityError",
    "UNPROJECTED_STATUS",
    "PROJECTED_STATUS",
    "PROJECTED_RITZ_STATUS",
    "SectorProjector",
    "DiagnosticEigenpair",
    "DiagnosticSpectrum",
    "solve_c144_diagnostic",
    "derivative_step_tolerance_scan",
]
