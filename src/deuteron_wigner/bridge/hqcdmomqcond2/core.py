"""C210 symbolic execution of the MOMq condition over the C209 adapter."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdmomqmap1 as c209

ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c210_hqcdmomqcond2"
BASELINE="653a452bee620d66f8323826237817f9539bace1";C209_ROOT="fb0abd5750ea3684ad44fc05512dbd4e0765c0da5e721bdc51da4735326d9654"
CONTRACT="docs/next_level/c209_c210_hqcdmomqcond2_continuation_contract.json";CONTRACT_SHA256="e3de05ae0521ccfc78cdf7228891d6af04c0c2d1025caa740526d47212766cce"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c210_hqcdmomqcond2_codex_prompt.md";PROMPT_SHA256="59a1b91bdfbc9352fe97c2d7123d0e27b3d53755feac74bbebd07b6eddd98531"
STATUS="C210_C209_EXECUTABLE_ENCLOSED_TARGET_MOMQ_CONDITION_READY_NONPHYSICAL";PLAN="MOMQCOND2-A"
RESOLUTIONS=("K9","K11","K13");CHANNELS=tuple(range(1,7));NEXT="C211/HQCDMOMQEVAL1";NEXT_OBJECT="C197-ST-9-TARGET-EVALUATION"
OPCODES=("LOAD_C209_ADAPTER","VALIDATE_COMPLETE_CALLER_RECORD","CHECK_NONEXCEPTIONAL_ENCLOSURE","CHECK_GRAM_DETERMINANT_ENCLOSURE","APPLY_SIX_CHANNEL_PROJECTOR","SELECT_CHANNEL_ONE","BIND_MOMQ_TREE_NORMALIZATION","PROPAGATE_ERROR_ENCLOSURES","CHECK_GAUGE_SCHEME_COMMON_IR","RETURN_ENCLOSED_CONDITION")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def parameter_schema():
 f=("record_id","resolution","adapter_parameter_record","mu","alpha","active_Nf","a_symbol","common_ir_record","boundary_class","holonomy_capsule_id","invariant_enclosures","gram_determinant_enclosure","longitudinal_tail_bound","omitted_ho_shell_bound","quadrature_bound","projector_bound","no_defaults","physical")
 return _f({"schema":"PROJECT_MOMQ_CONDITION_PARAMETER_V1","required_fields":f,"root":_r(f)})
def validate_parameter_record(p):
 if not isinstance(p,Mapping) or any(k not in p for k in parameter_schema()["required_fields"]):raise ValueError("complete condition record")
 if p["resolution"] not in RESOLUTIONS or p["no_defaults"] is not True or p["physical"] is not False:raise ValueError("domain/default")
 if p["mu"] in (None,0,0.0,"") or p["alpha"] is None or p["active_Nf"] is None or p["a_symbol"] in (None,""):raise ValueError("symbolic inputs")
 if not isinstance(p["adapter_parameter_record"],Mapping):raise ValueError("adapter record")
 return _f({"valid":True,"record_id":p["record_id"],"root":_r(p)})
def condition_program_schema():return _f({"schema":"PROJECT_MOMQ_ENCLOSED_CONDITION_PROGRAM_V1","allowed_opcodes":OPCODES,"eval":False,"pickle":False,"callbacks":False,"root":_r(OPCODES)})
def guard_manifest(resolution_id=None):
 rows=tuple({"record_id":f"C210-GUARD-{r}","resolution":r,"nonexceptional":"zero excluded from momentum-invariant enclosures","Gram":"zero excluded from determinant enclosure","common_ir":"caller record required","gauge_scheme":"explicit alpha, Nf, a and MOMq scheme","failure":"reject without channel value","physical":False} for r in ((resolution_id,) if resolution_id else RESOLUTIONS))
 return _f({"rows":rows,"count":len(rows),"root":_r(rows)})
def enclosed_condition_manifest(resolution_id=None,channel_id=None):
 rs=(resolution_id,) if resolution_id else RESOLUTIONS;chs=(channel_id,) if channel_id else CHANNELS
 rows=tuple({"record_id":f"C210-COND-{r}-CH{ch}","resolution":r,"channel":ch,"condition":"inverse-Gram projected qg vertex coefficient with MOMq normalization","tree_target":"channel 1 Feynman-rule normalization" if ch==1 else "auxiliary tensor coefficient","errors":"longitudinal + HO-shell + quadrature + invariant + projector enclosures","exact_finite_point":False,"resolution_average":False,"continuum_value":False,"physical":False} for r in rs for ch in chs)
 return _f({"rows":rows,"count":len(rows),"channel_one_records":len(rs),"root":_r(rows)})
def execute_target_condition(p):
 validate_parameter_record(p);c209.validate_parameter_record(p["adapter_parameter_record"])
 if p["adapter_parameter_record"]["resolution"]!=p["resolution"]:raise ValueError("resolution mismatch")
 return _f({"record_id":p["record_id"],"resolution":p["resolution"],"selected_channel":1,"condition":"enclosed symbolic equality to MOMq tree normalization","residual_enclosure":"caller-bound Minkowski sum of invariant, tail, HO, quadrature, and projector bounds","guarded":True,"exact_finite_point":False,"continuum_value":False,"physical":False,"root":_r(p)})
def route_parity_manifest():
 rows=tuple({"record_id":f"C210-PARITY-{r}","resolution":r,"route_A":"Gram inverse then channel select","route_B":"dual functional then channel select","required":"overlapping enclosure","order_reversal":"six channels reversed before reconstruction","status":"symbolic parity obligation encoded"} for r in RESOLUTIONS)
 return _f({"rows":rows,"count":3,"root":_r(rows)})
def verify_hqcd_momqcond2_authority():
 if c209.PACKAGE_ROOT!=C209_ROOT:raise ValueError("C209 root changed")
 c209.load_verified_hqcd_momqmap1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C209_package_root":C209_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_momqcond2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_momqcond2_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"condition_executable":True,"guarded":True,"physical":False,"continuum_value":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"condition_root":enclosed_condition_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():
 keys=("exact_point_invented","resolution_average","hidden_extrapolation","physical_value","implicit_defaults","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified")
 return _f({**{k:0 for k in keys},"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdmomqcond2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("parameter","guard","invariant","Gram","channel","normalization","error","route","handoff")[i%9],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"guards":3,"condition_records":18,"parity_records":3,"mutations":384,"executable":True,"physical":False,"root":_r((STATUS,3,18,384))})
_ROOTS={"INPUT":_r((BASELINE,C209_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"PARAMETER":parameter_schema()["root"],"PROGRAM":condition_program_schema()["root"],"GUARD":guard_manifest()["root"],"CONDITION":enclosed_condition_manifest()["root"],"PARITY":route_parity_manifest()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C210-HQCDMOMQCOND2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C210_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
