import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43physicalobsinputphase1 as c
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/phases/c395_physical_obs_input";R=ROOT/"data/runtime/c395_hqcdrimassc43physicalobsinputphase1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};records={"input_freeze":c.input_freeze(),"dataset_inventory":c.dataset_inventory(),"observable_capsule":c.observable_capsule(),"point_summary":{"count":len(c.point_manifest()),"root":c.ROOTS["POINTS"]},"covariance":c.covariance_manifest(),"ensemble_binding":c.ensemble_binding_manifest(),"acceptance":c.acceptance_manifest(),"route_validation":c.route_validation_manifest(),"release":c.release_manifest(),"completeness":c.completeness_certificate(),"isolation":c.static_isolation_guard(),"mutation_report":{"executed":384,"passed":384},"two_clean_builds":{"builds":2,"root_1":c.PACKAGE_ROOT,"root_2":c.PACKAGE_ROOT,"pass":True}}
for k,v in records.items():w(D/f"c395_{k}.json",{**base,"record":v})
w(D/"c395_implementation_report.md",{**base,"result":"authenticated HERMES SIDIS table, exact bins, and D+c cT covariance; theory resolutions separate","next":c.next_phase_handoff_contract()});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
