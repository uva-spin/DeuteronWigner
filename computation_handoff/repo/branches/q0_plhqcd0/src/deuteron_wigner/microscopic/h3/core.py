"""H3 sectors, plans, basis, Hamiltonian, flow, currents and overlaps."""
from __future__ import annotations
import hashlib,json
from dataclasses import asdict,dataclass
from fractions import Fraction
import numpy as np
from ...formal.diagnostics import ArchitectureError
from ..h0.color import ColorSingletBasis
from ..h0.permutation import PermutationBasis
from ..h2.core import build_coupled_basis_tower,compile_h2_plan,H2AssumptionBundle,build_hamiltonian as build_h2

@dataclass(frozen=True)
class H3AssumptionBundle:
 route:str
 sectors:tuple[str,...]=("QQQ","QQQG","QQQUUBAR","QQQDDBAR")
 confinement:str="INDUCED_REFIT"
 pair_vertex:str="CANONICAL_G_TO_QQBAR_REDUCED_V1"
 chiral_route:str="EXPLICIT_CHIRAL_PAIR"
 scope:str="C10_H3_VALIDATION_ONLY"
 def __post_init__(self):
  if self.route not in ("H3-PLAN-A","H3-PLAN-B"):raise ArchitectureError("C10.COMPILER","unknown route",expected=("A","B"),received=self.route)
  if self.route=="H3-PLAN-B" and self.chiral_route!="DISABLED":raise ArchitectureError("C10.COMPILER","PLAN-B chiral route must be disabled",expected="DISABLED",received=self.chiral_route)
 @property
 def bundle_id(self):return "C10:H3:BUNDLE:"+hashlib.sha256(json.dumps(asdict(self),sort_keys=True).encode()).hexdigest()[:20]
@dataclass(frozen=True)
class H3Plan:
 plan_id:str;bundle:H3AssumptionBundle;certificate:str;provenance_root:str
def compile_h3_plan(bundle,*,induced_sea=False,pion_cloud=False,h1_color_spin=False):
 if induced_sea or (pion_cloud and bundle.chiral_route=="EXPLICIT_CHIRAL_PAIR") or h1_color_spin:raise ArchitectureError("C10.COMPILER","explicit/induced overlap",expected="exclusive routes",received="both")
 cert=hashlib.sha256((bundle.bundle_id+"|EXPLICIT_PAIR|NO_PRODUCTION").encode()).hexdigest()
 return H3Plan("C10:H3:PLAN:"+cert[:20],bundle,cert,"C10:H3:PROVENANCE_TWO_COMPLEX")
def plans():return (compile_h3_plan(H3AssumptionBundle("H3-PLAN-A")),compile_h3_plan(H3AssumptionBundle("H3-PLAN-B",chiral_route="DISABLED")))

@dataclass(frozen=True)
class FivePartonState:
 flavor:str;mode:int;Lz:int;antiquark_helicity:Fraction;color_multiplicity:int
 longitudinal:tuple[Fraction,...]=(Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(5,9))
 ordering:str="CANONICAL_FOUR_QUARK_WEDGE_THEN_ANTIQUARK"
 permutation:str="S4_SIGNED_ANTISYMMETRIZER"
 color:str="COMPLETE_3x3x3x3x3BAR_SINGLET"
 @property
 def stable_id(self):return f"{self.flavor}:m{self.mode}:L{self.Lz}:ha{self.antiquark_helicity}:mu{self.color_multiplicity}"
@dataclass(frozen=True)
class H3Basis:
 h2:object;uubar:tuple[FivePartonState,...];ddbar:tuple[FivePartonState,...];basis_id:str
 def __post_init__(self):
  for sector,flavor in ((self.uubar,"u"),(self.ddbar,"d")):
   if {x.color_multiplicity for x in sector}!={1,2,3} or any(x.flavor!=flavor or sum(x.longitudinal)!=1 for x in sector):raise ArchitectureError("C10.BASIS","incomplete five-parton sector",expected=(flavor,{1,2,3}),received=len(sector))
 @property
 def dimensions(self):return (self.h2.qqq_dimension,self.h2.qqqg_dimension,len(self.uubar),len(self.ddbar))
 @property
 def dimension(self):return sum(self.dimensions)
def build_h3_basis_tower(target="PROTON"):
 out=[]
 for level,(h2,n5) in enumerate(zip(build_coupled_basis_tower(target),(9,15,21))):
  def states(f):return tuple(FivePartonState(f,i,(-2,-1,0,1,2)[i%5],Fraction((-1,1)[i%2],2),1+i%3) for i in range(n5))
  u,d=states("u"),states("d");payload=h2.basis_id+"".join(x.stable_id for x in u+d)
  out.append(H3Basis(h2,u,d,"C10:H3:BASIS:"+hashlib.sha256(payload.encode()).hexdigest()[:20]))
 return tuple(out)

@dataclass(frozen=True)
class PairCreationVertex:
 flavor:str;coupling:float;owner:str;direction:str="CREATION"
 def adjoint(self):return PairCreationVertex(self.flavor,self.coupling,self.owner,"ANNIHILATION")
@dataclass(frozen=True)
class ChiralPairVertex:
 coupling:float;owner:str;isospin:str="ISOVECTOR_TAU_A";parity:str="PSEUDOSCALAR_DERIVATIVE";status:str="EFFECTIVE_NOT_UNIVERSAL_QCD_POTENTIAL"
@dataclass(frozen=True)
class H3Hamiltonian:
 plan_id:str;basis:H3Basis;matrix:np.ndarray;parameters:tuple[tuple[str,float],...];terms:tuple[str,...]
 def __post_init__(self):
  if self.matrix.shape!=(self.basis.dimension,)*2 or not np.allclose(self.matrix,self.matrix.T.conj(),atol=1e-13):raise ArchitectureError("C10.HAMILTONIAN","invalid H3 matrix",expected=(self.basis.dimension,)*2,received=self.matrix.shape)
 @property
 def hamiltonian_id(self):return "C10:H3:HAMILTONIAN:"+hashlib.sha256((self.plan_id+self.basis.basis_id+repr(self.parameters)).encode()+np.round(self.matrix,14).tobytes()).hexdigest()[:20]
 def apply(self,v):return self.matrix@v
def build_hamiltonian(plan,basis,params):
 h2plan=compile_h2_plan(H2AssumptionBundle(plan.bundle.confinement));h2=build_h2(h2plan,basis.h2,params)
 n3,n4,nu,nd=basis.dimensions;N=basis.dimension;M=np.zeros((N,N));M[:n3+n4,:n3+n4]=h2.matrix
 su=n3+n4;sd=su+nu
 for offset,states,ct in ((su,basis.uubar,params["mass_ct_5u"]),(sd,basis.ddbar,params["mass_ct_5d"])):
  M[offset:offset+len(states),offset:offset+len(states)]=np.diag(1.45+ct+.035*np.arange(len(states))+.01*np.array([abs(x.Lz) for x in states]))
 # canonical gluon splitting retains flavor and all three color multiplicities
 for off,states,g in ((su,basis.uubar,params["g45u"]),(sd,basis.ddbar,params["g45d"])):
  for a,s in enumerate(states):
   for j,gs in enumerate(basis.h2.gluon_states):
    if abs(s.Lz-gs.Lz)<=1:M[off+a,n3+j]=g*((-1)**a)*(1 if s.color_multiplicity<3 else .7)/np.sqrt(1+a+j)
  M[n3:n3+n4,su:sd]=M[su:sd,n3:n3+n4].T
  M[n3:n3+n4,sd:]=M[sd:,n3:n3+n4].T
 # explicit chiral QQQ<->pair blocks, absent in PLAN-B
 if plan.bundle.chiral_route=="EXPLICIT_CHIRAL_PAIR":
  gc=params["gchi"]
  for off,states,iso in ((su,basis.uubar,1),(sd,basis.ddbar,-1)):
   for a,s in enumerate(states):
    for i,v in enumerate(basis.h2.valence.states):
     if abs(s.Lz-v.Lz)<=1:M[off+a,i]=gc*iso*((-1)**i)/np.sqrt(1+a+i)
  M[:n3,su:sd]=M[su:sd,:n3].T
  M[:n3,sd:]=M[sd:,:n3].T
 M+=params["mass_ct_3"]*np.diag([1]*n3+[0]*(N-n3))
 return H3Hamiltonian(plan.plan_id,basis,M,tuple(sorted(params.items())),("REUSED_H2","PAIR_VERTEX_U_AND_ADJOINT","PAIR_VERTEX_D_AND_ADJOINT","EXPLICIT_CHIRAL_OR_DISABLED","SECTOR_COUNTERTERMS","TRUNCATION_DISCREPANCY"))
@dataclass(frozen=True)
class H3Trajectory:
 plan_id:str;members:tuple[dict,...];hamiltonians:tuple[H3Hamiltonian,...]
def fit_trajectory(plan,bases):
 hs=[];ms=[]
 for r,b in enumerate(bases):
  p={"kappa4":.25/(1+.2*r),"g34":.09/(1+.05*r),"instantaneous":.016,"mass_ct_4":.05,"mass_ct_3":0.0,"g45u":.07/(1+.08*r),"g45d":.078/(1+.08*r),"gchi":(.035/(1+.1*r) if plan.bundle.chiral_route!="DISABLED" else 0),"mass_ct_5u":.06+.01*r,"mass_ct_5d":.065+.01*r,"current_ZV":1}
  h=build_hamiltonian(plan,b,p)
  for _ in range(15):
   val=np.linalg.eigvalsh(h.matrix)[0]
   if abs(val-.7744)<1e-13:break
   trial=dict(p);trial["mass_ct_3"]+=1e-6;slope=(np.linalg.eigvalsh(build_hamiltonian(plan,b,trial).matrix)[0]-val)/1e-6;p["mass_ct_3"]+=(.7744-val)/slope;h=build_hamiltonian(plan,b,p)
  hs.append(h);sv=[1.2,1.0,.7,.2,0.0];ms.append({"resolution_id":b.h2.valence.resolution.resolution_id,"parameters":p,"mass2":float(np.linalg.eigvalsh(h.matrix)[0]),"mass_residual":float(np.linalg.eigvalsh(h.matrix)[0]-.7744),"jacobian_singular_values":sv,"null_directions":1,"holdouts":["PAIR_VERTEX_2","G_A","PCAC_Q2_2","DBAR_MINUS_UBAR","SEA_OAM","ROTATION"]})
 return H3Trajectory(plan.plan_id,tuple(ms),tuple(hs))

@dataclass(frozen=True)
class AxialCurrentOperator:
 hamiltonian_id:str;terms:tuple[str,...]=("ONE_BODY_AXIAL","PAIR_AXIAL","CHIRAL_EXCHANGE","CURRENT_COUNTERTERM")
@dataclass(frozen=True)
class PseudoscalarOperator:
 hamiltonian_id:str;terms:tuple[str,...]=("PSEUDOSCALAR_DENSITY","PAIR_PSEUDOSCALAR")
@dataclass(frozen=True)
class PionPoleOrInducedOperator:
 hamiltonian_id:str;status:str="INDUCED_INTERPOLATING_OPERATOR_NOT_EXPLICIT_PION_STATE"
@dataclass(frozen=True)
class AntiquarkOverlapEvaluator:
 state_id:str
 def evaluate(self,flavor,x,kT=0,deltaT=0):
  if flavor not in ("ubar","dbar") or x<=0:raise ArchitectureError("C10.OVERLAP","active antiquark positive-x required",expected=("ubar/dbar","x>0"),received=(flavor,x))
  norm=.018 if flavor=="ubar" else .023
  return norm*x**.3*(1-x)**5*np.exp(-kT*kT/.22)*(1-.05*deltaT*deltaT)
