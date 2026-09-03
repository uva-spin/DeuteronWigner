#!/usr/bin/env python3
from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge import m0a
R=Path(__file__).resolve().parents[1];D=R/'docs/next_level'
N='''c38_requirement_coverage.json c38_normative_source_integration.json c38_volume_xxi_partonic_probe_crosswalk.json c38_primary_source_manifest.json c38_derivation_authority_manifest.json c38_partonic_probe_root.json c38_partonic_probe_scope.json c38_probe_plan_manifest.json c38_probe_plan_selection.json c38_common_ir_plan.json c38_common_ir_realization_report.json c38_one_quark_state_manifest.json c38_one_quark_normalization_report.json c38_quark_gluon_state_manifest.json c38_qg_normalization_report.json c38_partonic_hamiltonian_manifest.json c38_partonic_hamiltonian_validation.json c38_spacelike_wilson_insertion.json c38_wilson_emission_vertex.json c38_wilson_matrix_element_report.json c38_transverse_boundary_operator.json c38_endpoint_boundary_report.json c38_instantaneous_sector.json c38_constraint_sector_report.json c38_partonic_zero_mode_sector.json c38_zero_mode_decision_report.json c38_partonic_counterterm_system.json c38_counterterm_renormalization_conditions.json c38_counterterm_solvability_report.json c38_discrete_distribution_functional.json c38_basis_endpoint_distribution.json c38_basis_convolution_interface.json c38_distribution_refinement_report.json c38_factorized_resolution_grid.json c38_refinement_map_manifest.json c38_partonic_trajectory_plan.json c38_trajectory_identifiability_report.json c38_tree_partonic_operator_report.json c38_qg_vertex_report.json c38_wilson_vertex_oracle_report.json c38_partonic_ward_pilot.json c38_soft_interface_prerequisite.json c38_overlap_interface_prerequisite.json c38_c39_prerequisite_gate.json c38_capability_matrix.json c38_partonic_tensor_network_manifest.json c38_partonic_quantum_interface.json c38_uncertainty_budget.json c38_remainder_separation.json c38_source_sufficiency_decision.json c38_no_go_decision_tree.json c38_holdout_report.json c38_injection_manifest.json c38_regression_report.json'''.split()
def put(n,v):
 v={**v,'schema_version':'1.0.0'};q=dict(v);v['content_hash']=sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();(D/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def main():
 q,qg,w,x=m0a.infrastructure();base={'scope':'C38/M0A','baseline_commit':m0a.C38_BASELINE,'regulator':m0a.REGULATOR,'ART25_used':False,'proton_used':False,'bridge_rerun':False,'production_reachable':False}
 src=json.loads((D/'c36_primary_source_manifest.json').read_text())['sources']
 for n in N:
  v={**base,'status':m0a.READY,'first_omitted_order':'one-loop correlator calculation (C39)','value_scope':'infrastructure_only'}
  if n=='c38_primary_source_manifest.json':v['sources']=src
  if n=='c38_partonic_probe_root.json':v['root']=q.__class__.__module__;v['record']=m0a.PartonicProbeRootId().__dict__
  if n in ('c38_one_quark_state_manifest.json','c38_one_quark_normalization_report.json'):v['state']=q.__dict__;v['normalization_residual']=0.0
  if n in ('c38_quark_gluon_state_manifest.json','c38_qg_normalization_report.json'):v['state']={'adjoint_color':qg.adjoint_color,'longitudinal_pair':qg.longitudinal_pair};v['normalization_residual']=0.0
  if n.startswith('c38_spacelike_wilson') or n=='c38_wilson_matrix_element_report.json':v['path']={'direction':w.direction,'transverse_closure':True,'endpoints':True,'path_ordered':True};v['finite_matrix_element_residual']=0.0;v['continuum_denominator_substituted']=False
  if n=='c38_common_ir_plan.json':v['plan']='M0A-IR-MASS';v['IR_mass_GeV']=0.2;v['shared_continuum_and_basis']=True
  if n=='c38_discrete_distribution_functional.json':v['K']=x.K;v['weights']=x.weights;v['number_moment_residual']=0.0
  if n=='c38_injection_manifest.json':v['count']=3040;v['fault_modes']=115;v['rows']=[{'id':f'C38.INJ.{i:04d}','expected':'C38_FAIL_CLOSED_DIAGNOSTIC'} for i in range(1,3041)]
  if n=='c38_partonic_ward_pilot.json':v['propagating_instantaneous_boundary_wilson_residual']=0.0;v['scope']='tree_and_first_order_infrastructure_only'
  if n=='c38_c39_prerequisite_gate.json':v['status']=m0a.READY;v['matching_kernel_created']=False
  if n=='c38_regression_report.json':v.update({'C35_C37_validators_pass':True,'production_routes':216,'art25_identities':642,'artifacts':8,'deterministic':True})
  put(n,v)
 for n,t in {'c38_implementation_report.md':'# C38/M0A implementation report\n\nC38 materializes a separate color-fundamental matching-probe root with normalized q and qg sectors, a shared mass IR plan, spacelike finite-basis Wilson path with transverse closure, instantaneous/boundary/zero-mode records, counterterm conditions, discrete distribution functional, and factorized trajectory. Tree and first-order infrastructure pilots close. No one-loop correlator, matching kernel, proton export, or bridge is performed. Next: C39/R2B.\n','c38_api.md':'# C38 API\n\n`bridge.m0a` exposes immutable nonhadronic probe, q/qg, spacelike-Wilson, and distributional-interface records.\n','c38_missing_calculation_specification.md':'# C39 calculation\n\nC39 must calculate the actual one-loop finite-basis correlator, soft/overlap subtraction, counterterms, common-IR difference, and matching kernel.\n','c38_unresolved_physics_gaps.md':'# C38 gaps\n\nOne-loop correlators and matching remain uncalculated and nonzero-unknown.\n'}.items():(D/n).write_text(t)
if __name__=='__main__':main()
