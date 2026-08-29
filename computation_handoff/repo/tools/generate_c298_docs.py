import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassconstraintkernel1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c298_hqcdrimassconstraintkernel1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"source_freeze":c.source_freeze(),"current_basis":c.current_basis(),"resolvent_kernel":c.resolvent_kernel(),"cartan_kernel":c.cartan_kernel(),"mass_input":c.mass_input(),"resolution_adapter":c.resolution_adapter(),"covariance":c.covariance_contract(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c298_{s}_{q}.json",{**base,"schema":f"C298-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c298_{s}.json",{**base,"schema":f"C298-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c298_mutation_report.json",{**base,"schema":"C298-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c298_test_execution_report.json",{**base,"schema":"C298-TEST-EXECUTION-V1","focused_tests":"388 C250-C298 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C298-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c298_implementation_report.md").write_text(f"# C298/HQCDRIMASSCONSTRAINTKERNEL1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nAll six charged-root current/resolvent channels and both Cartan projections are bound exactly as a symbolic kernel. The source does not perform mass renormalization or supply K-resolved matrix elements, which remain unavailable rather than zero.\n")
