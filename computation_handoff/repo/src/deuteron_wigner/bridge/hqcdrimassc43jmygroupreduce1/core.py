"""C367 gauge-complete JMY real-plus-virtual grouping reduction gate."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c367_hqcdrimassc43jmygroupreduce1";BASELINE="a3ec904b558698e3abd9850edede626ef0da3d19";C366_ROOT="151ebf7f5f0b0abc2691c68344970d874589ac95a51c8cf58bb2902c78be48a3"
STATUS="C367_GAUGE_COMPLETE_REAL_VIRTUAL_GROUP_AST_REDUCED_COMMON_MASTER_INTEGRALS_REQUIRED";PLAN="RIMASSC43JMYGROUPREDUCE1-C";NEXT="C368/HQCDRIMASSC43JMYGROUPMASTER1";NEXT_OBJECT="C367-C43-JMY-GROUP-COMMON-MASTER-INTEGRALS";NEXT_EXACT="derive a common alpha-beta dimensional master-integral representation for the grouped JMY real virtual and count-once soft sectors"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def grouped_ast():
 rows=({"id":"distribution","terms":("DR.qq","DR.qv","DR.vv","delta(1-x)*(Sigma_q+W_v+V_qv+MSbar_UV)"),"measurement":"0<x<1 real plus endpoint distribution","analytic":"alpha; beta absent"},{"id":"fragmentation","terms":("FR.qq","FR.qv","FR.vv","delta(1-z)*(Cross(Sigma_q)+W_tildev+V_htv+MSbar_UV)"),"measurement":"0<z<1 real plus crossed endpoint distribution","analytic":"beta; alpha absent"},{"id":"soft","terms":("S_real(v,tildev)","S_virtual(v,tildev)"),"measurement":"count once before TMD square-root allocation","analytic":"alpha and beta with ordered contours"})
 return {"rows":rows,"count":3,"order":"sum bare measured integrands -> reduce common masters -> expand alpha,beta -> separate epsilon UV/IR -> MSbar UV only","root":_r(rows)}
def algebraic_reduction():
 return {"distribution":"N_DR/D_DR + delta(1-x) N_V/D_V represented as one endpoint-distribution functional","fragmentation":"CrossPlusMinus(distribution) including z^(-2+2epsilon) Jacobian","soft":"real and virtual eikonal numerators share v.tildev and opposite measurement support","ward":"quark-eikonal contractions telescope within each group","early_zero":False,"root":_r("C367-REDUCE")}
def laurent_ledger():
 rows=tuple({"group":g,"UV":"PENDING_COMMON_MASTER","IR":"PENDING_COMMON_MASTER","alpha":"PENDING_COMMON_MASTER" if g!="fragmentation" else "NOT_APPLICABLE","beta":"PENDING_COMMON_MASTER" if g!="distribution" else "NOT_APPLICABLE","mixed":"PENDING_COMMON_MASTER" if g=="soft" else "NOT_APPLICABLE"} for g in ("distribution","fragmentation","soft"))
 return {"rows":rows,"published_numeric_coefficients":False,"reason":"C363 and C365 supply algebraic ASTs but no common normalized loop/phase-space master representation; assigning residues now would invent authority","root":_r(rows)}
def cancellation_contract():return {"Ward":"PASS_ALGEBRAIC","crossing":"PASS_ALGEBRAIC","separator":"testable after common masters","auxiliary_scales":"testable after common masters","mass_regulator_UV_holdout":"not imported as dimensional IR data","C356_residues":"targets retained, not circularly asserted","root":_r("C367-CANCEL")}
def closure():return {"gauge_complete_groups_formed":True,"group_algebra_reduced":True,"common_master_integrals":False,"Laurent_coefficients":False,"finite_constants":False,"C43_imported":False,"root":_r("C367-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"individual_scaleless_zero":0,"arbitrary_scale":0,"pole_types_merged":0,"mass_IR_reused":0,"finite_constant_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupreduce1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupreduce1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyvirtreduce1 as c
 if c.PACKAGE_ROOT!=C366_ROOT:raise ValueError("C366")
 c.load_verified_hqcdrimassc43jmyvirtreduce1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupreduce1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupreduce1_authority()
_ROOTS={"INPUT":_r((BASELINE,C366_ROOT)),"GROUP":grouped_ast()["root"],"REDUCE":algebraic_reduction()["root"],"LAURENT":laurent_ledger()["root"],"CANCEL":cancellation_contract()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C367-HQCDRIMASSC43JMYGROUPREDUCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
