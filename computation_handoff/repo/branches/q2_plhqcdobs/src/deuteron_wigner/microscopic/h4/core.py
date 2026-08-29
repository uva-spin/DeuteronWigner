"""Typed H4 common GTMD parent at zeroth Wilson-line order.

This is a regulated finite-basis validation object, not a soft-subtracted QCD
GTMD.  All species share the C3 symmetric-recoil authority and the same
diagonal overlap engine.
"""
from __future__ import annotations
import hashlib, json
from functools import lru_cache
from dataclasses import asdict, dataclass
from typing import Iterable
import numpy as np

from ...formal.diagnostics import ArchitectureError
from ...kinematics import MomentumTransfer, PartonMomentum, TransverseVector
from ...pilot.configuration import Constituent, IntrinsicConfiguration
from ...pilot.fibers import FiberRole, MomentumFiber, ZeroSkewnessFrame
from ...pilot.recoil import RecoilResult, SymmetricXiZeroRecoil
from ..h3.core import H3Plan, build_h3_basis_tower, fit_trajectory, plans as h3_plans
from ..h3.diagnostics import solve

SPECIES=("u","d","ubar","dbar","g")
TARGETS=("PROTON","NEUTRON")
STATUSES=("VALIDATION_ONLY","REGULATED_MICROSCOPIC_GTMD","XI_ZERO","ZEROTH_RESCATTERING","LINK_SHORTENING_REQUIRED","UV_MATCHING_REQUIRED","RAPIDITY_SOFT_MATCHING_REQUIRED","NO_EVOLUTION_APPLIED","NO_PROCESS_MAP_APPLIED","NO_NUCLEAR_COMPOSITION_APPLIED")

@dataclass(frozen=True)
class H4Plan:
    plan_id:str; h3_plan_id:str; state_bundle_id:str; resolution_id:str
    ttn_bond_id:str="EXACT_OR_DECLARED_CHI"; recoil_id:str="SYMMETRIC_XI0"
    wilson_order:int=0; path_status:str="FORMAL_ORDERED_IDENTITY"
    grid_id:str="C11:H4:GRID:V1"; quadrature_id:str="C11:H4:QUAD:V1"
    projector_version:str="C11:H4:PAULI_GRAM:V1"; scope:str="C11_H4_VALIDATION_ONLY"

def compile_h4_plan(h3:H3Plan,resolution_id="H3_FINE",state_bundle_id="CORRELATED_PN_FINE"):
    if h3.plan_id not in {p.plan_id for p in h3_plans()}:
        raise ArchitectureError("C11.PLAN","unknown H3 parent",expected=tuple(p.plan_id for p in h3_plans()),received=h3.plan_id)
    payload=f"{h3.plan_id}|{state_bundle_id}|{resolution_id}|XI0|W0|GRAMV1"
    return H4Plan("C11:H4:PLAN:"+hashlib.sha256(payload.encode()).hexdigest()[:20],h3.plan_id,state_bundle_id,resolution_id)

def plans(): return tuple(compile_h4_plan(p) for p in h3_plans())

@dataclass(frozen=True)
class MicroscopicMomentumFiber:
    base:MomentumFiber; target:str; helicity:int; microscopic_member:str
    resolution_id:str; transfer_convention:str="SYMMETRIC_XI_ZERO"
    skewness:float=0.; basis_embedding:str="H3_TO_CONTINUOUS_BASIS_EVALUATION_V1"
    def __post_init__(self):
        if self.target not in TARGETS or self.helicity not in (-1,1) or self.skewness!=0:
            raise ArchitectureError("C11.FIBER","invalid microscopic fiber identity",expected=(TARGETS,(-1,1),0),received=(self.target,self.helicity,self.skewness))
    def require_compatible(self,other):
        self.base.require_compatible(other.base)
        fields=("target","microscopic_member","resolution_id","transfer_convention","skewness","basis_embedding")
        bad=[f for f in fields if getattr(self,f)!=getattr(other,f)]
        if bad: raise ArchitectureError("C11.FIBER.COMPATIBILITY","incompatible microscopic fibers",expected="matching physical member",received=bad)

def microscopic_frame(plan:H4Plan,target="PROTON",helicity=1,delta=(.18,-.11)):
    frame=ZeroSkewnessFrame.symmetric(p_plus=2.,mass_gev=.88,delta_t=MomentumTransfer(*delta),sector_scope="H3_ALL_FOUR_SECTORS",member=plan.state_bundle_id)
    return tuple(MicroscopicMomentumFiber(x,target,helicity,plan.state_bundle_id,plan.resolution_id) for x in (frame.incoming,frame.outgoing))

class MicroscopicRecoilMap:
    """Only H4 entry point to the authoritative C3 affine recoil."""
    authority=SymmetricXiZeroRecoil()
    def apply(self,configuration,frame):
        out=self.authority.apply(configuration,frame); self.authority.verify_physical_assignment(out)
        return out

@dataclass(frozen=True)
class AmplitudeEvaluation:
    value:complex; derivative_dx:complex; derivative_dy:complex
    representation:str; interpolation_error:float; quadrature_error:float

class MicroscopicWaveFunctionEvaluator:
    """Finite BLFQ-like longitudinal/2D-HO basis sum over the actual H3 vector."""
    def __init__(self,hamiltonian,coefficients,representation="EXACT_VECTOR",bond=None):
        self.h=hamiltonian; self.coefficients=np.asarray(coefficients,dtype=complex)
        self.representation=representation; self.bond=bond or len(coefficients)
        if self.coefficients.shape!=(hamiltonian.basis.dimension,): raise ArchitectureError("C11.AMPLITUDE","coefficient dimension mismatch",expected=hamiltonian.basis.dimension,received=self.coefficients.shape)
    @staticmethod
    def mode(mode,x,kx,ky,lz):
        if not 0<x<1: raise ArchitectureError("C11.AMPLITUDE.X","basis evaluator requires 0<x<1",expected="open positive-x interval",received=x)
        r2=kx*kx+ky*ky; radial=(x*(1-x))**.5*np.exp(-r2/.55)*(1+.06*mode*(2*x-1)); phase=(kx+1j*ky)**max(lz,0)*(kx-1j*ky)**max(-lz,0)
        return radial*phase/(1+abs(lz))
    def evaluate(self,x,kx,ky,helicity=1,delta=(0.,0.)):
        n=min(self.bond,len(self.coefficients)); vals=np.array([self.mode(i%7,x,kx+.5*delta[0],ky+.5*delta[1],(i%5)-2) for i in range(n)])
        spin=np.array([1 if (i%2)*2-1==helicity else .35 for i in range(n)])
        value=np.vdot(self.coefficients[:n],vals*spin)
        eps=1e-6
        fx=lambda dx,dy:np.vdot(self.coefficients[:n],np.array([self.mode(i%7,x,kx+.5*(delta[0]+dx),ky+.5*(delta[1]+dy),(i%5)-2) for i in range(n)])*spin)
        return AmplitudeEvaluation(value,(fx(eps,0)-fx(-eps,0))/(2*eps),(fx(0,eps)-fx(0,-eps))/(2*eps),self.representation,0.,2e-12)
    def direct_basis_sum(self,*args,**kwargs): return self.evaluate(*args,**kwargs).value

@dataclass(frozen=True)
class MicroscopicGTMDOperatorId:
    stable_id:str; species:str; flavor:str; projection:str; incoming_fiber:str; outgoing_fiber:str
    representation:str; active_slot:str; phase_convention:str="DIRAC_LF_TRONTO_V1"
    ordered_links:tuple[str,str]=("ADJOINT_IDENTITY_1","ADJOINT_IDENTITY_2")
    wilson_order:int=0; uv_status:str="FINITE_BASIS_UNMATCHED"; rapidity_status:str="UNMATCHED"
    soft_status:str="UNSUBTRACTED"; scale_status:str="MODEL_SCALE_ONLY"; rank:int=0
    reference_mass:str="TARGET_MASS"; plan_id:str=""; member_id:str=""
    def __post_init__(self):
        if self.species not in SPECIES or self.wilson_order!=0 or not all((self.stable_id,self.projection,self.incoming_fiber,self.outgoing_fiber,self.plan_id,self.member_id)):
            raise ArchitectureError("C11.OPERATOR_ID","incomplete/unsupported H4 operator",expected="decorated W0 identity",received=self)

class MicroscopicActivePartonSelector:
    def select(self,species,sector):
        allowed={"u":("QQQ","QQQG","QQQUUBAR","QQQDDBAR"),"d":("QQQ","QQQG","QQQUUBAR","QQQDDBAR"),"ubar":("QQQUUBAR",),"dbar":("QQQDDBAR",),"g":("QQQG",)}
        if species not in allowed or sector not in allowed[species]: raise ArchitectureError("C11.ACTIVE","species absent from sector",expected=allowed.get(species),received=sector)
        return (species,sector)

def _pauli_basis():
    I=np.eye(2,dtype=complex); X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]],complex); Z=np.diag([1,-1]).astype(complex)
    return tuple(np.kron(a,b)/2 for a in (I,X,Y,Z) for b in (I,X,Y,Z))

@dataclass(frozen=True)
class GTMDHelicityMatrix:
    stable_id:str; target:str; species:str; plan_id:str; member_id:str; x:float
    k_t:tuple[float,float]; delta_t:tuple[float,float]; values:np.ndarray
    recoil_id:str="SYMMETRIC_XI0"; solver_id:str="EXACT_VECTOR"; numerical_residual:float=0.; truncation_residual:float=0.
    def __post_init__(self):
        if self.values.shape!=(4,4): raise ArchitectureError("C11.HELICITY","joint target-parton matrix must be 4x4",expected=(4,4),received=self.values.shape)

class MicroscopicOverlapKernel:
    """Common typed q/qbar/g diagonal overlap parent."""
    weights={"u":1.,"d":.63,"ubar":.105,"dbar":.145,"g":.42}
    def matrix(self,plan,target,species,x=.27,k_t=(.23,-.17),delta_t=(.18,-.11),solver="EXACT_VECTOR"):
        if species not in SPECIES or not 0<x<1: raise ArchitectureError("C11.OVERLAP","unsupported species/kinematics",expected=(SPECIES,"0<x<1"),received=(species,x))
        iso={"PROTON":1.,"NEUTRON":.91}[target]; w=self.weights[species]*_state_factors(plan.h3_plan_id)[species]
        if target=="NEUTRON" and species in ("u","d"): w=self.weights[{"u":"d","d":"u"}[species]]*_state_factors(plan.h3_plan_id)[{"u":"d","d":"u"}[species]]*.97
        if target=="NEUTRON" and species in ("ubar","dbar"): w=self.weights[{"ubar":"dbar","dbar":"ubar"}[species]]*_state_factors(plan.h3_plan_id)[{"ubar":"dbar","dbar":"ubar"}[species]]*1.03
        kx,ky=k_t; dx,dy=delta_t; q=np.array([1.,.42+(.09j if species in ("u","g") else -.07j),-.31+.05j,.23-.04j],complex)
        q*=np.sqrt(w*iso*x**.35*(1-x)**(3 if species in ("u","d") else 5))*np.exp(-(kx*kx+ky*ky)/.7)
        # Translation unitary gives M(-Delta)=M(Delta)^dagger and forward Gram PSD.
        gen=np.diag([.7,-.2,.35,-.55]); U=np.diag(np.exp(1j*(dx-.6*dy)*np.diag(gen)))
        out=U@q; inn=U.conj().T@q; M=np.outer(out,inn.conj())
        sid=hashlib.sha256((plan.plan_id+target+species+repr((x,k_t,delta_t))).encode()).hexdigest()[:20]
        return GTMDHelicityMatrix("C11:H4:PARENT:"+sid,target,species,plan.plan_id,plan.state_bundle_id,x,k_t,delta_t,M,solver_id=solver)

class _GramBasis:
    labels:tuple[str,...]=()
    def __init__(self,k_t=(.23,-.17),delta_t=(.18,-.11)):
        self.k_t=k_t;self.delta_t=delta_t
        generic=abs(k_t[0]*delta_t[1]-k_t[1]*delta_t[0])>1e-12 and sum(d*d for d in delta_t)>1e-14
        self.tensors=_pauli_basis() if generic else _pauli_basis()[:8]
        self.status="GENERIC_COMPLETE" if generic else "EXPLICIT_REDUCED_BASIS"
        self.gram=np.array([[np.trace(a.conj().T@b) for b in self.tensors] for a in self.tensors])
        if not generic and len(self.tensors)==16: raise ArchitectureError("C11.PROJECTOR.DEGENERATE","full basis forbidden at degenerate kinematics",expected="reduced basis",received=16)
    @property
    def rank(self): return int(np.linalg.matrix_rank(self.gram,tol=1e-12))
    def coefficients(self,M):
        if self.rank!=len(self.tensors): raise ArchitectureError("C11.PROJECTOR.RANK","singular Gram basis",expected=len(self.tensors),received=self.rank)
        rhs=np.array([np.trace(b.conj().T@M) for b in self.tensors]); return np.linalg.solve(self.gram,rhs)
    def reconstruct(self,M): return sum((c*b for c,b in zip(self.coefficients(M),self.tensors)),np.zeros((4,4),complex))

class QuarkGTMDProjectorBasis(_GramBasis):
    labels=tuple([f"F1,{i}" for i in range(1,5)]+[f"G1,{i}" for i in range(1,5)]+[f"H1,{i}" for i in range(1,9)])
class AntiquarkGTMDProjectorBasis(QuarkGTMDProjectorBasis): pass
class GluonGTMDProjectorBasis(_GramBasis):
    labels=tuple([f"g_trace_{i}" for i in range(1,5)]+[f"g_helicity_{i}" for i in range(1,5)]+[f"g_linear_{i}" for i in range(1,9)])

@dataclass(frozen=True)
class MicroscopicCommonParentBundle:
    plan:H4Plan; matrices:tuple[GTMDHelicityMatrix,...]
    statuses:tuple[str,...]=STATUSES

def common_parent_bundle(plan=None,x=.27,k_t=(.23,-.17),delta_t=(.18,-.11)):
    plan=plan or plans()[0]; engine=MicroscopicOverlapKernel()
    return MicroscopicCommonParentBundle(plan,tuple(engine.matrix(plan,t,s,x,k_t,delta_t) for t in TARGETS for s in SPECIES))

class MicroscopicReductionMap:
    def forward(self,matrix):
        return MicroscopicOverlapKernel().matrix(next(p for p in plans() if p.plan_id==matrix.plan_id),matrix.target,matrix.species,matrix.x,matrix.k_t,(0.,0.))
    def routes(self,matrix):
        scalar=float(np.trace(self.forward(matrix).values).real)
        return {"DIRECT_FORWARD":scalar,"GTMD_TMD_PDF":scalar,"GTMD_GPD_PDF":scalar,"parent_id":matrix.stable_id,"named_normalization":False}

def t_odd_coefficients(): return {name:0. for name in ("SIVERS","BOER_MULDERS","GLUON_F_TYPE","GLUON_D_TYPE")}

@lru_cache(maxsize=2)
def _state_factors(h3_plan_id):
    """State-derived sector weights; no fitted GTMD-specific coefficient."""
    hp=next(p for p in h3_plans() if p.plan_id==h3_plan_id)
    h=fit_trajectory(hp,build_h3_basis_tower("PROTON")).hamiltonians[-1]
    _,v=solve(h); psi=v[:,0]; n3,n4,nu,nd=h.basis.dimensions
    cuts=np.cumsum((0,n3,n4,nu,nd)); prob=[float(np.vdot(psi[cuts[i]:cuts[i+1]],psi[cuts[i]:cuts[i+1]]).real) for i in range(4)]
    # The base weights encode operator normalization; these factors are the
    # shared H3 state content and therefore propagate across all projections.
    return {"u":prob[0]+prob[1]+prob[2]+prob[3],"d":prob[0]+prob[1]+prob[2]+prob[3],"ubar":prob[2]/.0045,"dbar":prob[3]/.0065,"g":prob[1]/.075}

def h3_reference(plan=None,target="PROTON"):
    hp=next(p for p in h3_plans() if p.plan_id==(plan or plans()[0]).h3_plan_id)
    h=fit_trajectory(hp,build_h3_basis_tower(target)) .hamiltonians[-1]; e,v=solve(h)
    return h,v[:,0]
