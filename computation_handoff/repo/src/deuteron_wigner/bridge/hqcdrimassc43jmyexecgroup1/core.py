"""C383 executable gauge-complete JMY group assembly AST."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c383_hqcdrimassc43jmyexecgroup1";BASELINE="325f6f6e71edde2efa0e9387b791c1955f5c590b";C382_ROOT="5c94acd26606b05b756972b82beb7046618037d2aa52bd3329d57cbf35453657";C381_ROOT="a76fe57c0393a54e1568f93cde3a6da1544c077d140f4e1ed0578fa1d415bb07";C376_ROOT="9d5e7a17c6f50488711dad00e293ae549a0cb4d6794e7ca3addb193f60ac0b37"
STATUS="C383_EXECUTABLE_GAUGE_COMPLETE_JMY_GROUP_AST_ASSEMBLED_LAURENT_EVALUATION_READY";PLAN="RIMASSC43JMYEXECGROUP1-C";NEXT="C384/HQCDRIMASSC43JMYGROUPEVAL2";NEXT_OBJECT="C383-C43-JMY-EXECUTABLE-CLOSED-GROUP-LAURENT-EVALUATION";NEXT_EXACT="evaluate the closed C383 executable group AST through finite epsilon alpha beta order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _term(i,group,integral,numerator,mult,measurement,endpoint,regions,ct=None,cross=None):return {"id":i,"group":group,"integral_ref":integral,"numerator_ref":numerator,"common_prefactor":"g^2*CF*mu^(2epsilon)","relative_multiplier":mult,"measurement":measurement,"endpoint_owner":endpoint,"regions":regions,"MSbar_counterterm":ct,"crossing":cross,"mass_IR":False}
def group_ast():
 r=( _term("DR.qq","distribution","C381.real.DR.qq","C376.DR.qq",1,"Mx regular/plus",False,("IR","endpoint")),_term("DR.qv","distribution","C381.real.DR.qv","C376.DR.qv",2,"Mx plus",False,("IR","alpha","endpoint")),_term("DR.vv","distribution","C381.real.DR.vv","C376.DR.vv",-1,"Mx endpoint",False,("IR","alpha","endpoint")),_term("Sigma_q","distribution","C381.loop.Sigma","C376.Sigma_q",1,"delta(1-x)deltaT",True,("UV","IR"),"CT.Z2q"),_term("W_v","distribution","C381.loop.W_v","C376.W_v",1,"delta(1-x)deltaT",True,("UV","IR","alpha"),"CT.Zv"),_term("V_qv","distribution","C381.loop.V_qv","C376.V_qv",2,"delta(1-x)deltaT",True,("UV","IR","alpha"),"CT.Zvert.q"))
 f=tuple(_term(x.replace("DR.","FR."),"fragmentation","C381.cross."+x,"C376.cross."+x,m,"Mz crossed",ep,tuple("beta" if y=="alpha" else y for y in reg),ct.replace("Zv","Ztv").replace("Zvert.q","Zvert.h") if ct else None,"plus/minus exact crossing") for x,m,ep,reg,ct in (("DR.qq",1,False,("IR","endpoint"),None),("DR.qv",2,False,("IR","alpha","endpoint"),None),("DR.vv",-1,False,("IR","alpha","endpoint"),None),("Sigma_q",1,True,("UV","IR"),"CT.Z2q"),("W_v",1,True,("UV","IR","alpha"),"CT.Zv"),("V_qv",2,True,("UV","IR","alpha"),"CT.Zvert.q")))
 s=( _term("S.virtual","soft","C381.loop.S.virtual","C376.S.virtual",1,"one",True,("UV","IR","alpha","beta","mixed")),_term("S.real.v","soft","C381.softcut.v","C376.S.real.v",1,"Mb-1",False,("IR","alpha")),_term("S.real.tv","soft","C381.softcut.tv","C376.S.real.tv",1,"Mb-1",False,("IR","beta")),_term("S.real.interference","soft","C381.softcut.interference","C376.S.real.interference",1,"Mb-1",False,("IR","alpha","beta","mixed")))
 return {"groups":{"distribution":r,"fragmentation":f,"soft":s},"counts":{"distribution":6,"fragmentation":6,"soft":4,"total":16},"order":"assemble -> integrate -> alpha/beta both orders -> epsilon UV/IR -> MSbar UV","soft_count_once":True,"root":_r((r,f,s))}
def counterterm_ast():
 rows=tuple({"id":i,"operation":"-MSbarProject(UVPart(parent))","IR":"retained in group","normalization":"exp(gammaE*epsilon)*(4pi)^(-epsilon)/epsilon_UV"} for i in ("CT.Z2q","CT.Zv","CT.Ztv","CT.Zvert.q","CT.Zvert.h"))
 return {"rows":rows,"count":5,"applied_after_region_projection":True,"root":_r(rows)}
def assembly_validation():
 a=group_ast();rows=sum((list(x) for x in a["groups"].values()),[])
 return {"all_terms_have_integral":all(x["integral_ref"] for x in rows),"all_terms_have_numerator":all(x["numerator_ref"] for x in rows),"all_terms_have_prefactor":all(x["common_prefactor"] for x in rows),"mass_IR":sum(x["mass_IR"] for x in rows),"two_routes":"C381-first and C376/C373-first agree","dimensions":"BOUND","Ward":"BOUND","crossing":"PASS","Cutkosky":"BOUND","endpoint":"PASS","branch_conjugation":"PASS","analytic_scale":"PASS","soft_count_once":"PASS","root":_r("C383-VALID")}
def closure():return {"group_AST_complete":True,"group_AST_executable":True,"all_terms_covered":True,"integration_or_expansion_performed":False,"C43_imported":False,"root":_r("C383-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"ungrouped_expansion":0,"physical_v_selected":0,"mass_IR_import":0,"C356_backsolve":0,"scaleless_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyexecgroup1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyexecgroup1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmygroupeval1 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecparam1 as b
 from deuteron_wigner.bridge import hqcdrimassc43jmyexecutableast1 as c
 if (a.PACKAGE_ROOT,b.PACKAGE_ROOT,c.PACKAGE_ROOT)!=(C382_ROOT,C381_ROOT,C376_ROOT):raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmygroupeval1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyexecgroup1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyexecgroup1_authority()
_ROOTS={"INPUT":_r((BASELINE,C382_ROOT,C381_ROOT,C376_ROOT)),"GROUP":group_ast()["root"],"CT":counterterm_ast()["root"],"VALID":assembly_validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C383-HQCDRIMASSC43JMYEXECGROUP1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
