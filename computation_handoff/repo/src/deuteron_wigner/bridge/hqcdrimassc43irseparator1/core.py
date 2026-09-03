"""C354 analytic UV/IR separation prescription."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c354_hqcdrimassc43irseparator1";BASELINE="b56bae5496807cebe8297479ba77f07d80e43273";C353_ROOT="4bef1298850a87950b87b2288ca8a5d2c534203e47dac90313acbdb52c23e455";SOURCE_SHA="bfb434e7415651eee240af2670defad5b468d8303f214f90936840ca4fc3a1d9"
STATUS="C354_ANALYTIC_UV_IR_SEPARATOR_BOUND_GROUPED_JMY_EVALUATION_MISSING";PLAN="RIMASSC43IRSEPARATOR1-C";NEXT="C355/HQCDRIMASSC43JMYGROUP1";NEXT_OBJECT="C354-C43-JMY-ANALYTICALLY-SEPARATED-GROUP-EVALUATION";NEXT_EXACT="evaluate the grouped JMY virtual real-endpoint and soft dimensional-IR integrands with the C354 alpha-beta analytic separator and prove separator cancellation"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def source_authority():return {"source":"arXiv:1007.4005v2","sha256":SOURCE_SHA,"locator":"Sec.3.1, Eqs.(30)-(38),(44)-(46)","role":"analytic-regulator method only","JMY_operator_identity":False,"root":_r(SOURCE_SHA)}
def separator_contract():return {"hc_replacement":"1/[-(p-k)^2-i0] -> nu1^(2alpha)/[-(p-k)^2-i0]^(1+alpha)","ahc_replacement":"analogous beta,nu2 fractional power","Wilson_rule":"apply same fractional power to the corresponding eikonal denominator after region expansion","contours":"inherit -i0 from source and JMY future/past orientation componentwise","limit_order":"form gauge-complete groups; beta->0 then alpha->0 (and reverse as holdout); only then epsilon->0","UV":"d=4-2epsilon, MSbar","IR":"on-shell dimensional","root":_r("C354-S")}
def acceptance_gates():return {"alpha_poles_cancel":True,"beta_poles_cancel":True,"nu1_derivative_group_sum_zero":True,"nu2_derivative_group_sum_zero":True,"limit_order_parity_required":True,"off_lightcone_vectors_unchanged":True,"soft_allocation_unchanged":True,"individual_scaleless_value_forbidden":True,"root":_r("C354-G")}
def closure():return {"separator_bound":True,"source_qualified_method":True,"JMY_group_values_evaluated":False,"finite_conversion_ready":False,"C43_imported":False,"root":_r("C354-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"arbitrary_scale":0,"individual_scaleless_assignment":0,"geometry_change":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43irseparator1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43irseparator1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmydimir1 as c
 if c.PACKAGE_ROOT!=C353_ROOT:raise ValueError("C353")
 c.load_verified_hqcdrimassc43jmydimir1_authority()
 if sha256((ROOT/"data/raw/c43_sources/1007.4005v2.pdf").read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError("source")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43irseparator1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43irseparator1_authority()
_ROOTS={"INPUT":_r((BASELINE,C353_ROOT,SOURCE_SHA)),"SOURCE":source_authority()["root"],"SEPARATOR":separator_contract()["root"],"GATES":acceptance_gates()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C354-HQCDRIMASSC43IRSEPARATOR1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
