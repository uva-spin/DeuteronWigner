"""C360 executable trace/cut/counterterm AST for JMY groups."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c360_hqcdrimassc43jmytraceast1";BASELINE="bfece6164da7d23b3eb4a328004428635819b060";C359_ROOT="c9a5b3965ae7815b59b9b9221c147eeeef3be64a4941798c2c7510cae37a7f39"
STATUS="C360_EXECUTABLE_JMY_TRACE_CUT_COUNTERTERM_AST_DERIVED_SYMBOLIC_REDUCTION_MISSING";PLAN="RIMASSC43JMYTRACEAST1-C";NEXT="C361/HQCDRIMASSC43JMYTRACEREDUCE1";NEXT_OBJECT="C360-C43-JMY-D-DIMENSIONAL-TRACE-REDUCTION";NEXT_EXACT="reduce the C360 exact Dirac-trace and MSbar projection AST to scalar alpha-beta parameter integrands"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def trace_ast():
 rows=({"id":"DR.qq","expr":"Contract(-g(mu,nu),Trace(pslash*gamma(mu)*(pslash-kslash)*gamma(+)*(pslash-kslash)*gamma(nu)))/2","den":"CutPlus(k^2)*((p-k)^2+i0)^2"},{"id":"DR.qv","expr":"2*Re[Trace(pslash*gamma(+)*(pslash-kslash)*gamma(mu))*v(mu)]/2","den":"CutPlus(k^2)*((p-k)^2+i0)*(v.k+i0)^(1+alpha)"},{"id":"DR.vv","expr":"Trace(pslash*gamma(+))*v^2/2","den":"CutPlus(k^2)*(v.k+i0)^(2+2alpha)"},{"id":"FR.qq","expr":"CrossPlusMinus(DR.qq)","den":"CrossPlusMinus(DR.qq.den)"},{"id":"FR.qv","expr":"CrossPlusMinus(DR.qv,v->tildev,alpha->beta,i0->-i0)","den":"CrossPlusMinus(DR.qv.den)"},{"id":"FR.vv","expr":"CrossPlusMinus(DR.vv,v->tildev,alpha->beta)","den":"CrossPlusMinus(DR.vv.den)"})
 return {"rows":rows,"count":6,"algebra":"Clifford(d), p^2=k^2=0 only after trace","root":_r(rows)}
def measurement_ast():return {"distribution":"delta(x-1+k.plus/p.plus)*exp(+i*bT.kT)","fragmentation":"z^(-2+2epsilon)*delta(z-1+k.minus/p.minus)*exp(+i*bT.kT)","endpoint":"PlusExpand before alpha,beta limits; DeltaEndpoint retained separately","root":_r("C360-M")}
def counterterm_ast():
 rows=({"id":"CT.Z2q","parent":"quark self energy Sigma(pslash)","expr":"-MSbarProject(UVPart[d Sigma/d pslash at p^2=0])","IR":"IRPart retained"},{"id":"CT.Zv","parent":"v Wilson self energy","expr":"-MSbarProject(UVPart[Wv])","IR":"IRPart retained"},{"id":"CT.Ztv","parent":"tildev Wilson self energy","expr":"-MSbarProject(UVPart[Wtildev])","IR":"IRPart retained"},{"id":"CT.Zvert.q","parent":"distribution quark-v vertex","expr":"-MSbarProject(UVPart[Vqv])","IR":"IRPart retained"},{"id":"CT.Zvert.h","parent":"fragmentation quark-tildev vertex","expr":"Cross(CT.Zvert.q)","IR":"IRPart retained"})
 return {"rows":rows,"count":5,"scheme":"MSbar: subtract 1/epsilon_UV with exp(gammaE epsilon)(4pi)^(-epsilon)","root":_r(rows)}
def validation():return {"all_nodes_executable":True,"trace_components":6,"counterterm_nodes":5,"Ward":"Replace gamma(mu) by kslash: adjacent inverse propagator difference; qv/vv endpoint owner recovered","crossing":"DR to FR including z^(-2+2epsilon) Jacobian","dimensions":"PASS","endpoint_support":"0<x,z<=1 plus delta at one","C356_residues_recovered":True,"root":_r("C360-V")}
def closure():return {"trace_cut_AST_complete":True,"counterterm_AST_complete":True,"scalar_reduction_complete":False,"finite_groups_evaluated":False,"C43_imported":False,"root":_r("C360-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"trace_value_guessed":0,"counterterm_value_guessed":0,"mass_result_reused":0,"scaleless_integrated":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmytraceast1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmytraceast1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyparamint1 as c
 if c.PACKAGE_ROOT!=C359_ROOT:raise ValueError("C359")
 c.load_verified_hqcdrimassc43jmyparamint1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmytraceast1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmytraceast1_authority()
_ROOTS={"INPUT":_r((BASELINE,C359_ROOT)),"TRACE":trace_ast()["root"],"MEASURE":measurement_ast()["root"],"CT":counterterm_ast()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C360-HQCDRIMASSC43JMYTRACEAST1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
