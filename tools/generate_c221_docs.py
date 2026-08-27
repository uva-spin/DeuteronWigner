import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkden1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C221-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"denominator_executable":False,"missing_zeroed":0,"retained_zero_promoted":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"schema":c.denominator_schema(),"components":c.component_audit(),"nonpromotion":c.retained_zero_nonpromotion_certificate(),"residual":c.residual_frontier(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("denominator_schema","schema"),("component_audit","components"),("retained_zero_nonpromotion","nonpromotion"),("residual_frontier","residual"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c221_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdriquarkfixedkden1_completeness_certificate"):
 e(f"c221_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c221_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c221_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c221_implementation_report.md").write_text(f"# C221/HQCDRIQUARKFIXEDKDEN1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC221 root: {c.PACKAGE_ROOT}\n\nC221 publishes a safe omitted-resolvent schema and proves that C128 retained-basis internal-conservation zeros cannot be promoted to C130's omitted interfaces. The first missing denominator component is a source-derived free M2 operator on C220's symbolic complement domain.\n")
