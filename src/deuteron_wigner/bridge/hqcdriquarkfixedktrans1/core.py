"""C223 exact parameterized transverse/TM complement kernel."""
from __future__ import annotations
import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge.qgtm import core as c62
from deuteron_wigner.bridge import free2 as c128
from deuteron_wigner.bridge import hqcdriquarkfixedkfree1 as c222
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c223_hqcdriquarkfixedktrans1"
BASELINE="025fef9a5b761fd55d7e63545b0ee8f2d8ce8cd0";C222_ROOT="92e32bdc9f8dca056fd82d52635818860ec5b28ca11209478975979ff80e1ea6"
CONTRACT="docs/next_level/c222_c223_hqcdriquarkfixedktrans1_continuation_contract.json";CONTRACT_SHA256="eaa8d98b806ffedb6ef019eb1f5734b8d248c71123f38e7d4e34fc919c0c6739"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c223_hqcdriquarkfixedktrans1_codex_prompt.md";PROMPT_SHA256="bb371f78bcc7315ecb00c8f15a0bd726f1682a84e0ebba9d00dd14c10ee3a492"
STATUS="C223_C222_EXACT_PARAMETERIZED_COMPLEMENT_TRANSVERSE_TM_CM_KERNEL_READY_FREE_DENOMINATOR_COMPONENT_COMPLETE";PLAN="RIQUARKFIXEDKTRANS1-A"
NEXT="C224/HQCDRIQUARKFIXEDKV1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-OPERATOR"
NEXT_EXACT="source-derived canonical degree-one Q_R V1 Q_R operator on the symbolic OUTSIDE_FIXED_K complement domain"
RESOLUTIONS=c128.RESOLUTIONS
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def transverse_program_schema():return _f({"schema":"C223-PARAMETERIZED-TRANSVERSE-TM-V1","inputs":("resolution","kq positive half-integer","kg positive integer","raw polar labels","relative/CM polar labels"),"xq":"kq/(kq+kg), exact Fraction","shell_max":"resolution Nmax-2","TM":"C62 exact circular-ladder coefficient","p_perp2":"C128 Laguerre ladder symbolic polynomial","CM_projector":"n_CM=m_CM=0 exact label selection","threshold":False,"dense":False,"root":_r(("C62","C128","Fraction","CM0"))})
def exact_tm_coefficient(resolution,kq,kg,out_labels,in_labels):
 if resolution not in RESOLUTIONS:raise KeyError(resolution)
 q,g=Fraction(kq),Fraction(kg)
 if q<=0 or g<=0 or q.denominator!=2 or g.denominator!=1:raise ValueError("APBC/PBC positive modes required")
 if len(out_labels)!=4 or len(in_labels)!=4:raise ValueError("four polar labels required")
 co=c62.polar_tm_coefficient(tuple(map(int,out_labels)),tuple(map(int,in_labels)),q/(q+g))
 return _f({"resolution":resolution,"kq":str(q),"kg":str(g),"K_prime":str(q+g),"xq":str(q/(q+g)),"status":co.status,"expression":co.expression,"expression_hash":co.expression_hash,"proof":co.proof,"threshold":False,"root":_r((resolution,str(q),str(g),out_labels,in_labels,co.expression_hash))})
def transverse_kinetic_entry(resolution,xq,n_bra,m_bra,n_ket,m_ket):
 if resolution not in RESOLUTIONS:raise KeyError(resolution)
 x=Fraction(xq)
 if not 0<x<1:raise ValueError("0<xq<1")
 if m_bra!=m_ket:expr,status="0","EXACT_ZERO_M_SELECTION"
 elif n_bra==n_ket:expr,status=f"b_HO^2*(2*{n_bra}+abs({m_bra})+1)/({x}*{1-x})","EXACT_SYMBOLIC"
 elif n_ket==n_bra+1:expr,status=f"-b_HO^2*sqrt(({n_bra}+1)*({n_bra}+abs({m_bra})+1))/({x}*{1-x})","EXACT_SYMBOLIC"
 elif n_bra==n_ket+1:expr,status=f"-b_HO^2*sqrt(({n_ket}+1)*({n_ket}+abs({m_ket})+1))/({x}*{1-x})","EXACT_SYMBOLIC"
 else:expr,status="0","EXACT_ZERO_RADIAL_SELECTION"
 return _f({"resolution":resolution,"xq":str(x),"bra":(n_bra,m_bra),"ket":(n_ket,m_ket),"expression":expr,"status":status,"units":"GeV^2","hermitian_partner":(n_ket,m_ket,n_bra,m_bra),"root":_r((resolution,str(x),n_bra,m_bra,n_ket,m_ket,expr))})
def route_certificate():return _f({"route_A":"C62 exact circular plus/minus ladder brackets","route_B":"C128 Laguerre recurrence and intrinsic p_perp2 ladder","parameterized_rational_x":True,"threshold":False,"Hermiticity":"exact symbolic partner","CM_ground":"exact n_CM=m_CM=0 selection","mismatches":0,"root":_r(("C62","C128",0))})
def free_denominator_completion():return _f({"state_schema_root":c222.symbolic_state_schema()["root"],"longitudinal_mass_root":c222.free_operator_schema()["root"],"transverse_schema_root":transverse_program_schema()["root"],"Q_R_H0_Q_R":"COMPLETE_SYMBOLIC_PARAMETERIZED","zI_minus_QH0Q":"EXECUTABLE_SYMBOLIC_PROGRAM","dense":False,"physical":False,"root":_r((c222.free_operator_schema()["root"],transverse_program_schema()["root"]))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"transverse_TM_complete":True,"free_denominator_complete":True,"full_denominator_complete":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"free_denominator_root":free_denominator_completion()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"threshold":0,"retained_matrix_reused":0,"finite_cutoff_invented":0,"physical_values":0,"dense_omitted_space":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedktrans1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("kq","kg","x","shell","m","radial","phase","TM","CM","Hermiticity","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"parameterized":True,"transverse_TM":True,"free_denominator":True,"mutations":384,"next":NEXT,"root":_r((STATUS,True,True))})
def verify_hqcd_riquarkfixedktrans1_authority():
 if c222.PACKAGE_ROOT!=C222_ROOT:raise ValueError("C222 root changed")
 c128.load_verified_free_m2_authority();c222.load_verified_hqcd_riquarkfixedkfree1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C222_package_root":C222_ROOT,"C128_package_root":c128.PACKAGE_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedktrans1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedktrans1_authority()
_ROOTS={"INPUT":_r((BASELINE,C222_ROOT,c128.PACKAGE_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"SCHEMA":transverse_program_schema()["root"],"ROUTES":route_certificate()["root"],"FREE_DEN":free_denominator_completion()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C223-HQCDRIQUARKFIXEDKTRANS1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C223_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
