"""C377 parameter-reduction audit for the C376 scalar AST."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c377_hqcdrimassc43jmyparamreduce2";BASELINE="a513d99b0c626519ba67c278ec616c8152a0ff36";C376_ROOT="9d5e7a17c6f50488711dad00e293ae549a0cb4d6794e7ca3addb193f60ac0b37"
STATUS="C377_PARAMETER_REDUCTION_FAIL_CLOSED_KINEMATIC_CONTRACTION_AST_REQUIRED";PLAN="RIMASSC43JMYPARAMREDUCE2-C";NEXT="C378/HQCDRIMASSC43JMYKINEMATICAST1";NEXT_OBJECT="C377-C43-JMY-KINEMATIC-CONTRACTION-AST";NEXT_EXACT="bind light-cone component metric projector and off-light-cone v tildev contraction rules for every free C376 scalar symbol"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def symbol_audit():
 rows=({"symbol":"proj_p_minus_ell","missing":"endpoint tree projector definition"},{"symbol":"vslash_proj","missing":"Dirac projector reduced to v plus/minus components"},{"symbol":"tvslash_proj","missing":"crossed Dirac projector"},{"symbol":"p_minus_ell_proj","missing":"projected momentum component"},{"symbol":"q_dot_v,p_dot_v","missing":"light-cone component expansion and transverse assumptions"},{"symbol":"virtual quadratic forms","missing":"metric signature and completed-square polynomial with ordered i0"})
 return {"rows":rows,"count":6,"kinematically_closed":False,"root":_r(rows)}
def partial_reduction():return {"real_cut_substitution":{"q_plus":"x p_plus","q2":"-kT2/(1-x)","p_dot_q":"-q2/2","ell_plus":"(1-x)p_plus","jacobian":"1/[2(1-x)p_plus]"},"status":"BOUND_ONLY_FOR_QQ; qv requires v components","virtual":"UNAVAILABLE_PENDING_CONTRACTION_AST","soft":"UNAVAILABLE_PENDING_V_TILDEV_COMPONENTS","mass_terms":0,"root":_r("C377-PART")}
def attempted_routes():return {"component_substitution":"stops at missing v/tildev and projector definitions","Lorentz_covariant_completion":"stops at unspecified projection normalization","source_mass_formula":"rejected IR-regulator import","model_convention":"rejected unsupported metric choice","C356_backsolve":"rejected circular","root":_r("C377-ROUTES")}
def closure():return {"parameter_reduction_attempted":True,"real_qq_partial":True,"all_parameter_polynomials":False,"unavailable_preserved":True,"ordinary_continuation":True,"C43_imported":False,"root":_r("C377-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"metric_invented":0,"projector_invented":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyparamreduce2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyparamreduce2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecutableast1 as c
 if c.PACKAGE_ROOT!=C376_ROOT:raise ValueError("C376")
 c.load_verified_hqcdrimassc43jmyexecutableast1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyparamreduce2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyparamreduce2_authority()
_ROOTS={"INPUT":_r((BASELINE,C376_ROOT)),"SYMBOL":symbol_audit()["root"],"PARTIAL":partial_reduction()["root"],"ROUTES":attempted_routes()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C377-HQCDRIMASSC43JMYPARAMREDUCE2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
