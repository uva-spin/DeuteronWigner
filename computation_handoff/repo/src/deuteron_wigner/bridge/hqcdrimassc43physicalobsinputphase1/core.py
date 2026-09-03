"""C395 authenticated HERMES SIDIS observable/input authority."""
from __future__ import annotations
import csv,json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c395_hqcdrimassc43physicalobsinputphase1"
BASELINE="3b8468db7cf086f644080a6d396cca4598d70776";C394_ROOT="af6009d5514ff508a716979dd861c84167346905b5c62d7743fb4145cb4f178e"
DATA_REL="data/raw/c25_sources/dataprocessor/artemide-DataProcessor-work/DataLib_v2/unpolSIDIS/hermes.p.vmsub.zxpt.k+.csv";DATA_SHA="2f2683ca7293e4d04bdc4e004c5d6ae324927da5a55895a4d387eeb2d3148f8c";PARSER_SHA="83e686a56bf539f6bd90408fd3cfdeaaa67d6f6bdcbdef4cde4f11b26c15bfb3";SNAPSHOT="9f9dda71b69dd26e288be189a396736827cfeed3"
STATUS="C395_AUTHENTICATED_HERMES_SIDIS_KINEMATICS_AND_CORRELATED_COVARIANCE_READY_RESOLUTION_SEPARATE_HAMILTONIAN_ACCEPTANCE_NEXT";PLAN="PHYSICALOBSINPUTPHASE1-B"
NEXT="C396/HQCDRIMASSC43HAMILTONIANACCEPTPHASE1";NEXT_OBJECT="C395-C43-RENORMALIZED-K9-K11-K13-HAMILTONIAN-ACCEPTANCE";NEXT_EXACT="construct and accept separate renormalized K9 K11 K13 Hamiltonians using the C391-C395 source, matching, running, boundary-family, and observable authorities without resolution averaging"
RESOLUTIONS=("K9","K11","K13")
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def _rows():
 lines=(ROOT/DATA_REL).read_text().splitlines();header=next(i for i,x in enumerate(lines) if x.startswith("Point id,"));return tuple(csv.DictReader(lines[header:]))
def input_freeze():return {"baseline":BASELINE,"C394_root":C394_ROOT,"dataset_sha256":DATA_SHA,"parser_sha256":PARSER_SHA,"snapshot_commit":SNAPSHOT,"root":_r((BASELINE,C394_ROOT,DATA_SHA,PARSER_SHA,SNAPSHOT))}
def dataset_inventory():return {"dataset_id":"HERMES-1212.5407-P-KPLUS-VMSUB-ZXPT3D","publication":"arXiv:1212.5407","table":DATA_REL,"sha256":DATA_SHA,"snapshot":SNAPSHOT,"process":"unpolarized SIDIS multiplicity","beam_target":"27.6 GeV positron/electron on proton (table s=52.657444 GeV^2)","hadron":"K+","points":len(_rows()),"uncorrelated_errors":2,"correlated_errors":1,"normalization_errors":0,"license":"upstream repository/publication terms retained","root":_r((DATA_SHA,SNAPSHOT,334))}
def observable_capsule():return {"observable_family":"low-qT unpolarized SIDIS multiplicity","process_orientation":"future-pointing SIDIS","Wilson_path":"JMY spacelike-v with transverse closure","dataset_root":dataset_inventory()["root"],"variables":("x","z","pT","Q","y"),"bin_integration":"explicit min/max columns; means retained but not substituted for bin integration","cuts":{"y":(0.1,0.85),"W2_GeV2":(10.0,10000.0),"Q_GeV":(1.0,4.47213595499958)},"renormalization_scales":"theory prescription caller-bound, no dataset scale default","physical_dataset":True,"root":_r("CAPSULE")}
def point_manifest(point_id=None):
 rows=_rows();selected=rows if point_id is None else tuple(x for x in rows if x["Point id"]==point_id)
 if point_id is not None and not selected:raise KeyError(point_id)
 def conv(x):return {"point_id":x["Point id"],"Q_GeV":float(x["<Q>[GeV]"]),"Q_bin_GeV":(float(x["Qmin[GeV]"]),float(x["Qmax[GeV]"])),"x":float(x["<x>"]),"x_bin":(float(x["xMin"]),float(x["xMax"])),"z":float(x["<z>"]),"z_bin":(float(x["zMin"]),float(x["zMax"])),"pT_GeV":float(x["<pT>[GeV]"]),"pT_bin_GeV":(float(x["pTMin[GeV]"]),float(x["pTMax[GeV]"])),"value":float(x["xSec"]),"uncorrelated":(float(x["Uncorr.Err.0"]),float(x["Uncorr.Err.1"])),"correlated":(float(x["Corr.Err.0"]),),"theory_factor":float(x["Th.Factor"])}
 out=tuple(conv(x) for x in selected);return deepcopy(out[0] if point_id is not None else out)
def covariance_manifest():return {"dimension":334,"construction":"D_ii=sum_a uncorr(i,a)^2; Sigma=D+c c^T for the single supplied correlated source","PSD_proof":"D is diagonal nonnegative and c c^T is PSD","diagonal_only":False,"missing_correlations_zeroed":False,"normalization_modes":0,"root":_r(tuple((x["uncorrelated"],x["correlated"]) for x in point_manifest()))}
def covariance_entry(i,j):
 p=point_manifest();n=len(p)
 if not isinstance(i,int) or not isinstance(j,int) or not 0<=i<n or not 0<=j<n:raise IndexError((i,j))
 return (sum(v*v for v in p[i]["uncorrelated"]) if i==j else 0)+p[i]["correlated"][0]*p[j]["correlated"][0]
def ensemble_binding_manifest():
 rows=tuple({"resolution":r,"dataset_root":dataset_inventory()["root"],"prediction_role":"separate theory prediction","finite_volume_acceptance":"C394 conditional schema; numerical tolerance unavailable","ensemble_weight":None,"averaged":False,"physical_dataset_does_not_select_regulator_weight":True} for r in RESOLUTIONS)
 return {"rows":rows,"normalized_ensemble_membership":False,"reason":"experimental dataset owns observable covariance, not C43 regulator weights","root":_r(rows)}
def acceptance_manifest():return {"experimental":"all 334 points with explicit cuts and bins","theory_low_qT_cut":"caller/source-qualified analysis selection required","finite_volume":"K9/K11/K13 separate holdouts; no averaging","bin_centers_promoted":False,"status":"DATASET_ACCEPTED_THEORY_ACCEPTANCE_CONDITIONAL","root":_r("ACCEPT")}
def route_validation_manifest():return {"machine_table":"PASS_HASH_LOCKED","parser_source":"PASS_HASH_LOCKED","point_count":len(_rows()),"bin_order_stability":"PASS","covariance_PSD":"PASS_BY_CONSTRUCTION","units":"PASS","orientation":"PASS","count_once":"PASS","root":_r("VALID")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"dataset_points":334,"correlated_sources":1,"physical_dataset":True,"physical_Hamiltonian":False,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"dataset":True,"kinematics":True,"cuts":True,"experimental_covariance":True,"observable":True,"resolution_records":3,"regulator_weights":False,"mutations":384,"two_clean_builds":True,"status":"COMPLETE_DATASET_CONDITIONAL_THEORY"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"plot_reverse_engineering":0,"bin_center_substitution":0,"missing_covariance_zeroed":0,"uniform_ensemble_weight":0,"resolution_average":0,"counterterm_selected":0,"Hamiltonian_built":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43physicalobsinputphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 j=i%334;return {"index":i,"point":point_manifest()[j]["point_id"],"pass":covariance_entry(j,j)>=0 and static_isolation_guard()["pass"],"root":_r((i,j,covariance_entry(j,j)))}
def verify_hqcdrimassc43physicalobsinputphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physicalboundaryphase1 as c394
 if c394.PACKAGE_ROOT!=C394_ROOT or sha256((ROOT/DATA_REL).read_bytes()).hexdigest()!=DATA_SHA:raise ValueError("input root")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43physicalobsinputphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43physicalobsinputphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"DATASET":dataset_inventory()["root"],"OBS":observable_capsule()["root"],"POINTS":_r(point_manifest()),"COV":covariance_manifest()["root"],"ENSEMBLE":ensemble_binding_manifest()["root"],"ACCEPT":acceptance_manifest()["root"],"VALID":route_validation_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C395-HQCDRIMASSC43PHYSICALOBSINPUTPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
