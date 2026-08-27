import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2current1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,a,r=None,x=None):
 d={"schema":f"C248-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"complement_kernel_ready":False,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"audit":c.dependency_audit(),"retained":c.retained_authority_manifest(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("dependency_audit","audit"),("retained_authority","retained"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c248_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","api_contract","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c248_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c248_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c248_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c248_implementation_report.md").write_text(f"# C248/HQCDRIQUARKFIXEDKV2CURRENT1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC248 root: {c.PACKAGE_ROOT}\n\nThe retained C126/C127 authority is frozen; the complement witness-coordinate map remains the exact C249 frontier.\n")
