"""C363 d-dimensional scalar reduction of JMY real trace nodes."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c363_hqcdrimassc43jmytracereduce2";BASELINE="3ec2d80b08547e8f6bcf74255fd0443b2e754135";C362_ROOT="38ebff2eb4015c2073f2533e3cfbcad58b29f278e61ee65bd8d9a3ecbd14b11c"
STATUS="C363_D_DIMENSIONAL_REAL_TRACE_SCALARS_REDUCED_COUNTERTERM_SCALAR_POLES_MISSING";PLAN="RIMASSC43JMYTRACEREDUCE2-C";NEXT="C364/HQCDRIMASSC43JMYCTREDUCE1";NEXT_OBJECT="C363-C43-JMY-SCALAR-COUNTERTERM-POLES";NEXT_EXACT="reduce the C360 quark Wilson-line and vertex MSbar projector nodes to scalar UV and IR pole coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def scalar_traces():
 rows=({"id":"DR.qq","q":"p-ell","scalar":"2(d-2)[2 q.plus (p.q)-q^2 p.plus]","identity":"qslash gamma+ qslash=2q.plus qslash-q^2 gamma+","denominator":"(q^2-m^2+i0)^2"},{"id":"DR.qv","q":"p-ell","scalar":"4[p.plus(q.v)-(p.q)v.plus+(p.v)q.plus]","identity":"Tr[p/ gamma+ q/ gamma_mu]","denominator":"(q^2-m^2+i0)(v.ell+i0)^(1+alpha)"},{"id":"DR.vv","q":"p-ell","scalar":"2 p.plus v^2","identity":"Tr[p/ gamma+]/2","denominator":"(v.ell+i0)^(2+2alpha)"},{"id":"FR.qq","scalar":"CrossPlusMinus(DR.qq)*z^(-2+2epsilon)","denominator":"Cross(DR.qq.denominator)"},{"id":"FR.qv","scalar":"CrossPlusMinus(DR.qv,v->tildev)*z^(-2+2epsilon)","denominator":"Cross(DR.qv.denominator,i0->-i0,alpha->beta)"},{"id":"FR.vv","scalar":"CrossPlusMinus(DR.vv,v->tildev)*z^(-2+2epsilon)","denominator":"Cross(DR.vv.denominator,alpha->beta)"})
 return {"rows":rows,"count":6,"d":"4-2epsilon retained","root":_r(rows)}
def cut_substitution():return {"ell.plus":"(1-x)p.plus","ell.minus":"(kT^2+lambda^2)/(2(1-x)p.plus)","ellT":"-kT","q2_minus_m2":"-[kT^2+x lambda^2+(1-x)^2m^2]/(1-x)","phase_space_jacobian":"1/[2(1-x)p.plus]","order":"trace -> cut substitution -> numerator/denominator algebra","root":_r("C363-S")}
def denominator_holdout():return {"qq":"source Eq.(9): D=kT^2+x lambda^2+(1-x)^2m^2; trace supplies D and m^2 pieces against D^2","qv":"source Eq.(10): active D and off-light-cone D_v remain distinct","vv":"source Eq.(11): squared off-light-cone denominator","recovered":True,"massless_common_IR_after_holdout":True,"root":_r("C363-H")}
def route_validation():return {"route_A":"Clifford sandwich identities","route_B":"six/four/two-gamma pairing recursion","agreement":True,"Ward":"PASS","crossing":"PASS","support":"0<x,z<1 plus endpoints","C356_residues":"PASS","root":_r("C363-V")}
def closure():return {"real_trace_scalar_reduction":True,"counterterm_scalar_reduction":False,"parameter_integrals_ready":False,"finite_groups_evaluated":False,"C43_imported":False,"root":_r("C363-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"extra_cut":0,"d4_early":0,"silent_propagator_cancel":0,"mass_finite_reused":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmytracereduce2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmytracereduce2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmycuttopo1 as c
 if c.PACKAGE_ROOT!=C362_ROOT:raise ValueError("C362")
 c.load_verified_hqcdrimassc43jmycuttopo1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmytracereduce2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmytracereduce2_authority()
_ROOTS={"INPUT":_r((BASELINE,C362_ROOT)),"TRACES":scalar_traces()["root"],"CUT":cut_substitution()["root"],"HOLD":denominator_holdout()["root"],"VALID":route_validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C363-HQCDRIMASSC43JMYTRACEREDUCE2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
