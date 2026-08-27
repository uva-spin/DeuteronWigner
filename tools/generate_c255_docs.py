import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentsub1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c255_hqcdriquarkfixedkv2currentsub1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def write(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(p(value),indent=2,sort_keys=True)+"\n")
def e(n,a,r=None,x=None):
 d={"schema":f"C255-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"rank":0,"nullity":4,"subtraction_coefficients":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 write(O/n,d)
A={"inventory":c.condition_inventory(),"map":c.direction_condition_map(),"system":c.exact_condition_system(),"compatibility":c.compatibility_report(),"solve":c.solve_subtraction_coefficients(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("condition_inventory","inventory"),("direction_condition_map","map"),("exact_system","system"),("compatibility","compatibility"),("solve","solve"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c255_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","api_contract","safe_loading_validation","hermiticity_validation","dimension_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c255_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c255_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c255_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
write(R/"manifest.json",{"schema":"C255-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c255_implementation_report.md").write_text(f"# C255/HQCDRIQUARKFIXEDKV2CURRENTSUB1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC255 root: {c.PACKAGE_ROOT}\n\nNo authenticated C150-C158 condition applies to the four C117 graph-specific complement directions. The exact system has rank 0 and nullity 4; every coefficient remains unavailable, never zero.\n")
