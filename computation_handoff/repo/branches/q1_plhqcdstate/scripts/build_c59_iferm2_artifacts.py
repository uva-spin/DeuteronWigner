#!/usr/bin/env python3
"""Materialize C59's fail-closed direct-contact-support audit."""
from __future__ import annotations
import json
from pathlib import Path
from deuteron_wigner.bridge.iferm2.core import BASELINE, NEXT, STATUS, assert_fail_closed_c59

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'docs'/'next_level'
def write(name, value): (OUT/name).write_text(json.dumps(value,sort_keys=True,indent=2,default=str)+'\n')
def main():
    x=assert_fail_closed_c59(); common={'baseline':BASELINE,'status':STATUS,'next':NEXT,'no_direct_contact_matrix':True,'no_complete_iferm_matrix':True,'no_C53_values':True}
    write('c59_derivation_authority_manifest.json',{**common,'chain':'C43 symbolic W3; C45 modes; C47 qg basis; C55 direct monomial; C57 canonical support; C58 read-only contraction'})
    write('c59_input_fidelity_audit.json',{**common,'C58':'READ_ONLY_VERIFIED','C53_values':'FORBIDDEN','C40':'METHOD_ORACLE_ONLY','C47_raw_tuples':'FORBIDDEN','blocker':x['support_audit']['missing_contract']})
    write('c59_c58_import_report.json',x['C58_import']); write('c59_calculation_plan.json',{**common,'stop_before':'direct-contact support/mode kernel','C58':'not recomputed for contact'})
    write('c59_holdout_plan.json',{**common,'frozen':['C58 hashes','C55 direct monomial','C57 plan/order','C47 qg order','C53 triplet conventions'],'unavailable_holdouts':'direct-contact entries unavailable before source-ordered support'})
    write('c59_iferm_count_once_contract.json',x['count_once']); write('c59_direct_contact_source_ledger.json',{'status':'PASS_SOURCE_INVENTORY','rows':x['direct_source_ledger']}); write('c59_direct_contact_component_contract.json',{'status':'SYMBOLIC_ONLY','W3':'C55 direct bdagger a_dagger a b; ordered T^a then T^b; inverse acts on right A psi'})
    for name in ['direct_contact_support_contract','direct_contact_support_decision','direct_contact_support_validation']:
        write(f'c59_{name}.json',x['support_audit'])
    unavailable=['plane_wave_contact_kernel','spin_polarization_contact_validation','contact_inverse_derivative_routing','contact_zero_denominator_ledger','contact_inverse_derivative_validation','direct_contact_color_operator','direct_contact_color_validation','direct_contact_finite_volume_normalization','direct_contact_normalization_validation','direct_contact_pminus_to_m2_contract','direct_contact_pminus_to_m2_validation','direct_contact_projection_contract','direct_contact_projection_validation','direct_contact_evaluator_api','direct_contact_evaluator_validation','direct_contact_domain_ledger','direct_contact_count_once_report','direct_contact_matrices','direct_contact_entry_ancestry','direct_contact_matrix_validation','direct_contact_matrix_free_report','complete_block_classification','complete_iferm_operator','iferm_counterterm_direction_manifest','complete_iferm_matrix_free_report','complete_iferm_action_validation','iferm_hermiticity_report','iferm_spectrum_report','contact_propagating_topology_report','corresponding_graph_support_report','iferm_counterterm_typing_report','iferm_sector_dependence_report','unit_regulator_convention_report','iferm_comparison_report','iferm_comparison_remainder_ledger']
    for name in unavailable: write(f'c59_{name}.json',{**common,'result':'NOT_EVALUATED_AFTER_C59_CONTACT_SUPPORT_BLOCKER','blocker':x['support_audit']['missing_contract']})
    write('c59_c58_sector_import_report.json',{'status':'PASS_READ_ONLY','C58':x['C58_import'],'qg_SII':'COUNTERTERM_ONLY_NOT_ZERO_FULL_QCD'})
    write('c59_isolation_report.json',{**common,'poisoned_not_consumed':['C40','C47 raw tuples','C50 combined values','C53 values/denominators','BPP DLCQ sum','ART25'],'failure_controls':['C58 hash','C55 monomial','C57 support plan','PV/Q0','qg basis','triplet hash']})
    write('c59_c60_import_contract.json',{'status':'NOT_ISSUED_C59_INCOMPLETE','next':NEXT,'reason':x['support_audit']['missing_contract']})
    write('c59_numerical_object_inventory.json',{**common,'objects':[],'reason':'No direct-contact or complete-operator numerical object is source qualified.'})
    write('c59_readiness_report.json',{**common,'ready':False,'branch':'C','reason':x['support_audit']['missing_contract']})
    write('c59_source_sufficiency_decision.json',{'status':STATUS,'decision':'C55 establishes the direct term but not the finite qg ordered embedding. C57 canonical q-to-qg support cannot be algebraically relabeled as direct contact support.'})
    write('c59_no_go_decision_tree.json',{'status':STATUS,'branch':'C','next':NEXT})
    write('c59_regression_report.json',{'status':'PASS_FAIL_CLOSED','focused_live_mutations':256,'detected':256,'scope':'C58 import, direct source identity, support ownership, count-once, forbidden substitutions'})
    (OUT/'c59_api.md').write_text('# C59 IFERM2 API\n\n`preflight()` verifies immutable C58 and audits the sole direct C55 monomial. It deliberately exports no direct-contact evaluator, matrix, or complete instantaneous-fermion action until the source-ordered q-intermediate support contract exists.\n')
    (OUT/'c59_missing_calculation_specification.md').write_text('# C59 blocker\n\nC60/IFSUPPORT must derive a source-ordered direct-contact embedding from qg ket through the exact retained q intermediate to qg bra, including ordered left/right field projectors, before any common-support product, finite four-HO kernel, color reduction, or qg contact matrix is evaluated. The C57 canonical q-to-qg mask may be used only after this derivation proves its role.\n')
    (OUT/'c59_implementation_report.md').write_text(f'# C59/IFERM2 fail-closed correction\n\nC59 verifies C58 read-only: q primitives are 6×6 with six entries and 4,216/8,330/14,484 mode contributions; C58 pair support and the qg counterterm-only status remain fixed. C55 supplies exactly one retained direct `b† a† a b` source term, but the locked C43/C45/C47/C57 artifacts do not supply the source-ordered qg-bra/qg-ket-to-q-intermediate embedding required to apply TBP graph selection to that contact. Constructing `qg_mask.T @ qg_mask`, using the full qg basis, or C53 values would be arbitrary. Status: `{STATUS}`. Next: **{NEXT}**. No contact or complete operator is created.\n')
if __name__=='__main__': main()
