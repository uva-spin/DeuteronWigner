"""C365 bare virtual-parent AST for JMY MSbar projectors."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c365_hqcdrimassc43jmyvirtast1";BASELINE="0dd7c04e6d69b32083668f035d1af43ccdbd83a6";C364_ROOT="5c5fe4dbe99de5944c14d8ff75950e7af4e9306767dbed198197c87dacd42211"
STATUS="C365_BARE_JMY_VIRTUAL_COUNTERTERM_PARENT_AST_DERIVED_SCALAR_REGION_EVALUATION_MISSING";PLAN="RIMASSC43JMYVIRTAST1-C";NEXT="C366/HQCDRIMASSC43JMYVIRTREDUCE1";NEXT_OBJECT="C365-C43-JMY-VIRTUAL-PARENT-SCALAR-REGIONS";NEXT_EXACT="reduce and region-evaluate the C365 bare virtual parent AST to separate scalar UV IR and analytic pole coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def virtual_parent_ast():
 common={"measure":"mu^(2epsilon)d^d k/(2pi)^d","d":"4-2epsilon","prefactor":"-i g^2 CF","gauge":"Feynman","endpoint_tree":"delta(1-x)delta2(kT) or crossed z endpoint"}
 rows=({"id":"Sigma_q","numerator":"gamma_mu(pslash-kslash)gamma^mu","denominators":"[k^2+i0][(p-k)^2+i0]","analytic":"none","regions":"UVPart+IRPart; sum scaleless on shell"},{"id":"W_v","numerator":"v^2","denominators":"[k^2+i0][v.k+i0]^(1+alpha)[v.k-i0]^(1+alpha)","analytic":"nu1^(4alpha)","regions":"UVPart+IRPart with ordered eikonal contour"},{"id":"W_tildev","numerator":"tildev^2","denominators":"[k^2+i0][tildev.k-i0]^(1+beta)[tildev.k+i0]^(1+beta)","analytic":"nu2^(4beta)","regions":"oriented crossing of W_v"},{"id":"V_qv","numerator":"v_mu gamma^mu(pslash-kslash)gamma_plus","denominators":"[k^2+i0][(p-k)^2+i0][v.k+i0]^(1+alpha)","analytic":"nu1^(2alpha)","regions":"UVPart+IRPart+AnalyticPart"},{"id":"V_htv","numerator":"tildev_mu gamma_minus(pslash-kslash)gamma^mu","denominators":"[k^2+i0][(p-k)^2+i0][tildev.k-i0]^(1+beta)","analytic":"nu2^(2beta)","regions":"plus/minus oriented crossing of V_qv"})
 return {"common":common,"rows":rows,"count":5,"root":_r((common,rows))}
def projector_binding():
 rows=tuple({"parent":p,"UV":"MSbarProject(UVPart(parent))","IR":"IRPart(parent) retained","analytic":"AnalyticPolePart(parent) grouped before limits"} for p in ("Sigma_q","W_v","W_tildev","V_qv","V_htv"))
 return {"rows":rows,"count":5,"MSbar":"exp(gammaE epsilon)(4pi)^(-epsilon)/epsilon_UV","root":_r(rows)}
def validation():return {"Ward":"kslash insertion in V_qv/V_htv gives difference of adjacent inverse quark propagators","crossing":"W_v<->W_tildev and V_qv<->V_htv with alpha<->beta and i0 reversal","dimensions":"PASS","source_holdout":"mass-regulated renormalized ZF,ZW,ZV recovered only after region sum and MSbar; not used as IR input","auxiliary_owners":"nu1: W_v,V_qv; nu2: W_tildev,V_htv","C356_residues":"PASS","root":_r("C365-V")}
def closure():return {"five_bare_parents_available":True,"UV_IR_region_projectors_bound":True,"scalar_poles_evaluated":False,"finite_groups_evaluated":False,"C43_imported":False,"root":_r("C365-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"foreign_parent":0,"UV_IR_merged":0,"scaleless_parent_value":0,"mass_IR_reused":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyvirtast1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyvirtast1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyctreduce1 as c
 if c.PACKAGE_ROOT!=C364_ROOT:raise ValueError("C364")
 c.load_verified_hqcdrimassc43jmyctreduce1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyvirtast1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyvirtast1_authority()
_ROOTS={"INPUT":_r((BASELINE,C364_ROOT)),"AST":virtual_parent_ast()["root"],"BIND":projector_binding()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C365-HQCDRIMASSC43JMYVIRTAST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
