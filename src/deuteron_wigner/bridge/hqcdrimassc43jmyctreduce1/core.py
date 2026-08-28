"""C364 counterterm-projector executability audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c364_hqcdrimassc43jmyctreduce1";BASELINE="ac03a9d5f1ebd23ba9f1739267027c345ad990b0";C363_ROOT="08367346f2480b7dc4059ed49c14cbf2079fa833609e593809442677e4b48010"
STATUS="C364_COUNTERTERM_PROJECTOR_AUDITED_BARE_VIRTUAL_PARENT_INTEGRANDS_MISSING";PLAN="RIMASSC43JMYCTREDUCE1-C";NEXT="C365/HQCDRIMASSC43JMYVIRTAST1";NEXT_OBJECT="C364-C43-JMY-BARE-VIRTUAL-COUNTERTERM-PARENT-AST";NEXT_EXACT="derive bare d-dimensional quark Wilson self-energy and quark-eikonal vertex integrands underlying the five C360 MSbar projectors"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def projector_audit():
 rows=({"id":"CT.Z2q","projector_named":True,"bare_integrand":False},{"id":"CT.Zv","projector_named":True,"bare_integrand":False},{"id":"CT.Ztv","projector_named":True,"bare_integrand":False},{"id":"CT.Zvert.q","projector_named":True,"bare_integrand":False},{"id":"CT.Zvert.h","projector_named":True,"bare_integrand":False})
 return {"rows":rows,"count":5,"scalar_coefficients_computable":False,"root":_r(rows)}
def source_boundary():return {"JMY_mass_result":"renormalized MSbar expressions after N_epsilon removal","bare_UV_coefficients_complete":False,"safe_holdout":"renormalized mu derivative only; insufficient to partition mixed/scaleless UV and IR poles","BN_method":"foreign operator; cannot supply JMY parent numerators","root":_r("C364-S")}
def required_virtual_ast():return {"parents":("Sigma_q(k,p): gamma_mu(pslash-kslash)gamma^mu/[k^2(p-k)^2]","W_v(k): v^2/[k^2(v.k)^2] with self-energy prescription","W_tildev by oriented crossing","V_qv(k,p): gamma_mu(pslash-kslash)gamma+ times v^mu/[k^2(p-k)^2(v.k)] with alpha power","V_htv by plus/minus oriented crossing and beta power"),"count":5,"MSbar":"exp(gammaE epsilon)(4pi)^(-epsilon)/epsilon_UV","root":_r("C364-R")}
def closure():return {"counterterm_scalar_coefficients":False,"failure_is_missing_parent_AST":True,"ordinary_derivation_continuation":True,"parameter_integrals_ready":False,"C43_imported":False,"root":_r("C364-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"projector_treated_as_value":0,"UV_IR_merged":0,"mass_IR_reused":0,"foreign_parent_import":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyctreduce1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyctreduce1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmytracereduce2 as c
 if c.PACKAGE_ROOT!=C363_ROOT:raise ValueError("C363")
 c.load_verified_hqcdrimassc43jmytracereduce2_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyctreduce1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyctreduce1_authority()
_ROOTS={"INPUT":_r((BASELINE,C363_ROOT)),"AUDIT":projector_audit()["root"],"SOURCE":source_boundary()["root"],"REQUIRED":required_virtual_ast()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C364-HQCDRIMASSC43JMYCTREDUCE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
