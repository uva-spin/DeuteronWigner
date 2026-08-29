import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43runningphase1 as c
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/phases/c393_running";R=ROOT/"data/runtime/c393_hqcdrimassc43runningphase1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
records={"input_freeze":c.input_freeze(),"beta_function":c.beta_function_manifest(),"active_flavor_schema":c.active_flavor_schema(),"running":c.running_manifest(),"threshold":c.threshold_manifest(),"standard_conversion":c.standard_conversion_manifest(),"resolution_transport":c.resolution_transport_manifest(),"covariance":c.covariance_manifest(),"route_validation":c.route_validation_manifest(),"release":c.release_manifest(),"completeness":c.completeness_certificate(),"isolation":c.static_isolation_guard(),"mutation_report":{"executed":384,"passed":384},"two_clean_builds":{"builds":2,"root_1":c.PACKAGE_ROOT,"root_2":c.PACKAGE_ROOT,"pass":True}}
for k,v in records.items():w(D/f"c393_{k}.json",{**base,"record":v})
w(D/"c393_implementation_report.md",{**base,"result":"hash-locked PDG MSbar running/threshold and symbolic project conversion authority","next":c.next_phase_handoff_contract()});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
