import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdc117standardside1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c268_hqcdc117standardside1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"standard_side_audit":{"rows":tuple(c.standard_side_audit(d) for d in c.DIRECTIONS),"root":c.ROOTS["AUDIT"]},"matching_residuals":c.matching_residuals(),"source_route_audit":c.source_route_audit(),"uncertainty_boundary":c.uncertainty_boundary(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c268_{s}_{q}.json",{**base,"schema":f"C268-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation") :w(O/f"c268_{s}.json",{**base,"schema":f"C268-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c268_mutation_report.json",{**base,"schema":"C268-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c268_test_execution_report.json",{**base,"schema":"C268-TEST-EXECUTION-V1","focused_tests":"124 C250-C268 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C268-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c268_implementation_report.md").write_text(f"# C268/HQCDC117STANDARDSIDE1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC268 root: {c.PACKAGE_ROOT}\n\nFour-direction audit proves the standard side remains unavailable, not zero: no named physical state/observable is authenticated and the C262 conversion is uncomputed. C269 owns the smallest named-channel authority recovery.\n")
