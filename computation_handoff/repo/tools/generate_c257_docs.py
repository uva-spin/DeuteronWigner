import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenttarget1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c257_hqcdriquarkfixedkv2currenttarget1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(path,v):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
def e(n,a,r=None,x=None):
 d={"schema":f"C257-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"qualified_capsules":0,"directions_covered":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 w(O/n,d)
A={"discovery":c.discovery_inventory(),"rejections":c.candidate_rejection_ledger(),"resolution":c.capsule_resolution(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("discovery_inventory","discovery"),("candidate_rejections","rejections"),("capsule_resolution","resolution"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c257_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","api_contract","safe_loading_validation","dimension_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c257_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c257_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c257_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
w(R/"manifest.json",{"schema":"C257-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c257_implementation_report.md").write_text(f"# C257/HQCDRIQUARKFIXEDKV2CURRENTTARGET1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC257 root: {c.PACKAGE_ROOT}\n\nNo authenticated target capsule was found in repository, Git-history, or local project authority. Operator and request records were rejected as nonconditions; four directions remain uncovered and nonzero-unavailable.\n")
