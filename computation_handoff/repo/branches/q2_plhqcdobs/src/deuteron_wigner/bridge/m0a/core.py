"""Deterministic C38 partonic-probe primitives; no matching kernel or hadron export."""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json, math
C38_BASELINE='0ac139f838960d77376b243733f267ab8d1fb507'; REGULATOR='O4-SPACELIKE-COLLINS-JMY'
READY='C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY'; NEXT='C39/R2B — finite-basis one-loop spacelike collinear correlator and matching difference'
def hash_(v): return sha256(json.dumps(asdict(v) if hasattr(v,'__dataclass_fields__') else v,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
@dataclass(frozen=True)
class PartonicProbeRootId:
 root_id:str='C38_FINITE_BASIS_PARTONIC_PROBE_ROOT'; color:str='fundamental'; hadron_identity:bool=False; probability:bool=False
 def __post_init__(self):
  if self.color!='fundamental' or self.hadron_identity or self.probability: raise ValueError('probe root must be nonhadronic fundamental')
 @property
 def sha256(self): return hash_(self)
@dataclass(frozen=True)
class OneQuarkState:
 flavor:str;color:int;helicity:int;K:int;Nmax:int;mode:tuple[int,int];norm:float
 def __post_init__(self):
  if self.color not in (0,1,2) or self.helicity not in (-1,1) or abs(self.norm-1)>1e-14: raise ValueError('invalid normalized fundamental quark')
@dataclass(frozen=True)
class QuarkGluonState:
 quark:OneQuarkState; adjoint_color:int; gluon_helicity:int; longitudinal_pair:tuple[int,int];norm:float
 def __post_init__(self):
  if not 0<=self.adjoint_color<8 or self.gluon_helicity not in (-1,1) or abs(self.norm-1)>1e-14: raise ValueError('invalid qg state')
@dataclass(frozen=True)
class SpacelikeWilsonInsertion:
 direction:tuple[float,float,float,float]; transverse_closure:bool; endpoints:bool; path_ordered:bool; finite_matrix_element:complex
 def __post_init__(self):
  if not all((self.transverse_closure,self.endpoints,self.path_ordered)) or self.direction[0]**2-self.direction[3]**2>=0: raise ValueError('incomplete spacelike path')
@dataclass(frozen=True)
class DistributionFunctional:
 K:tuple[int,...]; weights:tuple[float,...]
 def number_moment(self): return sum(self.weights)
 def __post_init__(self):
  if len(self.K)!=len(self.weights) or abs(self.number_moment()-1)>1e-14: raise ValueError('distributional partition failure')
def infrastructure():
 q=OneQuarkState('u',0,1,17,8,(0,0),1.0); qg=QuarkGluonState(q,3,-1,(9,8),1.0)
 w=SpacelikeWilsonInsertion((math.sinh(1),0,0,math.cosh(1)),True,True,True,complex(1,0))
 return q,qg,w,DistributionFunctional((17,23,31),(1/3,1/3,1/3))
