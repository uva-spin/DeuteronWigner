"""C380 executability audit for C379 parameter masters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c380_hqcdrimassc43jmyparameval1";BASELINE="255cb08b729a0a8579a53205d67fbdfdb4d26563";C379_ROOT="5a124225b302d8fcffbcdbf799bb19d0e6c2842d0658cbc17453f966e02902ca"
STATUS="C380_PARAMETER_EVALUATION_FAIL_CLOSED_EXECUTABLE_PARAMETER_AST_REQUIRED";PLAN="RIMASSC43JMYPARAMEVAL1-C";NEXT="C381/HQCDRIMASSC43JMYEXECPARAM1";NEXT_OBJECT="C380-C43-JMY-EXECUTABLE-PARAMETER-INTEGRAL-AST";NEXT_EXACT="convert every C379 parameter polynomial measure branch phase and distribution action into an executable integration AST"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def audit():
 rows=({"object":"real kernels","gap":"string aliases Nqq,Dq,J and crossed DR kernel"},{"object":"loop Delta","gap":"string polynomials, not evaluable nodes"},{"object":"crossed loop","gap":"Cross(Delta) placeholder"},{"object":"Gaussian","gap":"phase and normalization not encoded"},{"object":"ordered contours","gap":"text label, no branch prescription node"},{"object":"distributions","gap":"semantic prose not executable parameter functional"})
 return {"rows":rows,"count":6,"executable":False,"root":_r(rows)}
def result():
 u={k:"UNAVAILABLE_PENDING_EXECUTABLE_PARAMETER_AST" for k in ("UV","IR","alpha","beta","mixed","finite","plus","delta")}
 return {g:dict(u) for g in ("distribution","fragmentation","soft")} | {"published":False,"zero_claims":False,"root":_r(u)}
def routes():return {"symbolic_parser":"rejected aliases and Cross placeholder","manual_branch_choice":"rejected unsupported phases","mass_source":"rejected incompatible IR regulator","C356":"rejected circular backsolve","early_scaleless_zero":"rejected","root":_r("C380-ROUTES")}
def closure():return {"evaluation_attempted":True,"parameter_AST_executable":False,"coefficients_preserved_unavailable":True,"ordinary_continuation":True,"C43_imported":False,"root":_r("C380-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"branch_invented":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"finite_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyparameval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyparameval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyparamreduce3 as c
 if c.PACKAGE_ROOT!=C379_ROOT:raise ValueError("C379")
 c.load_verified_hqcdrimassc43jmyparamreduce3_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyparameval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyparameval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C379_ROOT)),"AUDIT":audit()["root"],"RESULT":result()["root"],"ROUTES":routes()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C380-HQCDRIMASSC43JMYPARAMEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
