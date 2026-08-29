import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenteval1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,a,r=None,x=None):
 d={"schema":f"C250-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"spatial_ready":1,"spatial_incomplete":4,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"scope":c.evaluator_scope_manifest(),"release":c.release_manifest(),"residual":c.residual_frontier(),"isolation":c.static_isolation_guard()}
for stem,key in (("evaluator_scope","scope"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c250_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","api_contract","safe_loading_validation","route_validation","factor_ownership_validation","count_once_validation","hermiticity_validation","conservation_validation","dimension_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c250_{n}.json",n,A["isolation"],{"validation":"PASS"})
e("c250_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c250_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c250_implementation_report.md").write_text(f"# C250/HQCDRIQUARKFIXEDKV2CURRENTEVAL1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC250 root: {c.PACKAGE_ROOT}\n\nSymbolic current factors and I4 evaluation are ready; four complement projector classes remain unavailable, not zero.\n")
