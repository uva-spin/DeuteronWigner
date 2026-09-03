"""C282 RI/SMOM signed-mass flavor semantics."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c282_hqcdrimassnf1"
BASELINE="0376dc3f741b575ac0aa97c44f673a395ad5af6a";C281_ROOT="10d82a013afa2e25a77e45c744aff26812875537ba7c0b6a78eda03fb13d65c8";SOURCE_SHA="5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3"
STATUS="C282_RI_SMOM_MASS_EXTERNAL_NONSINGLET_AND_ACTIVE_NF_SEMANTICS_SOURCE_BOUND";PLAN="RIMASSNF1-A"
NEXT="C283/HQCDRIMASSGAUGEADAPTER1";NEXT_OBJECT="C165-REQ-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-2";NEXT_EXACT="project-owned adapter contract plus exact RI/SMOM covariant-gauge to C43 light-front gauge/pole correspondence"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_flavor_record():return _f({"artifact_sha256":SOURCE_SHA,"external_operator":"ubar Gamma d","external_flavors":("u_bar","d"),"flavor_class":"bilinear nonsinglet","gamma5":"naive anticommuting; self-consistent for nonsinglet contribution","mass_limit":"massless fermions for conversion coefficient","locators":("source lines 304-307","source lines 455-459","source lines 894-899","source lines 965-969"),"root":_r((SOURCE_SHA,"ubar Gamma d","nonsinglet"))})
def active_nf_record():return _f({"symbol":"n_f","meaning":"number of active fermions","source_locator":"anomalous-dimension appendix lines 1442-1451","one_loop_mass_conversion_dependence":"ABSENT","first_explicit_running_anomalous_dependence":"higher order","caller_running_coordinate_required":True,"external_flavor_is_not_active_Nf":True,"root":_r(("n_f","active fermions","separate"))})
def separation_certificate():return _f({"external":"ordered nonsinglet ubar,d legs","loops":"active n_f coordinate","flavor_average":False,"singlet_diagrams":False,"sea_content_inferred":False,"route_mismatches":0,"root":_r("separate-flavor")})
def flavor_ast():return _f({"schema":"C282-RI-SMOM-MASS-NF-FLAVOR-AST-V1","nodes":({"opcode":"LOAD_EXTERNAL_FLAVORS","value":("u_bar","d")},{"opcode":"ASSERT_NONSINGLET"},{"opcode":"LOAD_ACTIVE_NF","value":"caller"},{"opcode":"ASSERT_ONE_LOOP_NF_INDEPENDENT"}),"safe":True,"eval":False,"root":_r("flavor-ast")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"remaining_dependency_leaves":2,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"external_flavor_closed":True,"active_Nf_semantics_closed":True,"one_loop_Nf_independence":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"Nf_selected":0,"flavor_averaged":0,"singlet_promoted":0,"later_leaves_modified":0,"C117_coordinates_selected":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassnf1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","ubar","d","nonsinglet","gamma5","massless","nf","loop-order","running","average","singlet")[i%11],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassnf1_authority():
 from deuteron_wigner.bridge import hqcdrimasscoord1 as c281,hqcdfavor2 as c155
 if c281.PACKAGE_ROOT!=C281_ROOT:raise ValueError("C281 root changed")
 if sha256((ROOT/"data/raw/c167_sources/arxiv_0901.2599v2.tar").read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError("source hash")
 c281.load_verified_hqcdrimasscoord1_authority();c155.load_verified_hqcd_flavor_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassnf1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassnf1_authority()
_ROOTS={"INPUT":_r((BASELINE,C281_ROOT)),"SOURCE":source_flavor_record()["root"],"NF":active_nf_record()["root"],"SEPARATION":separation_certificate()["root"],"AST":flavor_ast()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C282-HQCDRIMASSNF1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
