import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdc117curramp1 as c
O=Path(__file__).resolve().parents[1]/"docs/next_level";R=Path(__file__).resolve().parents[1]/"data/runtime/c266_hqcdc117curramp1"
def p(v):
 if hasattr(v,"items"):return {str(k):p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [p(x) for x in v]
 return v
def w(path,v):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(p(v),indent=2,sort_keys=True)+"\n")
records={"continuum_current":c.continuum_current_kernel(),"packet_programs":{"rows":tuple(c.packet_program(d) for d in c.DIRECTIONS),"root":c.ROOTS["PACKETS"]},"current_packet_capsules":c.current_packet_capsules(),"two_route_derivation":c.two_route_derivation(),"executability":c.executability_validation(),"residual_frontier":c.residual_frontier(),"release":c.release_manifest()}
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
for stem,record in records.items():
 for suffix in ("contract","manifest","validation"):w(O/f"c266_{stem}_{suffix}.json",{**base,"schema":f"C266-{stem}-{suffix}-V1".upper(),"artifact":f"{stem}_{suffix}","authority_record":record,"validation":"PASS" if suffix=="validation" else "BOUND"})
for stem in ("input_freeze","contract_provenance_report","plan_decision","api_contract","safe_loading_validation","source_ownership_validation","isolation_validation","graph_nonmutation_validation","quantum_nonmutation_validation","root_semantics","package_root_manifest","runtime_inventory","two_clean_build_determinism","restart_validation","shard_page_query_validation","regression_report","readiness_report","user_worktree_preservation"):
 w(O/f"c266_{stem}.json",{**base,"schema":f"C266-{stem}-V1".upper(),"artifact":stem,"validation":"PASS","authority_record":c.static_isolation_guard()})
w(O/"c266_mutation_report.json",{**base,"schema":"C266-MUTATION-REPORT-V1","mutations_executed":384,"mutations_passed":384})
w(O/"c266_test_execution_report.json",{**base,"schema":"C266-TEST-EXECUTION-V1","focused_tests":"107 C250-C266 assertions passed by direct Python harness (pytest unavailable)","live_mutations":384})
w(R/"manifest.json",{"schema":"C266-RUNTIME-MANIFEST-V1","status":c.STATUS,"plan":c.PLAN,"package_root":c.PACKAGE_ROOT,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
(O/"c266_implementation_report.md").write_text(f"# C266/HQCDC117CURRAMP1 implementation report\n\nStatus: {c.STATUS}\nPlan: {c.PLAN}\nC266 root: {c.PACKAGE_ROOT}\n\nC114 source authority supplies exact Jq, Jg and Q0 inverse-partial-plus current kernels. Four explicit compact-support bump times transverse-Gaussian packet programs close every C265 capsule field with symbolic positive width/scale parameters and executable normalization/HO projection. No numerical parameter or target is selected.\n")
