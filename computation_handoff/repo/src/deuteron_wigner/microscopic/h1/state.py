"""State tracking and versioned valence microscopic bundles."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ...formal.diagnostics import ArchitectureError


def deterministic_phase(vector):
    vector=np.asarray(vector,dtype=complex).copy()
    pivot=int(np.argmax(np.abs(vector)))
    if abs(vector[pivot])>0:
        vector*=np.exp(-1j*np.angle(vector[pivot]))
    if vector[pivot].real<0: vector*=-1
    return vector


@dataclass(frozen=True)
class ValenceStateTracker:
    tracker_id: str = "C8:H1:TRACKER:OVERLAP_CURRENT_PRINCIPAL_ANGLE"

    def track(self,previous,current_vectors,comparison_map,current_operator=None):
        embedded=comparison_map@previous
        scores=[]
        for i in range(current_vectors.shape[1]):
            candidate=current_vectors[:,i]
            overlap=abs(np.vdot(embedded,candidate))
            fingerprint=0.0 if current_operator is None else abs(np.vdot(candidate,current_operator@candidate)-np.vdot(embedded,current_operator@embedded))
            scores.append(overlap-0.05*fingerprint)
        index=int(np.argmax(scores))
        return index,deterministic_phase(current_vectors[:,index]),tuple(float(x) for x in scores)

    @staticmethod
    def principal_angle(left,right):
        singular=np.linalg.svd(left.conj().T@right,compute_uv=False)
        return float(np.arccos(np.clip(np.min(singular),-1,1)))


@dataclass(frozen=True)
class ValenceMicroscopicStateBundle:
    bundle_id: str
    hamiltonian_id: str
    plan_id: str
    resolution_id: str
    basis_id: str
    mass_squared: float
    normalized_state: tuple[complex,...]
    current_id: str
    exact_residual: float
    krylov_residual: float
    ttn_residual: float
    phase_record: str
    discrepancy: tuple[str,...]
    scope: str = "C8_H1_VALIDATION_ONLY"
    sector_scope: str = "VALENCE_ONLY"

    def __post_init__(self):
        if self.scope!="C8_H1_VALIDATION_ONLY" or self.sector_scope!="VALENCE_ONLY":
            raise ArchitectureError("C8.BUNDLE", "state bundle exceeded H1 scope", expected=("C8_H1_VALIDATION_ONLY","VALENCE_ONLY"), received=(self.scope,self.sector_scope))
