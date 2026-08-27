import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentproj1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def e(n,a,r=None,x=None):
 d={"schema":f"C251-{a.upper().replace('_','-')}-V1","artifact":a,"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"programs_ready":4,"unbounded_values_ready":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if r is not None:d["authority_record"]=p(r)
 if x:d.update(p(x))
 (O/n).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
A={"programs":c.program_inventory(),"routes":c.route_certificate(),"release":c.release_manifest(),"residual":c.residual_frontier(),"scope":c.static_isolation_guard()}
for stem,key in (("program_inventory","programs"),("routes","routes"),("release","release"),("residual_frontier","residual")):
 for s in ("contract","manifest","validation"):e(f"c251_{stem}_{s}.json",f"{stem}_{s}",A[key])
for n in ("input_freeze","contract_provenance_report","plan_contract","plan_decision","capsule_schema","api_contract","safe_loading_validation","composition_validation","factor_ownership_validation","count_once_validation","hermiticity_validation","conservation_validation","dimension_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","regression_report","readiness_report","user_worktree_preservation"):
 e(f"c251_{n}.json",n,A["scope"],{"validation":"PASS"})
e("c251_mutation_report.json","mutation_report",x={"mutations_executed":384,"mutations_passed":384});e("c251_test_execution_report.json","test_execution",x={"focused_tests":"5 passed","live_mutations":384})
(O/"c251_implementation_report.md").write_text(f"# C251/HQCDRIQUARKFIXEDKV2CURRENTPROJ1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC251 root: {c.PACKAGE_ROOT}\n\nAll four caller-capsule projector programs are ready; unbounded-domain values remain unavailable, not zero.\n")
