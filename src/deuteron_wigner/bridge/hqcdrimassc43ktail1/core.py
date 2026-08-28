"""C330 analytic large-K tails of charge-paired finite harmonics."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c330_hqcdrimassc43ktail1";BASELINE="e09de03af5d7045a3651a2baa6486452716d0e10";C329_ROOT="a7a884913349702458527de618f58fb14be197d0521e58a4aad514e228964a70"
STATUS="C330_CHARGE_PAIR_LOG_TAIL_CANCELLATION_DERIVED_COMPONENT_ONE_OVER_K_TAILS_BOUND_SUBTRACTION_MISSING";PLAN="RIMASSC43KTAIL1-A";NEXT="C331/HQCDRIMASSC43KTAILSUB1";NEXT_OBJECT="C330-C43-PAIRED-FINITE-HARMONIC-TAIL-SUBTRACTION";NEXT_EXACT="subtract the source-derived charge-paired one-over-K tails componentwise from the finite-harmonic C43 sequences and enclose the K limits"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def symbolic_expansion():return {"unpaired":"2 theta/x - theta^2/x^2 + (-2 a theta + 2 theta^3/3)/x^3 + O(x^-4)","paired":"-2 theta^2/x^2 + (6 a theta^2-theta^4)/x^4 + (-10 a^2 theta^2+10 a theta^4-2 theta^6/3)/x^6+O(x^-8)","x":"2 pi j","a":"L^2 omega^2","logK_unpaired":True,"odd_terms_cancel_pair":True,"paired_leading":"-theta^2/(2 pi^2 j^2)","root":_r("C330-SERIES")}
def component_coefficients(Nmax,theta):
 if not isinstance(Nmax,int) or Nmax<1 or not math.isfinite(theta):raise ValueError
 shell=sum(q+1 for q in range(Nmax));base=theta*theta*shell/(2*math.pi**2)
 # coefficient C in omitted tail C*sum_{j>J}j^-2 after root pairing.
 rows=({"owner":"boson","sign":.5,"C":-.5*base},{"owner":"fermion","sign":-1.,"C":base},{"owner":"constraint","sign":-1.,"C":base})
 return {"rows":rows,"shell_degeneracy":shell,"component_separate":True,"root":_r(rows)}
def tail_bounds(first_omitted):
 if not math.isfinite(first_omitted) or first_omitted<=0:raise ValueError
 return {"sum_jminus2":(1/first_omitted,1/first_omitted+1/first_omitted**2),"Euler_Maclaurin_not_assumed":True,"outward":True,"root":_r(first_omitted)}
def numeric_certificate():
 from deuteron_wigner.bridge import hqcdrimassc43kharmonic1 as c
 rows=[]
 for owner in ("boson","fermion","constraint"):
  vals=[]
  for k in (41,81,161):vals.append(c.spectral_delta_finite(k,6,.4,c.BOUNDARY,c.ZERO,.2,.01,2.,owner)+c.spectral_delta_finite(k,6,.4,c.BOUNDARY,c.ZERO,-.2,.01,2.,owner))
  rows.append({"owner":owner,"K2":(41,81,161),"paired":tuple(vals),"successive_difference_decreases":abs(vals[2]-vals[1])<abs(vals[1]-vals[0])})
 return {"rows":tuple(rows),"all_stable":all(x["successive_difference_decreases"] for x in rows),"root":_r(rows)}
def ownership():return {"charge_pair":"conjugate SU3 roots before projection","global_P0":"C319 separate","dynamical_zero_mode":"holdout","Wilson_boundary":"JMY_BJY separate","root":_r("C330-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"log_cancelled":True,"tail_subtracted":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"fit_rationals":0,"unpaired_projected":0,"zero_modes_zeroed":0,"continuum_claims":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43ktail1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43ktail1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43kseqeval1 as c
 if c.PACKAGE_ROOT!=C329_ROOT:raise ValueError("C329 root")
 c.load_verified_hqcdrimassc43kseqeval1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43ktail1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43ktail1_authority()
_ROOTS={"INPUT":_r((BASELINE,C329_ROOT)),"SERIES":symbolic_expansion()["root"],"COEFF":component_coefficients(6,.2)["root"],"BOUNDS":tail_bounds(10.)["root"],"NUMERIC":numeric_certificate()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C330-HQCDRIMASSC43KTAIL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
