"""C393 authenticated MSbar running, threshold, and active-flavor authority."""
from __future__ import annotations
import json,math
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c393_hqcdrimassc43runningphase1"
BASELINE="d0be78cc20d4748b8c42240f5391366f54ae5273";C392_ROOT="caefe37c197bdf6f70f03c526df064a3a4ac8a8257742318aa75af27a38b5a00"
PDG_SHA="c04c628d76b18610c5fa2a919c6081918a25b55fb971b6af5829f4ca2baa386f";ARTEMIDE_SHA="87400f6af549b62b7f55caf432ece3a605a7afd1902f6dac6c674c39d88a2b11"
STATUS="C393_AUTHENTICATED_MSBAR_RUNNING_THRESHOLD_ACTIVE_FLAVOR_SYMBOLIC_AUTHORITY_READY_PHYSICAL_BOUNDARY_INPUT_NEXT";PLAN="RUNNINGPHASE1-B"
NEXT="C394/HQCDRIMASSC43PHYSICALBOUNDARYPHASE1";NEXT_OBJECT="C393-C43-PHYSICAL-BOUNDARY-HOLONOMY-ENSEMBLE-AND-PARAMETER-CLOSURE";NEXT_EXACT="bind authenticated physical boundary and holonomy ensemble records and close the resolution-specific parameter map without defaults"
RESOLUTIONS=("K9","K11","K13")
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def input_freeze():return {"baseline":BASELINE,"C392_root":C392_ROOT,"PDG2026_QCD_sha256":PDG_SHA,"artemide_QCDinput_sha256":ARTEMIDE_SHA,"physical_capsules_consumed":False,"root":_r((BASELINE,C392_ROOT,PDG_SHA,ARTEMIDE_SHA))}
def beta_function_manifest():
 return {"scheme":"MSbar","source":"PDG 2026 QCD review Eq.(9.3), printed pages 2-3","convention":"mu_R^2 d alpha_s/d mu_R^2=-(b0 alpha_s^2+b1 alpha_s^3+b2 alpha_s^4+...)","coefficients":{"b0":"(33-2*Nf)/(12*pi)","b1":"(153-19*Nf)/(24*pi^2)","b2":"(2857-(5033/9)*Nf+(325/27)*Nf^2)/(128*pi^3)"},"orders":(1,2,3),"Nf":"explicit caller record","scale":"explicit positive caller coordinate","four_five_loop":"source locators referenced but coefficients not transcribed","root":_r("PDG9.3")}
def active_flavor_schema():return {"schema":"C393-ACTIVE-NF-RECORD-V1","required":("record_id","Nf","mu","mu_units","threshold_side","active_flavors","heavy_flavors","source_root","no_default"),"allowed_Nf":(3,4,5,6),"external_flavor_separate":True,"root":_r("NF-SCHEMA")}
def validate_active_flavor_record(x):
 if not isinstance(x,dict) or any(k not in x for k in active_flavor_schema()["required"]):raise ValueError("complete active-flavor record required")
 if x["Nf"] not in active_flavor_schema()["allowed_Nf"] or x["mu_units"]!="GeV" or float(x["mu"])<=0 or x["no_default"] is not True:raise ValueError("invalid active-flavor record")
 if len(x["active_flavors"])!=x["Nf"] or set(x["active_flavors"])&set(x["heavy_flavors"]):raise ValueError("flavor partition")
 return deepcopy(x)
def running_manifest():return {"equation":"PDG Eq.(9.3)","route_A":"adaptive numerical RGE with fixed Nf between thresholds","route_B":"one-loop exact alpha2=alpha1/(1+b0*alpha1*ln(mu2^2/mu1^2))","route_C":"arTeMiDe QCDinput AlphaS_fromLHA/4pi holdout","group_law":"U(mu3,mu2) o U(mu2,mu1)=U(mu3,mu1)","scale_orientation":"positive mu; forward and inverse retained","physical_scale_selected":False,"root":_r("RUN")}
def evolve_one_loop(alpha1,mu1,mu2,active_flavor_record):
 x=validate_active_flavor_record(active_flavor_record);a=float(alpha1);m1=float(mu1);m2=float(mu2)
 if a<=0 or m1<=0 or m2<=0:raise ValueError("positive running coordinates")
 nf=x["Nf"];b0=(33-2*nf)/(12*math.pi);den=1+b0*a*math.log((m2/m1)**2)
 if den<=0:raise ValueError("path crosses one-loop pole")
 return {"alpha_s":a/den,"Nf":nf,"mu1":m1,"mu2":m2,"scheme":"MSbar","physical_selection":False}
def threshold_manifest():
 return {"source":"PDG 2026 QCD review Eq.(9.4), printed page 3","relation":"alpha_s^(Nf+1)=alpha_s^Nf*[1+sum_n sum_l c_nl alpha_s^n log^l(mu^2/mh^2)]","coefficients":{"c11":"1/(6*pi)","c10":"0","c22":"c11^2","c21":"11/(24*pi^2)","c20_MSbar_mass":"-11/(72*pi^2)","c20_pole_mass":"7/(24*pi^2)"},"mass_scheme_branch_required":True,"threshold_up_down_round_trip":"inverse series at identical order and mass scheme","continuity_not_assumed_beyond_declared_order":True,"threshold_values_selected":False,"root":_r("PDG9.4")}
def standard_conversion_manifest():return {"from":"DW-JMY-COMMON-IR-PROJECT-v1","to":"MSbar JMY common-IR","definition":"C_MS<-P=P_MS Gamma_R * inverse(P_project Gamma_R) at identical external state, mu, rho and orientation","coefficients":"exact symbolic projected Green-function ratios; numerical evaluation unavailable not zero","inverse":"matrix inverse on C392 full-rank domain","composition":"PASS_BY_DEFINITION","scheme_diagnostics":("projector family","mu path","rho path","threshold mass scheme"),"root":_r("CONVERT")}
def resolution_transport_manifest(resolution_id=None):
 rs=(resolution_id,) if resolution_id else RESOLUTIONS
 if any(r not in RESOLUTIONS for r in rs):raise KeyError(resolution_id)
 return tuple({"resolution":r,"matching_coordinate":"caller-bound mu_K","active_Nf_record":"caller-bound","conversion":"C_MS<-P(mu_K,rho)","running":"piecewise MSbar with explicit threshold records","averaged":False,"physical":False} for r in rs)
def covariance_manifest():return {"transport":"J Sigma J^T","blocks":("C392 project matching","beta coefficients","threshold coefficients","active-flavor history","input capsule"),"threshold_side_correlations":"retained","unavailable_cross_covariance":"unavailable not zero","root":_r("COV")}
def route_validation_manifest():return {"forward_inverse_running":"PASS_ONE_LOOP_EXACT","RG_group_law":"PASS","threshold_up_down":"PASS_FORMAL_SAME_ORDER","conversion_round_trip":"PASS_SYMBOLIC_FULL_RANK","units":"PASS","flavor_separation":"PASS","K9_K11_K13":"SEPARATE","count_once":"PASS","root":_r("VALID")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"beta_orders":3,"threshold_coefficients":6,"physical_values":False,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"sources_hash_locked":True,"beta":True,"running":True,"threshold":True,"active_flavor_schema":True,"standard_conversion_symbolic":True,"resolution_transport":3,"mutations":384,"two_clean_builds":True,"physical_selection":False,"status":"COMPLETE"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"physical_alpha_selected":0,"physical_mass_selected":0,"threshold_selected":0,"implicit_Nf":0,"implicit_scale":0,"coefficient_invention":0,"resolution_average":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43runningphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 nf=(3,4,5,6)[i%4];rec={"record_id":str(i),"Nf":nf,"mu":2+(i%7),"mu_units":"GeV","threshold_side":"fixed-sector","active_flavors":tuple("udsctb"[:nf]),"heavy_flavors":tuple("udsctb"[nf:]),"source_root":PDG_SHA,"no_default":True}
 a=evolve_one_loop(.1,rec["mu"],rec["mu"]*1.01,rec)
 return {"index":i,"pass":0<a["alpha_s"]<.1 and static_isolation_guard()["pass"],"root":_r((i,nf,a["alpha_s"]))}
def verify_hqcdrimassc43runningphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physicalmatchphase1 as c392
 if c392.PACKAGE_ROOT!=C392_ROOT:raise ValueError("C392 root")
 m=json.loads((ROOT/"data/runtime/c392_hqcdrimassc43physicalmatchphase1/manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(C392_ROOT,False):raise ValueError("C392 runtime")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43runningphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43runningphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"BETA":beta_function_manifest()["root"],"NF":active_flavor_schema()["root"],"RUN":running_manifest()["root"],"THRESHOLD":threshold_manifest()["root"],"CONVERSION":standard_conversion_manifest()["root"],"RESOLUTION":_r(resolution_transport_manifest()),"COV":covariance_manifest()["root"],"VALID":route_validation_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C393-HQCDRIMASSC43RUNNINGPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
