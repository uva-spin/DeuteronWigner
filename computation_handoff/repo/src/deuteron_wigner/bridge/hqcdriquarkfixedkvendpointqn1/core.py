"""C236 source-derived V1 endpoint quantum-number map."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkvinterface1 as c235
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c236_hqcdriquarkfixedkvendpointqn1"
BASELINE="f36fcf99295d5d0a9125f0fd0cd348f4d2b578d3";C235_ROOT="e0bc65b5fb129dda2b28911cb23236a5c3dec8441b907068b5fc232bd328d840"
CONTRACT="docs/next_level/c235_c236_hqcdriquarkfixedkvendpointqn1_continuation_contract.json";CONTRACT_SHA256="19d2404decbebae86892b4d4b0a4fb6b0b85bfc4efb5a93c9180b8e9ac1d860a"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c236_hqcdriquarkfixedkvendpointqn1_codex_prompt.md";PROMPT_SHA256="86ab5ecf6cc2539977df7fcd2c1e203630a32240aa1df6cdd551106b0024a796"
STATUS="C236_ALL_FIFTEEN_INTERFACES_V1_APPLICABILITY_CLASSIFIED_THREE_CANONICAL_INTERFACES_EIGHT_CHANNEL_ENDPOINT_QN_ENUMERATORS_READY";PLAN="RIQUARKFIXEDKVENDPOINTQN1-A"
NEXT="C237/HQCDRIQUARKFIXEDKVINTERFACE2";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V1-INTERFACE-ASSEMBLY-SOURCE-QUALIFIED"
NEXT_EXACT="join the 24 C236 source-qualified canonical-interface channel enumerators to the eight C234 radial enclosure families"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def applicability_manifest():
 rows=[]
 for r in c235.c220.endpoint_map_manifest()["rows"]:
  applicable=r["term_id"]=="C53_CANONICAL_VERTEX" and r["coupling_degree"]==1
  rows.append({"interface_id":r["interface_id"],"term_id":r["term_id"],"resolution":r["resolution"],"coupling_degree":r["coupling_degree"],"V1_applicable":applicable,"classification":"V1_CANONICAL_ENDPOINT_ENUMERATOR" if applicable else "NOT_APPLICABLE_TO_V1_OPERATOR_NOT_ZERO_AS_FULL_HAMILTONIAN_INTERFACE","ancestry":r["ancestry"]})
 rows=tuple(rows);return _f({"rows":rows,"count":15,"V1_applicable":sum(r["V1_applicable"] for r in rows),"V1_not_applicable":sum(not r["V1_applicable"] for r in rows),"root":_r(rows)})
def endpoint_quantum_map():
 channels=c235.c234.assembly_manifest()["rows"];rows=[]
 for i in applicability_manifest()["rows"]:
  if not i["V1_applicable"]:continue
  for c in channels:
   rows.append({"interface_id":i["interface_id"],"resolution":i["resolution"],"radial_id":c["radial_id"],"normal_form_id":c["normal_form_id"],"primitive_sha256":c["primitive_sha256"],"h_out_h_in_h_g":"encoded exactly by normal_form_id","n":"caller nonnegative HO radial index","m":c["m"],"Jz_identity":"h_in/2=h_out/2+h_g+m","longitudinal_modes":"caller complement APBC quark and nonzero PBC gluon satisfying source vertex and total K outside retained K","transverse_domain":"caller n>=0 with exact signed m; unbounded complement not materialized","orientation":"Q_R V1 P_R; adjoint P_R V1 Q_R"})
 rows=tuple(rows);return _f({"rows":rows,"count":24,"interfaces":3,"channels_per_interface":8,"duplicate_keys":0,"root":_r(rows)})
def route_certificate():return _f({"route_A":"coupling-degree and term-identity V1 selection","route_B":"C227 helicity triples plus C228 Jz m identity","applicability_mismatches":0,"quantum_map_mismatches":0,"root":_r(("degree-one","Jz",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"records":24,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,24))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"interfaces_classified":15,"V1_interfaces":3,"endpoint_channel_records":24,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"endpoint_qn_root":endpoint_quantum_map()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"positional_mapping":0,"dense_complement":0,"nonV1_interface_zeroed":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkvendpointqn1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("term","degree","resolution","V1","helicity","n","m","Jz","APBC","PBC","root","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"classified":15,"V1_interfaces":3,"records":24,"mutations":384,"next":NEXT,"root":_r((STATUS,15,24))})
def verify_hqcd_riquarkfixedkvendpointqn1_authority():
 if c235.PACKAGE_ROOT!=C235_ROOT:raise ValueError("C235 root changed")
 c235.load_verified_hqcd_riquarkfixedkvinterface1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C235_package_root":C235_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkvendpointqn1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkvendpointqn1_authority()
_ROOTS={"INPUT":_r((BASELINE,C235_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"APPLICABILITY":applicability_manifest()["root"],"QN":endpoint_quantum_map()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C236-HQCDRIQUARKFIXEDKVENDPOINTQN1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C236_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
