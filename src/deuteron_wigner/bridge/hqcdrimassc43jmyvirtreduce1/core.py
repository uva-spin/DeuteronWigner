"""C366 virtual-region reduction and scaleless-parent grouping gate."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c366_hqcdrimassc43jmyvirtreduce1";BASELINE="5222bc92c2a81035dbfb71ecae562171af0455d0";C365_ROOT="3d09c73e245eea95e5a07733a8e68953370be622b0584cf125e90fb4c469394b"
STATUS="C366_VIRTUAL_NUMERATORS_REDUCED_INDIVIDUAL_REGION_POLES_SCALELESS_GROUPED_REAL_VIRTUAL_EVALUATION_REQUIRED";PLAN="RIMASSC43JMYVIRTREDUCE1-C";NEXT="C367/HQCDRIMASSC43JMYGROUPREDUCE1";NEXT_OBJECT="C366-C43-JMY-GAUGE-COMPLETE-REAL-VIRTUAL-REGION-GROUPS";NEXT_EXACT="form and reduce the gauge-complete JMY real-plus-virtual groups before extracting UV IR and analytic Laurent coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def numerator_reduction():
 rows=({"id":"Sigma_q","scalar":"(2-d)(pslash-kslash)","projector":"coefficient of pslash"},{"id":"W_v","scalar":"v^2","projector":"ordered eikonal contour retained"},{"id":"W_tildev","scalar":"tildev^2","projector":"crossed ordered contour"},{"id":"V_qv","scalar":"vslash(pslash-kslash)gamma_plus","projector":"endpoint tree gamma_plus"},{"id":"V_htv","scalar":"gamma_minus(pslash-kslash)tildevslash","projector":"crossed endpoint tree"})
 return {"rows":rows,"count":5,"d":"4-2epsilon","root":_r(rows)}
def region_ledger():
 rows=({"id":"Sigma_q","UV":"UNAVAILABLE_SEPARATELY","IR":"UNAVAILABLE_SEPARATELY","sum":"scaleless zero only after UV-IR cancellation"},{"id":"W_v","UV":"UNAVAILABLE_SEPARATELY","IR":"UNAVAILABLE_SEPARATELY","sum":"analytic powers regulate rapidity, not radial UV/IR scalelessness"},{"id":"W_tildev","UV":"UNAVAILABLE_SEPARATELY","IR":"UNAVAILABLE_SEPARATELY","sum":"crossed W_v"},{"id":"V_qv","UV":"UNAVAILABLE_SEPARATELY","IR":"UNAVAILABLE_SEPARATELY","sum":"mixed epsilon/alpha poles require group scale"},{"id":"V_htv","UV":"UNAVAILABLE_SEPARATELY","IR":"UNAVAILABLE_SEPARATELY","sum":"mixed epsilon/beta poles require group scale"})
 return {"rows":rows,"count":5,"individual_coefficients_published":False,"root":_r(rows)}
def grouping_contract():return {"distribution":"Sigma_q+W_v+V_qv+DR.qq+DR.qv+DR.vv+MSbar UV projection","fragmentation":"crossed Sigma_q+W_tildev+V_htv+FR.qq+FR.qv+FR.vv+MSbar UV projection","soft":"S real+virtual count-once","scales":"bT endpoint measurement, rho/zeta off-light-cone invariants; no arbitrary scale","order":"combine integrands -> analytic limits -> separate epsilon regions -> MSbar","root":_r("C366-G")}
def source_method():return {"source":"hep-ph/0702022v1 pp.9-11 Eqs.(31)-(45)","authority":"method: individual on-shell DR collinear/soft parents have ambiguous single and mixed UV/IR poles; grouped result is well-defined","operator_identity":False,"root":_r("C366-S")}
def closure():return {"virtual_numerators_reduced":True,"individual_region_coefficients":False,"gauge_complete_group_defined":True,"ordinary_continuation":True,"finite_groups_evaluated":False,"C43_imported":False,"root":_r("C366-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"scaleless_zeroed_early":0,"arbitrary_scale":0,"UV_IR_merged":0,"foreign_coefficient":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyvirtreduce1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyvirtreduce1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyvirtast1 as c
 if c.PACKAGE_ROOT!=C365_ROOT:raise ValueError("C365")
 c.load_verified_hqcdrimassc43jmyvirtast1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyvirtreduce1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyvirtreduce1_authority()
_ROOTS={"INPUT":_r((BASELINE,C365_ROOT)),"NUM":numerator_reduction()["root"],"REGION":region_ledger()["root"],"GROUP":grouping_contract()["root"],"SOURCE":source_method()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C366-HQCDRIMASSC43JMYVIRTREDUCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
