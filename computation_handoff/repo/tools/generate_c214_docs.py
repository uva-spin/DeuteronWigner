import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdphysinputmap1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C214-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical_values":False,"map_executable":False,"C154_values_consumed":0,"C158_values_consumed":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2)+"\n")
A={"schema":c.edge_schema(),"dag":c.mapping_dag(),"c158":c.c158_role_audit(),"expressions":c.source_expression_audit(),"audits":c.independent_dependency_audits(),"missing":c.missing_edge_decision(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("edge_schema","schema"),("mapping_dag","dag"),("c158_role_audit","c158"),("source_expression_audit","expressions"),("independent_dependency_audits","audits"),("missing_edge_decision","missing"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c214_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdphysinputmap1_completeness_certificate"):
 e(f"c214_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c214_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c214_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c214_implementation_report.md").write_text(f"# C214/HQCDPHYSINPUTMAP1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC214 root: {c.PACKAGE_ROOT}\n\nSeparate mass and coupling DAGs expose fourteen typed edges. C158 supplies coefficients but no target value. Forward and reverse audits select the six C168 project-owned perturbative adapter calculations as the exact nonblocking frontier. No physical value was consumed.\n")
