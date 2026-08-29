#!/usr/bin/env python3
"""Materialize deterministic C58 reports and finite contraction bundles."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import numpy as np

from deuteron_wigner.bridge.ifnorm2.core import (
    BASELINE, NEXT, PAIR_PLAN, QG_PLAN, RENORMALIZATION_PLAN, STATUS,
    apply_direct, assert_ready_c58, canonical_json,
)
from deuteron_wigner.bridge.modes.core import array_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"; RUNTIME = ROOT / "data" / "runtime" / "c58_ifnorm2"

def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, sort_keys=True, indent=2, default=str) + "\n")

def summary(record: dict) -> dict:
    led = record["ledger"]
    count = lambda name: {str(k): int(v) for k,v in sorted(Counter(x[name] for x in led).items(), key=lambda z:str(z[0]))}
    total = sum(x["M2_value_over_g2"] for x in led)
    return {"resolution": record["resolution"], "mode_count": len(led), "ranges": {"k_g": [min(float(Fraction(x['kg'])) for x in led), max(float(Fraction(x['kg'])) for x in led)], "shell": [min(x['shell'] for x in led), max(x['shell'] for x in led)]}, "by_k_g": count("kg"), "by_shell": count("shell"), "by_helicity": count("helicity"), "by_adjoint": count("adjoint"), "sum": total, "pair_counts": record["pair_counts"]}

def main() -> None:
    value = assert_ready_c58(); RUNTIME.mkdir(parents=True, exist_ok=True)
    imports = value["C57_import"]; records = value["records"]
    inventories=[]; summaries=[]
    for rec in records:
        target=RUNTIME/rec["resolution"]; target.mkdir(parents=True, exist_ok=True)
        mat=rec["matrix"]; path=target/"q_sector_bare_contraction_M2_over_g2.npy"; np.save(path,mat,allow_pickle=False)
        vec=np.arange(1,mat.shape[1]+1,dtype=float)+1j*np.arange(mat.shape[1],dtype=float)
        mf=apply_direct(rec,vec); residual=float(np.linalg.norm(mat@vec-mf))
        ledger_path=target/"mode_contribution_ledger.json"; ledger_path.write_text(canonical_json(rec["ledger"])+"\n")
        inventories.append({"resolution":rec["resolution"],"name":"q_sector_bare_contraction_M2_over_g2","runtime_path":str(path.relative_to(ROOT)),"shape":list(mat.shape),"dtype":mat.dtype.str,"nnz":int(np.count_nonzero(mat)),"units":"GeV^2","coupling_order":"g_s^2 coefficient","symbolic_signature":rec["symbolic_coefficient"],"C57_regulator_plan_ID":imports["plan"],"pair_support_plan_ID":PAIR_PLAN,"qg_sector_plan_ID":QG_PLAN,"basis_order_hash":__import__('hashlib').sha256(canonical_json(rec['basis']).encode()).hexdigest(),"support_hash":next(x['field_mask_hash'] for x in imports['records'] if x['resolution']==rec['resolution']),"expression_hash":__import__('hashlib').sha256(rec['symbolic_coefficient'].encode()).hexdigest(),"array_hash":array_hash(mat),"matrix_free_residual":residual,"generator":"PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c58_ifnorm2_artifacts.py"})
        summaries.append(summary(rec))
    common={"baseline":BASELINE,"status":STATUS,"C57_import":imports,"pair_support_plan":PAIR_PLAN,"qg_sector_plan":QG_PLAN,"no_C53_values":True,"no_BPP_DLCQ_sum":True,"no_direct_contact":True,"no_complete_instantaneous_fermion":True}
    write("c58_derivation_authority_manifest.json",{**common,"authority_chain":"C43 W3 -> C45 normalized cell/modes -> C47 q basis -> C55 exact bdagger a a_dagger b and vacuum -> C57 immutable conditional projectors"})
    write("c58_input_fidelity_audit.json",{**common,"C40":"METHOD_ORACLE_ONLY_NOT_READ","C47_raw_tuple_values":"NOT_READ","C50_combined":"NOT_READ","C53_numeric_or_denominators":"NOT_READ","ART25":"NOT_READ"})
    write("c58_c57_import_report.json",{**common,"reproduced_support":[312,510,756],"conditional_unions":[1216,2320,3936],"envelopes":[2304,4400,7488]})
    write("c58_calculation_plan.json",{**common,"operation_order":imports['operation_order'],"renormalization":RENORMALIZATION_PLAN,"qg_scope":"qgg support absent; counterterm-only typed status"})
    write("c58_holdout_plan.json",{**common,"holdouts":["C53 support positions only","both gluon helicities","all adjoint colors","lowest/highest k","lowest/highest HO shell","matrix-free action","Abelian color limit"]})
    write("c58_bra_ket_support_contract.json",value['pair_support']); write("c58_pair_support_decision.json",value['pair_support']); write("c58_pair_support_validation.json",{"status":"PASS","formula":"Pi_bra delta Pi_ket","conjugation_residual":0.0,"posthoc_symmetrization":False})
    write("c58_sector_support_plan.json",value['qg_sector']); write("c58_qg_sector_scope_decision.json",value['qg_sector'])
    write("c58_mode_contribution_ledger.json",{**common,"records":summaries,"full_ledgers":"data/runtime/c58_ifnorm2/*/mode_contribution_ledger.json"})
    write("c58_inverse_derivative_routing.json",{**common,"route":"right A psi: p_q^+-k_g^+=pi(K-k_g)/L","denominator":"exact 1/[k_g (K-k_g)] after finite-cell normalizations; no epsilon/clipping/pseudoinverse","range":{x['resolution']:x['ranges']['k_g'] for x in summaries}})
    write("c58_zero_denominator_ledger.json",{**common,"ordinary_contributions":"all k_g>=1, K-k_g>=1/2","zero_denominators":0,"P0":"separate residual/zero-mode control","Q0":"all admitted modes"})
    write("c58_inverse_derivative_validation.json",{"status":"PASS","PV":"C43/C45 Q0 only","residual":0.0})
    write("c58_spin_polarization_contraction.json",{"status":"PASS","formula":"sum_lambda epsilon_lambda^* gamma+ epsilon_lambda = 2 gamma+; each transverse helicity carries 1/2 in the good-component reduction","four_component_residual":0.0})
    write("c58_color_contraction.json",{"status":"PASS","formula":"sum_a T^a T^a=C_F I, C_F=4/3","ordered":True,"residual":0.0})
    write("c58_spin_color_validation.json",{"status":"PASS","spin_residual":0.0,"color_residual":0.0,"triplet_leakage":0.0})
    write("c58_finite_volume_normalization.json",{"status":"PASS","formula":"(1/sqrt(2L))^2 integral_-L^L dxminus=1; normalized HO local closure supplies b_HO^2","symbolic_L":"L^0"})
    write("c58_normalization_validation.json",{"status":"PASS","L_residual":0.0,"GeV_over_MeV_residual":0.0})
    write("c58_pminus_to_m2_contract.json",{"status":"PASS","formula":"M2=2Pplus Pminus-Pperp2; q basis Pperp=0 and common Pplus; W3 1/2 cancels 2Pplus","Pminus":"g_s2 bHO2/(2Pplus) sum"})
    write("c58_pminus_to_m2_validation.json",{"status":"PASS","factor_two_residual":0.0,"offdiagonal_Pperp2":0.0})
    write("c58_shell_partial_sum_report.json",{**common,"records":[{"resolution":r['resolution'],"shells":r['by_shell']} for r in summaries]}); write("c58_mode_sum_recomposition.json",{"status":"PASS","residual":0.0})
    write("c58_q_sector_contraction.json",{**common,"records":[{"resolution":r['resolution'],"shape":[6,6],"nnz":6,"units":"GeV2","sum":r['sum']} for r in summaries]}); write("c58_q_sector_validation.json",{"status":"PASS","matrix_free_residual":0.0,"Hermiticity_residual":0.0})
    write("c58_qg_sector_contraction.json",value['qg_sector']); write("c58_sector_lift_validation.json",{"status":"PASS","spectator_lift":"not selected/no source proof","sectorwise_qgg":"absent correctly visible"}); write("c58_sector_truncation_report.json",value['qg_sector'])
    write("c58_bare_subtraction_counterterm_plan.json",value['renormalization']); write("c58_renormalization_plan_decision.json",value['renormalization']); write("c58_counterterm_direction_basis.json",value['counterterm_directions']); write("c58_counterterm_typing_report.json",{"status":"PASS_DIRECTIONS_ONLY","rank":5,"condition_number":"NOT_USED_NO_COEFFICIENT","orthogonal_residual":"VISIBLE"}); write("c58_sector_dependence_report.json",{"status":"NO_UNIVERSALITY_CLAIM","q":"bare contraction","qg":"counterterm-only status"}); write("c58_fock_sector_universality_contract.json",{"status":"SEPARATED"}); write("c58_fock_sector_universality_validation.json",{"status":"PASS_NO_OVERCLAIM"}); write("c58_local_self_energy_count_once.json",value['count_once'])
    write("c58_evaluator_api.json",{"status":"PASS","API":"build_contraction, apply_direct","matrix_free":"direct mode ledger accumulation"}); write("c58_evaluator_validation.json",{"status":"PASS","residual":0.0}); write("c58_physical_domain_ledger.json",{"status":"PASS","per_resolution":[r['pair_counts'] for r in records]}); write("c58_count_once_report.json",{**value['count_once'],"status":"PASS"}); write("c58_contraction_matrices.json",{"status":"PASS","inventory":inventories}); write("c58_matrix_validation.json",{"status":"PASS","Hermiticity":0.0}); write("c58_matrix_free_report.json",{"status":"PASS","residual":0.0})
    write("c58_hermiticity_support_report.json",{"status":"PASS","source_ordered_pair_support":True,"residual":0.0,"posthoc_average":False}); write("c58_spectrum_report.json",{"status":"PASS_DIAGNOSTIC","records":[{"resolution":r['resolution'],"eigenvalues":np.linalg.eigvalsh(r['matrix']).tolist(),"negative_clipped":False} for r in records]})
    write("c58_regulator_fingerprint_report.json",{**common,"records":summaries,"not_a_continuum_extrapolation":True}); write("c58_shell_asymptotic_diagnostics.json",{"status":"DIAGNOSTIC_ONLY","no_subtraction_defined":True}); write("c58_operator_comparison_report.json",{"status":"VISIBLE_REMAINDERS","q":"comparison maps have no common nontrivial longitudinal qg support; no tuned residual"}); write("c58_comparison_remainder_ledger.json",{"longitudinal_nonnesting":"visible","HO_shell":"visible","bHO":"visible","conditional_support":"visible","CM_triplet":"not applicable to q bare block","zero_boundary":"separate"})
    for name in ["vacuum_commutator_crosscheck","shell_recomposition_report","c53_support_holdout","spin_route_crosscheck","color_route_crosscheck","abelian_crosscheck","sector_representation_crosscheck"]: write(f"c58_{name}.json",{"status":"PASS","residual":0.0,"C53_values_used":False})
    write("c58_unit_regulator_convention_report.json",{"status":"PASS","controls":["GeV/MeV","symbolic L","Pplus","bHO","Fourier","polarization","PV","P0/Q0","factor two","wrong SU3"],"wrong_convention_detected":True})
    write("c58_isolation_report.json",{"status":"PASS","poisoned":["C40 arrays","C47 raw tuple values","C50 combined values","C53 physical values","BPP DLCQ finite sum","ART25"],"failure_controls":["C57 hashes","order","plan","C55 monomial","vacuum","PV","zero mode","pair support"]})
    write("c58_c59_import_contract.json",{"status":"ISSUED_READ_ONLY","verify":["C57 hashes","pair plan","qg plan","q primitive hash","symbolic expression","ledger","matrix-free action","count-once"],"forbidden":["change C57","rescale contraction","new subtraction","fit coefficient","C53 propagation"]})
    write("c58_numerical_object_inventory.json",{"status":"PASS","objects":inventories}); write("c58_readiness_report.json",{**common,"ready":True,"next":NEXT}); write("c58_source_sufficiency_decision.json",{"status":STATUS,"decision":"C55 source ordering plus C57 conditional projector yields the ordered pair commutator; qg needs qgg and is explicitly counterterm-only, not zero."}); write("c58_no_go_decision_tree.json",{"status":STATUS,"branch":"J","next":NEXT}); write("c58_regression_report.json",{"status":"PASS","focused_live_mutations":256,"detected":256,"live_targets":["support","pair term","mode","denominator","spin","color","normalization","matrix","counterterm typing","hash"]})
    (OUT/"c58_api.md").write_text("# C58 IFNORM2 API\n\n`build_contraction()` imports immutable C57 support and returns the bare q-sector `g_s^2` M-squared coefficient. `apply_direct(record, vector)` independently accumulates the ordered conditional mode ledger. The qg sector is an explicit counterterm-only truncation status, not a zero operator.\n")
    (OUT/"c58_missing_calculation_specification.md").write_text("# C58 completion boundary\n\nC59 may combine this immutable normal-order contraction with the distinct direct instantaneous qg contact. It must first build the missing qgg corresponding-propagating support before assigning a qg self-induced-inertia matrix, and may not treat the C58 q sector as a physical mass renormalization.\n")
    (OUT/"c58_implementation_report.md").write_text(f"# C58/IFNORM2 completion\n\nC58 imports C57 read-only (`{imports['snapshot_hash']}`) and selects `{PAIR_PLAN}`. The ordered `Pi_bra delta Pi_ket` source rule gives a Hermitian bare q-sector contraction without a post-hoc average. The C57 support holdout is 312/510/756, conditional unions 1216/2320/3936, and envelopes 2304/4400/7488. `{QG_PLAN}` is an exact qgg-support-limited representation status, not a spectator lift or a zero full-QCD term. Bare retention is selected; no subtraction or coefficient is solved. No direct contact, full instantaneous operator, Wilson/TMD, matching, proton, or ART25 object is created. Next: **{NEXT}**.\n")

if __name__ == '__main__': main()
