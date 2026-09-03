"""Hamiltonian-owned valence vector current."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ...formal.diagnostics import ArchitectureError
from .hamiltonian import ValenceHamiltonian


@dataclass(frozen=True)
class ValenceVectorCurrent:
    current_id: str
    hamiltonian_id: str
    target: str
    shared_ZV: float
    route: str = "GAUGED_HAMILTONIAN"
    terms: tuple[str,...] = ("ONE_BODY_EXACT_FLAVOR_CHARGES","SHARED_NORMALIZATION_COUNTERTERM")

    @classmethod
    def for_hamiltonian(cls,hamiltonian: ValenceHamiltonian,shared_ZV=1.0):
        return cls("C8:H1:CURRENT:"+hamiltonian.hamiltonian_id.split(":")[-1],hamiltonian.hamiltonian_id,hamiltonian.basis.target,shared_ZV)

    def matrix(self,hamiltonian: ValenceHamiltonian,Q2=0.0,component="PLUS"):
        if hamiltonian.hamiltonian_id!=self.hamiltonian_id:
            raise ArchitectureError("C8.CURRENT", "current/Hamiltonian identity mismatch", expected=self.hamiltonian_id, received=hamiltonian.hamiltonian_id)
        charge=1.0 if self.target=="PROTON" else 0.0
        n=hamiltonian.basis.dimension
        radial=np.array([s.radial+abs(s.Lz) for s in hamiltonian.basis.states],float)
        shape=np.exp(-Q2*(0.18+0.025*radial))
        if self.target=="NEUTRON" and Q2>0:
            shape=Q2*0.025*np.exp(-0.2*Q2)*(1+0.05*radial)
        else:
            shape=charge*shape
        component_factor=1.0 if component=="PLUS" else 1.0+0.018/(1+n)
        return np.diag(self.shared_ZV*component_factor*shape).astype(complex)

    def expectation(self,hamiltonian,state,Q2=0.0,component="PLUS"):
        op=self.matrix(hamiltonian,Q2,component)
        return float(np.vdot(state,op@state).real)
