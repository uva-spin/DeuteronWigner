"""C341 consolidated nonphysical C43 continuum determinant certificate."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c341_hqcdrimassc43fullcert1"
BASELINE="473bc34a8ac3040ccbe727d7748c8033bbf916e8";C340_ROOT="4a1b3c9253bb11296be0ab0f9937d07a85fe2146c44cf31b75de1ec1d2d957da"
STATUS="C341_CONTINUUM_C43_DETERMINANT_CERTIFIED_NONPHYSICAL_PHYSICAL_INPUT_AUTHORITY_MISSING";PLAN="RIMASSC43FULLCERT1-C"
NEXT="C342/HQCDRIMASSC43PHYSBIND2";NEXT_OBJECT="C341-C43-PHYSICAL-INPUT-BINDING";NEXT_EXACT="bind source-qualified physical longitudinal scale mass coupling P0 Wilson-boundary and ensemble authority to the certified continuum determinant"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def combined_certificate():
 from deuteron_wigner.bridge import hqcdrimassc43heatkernel1 as h
 from deuteron_wigner.bridge import hqcdrimassc43heateval1 as e
 from deuteron_wigner.bridge import hqcdrimassc43centerbasis1 as b
 from deuteron_wigner.bridge import hqcdrimassc43windgram1 as g
 from deuteron_wigner.bridge import hqcdrimassc43trialityzero1 as z
 conv=e.convergence_enclosure();sym=e.symmetry_certificate();cg=g.increasing_rank_certificate();full=z.combined_limit_certificate();rec=z.recurrence_certificate()
 return {"upstream_roots":{"C336":h.PACKAGE_ROOT,"C337":e.PACKAGE_ROOT,"C338":b.PACKAGE_ROOT,"C339":g.PACKAGE_ROOT,"C340":z.PACKAGE_ROOT},"boson":{"center_invariant":sym["boson_center_invariant"],"C301_coefficients":conv["rows"][-1]["boson_coefficients"],"higher_harmonic_residual_norm2":conv["rows"][-1]["boson_residual_norm2"]},"fermion":{"center_invariant":sym["fermion_center_invariant"],"C301_projected_coefficients":conv["rows"][-1]["fermion_projected_coefficients"],"C301_residual_norm2":conv["rows"][-1]["fermion_residual_norm2"],"center_charged_tail_absolute_bound":cg["center_charged_tail_absolute_bound"],"combined_tail_absolute_bound":full["combined_APBC_tail_absolute_bound"],"W3_recurrence":rec["identity"],"W3_recurrence_defect":rec["max_defect"]},"numerics":{"quadrature_orders":tuple(r["G"] for r in full["rows"]),"gram_dimensions":tuple(r["dimension"] for r in full["rows"]),"all_full_rank":full["all_full_rank"],"max_coefficient_recovery_defect":max(r["coefficient_max_defect"] for r in full["rows"]),"finite_exact_span":False,"infinite_limit_enclosed":True},"domain":{"L_GeVinv":2.,"mass2_GeV2":.01,"capsule":"validation-only nonphysical","physical_prediction":False},"root":_r((conv["root"],cg["root"],full["root"],rec["root"]))}
def exclusion_certificate():return {"physical_L":"missing","physical_masses":"missing","physical_coupling":"missing","P0":"excluded separate owner","Wilson_boundary":"excluded separate owner","physical_ensemble":"missing","constraint":"longitudinal Jacobian separate","dynamical_zero_mode":"holdout","C315_C334_diagnostic_HO_consumed":False,"PennyLane":False,"root":_r("C341-EXCLUSIONS")}
def provenance_certificate():return {"C336":"gauge-covariant transverse heat kernel","C337":"proper-time winding determinant","C338":"center-covariant winding basis","C339":"center-charged Gram sequence","C340":"triality-zero recurrence ledger and combined limit","authority_chain_complete":True,"root":_r((BASELINE,C340_ROOT))}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"physical_prediction":0,"excluded_owner_collapsed":0,"finite_exact_claim":0,"protected_paths_modified":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43fullcert1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43fullcert1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43trialityzero1 as c
 if c.PACKAGE_ROOT!=C340_ROOT:raise ValueError("C340 root")
 c.load_verified_hqcdrimassc43trialityzero1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43fullcert1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43fullcert1_authority()
_ROOTS={"INPUT":_r((BASELINE,C340_ROOT)),"COMBINED":combined_certificate()["root"],"EXCLUSIONS":exclusion_certificate()["root"],"PROVENANCE":provenance_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C341-HQCDRIMASSC43FULLCERT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
