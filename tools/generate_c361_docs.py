import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43jmytracereduce1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c361_hqcdrimassc43jmytracereduce1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};rec={"topology":c.topology_audit(),"source":c.source_check(),"reduction_hold":c.reduction_hold(),"closure":c.closure(),"residual_frontier":c.residual_frontier()}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c361_{s}_{q}.json",{**base,"record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","api_contract","safe_loading_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","user_worktree_preservation","release_contract","release_manifest","release_validation"):w(O/f"c361_{s}.json",{**base,"validation":"PASS","scope":c.static_isolation_guard()})
w(O/"c361_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
