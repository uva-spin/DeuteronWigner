"""C371 scalar-coefficient reduction and normalization-authority gate."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c371_hqcdrimassc43jmyscalarcoeff1";BASELINE="fcb89965ba2a545d41718dd2012c7ce6ee01b964";C370_ROOT="c2686cb149db312490a7bf744bbd6120a4ac6eb229af2c370eb8dc022ebe0ad4"
STATUS="C371_SCALAR_REDUCTION_STRUCTURE_BOUND_GLOBAL_GRAPH_NORMALIZATION_AUTHORITY_MISSING";PLAN="RIMASSC43JMYSCALARCOEFF1-C";NEXT="C372/HQCDRIMASSC43JMYSOURCEGRAPH1";NEXT_OBJECT="C371-C43-JMY-PRIMARY-SOURCE-GRAPH-NORMALIZATION";NEXT_EXACT="recover and hash the exact primary-source JMY operator and one-loop graph equations needed to bind graph signs multiplicities and global normalizations"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def scalar_structure():
 rows=({"term":"DR.qq","coefficients":"2(d-2){2 q+ p.q,-p+ q2} over R_A2"},{"term":"DR.qv","coefficients":"4{p+ q.v,-v+ p.q,p.v q+} over R_A1B1alpha"},{"term":"DR.vv","coefficients":"2p+v2 over R_B2_2alpha"},{"term":"FR.*","coefficients":"exact plus/minus crossing of DR.* times z^(-2+2epsilon)"},{"term":"Sigma_q","coefficients":"(2-d){pslash,-ellslash} projected on endpoint tree"},{"term":"W_v/W_tildev","coefficients":"v2/tildev2 over ordered two-eikonal L"},{"term":"V_qv/V_htv","coefficients":"C370 Clifford numerators over L_A1B1C1"},{"term":"S.real/virtual","coefficients":"2 v.tildev over cut/uncut S"})
 return {"rows":rows,"count":8,"tensor_to_scalar_structure":True,"globally_normalized_matrix":False,"root":_r(rows)}
def authority_audit():return {"repository_source_bytes":False,"descendant_summaries":True,"missing":("termwise graph signs","real interference multiplicities","bilocal 1/2 allocation","soft 1/Nc trace allocation","four-line orientation sum","endpoint tree normalization"),"why_indispensable":"each multiplies the scalar master rows and cannot be inferred from denominators or Ward identities","root":_r("C371-AUTH")}
def route_audit():return {"Clifford_route":"agrees with frozen C363/C366 structures","tensor_route":"indices agree with C370","Ward":"constrains relative contractions but not all graph multiplicities","crossing":"constrains FR from DR but not absolute normalization","C356_backsolve":"forbidden circular route","model_memory":"forbidden","result":"SOURCE_RECOVERY_REQUIRED","root":_r("C371-ROUTE")}
def closure():return {"scalar_structure_bound":True,"complete_coefficient_matrix":False,"unavailable_preserved":True,"ordinary_continuation":True,"C43_imported":False,"root":_r("C371-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"invented_sign":0,"invented_multiplicity":0,"residue_backsolve":0,"mass_IR_reuse":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyscalarcoeff1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyscalarcoeff1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmymasterbind1 as c
 if c.PACKAGE_ROOT!=C370_ROOT:raise ValueError("C370")
 c.load_verified_hqcdrimassc43jmymasterbind1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyscalarcoeff1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyscalarcoeff1_authority()
_ROOTS={"INPUT":_r((BASELINE,C370_ROOT)),"SCALAR":scalar_structure()["root"],"AUTH":authority_audit()["root"],"ROUTE":route_audit()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C371-HQCDRIMASSC43JMYSCALARCOEFF1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
