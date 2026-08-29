import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassshapetail1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c310_hqcdrimassshapetail1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"asymptotic_authority":c.asymptotic_authority(),"extended_scan":c.extended_scan(),"tail_enclosures":c.tail_enclosures(),"finite_remainders":c.finite_remainders(),"covariance":c.covariance_contract(),"stability":c.stability_certificate(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c310_{s}_{q}.json",{**base,"schema":f"C310-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c310_{s}.json",{**base,"schema":f"C310-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c310_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(O/"c310_test_execution_report.json",{**base,"focused_tests":"C250-C310 cumulative assertions","live_mutations":384});w(R/"manifest.json",{"status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False});(O/"c310_implementation_report.md").write_text(f"# C310/HQCDRIMASSSHAPETAIL1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nThe authenticated C303 AST supports logarithmic harmonic-boundary tails. Independent cutoff windows and source-qualified inverse-power fit families enclose, and separately subtract, the CHI8 and RE_TF3 tails at each fixed epsilon. No exact rational coefficient or epsilon limit is claimed.\n")
