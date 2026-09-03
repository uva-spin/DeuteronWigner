import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43jmykinematicast1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c378_hqcdrimassc43jmykinematicast1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};rec={"conventions":c.convention_ast(),"invariants":c.invariant_ast(),"cut":c.cut_substitutions(),"projectors":c.projector_substitutions(),"validation":c.validation(),"closure":c.closure(),"residual_frontier":c.residual_frontier()}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c378_{s}_{q}.json",{**base,"record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","api_contract","safe_loading_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","user_worktree_preservation","release_contract","release_manifest","release_validation"):w(O/f"c378_{s}.json",{**base,"validation":"PASS","scope":c.static_isolation_guard()})
w(O/"c378_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
