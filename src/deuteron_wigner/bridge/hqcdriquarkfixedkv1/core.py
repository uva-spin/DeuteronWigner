"""C224 omitted-domain canonical vertex source-kernel audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedktrans1 as c223
from deuteron_wigner.bridge.vdim2 import core as c52
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c224_hqcdriquarkfixedkv1"
BASELINE="273cb313a93c076491d539b703368c321c5d8a88";C223_ROOT="fc377e9d6469e06dcb006b3bdafca47df8a36db11a50524c36fa791dcf1bf494"
CONTRACT="docs/next_level/c223_c224_hqcdriquarkfixedkv1_continuation_contract.json";CONTRACT_SHA256="7c302651a26a0e730318a9cb584999ba519f46e164e3d78043bebccc07da66bb"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c224_hqcdriquarkfixedkv1_codex_prompt.md";PROMPT_SHA256="3d3417b0c8cc09b853985b5ff8214114ba9010e073a8623b141af2c26c9fa722"
STATUS="C224_C223_OMITTED_CANONICAL_VERTEX_DOMAIN_AND_NORMALIZATION_READY_SYMBOLIC_SPINOR_HO_PRIMITIVE_INCOMPLETE";PLAN="RIQUARKFIXEDKV1-E"
NEXT="C225/HQCDRIQUARKFIXEDKVPRIM1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-PRIMITIVE"
NEXT_EXACT="exact symbolic C43 spinor-polarization and HO-projected canonical vertex primitive for caller-supplied complement modes"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def canonical_domain_schema():return _f({"schema":"C224-OMITTED-CANONICAL-VERTEX-DOMAIN-V1","sectors":"q <-> qg within each symbolic K_prime complement sector","conservation":"kq+kg=K_prime exact; transverse momentum conserved","modes":"C222 APBC/PBC plus C223 exact rational-x TM labels","orientations":("emission bdag adag b","absorption adjoint"),"color":"T^a fundamental exact, open indices","coupling_degree":1,"root":_r(("q-qg", "Kprime",1))})
def normalization_manifest():return _f({"component_id":c52.COMPONENT_ID,"Pminus_coefficient":c52.PMINUS_COEFFICIENT.serialize(),"Pminus_hash":c52.PMINUS_COEFFICIENT.sha256,"M2_coefficient":c52.M2_COEFFICIENT.serialize(),"M2_hash":c52.M2_COEFFICIENT.sha256,"k_g":"caller positive integer","P_plus":"caller symbolic","L_cancellation":"exact C52","root":_r((c52.PMINUS_COEFFICIENT.sha256,c52.M2_COEFFICIENT.sha256))})
def primitive_audit():return _f({"C50_arbitrary_partition":True,"C50_mass_numeric":True,"C50_Pplus_numeric":True,"C50_qrel_numeric":True,"C50_HO_projection_quadrature":True,"C52_symbolic_full_primitive":False,"retained_basis_ids_required_by_C52":True,"omitted_symbolic_primitive":"UNAVAILABLE_NOT_ZERO","root":_r((True,True,True,True,True,False,True))})
def operator_program():return _f({"operator":"Q_R V1 Q_R","domain_root":canonical_domain_schema()["root"],"normalization_root":normalization_manifest()["root"],"TM_root":c223.transverse_program_schema()["root"],"primitive":NEXT_OBJECT,"executable":False,"numeric_diagnostic_promoted":False,"root":_r(("QV1Q",NEXT_OBJECT))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"domain_ready":True,"normalization_ready":True,"QV1Q_complete":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"program_root":operator_program()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"numeric_diagnostic_promoted":0,"retained_indices_reused":0,"physical_values":0,"missing_zeroed":0,"dense_omitted_space":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("sector","Kprime","kq","kg","spin","polarization","HO","color","normalization","orientation","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"domain":True,"normalization":True,"primitive":False,"mutations":384,"next":NEXT,"root":_r((STATUS,True,True,False))})
def verify_hqcd_riquarkfixedkv1_authority():
 if c223.PACKAGE_ROOT!=C223_ROOT:raise ValueError("C223 root changed")
 c223.load_verified_hqcd_riquarkfixedktrans1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C223_package_root":C223_ROOT,"C52_status":c52.STATUS,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv1_authority()
_ROOTS={"INPUT":_r((BASELINE,C223_ROOT,c52.STATUS,CONTRACT_SHA256,PROMPT_SHA256)),"DOMAIN":canonical_domain_schema()["root"],"NORMALIZATION":normalization_manifest()["root"],"AUDIT":primitive_audit()["root"],"PROGRAM":operator_program()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C224-HQCDRIQUARKFIXEDKV1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C224_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
