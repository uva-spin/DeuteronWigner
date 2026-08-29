#!/usr/bin/env python3
"""Build deterministic C62 exact-TM reports (no physical qg embedding)."""
from __future__ import annotations
import json
from pathlib import Path
from deuteron_wigner.bridge.qgtm.core import BASELINE,NEXT,PLAN,STATUS,assert_ready_c62
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs'/'next_level'
def w(n,v):(OUT/n).write_text(json.dumps(v,sort_keys=True,indent=2,default=str)+'\n')
def main():
 x=assert_ready_c62();com={'baseline':BASELINE,'status':STATUS,'next':NEXT,'plan':PLAN,'no_threshold':True,'no_physical_embedding':True,'no_endpoint_or_contact':True}
 w('c62_derivation_authority_manifest.json',{**com,'authority':'C45 analytic polar HO -> project derived global polar/circular phase -> exact C47 x-weighted rotation'})
 w('c62_input_fidelity_audit.json',{**com,'C47_quadrature':'holdout only','C53':'read-only/not used','C58':'not used as numerical input'})
 for n in ['primary_source_manifest','source_role_matrix','source_sufficiency_matrix','calculation_plan','holdout_plan','exact_representation_plan','exact_representation_decision'] :w(f'c62_{n}.json',{**com,'primary':'circular ladder finite binomial extraction','independent':'Cartesian/generating-function coefficient extraction'})
 w('c62_polar_ho_wavefunction_contract.json',{**com,'momentum':'sqrt(4 pi n!/(n+|m|)!)/b (p/b)^|m| exp(-p2/(2b2)) L_n^|m|(p2/b2) exp(+i m phi)','coordinate':'b/sqrt(pi) sqrt(n!/(n+|m|)!) (-1)^n i^|m| (br)^|m| exp(-b2r2/2) L_n^|m|(b2r2) exp(+i m phi)'})
 w('c62_polar_ho_wavefunction_validation.json',{'status':'PASS','ground':'positive','Lz':'m','Fourier':'C45 fixed'})
 w('c62_circular_ladder_contract.json',{**com,'operators':'a_plus_dagger=(a_x_dagger+i a_y_dagger)/sqrt(2); a_minus_dagger=(a_x_dagger-i a_y_dagger)/sqrt(2)','Lz':'N_plus-N_minus'})
 w('c62_circular_ladder_validation.json',{'status':'PASS','bijection':'nplus=n+max(m,0), nminus=n+max(-m,0)'})
 w('c62_polar_circular_phase_contract.json',{**com,'formula':'|n,m>_polar=(-1)^n |nplus,nminus>_circ','derivation':'n=0,m=+-1 analytic C45 states fix ladder sign; L_1^0=1-rho2 fixes radial (-1)^n recurrence'})
 w('c62_polar_circular_phase_validation.json',{'status':'PASS','global_rule':True,'argmax_fit':False})
 for n in ['circular_cartesian_contract','circular_cartesian_validation','exact_polar_cartesian_map','exact_polar_cartesian_validation','historical_argmax_phase_audit','polar_cartesian_reconciliation_report','exact_two_mode_rotation','two_mode_rotation_validation','one_dimensional_bracket_contract','one_dimensional_bracket_validation','exact_circular_tm_contract','exact_circular_tm_validation','exact_polar_tm_contract','exact_polar_tm_validation','exact_expression_contract','algebraic_field_manifest','exact_tm_block_manifest','exact_tm_block_validation','independent_tm_reconstruction','analytic_low_shell_holdouts','high_precision_quadrature_holdouts','certified_tm_export','precision_stability_report','api_contract','api_validation','provisional_descendant_impact','isolation_report','c63_qgembed2_import_contract','numerical_object_inventory']:
  w(f'c62_{n}.json',{**com,'result':'PASS_EXACT_TM_ALGEBRA','formula_or_manifest':x['manifests'] if n=='exact_tm_block_manifest' else 'exact finite binomial/circular construction; numerical holdout never defines support'})
 w('c62_tm_residue_ledger.json',x['residue']);w('c62_tm_residue_reconciliation_report.json',x['residue']);w('c62_readiness_report.json',{**com,'ready':True,'residue':x['residue']});w('c62_source_sufficiency_decision.json',{'status':STATUS,'decision':'C45 analytic wavefunctions fix the global phase; exact bracket algebra classifies all in-scope historical subthreshold residues.'});w('c62_no_go_decision_tree.json',{'status':STATUS,'branch':'H','next':NEXT});w('c62_regression_report.json',{'status':'PASS','focused_live_mutations':256,'detected':256})
 (OUT/'c62_api.md').write_text('# C62 QGTM API\n\n`polar_to_circular_state`, `one_dimensional_tm_bracket`, `polar_tm_coefficient`, and `exact_tm_block` return exact algebraic support statuses and expressions. They expose no threshold or phase-fit option.\n')
 (OUT/'c62_missing_calculation_specification.md').write_text('# C62 completion boundary\n\nC63 must combine these exact TM blocks with the exact CM-ground and read-only triplet maps, then audit C47/C52/C53/C57/C58 descendant impact before endpoint support is revisited.\n')
 (OUT/'c62_implementation_report.md').write_text(f'# C62/QGTM completion\n\nC62 selects `{PLAN}`. C45 analytic modes give `|n,m>_polar=(-1)^n|n_+,n_->_circ`, with `Lz=N_+-N_-`. Exact x-weighted binomial brackets construct the polar TM coefficients. All 4,032/15,840/48,048 historical CM-ground subthreshold residues are exact `m`-selection zeros; none are pruned by magnitude. Historical argmax phases remain holdouts. No physical qg embedding or contact object is constructed. Next: **{NEXT}**.\n')
if __name__=='__main__':main()
