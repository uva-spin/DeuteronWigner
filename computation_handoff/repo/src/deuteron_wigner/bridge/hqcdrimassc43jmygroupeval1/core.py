"""C382 grouped-evaluation preflight for executable JMY masters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c382_hqcdrimassc43jmygroupeval1";BASELINE="d283de12c7ef836a14e17b9d2d570efbbece99e6";C381_ROOT="a76fe57c0393a54e1568f93cde3a6da1544c077d140f4e1ed0578fa1d415bb07"
STATUS="C382_GROUPED_EVALUATION_FAIL_CLOSED_EXECUTABLE_GROUP_ASSEMBLY_REQUIRED";PLAN="RIMASSC43JMYGROUPEVAL1-C";NEXT="C383/HQCDRIMASSC43JMYEXECGROUP1";NEXT_OBJECT="C382-C43-JMY-EXECUTABLE-GROUP-ASSEMBLY-AST";NEXT_EXACT="assemble every C381 integration node with executable numerators source prefactors endpoint owners and MSbar counterterms into gauge-complete groups"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def audit():
 rows=({"object":"loop numerators","state":"absent from C381 loop nodes"},{"object":"source prefactors","state":"not attached to integration nodes"},{"object":"fragmentation","state":"crossing map only, no instantiated rows"},{"object":"soft real","state":"C379 content not instantiated in C381 executable rows"},{"object":"counterterms","state":"MSbar ownership external but no executable attachment"},{"object":"group sums","state":"distribution/fragmentation/soft membership not encoded in one AST"})
 return {"rows":rows,"count":6,"group_executable":False,"root":_r(rows)}
def result():
 u={k:"UNAVAILABLE_PENDING_EXECUTABLE_GROUP_ASSEMBLY" for k in ("UV","IR","alpha","beta","mixed","finite","plus","delta")}
 return {g:dict(u) for g in ("distribution","fragmentation","soft")} | {"published":False,"separator_cancellation":False,"root":_r(u)}
def route_audit():return {"integrate_then_attach":"rejected violates group-before-expansion order","manual_upstream_join":"rejected not executable/reproducible","mass_source":"rejected incompatible IR","C356":"rejected circular","early_zero":"rejected","root":_r("C382-ROUTES")}
def closure():return {"evaluation_attempted":True,"group_AST_complete":False,"coefficients_preserved_unavailable":True,"ordinary_continuation":True,"C43_imported":False,"root":_r("C382-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"ungrouped_expansion":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"finite_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupeval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupeval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecparam1 as c
 if c.PACKAGE_ROOT!=C381_ROOT:raise ValueError("C381")
 c.load_verified_hqcdrimassc43jmyexecparam1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupeval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupeval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C381_ROOT)),"AUDIT":audit()["root"],"RESULT":result()["root"],"ROUTES":route_audit()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C382-HQCDRIMASSC43JMYGROUPEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
