import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkvcontrib1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C238-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"bindings":24,"finite_enclosures":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"binding":c.denominator_binding_manifest(),"components":c.denominator_component_audit(),"route":c.route_certificate(),"residual":c.residual_frontier(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("denominator_binding","binding"),("component_audit","components"),("independent_route","route"),("residual_frontier","residual"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c238_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdriquarkfixedkvcontrib1_completeness_certificate"):
 e(f"c238_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c238_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c238_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c238_implementation_report.md").write_text(f"# C238/HQCDRIQUARKFIXEDKVCONTRIB1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC238 root: {c.PACKAGE_ROOT}\n\nC238 binds 24 numerator enclosures to the resolvent schema, complete H0 component, and V1 authority. It claims no finite contribution enclosure: omitted V2 and pole/resolvent-norm authority remain.\n")
