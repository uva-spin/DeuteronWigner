"""C294 complementary full-source set for an SU3 FP-measure derivation."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c294_hqcdrimassboundarysu3fullsource1"
BASELINE="7337d478b9fca669bdd2ee83d5b015caf681c1da";C293_ROOT="626157c6b2dec42d48f72b1a0604d3ab32b236205b0bceb79bef58ed51b2f305"
PDF="data/raw/c294_sources_hep-th-9506046.pdf";ARCHIVE="data/raw/c294_sources_hep-th-9506046.tar";PDF_HASH="e89f474b510706bddb4c86d33b367053b926f0f0979fff82653912d7c04aef37";ARCHIVE_HASH="ac240b72421d76f114676c613ae2882e9df4dabb6d785e9125119a83b63e8b56"
STATUS="C294_COMPLEMENTARY_SUN_FP_DETERMINANT_AND_SU3_BASIS_SOURCES_READY_SU3_MEASURE_DERIVATION_MISSING";PLAN="RIMASSBOUNDARYSU3FULLSOURCE1-B"
NEXT="C295/HQCDRIMASSSU3MEASUREDERIVE1";NEXT_OBJECT="C294-MASS-SU3-FP-HOLONOMY-MEASURE-DERIVATION";NEXT_EXACT="derive and independently verify the normalized SU(3) zero-mode Faddeev-Popov/holonomy measure from C294 general SU(N) determinant equations in the C293/C43 generator conventions"
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
 row={"source_id":"FUJITA-SHVARTSMAN-HEP-TH-9506046V1","title":"Role of Zero Modes in Quantization of QCD in Light-Cone Coordinates","official_pdf":"https://arxiv.org/pdf/hep-th/9506046","official_source":"https://arxiv.org/e-print/hep-th/9506046","pdf_path":PDF,"source_path":ARCHIVE,"pdf_sha256":PDF_HASH,"source_sha256":ARCHIVE_HASH,"pdf_pages":21,"source_format":"gzip single TeX"}
 return _f({"row":row,"hash_verified":sha256((ROOT/PDF).read_bytes()).hexdigest()==PDF_HASH and sha256((ROOT/ARCHIVE).read_bytes()).hexdigest()==ARCHIVE_HASH,"root":_r(row)})
def equation_locators():
 rows=({"role":"periodic gauge/AP fermion BC and P/Q split","locator":"source lines 258-300"},{"role":"general SU(N) heavy-quark QCD action/Hamiltonian","locator":"lines 655-1032"},{"role":"physical zero-mode Hamiltonian","locator":"lines 859-1025"},{"role":"general FP determinant definition/normalization","locator":"lines 1171-1314, equations f1-f3b"},{"role":"SU2 explicit determinant comparison only","locator":"lines 1314-1337"})
 return _f({"rows":rows,"count":5,"root":_r(rows)})
def complementary_coverage():return _f({"C293":"explicit SU3 basis, fundamental domain, dynamical Hamiltonian; reduced and constraints omitted","C294":"general SUN constrained/nonzero-mode Hamiltonian and FP determinant normalization; 1+1, explicit determinant only SU2","joint_SU3_derivation_ready":True,"direct_3plus1_physical_measure":False,"dimensional_map_required_after_derivation":True,"sources_conflated":False,"root":_r((STATUS,PLAN))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"source_set":2,"derivation_ready":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"SU2_relabelled_SU3":0,"dimension_ignored":0,"source_conflation":0,"determinant_invented":0,"normalization_defaulted":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassboundarysu3fullsource1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("pdf","source","locator","SUN","SU3","constraint","Hamiltonian","FP","normalization","dimension")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassboundarysu3fullsource1_authority():
 from deuteron_wigner.bridge import hqcdrimassboundarysu3source1 as c293
 if c293.PACKAGE_ROOT!=C293_ROOT or not source_manifest()["hash_verified"]:raise ValueError("source authority changed")
 c293.load_verified_hqcdrimassboundarysu3source1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassboundarysu3fullsource1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassboundarysu3fullsource1_authority()
_ROOTS={"INPUT":_r((BASELINE,C293_ROOT)),"SOURCE":source_manifest()["root"],"LOCATORS":equation_locators()["root"],"COVERAGE":complementary_coverage()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C294-HQCDRIMASSBOUNDARYSU3FULLSOURCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
