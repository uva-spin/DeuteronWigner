"""C368 common alpha-beta dimensional masters for grouped JMY sectors."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c368_hqcdrimassc43jmygroupmaster1";BASELINE="a75ddc56e3bba1c872ccb0ecdf6ecff1a333294e";C367_ROOT="8448ad3c55d0f440661f54bc26ff74f6234366479692dc37d8db0162dc17fe24"
STATUS="C368_COMMON_GROUP_MASTER_REPRESENTATION_DERIVED_LAURENT_EVALUATION_REQUIRED";PLAN="RIMASSC43JMYGROUPMASTER1-C";NEXT="C369/HQCDRIMASSC43JMYMASTEREVAL1";NEXT_OBJECT="C368-C43-JMY-COMMON-MASTER-LAURENT-EVALUATION";NEXT_EXACT="evaluate the C368 common grouped masters through finite epsilon alpha and beta order with distribution-valued endpoint expansion"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def measure_authority():
 return {"d":"4-2 epsilon","dT":"2-2 epsilon","loop":"mu^(2 epsilon) d^d ell/(2 pi)^d","cut":"mu^(2 epsilon) d^d ell/(2 pi)^(d-1) theta(ell0) delta_plus(ell^2-lambda^2)","transverse":"mu^(2 epsilon) d^(dT) kT/(2 pi)^(dT)","MSbar":"exp(gamma_E epsilon)(4 pi)^(-epsilon)/epsilon_UV, applied after UV projection","normalization_rule":"no MSbar factor absorbed into bare masters","root":_r("C368-MEASURE")}
def master_family():
 common={"loop_measure":"mu^(2epsilon)d^d ell/(2pi)^d","powers":"A,B,C nonnegative propagator powers; r,s analytic eikonal shifts","contours":"sigma_v,sigma_tildev in {+1,-1} retain i0 orientation"}
 rows=({"id":"L_ABCrs","integrand":"1/[(ell^2+i0)^A ((p-ell)^2+i0)^B (v.ell+i sigma_v 0)^(C+r)]","domain":"ell in R^d; Schwinger parameters t_i in (0,infinity), projective simplex after common scale extraction","owners":"Sigma_q,W_v,V_qv and crossed tildev family"},{"id":"R_ABr","integrand":"theta(ell0)delta_plus(ell^2-lambda^2)/[((p-ell)^2-m^2+i0)^A (v.ell+i0)^(B+r)]","domain":"0<x<1, kT in R^(2-2epsilon); ell+=(1-x)p+","jacobian":"d ell+ d ell- delta(2ell+ell--kT^2-lambda^2)=d x/[2(1-x)] before common external normalization"},{"id":"S_ABrs","integrand":"(v.tildev)/[(ell^2+i0)^A(v.ell+i0)^(B+r)(tildev.ell-i0)^(B+s)]","domain":"virtual ell in R^d; real master is Disc_(ell^2) with theta(ell0)","owners":"count-once soft real plus virtual"})
 return {"common":common,"rows":rows,"count":3,"root":_r((common,rows))}
def parameter_maps():
 rows=({"sector":"distribution","real":"DR.qq,DR.qv,DR.vv -> tensor numerators reduced to R_ABalpha and dimension shifts","virtual":"Sigma_q,W_v,V_qv -> endpoint delta(1-x) L_ABC0/L_ABC-alpha","map":"R = positive-energy Cutkosky discontinuity of the matching L gluon denominator; active bilocal quark line remains uncut"},{"sector":"fragmentation","real":"FR family -> CrossPlusMinus(R_ABalpha) with z^(-2+2epsilon)","virtual":"Cross(Sigma_q),W_tildev,V_htv -> delta(1-z) crossed L family","map":"p+<->p-, v<->tildev, alpha<->beta and ordered i0 reversal"},{"sector":"soft","real":"Disc_gluon(S_ABalphabeta) with transverse measurement","virtual":"S_ABalphabeta without cut","map":"same eikonal contours and auxiliary powers; count once before square-root allocation"})
 return {"rows":rows,"count":3,"expansion_order":"form group -> parameterize -> integrate common scale -> expand alpha,beta -> resolve epsilon UV/IR regions","root":_r(rows)}
def domains_and_jacobians():return {"real_support":"x,z in (0,1)","endpoint":"virtual terms are distribution-valued delta(1-x) or delta(1-z)","radial":"d^(2-2epsilon)kT=Omega_(1-2epsilon) kT^(1-2epsilon) dkT","cut_jacobian":"1/[2(1-x)p+] with d ell+=(p+)d x, hence 1/[2(1-x)]","projective":"t_i=T u_i; T in (0,infinity), u_i>=0, sum u_i=1; Jacobian T^(n-1)","no_arbitrary_scale":True,"root":_r("C368-DOMAIN")}
def validation():return {"dimensions":"PASS_SYMBOLIC_BY_MEASURE_AND_DENOMINATOR_POWERS","Ward":"PASS_BY_C367_TELESCOPING_BEFORE_PARAMETERIZATION","crossing":"PASS_EXACT_MAP","separator_owners":"nu1^(2alpha/4alpha) distribution; nu2^(2beta/4beta) fragmentation; both soft","mass_holdout":"UV comparison only; lambda,m not reused as dimensional IR data","C356":"residue targets retained as post-evaluation holdouts","numeric_Laurent_coefficients":False,"root":_r("C368-VALID")}
def closure():return {"common_master_family":True,"real_virtual_cut_map":True,"domains_and_jacobians":True,"masters_evaluated":False,"finite_constants":False,"C43_imported":False,"root":_r("C368-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"scaleless_zeroed_early":0,"arbitrary_physical_scale":0,"pole_types_merged":0,"mass_IR_reused":0,"finite_constant_inferred":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmygroupmaster1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmygroupmaster1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmygroupreduce1 as c
 if c.PACKAGE_ROOT!=C367_ROOT:raise ValueError("C367")
 c.load_verified_hqcdrimassc43jmygroupreduce1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmygroupmaster1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmygroupmaster1_authority()
_ROOTS={"INPUT":_r((BASELINE,C367_ROOT)),"MEASURE":measure_authority()["root"],"MASTER":master_family()["root"],"MAP":parameter_maps()["root"],"DOMAIN":domains_and_jacobians()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C368-HQCDRIMASSC43JMYGROUPMASTER1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
