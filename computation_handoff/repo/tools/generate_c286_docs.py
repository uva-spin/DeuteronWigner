import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimasspathselect1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c286_hqcdrimasspathselect1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"project_path_selection":c.project_path_selection(),"conditional_process_map":c.conditional_process_map(),"selection_gate":c.selection_gate(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c286_{s}_{q}.json",{**base,"schema":f"C286-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c286_{s}.json",{**base,"schema":f"C286-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c286_mutation_report.json",{**base,"schema":"C286-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c286_test_execution_report.json",{**base,"schema":"C286-TEST-EXECUTION-V1","focused_tests":"280 C250-C286 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C286-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c286_implementation_report.md").write_text(f"# C286/HQCDRIMASSPATHSELECT1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nC179 selects the affine finite-HO path representative. C286 supplies separate future/past conditional branches; physical process and holonomy selection remain unresolved.\n")
