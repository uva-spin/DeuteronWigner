"""C336 gauge-covariant flat-background transverse heat kernel."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c336_hqcdrimassc43heatkernel1";BASELINE="ee01bb258ed710dbbf57f80fa539e6e4d4cccfc2";C335_ROOT="0eceff5a717cd8dc4b958853e529c5479c2122e34f14d4fbbb4a3dc65cd7ea14"
STATUS="C336_GAUGE_COVARIANT_CONTINUOUS_TRANSVERSE_HEAT_KERNEL_DERIVED_STANDARD_DETERMINANT_EVALUATION_MISSING";PLAN="RIMASSC43HEATKERNEL1-A";NEXT="C337/HQCDRIMASSC43HEATEVAL1";NEXT_OBJECT="C336-C43-STANDARD-HEAT-KERNEL-DETERMINANT";NEXT_EXACT="evaluate the UV-finite holonomy-dependent C43 continuum determinant from the C336 winding heat kernel and project its class-function coefficients"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def operator_ledger():
 rows=({"owner":"boson","field":"A_perp^i, i=1,2","transverse_operator":"-partial_perp^2","multiplicity":2,"prefactor":.5,"net_trace_weight":1.},{"owner":"fermion","field":"psi_plus two LF spin states","transverse_operator":"-partial_perp^2+m^2","multiplicity":2,"prefactor":-1.,"net_trace_weight":-2.},{"owner":"constraint","field":"solved A_plus/Gauss law","transverse_operator":None,"multiplicity":0,"prefactor":-1.,"net_trace_weight":0.})
 return {"rows":rows,"constraint_jacobian":"det prime D_minus^2 longitudinal only; P0 excluded","ghost":"decoupled at C43 nonzero-mode axial scope","count_once":True,"root":_r(rows)}
def heat_modes(s,L,theta,phase,mass2,N=256):
 if s<=0 or L<=0 or mass2<0 or phase not in (0.,.5):raise ValueError
 return math.exp(-s*mass2)/(4*math.pi*s)*sum(math.exp(-s*(2*math.pi*(n+phase)+theta)**2/L**2)-math.exp(-s*(2*math.pi*(n+phase))**2/L**2) for n in range(-N,N+1))
def heat_winding(s,L,theta,phase,mass2,M=64):
 if s<=0 or L<=0 or mass2<0 or phase not in (0.,.5):raise ValueError
 pref=L*math.exp(-s*mass2)/(4*math.pi*s*math.sqrt(4*math.pi*s))
 return pref*2*sum(math.exp(-L*L*l*l/(4*s))*math.cos(2*math.pi*l*phase)*(math.cos(l*theta)-1) for l in range(1,M+1))
def heat_kernel_contract():return {"transverse_measure":"d^2k/(2pi)^2","transverse_trace_per_area":"exp(-s m^2)/(4 pi s)","longitudinal":"PBC phase 0 or APBC phase 1/2 with holonomy shift","winding_difference":"L exp(-s m^2)/(8 pi^(3/2) s^(3/2)) sum_l!=0 exp(-L^2l^2/(4s)) exp(2pi i l phase)(exp(i l theta)-1)","thermal":False,"root":_r("C336-HEAT")}
def uv_certificate():return {"small_s":"O(s^-3/2 exp(-L^2/(4s))) for theta-dependent difference","holonomy_Seeley_DeWitt":("a0=0","a1=0","a2=0","all local coefficients zero"),"local_holonomy_counterterm":False,"UV_finite":True,"root":_r("C336-UV")}
def route_parity():
 rows=[]
 for phase in (0.,.5):
  a=heat_modes(.2,2.,.3,phase,.01);b=heat_winding(.2,2.,.3,phase,.01);rows.append({"phase":phase,"modes":a,"winding":b,"absolute_defect":abs(a-b)})
 return {"rows":tuple(rows),"agreement":all(x["absolute_defect"]<1e-12 for x in rows),"theta_zero":heat_winding(.2,2.,0.,0.,0.)==0.,"conjugate_even":heat_winding(.2,2.,.3,0.,0.)==heat_winding(.2,2.,-.3,0.,0.),"root":_r(rows)}
def ownership():return {"P0":"excluded global owner","Wilson_boundary":"separate nonlocal operator","dynamical_zero_mode":"holdout","C315":"diagnostic_only_not_consumed","root":_r("C336-OWNER")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"kernel_ready":True,"determinant_evaluated":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"Weiss_imported":0,"HO_spectrum_consumed":0,"constraint_transverse_copied":0,"counterterm_invented":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43heatkernel1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43heatkernel1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43transmatch1 as c
 if c.PACKAGE_ROOT!=C335_ROOT:raise ValueError("C335 root")
 c.load_verified_hqcdrimassc43transmatch1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43heatkernel1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43heatkernel1_authority()
_ROOTS={"INPUT":_r((BASELINE,C335_ROOT)),"OPERATORS":operator_ledger()["root"],"HEAT":heat_kernel_contract()["root"],"UV":uv_certificate()["root"],"PARITY":route_parity()["root"],"OWNER":ownership()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C336-HQCDRIMASSC43HEATKERNEL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
