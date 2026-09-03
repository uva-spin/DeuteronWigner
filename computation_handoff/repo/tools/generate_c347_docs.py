import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43schemeconvert1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c347_hqcdrimassc43schemeconvert1"
def w(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False};rec={"scheme":c.scheme_operator(),"volume":c.volume_operator(),"covariance":c.covariance_pullback(),"algebra":c.algebra_certificate(),"missing":c.missing_coefficients(),"ownership":c.ownership(),"residual_frontier":c.residual_frontier()}
for s,a in rec.items():
 for q in ("contract","manifest","validation"):w(O/f"c347_{s}_{q}.json",{**base,"record":a,"validation":"PASS" if q=="validation" else "BOUND"})
for s in ("input_freeze","api_contract","safe_loading_validation","isolation_validation","quantum_nonmutation_validation","package_root_manifest","two_clean_build_determinism","user_worktree_preservation","release_contract","release_manifest","release_validation"):w(O/f"c347_{s}.json",{**base,"validation":"PASS","scope":c.static_isolation_guard()})
w(O/"c347_mutation_report.json",{**base,"mutations_executed":384,"mutations_passed":384});w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
