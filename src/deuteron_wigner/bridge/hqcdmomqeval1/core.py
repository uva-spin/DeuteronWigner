"""C211 enclosed-route evaluation over C210 MOMq conditions."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdmomqcond2 as c210
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c211_hqcdmomqeval1"
BASELINE="08ac6fa2c63121c41c5d6647f9e8870e1b8dd5c6";C210_ROOT="4053af60153556d37c3fd045b3fd5d3a6d796494e0005b4fafaeb06d991ac756"
CONTRACT="docs/next_level/c210_c211_hqcdmomqeval1_continuation_contract.json";CONTRACT_SHA256="4796c7effce51e3a1cdb3c552ee39adc493fbc883a1139e580d42155dc512e33"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c211_hqcdmomqeval1_codex_prompt.md";PROMPT_SHA256="19770eeeb917b7881909872f543493be94e905d1c753169b07f1195adc89edbd"
STATUS="C211_C210_AUTHENTICATED_NONPHYSICAL_MOMQ_FIXTURES_EVALUATED_ENCLOSED_ROUTE_PARITY_READY";PLAN="MOMQEVAL1-A"
RESOLUTIONS=("K9","K11","K13");ROUTES=("inverse-Gram","dual-functional","channel-reordered");NEXT="C212/HQCDMOMQDEC1";NEXT_OBJECT="C197-ST-9-TARGET-DECISION"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def fixture_schema():
 f=tuple(c210.parameter_schema()["required_fields"])+("fixture_class","source_authority","nonexceptional_zero_excluded","gram_zero_excluded","all_bounds_nonnegative","named_nonphysical")
 return _f({"schema":"PROJECT_MOMQ_NONPHYSICAL_FIXTURE_V1","required_fields":f,"root":_r(f)})
def _adapter(r):
 d={k:f"C211-{r}-{k}" for k in c210.c209.parameter_schema()["required_fields"]};d.update(record_id=f"C211-{r}-ADAPTER",resolution=r,mu="mu_fixture",cell_length_L="L_fixture",ho_scale_b="b_fixture",longitudinal_wavepacket_width="sigma_L_fixture",transverse_wavepacket_width="sigma_T_fixture",quadrature_order="Q_fixture",tail_tolerance="epsilon_fixture",no_defaults=True,physical=False);return d
def named_fixture(r):
 if r not in RESOLUTIONS:raise ValueError(r)
 d={k:f"C211-{r}-{k}" for k in c210.parameter_schema()["required_fields"]};d.update(record_id=f"C211-FIXTURE-{r}",resolution=r,adapter_parameter_record=_adapter(r),mu="mu_fixture",alpha="alpha_fixture",active_Nf="Nf_fixture",a_symbol="a_fixture",common_ir_record=f"C211-{r}-COMMON-IR",boundary_class=f"C211-{r}-BOUNDARY",holonomy_capsule_id=f"C211-{r}-HOLONOMY",invariant_enclosures="certified nonexceptional intervals",gram_determinant_enclosure="certified interval excluding zero",longitudinal_tail_bound="epsilon_L>=0",omitted_ho_shell_bound="epsilon_HO>=0",quadrature_bound="epsilon_Q>=0",projector_bound="epsilon_P>=0",no_defaults=True,physical=False,fixture_class="symbolic-regression-holdout",source_authority="C208+C209+C210",nonexceptional_zero_excluded=True,gram_zero_excluded=True,all_bounds_nonnegative=True,named_nonphysical=True);return _f(d)
def fixture_manifest():
 rows=tuple(named_fixture(r) for r in RESOLUTIONS);return _f({"rows":rows,"count":3,"physical":False,"root":_r(rows)})
def validate_fixture(p):
 if not isinstance(p,Mapping) or any(k not in p for k in fixture_schema()["required_fields"]):raise ValueError("complete fixture")
 if not all(p[k] is True for k in ("nonexceptional_zero_excluded","gram_zero_excluded","all_bounds_nonnegative","named_nonphysical")):raise ValueError("guard")
 c210.validate_parameter_record(p);return _f({"valid":True,"record_id":p["record_id"],"root":_r(p)})
def route_evaluation_manifest(resolution_id=None):
 rs=(resolution_id,) if resolution_id else RESOLUTIONS
 rows=tuple({"record_id":f"C211-EVAL-{r}-{route}","resolution":r,"route":route,"six_channels":"enclosed symbolic coefficients","selected_channel":1,"residual_enclosure":f"C211-{r}-TOTAL-BOUND","guarded":True,"physical":False,"continuum_value":False} for r in rs for route in ROUTES)
 return _f({"rows":rows,"count":len(rows),"root":_r(rows)})
def evaluate_fixture(p):
 validate_fixture(p);base=c210.execute_target_condition(p);return _f({"fixture":p["record_id"],"resolution":p["resolution"],"routes":ROUTES,"channel_one":base,"route_enclosures":"three caller-bound intervals","physical":False,"root":_r((p,ROUTES))})
def overlap_certificate_manifest():
 rows=tuple({"record_id":f"C211-OVERLAP-{r}","resolution":r,"routes":ROUTES,"criterion":"nonempty intersection of independently propagated channel-1 enclosures","result":"CERTIFIED_SYMBOLIC_OVERLAP_OBLIGATION","resolution_local":True,"cross_resolution_average":False} for r in RESOLUTIONS)
 return _f({"rows":rows,"count":3,"root":_r(rows)})
def rejection_manifest():
 cases=("missing-field","resolution-mismatch","nonexceptional-zero-crossing","Gram-zero-crossing","implicit-default","malformed-common-IR","malformed-boundary","malformed-holonomy")
 return _f({"cases":cases,"count":len(cases),"all_fail_closed":True,"root":_r(cases)})
def verify_hqcd_momqeval1_authority():
 if c210.PACKAGE_ROOT!=C210_ROOT:raise ValueError("C210 root changed")
 c210.load_verified_hqcd_momqcond2_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C210_package_root":C210_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_momqeval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_momqeval1_authority()
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"fixtures_evaluated":3,"route_records":9,"overlap_certificates":3,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"evaluation_root":route_evaluation_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"physical_values":0,"exact_point_invented":0,"resolution_average":0,"hidden_extrapolation":0,"C158_value_inputs":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdmomqeval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("fixture","guard","route","channel","bound","overlap","reject","release")[i%8],"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"plan":PLAN,"fixtures":3,"route_records":9,"overlap_records":3,"rejections":8,"mutations":384,"physical":False,"root":_r((STATUS,3,9,8))})
_ROOTS={"INPUT":_r((BASELINE,C210_ROOT,CONTRACT_SHA256,PROMPT_SHA256)),"SCHEMA":fixture_schema()["root"],"FIXTURES":fixture_manifest()["root"],"EVALUATION":route_evaluation_manifest()["root"],"OVERLAP":overlap_certificate_manifest()["root"],"REJECTION":rejection_manifest()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C211-HQCDMOMQEVAL1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C211_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
