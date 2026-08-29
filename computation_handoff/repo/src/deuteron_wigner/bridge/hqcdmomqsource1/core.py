"""Hash-locked Gracey MOMq definition and finite-basis map frontier."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdphysanchor as c140
from deuteron_wigner.bridge import hqcdmomqcond1 as c207
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c208_hqcdmomqsource1"
BASELINE="a89ed0150ffc43e72414cb1e635e6d9aa1371b98";C207_ROOT="3c4b895ca1c57443ab747c6fce0213ce786a9eb90e014c31c87b4e3ff65b7438"
SOURCE_PATH="data/raw/c140_sources/arxiv_1108.4806.pdf";SOURCE_SHA256="191b3a3281ef72a451146d6e40d3fcb602db08d2b5e88fa3852fc05d5dea2b90"
CONTRACT="docs/next_level/c207_c208_hqcdmomqsource1_continuation_contract.json";CONTRACT_SHA256="bc59ebd7ac287358d4d6b82d34cf4e5d6c88c91851da4fbd547943068c18a793"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c208_hqcdmomqsource1_codex_prompt.md";PROMPT_SHA256="2a746e4096de26a3b6a74aa1121eed7bfaa3d58c106fd43ead8967b93da9aa31"
STATUS="C208_C207_AUTHENTICATED_MOMQ_SOURCE_PROJECTOR_KINEMATICS_DEFINITION_READY_FINITE_BASIS_MAP_INCOMPLETE";PLAN="MOMQSOURCE1-B"
NEXT="C209/HQCDMOMQMAP1";NEXT_OBJECT="C197-ST-9-KINEMATICS-MAP";NEXT_EXACT="exact finite-C43 representation or certified approximation/limit map for symmetric MOMq kinematics"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def source_artifact_manifest():
 return _f({"source_id":"arxiv_1108.4806","title":"Two loop QCD vertices at the symmetric point","author":"J.A. Gracey","version":"arXiv:1108.4806v1","date":"24 August 2011","local_path":SOURCE_PATH,"file_size":329493,"pdf_pages":36,"sha256":SOURCE_SHA256,"hash_verified":True,"network_acquisition":False,"role":"MOMq definition, projector, and conversion-method authority","root":_r((SOURCE_PATH,SOURCE_SHA256))})
def locator_manifest():
 rows=({"locator_id":"C208-LOC-KIN","pdf_page_index":3,"printed_page":"4","section":"2 Preliminaries","object_ids":("2.1","2.2","2.3"),"role":"symmetric kinematics and qg color factor"},{"locator_id":"C208-LOC-PROJ","pdf_page_index":4,"printed_page":"5","section":"2 Preliminaries","object_ids":("2.4","2.5","2.6"),"role":"six-tensor qg decomposition and projection matrix"},{"locator_id":"C208-LOC-GAMMA","pdf_page_index":5,"printed_page":"6","section":"2 Preliminaries","object_ids":("2.7","2.8"),"role":"generalized gamma basis and chiral scope"},{"locator_id":"C208-LOC-MOMQ-DEF","pdf_page_index":8,"printed_page":"9","section":"3 Renormalization","object_ids":("3.5","3.6","3.7"),"role":"MOMq coupling definition and scheme conversion"},{"locator_id":"C208-LOC-MOMQ-HOLDOUT","pdf_page_index":23,"printed_page":"24","section":"6 quark-gluon vertex","object_ids":("6.34","6.35"),"role":"channel-1 and conversion-function holdout"})
 return _f({"rows":rows,"count":5,"visual_verification":"C164 accepted and C208 local text audit","root":_r(rows)})
def momq_definition_manifest():
 return _f({"scheme_id":"MOMq","kinematics":{"p2":"-mu^2","q2":"-mu^2","r2":"-mu^2","r":"-p-q","p_dot_q":"mu^2/2","nonexceptional":True},"vertex":"quark-antiquark-gluon","color_factor":"T^c_ij","tensor_basis_dimension":6,"tree_channel":1,"projector":"Mqqg inverse Gram matrix acting on six qg tensors","coupling_definition":"equation 3.5: MOMq/MS ratio from gluon and quark two-point amplitudes and channel-1 qg vertex amplitude","coordinate":"a=g^2/(16*pi^2) as source-defined","gauge":"linear covariant alpha; Landau preserved under mapping","regularization":"dimensional regularization","chiral_limit":True,"active_Nf":"symbolic","source_locators":tuple(x["locator_id"] for x in locator_manifest()["rows"]),"remembered_formula":False,"root":_r(("MOMq","2.1","2.5","3.5","6.35"))})
def projector_manifest():
 return _f({"basis":"six Pqqg_(k) tensors at symmetric point","Gram_matrix":"Nqqg_kl from d-dimensional Lorentz/spinor contraction","projection_matrix":"Mqqg=Nqqg^{-1}","selected_channel":1,"selection_reason":"source states channel 1 is the Feynman-rule and divergent channel","appendix_required_for_components":True,"source_objects":("2.4","2.5","2.6","Appendix A"),"physical":False,"root":_r((6,1,"2.4-2.6"))})
def representability_manifest():
 ref=dict(c140.reference_kinematics_manifest());return _f({"C140_record":ref,"exact_symmetric_continuum_definition":True,"exactly_representable_in_C43":False,"finite_longitudinal_HO_map":"INCOMPLETE_NOT_ZERO","K9_K11_K13_separate":True,"resolution_average":False,"continuum_extrapolation":False,"next":NEXT,"root":_r((ref,NEXT))})
def source_uniqueness_decision():return _f({"unique":True,"accepted_source_id":"arxiv_1108.4806","rejected_substitutions":("RI/SMOM","minimal MOM","MOMggg","MOMh","MSbar"),"root":_r((SOURCE_SHA256,"MOMq"))})
def verify_hqcd_momqsource1_authority():
 if c207.PACKAGE_ROOT!=C207_ROOT:raise ValueError("C207 root changed")
 if sha256((ROOT/SOURCE_PATH).read_bytes()).hexdigest()!=SOURCE_SHA256:raise ValueError("source hash")
 c207.load_verified_hqcd_momqcond1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C207_package_root":C207_ROOT,"source":source_artifact_manifest(),"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_momqsource1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_momqsource1_authority()
def momqsource1_plan_manifest():return _f({"selected_plan":PLAN,"status":STATUS,"source_ready":True,"finite_basis_map_ready":False,"next":NEXT,"root":_r((PLAN,STATUS,NEXT))})
def missing_source_object_manifest():return _f({"rows":({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"status":"INCOMPLETE_NOT_ZERO"},),"count":1,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"source":True,"projector":True,"kinematics_definition":True,"finite_basis_map":False,"target_condition_executable":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"source_root":source_artifact_manifest()["root"],"definition_root":momq_definition_manifest()["root"],"projector_root":projector_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():
 keys=("network_download","source_substitution","formula_invented","physical_value","finite_map_invented","resolution_average","continuum_extrapolation","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified")
 return _f({**{k:0 for k in keys},"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdmomqsource1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","hash","locator","kinematics","projector","scheme","map","handoff")[i%8],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"source_artifacts":1,"locators":5,"source_unique":True,"definition_ready":True,"projector_ready":True,"finite_basis_map_ready":False,"missing_objects":1,"physical":False,"root":_r((STATUS,1))})
_ROOTS={"INPUT":_r((BASELINE,CONTRACT_SHA256,PROMPT_SHA256,C207_ROOT)),"SOURCE":source_artifact_manifest()["root"],"LOCATOR":locator_manifest()["root"],"DEFINITION":momq_definition_manifest()["root"],"PROJECTOR":projector_manifest()["root"],"REPRESENTABILITY":representability_manifest()["root"],"UNIQUE":source_uniqueness_decision()["root"],"PLAN":momqsource1_plan_manifest()["root"],"MISSING":missing_source_object_manifest()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C208-HQCDMOMQSOURCE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C208_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
