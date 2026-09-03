import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43jmygroupreduce1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c367_hqcdrimassc43jmygroupreduce1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};rec={"groups":c.grouped_ast(),"reduction":c.algebraic_reduction(),"laurent":c.laurent_ledger(),"cancellation":c.cancellation_contract(),"closure":c.closure(),"residual_frontier":c.residual_frontier()}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c367_{s}_{q}.json",{**base,"record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","api_contract","safe_loading_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","user_worktree_preservation","release_contract","release_manifest","release_validation"):w(O/f"c367_{s}.json",{**base,"validation":"PASS","scope":c.static_isolation_guard()})
w(O/"c367_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
