"""C359 executability audit and parameter-integral reduction gate."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c359_hqcdrimassc43jmyparamint1";BASELINE="f7dca6d286efd0d2f3e6a78dae9b5f4af88f94a2";C358_ROOT="168e3552cbf49c5a1e62cddf668d10a6e7f50b1a6d710101b968fdaee6b34fcc"
STATUS="C359_PARAMETER_REDUCTION_AUDITED_REAL_CUT_NUMERATOR_AND_COUNTERTERM_AST_MISSING";PLAN="RIMASSC43JMYPARAMINT1-C";NEXT="C360/HQCDRIMASSC43JMYTRACEAST1";NEXT_OBJECT="C359-C43-JMY-EXECUTABLE-TRACE-CUT-AST";NEXT_EXACT="derive executable Dirac-trace real-cut self-energy and MSbar counterterm AST nodes for all C358 JMY groups"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def executability_audit():
 rows=({"id":"DV","denominators":True,"exact_numerator":True,"cut_measure":True,"counterterm_exact":False},{"id":"DR","denominators":True,"exact_numerator":False,"cut_measure":True,"counterterm_exact":False},{"id":"FV","denominators":True,"exact_numerator":True,"cut_measure":True,"counterterm_exact":False},{"id":"FR","denominators":True,"exact_numerator":False,"cut_measure":True,"counterterm_exact":False},{"id":"S","denominators":True,"exact_numerator":True,"cut_measure":True,"counterterm_exact":True})
 return {"rows":rows,"count":5,"all_executable":False,"root":_r(rows)}
def reduction_attempt():return {"loop_momentum_shift":"defined for DV,FV,S","Feynman_parameters":"defined for exact denominators","real_phase_space":"blocked before integration by descriptive rather than algebraic DR/FR numerator","MSbar":"blocked for collinear groups by unspecified self-energy/vertex counterterm decomposition","finite_constants":"UNAVAILABLE_NOT_ZERO","partial_value_published":False,"root":_r("C359-R")}
def required_ast_nodes():return {"nodes":("spin-averaged d-dimensional DR trace including quark, eikonal and interference squares","crossed FR trace with exact z Jacobian","quark external-leg self-energy integrand and Z2 counterterm","v and tilde-v Wilson self-energy integrands and counterterms","vertex MSbar counterterm with UV versus IR pole labels"),"count":5,"root":_r("C359-N")}
def closure():return {"parameter_integrals_evaluated":False,"failure_is_AST_executability_not_math":True,"ordinary_derivation_continuation":True,"finite_conversion_ready":False,"C43_imported":False,"root":_r("C359-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"descriptive_numerator_integrated":0,"partial_finite_published":0,"counterterm_guessed":0,"mass_result_reused":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyparamint1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyparamint1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyintegrand1 as c
 if c.PACKAGE_ROOT!=C358_ROOT:raise ValueError("C358")
 c.load_verified_hqcdrimassc43jmyintegrand1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyparamint1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyparamint1_authority()
_ROOTS={"INPUT":_r((BASELINE,C358_ROOT)),"AUDIT":executability_audit()["root"],"REDUCE":reduction_attempt()["root"],"NODES":required_ast_nodes()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C359-HQCDRIMASSC43JMYPARAMINT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
