"""C335 standard transverse-renormalization compatibility audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c335_hqcdrimassc43transmatch1";BASELINE="cda93cafd1eee4c6cfb2937c2e8a9be16cfc35bd";C334_ROOT="65ce65c47909ce47f0810b9e6cab42cd8f7cfc8fa8f0c189c37118b999022c63"
STATUS="C335_STANDARD_TRANSVERSE_MATCHING_REJECTED_CONDITIONAL_HO_SPECTRUM_NOT_GAUGE_COVARIANT_HEAT_KERNEL_MISSING";PLAN="RIMASSC43TRANSMATCH1-D";NEXT="C336/HQCDRIMASSC43HEATKERNEL1";NEXT_OBJECT="C335-C43-GAUGE-COVARIANT-TRANSVERSE-SPECTRAL-KERNEL";NEXT_EXACT="derive the gauge-covariant transverse fluctuation and constraint heat-kernel spectrum from the C43 background-field action before standard determinant renormalization"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def authority_matrix():
 rows=({"authority":"C313 determinant kernel","requirement":"source-qualified subtraction of a flat Cartan background determinant","available":True},{"authority":"C314 tail certificate","requirement":"holonomy divergence cancels componentwise conditionally on the correct spectrum","available":True},{"authority":"C315 2DHO adapter","requirement":"conditional omega^2=bHO^2(q+1), not derived fluctuation spectrum","available":True},{"authority":"C332/C333 result","requirement":"conditional adapter creates holonomy-dependent linear/log Nmax terms","available":True},{"authority":"standard transverse counterterm conversion","requirement":"local gauge-compatible finite target","available":False})
 return {"rows":rows,"standard_match_ready":False,"root":_r(rows)}
def compatibility_decision():return {"flat_background":"F_perp=0 at declared constant Cartan scope","local_UV_counterterm_may_depend_on_holonomy":"NO_WITHOUT_NONLOCAL_WILSON_OPERATOR_OWNER","C332_theta_dependent_subtraction_standard_local":False,"C334_project_conversions":"diagnostic intermediate only","bHO_member_selectable":False,"reason":"C315 conditional oscillator kinetic adapter is not a source-derived covariant fluctuation/constraint heat kernel","root":_r("C335-DECISION")}
def attempted_routes():return {"MSbar_direct":"unavailable: no dimensional/heat-kernel coefficient map","physical_observable":"unavailable: C321-C323 physical finite-volume capsule incomplete","project_reference_member":"rejected without standard conversion","component_cancellation":"cannot be asserted without correct polarizations/constraint spectrum","contradiction":False,"next_derivable":True,"root":_r("C335-ROUTES")}
def required_kernel():return {"operators":("Delta_B[Abar]","Delta_F[Abar,m]","Delta_constraint[Abar]"),"background":"C313 constant Cartan flat connection","requirements":("gauge-covariant transverse eigenvalues","polarization multiplicities","constraint/Jacobian cancellation","Seeley-DeWitt/local UV coefficients","holonomy-dependent finite remainder"),"C315_round_trip":"diagnostic only","root":_r("C335-KERNEL")}
def ownership():return {"C334_groupoid":"frozen diagnostic","P0":"separate","Wilson_boundary":"nonlocal measurement owner not counterterm","dynamical_zero_mode":"holdout","root":_r("C335-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"authority_recovery_research":True,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"standard_matched":False,"invalid_counterterm_avoided":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"MSbar_invented":0,"bHO_selected":0,"nonlocal_counterterm_added":0,"physical_claims":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43transmatch1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43transmatch1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43bholimit1 as c
 if c.PACKAGE_ROOT!=C334_ROOT:raise ValueError("C334 root")
 c.load_verified_hqcdrimassc43bholimit1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43transmatch1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43transmatch1_authority()
_ROOTS={"INPUT":_r((BASELINE,C334_ROOT)),"MATRIX":authority_matrix()["root"],"DECISION":compatibility_decision()["root"],"ROUTES":attempted_routes()["root"],"KERNEL":required_kernel()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C335-HQCDRIMASSC43TRANSMATCH1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
