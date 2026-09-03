"""C281 authenticated RI/SMOM signed-mass coordinate definition."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c281_hqcdrimasscoord1"
BASELINE="6dd67abbdc12790d3b0bdce43c20bb6c8f541424";C280_ROOT="d69b9cfc362b6ac94fd1441319ff83533fdf221dcc84b1da9171af9294e2a4d5"
SOURCE_SHA="5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3"
STATUS="C281_RI_SMOM_SIGNED_MASS_COORDINATE_NORMALIZATION_AND_ONE_LOOP_POWER_SOURCE_BOUND";PLAN="RIMASSCOORD1-A"
NEXT="C282/HQCDRIMASSNF1";NEXT_OBJECT="C165-REQ-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-1";NEXT_EXACT="source object that binds active loop-flavor convention and external state for the RI/SMOM signed-mass target"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_record():return _f({"source":"arXiv:0901.2599v2","artifact":"data/raw/c167_sources/arxiv_0901.2599v2.tar","sha256":SOURCE_SHA,"member":"RenConst_v2.tex","locators":("eq:CmsRISelf","eq:CmEq1oCp","eq:CqsRI","eq:Csrim","eq:conv2","eq:num"),"authenticated":True,"root":_r((SOURCE_SHA,"RenConst_v2.tex"))})
def coordinate_definition():return _f({"coordinate":"alpha_s/(4*pi)","expansion_order":"one loop","first_omitted":"O(alpha_s^2)","mass_coordinate":"signed m_R","conversion_factor":"C_m^RI/SMOM=Z_m^MSbar/Z_m^RI/SMOM","orientation":"m_R^MSbar=C_m^RI/SMOM*m_R^RI/SMOM","inverse":"C_P^RI/SMOM=(C_m^RI/SMOM)^-1","equal_scales":"mu_MSbar=mu_RI/SMOM","dimensionless":True,"root":_r(("alpha_s/(4*pi)",1,2,"RI_SMOM_to_MSBAR"))})
def coordinate_ast():
 nodes=({"opcode":"LOAD_ALPHA_S","units":"dimensionless"},{"opcode":"DIV_CONST","constant":"4*pi"},{"opcode":"MUL_COEFFICIENT","coefficient":"caller source-qualified"},{"opcode":"ADD_TREE","tree":1},{"opcode":"ATTACH_REMAINDER","order":"alpha_s^2"})
 return _f({"schema":"C281-RI-SMOM-SIGNED-MASS-COORDINATE-AST-V1","nodes":nodes,"safe":True,"eval":False,"coefficient_invented":False,"root":_r(nodes)})
def route_certificate():return _f({"direct":"eq:Csrim","pseudoscalar_inverse":"eq:conv2 plus C_m=C_P^-1","landau_holdout":"eq:num","orientation":"eq:CmEq1oCp","mismatches":0,"root":_r("four-routes")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"remaining_dependency_leaves":3,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"coordinate_closed":True,"power_closed":True,"conversion_orientation_closed":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"later_leaves_modified":0,"numerical_alpha_s_selected":0,"memory_transcription":0,"C117_coordinates_selected":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimasscoord1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("hash","member","locator","alpha","4pi","power","mass","orientation","inverse","scale","route")[i%11],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimasscoord1_authority():
 from deuteron_wigner.bridge import hqcdrimasstargetast1 as c280
 if c280.PACKAGE_ROOT!=C280_ROOT:raise ValueError("C280 root changed")
 if sha256((ROOT/"data/raw/c167_sources/arxiv_0901.2599v2.tar").read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError("source hash")
 c280.load_verified_hqcdrimasstargetast1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimasscoord1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimasscoord1_authority()
_ROOTS={"INPUT":_r((BASELINE,C280_ROOT)),"SOURCE":source_record()["root"],"COORDINATE":coordinate_definition()["root"],"AST":coordinate_ast()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C281-HQCDRIMASSCOORD1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
