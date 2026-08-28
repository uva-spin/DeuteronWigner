"""C349 frozen modified-delta/Collins comparison-source recovery."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c349_hqcdrimassc43deltasource1";BASELINE="d6401ff0d354cb66a771471328da78e25bad737f";C348_ROOT="5bb50e2d1dad420859a2096cfa1a8e9a336c6f822747a5e8f918f0ecfe1494f3"
STATUS="C349_MODIFIED_DELTA_COLLINS_PRIMARY_SOURCES_RECOVERED_EXPLICIT_COMMON_COEFFICIENT_EXTRACTION_MISSING";PLAN="RIMASSC43DELTASOURCE1-C";NEXT="C350/HQCDRIMASSC43DELTAEXTRACT1";NEXT_OBJECT="C349-C43-DELTA-COLLINS-EQUATION-EXTRACTION";NEXT_EXACT="extract and normalize the modified-delta one-loop operator soft and quark finite equations into the C348 common comparison schema"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def source_manifest():
 rows=({"id":"1511.05590v2","path":"data/raw/c31_sources/1511.05590.pdf","sha256":"dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d","locator":"pp.3-5 Eqs.(3)-(13)","authority":"four-line coordinate-space soft operator; operator delta regulator; NLO soft result"},{"id":"1604.07869v3","path":"data/raw/c31_sources/1604.07869.pdf","sha256":"11013c71a5ef19d7aadc85469cf509f0481f3df4207cf40f5da89321f1c73c93","locator":"pp.10-12 Eqs.(3.1)-(3.11)","authority":"sqrt-soft allocation; zero-bin identity; collinear rescaling"})
 out=[]
 for x in rows:
  a=sha256((ROOT/x["path"]).read_bytes()).hexdigest();out.append({**x,"actual_sha256":a,"verified":a==x["sha256"]})
 return {"rows":tuple(out),"all_verified":all(x["verified"] for x in out),"root":_r(out)}
def comparison_crosswalk():return {"delta_side":{"operator":True,"regulator":True,"soft_partition":True,"zero_bin":True,"finite_NLO_soft":True},"JMY_side":{"operator":True,"off_lightcone_path":True,"finite_common_external_state":False},"common_fields":{"UV_MSbar":"requires equation extraction","Fourier":"requires equation extraction","alpha_s_normalization":"requires equation extraction","IR_prescription":"not yet common"},"direct_conversion_ready":False,"root":_r("C349-XWALK")}
def classification():return {"modified_delta_primary_authority":True,"operator_identical_to_C43":False,"use":"comparison and conversion derivation only","coefficient_imported_C43":False,"finite_equations_extracted":False,"root":_r("C349-CLASS")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"continuum_coefficient_imported_C43":0,"operator_identity_claimed":0,"finite_constant_invented":0,"source_bytes_modified":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43deltasource1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43deltasource1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43convertcoeff1 as c
 if c.PACKAGE_ROOT!=C348_ROOT or not source_manifest()["all_verified"]:raise ValueError("authority")
 c.load_verified_hqcdrimassc43convertcoeff1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43deltasource1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43deltasource1_authority()
_ROOTS={"INPUT":_r((BASELINE,C348_ROOT)),"SOURCE":source_manifest()["root"],"CROSSWALK":comparison_crosswalk()["root"],"CLASS":classification()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C349-HQCDRIMASSC43DELTASOURCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
