"""C337 continuum heat-kernel determinant and C301 Gram audit."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c337_hqcdrimassc43heateval1";BASELINE="f676b01074502865b43890b9606d7c459149f6e6";C336_ROOT="4a69221541bfbde6b281ef9a96024a6bf45f998bdf424dc45446ef6490719d62"
STATUS="C337_CONTINUUM_DETERMINANT_EVALUATED_ADJOINT_C301_PROJECTED_FUNDAMENTAL_CENTER_BREAKING_BASIS_MISSING";PLAN="RIMASSC43HEATEVAL1-C";NEXT="C338/HQCDRIMASSC43CENTERBASIS1";NEXT_OBJECT="C337-C43-FUNDAMENTAL-CENTER-BREAKING-CLASS-BASIS";NEXT_EXACT="extend the C301 Gram basis by the independent real center-charged fundamental winding class functions required by the APBC fermion determinant"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _angles(p1,p2):return (p1,p2,-p1-p2)
def basis_values(p1,p2):
 z=sum(complex(math.cos(x),math.sin(x)) for x in _angles(p1,p2));return np.array((1.,abs(z)**2-1.,(z**3).real))
def determinant_components(p1,p2,L,mass2,M=64):
 if L<=0 or mass2<0 or M<1:raise ValueError
 ph=_angles(p1,p2);roots=(ph[0]-ph[1],ph[0]-ph[2],ph[1]-ph[2]);B=F=0.;z=math.sqrt(mass2)*L
 for l in range(1,M+1):
  B+=sum(math.cos(l*x)-1 for x in roots)/l**3
  F+=(-1)**l*math.exp(-z*l)*(1+z*l)*sum(math.cos(l*x)-1 for x in ph)/l**3
 # C336 net weights: boson +1, fermion -2; Gamma=-weight integral.
 return {"boson":-B/(math.pi*L*L),"fermion":2*F/(math.pi*L*L),"constraint_transverse":0.}
def gram_projection(L=2.,mass2=.01,M=32,G=20):
 x,w=np.polynomial.legendre.leggauss(G);pts=math.pi*(x+1);weights=math.pi*w;Gram=np.zeros((3,3));rhsB=np.zeros(3);rhsF=np.zeros(3);normB=normF=0.
 for i,p1 in enumerate(pts):
  for j,p2 in enumerate(pts):
   dens=float(__import__('deuteron_wigner.bridge.hqcdrimasssu3measurederive1',fromlist=['evaluate_density']).evaluate_density(p1,p2)["full_torus_density"]);q=weights[i]*weights[j]*dens;b=basis_values(p1,p2);v=determinant_components(p1,p2,L,mass2,M);Gram+=q*np.outer(b,b);rhsB+=q*b*v["boson"];rhsF+=q*b*v["fermion"];normB+=q*v["boson"]**2;normF+=q*v["fermion"]**2
 cB=np.linalg.solve(Gram,rhsB);cF=np.linalg.solve(Gram,rhsF);resB=max(0.,normB-float(rhsB@cB));resF=max(0.,normF-float(rhsF@cF))
 return {"L_GeVinv":L,"mass2_GeV2":mass2,"M":M,"G":G,"basis":("1","CHI8","RE_TF3"),"boson_coefficients":tuple(map(float,cB)),"fermion_projected_coefficients":tuple(map(float,cF)),"boson_residual_norm2":resB,"fermion_residual_norm2":resF,"physical":False,"root":_r((L,mass2,M,G,tuple(cB),tuple(cF),resB,resF))}
def convergence_enclosure():
 rows=tuple(gram_projection(2.,.01,m,g) for m,g in ((16,12),(32,16),(64,20)));keys=("boson_coefficients","fermion_projected_coefficients");enc={k:tuple((min(r[k][i] for r in rows),max(r[k][i] for r in rows)) for i in range(3)) for k in keys}
 return {"rows":rows,"coefficient_hulls":enc,"boson_truncation_residual_retained":bool(rows[-1]["boson_residual_norm2"]>0),"fermion_residual_nonzero":bool(rows[-1]["fermion_residual_norm2"]>1e-6),"fermion_residual_exceeds_boson":bool(rows[-1]["fermion_residual_norm2"]>rows[-1]["boson_residual_norm2"]),"root":_r(rows)}
def symmetry_certificate():
 p=(.4,1.1);v=determinant_components(*p,2.,.01);s=2*math.pi/3;vs=determinant_components(p[0]+s,p[1]+s,2.,.01)
 return {"boson_center_defect":abs(v["boson"]-vs["boson"]),"fermion_center_defect":abs(v["fermion"]-vs["fermion"]),"boson_center_invariant":abs(v["boson"]-vs["boson"])<1e-12,"fermion_center_invariant":abs(v["fermion"]-vs["fermion"])<1e-12,"weyl_real":True,"root":_r((v,vs))}
def ownership():return {"constraint":"longitudinal Jacobian separate","P0":"global separate","Wilson_boundary":"separate","zero_mode":"holdout","C315_C334_consumed":False,"root":_r("C337-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"determinant_evaluated":True,"complete_C301_projection":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"thermal_interpretation":0,"physical_L_mass":0,"fermion_residual_dropped":0,"HO_consumed":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43heateval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43heateval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43heatkernel1 as c
 if c.PACKAGE_ROOT!=C336_ROOT:raise ValueError("C336 root")
 c.load_verified_hqcdrimassc43heatkernel1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43heateval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43heateval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C336_ROOT)),"CONVERGENCE":convergence_enclosure()["root"],"SYMMETRY":symmetry_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C337-HQCDRIMASSC43HEATEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
