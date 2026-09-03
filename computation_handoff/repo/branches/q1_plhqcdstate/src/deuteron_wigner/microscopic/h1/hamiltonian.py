"""Typed interacting valence Hamiltonian and H1 term basis."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np

from ...formal.diagnostics import ArchitectureError
from .basis import H1ValenceBasis
from .planning import H1PredictionPlan


@dataclass(frozen=True)
class ValenceHamiltonianTerm:
    term_id: str
    operator_class: str
    basis_id: str
    parameter_block_id: str
    kernel_identity: str
    status: str
    provenance: str
    ablation_relation: str
    self_adjoint_proof: str = "REAL_SYMMETRIC_CONSTRUCTION"
    source_sector: str = "qqq"
    target_sector: str = "qqq"
    selection_rules: str = "COLOR_FLAVOR_JZ_PARITY_PERMUTATION_PRESERVING"
    naturalness_metadata: str = "DIMENSIONLESS_COEFFICIENT_O1_VALIDATION_PRIOR"


@dataclass(frozen=True)
class H1TruncationDiscrepancy:
    omitted: tuple[str,...] = ("qqqg","qqqq-qbar","higher_orbitals","zero_modes","instantaneous_partners","basis_tail")
    interpretation: str = "UNIMPLEMENTED_NOT_ZERO"


@dataclass(frozen=True)
class ValenceHamiltonian:
    plan_id: str
    basis: H1ValenceBasis
    terms: tuple[ValenceHamiltonianTerm,...]
    matrix: np.ndarray
    parameters: tuple[tuple[str,float],...]
    discrepancy: H1TruncationDiscrepancy

    def __post_init__(self):
        if self.matrix.shape!=(self.basis.dimension,self.basis.dimension) or not np.allclose(self.matrix,self.matrix.conj().T,atol=1e-13):
            raise ArchitectureError("C8.HAMILTONIAN", "Hamiltonian matrix invalid", expected="Hermitian basis-sized block", received=self.matrix.shape)
    @property
    def hamiltonian_id(self):
        payload=self.plan_id+self.basis.basis_id+repr(self.parameters)+hashlib.sha256(np.round(self.matrix,14).tobytes()).hexdigest()
        return "C8:H1:HAMILTONIAN:"+hashlib.sha256(payload.encode()).hexdigest()[:20]
    def apply(self,vector): return self.matrix@np.asarray(vector)


def _operator_matrices(basis):
    n=basis.dimension
    radial=np.array([s.radial for s in basis.states],float)
    lz=np.array([s.Lz for s in basis.states],float)
    free=np.diag(0.55+0.18*radial+0.08*lz*lz+0.025*np.arange(n))
    conf=np.diag(0.10*(1+radial+np.abs(lz)))
    for i in range(n-1):
        if abs(basis.states[i].Lz-basis.states[i+1].Lz)<=1:
            conf[i,i+1]=conf[i+1,i]=0.028
    spin=np.diag(np.array([1 if s.pair_spin else -0.55 for s in basis.states]))
    for i in range(n):
        for j in range(i):
            if abs(basis.states[i].Lz-basis.states[j].Lz)==1 and basis.states[i].radial==basis.states[j].radial:
                spin[i,j]=spin[j,i]=0.035
    identity=np.eye(n)
    return free,conf,spin,identity


def build_hamiltonian(plan: H1PredictionPlan,basis: H1ValenceBasis,parameters: dict[str,float]):
    free,conf,spin,identity=_operator_matrices(basis)
    kappa=parameters.get("kappa4",0.0)
    cspin=parameters.get("color_spin",0.0)
    dm2=parameters.get("mass_ct",0.0)
    if plan.assumption.confinement_route=="ZERO_CONFINEMENT" and abs(kappa)>0:
        raise ArchitectureError("C8.HAMILTONIAN", "zero and induced confinement mixed", expected=0.0, received=kappa)
    matrix=free+kappa*conf+cspin*spin+dm2*identity
    terms=[
        ValenceHamiltonianTerm("C8:H1:FREE","CANONICAL",basis.basis_id,"H0_BASIS_MASSES","C7_FREE_INVARIANT_MASS","canonical","C7:PROV:FREE","RETAINED_FROM"),
        ValenceHamiltonianTerm("C8:H1:MASS_CT","COUNTERTERM",basis.basis_id,"LIGHT_QUARK_MASS_CT","IDENTITY_MASS_SQUARED","counterterm","C8:PROV:RENORMALIZATION","ADDS_TO"),
    ]
    if plan.assumption.confinement_route=="INDUCED_REFIT":
        terms.append(ValenceHamiltonianTerm("C8:H1:INDUCED_CONF","INDUCED",basis.basis_id,"KAPPA_TL_R","JACOBI_HARMONIC_IR_V1","induced","C8:PROV:OMITTED_IR_SECTORS","ALTERNATIVE_BRANCH_TO_ZERO"))
    if plan.assumption.spin_interaction_route=="EFFECTIVE_COLOR_SPIN":
        terms.append(ValenceHamiltonianTerm("C8:H1:COLOR_SPIN","INDUCED",basis.basis_id,"COLOR_SPIN_R","PAIR_COLOR_SPIN_REGULATED_V1","induced","C8:PROV:FESHBACH_QQQG","ALTERNATIVE_TO_EXPLICIT_QQQG_DYNAMICS"))
    return ValenceHamiltonian(plan.plan_id,basis,tuple(terms),matrix,tuple(sorted(parameters.items())),H1TruncationDiscrepancy())
