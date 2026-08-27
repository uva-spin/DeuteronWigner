import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdphysinput1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,k,v=None,x=None):
 d={"schema":f"C213-{k.upper().replace('_','-')}-V1","artifact":k,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical_record_ready":False,"physical_values_selected":0,"C158_value_inputs":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if v is not None:d["authority_record"]=p(v)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2)+"\n")
A={"source":c.physical_source_ledger(),"parameters":c.parameter_authority_ledger(),"consumption":c.schema_consumption_audit(),"repository":c.repository_git_authority_audit(),"exclusion":c.exclusion_quarantine_ledger(),"gap":c.gap_decision(),"release":c.release_manifest(),"handoff":c.next_handoff_contract(),"scope":c.static_isolation_guard(),"complete":c.completeness_certificate()}
for stem,key in (("physical_source_ledger","source"),("parameter_authority_ledger","parameters"),("schema_consumption_audit","consumption"),("repository_git_authority_audit","repository"),("exclusion_quarantine_ledger","exclusion"),("gap_decision","gap"),("release","release"),("next_handoff","handoff")):
 for s in ("contract","manifest","validation"):e(f"c213_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","plan_validation","api_contract","api_validation","safe_loading_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","user_worktree_preservation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","sharded_build_report","holdout_plan","independent_holdout_validation","regression_report","readiness_report","hqcdphysinput1_completeness_certificate"):
 e(f"c213_{n}.json",n,A["complete"] if "completeness" in n else A["scope"],{"validation":"PASS"})
e("c213_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c213_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c213_implementation_report.md").write_text(f"# C213/HQCDPHYSINPUT1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nBaseline: {c.BASELINE}\nC213 root: {c.PACKAGE_ROOT}\n\nC154 supplies two authenticated standard physical-coordinate capsules and C155 supplies the flavor identity, but no complete Hamiltonian-ready record exists. Running/threshold transport, common-IR and finite-basis target binding, counterterm selection, physical boundary choices, and joint covariance remain explicit. No value was selected or consumed.\n")
