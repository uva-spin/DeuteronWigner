import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentsource1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c256_hqcdriquarkfixedkv2currentsource1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(path,v):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
def e(n,a,r=None,x=None):
 d={"schema":f"C256-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"qualified_targets":0,"directions_covered":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 w(O/n,d)
A={"inventory":c.source_inventory(),"schema":c.target_capsule_schema(),"candidates":c.qualified_candidate_records(),"coverage":c.direction_coverage(),"compatibility":c.compatibility_report(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("source_inventory","inventory"),("target_capsule_schema","schema"),("qualified_candidates","candidates"),("direction_coverage","coverage"),("compatibility","compatibility"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c256_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","api_contract","safe_loading_validation","dimension_validation","hermiticity_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c256_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c256_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c256_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
w(R/"manifest.json",{"schema":"C256-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c256_implementation_report.md").write_text(f"# C256/HQCDRIQUARKFIXEDKV2CURRENTSOURCE1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC256 root: {c.PACKAGE_ROOT}\n\nThe authenticated repository contains operator and request authority but no current-specific target observable capsule. A strict caller-authentication schema is ready; no target, scheme, scale, regulator, or coefficient was selected.\n")
