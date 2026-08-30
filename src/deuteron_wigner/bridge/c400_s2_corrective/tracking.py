"""Sector-exact, ambiguity-aware state tracking for C400 diagnostics.

This implementation is independent of the P1B/P1C tracker so historical phase
records remain immutable.  It uses assignment within exact conserved sectors,
assesses ambiguity at the complete assignment-objective level, keeps surplus
states surplus even inside degenerate components, and returns actual subspace
projectors/principal angles.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence, Tuple

import numpy as np
from scipy.optimize import linear_sum_assignment


class TrackingError(ValueError):
    """Raised when explicit state-tracking invariants are violated."""


@dataclass(frozen=True)
class StateRecord:
    state_id: str
    sector: Tuple[Tuple[str, str], ...]
    eigenvalue: float
    vector: np.ndarray

    def __post_init__(self) -> None:
        if not isinstance(self.state_id, str) or not self.state_id.strip():
            raise TrackingError("state_id is required")
        items = tuple(self.sector.items()) if isinstance(self.sector, Mapping) else tuple(self.sector)
        normalized: list[tuple[str, str]] = []
        keys: set[str] = set()
        for item in items:
            if not isinstance(item, (tuple, list)) or len(item) != 2:
                raise TrackingError("sector must contain key/value pairs")
            key, value = str(item[0]), str(item[1])
            if not key.strip() or key in keys:
                raise TrackingError("sector keys must be nonempty and unique")
            keys.add(key)
            normalized.append((key, value))
        if not normalized:
            raise TrackingError("at least one conserved-sector label is required")
        if not np.isfinite(self.eigenvalue):
            raise TrackingError("eigenvalue must be finite")
        vector = np.asarray(self.vector, dtype=np.complex128)
        if vector.ndim != 1 or vector.size == 0 or not np.all(np.isfinite(vector)):
            raise TrackingError("state vector must be finite, one-dimensional, and nonempty")
        if np.linalg.norm(vector) == 0.0:
            raise TrackingError("state vector cannot be zero")
        frozen = np.array(vector, copy=True)
        frozen.setflags(write=False)
        object.__setattr__(self, "sector", tuple(sorted(normalized)))
        object.__setattr__(self, "vector", frozen)


@dataclass(frozen=True)
class TrackingPolicy:
    overlap_minimum: float = 0.5
    degeneracy_gap: float = 1.0e-8
    assignment_tie_tolerance: float = 1.0e-10
    norm_tolerance: float = 1.0e-8
    order_reference: str = "ascending_eigenvalue"

    def __post_init__(self) -> None:
        if not 0.0 <= self.overlap_minimum <= 1.0:
            raise TrackingError("overlap_minimum must lie in [0,1]")
        if self.degeneracy_gap < 0.0 or self.assignment_tie_tolerance < 0.0:
            raise TrackingError("gap and tie tolerances must be nonnegative")
        if self.norm_tolerance <= 0.0:
            raise TrackingError("norm_tolerance must be positive")
        if self.order_reference not in {"ascending_eigenvalue", "descending_eigenvalue"}:
            raise TrackingError("unsupported order_reference")


@dataclass(frozen=True)
class TrackedState:
    previous_state_id: str
    current_state_id: str
    sector: Tuple[Tuple[str, str], ...]
    overlap_magnitude: float
    phase_factor: complex
    phase_aligned_vector: np.ndarray
    eigenvalue_gap: float


@dataclass(frozen=True)
class SubspaceDiagnostic:
    current_state_ids: Tuple[str, ...]
    previous_state_ids: Tuple[str, ...]
    sector: Tuple[Tuple[str, str], ...]
    principal_angles_rad: Tuple[float, ...]
    singular_values: Tuple[float, ...]
    old_projector: np.ndarray
    current_projector: np.ndarray
    projector_frobenius_distance: float
    aligned_current_basis: np.ndarray | None
    procrustes_transport: np.ndarray | None
    rectangular: bool


@dataclass(frozen=True)
class TrackingResult:
    assignments: Tuple[Tuple[str, str], ...]
    tracked_states: Tuple[TrackedState, ...]
    overlap_matrix: Tuple[Tuple[float, ...], ...]
    previous_state_ids: Tuple[str, ...]
    current_state_ids: Tuple[str, ...]
    individual_identity_status: Mapping[str, str]
    missing_previous_state_ids: Tuple[str, ...]
    surplus_current_state_ids: Tuple[str, ...]
    assignment_ambiguous: bool
    ambiguous_previous_state_ids: Tuple[str, ...]
    best_assignment_objectives: Mapping[Tuple[Tuple[str, str], ...], float]
    second_best_assignment_objectives: Mapping[Tuple[Tuple[str, str], ...], float | None]
    swap_detected: bool
    swap_sectors: Tuple[Tuple[Tuple[str, str], ...], ...]
    near_degenerate_groups: Tuple[Tuple[str, ...], ...]
    subspace_diagnostics: Mapping[Tuple[str, ...], SubspaceDiagnostic]


class StateTracker:
    def __init__(self, policy: TrackingPolicy | None = None) -> None:
        self.policy = policy or TrackingPolicy()

    @staticmethod
    def _sector(record: StateRecord) -> Tuple[Tuple[str, str], ...]:
        return tuple(record.sector)

    def _validate(self, previous: Sequence[StateRecord], current: Sequence[StateRecord]) -> None:
        if not previous or not current:
            raise TrackingError("previous and current state sets are required")
        for label, rows in (("previous", previous), ("current", current)):
            ids = [row.state_id for row in rows]
            if len(ids) != len(set(ids)):
                raise TrackingError(f"{label} state IDs must be unique")
        dimension = previous[0].vector.size
        if any(row.vector.size != dimension for row in tuple(previous) + tuple(current)):
            raise TrackingError("state-vector dimensions differ")
        for row in tuple(previous) + tuple(current):
            if abs(float(np.linalg.norm(row.vector)) - 1.0) > self.policy.norm_tolerance:
                raise TrackingError("state vector violates normalization policy")

    @staticmethod
    def _assignment(overlap: np.ndarray, forbidden: tuple[int, int] | None = None) -> tuple[np.ndarray, np.ndarray, float]:
        if overlap.ndim != 2 or min(overlap.shape) == 0:
            return np.asarray([], dtype=int), np.asarray([], dtype=int), 0.0
        score = np.array(overlap, copy=True)
        if forbidden is not None:
            score[forbidden] = -1.0e300
        rows, columns = linear_sum_assignment(-score)
        values = score[rows, columns]
        if np.any(values < -1.0e200):
            return rows, columns, float("-inf")
        return rows, columns, float(np.sum(values))

    def _assignment_with_ambiguity(
        self, overlap: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, float, float | None, bool]:
        rows, columns, best = self._assignment(overlap)
        alternatives: list[float] = []
        for row, column in zip(rows, columns):
            _, _, candidate = self._assignment(overlap, (int(row), int(column)))
            if np.isfinite(candidate):
                alternatives.append(candidate)
        second = max(alternatives) if alternatives else None
        ambiguous = second is not None and best - second <= self.policy.assignment_tie_tolerance
        return rows, columns, best, second, ambiguous

    def _ordered_indices(self, rows: Sequence[StateRecord]) -> Tuple[int, ...]:
        reverse = self.policy.order_reference == "descending_eigenvalue"
        return tuple(
            sorted(
                range(len(rows)),
                key=lambda index: (rows[index].eigenvalue, rows[index].state_id),
                reverse=reverse,
            )
        )

    def _near_degenerate_groups(self, current: Sequence[StateRecord]) -> Tuple[Tuple[str, ...], ...]:
        groups: list[tuple[str, ...]] = []
        sectors: dict[Tuple[Tuple[str, str], ...], list[int]] = {}
        for index, state in enumerate(current):
            sectors.setdefault(self._sector(state), []).append(index)
        for indices in sectors.values():
            adjacency = {index: set() for index in indices}
            for offset, left in enumerate(indices):
                for right in indices[offset + 1 :]:
                    if abs(current[left].eigenvalue - current[right].eigenvalue) <= self.policy.degeneracy_gap:
                        adjacency[left].add(right)
                        adjacency[right].add(left)
            seen: set[int] = set()
            for start in indices:
                if start in seen or not adjacency[start]:
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
                groups.append(tuple(sorted(current[index].state_id for index in component)))
        return tuple(sorted(groups))

    @staticmethod
    def _orthonormal_basis(vectors: Sequence[np.ndarray]) -> np.ndarray:
        if not vectors:
            return np.empty((0, 0), dtype=np.complex128)
        matrix = np.column_stack(vectors)
        q, r = np.linalg.qr(matrix)
        rank = int(np.count_nonzero(np.abs(np.diag(r)) > 1.0e-12))
        return q[:, :rank]

    def match(self, previous: Sequence[StateRecord], current: Sequence[StateRecord]) -> TrackingResult:
        previous_rows = tuple(previous)
        current_rows = tuple(current)
        self._validate(previous_rows, current_rows)
        overlap_complex = np.asarray(
            [[np.vdot(old.vector, new.vector) for new in current_rows] for old in previous_rows],
            dtype=np.complex128,
        )
        overlap = np.abs(overlap_complex)

        previous_groups: dict[Tuple[Tuple[str, str], ...], list[int]] = {}
        current_groups: dict[Tuple[Tuple[str, str], ...], list[int]] = {}
        for index, row in enumerate(previous_rows):
            previous_groups.setdefault(self._sector(row), []).append(index)
        for index, row in enumerate(current_rows):
            current_groups.setdefault(self._sector(row), []).append(index)

        assignments: dict[int, int] = {}
        assigned_current: set[int] = set()
        ambiguous_previous: set[str] = set()
        best_objectives: dict[Tuple[Tuple[str, str], ...], float] = {}
        second_objectives: dict[Tuple[Tuple[str, str], ...], float | None] = {}

        for sector in sorted(set(previous_groups) | set(current_groups)):
            old_indices = previous_groups.get(sector, [])
            new_indices = current_groups.get(sector, [])
            if not old_indices or not new_indices:
                continue
            local = overlap[np.ix_(old_indices, new_indices)]
            local_rows, local_columns, best, second, ambiguous = self._assignment_with_ambiguity(local)
            best_objectives[sector] = best
            second_objectives[sector] = second
            for local_row, local_column in zip(local_rows, local_columns):
                old_index = old_indices[int(local_row)]
                new_index = new_indices[int(local_column)]
                if overlap[old_index, new_index] < self.policy.overlap_minimum:
                    continue
                assignments[old_index] = new_index
                assigned_current.add(new_index)
            if ambiguous:
                ambiguous_previous.update(previous_rows[index].state_id for index in old_indices)

        missing_previous = tuple(
            row.state_id for index, row in enumerate(previous_rows) if index not in assignments
        )
        surplus_current = tuple(
            row.state_id for index, row in enumerate(current_rows) if index not in assigned_current
        )
        identity: dict[str, str] = {
            row.state_id: (
                "INDIVIDUAL_OVERLAP_CONTINUED" if index in assigned_current else "SURPLUS_UNMATCHED"
            )
            for index, row in enumerate(current_rows)
        }

        tracked: list[TrackedState] = []
        for old_index in sorted(assignments):
            new_index = assignments[old_index]
            old, new = previous_rows[old_index], current_rows[new_index]
            raw = overlap_complex[old_index, new_index]
            phase = 1.0 + 0.0j if abs(raw) == 0.0 else raw / abs(raw)
            aligned = np.asarray(new.vector * np.conjugate(phase), dtype=np.complex128)
            aligned = np.array(aligned, copy=True)
            aligned.setflags(write=False)
            same_sector_indices = current_groups[self._sector(new)]
            gap = min(
                (
                    abs(new.eigenvalue - current_rows[index].eigenvalue)
                    for index in same_sector_indices
                    if index != new_index
                ),
                default=float("inf"),
            )
            tracked.append(
                TrackedState(
                    old.state_id,
                    new.state_id,
                    self._sector(new),
                    float(abs(raw)),
                    complex(phase),
                    aligned,
                    float(gap),
                )
            )

        near_groups = self._near_degenerate_groups(current_rows)
        diagnostics: dict[Tuple[str, ...], SubspaceDiagnostic] = {}
        current_by_id = {row.state_id: row for row in current_rows}
        old_for_current = {
            current_rows[new_index].state_id: previous_rows[old_index]
            for old_index, new_index in assignments.items()
        }
        for group in near_groups:
            current_group = tuple(current_by_id[state_id] for state_id in group)
            matched_current = tuple(row for row in current_group if row.state_id in old_for_current)
            previous_group = tuple(old_for_current[row.state_id] for row in matched_current)
            for row in matched_current:
                identity[row.state_id] = "SUBSPACE_ONLY_NEAR_DEGENERACY"
            # Surplus states deliberately retain SURPLUS_UNMATCHED.
            old_basis = self._orthonormal_basis([row.vector for row in previous_group])
            current_basis = self._orthonormal_basis([row.vector for row in current_group])
            dimension = current_rows[0].vector.size
            old_projector = (
                old_basis @ old_basis.conj().T
                if old_basis.size
                else np.zeros((dimension, dimension), dtype=np.complex128)
            )
            current_projector = current_basis @ current_basis.conj().T
            singular_values = (
                np.linalg.svd(old_basis.conj().T @ current_basis, compute_uv=False)
                if old_basis.size and current_basis.size
                else np.asarray([], dtype=float)
            )
            singular_values = np.clip(np.real(singular_values), 0.0, 1.0)
            principal_angles = np.arccos(singular_values)
            transport = None
            aligned_basis = None
            if old_basis.shape[1] == current_basis.shape[1] and old_basis.shape[1] > 0:
                left, _, right_h = np.linalg.svd(old_basis.conj().T @ current_basis)
                transport = right_h.conj().T @ left.conj().T
                aligned_basis = current_basis @ transport
            for array in (old_projector, current_projector, transport, aligned_basis):
                if isinstance(array, np.ndarray):
                    array.setflags(write=False)
            diagnostics[group] = SubspaceDiagnostic(
                current_state_ids=group,
                previous_state_ids=tuple(row.state_id for row in previous_group),
                sector=self._sector(current_group[0]),
                principal_angles_rad=tuple(float(value) for value in principal_angles),
                singular_values=tuple(float(value) for value in singular_values),
                old_projector=old_projector,
                current_projector=current_projector,
                projector_frobenius_distance=float(np.linalg.norm(old_projector - current_projector)),
                aligned_current_basis=aligned_basis,
                procrustes_transport=transport,
                rectangular=old_basis.shape[1] != current_basis.shape[1],
            )

        swap_sectors: list[Tuple[Tuple[str, str], ...]] = []
        for sector, old_indices in previous_groups.items():
            sector_assignments = {index: assignments[index] for index in old_indices if index in assignments}
            if len(sector_assignments) < 2:
                continue
            current_indices = current_groups.get(sector, [])
            old_order = sorted(
                sector_assignments,
                key=lambda index: (previous_rows[index].eigenvalue, previous_rows[index].state_id),
                reverse=self.policy.order_reference == "descending_eigenvalue",
            )
            new_order = sorted(
                current_indices,
                key=lambda index: (current_rows[index].eigenvalue, current_rows[index].state_id),
                reverse=self.policy.order_reference == "descending_eigenvalue",
            )
            rank = {index: position for position, index in enumerate(new_order)}
            mapped = [rank[sector_assignments[index]] for index in old_order]
            if any(left > right for left, right in zip(mapped, mapped[1:])):
                swap_sectors.append(sector)

        return TrackingResult(
            assignments=tuple(
                (previous_rows[old].state_id, current_rows[new].state_id)
                for old, new in sorted(assignments.items())
            ),
            tracked_states=tuple(tracked),
            overlap_matrix=tuple(tuple(float(value) for value in row) for row in overlap),
            previous_state_ids=tuple(row.state_id for row in previous_rows),
            current_state_ids=tuple(row.state_id for row in current_rows),
            individual_identity_status=identity,
            missing_previous_state_ids=missing_previous,
            surplus_current_state_ids=surplus_current,
            assignment_ambiguous=bool(ambiguous_previous),
            ambiguous_previous_state_ids=tuple(sorted(ambiguous_previous)),
            best_assignment_objectives=best_objectives,
            second_best_assignment_objectives=second_objectives,
            swap_detected=bool(swap_sectors),
            swap_sectors=tuple(swap_sectors),
            near_degenerate_groups=near_groups,
            subspace_diagnostics=diagnostics,
        )


__all__ = [
    "TrackingError",
    "StateRecord",
    "TrackingPolicy",
    "TrackedState",
    "SubspaceDiagnostic",
    "TrackingResult",
    "StateTracker",
]
