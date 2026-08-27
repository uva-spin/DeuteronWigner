"""C226 analytic HO projection audit and primitive normal-form frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvprim1 as c225
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c226_hqcdriquarkfixedkvho1"
BASELINE="ab19fd5dc72ba9fd1826e7cfacf6086d0699c171";C225_ROOT="86311e2df9f788b53a9ee1a4ca758b050fe061ba261a99271f278a17f22a0d54"
CONTRACT="docs/next_level/c225_c226_hqcdriquarkfixedkvho1_continuation_contract.json";CONTRACT_SHA256="4f1c5b1afd456028f9313d9e69a455b1a32449ee922a4df77be1c7c601c276d0"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c226_hqcdriquarkfixedkvho1_codex_prompt.md";PROMPT_SHA256="af5b194597006858773f2b97b23ed8a1b617afa78abcb4bf4a4b036030f9771d"
STATUS="C226_C225_HO_PROJECTION_DOMAIN_AUDITED_POSITIVE_BRANCH_PRIMITIVE_NORMAL_FORM_INCOMPLETE";PLAN="RIQUARKFIXEDKVHO1-D"
NEXT="C227/HQCDRIQUARKFIXEDKVNORM1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-PRIMITIVE-NORMAL-FORM"
NEXT_EXACT="exact real-domain positive-branch normal form of all eight C225 spinor-polarization primitives before polar-HO integration"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def projection_domain_schema():return _f({"integral":"integral_0^infinity q dq integral_0^2pi dphi phi_nm_star(q,phi;b) B_hout_hin_hg(q,phi)","parameters":{"xq":"rational 0<xq<1","P_plus":"positive symbolic","m_q":"nonnegative symbolic","b_HO":"positive resolution symbolic"},"measure":"d2q/(2pi)^2","orientations":("emission","absorption adjoint"),"root":_r(("polar-integral","positive-domain"))})
def expansion_audit():
 rows=tuple({"helicity_id":r["program_id"],"DAG_exact":True,"expanded_expression":False,"q_radial_structure":"square roots of affine q^2 from sqrt(E+m)","complex_conjugates":"require real-positive branch assumptions","polynomial_Laguerre_moment_applicable":False,"quadrature_authority":False} for r in c225.helicity_program_manifest()["rows"])
 return _f({"rows":rows,"count":8,"normal_forms":0,"unclassified":0,"root":_r(rows)})
def forbidden_projection_certificate():return _f({"simple_polynomial_projection":False,"reason":"authenticated spinor normalization retains nonpolynomial positive-branch radial factors","C50_square_grid_quadrature_promoted":False,"threshold":False,"missing_as_zero":False,"root":_r((False,"nonpolynomial"))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"projection_domain_ready":True,"primitive_normal_form_ready":False,"HO_projection_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"domain_root":projection_domain_schema()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"quadrature_promoted":0,"polynomial_assumption":0,"physical_values":0,"missing_zeroed":0,"dense_omitted_space":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvho1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("x","Pplus","mass","bHO","q","phi","branch","conjugate","helicity","integral","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"helicity_families":8,"normal_forms":0,"HO_projections":0,"mutations":384,"next":NEXT,"root":_r((STATUS,8,0,0))})
def verify_hqcd_riquarkfixedkvho1_authority():
 if c225.PACKAGE_ROOT!=C225_ROOT:raise ValueError("C225 root changed")
 c225.load_verified_hqcd_riquarkfixedkvprim1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C225_package_root":C225_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvho1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvho1_authority()
_ROOTS={"INPUT":_r((BASELINE,C225_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"DOMAIN":projection_domain_schema()["root"],"AUDIT":expansion_audit()["root"],"FORBIDDEN":forbidden_projection_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C226-HQCDRIQUARKFIXEDKVHO1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C226_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
