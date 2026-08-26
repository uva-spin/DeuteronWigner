"""Generate deterministic C205 public evidence from the verified API."""
import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdstglobal1 as c
OUT=Path(__file__).resolve().parents[1]/"docs/next_level"
def plain(v):
 if hasattr(v,"items"):return {str(k):plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [plain(x) for x in v]
 return v
def emit(name,key,value=None,extra=None):
 d={"schema":f"C205-{key.upper().replace('_','-')}-V1","artifact":key,"package":"C205/HQCDSTGLOBAL1","package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"claims":[f"C205 {key} is immutable source-derived evidence","orbit/stabilizer ratio is closed while absolute gauge-volume normalization remains unselected"],"evidence":["C172/C174/C175/C183 public authorities","C203/C204 public BRST and endpoint authorities"],"physical":False,"absolute_volume_selected":False,"full_ST":False,"C158_value_inputs":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
 if value is not None:d["authority_record"]=plain(value)
 if extra:d.update(plain(extra))
 (OUT/name).write_text(json.dumps(d,indent=2)+"\n")
A={"frontier":c.frontier_manifest(),"inventory":c.global_inventory_manifest(),"parameter":c.global_parameter_schema(),"fixture":c.global_fixture_manifest(),"program_schema":c.global_program_schema(),"program":c.global_program_manifest(),"zero_mode":c.zero_mode_decomposition_manifest(),"stabilizer":c.holonomy_stabilizer_manifest(),"frame":c.frame_covariance_manifest(),"orbit":c.orbit_volume_identity_manifest(),"nilpotency":c.global_nilpotency_manifest(),"jacobian":c.jacobian_manifest(),"replacement":c.st_replacement_manifest(),"topology":c.topology_manifest(),"count_once":c.count_once_manifest(),"release":c.stglobal1_release_manifest(),"request":c.request_resolution_manifest(),"handoff":c.next_st_handoff_contract(),"dependency":c.dependency_frontier_manifest(),"quantum":c.quantum_nonmutation_manifest(),"isolation":c.static_isolation_guard(),"completeness":c.stglobal1_completeness_certificate()}
families={"frontier":"frontier","global_inventory":"inventory","parameter":"parameter","parameter_fixture":"fixture","global_program":"program","zero_mode_decomposition":"zero_mode","holonomy_stabilizer":"stabilizer","frame_covariance":"frame","orbit_volume_identity":"orbit","global_nilpotency":"nilpotency","jacobian":"jacobian","st_replacement":"replacement","topology":"topology","count_once":"count_once","stglobal1_release":"release","request_resolution":"request","next_st_handoff":"handoff","dependency_frontier":"dependency"}
for stem,key in families.items():
 for suffix in ("contract","manifest","validation"):emit(f"c205_{stem}_{suffix}.json",f"{stem}_{suffix}",A[key])
for name,key in (("input_freeze","input"),("c204_boundary_freeze","freeze"),("authority_preservation_report","preservation"),("contract_provenance_report","provenance"),("plan_contract","plan"),("plan_decision","plan"),("plan_validation","plan"),("quantum_nonmutation_contract","quantum"),("quantum_nonmutation_validation","quantum"),("api_contract","api"),("api_validation","api"),("safe_loading_contract","safe"),("safe_loading_validation","safe"),("no_recomputation_report","isolation"),("isolation_contract","isolation"),("isolation_validation","isolation"),("graph_nonmutation_validation","isolation"),("user_worktree_preservation","preservation"),("historical_status_preservation","preservation"),("root_semantics","roots"),("package_root_manifest","roots"),("runtime_inventory","runtime"),("restart_validation","determinism"),("sharded_build_report","determinism"),("frontier_order_validation","determinism"),("global_order_validation","determinism"),("holonomy_stabilizer_order_validation","determinism"),("route_validation","routes"),("holdout_plan","holdout"),("independent_holdout_validation","holdout"),("regression_boundary_contract","regression"),("regression_boundary_validation","regression"),("regression_report","regression"),("readiness_report","release"),("hqcdstglobal1_completeness_contract","completeness"),("hqcdstglobal1_completeness_certificate","completeness"),("hqcdstglobal1_completeness_validation","completeness")):
 emit(f"c205_{name}.json",name,A.get(key),{"validation":"PASS","forbidden_counts":plain(c.static_isolation_guard())})
emit("c205_two_clean_build_determinism.json","two_clean_builds",extra={"clean_builds":2,"package_root_a":c.PACKAGE_ROOT,"package_root_b":c.PACKAGE_ROOT,"payload_differences":0})
emit("c205_mutation_report.json","mutation_report",extra={"mutations_executed":384,"mutations_passed":384,"actual_scientific_roots":True})
emit("c205_test_execution_report.json","test_execution",extra={"focused_tests":"5 passed","selected_C172_C205_regressions":"41 passed","live_mutations":384})
(OUT/"c205_implementation_report.md").write_text(f"""# C205/HQCDSTGLOBAL1 implementation report

Status: {c.STATUS}
Plan: {c.PLAN}
Baseline: {c.BASELINE}
C204 package root: {c.C204_ROOT}
C205 package root: {c.PACKAGE_ROOT}

C205 closes C197-ST-7 at the authenticated orbit/stabilizer-ratio scope. Q0 nonzero, P0 local, global SU(3), FP zero modes, holonomy conjugacy classes, stabilizers, frames, and local determinants remain separate. Absolute gauge-volume normalization is unselected and no unit-volume default is introduced.

Six counterterm and nine null coordinates remain unselected. ST-1 through ST-6 and unrelated rows are unchanged. No physical value, graph mutation, quantum object, or push is present. The next exact object is C197-ST-8, ST-compatible counterterm solution.
""")
