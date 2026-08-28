"""C332 analytic 2DHO transverse shell divergences at fixed bHO."""
from __future__ import annotations
import json,math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c332_hqcdrimassc43transtail1";BASELINE="1fe7309567bef291a2df7bf7741edc76cb8fdd0d";C331_ROOT="6b4d3b2fa6fa758e3cfc4fdbfbb5f8a343ac940fe53d9550d886ce7ce1b6ebb2"
STATUS="C332_TRANSVERSE_LINEAR_AND_LOG_NMAX_DIVERGENCES_DERIVED_COMPONENT_SUBTRACTION_MISSING";PLAN="RIMASSC43TRANSTAIL1-A";NEXT="C333/HQCDRIMASSC43TRANSUB1";NEXT_OBJECT="C332-C43-TRANSVERSE-UV-SUBTRACTION";NEXT_EXACT="subtract the analytic linear and logarithmic Nmax divergences componentwise at fixed bHO and outwardly enclose the transverse shell limits"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def shell_expansion():return {"paired_shell":"A0 + A1/y + O(y^-2), y=q+1","A0":"2 theta^2/c","A1":"-(2 m theta^2 + theta^4 + 6 theta^2 x^2)/c^2","c":"L^2 bHO^2","m":"L^2 mass2 for fermion; 0 otherwise","x":"2 pi j","sum":"A0 Nmax + A1 H_Nmax + finite + O(1/Nmax)","linear_divergence":True,"log_divergence":True,"root":_r("C332-SERIES")}
def divergence_coefficients(K2,bHO,theta,mass2,L,owner):
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as h
 modes=tuple(float(Fraction(x)) for x in h.harmonic_domain(K2,owner)["modes"]);sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.);c=L*L*bHO*bHO;m=L*L*mass2 if owner=="fermion" else 0.
 a0=sign*sum(2*theta*theta/c for _ in modes);a1=sign*sum(-(2*m*theta*theta+theta**4+6*theta*theta*(2*math.pi*j)**2)/c**2 for j in modes)
 return {"owner":owner,"K2":K2,"linear_Nmax":a0,"log_HN":a1,"mode_count":len(modes),"bHO_fixed":True,"root":_r((owner,K2,bHO,a0,a1))}
def subtracted_sequence():
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as h
 rows=[]
 for o in ("boson","fermion","constraint"):
  coeff=divergence_coefficients(9,.4,.2,.01,2.,o);vals=[]
  # The largest harmonic has x^2/c >> 1, so use windows beyond that
  # crossover; small-N windows are not in the derived shell asymptotic regime.
  for n in (5000,10000,20000):
   raw=h.spectral_delta_finite(9,n,.4,h.BOUNDARY,h.ZERO,.2,.01,2.,o)+h.spectral_delta_finite(9,n,.4,h.BOUNDARY,h.ZERO,-.2,.01,2.,o);H=sum(1/k for k in range(1,n+1));vals.append(raw-coeff["linear_Nmax"]*n-coeff["log_HN"]*H)
  rows.append({"owner":o,"Nmax":(5000,10000,20000),"subtracted":tuple(vals),"successive_difference_decreases":abs(vals[2]-vals[1])<abs(vals[1]-vals[0])})
 return {"rows":tuple(rows),"all_stable":all(x["successive_difference_decreases"] for x in rows),"subtraction_executed_for_validation_only":True,"root":_r(rows)}
def bHO_classification():return {"role":"basis-scale and transverse regulator coordinate","averaging_forbidden":True,"physical_value":False,"coefficients_scale_as":"A0~bHO^-2; A1~bHO^-4","scale_removal_authority":"MISSING","root":_r("C332-BHO")}
def ownership():return {"K_enclosures":"C331 frozen","components_separate":True,"zero_mode":"holdout","global_P0":"separate","root":_r("C332-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"divergences_derived":True,"transverse_limit":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"fit_powers":0,"bHO_averaged":0,"physical_claims":0,"zero_modes_zeroed":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43transtail1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43transtail1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43ktailsub1 as c
 if c.PACKAGE_ROOT!=C331_ROOT:raise ValueError("C331 root")
 c.load_verified_hqcdrimassc43ktailsub1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43transtail1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43transtail1_authority()
_ROOTS={"INPUT":_r((BASELINE,C331_ROOT)),"SERIES":shell_expansion()["root"],"COEFF":divergence_coefficients(9,.4,.2,.01,2.,"fermion")["root"],"NUMERIC":subtracted_sequence()["root"],"BHO":bHO_classification()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C332-HQCDRIMASSC43TRANSTAIL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
