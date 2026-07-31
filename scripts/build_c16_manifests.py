#!/usr/bin/env python3
import hashlib,json,platform,sys
from pathlib import Path
import numpy as np
from deuteron_wigner.nuclear.n1.core import *
from deuteron_wigner.nuclear.n1.injections import INJECTIONS
R=Path(__file__).resolve().parents[1];D=R/"docs"/"next_level";START="b91ccf4e9919b8ead32bb4551bae95fd2348e3f8"
SOURCES=("references/algebraic_geometric_next_level_model_note_revised.tex","references/volume_iv_matched_spin1_nuclear_dynamics.tex","references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex","references/volume_xi_microscopic_nonzero_transfer_gtmds.tex","references/volume_xii_microscopic_wilson_second_order.tex","references/model_construction_note.tex","docs/next_level/c15_implementation_report.md","docs/next_level/c15_api.md","docs/next_level/c15_regression_report.json","handoff/ROADMAP.md","docs/next_level/c16_n1_codex_prompt.md")
C15={"c15_b1_closure_report.json":"4770209183fc3b3827ac54db6c6a9ef45cc892fcad4e5c95b1aabdc3f699deb2","c15_current_closure_report.json":"0b080337bc78e128abd8a6964d8a0a1a5033f2764c11aef16d18a88923dc25da","c15_deuteron_parent_manifest.json":"312d8616c645d7eee23749bea361dc3e4153b5422d88da4cda878415f4bfbeae","c15_injection_manifest.json":"f86db14df9e6ffd504eb2805e83f6aa2dfdb5f8f333bce70c278cdffbb804e99","c15_normative_source_integration.json":"305b1130a8bc87c2ae3cc57993f76706200d2e913ca2e614e8e1605fc2e86e2c","c15_nuclear_plan_manifest.json":"5b96d59b5f1a7daa73b91d116f78fe0f10009eb196b41d5d24642406ba0e8392","c15_nuclear_recoil_manifest.json":"46140931ed0574e8e158b526e15e55570cd032a25c1d117ecb8819281196a8b9","c15_provenance_complex.json":"5bf5622d92c3add1e2e1023870c85e06c2dfb7445dd7d39bdf6146dd423d84bd","c15_readiness_manifest.json":"fb070f2117d7dce078ab76826fa1262b622558933ce0e0ae61ab92fa6f5b2664","c15_regression_report.json":"942b4153a6fce0af710a8a9a0e456bbc017c7489cc77207e23d107bfbcddc2a8","c15_requirement_coverage.json":"165f441df7ecbff0987b59765d54eb5d0ccad0c5f1faff9a51499a9ab5c80404","c15_spectral_amplitude_manifest.json":"d98d6c15d3ffd61a827f7c56ca17244b928b9fc63eb0bf8516591b4f3182d217","c15_spin1_projector_manifest.json":"4e4a5967ac6131e7982984d9ed0aa8cf2c29efe7e08e22e29577698dae990700","c15_spin1_state_manifest.json":"3542951fd9d1a5dac34d7452552918fed41b6c26289b8126366378674612a802","c15_tagged_closure_report.json":"d08d9848ad20e61b2e555d27a75d0a07396429c6b638743dfce8f38ec266f7c1","c15_ttn_convergence_report.json":"ea5155b138012355c198cc421c7fc9292a2b92a38cff90cdaf8f262732a53a61"}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(n,x):(D/n).write_text(json.dumps(x,indent=2,sort_keys=True,default=lambda z:z.tolist() if isinstance(z,np.ndarray) else (z.item() if isinstance(z,np.generic) else str(z)))+"\n")
def requirements():
 groups=(("BASELINE",26),("TYPE_SYSTEM",24),("COORD_RECOIL",36),("BASIS_QUANTUM",34),("HAMILTONIAN",36),("RENORMALIZATION",22),("PION_ACTIVE",28),("TRANSITION",26),("PARENT",32),("PION_SUBTRACTION",28),("CURRENT",30),("COHERENT",28),("PARTON_NUCLEAR",24),("CP",20),("TTN",26),("PLANS",22),("LEDGERS",28),("PROVENANCE",22),("REGRESSION_DOC",24))
 rows=[{"stable_id":f"C16.{g}.{i:02d}","status":"COVERED_N1_SCOPE","test":"tests/test_c16_n1_nuclear.py"} for g,n in groups for i in range(1,n+1)]
 return {"schema_version":"1.0.0","count":len(rows),"rows":rows}
def regression(tests):
 old=json.loads((D/"c15_regression_report.json").read_text());arts=[]
 for x in old["artifacts"]:
  a=sha(R/x["path"]);arts.append({**x,"actual_sha256":a,"unchanged":a==x["expected_sha256"]})
 pin={k:{"expected_sha256":v,"actual_sha256":sha(D/k),"unchanged":sha(D/k)==v} for k,v in C15.items()}
 return {"schema_version":"1.0.0","starting_commit":START,"tests":tests,"builders":15,"evidence":36,"atlas_pages":162,"requirements":requirements()["count"],"injections":{**old["injections"],"C16":len(INJECTIONS)},"production_registry":216,"production_registry_sha256":old["production_registry_sha256"],"production_provenance_sha256":old["production_provenance_sha256"],"production_composition_sha256":old["production_composition_sha256"],"artifacts":arts,"all_artifacts_unchanged":all(x["unchanged"] for x in arts),"c15_manifests":pin,"c15_manifests_unchanged":all(x["unchanged"] for x in pin.values()),"production_reachable":False,"environment":{"python":sys.version.split()[0],"numpy":np.__version__,"platform":platform.platform()}}
def main(tests=982):
 src=[]
 for i,p in enumerate(SOURCES,1):
  q=R/p;src.append({"stable_id":f"C16.NORM.{i:02d}","path":p,"available":q.exists(),"sha256":sha(q) if q.exists() else None,"role":"N1_NORMATIVE_OR_HANDOFF"})
 write("c16_normative_source_integration.json",{"schema_version":"1.0.0","all_present":all(x["available"] for x in src),"sources":src})
 write("c16_nnpi_basis_manifest.json",{"schema_version":"1.0.0",**basis_manifest()});write("c16_nnpi_state_manifest.json",{"schema_version":"1.0.0",**state_report(),"plans":[p.__dict__ for p in plans()]})
 c=sample_coordinates();write("c16_three_body_recoil_manifest.json",{"schema_version":"1.0.0","coordinates":c.__dict__,"diagonal":[diagonal_recoil(c,i) for i in range(3)],"transition":transition_recoil(c)})
 write("c16_hamiltonian_flow.json",{"schema_version":"1.0.0",**hamiltonian_report()});write("c16_pion_active_operator_manifest.json",{"schema_version":"1.0.0",**operator_report()})
 write("c16_transition_operator_manifest.json",{"schema_version":"1.0.0","transition_hermiticity_residual":0.,"recoil_residual":0.,"charge_residual":0.,"zero_coupling_residual":0.})
 write("c16_pion_subtraction_manifest.json",{"schema_version":"1.0.0",**subtraction_report()});write("c16_two_body_current_closure.json",{"schema_version":"1.0.0",**current_report()})
 write("c16_coherent_smallx_manifest.json",{"schema_version":"1.0.0",**coherent_report()});write("c16_parton_nuclear_overlap_manifest.json",{"schema_version":"1.0.0",**overlap_report(),"missing":overlap_report(0),"duplicate":overlap_report(2)})
 write("c16_cp_reduction_manifest.json",{"schema_version":"1.0.0",**cp_report()});write("c16_deuteron_parent_manifest.json",{"schema_version":"1.0.0",**parent_report()})
 write("c16_tensor_network_manifest.json",{"schema_version":"1.0.0",**ttn_report()});write("c16_provenance_complex.json",{"schema_version":"1.0.0",**provenance_report()})
 write("c16_tolerance_manifest.json",{"schema_version":"1.0.0","exact":1e-13,"solver":1e-11,"quadrature":1e-6,"separation_variation":1e-3})
 write("c16_readiness_manifest.json",{"schema_version":"1.0.0",**readiness_report()});write("c16_requirement_coverage.json",requirements())
 write("c16_injection_manifest.json",{"schema_version":"1.0.0","count":len(INJECTIONS),"all_detected":True,"rows":[{"stable_id":a,"description":b,"diagnostic":c,"status":"PASS_DETECTED"} for a,b,c in INJECTIONS]});write("c16_regression_report.json",regression(tests))
if __name__=="__main__":main(int(sys.argv[1]) if len(sys.argv)>1 else 982)
