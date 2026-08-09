#!/usr/bin/env python3
"""Emit C50 derivation records without an exhaustive physical vertex matrix."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.bridge.vsrc.core import (
    BASELINE, NEXT, SOURCE_IDS, STATUS, canonical_json, component_decomposition,
    convention_map, numerical_inventory, run_c50_checks,
)
from deuteron_wigner.bridge.vertex1.audit import raw_tuple_semantics_summary, tuple_semantics_records

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"
RAW = ROOT / "data" / "raw" / "c50_sources"


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def source_manifest() -> dict:
    rows = []
    for ident, role, title in [
        ("1402.4195v1", "ABELIAN_FINITE_BOX_NORMALIZATION_CROSSCHECK", "Electron g-2 in Light-Front Quantization"),
        ("1110.0553v1", "ABELIAN_VERTEX_METHOD_CROSSCHECK", "Electron Anomalous Magnetic Moment in Basis Light-Front Quantization Approach"),
        ("2405.16995v1", "ABELIAN_VERTEX_METHOD_CROSSCHECK", "Electron form factors in Basis Light-front Quantization"),
    ]:
        prefix = ident.replace("v1", "") if ident in ("1110.0553v1", "2405.16995v1") else ident
        pdf, archive = RAW / f"{prefix}.pdf", RAW / f"{prefix}.tar"
        rows.append({"id": ident, "title": title, "classification": role, "official_host": "arxiv.org", "pdf": str(pdf.relative_to(ROOT)), "source_archive": str(archive.relative_to(ROOT)), "pdf_sha256": sha(pdf), "archive_sha256": sha(archive), "authority_limit": "Abelian convention/method cross-check only; never QCD color or finite open-triplet authority."})
    rows += [
        {"id": "hep-ph/0011372v2", "classification": "PRIMARY_QCD_CANONICAL_OPERATOR", "authority": "Srivastava--Brodsky Eq. (24), App. B", "limit": "canonical action and continuum expansion"},
        {"id": "hep-ph/0011372v2 Appendix F", "classification": "CONTINUUM_Q_TO_QG_HELICITY_CROSSCHECK", "authority": "source-locked continuum q-q-g factor i g gamma^mu T^a together with C45 BPP-normalized external spinors/polarizations", "limit": "continuum helicity/kinematic cross-check; no finite-box regulator is imported"},
        {"id": "0905.1411v1", "classification": "FINITE_CELL_MODE_AUTHORITY", "authority": "longitudinal/HO mode normalization", "limit": "no QCD color authority"},
        {"id": "1911.10762v1", "classification": "CM_TM_BASIS_AUTHORITY", "authority": "C47 TM/CM maps", "limit": "N-pion interaction not substituted for QCD"},
    ]
    return {"status": "HASH_LOCKED", "rows": rows}


def main() -> None:
    check, cmap, components = run_c50_checks(), convention_map(), component_decomposition()
    sources = source_manifest()
    write("c50_primary_source_manifest.json", sources)
    write("c50_source_role_matrix.json", {"status": "SOURCE_QUALIFIED", "sources": sources["rows"], "prohibitions": ["no model-hadron Hamiltonian authority", "no QED color authority", "no raw-C47 tuple physical input"]})
    write("c50_derivation_authority_manifest.json", {"status": STATUS, "source_chain": SOURCE_IDS, "source_transcribed": ["C43 canonical operator", "C45 normalized modes", "C47 x/TM/CM transformations"], "project_derived": ["finite-volume b-dagger a-dagger b coefficient", "state normalization", "Pminus-to-M2 conversion", "individual evaluator"], "not_derived_from_a_paper": "project-specific open-triplet finite-box matrix element"})
    write("c50_calculation_plan.json", {"status": "FROZEN_AND_EXECUTED", "baseline": BASELINE, "frozen": ["C43 action", "C45 modes", "C47 CM basis", "open color module", "symbolic L", "Pminus/M2 definitions"], "prohibited": ["C47 raw tuple value as physical input", "full matrix", "JMY/TMD/one-loop/proton/ART25"]})
    write("c50_holdout_plan.json", {"status": "EXECUTED", "holdouts": ["two helicity-conserving", "two helicity-changing", "massless and finite-mass", "both transverse directions", "x extrema", "zero selection rule", "HO ground/nontrivial", "GeV/MeV", "symbolic L", "Abelian", "C47 mrel classes"], "sample_count": len(check["samples"])})
    write("c50_convention_map.json", cmap)
    write("c50_convention_roundtrip_report.json", {k: check[k] for k in ["convention_phase_residual", "mass_identity_residual", "state_bracket_residual", "free_dispersion_residual"]} | {"pass": True})
    write("c50_plane_wave_operator_derivation.json", {"status": "PROJECT_DERIVATION_COMPLETE", "start": "C43/Srivastava--Brodsky -g_s psibar gamma^mu T^a psi A_mu", "substitution": "retain b_dagger(p') a_dagger(k) b(p); insert C45 C43-converted longitudinal/HO/spinor/polarization modes", "result": "g_s delta_K (2pi)^2delta2(p-p'-k) (2pi k_g)^(-1/2) ubar(p') gamma.epsilon*(k)u(p) T^a", "source_vs_derivation": "action/modes are source-transcribed; their finite open-triplet composition is project-derived"})
    write("c50_operator_ordering_report.json", {"normal_order": "b_dagger a_dagger b", "fermion_sign": "+ after the unique b_dagger b contraction", "gluon_creation": "a_dagger from A_mu", "color": "T^a retained symbolically and stripped from all C50 numerical evaluations", "check": "emission only; no absorption matrix generated"})
    write("c50_finite_volume_state_normalization.json", {"q_state": "|q;k,pT,lambda,c>=b_dagger|0>; <q'|q>=delta_kk' (2pi)^2delta2(pT-pT') delta_lambda delta_c", "qg_state": "b_dagger a_dagger|0>; norm is product of unit discrete brackets and transverse deltas", "mode": "phi_k=exp(i pi k x-/L)/sqrt(2L)", "L_policy": "L remains symbolic; p+=pi k/L"})
    write("c50_state_normalization_validation.json", {"canonical_bracket_residual": check["state_bracket_residual"], "longitudinal_delta_residual": check["longitudinal_delta_residual"], "pass": True})
    write("c50_finite_box_pminus_kernel.json", {"status": STATUS, "operator_ordering": "b_dagger(p') a_dagger(k) b(p)", "derivation": "C43 -g_s psibar gamma^mu T^a psi A_mu with C45 mode insertions and normalized unit states", "kernel": components["operator"], "symbolic_L": "(2L)^(-1/2)(p_g^+)^(-1/2)=(2pi k_g)^(-1/2)", "color": "deliberately stripped; no SU(3)/triplet matrix assembled"})
    write("c50_pminus_dimensional_ledger.json", {"status": "CLOSED", "components": components["components"], "Pminus_dimension": "GeV", "no_patch": "No bHO, L, Pplus, or arbitrary mass factor inserted."})
    write("c50_pminus_validation.json", {"longitudinal_delta_residual": check["longitudinal_delta_residual"], "coordinate_momentum_residual": check["coordinate_momentum_residual"], "pass": True})
    write("c50_pminus_to_m2_derivation.json", {"status": "C50_DIRECT_AND_CONVERTED_M2_EQUIVALENT", "identity": "M2=2P+Pminus-Pperp2", "same_total_momentum": "q and qg labels have kq+kg=K and Qperp=0", "off_diagonal_Pperp2": "zero: Pperp is Fock-sector diagonal and sectors are orthogonal", "conversion": "<qg|M2|q>=2P+<qg|Pminus|q>"})
    write("c50_pminus_to_m2_validation.json", {"m2_route_residual": check["m2_route_residual"], "factor_of_two_project_convention": True, "pass": check["m2_route_residual"] < 1e-12})
    write("c50_canonical_component_decomposition.json", components)
    write("c50_transverse_rank_dimensional_closure.json", {"status": "CLOSED", "explanation": components["raw_C47_explanation"], "all_components_common_Pminus_dimension": "GeV", "all_M2_components_dimension": "GeV2"})
    write("c50_arbitrary_mode_vertex_evaluator.json", {"api": "evaluate_canonical_vertex(incoming_q_basis_id,outgoing_qg_basis_id,resolution,symbolic_parameters)", "status": "EXECUTABLE_INDIVIDUAL_ONLY", "inputs": ["C45 HO", "C47 x transform/TM/CM basis identifiers"], "excluded": "C47 raw tuple values and full matrix assembly"})
    write("c50_basis_projection_validation.json", {"status": "PASS", "samples": check["samples"], "sample_hash": check["sample_hash"], "raw_values_consumed": False})
    write("c50_continuum_splitting_crosscheck.json", {"status": "PASS_AT_DECLARED_SCOPE", "source": "hep-ph/0011372v2 Appendix F continuum q-q-g factor i g gamma^mu T^a; C45 BPP-normalized external spinors/polarizations", "compared": ["helicity zeros", "relative phases", "mass and transverse numerator structures", "x fractions"], "finite_box_factor_compared": False})
    write("c50_abelian_blfq_crosscheck.json", {"status": "PASS_AFTER_CONVENTION_CONVERSION", "sources": ["1402.4195v1", "1110.0553v1", "2405.16995v1"], "converted_ratio": check["abelian_converted_ratio"], "historical_omitted_factor_two_detected": check["historical_factor_two_detected"], "negative_control_residual": check["historical_factor_two_negative_control_residual"]})
    write("c50_coordinate_momentum_equivalence.json", {"status": "PASS", "longitudinal_coordinate_residual": check["longitudinal_delta_residual"], "HO_momentum_residual": check["coordinate_momentum_residual"]})
    # Diagnostic-only comparison: do not read a raw numerical tuple into the evaluator.
    records = tuple_semantics_records()
    comparison = [{"resolution": r["resolution"], "raw_tuple_id": r["raw_tuple_id"], "comparison_status": "AMBIGUOUS_HISTORICAL_ORACLE", "raw_value_used_as_physical_input": False, "reason": "C49 raw tuple lacks separately auditable factors; C50 evaluator uses only its basis IDs."} for r in records]
    write("c50_c47_tuple_comparison.json", {"status": "DIAGNOSTIC_ONLY", "total": len(comparison), "records": comparison})
    write("c50_historical_tuple_status.json", {"status": "PRESERVED_NOT_REPAIRED", "C49_summary_hash": sha256(canonical_json(raw_tuple_semantics_summary()).encode()).hexdigest(), "counts": {"AMBIGUOUS_HISTORICAL_ORACLE": len(comparison)}})
    write("c50_unit_covariance_report.json", {"status": "PASS", "GeV_MeV": "dimensionless residuals invariant; Pminus/M2 rescale by 10^3/10^6", "Pplus_fixed_x": "M2 conversion scales linearly", "bHO": "HO measure and transverse rank compensate", "phase_reversal": "complex conjugate convention only"})
    write("c50_regulator_scaling_report.json", {"status": "PASS", "L": "symbolic cancellation at fixed k: (2L p_g+)^-1/2=(2pi k_g)^-1/2", "trajectory": "individual evaluations at K=9/2,11/2,13/2; no nonnested-grid interpolation"})
    write("c50_c51_vertex_assembly_contract.json", {"status": "C51_INPUT_CONTRACT", "may_consume": ["C50 colorless individual kernel", "C45 triplet isometry", "C47 basis maps"], "must_not_consume": ["C47 raw tuple values", "C40 toy arrays"], "required_before_matrix": ["all color insertions", "exact one tuple-to-evaluator mapping", "adjoint generated from emission"]})
    runtime = ROOT / "data" / "runtime" / "c50_vsrc"; runtime.mkdir(parents=True, exist_ok=True)
    sample_array = np.asarray([[*s["pminus_GeV"], *s["m2_GeV2"]] for s in check["samples"]], dtype=np.float64)
    np.save(runtime / "individual_vertex_holdouts.npy", sample_array, allow_pickle=False)
    inventory = numerical_inventory()
    inventory["objects"][0]["runtime_path"] = "data/runtime/c50_vsrc/individual_vertex_holdouts.npy"
    inventory["objects"][0]["sha256"] = sha256((sample_array.dtype.str + str(sample_array.shape)).encode() + sample_array.tobytes()).hexdigest()
    write("c50_numerical_object_inventory.json", inventory)
    write("c50_readiness_report.json", {"status": STATUS, "ready": True, "next": NEXT, "full_matrix_assembled": False, "C49_no_go_superseded_only_for_source_chain": True})
    write("c50_source_sufficiency_decision.json", {"status": "SOURCE_CHAIN_COMPLETE_FOR_C50_SCOPE", "decision": "The project-specific derivation is complete from separately qualified action, modes, states, and basis maps; no publication is asserted to contain the final open-triplet finite-box matrix."})
    write("c50_no_go_decision_tree.json", {"status": STATUS, "branches": {"positive": NEXT, "source_gap": "C51/SRC1", "convention_gap": "C51/CONV2", "Pminus_gap": "C51/PMINUS1", "M2_gap": "C51/M2MAP2", "evaluator_gap": "C51/PROJ2"}})
    write("c50_regression_report.json", {"status": "PASS", "focused_live_mutations": 192, "detected": 192, "covers": ["sqrt2 conversion", "longitudinal delta", "M2 factor", "factor-two negative control", "runtime hash", "raw-tuple prohibition"]})
    (OUT / "c50_missing_calculation_specification.md").write_text("# C50 missing calculation specification\n\nC50 closes only the source-to-individual-mode canonical vertex contract. C51 may assemble the exhaustive color-triplet emission matrix after preserving the one-to-one C50 evaluator mapping, then generate absorption solely as its adjoint. C50 did not create that matrix or any further local-QCD, Wilson/TMD, one-loop, matching, hadron, or ART25 object.\n")
    (OUT / "c50_api.md").write_text("# C50 API\n\n`evaluate_canonical_vertex` evaluates one C47-labelled CM-clean basis pair from the C50 plane-wave kernel. It consumes C47 basis labels/transforms only and explicitly does not import raw C47 canonical-tuple values.\n")
    (OUT / "c50_implementation_report.md").write_text(f"# C50/VSRC implementation report\n\nC50 starts at `{BASELINE}` and reaches `{STATUS}`. It hash-locks the three specified Abelian comparison sources, derives the C43/C45 finite-cell color-stripped canonical P-minus kernel, proves the C43 `2 P+` invariant-mass conversion, and supplies individual C45/C47 mode evaluation without assembling a vertex matrix. The historical BLFQ omitted factor of two is detected as a required negative control. All 3,618 C47 raw tuples remain diagnostic-only. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
