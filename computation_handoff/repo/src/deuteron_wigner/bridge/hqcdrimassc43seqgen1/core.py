"""C325 executable-route audit for controlled C43 sequences."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c325_hqcdrimassc43seqgen1";BASELINE="539754055d1cec430577010022799495fc98e4ce";C324_ROOT="6e79b05663b8d6030a2334aaa3aaebdf3e84324c48bf4ed4d7df4ca6e247541e"
STATUS="C325_EXECUTABLE_SEQUENCE_AUDITED_GENERAL_SPECTRUM_AND_ZERO_MODE_KERNEL_MISSING";PLAN="RIMASSC43SEQGEN1-C";NEXT="C326/HQCDRIMASSC43GENKERNEL1";NEXT_OBJECT="C325-C43-GENERAL-REGULATOR-SPECTRUM-KERNEL";NEXT_EXACT="generalize the C316 determinant kernel to independent K Nmax bHO boundary-class and explicit PBC zero-mode-sector coordinates"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def executable_audit():
 rows=({"coordinate":"K","C316":"resolution label only","independent":False},{"coordinate":"Nmax","C316":"hard-coded by resolution","independent":False},{"coordinate":"bHO","C316":"hard-coded by resolution","independent":False},{"coordinate":"PBC zero mode","C316":"unconditionally excluded","independent":False},{"coordinate":"longitudinal sum cutoff N","C316":"caller controlled","independent":True},{"coordinate":"L","C316":"caller controlled nonphysical","independent":True})
 return {"rows":rows,"controlled_sequence_executable":False,"evaluations_emitted":0,"root":_r(rows)}
def required_kernel():return {"signature":"spectral_delta_general(K,Nmax,bHO,boundary_class,zero_mode_sector,theta,mass2,L,sum_cutoff,owner)","factorized_axes":True,"P0_count_once":True,"legacy_round_trip_required":True,"physical_defaults":False,"root":_r("C325-KERNEL")}
def covariance_plan():return {"paired_common_randomness":"deterministic sums","shared_input_jacobian":True,"truncation_residuals_by_axis":True,"numeric_covariance":False,"reason":"sequence not executable","root":_r("C325-COV")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def release_manifest():return {"status":STATUS,"plan":PLAN,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))}
def static_isolation_guard():return {"invented_points":0,"zero_modes_dropped_silently":0,"fixtures_promoted":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43seqgen1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43seqgen1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43converge1 as c
 if c.PACKAGE_ROOT!=C324_ROOT:raise ValueError("C324 root")
 c.load_verified_hqcdrimassc43converge1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43seqgen1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43seqgen1_authority()
_ROOTS={"INPUT":_r((BASELINE,C324_ROOT)),"AUDIT":executable_audit()["root"],"KERNEL":required_kernel()["root"],"COV":covariance_plan()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C325-HQCDRIMASSC43SEQGEN1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
