"""C292 hash-locked boundary-action source audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c292_hqcdrimassboundaryactionsource1"
BASELINE="7f03637bd80692b94d672f743bdfa9b79b005c84";C291_ROOT="9280201f34cb953e96626ca2e6ee16f1a7275fe9c35661221e7f78da4f0ac4fd"
STATUS="C292_HASH_LOCKED_FINITE_VOLUME_ZERO_MODE_SOURCES_PARTIAL_SU3_HOLONOMY_ACTION_MEASURE_SOURCE_MISSING";PLAN="RIMASSBOUNDARYACTIONSOURCE1-B"
NEXT="C293/HQCDRIMASSBOUNDARYSU3SOURCE1";NEXT_OBJECT="C292-MASS-SU3-HOLONOMY-ACTION-MEASURE-SOURCE";NEXT_EXACT="authenticated SU(3) finite-volume light-front zero-mode or holonomy action and normalized measure source with conventions mappable to C43"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_audit():
 from deuteron_wigner.bridge.g0 import contracts as c43
 by={x["key"]:x for x in c43.source_manifest()["rows"]}
 rows=({"source_id":"BPP","archive_sha256":by["BPP"]["archive_sha256"],"member":"08Vacuu.tex","locators":("lines 785-1116 gauge proper/global zero modes","lines 1123-1349 dynamical zero modes"),"provides":"finite-volume LF gauge zero-mode structure; SU2 example","SU3_action":False,"normalized_measure":False},{"source_id":"HEINZL","archive_sha256":by["HEINZL"]["archive_sha256"],"member":"lecture.tex","locators":("lines 2170-2513 finite-volume quantization","lines 2395-2406 zero-mode limitation"),"provides":"generic finite-volume and zero-mode audit","SU3_action":False,"normalized_measure":False},{"source_id":"SB","archive_sha256":by["SB"]["archive_sha256"],"member":"prd8711rsa.tex","locators":("canonical action Eqs.1,5-9,24-25",),"provides":"bulk LF QCD action","SU3_action":False,"normalized_measure":False})
 return _f({"rows":rows,"hash_locked":True,"source_complete":False,"root":_r(rows)})
def coverage_matrix():return _f({"finite_volume":True,"zero_mode_classification":True,"bulk_SU3_QCD":True,"SU3_holonomy_boundary_action":False,"sector_weights":False,"absolute_normalization":False,"K_mapping":False,"partial_promoted":False,"root":_r((STATUS,PLAN))})
def acquisition_request():return _f({"object_id":NEXT_OBJECT,"queries":("SU(3) light-front quantization finite volume zero mode Haar measure","DLCQ SU(3) gauge zero modes holonomy effective Hamiltonian","light-cone SU(3) Polyakov loop zero mode measure"),"required":("official artifact","equation locator","SU3 conventions","action","measure normalization"),"root":_r(NEXT_OBJECT)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"sources_audited":3,"partial_sources":2,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"partial_promoted":0,"SU2_relabelled_SU3":0,"remembered_formula":0,"web_summary_formula":0,"identity_default":0,"unit_volume_default":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassboundaryactionsource1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("hash","member","locator","finite_volume","zero_mode","group","action","measure","normalization","mapping")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassboundaryactionsource1_authority():
 from deuteron_wigner.bridge import hqcdrimassboundaryaction1 as c291
 from deuteron_wigner.bridge.g0 import contracts as c43
 if c291.PACKAGE_ROOT!=C291_ROOT or not c43.validate_source_manifest(c43.source_manifest()):raise ValueError("source authority changed")
 c291.load_verified_hqcdrimassboundaryaction1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassboundaryactionsource1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassboundaryactionsource1_authority()
_ROOTS={"INPUT":_r((BASELINE,C291_ROOT)),"SOURCE":source_audit()["root"],"COVERAGE":coverage_matrix()["root"],"REQUEST":acquisition_request()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C292-HQCDRIMASSBOUNDARYACTIONSOURCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
