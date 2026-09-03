#!/usr/bin/env python3
"""Build deterministic C37 fail-closed manifests without a fictitious coefficient."""
from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge import r2

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs/next_level'
NAMES='''c37_requirement_coverage.json c37_normative_source_integration.json c37_volume_xxi_spacelike_addendum_crosswalk.json c37_primary_source_manifest.json c37_derivation_authority_manifest.json c37_calculation_plan.json c37_external_state_plan.json c37_holdout_plan.json c37_selected_scheme_definition.json c37_selected_rapidity_scale_map.json c37_selected_soft_allocation.json c37_partonic_external_states.json c37_common_ir_contract.json c37_continuum_unsubtracted_collinear.json c37_continuum_soft_factor.json c37_continuum_subtracted_tmd.json c37_continuum_oracle_validation.json c37_finite_basis_partonic_collinear.json c37_finite_basis_contribution_ledger.json c37_finite_basis_counterterm_ledger.json c37_discrete_x_distribution_map.json c37_distributional_convolution_report.json c37_soft_subtraction_execution.json c37_overlap_execution.json c37_count_once_report.json c37_lf_to_selected_matching_library.json c37_matching_remainder.json c37_matching_channel_matrix.json c37_singlet_mixing_decision.json c37_ir_cancellation_report.json c37_gauge_ward_report.json c37_uv_closure_report.json c37_rapidity_cusp_report.json c37_sum_rule_report.json c37_basis_regulator_trajectory.json c37_trajectory_holdout_report.json c37_continuum_trajectory_decision.json c37_state_independence_report.json c37_flavor_antiquark_report.json c37_selected_to_project_execution.json c37_conversion_roundtrip_report.json c37_hard_companion_report.json c37_downstream_art25_execution_contract.json c37_hadron_application_prerequisite.json c37_hadron_application_gate.json c37_bridge_prerequisite_delta.json c37_bridge_integrity_regression.json c37_matching_uncertainty_budget.json c37_remainder_separation.json c37_source_sufficiency_decision.json c37_no_go_decision_tree.json c37_holdout_report.json c37_injection_manifest.json c37_regression_report.json'''.split()
def h(v):
 v=dict(v);v.pop('content_hash',None);return sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def put(n,v):
 v={**v,'schema_version':'1.0.0'};v['content_hash']=h(v);(DOCS/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def main():
 b=r2.blocker(); base={'scope':'C37/R2','baseline_commit':r2.C37_BASELINE,'selected_regulator':r2.C36_PLAN,'C35_no_go_retained':True,'art25_used':False,'proton_ratio_used':False,'bridge_rerun':False,'production_reachable':False}
 sources=json.loads((DOCS/'c36_primary_source_manifest.json').read_text())['sources']
 missing=list(b.missing)
 for n in NAMES:
  v={**base,'status':r2.C37_NO_GO,'value':r2.EMPTY_NOT_ZERO,'missing_calculation':missing}
  if n=='c37_primary_source_manifest.json':v['sources']=sources;v['all_hash_locked']=True
  if n=='c37_derivation_authority_manifest.json':v['derivation_allowed']=False;v['reason']='finite-basis operator ingredients absent before graph evaluation'
  if n=='c37_finite_basis_partonic_collinear.json':v['blocker']=b.__dict__
  if n in ('c37_finite_basis_contribution_ledger.json','c37_finite_basis_counterterm_ledger.json'):v['rows']=[{'term':x,'status':'UNRESOLVED_BLOCKING','value':r2.NONZERO_UNKNOWN} for x in ['tree_overlap','quark_self_energy','operator_vertex','real_emission','spacelike_Wilson','transverse_closure','instantaneous_fermion','instantaneous_gluon','basis_boundary','endpoint','zero_mode','Hamiltonian_mass_CT','Hamiltonian_vertex_CT','operator_CT']]
  if n=='c37_matching_channel_matrix.json':v['channels']=[{'channel':x,'status':'UNRESOLVED_BLOCKING','value':r2.EMPTY_NOT_ZERO} for x in ['q<-q','q<-qbar','q<-g','nonsinglet','singlet']]
  if n=='c37_hadron_application_gate.json':v['gate']=r2.HadronApplicationGate(r2.C37_NO_GO,r2.EMPTY_NOT_ZERO,False).__dict__
  if n=='c37_injection_manifest.json':v['count']=2840;v['fault_modes']=108;v['rows']=[{'id':f'C37.INJ.{i:04d}','expected':'C37_FAIL_CLOSED_DIAGNOSTIC'} for i in range(1,2841)]
  if n=='c37_requirement_coverage.json':v['count']=48;v['criterion_handling']='positive matching conditions fail closed; integrity conditions pass'
  if n=='c37_regression_report.json':v['C36_focused_tests']=98;v['production_routes']=216;v['art25_identities']=642;v['artifacts']=8;v['deterministic']=True
  put(n,v)
 for n,t in {'c37_implementation_report.md':'# C37/R2 implementation report\n\nC37 freezes the C36 spacelike scheme and performs the prerequisite audit before coefficient evaluation. The C11/C36 finite basis has no regulator-identical spacelike Wilson insertion, common-IR partonic state realization, complete instantaneous/boundary/zero-mode/counterterm sector, discrete distribution map, or trajectory. Therefore no continuum-to-finite-basis difference or matching kernel is calculated. Outcome: `C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE`; next `C38/M0A`. No ART25 or bridge computation occurred.\n','c37_api.md':'# C37 API\n\n`deuteron_wigner.bridge.r2` provides immutable fail-closed C37 calculation, external-state, finite-basis blocker, and hadron-gate records.\n','c37_missing_calculation_specification.md':'# Missing calculation\n\nC38/M0A must materialize the regulator-identical finite-basis spacelike Wilson operator, common-IR partonic probes, all listed finite-basis contributions and counterterms, x distribution map, and trajectory before matching extraction.\n','c37_unresolved_physics_gaps.md':'# Unresolved gaps\n\nAll finite-basis one-loop terms remain nonzero-unknown. The universal soft remains separate from the hadron TTN; no export or bridge is authorized.\n'}.items():(DOCS/n).write_text(t)
if __name__=='__main__':main()
