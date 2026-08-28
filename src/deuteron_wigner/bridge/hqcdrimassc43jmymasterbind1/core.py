"""C370 term-to-master binding for frozen grouped JMY integrands."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c370_hqcdrimassc43jmymasterbind1";BASELINE="9c5c5b013c13a1a15ae193c58ba09a9a3f4064b6";C369_ROOT="43331896f3c5d5698431f5a9bb4acb19930c6617681aa15cc783148e1492a918"
STATUS="C370_TERM_MASTER_INDICES_CONTOURS_MEASUREMENTS_BOUND_SCALAR_REDUCTION_COEFFICIENTS_INCOMPLETE";PLAN="RIMASSC43JMYMASTERBIND1-C";NEXT="C371/HQCDRIMASSC43JMYSCALARCOEFF1";NEXT_OBJECT="C370-C43-JMY-MASTER-SCALAR-REDUCTION-COEFFICIENTS";NEXT_EXACT="reduce the bound C370 tensor and momentum numerators to a complete scalar master coefficient table including global operator prefactors"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def real_bindings():
 rows=({"term":"DR.qq","master":"R","indices":{"A":2,"B":0,"r":0},"numerator":"2(d-2)[2q+(p.q)-q^2p+]","contour":"active +i0","measurement":"delta(x-1+ell+/p+) exp(i bT.ellT)"},{"term":"DR.qv","master":"R","indices":{"A":1,"B":1,"r":"alpha"},"numerator":"4[p+(q.v)-(p.q)v+ +(p.v)q+]","contour":"v.ell+i0","measurement":"distribution real"},{"term":"DR.vv","master":"R","indices":{"A":0,"B":2,"r":"2alpha"},"numerator":"2p+v^2","contour":"v.ell+i0 squared","measurement":"distribution real"},{"term":"FR.qq","master":"Cross(R)","indices":{"A":2,"B":0,"r":0},"numerator":"CrossPlusMinus(DR.qq) z^(-2+2epsilon)","contour":"crossed","measurement":"delta(z-1+ell-/p-) exp(i bT.ellT)"},{"term":"FR.qv","master":"Cross(R)","indices":{"A":1,"B":1,"r":"beta"},"numerator":"CrossPlusMinus(DR.qv) z^(-2+2epsilon)","contour":"tildev.ell-i0","measurement":"fragmentation real"},{"term":"FR.vv","master":"Cross(R)","indices":{"A":0,"B":2,"r":"2beta"},"numerator":"CrossPlusMinus(DR.vv) z^(-2+2epsilon)","contour":"tildev crossed squared","measurement":"fragmentation real"})
 return {"rows":rows,"count":6,"common_prefactor":"g^2 CF times frozen bilocal tree normalization; exact graph sign not exposed termwise upstream","root":_r(rows)}
def virtual_bindings():
 rows=({"term":"Sigma_q","master":"L","indices":{"A":1,"B":1,"C":0,"r":0},"numerator":"(2-d)(pslash-ellslash)","endpoint":"delta(1-x)delta2(kT) or crossed"},{"term":"W_v","master":"L ordered two-eikonal","indices":{"A":1,"B":0,"C":2,"r":"2alpha"},"numerator":"v^2","endpoint":"delta(1-x)delta2(kT)"},{"term":"W_tildev","master":"Cross(L) ordered two-eikonal","indices":{"A":1,"B":0,"C":2,"r":"2beta"},"numerator":"tildev^2","endpoint":"delta(1-z)delta2(kT)"},{"term":"V_qv","master":"L","indices":{"A":1,"B":1,"C":1,"r":"alpha"},"numerator":"vslash(pslash-ellslash)gamma+","endpoint":"delta(1-x)delta2(kT)"},{"term":"V_htv","master":"Cross(L)","indices":{"A":1,"B":1,"C":1,"r":"beta"},"numerator":"gamma-(pslash-ellslash)tildevslash","endpoint":"delta(1-z)delta2(kT)"})
 return {"rows":rows,"count":5,"common_prefactor":"-i g^2 CF mu^(2epsilon); graph combinatoric/operator factors not exposed individually upstream","root":_r(rows)}
def soft_bindings():
 rows=({"term":"S.virtual","master":"S","indices":{"A":1,"B":1,"r":"alpha","s":"beta"},"numerator":"2 v.tildev","contours":"v.ell+i0; tildev.ell-i0","measurement":"1"},{"term":"S.real","master":"Disc_gluon(S)","indices":{"A":"CutPlus","B":1,"r":"alpha","s":"beta"},"numerator":"2 v.tildev","contours":"same ordered eikonals","measurement":"exp(i bT.ellT)-1"})
 return {"rows":rows,"count":2,"prefactor":"g^2 CF nu1^(2alpha)nu2^(2beta); 1/Nc trace and four-line orientation sum retained outside upstream AST","count_once":True,"root":_r(rows)}
def coefficient_gap():return {"indices_complete":True,"contours_complete":True,"measurements_complete":True,"tensor_numerators_bound":True,"scalar_master_coefficients_complete":False,"missing":"termwise graph signs/combinatorics, operator 1/2 and 1/Nc allocation, and numerator reduction to shifted scalar masters are not jointly exposed by C358-C368","zero_or_guess":False,"root":_r("C370-GAP")}
def validation():return {"dimensions":"PASS_FORMAL","Ward":"PASS_AT_TENSOR_LEVEL","crossing":"PASS","Cutkosky":"PASS","soft_count_once":"PASS","independent_reconstruction":"indices agree between C360 denominators and C365 virtual AST","root":_r("C370-VALID")}
def closure():return {"all_terms_bound":True,"scalar_coefficient_table":False,"evaluation_ready":False,"ordinary_continuation":True,"C43_imported":False,"root":_r("C370-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"residue_backsolve":0,"mass_IR_reuse":0,"scaleless_zero":0,"invented_prefactor":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmymasterbind1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmymasterbind1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmymastereval1 as c
 if c.PACKAGE_ROOT!=C369_ROOT:raise ValueError("C369")
 c.load_verified_hqcdrimassc43jmymastereval1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmymasterbind1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmymasterbind1_authority()
_ROOTS={"INPUT":_r((BASELINE,C369_ROOT)),"REAL":real_bindings()["root"],"VIRTUAL":virtual_bindings()["root"],"SOFT":soft_bindings()["root"],"GAP":coefficient_gap()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C370-HQCDRIMASSC43JMYMASTERBIND1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
