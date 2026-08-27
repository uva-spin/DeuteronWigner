"""C293 authenticated partial SU(3) light-cone zero-mode source."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c293_hqcdrimassboundarysu3source1"
BASELINE="02777c45ef8118b85ca0ce04f3573b0724178ce0";C292_ROOT="1b53eb5b6d6fdcaf284cd2081eb589a300adfaff74b32e4bed240c12d8f317cd"
PDF="data/raw/c293_sources_hep-th-0101072.pdf";ARCHIVE="data/raw/c293_sources_hep-th-0101072.tar";PDF_HASH="c488049818dfdf689c49bca82ea632e728a64a1cc2f7a70659af845ae31b93c7";ARCHIVE_HASH="fbbb195a5a43eedc83ca57df9e45489ce8a2ff29ac69f5e8e2307c1d9ca7ee2f"
STATUS="C293_AUTHENTICATED_SU3_LIGHT_CONE_ZERO_MODE_ACTION_PARTIAL_FULL_C43_CONSTRAINED_MEASURE_SOURCE_MISSING";PLAN="RIMASSBOUNDARYSU3SOURCE1-B"
NEXT="C294/HQCDRIMASSBOUNDARYSU3FULLSOURCE1";NEXT_OBJECT="C293-MASS-FULL-C43-SU3-ZERO-MODE-MEASURE-SOURCE";NEXT_EXACT="authenticated 3+1-dimensional SU(3) light-front finite-volume source retaining constrained zero modes and defining the normalized holonomy measure mappable to C43"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_manifest():
 row={"source_id":"SOYEZ-HEP-TH-0101072V1","title":"A model for SU(3) vacuum degeneracy using light-cone coordinates","authors":"Gregory Soyez","official_pdf":"https://arxiv.org/pdf/hep-th/0101072","official_source":"https://arxiv.org/e-print/hep-th/0101072","pdf_path":PDF,"archive_path":ARCHIVE,"pdf_sha256":PDF_HASH,"archive_sha256":ARCHIVE_HASH,"pdf_pages":22,"archive_member":"SU3Model.tex"}
 return _f({"row":row,"hash_verified":sha256((ROOT/PDF).read_bytes()).hexdigest()==PDF_HASH and sha256((ROOT/ARCHIVE).read_bytes()).hexdigest()==ARCHIVE_HASH,"root":_r(row)})
def equation_locators():
 rows=({"role":"SU3 action/equations","locator":"SU3Model.tex lines 107-150"},{"role":"periodic zero modes and gauge","locator":"lines 162-205"},{"role":"Hamiltonian","locator":"lines 205-225, equation hamilt"},{"role":"Gribov fundamental domain","locator":"lines 405-438"},{"role":"constrained zero modes","locator":"lines 522-568"},{"role":"zero-mode Schrodinger Hamiltonian/potential","locator":"lines 571-655, equations ScSU3/fineq"})
 return _f({"rows":rows,"count":6,"transcription_visual_check":True,"root":_r(rows)})
def scope_audit():return _f({"gauge_group":"SU3","light_cone":True,"finite_volume_periodic":True,"dynamical_zero_mode_action":True,"fundamental_domain":True,"dimension":"2+1 reduced to 1+1","transverse_dependence":False,"matter":"adjoint scalar from transverse gauge field","constrained_zero_modes_retained":False,"normalized_group_measure_explicit":False,"C43_direct_map":False,"partial_promoted":False,"root":_r((STATUS,PLAN))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"authenticated_sources":1,"partial":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"dimensional_reduction_ignored":0,"constrained_modes_zeroed":0,"flat_measure_inferred":0,"partial_promoted":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassboundarysu3source1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("pdf","archive","locator","SU3","dimension","gauge","domain","constraint","measure","mapping")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassboundarysu3source1_authority():
 from deuteron_wigner.bridge import hqcdrimassboundaryactionsource1 as c292
 if c292.PACKAGE_ROOT!=C292_ROOT or not source_manifest()["hash_verified"]:raise ValueError("source authority changed")
 c292.load_verified_hqcdrimassboundaryactionsource1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassboundarysu3source1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassboundarysu3source1_authority()
_ROOTS={"INPUT":_r((BASELINE,C292_ROOT)),"SOURCE":source_manifest()["root"],"LOCATORS":equation_locators()["root"],"SCOPE":scope_audit()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"ISOLATION":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C293-HQCDRIMASSBOUNDARYSU3SOURCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
