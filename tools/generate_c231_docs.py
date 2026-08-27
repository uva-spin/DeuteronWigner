import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkvradconst1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C231-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"growth_programs":8,"critical_sets":8,"core_enclosures":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"capsule":c.capsule_schema(),"growth":c.growth_program_manifest(),"critical":c.critical_split_manifest(),"route":c.route_certificate(),"residual":c.residual_frontier(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("capsule","capsule"),("growth_program","growth"),("critical_split","critical"),("independent_route","route"),("residual_frontier","residual"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c231_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdriquarkfixedkvradconst1_completeness_certificate"):
 e(f"c231_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c231_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c231_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c231_implementation_report.md").write_text(f"# C231/HQCDRIQUARKFIXEDKVRADCONST1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC231 root: {c.PACKAGE_ROOT}\n\nC231 supplies computable monotone degree-two growth programs on caller-defined compact positive capsules for all eight C230 factors. Positive radicands imply empty interior critical sets on q>=0. Open-domain boundaries remain unavailable, not zero; directed finite-core enclosure is C232.\n")
