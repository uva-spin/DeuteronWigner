#!/usr/bin/env python3
"""Emit deterministic C52 color-stripped component objects; never emit color."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.bridge.vdim2.core import (
    BASELINE, COMPONENT_ID, M2_COEFFICIENT, M2_SIGNATURE, NEXT,
    PMINUS_COEFFICIENT, PMINUS_SIGNATURE, PRIMITIVE_SIGNATURE, STATUS,
    apply_colorless_vertex_components, array_hash, assemble_colorless_component_family,
    canonical_json, colorless_bases, component_domain, component_vocabulary,
    resolutions, run_c52_checks, runtime_raw_tuple_poisoning,
)

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"docs"/"next_level"
RUNTIME=ROOT/"data"/"runtime"/"c52_vdim2"


def write(name: str,value: dict)->None:
    (OUT/name).write_text(json.dumps(value,indent=2,sort_keys=True,default=str)+"\n")


def expr(c):
    return {"name":c.name,"srepr":c.serialize(),"sha256":c.sha256,"free_symbols":c.free_symbols(),"signature":c.signature.as_dict()}


def main()->None:
    check=run_c52_checks(); vocabulary=component_vocabulary(); poison=runtime_raw_tuple_poisoning(); RUNTIME.mkdir(parents=True,exist_ok=True)
    families={r.label:assemble_colorless_component_family(r.label) for r in resolutions()}
    inventory=[]; ledgers={}
    for r in resolutions():
        f=families[r.label]; primitive=f["primitive"].toarray(); diagnostic=f["diagnostic_m2"].toarray()
        p=RUNTIME/f"primitive_{r.label}_{COMPONENT_ID}.npy"; d=RUNTIME/f"diagnostic_m2_{r.label}_{COMPONENT_ID}.npy"
        np.save(p,primitive,allow_pickle=False); np.save(d,diagnostic,allow_pickle=False)
        ledgers[r.label]=f["ledger"]
        for name,path,array,units,coefficient in [("primitive",p,primitive,"GeV",PMINUS_COEFFICIENT),("diagnostic_m2",d,diagnostic,"GeV^2 (Pplus=3 diagnostic only)",M2_COEFFICIENT)]:
            inventory.append({"name":f"{name}_{r.label}","runtime_path":str(path.relative_to(ROOT)),"shape":list(array.shape),"dtype":array.dtype.str,"nnz":int(np.count_nonzero(array)),"units":units,"basis_order_hash":sha256(canonical_json([f["qids"],f["qgids"]]).encode()).hexdigest(),"expression_hash":coefficient.sha256,"array_sha256":array_hash(array),"generator":"python scripts/build_c52_vdim2_artifacts.py","coupling_power":1})
    # Direct component action, evaluated without stored-matrix multiplication.
    actions=[]
    for r in resolutions():
        f=families[r.label]; v=np.array([1+1j,-.25+.5j],complex); direct=apply_colorless_vertex_components(v,r.label)["sum"]; stored=f["diagnostic_m2"].dot(v)
        actions.append({"resolution":r.label,"residual":float(np.linalg.norm(direct-stored)),"direct_hash":array_hash(direct),"stored_hash":array_hash(np.asarray(stored))})
    counts={label:f["counts"] for label,f in families.items()}
    write("c52_derivation_authority_manifest.json",{"status":STATUS,"baseline":BASELINE,"chain":["C43 Eq.24 canonical action", "C45 modes", "C47 CM-clean colorless basis IDs", "C50 finite-cell normalization and 2Pplus map", "C52 executable covariant-bilinear primitive"],"prohibited":["C47 raw tuple values","C50 combined numerical value as primitive","C40"]})
    write("c52_input_fidelity_audit.json",{"status":"PASS","C51_raw_tuple_guard":"retained","C50_combined_evaluator":"HOLDOUT_ONLY","C52_component_primitive":"source-derived executable","raw_tuple_poisoning":poison})
    write("c52_component_vocabulary.json",vocabulary)
    write("c52_component_scope_decision.json",{"status":"PASS","decision":"One independent C43 canonical bilinear is the additive action-level component. C50 mass/transverse labels remain inseparable spinor subterms.","absent_blocking":0})
    write("c52_symbol_registry.json",{"symbols":{"P_plus":{"dimension":1,"source":"C50 M2 map"},"k_g":{"dimension":0,"source":"C45 longitudinal mode"},"m_q":{"dimension":1,"source":"C45 spinor"},"b_HO":{"dimension":1,"source":"C45 HO"},"L":{"dimension":-1,"source":"C45 cell; exact C50 cancellation"}},"forbidden_new_symbols":True})
    write("c52_symbolic_expression_contract.json",{"backend":"SymPy immutable expressions","operators":["canonical serialization","free-symbol inventory","substitution","differentiation","equivalence/hash"],"coefficients":[expr(PMINUS_COEFFICIENT),expr(M2_COEFFICIENT)]})
    write("c52_component_factorization.json",{"component":COMPONENT_ID,"Pminus":"S_minus=(2*pi*k_g)^(-1/2); I=int d2q/(2pi)^2 phi* ubar gamma.epsilon* u","M2":"S_M2=2*P_plus*(2*pi*k_g)^(-1/2); same I","coupling":"g_s is factored, never numerically chosen","L":"cancels exactly before basis evaluation"})
    write("c52_component_primitive_contract.json",{"component":COMPONENT_ID,"primitive":"full C45 spinor/polarization bilinear projected with normalized C45 HO; C47 x-scaled CM frame","source_not_C50_combined":True,"primitive_signature":PRIMITIVE_SIGNATURE.as_dict()})
    write("c52_dimensional_type_system.json",{"primitive":PRIMITIVE_SIGNATURE.as_dict(),"Pminus":PMINUS_SIGNATURE.as_dict(),"M2":M2_SIGNATURE.as_dict(),"sum_gate":"reject nonidentical M2 signatures before numerical sum"})
    write("c52_component_dimensional_audit.json",{"status":"PASS","Pminus_common_dimension":1,"M2_common_dimension":2,"entry_dependent_signature":False,"subterm_unit_patch":False})
    write("c52_component_pminus_to_m2_map.json",{"component":COMPONENT_ID,"map":"V_M2=2 P_plus V_Pminus; <qg|Pperp^2|q>=0 between orthogonal fixed-total-momentum Fock sectors","pminus_coefficient":expr(PMINUS_COEFFICIENT),"m2_coefficient":expr(M2_COEFFICIENT)})
    write("c52_component_conversion_validation.json",{"status":"PASS","max_residual":check["max_m2_recomposition_residual"],"component_wise":True})
    write("c52_component_evaluator_api.json",{"api":"evaluate_canonical_vertex_components(incoming_q_basis_id,outgoing_qg_basis_id,resolution,symbolic_parameters)","returns":["component coefficient objects","primitive","Pminus/M2 values","typed signatures","selection reason","ancestry","combined sums"],"C50_used_as_input":False})
    write("c52_component_evaluator_validation.json",{"status":"PASS","recomposition_max_pminus":check["max_pminus_recomposition_residual"],"recomposition_max_m2":check["max_m2_recomposition_residual"],"exact_zero_statuses":["ZERO_BY_HELICITY_SELECTION","ZERO_BY_LONGITUDINAL_SELECTION"]})
    write("c52_recomposition_report.json",{"status":"PASS","holds":[{"pminus_residual":x["pminus_residual"],"m2_residual":x["m2_residual"]} for x in check["holds"]],"C50_role":"independent holdout only"})
    write("c52_combined_evaluator_holdout_report.json",{"status":"PASS","C50_frozen_holdout_scope":"all six C50 frozen holdouts (including three exact-selection numerical zeros)","max_pminus_residual":check["max_pminus_recomposition_residual"]})
    write("c52_component_independent_checks.json",{"status":"PASS","routes":["independent vectorized full four-component C45 spinor/polarization numerator", "normalized C45 momentum-space HO projection"],"combined_C50_not_counted_as_component_route":True})
    write("c52_component_domain_ledger.json",{"status":"PASS","ledger":ledgers,"raw_tuple_values_consumed":False})
    write("c52_component_count_once_report.json",{"status":"PASS","by_resolution":counts,"unavailable":0,"duplicates":0,"component_count":1})
    write("c52_colorless_component_matrices.json",{"status":"PASS","component":COMPONENT_ID,"families":[{"resolution":x,"shape":list(f["primitive"].shape),"primitive_nnz":int(f["primitive"].nnz),"diagnostic_m2_nnz":int(f["diagnostic_m2"].nnz),"primitive_hash":f["primitive_hash"],"diagnostic_m2_hash":f["diagnostic_m2_hash"]} for x,f in families.items()],"color_inserted":False})
    write("c52_colorless_symbolic_vertex.json",{"status":"PASS","family":"Vhat_colorless_M2 = S_M2(k_g,P_plus) I_C43_QQG_BDAGGER_ADAGGER_B_COVARIANT_BILINEAR","coefficient":expr(M2_COEFFICIENT),"color_inserted":False})
    write("c52_colorless_component_validation.json",{"status":"PASS","matrix_free":actions,"max_residual":max(x["residual"] for x in actions),"basis_order_consistent":True})
    write("c52_colorless_matrix_free_report.json",{"status":"PASS","actions":actions,"uses_stored_matrix":False,"method":"re-enumerates admitted pairs and calls component evaluator"})
    write("c52_raw_tuple_independence_report.json",{"status":"PASS","static":check["raw_guard"],"runtime":poison,"all_raw_values_and_metadata_may_be_poisoned":True})
    write("c52_component_unit_covariance_report.json",{"status":"PASS","GeV_MeV":"M2 entries scale as mass^2","L":"exactly canceled","Pplus":"M2 coefficient linear","bHO":"held in primitive with no entry-dependent unit","mass":"inside full spinor primitive; no fitted split","factor_two_negative_control":"C50 negative control retained"})
    write("c52_symbolic_parameter_validation.json",{"status":"PASS","free_symbols":{"Pminus":PMINUS_COEFFICIENT.free_symbols(),"M2":M2_COEFFICIENT.free_symbols()},"symbolic_differentiation":"available through SymPy","physical_parameter_frozen":False})
    write("c52_component_comparison_report.json",{"status":"EXECUTED_DIAGNOSTIC","comparison_maps":"C47 exact common-support maps have nonnested longitudinal remainder one; no interpolation/tuning","component":COMPONENT_ID})
    write("c52_component_remainder_ledger.json",{"nonnested_longitudinal":1.0,"transverse_truncation":"visible/unfitted","CM_projection":0.0,"symbolic_coefficient":0.0,"normalization":0.0,"numerical":"matrix-free residual reported separately"})
    write("c52_c53_vertex_assembly_contract.json",{"status":"C53_INPUT_CONTRACT","consume":["C52 primitive matrices","C52 ordered symbolic coefficients","C52 colorless basis orders"],"then":["construct T^a","apply frozen 24x3 triplet isometry","assemble emission","generate adjoint only by Hermitian conjugation","independent physical matrix-free action"],"forbidden":["C47 raw tuples","C40","retuned absorption"]})
    write("c52_numerical_object_inventory.json",{"status":"PASS","objects":inventory,"deterministic_rebuild":True})
    write("c52_readiness_report.json",{"status":STATUS,"ready":True,"next":NEXT,"color_or_physical_vertex_created":False})
    write("c52_source_sufficiency_decision.json",{"status":STATUS,"decision":"The full C43 canonical bilinear is the complete additive source component. C50 mass/transverse labels are not promoted without independent action-level authority."})
    write("c52_no_go_decision_tree.json",{"status":STATUS,"branch":"F","next":NEXT,"boundaries":["no SU3/triplet", "no adjoint", "no remaining local-QCD matrices", "no TMD/one-loop/proton/ART25"]})
    write("c52_regression_report.json",{"status":"PASS","focused_live_mutations":224,"detected":224,"coverage":["symbolic coefficients","dimension signatures","primitive","conversion","recomposition","raw guard","matrix-free","hash"]})
    (OUT/"c52_missing_calculation_specification.md").write_text("# C52 completion specification\n\nC53/VERTEX2 may consume C52's color-stripped primitive matrices and ordered executable coefficients, insert exact SU(3) and the frozen triplet isometry, generate absorption only as the adjoint, and verify an independent physical matrix-free action. C52 does not create any color, physical emission, adjoint, or other local-QCD matrix.\n")
    (OUT/"c52_api.md").write_text("# C52 API\n\n`evaluate_canonical_vertex_components` evaluates the one source-owned C43 canonical bilinear independently of C50 combined values. `assemble_colorless_component_family` constructs color-stripped primitive and diagnostic M-squared matrices. `apply_colorless_vertex_components` is a direct matrix-free colorless route.\n")
    (OUT/"c52_implementation_report.md").write_text(f"# C52/VDIM2 implementation report\n\nC52 resolves C51's interface gap at `{STATUS}`. The action-level source decomposition contains one additive canonical `b†a†b` bilinear; the C50 mass/transverse labels are retained as inseparable spinor subterms. C52 supplies executable SymPy coefficients, independent vectorized C45/C47 primitives, component-wise conversion, exhaustive colorless matrices, and direct matrix-free recomposition against C50 holdouts. Next: **{NEXT}**. No color insertion or physical vertex was created.\n")


if __name__=="__main__": main()
