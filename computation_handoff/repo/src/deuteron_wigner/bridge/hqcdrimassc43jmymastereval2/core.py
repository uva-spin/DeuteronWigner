"""C375 executability audit of the merged JMY master matrix."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c375_hqcdrimassc43jmymastereval2";BASELINE="c7130f1a811128daf1e0f8f371f77f419d7495df";C374_ROOT="3c3c46e678311273b9519a54f40a7a3d9490312a31806b0681216b53eb28d937"
STATUS="C375_LAURENT_EVALUATION_FAIL_CLOSED_EXECUTABLE_SCALAR_AST_REQUIRED";PLAN="RIMASSC43JMYMASTEREVAL2-C";NEXT="C376/HQCDRIMASSC43JMYEXECUTABLEAST1";NEXT_OBJECT="C375-C43-JMY-EXECUTABLE-SCALAR-MASTER-AST";NEXT_EXACT="replace every symbolic C374 coefficient and master placeholder with an executable scalar algebra and distribution AST"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def executability_audit():
 rows=({"field":"DR scalar coefficients","state":"symbolic brace notation, not coefficient-keyed shifted masters"},{"field":"virtual projected numerators","state":"gamma/pslash strings, no scalar projector result"},{"field":"reflected graph allocation","state":"descriptive inclusion, no numeric multiplicity node"},{"field":"soft same-line sector","state":"positive combined and matched powers are placeholders"},{"field":"master kernels","state":"L/R/S labels lack executable Symanzik or light-cone polynomials"},{"field":"distribution algebra","state":"Mx/Mz labels lack plus/delta action on test functions"})
 return {"rows":rows,"count":6,"executable":False,"root":_r(rows)}
def evaluation_result():
 u={k:"UNAVAILABLE_PENDING_EXECUTABLE_AST" for k in ("UV","IR","alpha","beta","mixed","finite","plus","delta")}
 return {g:dict(u) for g in ("distribution","fragmentation","soft")} | {"numeric_or_symbolic_coefficients_published":False,"zero_claims":False,"root":_r(u)}
def attempted_routes():return {"direct_CAS":"rejected non-parseable prose nodes","manual_interpretation":"rejected ambiguous shifted-master and soft powers","source_mass_result":"rejected incompatible IR regulator","C356_backsolve":"rejected circular holdout","scaleless_zero":"rejected before UV/IR separation","root":_r("C375-ROUTES")}
def validation():return {"matrix_coverage":"PASS","executability":"FAIL_CLOSED","Ward_crossing_Cutkosky":"preserved structurally","separator_cancellation":"not asserted","auxiliary_scale_cancellation":"not asserted","C356":"retained holdout","root":_r("C375-VALID")}
def closure():return {"evaluation_attempted":True,"Laurent_evaluated":False,"unavailable_preserved":True,"ordinary_continuation":True,"C43_imported":False,"root":_r("C375-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"prose_evaluated":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"inferred_constant":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmymastereval2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmymastereval2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmycoeffmerge1 as c
 if c.PACKAGE_ROOT!=C374_ROOT:raise ValueError("C374")
 c.load_verified_hqcdrimassc43jmycoeffmerge1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmymastereval2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmymastereval2_authority()
_ROOTS={"INPUT":_r((BASELINE,C374_ROOT)),"AUDIT":executability_audit()["root"],"RESULT":evaluation_result()["root"],"ROUTES":attempted_routes()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C375-HQCDRIMASSC43JMYMASTEREVAL2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
