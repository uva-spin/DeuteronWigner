"""Exact finite-dimensional Feshbach and induced-operator benchmark."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from ..formal.diagnostics import ArchitectureError


@dataclass(frozen=True)
class FeshbachResult:
    stable_id: str
    energy: float
    gap: float
    coupling: float
    resolvent_condition_number: float
    omega: float
    norm_kernel: float
    full_matrix_element: float
    effective_matrix_element: float
    pop_matrix_element: float
    energy_residual: float
    operator_residual: float
    pop_failure: float
    status: str = "VALIDATION_ONLY"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class FiniteFeshbachModel:
    h_pp: float = 0.2
    h_qq: float = 2.4
    coupling: float = 0.35
    operator: tuple[tuple[float, float], tuple[float, float]] = (
        (0.0, 0.7), (0.7, 0.3),
    )
    singular_tolerance: float = 1e-10
    stable_id: str = "C4:FESHBACH:TWO_SECTOR"

    def __post_init__(self) -> None:
        matrix = np.asarray(self.operator, float)
        if matrix.shape != (2, 2) or not np.allclose(matrix, matrix.T):
            raise ArchitectureError(
                "C4.FESHBACH.HERMITICITY", "operator must be Hermitian 2x2",
                expected="real symmetric 2x2", received=self.operator,
            )
        if self.h_qq <= self.h_pp:
            raise ArchitectureError(
                "C4.FESHBACH.THRESHOLD", "higher sector must lie above retained state",
                expected="h_qq>h_pp", received=(self.h_pp, self.h_qq),
            )

    def omega(self, energy: float) -> float:
        denominator = energy - self.h_qq
        if abs(denominator) <= self.singular_tolerance:
            raise ArchitectureError(
                "C4.FESHBACH.SINGULAR", "singular or near-threshold resolvent",
                expected=f"|E-H_QQ|>{self.singular_tolerance}",
                received=denominator,
            )
        return self.coupling / denominator

    def effective_hamiltonian(self, energy: float) -> float:
        return self.h_pp + self.coupling * self.omega(energy)

    def effective_operator(self, outgoing_energy: float, incoming_energy: float) -> float:
        left, right = self.omega(outgoing_energy), self.omega(incoming_energy)
        operator = np.asarray(self.operator, float)
        unnormalized = (
            operator[0, 0] + left * operator[1, 0]
            + operator[0, 1] * right + left * operator[1, 1] * right
        )
        return float(unnormalized / np.sqrt((1 + left * left) * (1 + right * right)))

    def solve(self) -> FeshbachResult:
        hamiltonian = np.asarray(
            ((self.h_pp, self.coupling), (self.coupling, self.h_qq)), float
        )
        energies, vectors = np.linalg.eigh(hamiltonian)
        energy = float(energies[0])
        vector = vectors[:, 0]
        if vector[0] < 0:
            vector = -vector
        omega = self.omega(energy)
        normalized_retained = np.asarray((1, omega), float) / np.sqrt(1 + omega**2)
        operator = np.asarray(self.operator, float)
        full = float(vector @ operator @ vector)
        effective = self.effective_operator(energy, energy)
        pop = float(operator[0, 0])
        return FeshbachResult(
            self.stable_id, energy, self.h_qq - energy, self.coupling,
            1.0, omega, 1 + omega**2, full, effective, pop,
            abs(energy - self.effective_hamiltonian(energy)),
            abs(full - effective), abs(full - pop),
        )


def require_exclusive_representation(*, explicit_sector: bool, induced_operator: bool) -> None:
    if explicit_sector and induced_operator:
        raise ArchitectureError(
            "C4.INDUCED_OPERATOR.DOUBLE_COUNT",
            "explicit higher sector and its induced operator cannot coexist",
            expected="exactly one representation", received="both enabled",
        )
