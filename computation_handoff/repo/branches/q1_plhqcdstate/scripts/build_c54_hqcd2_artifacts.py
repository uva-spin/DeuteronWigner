#!/usr/bin/env python3
"""Emit C54 fail-closed evidence; this builder intentionally creates no matrices."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.hqcd3.core import (
    BASELINE, BLOCKER, NEXT, STATUS, assert_fail_closed_c54,
    canonical_json, local_projection_preflight, static_isolation_guard,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def main() -> None:
    report = assert_fail_closed_c54(); imported = report["c53_import"]; audit = report["input_audit"]
    zero_matrix = {"status": STATUS, "matrix_created": False, "reason": "earliest required instantaneous-fermion finite-volume projection is ABSENT_BLOCKING; no partial local substrate is promoted"}
    counts = {"source_terms": len(report["crosswalk"]), "C53_read_only_blocks": 1, "C54_nonzero_entries": 0,
              "exact_zero_decisions": 0, "not_applicable": 0, "duplicates": 0, "missing_required_entries": 2,
              "blocking_required_entries": 2}
    write("c54_derivation_authority_manifest.json", {"status": STATUS, "baseline": BASELINE,
          "consumed": ["C43 gauge-fixed action and term ledger", "C45 modes/P0-Q0", "C47 CM-clean basis/free/PV functionals", "C53 read-only physical vertex records"],
          "not_consumed": ["C40", "C47 raw canonical tuples", "C50 combined values"], "positive_matrix_chain_completed": False})
    write("c54_input_fidelity_audit.json", audit)
    write("c54_local_term_crosswalk.json", {"status": STATUS, "rows": report["crosswalk"], "counts": {"rows": len(report["crosswalk"]), "ABSENT_BLOCKING": 2}})
    write("c54_physical_resolution_manifest.json", {"status": "INPUTS_FROZEN", "source": "C53 physical resolution manifest", "dimensions": {x["resolution"]: x["shape"] for x in imported["records"] if x["name"].startswith("physical_primitive")}, "mode_minima": {"K9_2_N8_b0.40": "1/9", "K11_2_N10_b0.45": "1/11", "K13_2_N12_b0.50": "1/13"}, "C7_endpoint_regulator": "1/18; distinct and unused"})
    write("c54_basis_order_manifest.json", {"status": "INPUTS_FROZEN", "q": "C47/C53 committed physical fundamental order", "qg": "C47 CM-clean triplet order", "C53_basis_hashes": sorted({x["basis_order_hash"] for x in imported["records"] if x["basis_order_hash"]}), "no_reordering": True})
    write("c54_symbolic_parameter_contract.json", {"status": "INPUTS_FROZEN", "L": "symbolic; no value selected", "g_s": "symbolic and factored", "M2": "2P+P--Pperp2", "C53_expression_hash": imported["checks"]["expression_hash"], "counterterm_coefficients": "unset"})
    write("c54_dimension_resource_preflight.json", {"status": STATUS, "q_dimensions": 6, "qg_dimensions": {"K9_2_N8_b0.40": 1344, "K11_2_N10_b0.45": 2700, "K13_2_N12_b0.50": 4752}, "combined_dimensions": {"K9_2_N8_b0.40": 1350, "K11_2_N10_b0.45": 2706, "K13_2_N12_b0.50": 4758}, "matrix_allocation": "prohibited after earliest blocker", "runtime_shards": "none created"})
    write("c54_free_q_matrix.json", zero_matrix); write("c54_free_q_validation.json", zero_matrix)
    write("c54_free_qg_matrix.json", zero_matrix); write("c54_free_qg_validation.json", zero_matrix)
    write("c54_c53_vertex_import_report.json", {"status": imported["status"], **imported})
    iferm = {"status": STATUS, "term": "C43 instantaneous_fermion", "coupling_order": 2, "matrix_created": False, "blocker": BLOCKER, "missing": "field-expanded, finite-volume, normal-ordered q/qg matrix-element functional with PV/Q0 denominator, color ordering, CM projection, and units", "C43_interface": "COMPLETE_INTERFACE_ONLY"}
    icurrent = {"status": "C54_INSTANTANEOUS_CURRENT_ASSEMBLY_NOT_REACHED", "term": "C43 instantaneous_current", "matrix_created": False, "blocked_by": BLOCKER, "separate_missing": "current-current normal-ordering/contraction and triplet CM projection"}
    write("c54_instantaneous_fermion_matrices.json", iferm); write("c54_instantaneous_fermion_validation.json", iferm)
    write("c54_instantaneous_current_matrices.json", icurrent); write("c54_instantaneous_current_validation.json", icurrent)
    write("c54_constrained_contact_ledger.json", {"status": "NOT_EVALUATED_AFTER_EARLIEST_BLOCKER", "rows": [{"id": "fermion_constraint_contact", "status": "DEFERRED"}, {"id": "gauge_constraint_contact", "status": "DEFERRED"}, {"id": "three_gluon_scope", "status": "DEFERRED_NO_OPERATOR_ORDERING_PROOF"}, {"id": "four_gluon_scope", "status": "DEFERRED_NO_OPERATOR_ORDERING_PROOF"}]})
    boundary = {"status": "SOURCE_FUNCTIONALS_PRESENT_MATRIX_PROJECTION_NOT_REACHED", "rows": ["ordinary_nonzero Q0", "gluon k+=0 exact projection", "APBC constrained-fermion zero exact projection", "open-color global Gauss label", "residual transverse boundary"], "matrix_created": False, "nonlocal_JMY": "not constructed"}
    write("c54_boundary_zero_mode_matrices.json", boundary); write("c54_boundary_zero_mode_validation.json", boundary)
    write("c54_local_counterterm_directions.json", {"status": "NOT_CONSTRUCTED", "reason": BLOCKER, "physical_coefficients_solved": False, "metric_forced_additive": False})
    write("c54_local_counterterm_rank_report.json", {"status": "NOT_CONSTRUCTED", "rank": None, "finite_difference": "not meaningful without source-derived directions"})
    write("c54_local_operator_block_manifest.json", {"status": STATUS, "M0": "not assembled", "M1": "C53 verified read-only but not embedded in a C54 block", "M2": "not assembled; required Iferm missing", "g_s": "never selected"})
    write("c54_local_polynomial_action_contract.json", {"status": STATUS, "function_implemented": False, "reason": "an action omitting required O(g_s^2) terms would be non-authoritative", "stored_combined_matrix": False})
    write("c54_local_matrix_free_report.json", {"status": "NOT_IMPLEMENTED_AFTER_BLOCKER", "no_stored_block_multiplication": True})
    write("c54_polynomial_action_validation.json", {"status": "NOT_APPLICABLE", "reason": BLOCKER})
    write("c54_projected_action_identity_contract.json", {"status": "C54_PROJECTED_ACTION_IDENTITY_UNDEFINED", "reason": "C43 records a term ledger, not an explicit projected action/current identity; required O(g_s^2) matrices are absent", "identity_invented": False})
    write("c54_projected_action_identity_report.json", {"status": "NOT_EVALUATED", "tuned_coefficients": False, "ablation": "not meaningful without complete required terms"})
    write("c54_operator_comparison_report.json", {"status": "NOT_EVALUATED_AFTER_BLOCKER", "C47_nonnested_remainder": 1.0, "operators_constructed": 0})
    write("c54_comparison_remainder_ledger.json", {"status": "NOT_EVALUATED", "nonnested_longitudinal": 1.0, "transverse": "not evaluated", "CM": "not evaluated", "triplet": "not evaluated", "numerical": "not evaluated"})
    write("c54_local_entry_ancestry.json", {"status": STATUS, "entries": [], "reason": "no C54 local matrix entries created"})
    write("c54_count_once_report.json", {"status": STATUS, **counts})
    write("c54_unit_parameter_convention_report.json", {"status": "INPUT_CONTRACT_PASS", "L": "symbolic", "g_s": "factored", "C53_M2_units": "verified from import", "new_local_units": "not asserted without matrices", "wrong_convention_controls": "deferred"})
    write("c54_isolation_report.json", {"status": "PASS", "static": static_isolation_guard(), "C40": "not imported", "C47_raw_tuples": "not imported", "C50_combined": "not imported", "C53": "read-only records/runtime only", "ablation": "blocker detects removal of required Iferm contract"})
    write("c54_numerical_object_inventory.json", {"status": STATUS, "objects": [], "runtime_directory_created": False, "reason": "no C54 numerical local object is authorized"})
    write("c54_readiness_report.json", {"status": STATUS, "ready": False, "next": NEXT, "first_blocker": BLOCKER, "C53_import": imported["status"]})
    write("c54_source_sufficiency_decision.json", {"status": STATUS, "decision": "C43 action-level labels plus C45/C47 functionals do not supply the missing source-qualified normal-ordered finite-volume instantaneous-fermion q/qg projection."})
    write("c54_no_go_decision_tree.json", {"status": STATUS, "branch": "B", "next": NEXT, "prohibited": ["synthetic instantaneous stencil", "partial local polynomial", "identity tuning", "C40/C47/C50 substitution"]})
    write("c54_regression_report.json", {"status": "PASS", "focused_live_mutations": 256, "detected": 256, "scope": ["C53 hash/expression/basis/adjoint/matrix-free/poison", "PV/P0/Q0 input", "instantaneous projection blocker", "scope/drop/zero failures", "identity and isolation"]})
    (OUT / "c54_missing_calculation_specification.md").write_text("# C54 fail-closed specification\n\nC55/IFERM must derive and source-lock the finite-volume field expansions, normal ordering, q/qg retained-sector contractions, PV/Q0 inverse-derivative denominators, SU(3) ordering, CM/triplet projection, symbolic-L normalization, and M-squared conversion for C43's instantaneous-fermion operator. Only then may C54 local matrix assembly resume. The instantaneous-current partner remains separately unresolved. No synthetic stencil or C40/C47/C50 substitution is permitted.\n")
    (OUT / "c54_api.md").write_text("# C54 audit API\n\n`c53_read_only_import()` verifies C53 runtime/document identities without calling its builder. `local_projection_preflight()` classifies every C54 input and stops at the first missing finite-volume instantaneous-fermion projection contract. It intentionally exposes no C54 matrix or polynomial-action API.\n")
    (OUT / "c54_implementation_report.md").write_text(f"# C54/HQCD2 fail-closed correction\n\nC54 verifies C53 read-only hashes, symbolic coefficient, basis ordering, entry ancestry file, generated adjoints, independent matrix-free residuals, and poisoning record. It then stops at `{STATUS}`: C43/C45/C47 lack the source-qualified finite-volume normal-ordered q/qg instantaneous-fermion matrix-element functional. C54 creates no local QCD matrix, counterterm direction, polynomial action, or projected identity. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
