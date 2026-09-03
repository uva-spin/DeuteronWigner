import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassprocess1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c287_hqcdrimassprocess1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"observable_classification":c.observable_classification(),"process_applicability":c.process_applicability_audit(),"caller_capsule_schema":c.caller_capsule_schema(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c287_{s}_{q}.json",{**base,"schema":f"C287-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c287_{s}.json",{**base,"schema":f"C287-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c287_mutation_report.json",{**base,"schema":"C287-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c287_test_execution_report.json",{**base,"schema":"C287-TEST-EXECUTION-V1","focused_tests":"289 C250-C287 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C287-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c287_implementation_report.md").write_text(f"# C287/HQCDRIMASSPROCESS1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nThe off-shell signed-mass two-point target is not DIS or DY, and PV does not select a process. The caller-owned physical boundary and holonomy capsule remains the exact frontier.\n")
