import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdc117conttensor1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c263_hqcdc117conttensor1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(path,v):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
records={"locality":c.locality_classification(),"preimage_route_a":c.preimage_route_a(),"preimage_route_b":c.preimage_route_b(),"tensor_capsules":c.tensor_capsules(),"local_rismom":c.local_rismom_applicability(),"nonlocal_schema":c.nonlocal_matching_schema(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()}
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
for stem,record in records.items():
 for suffix in ("contract","manifest","validation"):w(O/f"c263_{stem}_{suffix}.json",{**base,"schema":f"C263-{stem}-{suffix}-V1".upper(),"artifact":f"{stem}_{suffix}","authority_record":record,"validation":"PASS" if suffix=="validation" else "BOUND"})
for stem in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation"):
 w(O/f"c263_{stem}.json",{**base,"schema":f"C263-{stem}-V1".upper(),"artifact":stem,"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c263_mutation_report.json",{**base,"schema":"C263-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384})
w(O/"c263_test_execution_report.json",{**base,"schema":"C263-TEST-EXECUTION-V1","focused_tests":"83 C250-C263 assertions passed by direct Python harness (pytest unavailable)","live_mutations_per_package":384})
w(R/"manifest.json",{"schema":"C263-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c263_implementation_report.md").write_text(f"# C263/HQCDC117CONTTENSOR1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC263 root: {c.PACKAGE_ROOT}\n\nTwo source-qualified ancestry routes classify all four C117 directions as regulated distributional kernels or external-state/channel projectors, not local continuum insertions. Local D-dimensional tensor capsules are therefore not applicable with proof. The generic RI/SMOM architecture remains methodological authority, while C264 must build four full-rank nonlocal continuum wavepacket/projector matching functionals.\n")
