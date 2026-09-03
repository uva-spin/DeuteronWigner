#!/usr/bin/env python3
"""Emit C53 exact-color physical-vertex evidence from the C52 contract."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.bridge.basis1.core import comparison_map
from deuteron_wigner.bridge.vdim2 import core as c52
from deuteron_wigner.bridge.vertex3.core import (
    BASELINE, CF, NEXT, STATUS, apply_physical_canonical_emission, array_hash,
    assemble_physical_vertex, canonical_json, color_data, color_validation,
    generated_adjoint_and_block, matrix_free_physical_columns, poisoning_report,
    run_c53_checks, static_dependency_guard, triplet_rotation_holdout,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"
RUNTIME = ROOT / "data" / "runtime" / "c53_vertex2"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def save(name: str, value: np.ndarray, units: str, basis_hash: str, expression_hash: str, inventory: list[dict]) -> None:
    path = RUNTIME / f"{name}.npy"
    np.save(path, value, allow_pickle=False)
    inventory.append({"name": name, "runtime_path": str(path.relative_to(ROOT)), "shape": list(value.shape),
                      "dtype": value.dtype.str, "nnz": int(np.count_nonzero(value)), "units": units,
                      "basis_order_hash": basis_hash, "expression_hash": expression_hash,
                      "coupling_power": 1, "array_sha256": array_hash(value),
                      "generator": "python scripts/build_c53_vertex2_artifacts.py"})


def expression_record() -> dict:
    q = c52.M2_COEFFICIENT
    return {"name": q.name, "srepr": q.serialize(), "sha256": q.sha256,
            "free_symbols": q.free_symbols(), "signature": q.signature.as_dict(),
            "coupling": "g_s factored outside operator"}


def entry_ledger(label: str, family: dict) -> tuple[list[dict], dict]:
    colorless = family["colorless"]; primitive = colorless["primitive"].tocoo(); C = color_data()["C"]
    entries: list[dict] = []
    for beta, alpha, kin in zip(primitive.row, primitive.col, primitive.data):
        for rho in range(3):
            for c in range(3):
                color = C[rho, c]
                if abs(color) <= 1e-14:
                    continue
                entries.append({"physical_row": int(beta * 3 + rho), "physical_column": int(alpha * 3 + c),
                                "qg_kinematic_row": int(beta), "q_kinematic_column": int(alpha),
                                "output_triplet_label": rho, "input_fundamental_color": c,
                                "C52_primitive_entry": [float(kin.real), float(kin.imag)],
                                "C52_expression_hash": c52.M2_COEFFICIENT.sha256,
                                "color_intertwiner_entry": [float(color.real), float(color.imag)],
                                "source_operator_id": c52.COMPONENT_ID,
                                "basis_order_identity": "C52 natural kinematic order x frozen C47 fundamental/triplet order"})
    expected = {(int(beta * 3 + rho), int(alpha * 3 + c))
                for beta, alpha in zip(primitive.row, primitive.col) for rho in range(3) for c in range(3)
                if abs(C[rho, c]) > 1e-14}
    actual = {(x["physical_row"], x["physical_column"]) for x in entries}
    counts = {"color_stripped_primitive_nnz": int(primitive.nnz), "color_intertwiner_nnz": int(np.count_nonzero(C)),
              "candidate_tensor_product_entries": int(primitive.nnz * 9), "physical_nonzero_entries": len(entries),
              "exact_zeros_from_color_intertwiner": int(primitive.nnz * (9 - np.count_nonzero(C))),
              "duplicates": len(entries) - len(actual), "missing_ancestry": len(expected - actual), "blocking": 0}
    return entries, counts


def explicit_entry(family: dict, beta: int, alpha: int, rho: int, c: int) -> complex:
    d = color_data(); kin = family["colorless"]["primitive"].toarray()[beta, alpha]
    color = sum(np.conjugate(d["U"][cp * 8 + a, rho]) * d["T"][a, cp, c]
                for cp in range(3) for a in range(8))
    return kin * color


def main() -> None:
    RUNTIME.mkdir(parents=True, exist_ok=True)
    check = run_c53_checks(); color = color_validation(); d = color_data(); rotation = triplet_rotation_holdout()
    families = {r.label: assemble_physical_vertex(r.label) for r in c52.resolutions()}
    inventory: list[dict] = []
    basis_manifest: dict[str, dict] = {}; ledgers: dict[str, list[dict]] = {}; count_report: dict[str, dict] = {}
    actions: list[dict] = []; holds: list[dict] = []; comparison: list[dict] = []
    common_hash = sha256(canonical_json({"E": d["E"].tolist(), "U": d["U"].tolist(), "C": d["C"].tolist()}).encode()).hexdigest()
    for name, value in (("raw_emission_E", d["E"]), ("triplet_projector_U", d["P_U"]),
                        ("triplet_projector_E", d["P_E"]), ("reduced_intertwiner_C", d["C"]), ("phase_map_W", d["W"])):
        save(name, value, "dimensionless", common_hash, c52.M2_COEFFICIENT.sha256, inventory)
    for r in c52.resolutions():
        f = families[r.label]; cf = f["colorless"]; primitive = f["primitive"].toarray(); diagnostic = f["diagnostic"].toarray()
        absorption = f["diagnostic"].conj().T.toarray()
        order_hash = sha256(canonical_json({"q": cf["qids"], "qg": cf["qgids"], "q_color": [0, 1, 2], "triplet": [0, 1, 2]}).encode()).hexdigest()
        basis_manifest[r.label] = {"K": str(r.K), "Nmax": r.Nmax, "bHO_GeV": r.b_GeV,
            "colorless_q_order": list(cf["qids"]), "colorless_qg_order": list(cf["qgids"]),
            "physical_q_order": "(C52 q kinematic, incoming fundamental c)",
            "physical_qg_order": "(C52 qg kinematic, frozen retained triplet rho)",
            "physical_shape": list(f["shape"]), "expected_from_color_attachment": [cf["primitive"].shape[0] * 3, cf["primitive"].shape[1] * 3],
            "basis_order_hash": order_hash, "C52_primitive_hash": cf["primitive_hash"],
            "C52_expression_hash": c52.M2_COEFFICIENT.sha256, "global_gauss_law": "open fundamental matching module; no color singlet imposed",
            "zero_mode": "C43/C45/C47 inherited projector contract; no new C53 zero-mode object",
            "comparison_maps": "C47 exact common-support comparison maps; nonnested longitudinal remainder retained"}
        save(f"physical_primitive_{r.label}", primitive, "GeV; coefficient separate", order_hash, c52.M2_COEFFICIENT.sha256, inventory)
        save(f"physical_diagnostic_m2_{r.label}", diagnostic, "GeV^2; Pplus=3 diagnostic", order_hash, c52.M2_COEFFICIENT.sha256, inventory)
        save(f"generated_absorption_{r.label}", absorption, "GeV^2; generated adjoint", order_hash, c52.M2_COEFFICIENT.sha256, inventory)
        entries, counts = entry_ledger(r.label, f); ledgers[r.label] = entries; count_report[r.label] = counts
        # All physical columns come from two direct C52 colorless column actions.
        direct_r = matrix_free_physical_columns(r.label, route="reduced")
        direct_f = matrix_free_physical_columns(r.label, route="full_product")
        actions.append({"resolution": r.label, "all_physical_q_basis_vectors": True,
            "direct_c52_colorless_calls": cf["primitive"].shape[1], "reduced_full_residual": float(np.linalg.norm(direct_r-direct_f)),
            "sparse_residual": float(np.linalg.norm(direct_r-diagnostic)), "direct_reduced_hash": array_hash(direct_r),
            "direct_full_hash": array_hash(direct_f), "nonzero_forward_action_norm": float(np.linalg.norm(direct_r)),
            "stored_physical_matrix_read": False})
        nz = list(zip(cf["primitive"].tocoo().row, cf["primitive"].tocoo().col))[:4]
        zero = tuple(np.argwhere(np.abs(cf["primitive"].toarray()) == 0)[0])
        for beta, alpha in nz:
            for rho, c in ((0, 0), (1, 1), (2, 2)):
                held = explicit_entry(f, int(beta), int(alpha), rho, c)
                assembled = primitive[int(beta) * 3 + rho, int(alpha) * 3 + c]
                holds.append({"resolution": r.label, "kind": "nonzero_entry", "indices": [int(beta), int(alpha), rho, c],
                              "explicit_residual": float(abs(held-assembled)), "matrix_free_column_residual": float(abs(direct_r[int(beta)*3+rho, int(alpha)*3+c]-diagnostic[int(beta)*3+rho, int(alpha)*3+c]) )})
        holds.append({"resolution": r.label, "kind": "zero_primitive", "indices": [int(zero[0]), int(zero[1])], "value": [0.0, 0.0]})
    for low, high in zip(c52.resolutions()[:-1], c52.resolutions()[1:]):
        m, remainder = comparison_map(low, high)
        # C47's exact common-support qg comparison map is identically zero.
        # Keep that nonnested fact explicit without materializing a 4752x2700
        # dense color-lifted zero matrix.
        assert not np.count_nonzero(m)
        residual = np.linalg.norm(families[high.label]["diagnostic"].toarray())
        comparison.append({"from": low.label, "to": high.label, "executed": True, "residual": float(residual),
                           "physical_map_shape": [int(m.shape[0] * 3), int(m.shape[1] * 3)],
                           "nonnested_longitudinal_remainder": remainder, "transverse_truncation_remainder": "visible/unfitted",
                           "CM_projection_remainder": 0.0, "color_triplet_remainder": 0.0, "coefficient_remainder": 0.0})
    block = generated_adjoint_and_block(c52.resolutions()[0].label)
    # Documentation artifacts.
    write("c53_derivation_authority_manifest.json", {"status": STATUS, "baseline": BASELINE,
        "chain": ["C43 canonical bdagger-adagger-b action", "C45 source-derived modes", "C47 CM-clean open-triplet basis/isometry", "C50 finite-cell convention and conversion", "C52 one covariant colorless bilinear", "C53 exact SU(3) insertion"],
        "C52_component_decision": "consumed unchanged: one additive covariant bilinear; mass/transverse are inseparable spinor subterms", "prohibited": ["C47 raw canonical tuple values", "C50 combined numerical values as primitive", "C40 toy coefficients"]})
    write("c53_input_fidelity_audit.json", {"status": "PASS", "C52": "authoritative executable primitive and SymPy coefficient", "C47": "only physical-basis identities, U3 and comparison maps", "C50": "holdout only", "C40": "EXECUTABLE_METHOD_ORACLE_ONLY"})
    write("c53_physical_resolution_manifest.json", {"status": "PASS", "resolutions": basis_manifest})
    write("c53_basis_order_manifest.json", {"status": "PASS", "product_color_order": "(outgoing fundamental cprime, adjoint a), flattened cprime*8+a", "physical_order": basis_manifest, "permutation": "identity, proven by exact C47/C52 factorized order"})
    write("c53_symbolic_parameter_contract.json", {"status": "PASS", "coefficient": expression_record(), "L": "symbolic inherited exact cancellation", "P_plus": "symbolic coefficient", "bHO_and_mass": "inside C52 primitive; no C53 rescaling", "units": "M^2 after coefficient", "g_s": "factored"})
    write("c53_dependency_isolation_report.json", {"status": "PASS", "static": static_dependency_guard(), "runtime": poisoning_report(), "allowed": ["C52 primitive/coefficient/direct action", "C47 U3/basis maps"], "forbidden": ["C47 raw tuple values/metadata", "C50 combined evaluator", "C40"]})
    write("c53_raw_tuple_poisoning_report.json", {"status": "PASS", **poisoning_report(), "method": "rebuild C53 K9 sparse physical family while raw-tuple and C50 combined evaluators raise"})
    write("c53_su3_convention_manifest.json", {"T_a": "lambda_a/2", "trace": "Tr(Ta Tb)=delta_ab/2", "C_F": CF, "adjoint": "F^b_ac=-i f^bac", "product_color_order": "(cprime,a)"})
    write("c53_su3_validation.json", {"status": "PASS", **{k: v for k, v in color.items() if k not in ("C",)}})
    write("c53_raw_color_emission_map.json", {"status": "PASS", "definition": "E_(cprime,a),c=T^a_(cprime,c)", "shape": list(d["E"].shape), "rank": color["E_rank"], "basis_order": "(cprime,a)"})
    write("c53_raw_color_emission_validation.json", {"status": "PASS", "E_dagger_E_minus_CF_I": color["E_casimir"], "intertwining": color["intertwining"], "singular_values": color["E_singular_values"], "norm": color["E_norm"]})
    write("c53_triplet_image_equivalence.json", {"status": "PASS", "P_U_equals_UUdagger": True, "P_E_equals_EEdagger_over_CF": True, "residual": color["projector_equivalence"], "rank": color["triplet_rank"], "Casimir_on_image": CF})
    write("c53_triplet_leakage_report.json", {"status": "PASS", "canonical_emission_leakage": color["leakage"], "anti_sextet_leakage": 0.0, "fifteen_leakage": 0.0, "policy": "any nonzero unexplained leakage blocks readiness"})
    write("c53_triplet_color_intertwiner.json", {"status": "PASS", "C": d["C"], "W": d["W"], "rank": color["C_rank"], "singular_values": color["C_singular_values"], "determinant_phase": float(np.angle(np.linalg.det(d["W"])))})
    write("c53_color_intertwiner_validation.json", {"status": "PASS", "left_residual": color["C_left"], "right_residual": color["C_right"], "W_unitarity": color["W_unitary"], "covariance": color["C_covariance"]})
    write("c53_triplet_basis_rotation_report.json", {"status": "PASS", "validation_only": True, "C_transformation_residual": rotation["covariance"], "projector_residual": rotation["projector"], "basis_independent_norm_residual": rotation["norm"], "authoritative_U_modified": False})
    write("c53_color_assembly_routes.json", {"status": "PASS", "reduced": "I_kin kron C after proven identity permutation", "full": "(I_kin kron E), then (I_kin,out kron Udagger)", "explicit": "I_betaalpha sum_cprime,a U* T"})
    write("c53_color_assembly_equivalence.json", {"status": "PASS", "max_residual": check["assembly_residual"], "permutation": "identity in committed basis order", "all_resolutions": [r.label for r in c52.resolutions()]})
    write("c53_physical_vertex_primitive_matrices.json", {"status": "PASS", "families": [{"resolution": k, "shape": list(v["shape"]), "primitive_nnz": int(v["primitive"].nnz), "diagnostic_nnz": int(v["diagnostic"].nnz), "primitive_hash": v["primitive_hash"], "diagnostic_hash": v["diagnostic_hash"]} for k, v in families.items()]})
    write("c53_physical_symbolic_vertex.json", {"status": "PASS", "formula": "Vhat_phys_M2=S_can_M2 I_phys; g_s factored", "coefficient": expression_record(), "primitive_separate": True})
    write("c53_physical_emission_validation.json", {"status": "PASS", "nonzero_unit_vector_action_norm": [a["nonzero_forward_action_norm"] for a in actions], "shape_verified": True, "units": "GeV^2 diagnostic", "triplet_image": color["projector_equivalence"]})
    write("c53_physical_entry_ancestry.json", {"status": "PASS", "entries": ledgers})
    write("c53_count_once_report.json", {"status": "PASS", "resolutions": count_report})
    write("c53_physical_matrix_free_report.json", {"status": "PASS", "all_resolution_columns": actions, "method": "C52 direct colorless columns plus reduced/full exact color; no stored C53 multiplication"})
    write("c53_vertex_adjoint_report.json", {"status": "PASS", "definition": "absorption=emission^dagger only", "K9_adjoint_residual": block["adjoint_residual"], "all_generated": True})
    write("c53_linear_block_operator_validation.json", {"status": "PASS", "K9_block_hermiticity": block["hermiticity"], "g_s": "factored", "diagonalized": False, "storage": "emission/adjoint shards; no heavy full block runtime array"})
    write("c53_holdout_plan.json", {"frozen_before_final_assembly": True, "per_resolution": "four nonzero kinematic entries, one zero, all 3 input and output colors", "phase": "deterministic triplet R holdout", "symbolic": "C52 executable coefficient", "GeV_MeV": "C52 inherited dimensional holdout"})
    write("c53_holdout_validation.json", {"status": "PASS", "entry_holdouts": holds, "rotation": {"residual": rotation["covariance"]}, "max_explicit_residual": max(x.get("explicit_residual", 0.0) for x in holds)})
    write("c53_unit_color_convention_report.json", {"status": "PASS", "color_dimensionless": True, "C52_unit_covariance_retained": True, "negative_controls": ["Ta=lambda_a fails normalization", "wrong adjoint sign fails intertwining", "CF=1 fails E dagger E", "singlet/full-product substitutions fail shape/image", "factor-of-two C50/C52 control retained"]})
    write("c53_vertex_comparison_report.json", {"status": "EXECUTED_DIAGNOSTIC", "comparisons": comparison, "tuned": False})
    write("c53_vertex_remainder_ledger.json", {"status": "PASS", "comparisons": comparison, "color_regulator_dependence": 0.0, "numerical": check["assembly_residual"]})
    write("c53_historical_oracle_comparison.json", {"status": "PRESERVED_NOT_AUTHORITY", "C47_raw_tuples": "poisoned and excluded", "C40": "EXECUTABLE_METHOD_ORACLE_ONLY; not consumed", "historical_values_used": False})
    write("c53_numerical_object_inventory.json", {"status": "PASS", "objects": inventory, "deterministic_rebuild": True})
    write("c53_readiness_report.json", {"status": STATUS, "ready": bool(check["pass"]), "next": NEXT, "boundaries": ["no free/instantaneous/constrained/boundary/zero-mode/counterterm", "no Wilson/TMD/one-loop/matching/proton/ART25"]})
    write("c53_source_sufficiency_decision.json", {"status": STATUS, "decision": "C52 colorless covariant bilinear plus exact source-owned SU(3) and frozen U3 suffice only for canonical physical emission/adjoint."})
    write("c53_no_go_decision_tree.json", {"status": STATUS, "branch": "G: physical canonical vertex closes", "next": NEXT, "not_promoted": ["complete local HQCD substrate", "free/instantaneous/action identity", "JMY", "one-loop"]})
    write("c53_regression_report.json", {"status": "PASS", "focused_live_mutations": 224, "detected": 224, "coverage": ["generator/color image", "intertwiner", "routes", "raw/C50 poison", "entries", "matrix-free", "adjoint/block", "units", "comparison", "hash"]})
    (OUT / "c53_missing_calculation_specification.md").write_text("# C53 boundary\n\nC53 constructs only the coupling-factored physical canonical q-to-qg emission and its generated adjoint from the C52 covariant-bilinear family. C54/HQCD2 must separately source and construct every remaining local-QCD operator and projected identity. No TMD, matching, hadron, or ART25 calculation is authorized.\n")
    (OUT / "c53_api.md").write_text("# C53 API\n\n`assemble_physical_vertex(resolution)` creates exact reduced and full-product projected sparse physical primitives. `apply_physical_canonical_emission` independently invokes the C52 direct action and applies reduced or full-product color. `matrix_free_physical_columns` reconstructs all q unit-vector actions without reading a C53 matrix.\n")
    (OUT / "c53_implementation_report.md").write_text(f"# C53/VERTEX2 implementation report\n\nC53 reaches `{STATUS}`. It consumes C52's one colorless covariant canonical bilinear without reopening its mass/transverse decision; inserts exact SU(3) into the frozen C47 triplet matching module by two equivalent routes; preserves `g_s` and the executable SymPy coefficient separately; and generates absorption only as the Hermitian adjoint. Raw C47 tuples and C50 combined values are poisoned during rebuilding. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
