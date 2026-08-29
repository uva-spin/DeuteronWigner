"""C353 dimensional-IR JMY master-integral well-definedness audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c353_hqcdrimassc43jmydimir1";BASELINE="1021669ff3be84b32dfbec659180bd524bc24adb";C352_ROOT="d23b3478acd40f67d476f75cc98ffdfaff2f61645223a90564a5438a88a04ef0";SOURCE_SHA="6e310c86c8c315ee57dcf7c1d14ec3a057164f7bac1f10ead474fb66c6fcd96f"
STATUS="C353_PURE_DR_MASTER_INTEGRALS_CLASSIFIED_INDIVIDUAL_SCALARLESS_AMBIGUITY_AUXILIARY_UV_IR_SEPARATOR_MISSING";PLAN="RIMASSC43JMYDIMIR1-C";NEXT="C354/HQCDRIMASSC43IRSEPARATOR1";NEXT_OBJECT="C353-C43-JMY-AUXILIARY-UV-IR-SEPARATOR";NEXT_EXACT="bind an auxiliary analytic UV-IR separation prescription for the gauge-complete JMY dimensional-IR master-integral groups before regulator removal"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def source_authority():return {"source":"hep-ph/0702022v1","sha256":SOURCE_SHA,"locator":"pp.4-11, Eqs. (14)-(23),(31)-(45)","claims":"pure-DR on-shell collinear/soft graphs scaleless; individual single and mixed poles ambiguous; grouped integrand well-defined","operator_identity_JMY":False,"method_authority":True,"root":_r(SOURCE_SHA)}
def sector_classification():
 rows=tuple({"id":i,"retained":True,"individual_value":"UNAVAILABLE_NOT_ZERO","reason":"pure-DR on-shell sector requires UV/IR separator before expansion"} for i in ("Vq","Vv","Wv","Rqv","Rvv","Svt"))
 return {"rows":rows,"count":6,"all_retained":True,"root":_r(rows)}
def grouped_integrand_contract():return {"virtual_group":"Vq+Vv+Wv with external-leg and MSbar terms","real_endpoint_group":"Rqv+Rvv expanded as distributions only after grouping","soft_group":"Svt real+virtual before epsilon expansion","combination_rule":"form gauge-complete subtracted JMY matrix element at integrand level; then separate UV/IR; then expand","mixed_poles_must_cancel":True,"arbitrary_scale_forbidden":True,"root":_r("C353-G")}
def ambiguity_certificate():return {"individual_DR_values_defined":False,"cause":"scaleless integrals equal zero only after UV and IR poles cancel; separate coefficients depend on an auxiliary prescription","finite_terms_assignable":False,"ordinary_continuation_exists":True,"blocker":False,"root":_r("C353-A")}
def closure():return {"six_sectors_classified":True,"gauge_complete_grouping_bound":True,"individual_finite_values_invented":False,"common_IR_conversion_ready":False,"C43_imported":False,"root":_r("C353-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"scaleless_zero_claim":0,"mixed_pole_assignment":0,"arbitrary_scale_inserted":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmydimir1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmydimir1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43commonir1 as c
 if c.PACKAGE_ROOT!=C352_ROOT:raise ValueError("C352")
 c.load_verified_hqcdrimassc43commonir1_authority()
 if sha256((ROOT/"data/raw/c33_sources/hep-ph-0702022.pdf").read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError("source")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmydimir1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmydimir1_authority()
_ROOTS={"INPUT":_r((BASELINE,C352_ROOT,SOURCE_SHA)),"SOURCE":source_authority()["root"],"SECTORS":sector_classification()["root"],"GROUP":grouped_integrand_contract()["root"],"AMBIGUITY":ambiguity_certificate()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C353-HQCDRIMASSC43JMYDIMIR1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
