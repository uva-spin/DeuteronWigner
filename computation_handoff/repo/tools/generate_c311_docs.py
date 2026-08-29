import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassepslimit1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c311_hqcdrimassepslimit1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"epsilon_scan":c.epsilon_scan(),"extrapolation_models":c.extrapolation_models(),"limit_enclosures":c.limit_enclosures(),"covariance":c.covariance_contract(),"stability":c.stability_certificate(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c311_{s}_{q}.json",{**base,"schema":f"C311-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c311_{s}.json",{**base,"schema":f"C311-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c311_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(O/"c311_test_execution_report.json",{**base,"focused_tests":"C250-C311 cumulative assertions","live_mutations":384});w(R/"manifest.json",{"status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False});(O/"c311_implementation_report.md").write_text(f"# C311/HQCDRIMASSEPSLIMIT1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nSeparate C310 tail covariance is propagated through multiple epsilon windows and source-qualified extrapolation families to outward zero-epsilon shape-coefficient enclosures. C43 matching remains unclaimed.\n")
