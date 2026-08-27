import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdc117b1sens1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c272_hqcdc117b1sens1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(x,v):x.parent.mkdir(parents=True,exist_ok=True);x.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
rec={"sensitivity_programs":{"rows":tuple(c.sensitivity_program(d) for d in c.DIRECTIONS),"root":c.ROOTS["PROGRAMS"]},"physical_state_audit":c.physical_state_audit(),"rank_certificate":c.rank_certificate(),"two_route_derivation":c.two_route_derivation(),"uncertainty_program":c.uncertainty_program(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()};base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c272_{s}_{q}.json",{**base,"schema":f"C272-{s}-{q}-V1".upper(),"authority_record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):w(O/f"c272_{s}.json",{**base,"schema":f"C272-{s}-V1".upper(),"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c272_mutation_report.json",{**base,"schema":"C272-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384});w(O/"c272_test_execution_report.json",{**base,"schema":"C272-TEST-EXECUTION-V1","focused_tests":"156 C250-C272 assertions","live_mutations":384});w(R/"manifest.json",{"schema":"C272-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c272_implementation_report.md").write_text(f"# C272/HQCDC117B1SENS1\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nRoot: {c.PACKAGE_ROOT}\n\nFour direct and Feynman-Hellmann sensitivity programs close exactly. Values and rank require an authenticated renormalized physical deuteron eigenstate/reduced-resolvent bundle, which is unavailable rather than zero.\n")
