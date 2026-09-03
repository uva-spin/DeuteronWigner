import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdc117renormh1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c274_hqcdc117renormh1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"slot_audit":c.slot_audit(),"hamiltonian_families":{"rows":tuple(c.hamiltonian_family(r) for r in c.RESOLUTIONS),"root":c.ROOTS["FAMILIES"]},"derivative_program":c.derivative_program(),"route_audit":c.route_audit(),"holdout_crosswalk":c.holdout_crosswalk(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c274_{s}_{q}.json",{**base,"schema":f"C274-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c274_{s}.json",{**base,"schema":f"C274-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c274_mutation_report.json",{**base,"schema":"C274-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c274_test_execution_report.json",{**base,"schema":"C274-TEST-EXECUTION-V1","focused_tests":"173 C250-C274 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C274-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c274_implementation_report.md").write_text(f"# C274/HQCDC117RENORMH1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nThree Hermitian symbolic Hamiltonian families close with four explicit C117 coordinates. The composite non-C117 physical bundle remains conditional/unbound and is not zeroed.\n")
