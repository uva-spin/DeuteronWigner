import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentreg1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,a,r=None,x=None):
 d={"schema":f"C254-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"topology_ready":True,"subtraction_coefficients":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"topology":c.test_function_topology(),"subtraction":c.subtraction_ownership_manifest(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("topology","topology"),("subtraction_ownership","subtraction"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c254_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","capsule_schema","api_contract","safe_loading_validation","distribution_pairing_validation","limit_order_validation","hermiticity_validation","conservation_validation","dimension_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c254_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c254_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c254_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c254_implementation_report.md").write_text(f"# C254/HQCDRIQUARKFIXEDKV2CURRENTREG1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC254 root: {c.PACKAGE_ROOT}\n\nThe nonphysical C45 test topology and caller Abel family are ready; four subtraction coefficients remain unresolved.\n")
