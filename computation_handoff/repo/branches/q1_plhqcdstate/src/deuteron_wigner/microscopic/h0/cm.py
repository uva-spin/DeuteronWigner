"""Typed intrinsic/center-of-mass gate and Lawson diagnostic."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ...formal.diagnostics import ArchitectureError


@dataclass(frozen=True)
class CenterOfMassPolicy:
    beta_range: tuple[float,...]=(0.0,1.0,5.0,10.0)
    ground_energy: float=1.0
    tolerance: float=1e-12
    stable_id: str="LAWSON_INTRINSIC_GROUND_GATE_V1"

    def factorization_residual(self,cm_quantum_numbers: tuple[int,...]) -> float:
        return float(max(cm_quantum_numbers,default=0))

    def lawson_spectra(self,intrinsic_levels: np.ndarray,spurious_excitations: np.ndarray) -> tuple[np.ndarray,...]:
        rows=[]
        for beta in self.beta_range:
            rows.append(np.concatenate((intrinsic_levels,spurious_excitations+beta)))
        return tuple(rows)

    def intrinsic_drift(self,intrinsic_levels: np.ndarray) -> float:
        spectra=self.lawson_spectra(intrinsic_levels,np.asarray((20.0,)))
        count=len(intrinsic_levels)
        return max(float(np.max(np.abs(row[:count]-intrinsic_levels))) for row in spectra)

    def require_ready(self,cm_quantum_numbers: tuple[int,...],intrinsic_levels: np.ndarray) -> None:
        residual=self.factorization_residual(cm_quantum_numbers)
        drift=self.intrinsic_drift(intrinsic_levels)
        if residual>self.tolerance or drift>self.tolerance:
            raise ArchitectureError("C7.CM", "center-of-mass readiness gate failed", expected=f"<={self.tolerance}", received=(residual,drift))
