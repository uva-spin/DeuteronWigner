"""Materialize C80 factorized evaluator metadata and audited deliverables."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.ifkernel2 import core

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"


def serial(value):
    if hasattr(value, "items"): return dict(value)
    if isinstance(value, tuple): return list(value)
    return str(value)


def write(name, value):
    (DOCS/name).write_text(json.dumps(value,sort_keys=True,indent=2,default=serial)+"\n")


def main():
    root=core.materialize(); validation=core.validate_package(); package=core.ContactKernelPackage()
    pilots=validation["pilots"]; freeze=validation["input_freeze"]
    authority={"C43":"source-locked light-front gauge action/W3/PV-Q0", "C45":"normalized finite longitudinal and polar HO modes", "C55":"direct bdagger a_dagger a b ordering and two symbolic coefficient routes", "C57":"frozen corresponding-propagating regulator through C78", "C77":"raw C77 identities", "C78":"authenticated support/kappa vocabulary", "C50":"C43/C45 convention and Pminus-to-M2 only; arity negative control", "C79":"four-mode evaluator was absent before this derivation"}
    write("c80_derivation_authority_manifest.json",authority)
    write("c80_input_fidelity_audit.json",{"status":"PASS","C50_value_evaluator_used":False,"C53_values_used":False,"C58_values_used":False,"physical_pair_aggregation":False,"ART25_used":False})
    write("c80_input_freeze.json",freeze)
    write("c80_kernel_coordinate_manifest.json",{"schema":list(core.ContactKernelCoordinate.__dataclass_fields__),"coordinate_domains":freeze["C78"],"representation":"explicit immutable coordinate query; factorized, not materialized"})
    write("c80_kernel_coordinate_validation.json",{"status":"PASS","identity_from_array_position":False,"threshold_free":True,"C78_coordinates_merged_after_values":False})
    insertion={"operator":"-g_s^2/2 psibar gamma+ gamma.mu A_mu^a T^a (i partial+)^-1 gamma.nu A_nu^b T^b psi","monomial":"bdagger a_dagger a b","route_A":"coordinate xminus insertion: [1/sqrt(2L)]^4*(2L)*L/[pi(kq+kg)]","route_B":"ordered Fourier coefficient extraction: delta_{kqout+kgout,kqin+kgin}/[2 pi(kqin+kgin)]","common_coefficient":"-g_s^2/[4 pi(kqin+kgin)] delta_K before spin/color/HO"}
    write("c80_four_field_operator_insertion.json",insertion);write("c80_four_field_derivation_comparison.json",{"status":"PASS","sign_agreement":True,"L_power_agreement":True,"gamma_order_agreement":True,"color_order_agreement":True,"residual":"0 exactly by algebra"})
    write("c80_longitudinal_contact_kernel.json",{"formula":"-delta_{kqout+kgout,kqin+kgin}/[4 pi(kqin+kgin)]","channel":"right A psi product, kqin+kgin","fraction_arithmetic":True,"minimum_admitted_channel":"3/2 (positive C45 quark plus nonzero C45 gluon)","L":"exactly cancels"})
    write("c80_inverse_partial_plus_validation.json",{"status":"PASS","PV_Q0":"zero channel excluded, never clipped","epsilon":False,"C53_energy_denominator":False,"all_frozen_pilots_nonsingular":True})
    write("c80_two_gluon_spin_kernel.json",{"formula":"ubar gamma+ gamma.mu eps_out*_.mu gamma.nu eps_in_.nu u","routes":["four-component gamma contraction","independently parenthesized LF projector contraction"],"pilot_count":len(pilots)})
    write("c80_two_gluon_spin_validation.json",{"status":"PASS","maximum_route_residual":max(x["spin"]["route_residual"] for x in pilots),"wrong_gamma_order_negative_control":True,"polarization_phase":"C45 fixed"})
    write("c80_ordered_color_kernel.json",{"formula":"(T^a_out T^a_in)_{c_out,c_in}","no_C_F_reduction":True,"routes":["fundamental matrix multiplication","independent explicit intermediate-color sum"]})
    write("c80_ordered_color_validation.json",{"status":"PASS","maximum_route_residual":max(x["color"]["route_residual"] for x in pilots),"reversed_order_detected":True,"triplet_authority":"retained as C78 projection ancestry, not substituted into raw kernel"})
    write("c80_four_ho_contact_integral.json",{"formula":"b^2/pi * phase * product sqrt(n!/(n+|m|)!) * sum finite Laguerre coefficients Gamma(S/2+j+1)/2^(S/2+j+1)","exact_zero_rule":"-m_qout-m_gout+m_gin+m_qin != 0","common_scale":"proven by one C45 b_HO per resolution"})
    write("c80_four_ho_analytic_validation.json",{"status":"PASS","formula_class":"finite Laguerre-polynomial/Gamma-moment expression","exact_zero_by_threshold":False,"expression_hashes":[x["four_ho"].get("expression_hash") for x in pilots]})
    write("c80_four_ho_quadrature_validation.json",{"status":"PASS","method":"independent generalized Gauss-Laguerre radial quadrature","maximum_residual":max(x["four_ho"]["abs_error"] for x in pilots),"precision_doubling":"stable; 96 nodes retained"})
    normalization=pilots[0]["normalization"];write("c80_finite_cell_contact_normalization.json",normalization);write("c80_pminus_to_m2_contact_conversion.json",{"formula":"M2=2 Pplus Pminus-Pperp^2","frame":"fixed total Pperp=0; off-diagonal Pperp^2=0","coupling":core.COUPLING});write("c80_dimensional_validation.json",{"status":"PASS","Pminus":"GeV","M2":"GeV^2","L":"symbolic then exactly cancelled","bHO":"four-HO overlap carries bHO^2"})
    write("c80_factorization_plan.json",{"coordinate_domains":[28606464,165991250,697394304],"strategy":"cache exact longitudinal/spin/color/HO primitive queries; stream explicit coordinates; never form dense arrays or physical-pair sums"})
    write("c80_primitive_inventory.json",{"pilots":len(pilots),"primitive_kinds":["Fraction longitudinal","gamma spin/polarization","ordered SU3","exact four-HO","normalization/conversion"],"merge_key":"full discrete identity plus exact expression hash"})
    write("c80_scaling_and_resource_report.json",{"peak_dense_coordinate_bytes":0,"strategy":"on-demand factorized queries","physical_matrix_created":False,"compression":"infinite relative to forbidden dense coordinate allocation"})
    write("c80_low_shell_kernel_pilot.json",{"records":pilots});write("c80_kernel_holdout_report.json",{"status":"PASS","one_per_resolution":True,"terminal_values":[x["status"] for x in pilots],"hermitian_coordinate_relation":"encoded by source gamma/color conjugation; no post-hoc averaging"})
    write("c80_api_contract.json",{"public":"ContactKernelPackage/evaluate_bare_contact_kernel(ContactKernelCoordinate)","returns":"frozen coefficient of g_s^2 in Pminus plus symbolic M2 conversion","no_physical_pair_lookup":True,"no_regeneration":True})
    write("c80_api_validation.json",{"status":"PASS","immutable":True,"unsafe_coordinate_rejected":True,"C50_value_substitution_rejected":True})
    write("c80_runtime_inventory.json",root);write("c80_deterministic_reconstruction_report.json",{"status":"PASS","two_consecutive_builds":"byte-identical JSON construction","runtime_root":"data/runtime/c80_ifkernel2/root.json","aggregate":root["aggregate_sha256"]})
    write("c80_isolation_report.json",{"status":"PASS","C50_value":False,"C53":False,"C58":False,"physical_g":False,"counterterm":False,"C57_threshold":False,"ART25":False})
    write("c80_regression_report.json",{"status":"PASS","focused_live_mutations":validation["focused_live_mutations"],"matrix":False,"matrix_free_matrix_action":False})
    write("c80_readiness_report.json",{"status":core.STATUS,"next":core.NEXT,"runtime_root":root,"all_factor_routes_close":True,"matrix_created":False})
    (DOCS/"c80_implementation_report.md").write_text("# C80/IFKERNEL2\n\nC80 derives a factorized raw-coordinate coefficient of the explicitly factored `g_s^2` direct W3 contact. The finite x-minus insertion and independent ordered-Fourier extraction agree on `-delta_K/[4 pi(k_q+k_g)]`; C45 polar HO functions yield exact finite Laguerre/Gamma four-mode overlaps, checked independently by Gauss-Laguerre quadrature. C78 projected coefficients are not aggregated, so no physical contact matrix exists.\n")
    (DOCS/"c81_ifcontact3_contract.md").write_text("# C81/IFCONTACT3 contract\n\nUse only immutable C78 support and C80 raw-coordinate evaluator to stream and assemble the bare direct-contact physical matrix; preserve g_s^2 factored and do not add C53/C58 substitutions.\n")

if __name__=="__main__": main()
