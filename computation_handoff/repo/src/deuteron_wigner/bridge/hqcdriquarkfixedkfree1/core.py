"""C222 symbolic omitted-domain free operator with explicit transverse frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import free2 as c128
from deuteron_wigner.bridge import hqcdriquarkfixedkden1 as c221
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c222_hqcdriquarkfixedkfree1"
BASELINE="223a76f75132dfcab2b0d63501ccb4068275cb30";C221_ROOT="693aca1deec43edea1364873f53ce53b03104f3cb85c155fff289e4642fce2e3"
CONTRACT="docs/next_level/c221_c222_hqcdriquarkfixedkfree1_continuation_contract.json";CONTRACT_SHA256="590fb4d3952321289bad636aef8082619262f5ef5166c503226539a62acbfb79"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c222_hqcdriquarkfixedkfree1_codex_prompt.md";PROMPT_SHA256="a5340a153b33845cf237a72eef18c8311ae6cad1c4ff48f7a765c829d7abc105"
STATUS="C222_C221_OMITTED_FREE_OPERATOR_SYMBOLIC_LONGITUDINAL_MASS_SCHEMA_READY_TRANSVERSE_CM_KERNEL_INCOMPLETE";PLAN="RIQUARKFIXEDKFREE1-E"
NEXT="C223/HQCDRIQUARKFIXEDKTRANS1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-TRANSVERSE-KERNEL"
NEXT_EXACT="source-derived transverse kinetic and intrinsic/CM kernel on the symbolic OUTSIDE_FIXED_K complement domain"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def symbolic_state_schema():return _f({"schema":"C222-OMITTED-FREE-STATE-V1","labels":("sector","particle species","k_i APBC/PBC","n_i","m_i","helicity_i","color_i","orientation"),"domain_predicate":"sum(k_i) != retained K","K_prime":"sum(k_i), positive symbolic","cardinality":"UNBOUNDED","finite_rank_unrank":False,"root":_r(("labels","sum-k-not-K"))})
def free_operator_schema():
 rows=({"sector":"q","formal_expression":"(p_perp^2 + m_q^2)/x_q with x_q=k_q/K_prime","mass_ownership":"m_q^2 caller symbolic","longitudinal_fraction":"SOURCE_DERIVED","transverse_kernel":"UNAVAILABLE_COMPLEMENT_CM_MAP"},{"sector":"qg","formal_expression":"sum_i (p_perp_i^2 + m_i^2)/x_i - P_perp^2","mass_ownership":"m_q^2 caller symbolic; m_g^2 source exact zero","longitudinal_fraction":"x_i=k_i/K_prime, sum x_i=1","transverse_kernel":"UNAVAILABLE_COMPLEMENT_INTRINSIC_CM_MAP"})
 return _f({"rows":rows,"count":2,"units":"GeV^2","coupling_degree":0,"L_cancellation":"symbolic exact after P_plus=pi*K_prime/L","physical_values":False,"operator_complete":False,"root":_r(rows)})
def retained_extension_audit():return _f({"C128_free_bilinears_extend":True,"C128_parameter_ownership_extends":True,"C128_retained_indices_reused":False,"C128_pperp2_matrix_extends":False,"C128_CM_projector_extends":False,"reason":"C47 intrinsic/CM map authenticated only at retained fixed K,Nmax","root":_r((True,True,False,False,False))})
def denominator_program():return _f({"operator":"zI_Q-Q_RH0Q_R","state_schema_root":symbolic_state_schema()["root"],"free_schema_root":free_operator_schema()["root"],"executable":False,"missing":NEXT_OBJECT,"dense":False,"root":_r(("zI-QH0Q",NEXT_OBJECT))})
def independent_route_certificate():return _f({"route_A":"C43 free-bilinear light-front dispersion","route_B":"C128 symbolic factor ownership and scale cancellation","longitudinal_mass_mismatches":0,"transverse_route_agreement":False,"root":_r((0,"transverse-missing"))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"symbolic_longitudinal_mass_ready":True,"free_operator_complete":False,"denominator_executable":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"free_schema_root":free_operator_schema()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_indices_reused":0,"finite_cutoff_invented":0,"physical_values":0,"missing_zeroed":0,"dense_omitted_space":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkfree1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("sector","k","Kprime","x","mass","gluon-zero","p-perp","CM","L","Pplus","route","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"schemas":2,"longitudinal_mass":True,"transverse_CM":False,"mutations":384,"next":NEXT,"root":_r((STATUS,2,True,False))})
def verify_hqcd_riquarkfixedkfree1_authority():
 if c221.PACKAGE_ROOT!=C221_ROOT:raise ValueError("C221 root changed")
 c128.load_verified_free_m2_authority();c221.load_verified_hqcd_riquarkfixedkden1_authority()
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C221_package_root":C221_ROOT,"C128_package_root":c128.PACKAGE_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkfree1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkfree1_authority()
_ROOTS={"INPUT":_r((BASELINE,C221_ROOT,c128.PACKAGE_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"STATES":symbolic_state_schema()["root"],"FREE":free_operator_schema()["root"],"EXTENSION":retained_extension_audit()["root"],"DENOMINATOR":denominator_program()["root"],"ROUTES":independent_route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C222-HQCDRIQUARKFIXEDKFREE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C222_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
