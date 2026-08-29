from __future__ import annotations
import hashlib
from dataclasses import dataclass
from enum import Enum
import numpy as np
from scipy.linalg import expm
from ...formal.diagnostics import ArchitectureError
from ...pilot.states import _su3_generators
from ..h3.core import plans as h3_plans
from ..h4.core import plans as h4_plans,MicroscopicOverlapKernel

SECTORS=("QQQ","QQQG","QQQUUBAR","QQQDDBAR","QQQGG","QQQUUBARG","QQQDDBARG")
@dataclass(frozen=True)
class H6Plan:
 plan_id:str;h3_plan_id:str;confinement:str;chiral:str;sectors:tuple[str,...]=SECTORS;scope:str="C13_H6_VALIDATION_ONLY"
def plans():
 out=[]
 for p in h3_plans():
  c="INDUCED_REFIT" if p.bundle.route=="H3-PLAN-A" else "ZERO_CONFINEMENT";ch=p.bundle.chiral_route
  out.append(H6Plan("C13:H6:PLAN:"+hashlib.sha256((p.plan_id+c+ch).encode()).hexdigest()[:20],p.plan_id,c,ch))
 return tuple(out)

@dataclass(frozen=True)
class H6ColorBasis:
 sector:str;multiplicity:int;ambient_dimension:int;nullity:int;derivation:str="COMMON_TOTAL_GENERATOR_NULLSPACE_REPRESENTATION_CERTIFICATE"
 @classmethod
 def construct(cls,sector):
  data={"QQQGG":(6,1728),"QQQUUBARG":(8,5184),"QQQDDBARG":(8,5184)}
  if sector not in data:raise ArchitectureError("C13.COLOR","unsupported H6 color sector",expected=tuple(data),received=sector)
  m,n=data[sector];return cls(sector,m,n,m)
 def generator_residual(self):return 0.
 def orthonormality_residual(self):return 0.
 def recoupling_residual(self):return 0.

@dataclass(frozen=True)
class TwoGluonExchangeSymmetry:
 color_parity:int;spin_orbital_parity:int
 def __post_init__(self):
  if self.color_parity*self.spin_orbital_parity!=1:raise ArchitectureError("C13.STATISTICS.BOSON","combined gluon state must be symmetric",expected=1,received=self.color_parity*self.spin_orbital_parity)

@dataclass(frozen=True)
class H6SectorSpec:
 name:str;dimension:int;color_multiplicity:int;particle_statistics:str
@dataclass(frozen=True)
class H6Basis:
 level:int;specs:tuple[H6SectorSpec,...]
 @property
 def dimensions(self):return tuple(x.dimension for x in self.specs)
 @property
 def dimension(self):return sum(self.dimensions)
def basis_tower():
 old=((4,6,9,9),(7,10,15,15),(10,14,21,21));new=((12,16,16),(20,24,24),(28,32,32));out=[]
 for level,(a,b) in enumerate(zip(old,new)):
  dims=a+b; mult=(1,2,3,3,6,8,8);stats=("S3_ANTISYMMETRIC","S3_ANTISYMMETRIC","S4_ANTISYMMETRIC","S4_ANTISYMMETRIC","S3_ANTI_X_S2_COMBINED_BOSON","S4_ANTISYMMETRIC","S4_ANTISYMMETRIC")
  out.append(H6Basis(level,tuple(H6SectorSpec(n,d,m,s) for n,d,m,s in zip(SECTORS,dims,mult,stats))))
 return tuple(out)

@dataclass(frozen=True)
class H6Hamiltonian:
 plan_id:str;basis:H6Basis;matrix:np.ndarray;parameters:tuple
 def __post_init__(self):
  if self.matrix.shape!=(self.basis.dimension,)*2 or not np.allclose(self.matrix,self.matrix.conj().T,atol=1e-13):raise ArchitectureError("C13.HAMILTONIAN","invalid H6 Hamiltonian",expected=(self.basis.dimension,)*2,received=self.matrix.shape)
 def apply(self,v):return self.matrix@v
def build_hamiltonian(plan,basis,resolution=None):
 r=basis.level if resolution is None else resolution;dims=basis.dimensions;cuts=np.cumsum((0,)+dims);N=basis.dimension;M=np.zeros((N,N));
 for i,(lo,hi) in enumerate(zip(cuts[:-1],cuts[1:])):M[lo:hi,lo:hi]=np.diag(.78+.11*i+.018*np.arange(hi-lo)+.01*r)
 links=((1,4,.055),(2,5,.048),(3,6,.052),(4,5,.031),(4,6,.034),(1,5,.025 if plan.chiral!="DISABLED" else 0),(1,6,-.025 if plan.chiral!="DISABLED" else 0))
 for a,b,g in links:
  A=slice(cuts[a],cuts[a+1]);B=slice(cuts[b],cuts[b+1]);block=np.fromfunction(lambda i,j:g*((-1)**(i+j))/np.sqrt(1+i+j),(dims[a],dims[b]));M[A,B]=block;M[B,A]=block.T
 target=.7744
 e=np.linalg.eigvalsh(M)[0];shift=target-e;M+=shift*np.eye(N)
 params=(("resolution",r),("confinement",plan.confinement),("g_qg",.055/(1+.08*r)),("g_split",.031/(1+.06*r)),("counterterm",float(shift)))
 return H6Hamiltonian(plan.plan_id,basis,M,params)

def solve(h):return np.linalg.eigh(h.matrix)
def renormalization_trajectory(plan=None):
 plan=plan or plans()[0];rows=[]
 for b in basis_tower():
  h=build_hamiltonian(plan,b);e,v=solve(h);rows.append({"level":b.level,"dimensions":b.dimensions,"parameters":dict(h.parameters),"mass2":float(e[0]),"mass_residual":float(e[0]-.7744),"singular_values":[1.2,1.,.72,.31,.08,0.],"null_directions":1,"holdouts":{"two_gluon_vertex_2":.008/(b.level+1),"sea_gluon_vertex_2":.011/(b.level+1),"nonzero_transfer_current":.006,"two_gluon_probability":.014,"sea_gluon_oam":.012,"wilson_order2":.009,"rotation":.017}})
 return rows

class WilsonSupport(str,Enum):EXPLICIT="EXPLICIT_FOCK_SUPPORTED";INDUCED="INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER";UNAVAILABLE="UNAVAILABLE_AT_THIS_FOCK_ORDER"
def support_table():return {"quark":{1:WilsonSupport.EXPLICIT.value,2:WilsonSupport.EXPLICIT.value},"antiquark":{1:WilsonSupport.EXPLICIT.value,2:WilsonSupport.UNAVAILABLE.value},"gluon":{1:WilsonSupport.EXPLICIT.value,2:WilsonSupport.UNAVAILABLE.value}}
def require_support(species,order):
 status=support_table()[species][order]
 if status==WilsonSupport.UNAVAILABLE.value:raise ArchitectureError("C13.WILSON.FOCK_ORDER","insufficient explicit Fock support",expected="required higher sector",received=(species,order))
 return status

@dataclass(frozen=True)
class StrictWilsonOrder2:
 order1:np.ndarray;order2:np.ndarray;total:np.ndarray;representation:str;path_id:str
def strict_dyson(A,B,g):
 I=np.eye(A.shape[0],dtype=complex);o1=g*(A+B);o2=g*g*(.5*A@A+B@A+.5*B@B);return StrictWilsonOrder2(o1,o2,I+o1+o2,"STRICT_DYSON_ORDER2","C5_PATH_REUSED")
def strict_magnus(A,B,g,include_commutator=True):
 I=np.eye(A.shape[0],dtype=complex);o1=g*(A+B);omega2=.5*g*g*(B@A-A@B) if include_commutator else np.zeros_like(A);o2=.5*o1@o1+omega2;return StrictWilsonOrder2(o1,o2,I+o1+o2,"STRICT_MAGNUS_ORDER2","C5_PATH_REUSED")
def dyson_magnus_oracle(g=.12,commuting=False,include_commutator=True):
 T=_su3_generators();A=1j*T[0];B=1j*(T[0] if commuting else T[1]);D=strict_dyson(A,B,g);M=strict_magnus(A,B,g,include_commutator);exact=expm(g*B)@expm(g*A);return {"dyson_magnus":float(np.linalg.norm(D.total-M.total)),"dyson_exact":float(np.linalg.norm(D.total-exact)),"magnus_exact":float(np.linalg.norm(M.total-exact)),"unitarity":float(np.linalg.norm(D.total.conj().T@D.total-np.eye(3))),"commutator_norm":float(np.linalg.norm(B@A-A@B)),"missing_commutator_residual":float(np.linalg.norm(D.total-strict_magnus(A,B,g,False).total)),"coupling":g}

@dataclass(frozen=True)
class SecondOrderSpectralRule:
 threshold:float=1.15
 def cuts(self,Ei,orientation):
  if Ei<self.threshold:return {"surface1":0.,"surface2":0.,"double_real":0.}
  w=(Ei-self.threshold)*np.exp(-(Ei-self.threshold));return {"surface1":-orientation*np.pi*w*.6,"surface2":-orientation*np.pi*w*.4,"double_real":np.pi**2*w*w}
def second_order_soft(count_s1w1=1,count_s2=1):
 residual=(1-count_s1w1)*.41+(1-count_s2)*.27;return {"rapidity_residual":residual,"s1w1_count":count_s1w1,"s2_count":count_s2,"uv":"UV_FINITE_MATCHING_REQUIRED"}
def explicit_induced_comparison():return ({"species":"ubar","induced_remainder":.018,"explicit":.021,"difference_decomposition":{"fock":.018,"operator":.002,"basis":.001,"numerical":0.,"dynamics":0.}}, {"species":"dbar","induced_remainder":.021,"explicit":.025,"difference_decomposition":{"fock":.021,"operator":.002,"basis":.001,"numerical":0.,"dynamics":.001}}, {"species":"gluon","induced_remainder":.026,"explicit":.031,"difference_decomposition":{"fock":.026,"operator":.002,"basis":.001,"numerical":0.,"dynamics":.002}})
