"""Semantic replay and dependency-integrity utilities for C400.S2.

The P1C replay treated generator exit code zero as sufficient and reported a
hard-coded C64 dependency for every exception.  This module records the actual
exception object/path and compares eigensystems through stable mathematical
invariants rather than raw floating-array hashes.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import os
from pathlib import Path
import re
from typing import Any, Mapping, Sequence, Tuple

import numpy as np

from .state_identity import DiagnosticSpectrum


class ReplayIntegrityError(ValueError):
    """Raised when a replay record violates the versioned C400.S2 contract."""


_PATH_PATTERN = re.compile(
    r"(?P<path>(?:[A-Za-z]:)?(?:[/\\][^\s'\"<>:]+)+|(?:data|docs|src|tests|tools)/[^\s'\"<>:]+)"
)


@dataclass(frozen=True)
class DependencyFailure:
    status: str
    exception_type: str
    message: str
    first_missing_path: str | None
    candidate_paths: Tuple[str, ...]
    source: str
    hardcoded_substitution_used: bool = False


@dataclass(frozen=True)
class EigenClusterComparison:
    indices: Tuple[int, ...]
    reference_eigenvalues: Tuple[float, ...]
    candidate_eigenvalues: Tuple[float, ...]
    maximum_eigenvalue_difference: float
    singular_values: Tuple[float, ...]
    principal_angles_rad: Tuple[float, ...]
    projector_frobenius_distance: float
    singleton_overlap: float | None
    pass_eigenvalues: bool
    pass_subspace: bool


@dataclass(frozen=True)
class EigensystemComparison:
    status: str
    pass_all: bool
    reference_count: int
    candidate_count: int
    clusters: Tuple[EigenClusterComparison, ...]
    maximum_reference_residual: float
    maximum_candidate_residual: float
    residuals_pass: bool
    raw_vector_hashes_compared: bool = False
    physical_state_claim: bool = False


def _normalize_path(value: str, repository_root: Path | None) -> str:
    cleaned = value.strip().rstrip(".,;)\"]}")
    path = Path(cleaned).expanduser()
    if repository_root is not None:
        try:
            return path.resolve(strict=False).relative_to(repository_root.resolve(strict=False)).as_posix()
        except (ValueError, OSError):
            pass
    return path.as_posix()


def dependency_failure_record(
    error: BaseException,
    *,
    repository_root: str | Path | None = None,
) -> DependencyFailure:
    """Record the concrete exception and first path it actually names.

    ``FileNotFoundError.filename`` is authoritative when present.  Other error
    messages are scanned for source-like paths in encounter order.  No fallback
    dependency name is manufactured.
    """

    root = Path(repository_root).expanduser() if repository_root is not None else None
    raw_message = str(error)
    message = raw_message
    if root is not None:
        # Generated replay records must not depend on the checkout's absolute
        # directory.  The first missing object remains exact and repository-
        # relative below; the human-readable message uses a stable placeholder.
        root_variants = {
            str(root),
            str(root.resolve(strict=False)),
            root.as_posix(),
            root.resolve(strict=False).as_posix(),
        }
        for root_text in sorted(root_variants, key=len, reverse=True):
            if root_text:
                message = message.replace(root_text, "<REPOSITORY_ROOT>")
    candidates: list[str] = []
    filename = getattr(error, "filename", None)
    if filename:
        candidates.append(_normalize_path(str(filename), root))
    for match in _PATH_PATTERN.finditer(raw_message):
        normalized = _normalize_path(match.group("path"), root)
        if normalized not in candidates:
            candidates.append(normalized)
    first = candidates[0] if candidates else None
    return DependencyFailure(
        status="ACTUAL_EXCEPTION_RECORDED" if first else "EXCEPTION_WITHOUT_PATH_RECORDED",
        exception_type=type(error).__name__,
        message=message,
        first_missing_path=first,
        candidate_paths=tuple(candidates),
        source="caught exception; no hard-coded dependency substitution",
    )


def _validate_eigensystem(
    eigenvalues: Sequence[float],
    vectors: np.ndarray,
    residuals: Sequence[float],
    *,
    label: str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    values = np.asarray(eigenvalues, dtype=float)
    matrix = np.asarray(vectors, dtype=np.complex128)
    residual_array = np.asarray(residuals, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
        raise ReplayIntegrityError(f"{label} eigenvalues must be a nonempty finite vector")
    if matrix.ndim != 2 or matrix.shape[1] != values.size or not np.all(np.isfinite(matrix)):
        raise ReplayIntegrityError(f"{label} eigenvector matrix shape/content is invalid")
    if residual_array.shape != values.shape or not np.all(np.isfinite(residual_array)):
        raise ReplayIntegrityError(f"{label} residuals must match the eigenvalue shape")
    norms = np.linalg.norm(matrix, axis=0)
    if np.any(norms == 0.0):
        raise ReplayIntegrityError(f"{label} contains a zero eigenvector")
    matrix = matrix / norms
    gram = matrix.conj().T @ matrix
    if float(np.linalg.norm(gram - np.eye(values.size))) > 1.0e-6:
        raise ReplayIntegrityError(f"{label} eigenvectors are not orthonormal within tolerance")
    order = np.argsort(values, kind="stable")
    return values[order], matrix[:, order], residual_array[order]


def _clusters(
    reference_values: np.ndarray,
    candidate_values: np.ndarray,
    degeneracy_tolerance: float,
) -> Tuple[Tuple[int, ...], ...]:
    if degeneracy_tolerance < 0.0:
        raise ReplayIntegrityError("degeneracy_tolerance must be nonnegative")
    count = reference_values.size
    adjacency = {index: set() for index in range(count)}
    for index in range(count - 1):
        ref_close = abs(reference_values[index + 1] - reference_values[index]) <= degeneracy_tolerance
        cand_close = abs(candidate_values[index + 1] - candidate_values[index]) <= degeneracy_tolerance
        if ref_close or cand_close:
            adjacency[index].add(index + 1)
            adjacency[index + 1].add(index)
    groups: list[Tuple[int, ...]] = []
    seen: set[int] = set()
    for start in range(count):
        if start in seen:
            continue
        stack = [start]
        component: list[int] = []
        while stack:
            index = stack.pop()
            if index in seen:
                continue
            seen.add(index)
            component.append(index)
            stack.extend(adjacency[index] - seen)
        groups.append(tuple(sorted(component)))
    return tuple(groups)


def compare_eigensystems(
    reference_eigenvalues: Sequence[float],
    reference_vectors: np.ndarray,
    reference_residuals: Sequence[float],
    candidate_eigenvalues: Sequence[float],
    candidate_vectors: np.ndarray,
    candidate_residuals: Sequence[float],
    *,
    eigenvalue_atol: float = 1.0e-8,
    eigenvalue_rtol: float = 1.0e-8,
    residual_tolerance: float = 1.0e-7,
    degeneracy_tolerance: float = 1.0e-7,
    singleton_overlap_minimum: float = 0.999,
    subspace_singular_value_minimum: float = 0.999,
    projector_tolerance: float = 1.0e-5,
) -> EigensystemComparison:
    """Compare eigensystems through phase/subspace-invariant quantities.

    Singleton states are compared by absolute overlap, which is phase
    invariant.  Degenerate clusters are compared by principal angles and
    spectral-projector distance, so unitary rotations inside the cluster do not
    cause a false replay failure.
    """

    ref_values, ref_vectors, ref_residuals = _validate_eigensystem(
        reference_eigenvalues, reference_vectors, reference_residuals, label="reference"
    )
    cand_values, cand_vectors, cand_residuals = _validate_eigensystem(
        candidate_eigenvalues, candidate_vectors, candidate_residuals, label="candidate"
    )
    if ref_values.size != cand_values.size or ref_vectors.shape[0] != cand_vectors.shape[0]:
        return EigensystemComparison(
            status="EIGENSYSTEM_DIMENSION_MISMATCH",
            pass_all=False,
            reference_count=int(ref_values.size),
            candidate_count=int(cand_values.size),
            clusters=(),
            maximum_reference_residual=float(np.max(ref_residuals)),
            maximum_candidate_residual=float(np.max(cand_residuals)),
            residuals_pass=False,
        )
    if min(eigenvalue_atol, eigenvalue_rtol, residual_tolerance, singleton_overlap_minimum,
           subspace_singular_value_minimum, projector_tolerance) < 0.0:
        raise ReplayIntegrityError("comparison tolerances must be nonnegative")

    comparisons: list[EigenClusterComparison] = []
    for indices in _clusters(ref_values, cand_values, degeneracy_tolerance):
        idx = np.asarray(indices, dtype=int)
        ref_basis = ref_vectors[:, idx]
        cand_basis = cand_vectors[:, idx]
        ref_projector = ref_basis @ ref_basis.conj().T
        cand_projector = cand_basis @ cand_basis.conj().T
        singular_values = np.clip(
            np.real(np.linalg.svd(ref_basis.conj().T @ cand_basis, compute_uv=False)), 0.0, 1.0
        )
        angles = np.arccos(singular_values)
        eigenvalue_difference = np.abs(ref_values[idx] - cand_values[idx])
        eigenvalue_limit = eigenvalue_atol + eigenvalue_rtol * np.maximum(
            np.abs(ref_values[idx]), np.abs(cand_values[idx])
        )
        pass_eigenvalues = bool(np.all(eigenvalue_difference <= eigenvalue_limit))
        projector_distance = float(np.linalg.norm(ref_projector - cand_projector))
        singleton_overlap = float(singular_values[0]) if len(indices) == 1 else None
        if len(indices) == 1:
            pass_subspace = bool(singleton_overlap >= singleton_overlap_minimum)
        else:
            pass_subspace = bool(
                np.min(singular_values) >= subspace_singular_value_minimum
                and projector_distance <= projector_tolerance
            )
        comparisons.append(
            EigenClusterComparison(
                indices=indices,
                reference_eigenvalues=tuple(float(ref_values[i]) for i in indices),
                candidate_eigenvalues=tuple(float(cand_values[i]) for i in indices),
                maximum_eigenvalue_difference=float(np.max(eigenvalue_difference)),
                singular_values=tuple(float(value) for value in singular_values),
                principal_angles_rad=tuple(float(value) for value in angles),
                projector_frobenius_distance=projector_distance,
                singleton_overlap=singleton_overlap,
                pass_eigenvalues=pass_eigenvalues,
                pass_subspace=pass_subspace,
            )
        )

    max_ref_residual = float(np.max(ref_residuals))
    max_cand_residual = float(np.max(cand_residuals))
    residuals_pass = max(max_ref_residual, max_cand_residual) <= residual_tolerance
    passed = residuals_pass and all(row.pass_eigenvalues and row.pass_subspace for row in comparisons)
    return EigensystemComparison(
        status="SEMANTIC_EIGENSYSTEM_REPLAY_PASS" if passed else "SEMANTIC_EIGENSYSTEM_REPLAY_FAIL",
        pass_all=passed,
        reference_count=int(ref_values.size),
        candidate_count=int(cand_values.size),
        clusters=tuple(comparisons),
        maximum_reference_residual=max_ref_residual,
        maximum_candidate_residual=max_cand_residual,
        residuals_pass=residuals_pass,
    )


def compare_diagnostic_spectra(
    reference: DiagnosticSpectrum,
    candidate: DiagnosticSpectrum,
    **tolerances: Any,
) -> EigensystemComparison:
    if reference.resolution != candidate.resolution:
        raise ReplayIntegrityError("diagnostic spectrum resolutions differ")
    if reference.matrix_shape != candidate.matrix_shape:
        raise ReplayIntegrityError("diagnostic spectrum matrix shapes differ")
    reference_vectors = np.column_stack([pair.state.vector for pair in reference.eigenpairs])
    candidate_vectors = np.column_stack([pair.state.vector for pair in candidate.eigenpairs])
    return compare_eigensystems(
        [pair.state.eigenvalue for pair in reference.eigenpairs],
        reference_vectors,
        [pair.eigenvalue_residual for pair in reference.eigenpairs],
        [pair.state.eigenvalue for pair in candidate.eigenpairs],
        candidate_vectors,
        [pair.eigenvalue_residual for pair in candidate.eigenpairs],
        **tolerances,
    )


def semantic_replay_record(
    reference: DiagnosticSpectrum,
    candidate: DiagnosticSpectrum,
    *,
    dependency_reference: DependencyFailure | None = None,
    dependency_candidate: DependencyFailure | None = None,
    command: Sequence[str] = (),
    environment: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    comparison = compare_diagnostic_spectra(reference, candidate)
    dependency_match: bool | None
    if dependency_reference is None and dependency_candidate is None:
        dependency_match = None
    elif dependency_reference is None or dependency_candidate is None:
        dependency_match = False
    else:
        dependency_match = (
            dependency_reference.exception_type == dependency_candidate.exception_type
            and dependency_reference.first_missing_path == dependency_candidate.first_missing_path
        )
    pass_all = comparison.pass_all and dependency_match is not False
    return {
        "schema": "C400-S2-SEMANTIC-REPLAY-V1",
        "status": "FOCUSED_PHASE_SEMANTIC_REPLAY_PASS" if pass_all else "FOCUSED_PHASE_SEMANTIC_REPLAY_FAIL",
        "eigensystem": asdict(comparison),
        "dependency_reference": asdict(dependency_reference) if dependency_reference else None,
        "dependency_candidate": asdict(dependency_candidate) if dependency_candidate else None,
        "dependency_match": dependency_match,
        "command": tuple(str(item) for item in command),
        "environment": dict(environment or {}),
        "raw_eigenvector_hashes_compared": False,
        "full_historical_chain_replay_claim": False,
        "physical_state_claim": False,
        "pass": pass_all,
    }


__all__ = [
    "ReplayIntegrityError",
    "DependencyFailure",
    "EigenClusterComparison",
    "EigensystemComparison",
    "dependency_failure_record",
    "compare_eigensystems",
    "compare_diagnostic_spectra",
    "semantic_replay_record",
]
