"""Typed H0 Hamiltonian terms, free mass, and reduced canonical vertex."""

from __future__ import annotations

from dataclasses import dataclass
from math import exp

import numpy as np

from ...formal.diagnostics import ArchitectureError
from .basis import PhysicalFockBasis
from .color import emitted_gluon_color_amplitudes
from .resolution import HamiltonianResolution


_MASS={"u":0.33,"d":0.33,"NOT_APPLICABLE":0.0}


@dataclass(frozen=True)
class HamiltonianTerm:
    term_id: str
    source_sector: str
    target_sector: str
    symmetry_signature: str
    parameter_block_id: str
    regulator_identity: str
    zero_mode_and_endpoint_policy: str
    adjoint_term_id: str
    provenance_node: str
    approximation_status: str

    def __post_init__(self):
        required=(self.term_id,self.source_sector,self.target_sector,self.symmetry_signature,self.parameter_block_id,self.regulator_identity,self.zero_mode_and_endpoint_policy,self.adjoint_term_id,self.provenance_node,self.approximation_status)
        if not all(required):
            raise ArchitectureError("C7.TERM", "Hamiltonian term identity is incomplete", expected="all typed fields", received=required)

    def derivative(self,parameter_id: str):
        raise NotImplementedError


@dataclass(frozen=True)
class FreeInvariantMassTerm(HamiltonianTerm):
    @classmethod
    def for_sector(cls,sector: str):
        return cls(f"C7:H0:FREE:{sector}",sector,sector,"PRESERVES_ALL_EXACT_BLOCKS","H0_BASIS_MASSES","H0_HO_TRUNCATION","EXCLUDE_GLUON_ZERO_MODE_WITH_ENDPOINT_REGULATOR",f"C7:H0:FREE:{sector}","C7:PROV:FREE","VALIDATION_ONLY_FREE_INVARIANT_MASS")

    @staticmethod
    def state_value(state,resolution: HamiltonianResolution) -> float:
        b2=resolution.oscillator_scale_b.gev**2
        return float(sum((b2*item.ho_usage+_MASS[item.flavor]**2)/float(item.longitudinal_fraction_exact) for item in state.creation_labels))

    def assemble(self,basis: PhysicalFockBasis) -> np.ndarray:
        return np.diag([self.state_value(state,basis.resolution) for state in basis.states]).astype(complex)

    def apply(self,vector: np.ndarray,basis: PhysicalFockBasis) -> np.ndarray:
        values=np.asarray([self.state_value(state,basis.resolution) for state in basis.states])
        return values*np.asarray(vector)

    def matrix_element(self,bra,ket,resolution):
        return self.state_value(ket,resolution) if bra.stable_id==ket.stable_id else 0.0

    def derivative(self,parameter_id: str):
        if parameter_id!="H0_BASIS_MASSES":
            return 0.0
        return "ANALYTIC_DIAGONAL_MASS_DERIVATIVE"

    @staticmethod
    def independent_k2_quadrature(n: int,m: int,b: float) -> float:
        if n!=0:
            raise ArchitectureError("C7.FREE", "H0 quadrature oracle currently covers n=0 modes", expected=0, received=n)
        # Independent Gauss--Laguerre quadrature after y=k^2/b^2.  The
        # radial HO probability is proportional to y^|m| exp(-y).
        nodes,weights=np.polynomial.laguerre.laggauss(48)
        power=abs(m)
        return float(b*b*np.sum(weights*nodes**(power+1))/np.sum(weights*nodes**power))

    def quadrature_residual(self,basis: PhysicalFockBasis) -> float:
        maximum=0.0
        for state in basis.states:
            direct=0.0
            for item in state.creation_labels:
                k2=self.independent_k2_quadrature(item.transverse_n,item.transverse_m,basis.resolution.oscillator_scale_b.gev)
                direct+=(k2+_MASS[item.flavor]**2)/float(item.longitudinal_fraction_exact)
            maximum=max(maximum,abs(direct-self.state_value(state,basis.resolution)))
        return maximum


@dataclass(frozen=True)
class ReducedCanonicalVertexTerm(HamiltonianTerm):
    coupling: float
    emitter_index: int
    direction: str

    @classmethod
    def emission(cls,coupling=0.2,emitter_index=1):
        return cls("C7:H0:VERTEX:QQQ_TO_QQQG","qqq","qqqg","CHARGE_BARYON_JZ_COLOR_K_CONSERVING","H0_SHARED_BENCHMARK_COUPLING","H0_ANALYTIC_VERTEX_REGULATOR","EXCLUDE_ZERO_MODE_AND_ENDPOINTS","C7:H0:VERTEX:QQQG_TO_QQQ","C7:PROV:REDUCED_VERTEX","REDUCED_CANONICAL_INTERFACE_BENCHMARK",coupling,emitter_index,"EMISSION")

    def adjoint(self):
        return ReducedCanonicalVertexTerm("C7:H0:VERTEX:QQQG_TO_QQQ","qqqg","qqq","CHARGE_BARYON_JZ_COLOR_K_CONSERVING","H0_SHARED_BENCHMARK_COUPLING",self.regulator_identity,self.zero_mode_and_endpoint_policy,self.term_id,self.provenance_node,self.approximation_status,self.coupling,self.emitter_index,"ABSORPTION")

    def emission_matrix(self,source: PhysicalFockBasis,target: PhysicalFockBasis) -> np.ndarray:
        if source.sector.sector_id!="qqq" or target.sector.sector_id!="qqqg":
            raise ArchitectureError("C7.VERTEX", "vertex basis endpoint mismatch", expected=("qqq","qqqg"), received=(source.sector.sector_id,target.sector.sector_id))
        if source.target_charge!=target.target_charge or source.target_Jz!=target.target_Jz or source.resolution.resolution_id!=target.resolution.resolution_id:
            raise ArchitectureError("C7.VERTEX", "vertex exact block mismatch", expected="same charge/Jz/resolution", received=(source.target_charge,target.target_charge,source.target_Jz,target.target_Jz))
        color=emitted_gluon_color_amplitudes(self.emitter_index)
        emitted_mode=target.states[0].creation_labels[-1].longitudinal_mode_exact
        before=source.states[0].creation_labels[self.emitter_index].longitudinal_mode_exact
        after=target.states[0].creation_labels[self.emitter_index].longitudinal_mode_exact
        if before!=after+emitted_mode:
            # Reference modes permit emitter 1 or 2 depending selected source;
            # fail rather than hiding the exact K mismatch.
            raise ArchitectureError("C7.VERTEX", "vertex violates exact longitudinal momentum conservation", expected=before, received=after+emitted_mode)
        transverse_overlap=1.0
        helicity_selection=1.0
        regulator=exp(-float(emitted_mode/source.resolution.K))
        normalization=(float(before*after*emitted_mode))**-0.5
        fermion_sign=-1.0 if self.emitter_index%2 else 1.0
        vector=self.coupling*color*transverse_overlap*helicity_selection*regulator*normalization*fermion_sign
        return vector[:,None]

    def matrix(self,source: PhysicalFockBasis,target: PhysicalFockBasis) -> np.ndarray:
        emission=self.emission_matrix(source,target) if self.direction=="EMISSION" else self.adjoint().emission_matrix(target,source)
        return emission if self.direction=="EMISSION" else emission.conj().T

    def apply(self,vector,resolution):
        raise ArchitectureError("C7.VERTEX", "vertex apply requires typed source/target bases", expected="matrix(source,target) then apply", received="resolution-only")

    def matrix_element(self,bra,ket):
        raise ArchitectureError("C7.VERTEX", "use typed block matrix for reduced vertex", expected="matrix(source,target)", received=(bra,ket))

    def derivative(self,parameter_id: str):
        return "MATRIX_DIVIDED_BY_SHARED_COUPLING" if parameter_id==self.parameter_block_id else 0.0
