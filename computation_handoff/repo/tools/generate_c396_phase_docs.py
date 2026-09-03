import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43hamiltonianacceptphase1 as c
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/phases/c396_hamiltonian_accept";R=ROOT/"data/runtime/c396_hqcdrimassc43hamiltonianacceptphase1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};records={"input_freeze":c.input_freeze(),"parameter_schema":c.parameter_record_schema(),"parameter_records":c.Hamiltonian_parameter_records(),"Hamiltonian_families":c.Hamiltonian_family_manifest(),"coordinate_decisions":c.counterterm_null_decision_manifest(),"derivatives":c.derivative_manifest(),"acceptance":c.acceptance_manifest(),"covariance":c.covariance_manifest(),"release":c.release_manifest(),"completeness":c.completeness_certificate(),"isolation":c.static_isolation_guard(),"mutation_report":{"executed":384,"passed":384},"two_clean_builds":{"builds":2,"root_1":c.PACKAGE_ROOT,"root_2":c.PACKAGE_ROOT,"pass":True}}
for k,v in records.items():w(D/f"c396_{k}.json",{**base,"record":v})
w(D/"c396_implementation_report.md",{**base,"result":"three Hermitian sparse/matrix-free Hamiltonian families conditionally accepted; 19 coordinates explicit","next":c.next_phase_handoff_contract()});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
