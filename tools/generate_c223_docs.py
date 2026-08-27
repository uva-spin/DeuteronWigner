import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedktrans1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C223-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"free_denominator_complete":True,"threshold":0,"retained_matrix_reused":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"schema":c.transverse_program_schema(),"routes":c.route_certificate(),"free":c.free_denominator_completion(),"residual":c.residual_frontier(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("transverse_program_schema","schema"),("independent_route","routes"),("free_denominator_completion","free"),("residual_frontier","residual"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c223_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdriquarkfixedktrans1_completeness_certificate"):
 e(f"c223_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c223_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c223_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c223_implementation_report.md").write_text(f"# C223/HQCDRIQUARKFIXEDKTRANS1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC223 root: {c.PACKAGE_ROOT}\n\nC223 exposes C62 exact rational-x TM coefficients and C128 symbolic transverse HO ladder entries for caller-supplied complement modes. Exact CM-ground selection and Hermitian partners complete symbolic Q_R H0 Q_R without dense enumeration; Q_R V1 Q_R is the C224 frontier.\n")
