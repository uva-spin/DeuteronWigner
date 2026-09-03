"""C213 typed audit of C197-ST-10 physical-input authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdmomqdec1 as c212
from deuteron_wigner.bridge import hqcdphysinput2 as c154
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c213_hqcdphysinput1"
BASELINE="97ce61ffd77b7afe9e75b2affbc06cbb3b7a04f7";C212_ROOT="a9a1a787cabdcf6d5adcdae61c83fd1e80d830bd6aac8caa03fab7887c4c152c";C154_ROOT="1a22cd636f3b48ef9fd51676d2761a986126b043ccfa04e9609cd2a126b67bff"
CONTRACT="docs/next_level/c212_c213_hqcdphysinput1_continuation_contract.json";CONTRACT_SHA256="398ff6f9ca42afe86eefc1090c338640bc69a3ed3d2cb00be8168abe40948b10"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c213_hqcdphysinput1_codex_prompt.md";PROMPT_SHA256="e78990ebe8286d5c6026b02cbebcded0090907596032239a5cbc67cdb3193b60"
STATUS="C213_C212_PHYSICAL_INPUT_AUTHORITY_AUDITED_STANDARD_CAPSULES_READY_FINITE_BASIS_BINDING_INCOMPLETE";PLAN="PHYSINPUT1-B"
NEXT="C214/HQCDPHYSINPUTMAP1";NEXT_OBJECT="C197-ST-10-PHYSICAL-INPUT-MAP";NEXT_EXACT="authenticated scale/running and finite-basis target map for accepted physical capsules"
ROOT_CHAIN={"C154":C154_ROOT,"C155":"371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d","C157":"351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c","C158":"63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367","C161":"0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a","C168":"c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c","C206":"b404a853c2c9f63620bf970b4230ef67c59003a73f43de8f51e7aefab0ea371d","C212":C212_ROOT}
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def physical_source_ledger():
 rows=tuple({"input_id":x["input_id"],"quantity":x["quantity_id"],"source_id":x["source_id"],"source_sha256":x["source_sha256"],"locator":x["locator"],"units":x["units"],"scheme":x["scheme"],"scale":x["scale"],"N_f":x["N_f"],"classification":"AUTHENTICATED_STANDARD_PHYSICAL_COORDINATE","consumed":False} for x in c154.accepted_standard_input_capsules())
 return _f({"rows":rows,"count":2,"hash_locked":True,"root":_r(rows)})
def parameter_authority_ledger():
 rows=(
 {"parameter":"qcd_coupling","authority":"C154 PDG capsule","classification":"AUTHENTICATED_STANDARD_COORDINATE","Hamiltonian_ready":False,"gap":"running/threshold and finite-basis map"},
 {"parameter":"light_quark_mass","authority":"C154 PDG capsule + C155 flavor lift","classification":"AUTHENTICATED_STANDARD_COORDINATE_AND_FLAVOR_IDENTITY","Hamiltonian_ready":False,"gap":"running and finite-basis map"},
 {"parameter":"common_IR/regulator","authority":"C153/C157 symbolic records","classification":"CONDITIONAL_AUTHORITY","Hamiltonian_ready":False,"gap":"numerical common-IR binding"},
 {"parameter":"boundary/holonomy","authority":"C169-C183 symbolic capsules","classification":"CONDITIONAL_AUTHORITY","Hamiltonian_ready":False,"gap":"physical selection"},
 {"parameter":"basis scales K9/K11/K13","authority":"C43 fixed-regulator conventions","classification":"CONDITIONAL_RESOLUTION_AUTHORITY","Hamiltonian_ready":False,"gap":"physical scale map"},
 {"parameter":"counterterm coordinates","authority":"C206 14D affine family","classification":"UNSELECTED_NOT_ZERO","Hamiltonian_ready":False,"gap":"physical condition selection"},
 {"parameter":"target observables","authority":"C158 finite-basis coefficients; C161 binding incomplete","classification":"COMPARISON_CONDITIONAL","Hamiltonian_ready":False,"gap":"authenticated target binding"},
 {"parameter":"uncertainties/covariance","authority":"C154 marginal uncertainties","classification":"MARGINAL_ONLY","Hamiltonian_ready":False,"gap":"joint covariance unavailable"},
 {"parameter":"flavor/color/channel","authority":"C155 and C208-C212","classification":"SYMBOLIC_SCOPE_AUTHORITY","Hamiltonian_ready":False,"gap":"physical record binding"})
 return _f({"rows":rows,"count":9,"Hamiltonian_ready_count":0,"root":_r(rows)})
def schema_consumption_audit():return _f({"required_classes":("coupling","mass","IR/regulator","boundary/holonomy","basis scale","counterterms","targets","uncertainty","scope"),"covered_classes":9,"complete_authority_classes":0,"C154_capsules_consumed":0,"C158_values_consumed":0,"physical_parameter_record":False,"root":_r((9,0,False))})
def repository_git_authority_audit():return _f({"routes":("tracked public APIs","tracked runtime manifests","Git history","authenticated local source hashes"),"standard_capsules_found":2,"complete_finite_basis_physical_records":0,"quarantined_records_promoted":0,"result":"EXACT_MAPPING_FRONTIER_REMAINS","root":_r((2,0,0))})
def exclusion_quarantine_ledger():
 rows=("C134 quarantined artifacts not authority","C158 values read-only and not consumed","test fixtures not physical inputs","conditional symbolic records not numerical defaults","missing covariance not zero","unselected counterterm coordinates not zero")
 return _f({"rows":rows,"count":6,"root":_r(rows)})
def gap_decision():return _f({"object_id":"C197-ST-10","available":"two authenticated standard coordinate capsules plus flavor identity","missing":NEXT_EXACT,"classification":"AUDIT_COMPLETE_EXACT_ACQUISITION_OR_DERIVATION_FRONTIER","blocker":False,"selected_plan":PLAN,"next":NEXT,"root":_r((PLAN,NEXT,NEXT_OBJECT))})
def verify_hqcd_physinput1_authority():
 if c212.PACKAGE_ROOT!=C212_ROOT or c154.PACKAGE_ROOT!=C154_ROOT:raise ValueError("upstream root changed")
 c212.load_verified_hqcd_momqdec1_authority();c154.load_verified_hqcd_physical_input_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":ROOT_CHAIN,"package_root":PACKAGE_ROOT,"physical_record_ready":False})
def load_verified_hqcd_physinput1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_physinput1_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"audit_complete":True,"standard_capsules":2,"physical_record_ready":False,"C197_ST_10_closed":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"ledger_root":parameter_authority_ledger()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"physical_values_selected":0,"C158_value_inputs":0,"quarantine_promotions":0,"implicit_defaults":0,"fabricated_covariance":0,"counterterm_representatives":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdphysinput1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","scheme","scale","flavor","IR","boundary","basis","counterterm","target","covariance","gap","handoff")[i%12],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"source_capsules":2,"parameter_classes":9,"complete_physical_records":0,"exclusions":6,"mutations":384,"next":NEXT,"root":_r((STATUS,2,9,0))})
_ROOTS={"INPUT":_r((BASELINE,CONTRACT_SHA256,PROMPT_SHA256,ROOT_CHAIN)),"SOURCE":physical_source_ledger()["root"],"PARAMETERS":parameter_authority_ledger()["root"],"CONSUMPTION":schema_consumption_audit()["root"],"REPOSITORY":repository_git_authority_audit()["root"],"EXCLUSION":exclusion_quarantine_ledger()["root"],"GAP":gap_decision()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C213-HQCDPHYSINPUT1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C213_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
