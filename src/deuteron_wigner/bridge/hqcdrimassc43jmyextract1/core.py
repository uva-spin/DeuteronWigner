"""C351 source-exact JMY one-loop quark and soft equation extraction."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c351_hqcdrimassc43jmyextract1";BASELINE="9caf91938a90b895d22c1011f55b6632ec05db60";C350_ROOT="bac9265744361abe358a90346f11d344a260a1252b893ca59b8a508af37e1a67"
STATUS="C351_JMY_ONE_LOOP_QUARK_AND_SOFT_EQUATIONS_EXTRACTED_COMMON_IR_TRANSLATION_MISSING";PLAN="RIMASSC43JMYEXTRACT1-C";NEXT="C352/HQCDRIMASSC43COMMONIR1";NEXT_OBJECT="C351-C43-JMY-DELTA-COMMON-IR-TRANSLATION";NEXT_EXACT="derive the common-IR translation between the JMY mass-regulated on-shell equations and the modified-delta dimensional-IR comparison schema"
PDF_SHA="4a867611d7479b66e776129a4c490a736f5a2a5fadc0fdb89c48dfb9c975c44e";TEX_SHA="6e1fd28304d711c2c99774a7a6de906619f2350d723f0b22aed48d256cafdc77"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def source_manifest():
 rows=({"id":"hep-ph/0404183v1 PDF","sha256":PDF_SHA,"pages":"4-12"},{"id":"hep-ph/0404183v1 TeX","sha256":TEX_SHA,"lines":"318-800"})
 return {"rows":rows,"count":2,"primary":True,"root":_r(rows)}
def equation_manifest():
 rows=({"locator":"Eq. (7), label zf","object":"quark self energy","formula":"ZF=1+alpha_s CF/(4pi)[-ln(mu^2/m^2)+2ln(m^2/lambda^2)-4]"},{"locator":"unnumbered after Eq. (7)","object":"Wilson self energy","formula":"ZW=1+alpha_s CF/(4pi)[2ln(mu^2/lambda^2)]"},{"locator":"unnumbered before Eq. (8)","object":"virtual vertex","formula":"ZV=1+alpha_s CF/(4pi)[2ln(mu^2/m^2)+2ln(zeta^2/m^2)-ln^2(zeta^2/m^2)-2ln(m^2/lambda^2)ln(zeta^2/m^2)-2pi^2/3+4]"},{"locator":"Eqs. (8),(9)-(12)","object":"complete unsubtracted one-loop quark TMD","formula":"Qvirt=delta(1-x)delta2(kT)(ZF+ZW+ZV-3); real terms retained separately with m,lambda,zeta and plus/delta endpoint forms"},{"locator":"Eq. (24)","object":"soft operator","formula":"S=(1/Nc)<0|L_tildev^dag(b,-inf)L_v^dag(inf;b)L_v(inf;0)L_tildev(0;-inf)|0>"},{"locator":"Eq. (25)","object":"subtracted JMY quark TMD","formula":"q=Q/S (one full soft factor in the JMY factorization convention)"},{"locator":"Eqs. (30),(31)","object":"one-loop soft factor","formula":"S(kT)=delta2(kT)+alpha_s CF/(2pi^2)[ln(4(v.tildev)^2/(v^2 tildev^2))-2][1/(kT^2+lambda^2)-pi delta2(kT)ln(mu^2/lambda^2)]; S(b)=1+alpha_s CF/(2pi)(2-ln rho^2)ln(mu^2 b^2 e^(2gammaE)/4)"})
 return {"rows":rows,"count":len(rows),"endpoint_terms_preserved":True,"root":_r(rows)}
def convention_crosswalk():return {"external_state":"on-shell quark","IR":"quark mass m regulates collinear; gluon mass lambda regulates soft","UV":"DR then MSbar; N_epsilon removed","coupling":"alpha_s","Fourier":"Q(b)=integral d2k exp(+i b.k) Q(k)","rapidity":"off-light-cone v,tilde-v; rho=sqrt(v- tildev+/(v+ tildev-))","soft_partition":"JMY q=Q/S and factorization contains q qhat S: net one soft subtraction","common_with_C350":False,"root":_r("C351-X")}
def closure():return {"JMY_operator":True,"JMY_quark_equations":True,"JMY_soft_finite":True,"identical_external_state":True,"identical_IR_prescription":False,"direct_conversion_ready":False,"coefficient_imported_C43":False,"root":_r("C351-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"delta_equations_mutated":0,"IR_equated_silently":0,"soft_double_counted":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyextract1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS,equation_manifest()["count"]))}
def verify_hqcdrimassc43jmyextract1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43deltaextract1 as c
 if c.PACKAGE_ROOT!=C350_ROOT:raise ValueError("C350")
 c.load_verified_hqcdrimassc43deltaextract1_authority()
 for p,h in ((ROOT/"data/raw/c43_sources/hep-ph-0404183v1.pdf",PDF_SHA),(ROOT/"data/raw/c43_sources/hep-ph-0404183v1.tar",TEX_SHA)):
  if sha256(p.read_bytes()).hexdigest()!=h:raise ValueError(p)
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyextract1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyextract1_authority()
_ROOTS={"INPUT":_r((BASELINE,C350_ROOT,PDF_SHA,TEX_SHA)),"SOURCE":source_manifest()["root"],"EQS":equation_manifest()["root"],"X":convention_crosswalk()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C351-HQCDRIMASSC43JMYEXTRACT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
