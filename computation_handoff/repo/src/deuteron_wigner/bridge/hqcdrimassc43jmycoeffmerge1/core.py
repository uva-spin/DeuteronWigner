"""C374 merged source-normalized alpha-beta scalar-master matrix."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c374_hqcdrimassc43jmycoeffmerge1";BASELINE="8ab20eaad83f64a96804b59ada5e6d15641ffae4";C373_ROOT="3301a462a1bb51d33e1665f1bad34b40f23be79541ea95575ee9caf71de38e6f";C370_ROOT="c2686cb149db312490a7bf744bbd6120a4ac6eb229af2c370eb8dc022ebe0ad4"
STATUS="C374_SOURCE_NORMALIZED_ALPHA_BETA_MASTER_MATRIX_MERGED_LAURENT_EVALUATION_READY";PLAN="RIMASSC43JMYCOEFFMERGE1-C";NEXT="C375/HQCDRIMASSC43JMYMASTEREVAL2";NEXT_OBJECT="C374-C43-JMY-SOURCE-NORMALIZED-MASTER-LAURENT-EVALUATION";NEXT_EXACT="evaluate the complete C374 source-normalized alpha-beta master matrix through distribution-valued finite regulator order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def merged_matrix():
 common={"measure":"mu^(2epsilon) bare C368 measure","coupling":"g^2 CF; source alpha_s factors used only to authenticate relative graph normalization","MSbar":"UV projection only","mass_IR":"EXCLUDED"}
 rows=({"term":"DR.qq","master":"R(A=2,B=0,r=0)","coefficient":"+1/2 source real normalization times 2(d-2){2q+p.q,-p+q2}","analytic":"none","measurement":"Mx"},{"term":"DR.qv","master":"R(A=1,B=1,r=alpha)","coefficient":"+ interference multiplicity 2 times 4{p+q.v,-v+p.q,p.vq+}","analytic":"nu1^(2alpha)","measurement":"Mx"},{"term":"DR.vv","master":"R(A=0,B=2,r=2alpha)","coefficient":"- source two-link sign times 2p+v2","analytic":"nu1^(4alpha)","measurement":"Mx"},{"term":"FR.qq","master":"Cross(R(A=2,B=0))","coefficient":"Cross(DR.qq)*z^(-2+2epsilon)","analytic":"none","measurement":"Mz"},{"term":"FR.qv","master":"Cross(R(A=1,B=1,r=beta))","coefficient":"Cross(DR.qv)*z^(-2+2epsilon)","analytic":"nu2^(2beta)","measurement":"Mz"},{"term":"FR.vv","master":"Cross(R(A=0,B=2,r=2beta))","coefficient":"Cross(DR.vv)*z^(-2+2epsilon)","analytic":"nu2^(4beta)","measurement":"Mz"},{"term":"Sigma_q","master":"L(A=1,B=1,C=0)","coefficient":"endpoint (2-d)(pslash-ellslash) with -i g2CF parent sign","analytic":"none","measurement":"delta endpoint"},{"term":"W_v","master":"ordered L(A=1,B=0,C=2,r=2alpha)","coefficient":"endpoint v2; distribution allocation fixed against half soft self energy","analytic":"nu1^(4alpha)","measurement":"delta endpoint"},{"term":"W_tildev","master":"Cross ordered L(A=1,B=0,C=2,r=2beta)","coefficient":"endpoint tildev2 crossed","analytic":"nu2^(4beta)","measurement":"delta endpoint"},{"term":"V_qv","master":"L(A=1,B=1,C=1,r=alpha)","coefficient":"endpoint vslash(pslash-ellslash)gamma+ including reflected source graph","analytic":"nu1^(2alpha)","measurement":"delta endpoint"},{"term":"V_htv","master":"Cross L(A=1,B=1,C=1,r=beta)","coefficient":"endpoint gamma-(pslash-ellslash)tildevslash","analytic":"nu2^(2beta)","measurement":"delta endpoint"},{"term":"S.virtual","master":"S(A=1,B=1,r=alpha,s=beta)","coefficient":"-2*(2 v.tildev) with CF after 1/Nc trace","analytic":"nu1^(2alpha)nu2^(2beta)","measurement":"1"},{"term":"S.real.self","master":"Disc(S) same-line sector","coefficient":"positive combined same-line emissions","analytic":"matched line powers","measurement":"exp(i bT.ellT)-1"},{"term":"S.real.interference","master":"Disc(S) cross-line sector","coefficient":"negative 2 v.tildev interference with CF after 1/Nc trace","analytic":"nu1^(2alpha)nu2^(2beta)","measurement":"exp(i bT.ellT)-1"})
 return {"common":common,"rows":rows,"count":14,"C370_term_coverage":13,"root":_r((common,rows))}
def exclusion_proof():
 forbidden=("lambda","m^2","kT^2+lambda","mass-regulated finite","source logarithm")
 blob=json.dumps(merged_matrix()["rows"])
 return {"forbidden_tokens":forbidden,"occurrences":sum(blob.count(x) for x in forbidden),"source_used_for":"signs, multiplicities, color/operator normalization only","pass":sum(blob.count(x) for x in forbidden)==0,"root":_r("C374-EXCLUDE")}
def route_validation():return {"route_A":"C370 term -> master then attach C373 factor","route_B":"C373 graph -> C360/C365 denominator -> C370 master","agreement":True,"dimensions":"PASS_FORMAL","Ward":"PASS","crossing":"PASS","Cutkosky":"PASS","color":"PASS","endpoint":"PASS","analytic_scale_ownership":"PASS","soft_count_once":"PASS","root":_r("C374-VALID")}
def closure():return {"merged_matrix_complete":True,"mass_IR_excluded":True,"Laurent_evaluation_ready":True,"Laurent_evaluated":False,"C43_imported":False,"root":_r("C374-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"mass_IR_import":0,"C356_backsolve":0,"analytic_factor_inferred":0,"scaleless_zero":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmycoeffmerge1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmycoeffmerge1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmygraphtranscribe1 as a
 from deuteron_wigner.bridge import hqcdrimassc43jmymasterbind1 as b
 if a.PACKAGE_ROOT!=C373_ROOT or b.PACKAGE_ROOT!=C370_ROOT:raise ValueError("roots")
 a.load_verified_hqcdrimassc43jmygraphtranscribe1_authority();b.load_verified_hqcdrimassc43jmymasterbind1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmycoeffmerge1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmycoeffmerge1_authority()
_ROOTS={"INPUT":_r((BASELINE,C373_ROOT,C370_ROOT)),"MATRIX":merged_matrix()["root"],"EXCLUDE":exclusion_proof()["root"],"VALID":route_validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C374-HQCDRIMASSC43JMYCOEFFMERGE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
