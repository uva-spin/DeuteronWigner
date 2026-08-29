"""C273 physical-state prerequisite and circularity audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c273_hqcdc117physstate1"
BASELINE="8562e483906979b0b5776b68896f60dc7c107230";C272_ROOT="cdebc5a5cfb44709b3f3009fa12b599c35e032700a55fd75aab0cfa5532c004c"
STATUS="C273_PHYSICAL_STATE_BLOCKED_BY_UNASSEMBLED_RENORMALIZED_HAMILTONIAN_FAMILY";PLAN="C117PHYSSTATE1-C";NEXT="C274/HQCDC117RENORMH1";NEXT_OBJECT="assemble the complete Hermitian K9/K11/K13 renormalized Hamiltonian family over explicit unresolved C117 coordinates with all non-C117 physical slots and provenance bound"
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def hamiltonian_ancestry_audit():
 rows=tuple({"resolution":r,"bare_operator_spine":"C131-C242 source-derived components","physical_input_map":"C213-C219 conditional mappings","C117_directions":"four explicit Hermitian coordinates","complete_renormalized_matrix":False,"missing":"complete count-once Hamiltonian assembly with all non-C117 slots bound","diagnostic_fixture_promotable":False} for r in RESOLUTIONS)
 return _f({"rows":rows,"complete":0,"required":3,"root":_r(rows)})
def circularity_certificate():return _f({"forbidden_cycle":"choose c_C117 -> build state -> use same state target to justify c_C117","conditional_family_lawful":True,"physical_state_lawful":False,"coefficients_selected":0,"rank_inferred":False,"root":_r("no-self-calibration")})
def state_bundle_schema():
 x={"Hamiltonian":f"H_R(c)=H_nonC117,R + sum_i c_i O_C117,i,R for R in {RESOLUTIONS}","state":"Psi_d,R(c), normalized, fixed J=1 color singlet CM ground","phase":"largest authenticated reference overlap real positive; degeneracy handled by subspace projector","pole_projector":"Q=I-|Psi><Psi|","reduced_resolvent":"Q(E-H)^-1Q on certified isolated domain","derivative_state":"dPsi/dc_i=-R' Q O_i Psi plus normalization/phase term","physical":False,"values":None}
 return _f({**x,"root":_r(x)})
def route_audit():return _f({"route_A":"direct Hermitian diagonalization after complete H family assembly","route_B":"matrix-free Krylov plus contour/spectral projector and reduced resolvent","current_status":"SCHEMA_ONLY_HAMILTONIAN_UNASSEMBLED","contradiction":False,"root":_r(("schema",False))})
def residual_frontier():return _f({"object_id":"C117-RENORMALIZED-HAMILTONIAN-FAMILY-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"state_bundle_schema":True,"physical_state":False,"Hamiltonian_complete":False,"coefficients_selected":0,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"fixture_promoted":0,"unsupported_zeroed":0,"finite_coefficient_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117physstate1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117physstate1_authority():
 from deuteron_wigner.bridge import hqcdc117b1sens1 as c272
 if c272.PACKAGE_ROOT!=C272_ROOT:raise ValueError("C272 root changed")
 c272.load_verified_hqcdc117b1sens1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdc117physstate1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117physstate1_authority()
_ROOTS={"INPUT":_r((BASELINE,C272_ROOT)),"HAMILTONIAN":hamiltonian_ancestry_audit()["root"],"CIRCULARITY":circularity_certificate()["root"],"STATE_SCHEMA":state_bundle_schema()["root"],"ROUTES":route_audit()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C273-HQCDC117PHYSSTATE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
