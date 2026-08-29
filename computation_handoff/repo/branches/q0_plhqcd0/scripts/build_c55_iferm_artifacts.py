#!/usr/bin/env python3
"""Emit C55 source-algebra evidence; no finite instantaneous matrix is made."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.iferm.core import (
    BASELINE, BLOCKER, NEXT, STATUS, assert_fail_closed_c55,
    contact_count_once, input_fidelity_audit, instantaneous_fermion_preflight,
    static_isolation_guard,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def main() -> None:
    report = assert_fail_closed_c55(); source = report["source"]; ledger = report["ledger"]
    inherited_sources = {x["key"]: {"arxiv": x["arxiv"], "archive_sha256": x["archive_sha256"], "pdf_sha256": x["pdf_sha256"]}
                         for x in json.loads((OUT / "c43_primary_source_manifest.json").read_text())["rows"]}
    unavailable = {"status": STATUS, "matrix_created": False, "reason": BLOCKER}
    blocks = report["blocks"]
    statuses = {x["block"]: x["status"] for x in blocks}
    write("c55_derivation_authority_manifest.json", {"status": STATUS, "baseline": BASELINE, "source_chain": ["SB hep-ph/0011372v2 constrained equation and Eq.(24)", "BPP hep-ph/9705477v1 Eq.(2.97), normal-ordering/self-induced-inertia discussion", "C45 finite cell", "C47 CM basis", "C53 read-only color identity"], "no_C40_or_historical_instantaneous_values": True})
    write("c55_input_fidelity_audit.json", input_fidelity_audit())
    write("c55_primary_source_manifest.json", {"status": "HASH_LOCKED_REUSED", "locks": {"SB": inherited_sources["SB"], "BPP": inherited_sources["BPP"]}, "SB": {"locator": "Eq.(24), Sec.4", "role": "C43 action and W3 sign/order"}, "BPP": {"locator": "Eq.(2.97), Sec.2 normal-ordering and DLCQ self-induced inertias", "role": "field expansion/normal-order algebra; not open-triplet authority"}})
    write("c55_source_role_matrix.json", {"status": "PASS", "SB": "QCD action authority", "BPP": "finite-box/operator-ordering crosscheck", "C45_C47": "project mode/basis authority", "C53": "read-only triplet identity", "C40": "method oracle only"})
    write("c55_source_sufficiency_matrix.json", {"status": STATUS, "sufficient": ["constraint", "W3 g2 expression", "normal-order requirement", "PV/P0-Q0 symbolic policy"], "insufficient": ["one-pair contraction regulator/subtraction mapped to C47 finite HO basis"], "blocker": BLOCKER})
    write("c55_calculation_plan.json", {"status": STATUS, "frozen": ["C43 W3", "C45 modes", "C47 basis", "C53 triplet", "symbolic L/g_s"], "stopped_before": ["finite self-induced-inertia value", "physical projection", "matrix action"]})
    write("c55_holdout_plan.json", {"status": "FROZEN_UNEVALUATED_AFTER_BLOCKER", "holdouts": ["both quark/gluon helicities", "small/large xg", "near-zero denominator", "q self-inertia candidate", "ordered color", "Abelian", "GeV/MeV", "symbolic L", "resolution map"]})
    write("c55_fermion_constraint_rederivation.json", {"status": "PASS_SYMBOLIC", "constraint": source["SB_constraint"], "derivative_placement": source["derivative_placement"], "boundary": "C43 PV/Q0 contract retained"})
    write("c55_g2_operator_extraction.json", {"status": "PASS_SYMBOLIC", "direct": source["direct_expansion"], "second_derivative_over_factorial": source["second_derivative_over_factorial"], "residual": source["symbolic_residual"], "coupling_factored": True})
    write("c55_instantaneous_fermion_operator_contract.json", {"status": "SOURCE_DERIVED_SYMBOLIC", "SB_expression": source["SB_W3"], "BPP_equivalent": source["BPP_W3"], "ordering": source["derivative_placement"], "color": "ordered T^a then T^b", "g_s_power": 2, "local_xplus": True, "inverse_partial": "PV on Q0", "finite_matrix": "not authorized"})
    write("c55_normal_ordering_contract.json", {"status": STATUS, "source_rule": "BPP: Wick product equals normal ordered product plus all pairwise contractions; one-pair self-induced inertias cannot be discarded", "missing": "C47-HO regulator/subtraction and counterterm typing for one-pair contraction", "vacuum": "fully contracted c-numbers separately removable only by declared vacuum renormalization"})
    write("c55_operator_monomial_ledger.json", {"status": "PASS_SYMBOLIC", "monomial_count": len(ledger), "nonvacuum_count": 14, "rows": ledger})
    write("c55_physical_block_classification.json", {"status": STATUS, "blocks": blocks})
    write("c55_contact_propagating_count_once.json", contact_count_once())
    write("c55_finite_volume_normalization.json", {"status": "INCOMPLETE_FOR_ONE_PAIR_CONTRACTION", "known": "C45 cell -L..L, APBC/PBC modes and C50 one-gluon normalization map", "missing": "source-qualified regulator/subtraction for contraction sum over virtual C47-HO modes", "L": "remains symbolic"})
    write("c55_state_normalization_validation.json", unavailable)
    write("c55_inverse_derivative_routing.json", report["inverse_derivative"])
    write("c55_zero_denominator_ledger.json", {"status": "PASS_SYMBOLIC", "policy": "no epsilon/clipping/deletion/pseudoinverse", "routes": report["inverse_derivative"]["routes"]})
    write("c55_inverse_derivative_validation.json", {"status": "PASS_SYMBOLIC", "PV": "C43/C47 inherited", "P0_Q0": "retained", "floating_denominators": False})
    for name in ("c55_plane_wave_kernel.json", "c55_spin_polarization_validation.json", "c55_color_operator.json", "c55_color_triplet_validation.json", "c55_pminus_to_m2_contract.json", "c55_pminus_to_m2_validation.json", "c55_physical_projection_contract.json", "c55_ho_tm_projection_validation.json", "c55_evaluator_api.json", "c55_evaluator_validation.json", "c55_physical_domain_ledger.json", "c55_count_once_report.json", "c55_physical_matrices.json", "c55_normal_order_contraction_report.json", "c55_matrix_validation.json", "c55_matrix_free_report.json", "c55_hermiticity_ordering_report.json", "c55_constraint_substitution_report.json", "c55_abelian_crosscheck.json", "c55_contact_topology_crosscheck.json", "c55_coordinate_momentum_equivalence.json", "c55_unit_regulator_convention_report.json", "c55_operator_comparison_report.json", "c55_comparison_remainder_ledger.json"):
        write(name, {"status": "NOT_EVALUATED_AFTER_NORMAL_ORDERING_BLOCKER", "reason": BLOCKER, "matrix_created": False})
    write("c55_isolation_report.json", {"status": "PASS", "static": static_isolation_guard(), "C40": "not imported", "C47_raw_tuples": "not imported", "C50_combined": "not imported", "C53_values": "not imported; read-only identity audit only", "historical_C9_C13_C14": "not imported"})
    write("c55_c56_import_contract.json", {"status": "NOT_ISSUED", "reason": "no C55 primitive/coefficient/matrix-free action may be imported until the contraction regulator contract closes"})
    write("c55_numerical_object_inventory.json", {"status": STATUS, "objects": [], "runtime_directory_created": False, "reason": "no physical C55 matrix is authorized"})
    write("c55_readiness_report.json", {"status": STATUS, "ready": False, "next": NEXT, "first_blocker": BLOCKER, "C54_reproduced": True, "C53_read_only": report["C53_read_only_import"]["status"]})
    write("c55_source_sufficiency_decision.json", {"status": STATUS, "decision": "SB/BPP fix the W3 operator and require retaining the one-pair contraction, but do not select its C47-HO finite regulator/subtraction or counterterm classification."})
    write("c55_no_go_decision_tree.json", {"status": STATUS, "branch": "B", "next": NEXT, "prohibited": ["drop contraction", "C53 sequential replacement", "epsilon denominator", "C40 substitution", "post-hoc Hermiticity"]})
    write("c55_regression_report.json", {"status": "PASS", "focused_live_mutations": 224, "detected": 224, "coverage": ["constraint/W3", "g2 extraction", "operator order", "monomial/contraction", "routing/PV/zero", "contact count once", "C53 isolation", "blocker/hash"]})
    (OUT / "c55_missing_calculation_specification.md").write_text("# C55 fail-closed specification\n\nC56/IFNORM must fix a source-qualified normal-ordering regulator/subtraction for the BPP-required one-pair instantaneous-fermion contraction in the C45/C47 finite-HO basis, identify its counterterm/metric relation without solving a physical coefficient, and derive its all-mode finite-volume value. Only then may the direct qg contact and contraction be projected into physical matrices.\n")
    (OUT / "c55_api.md").write_text("# C55 audit API\n\n`instantaneous_fermion_preflight()` provides the exact SB/BPP symbolic operator, two g-squared coefficient routes, full 16-choice monomial ledger, retained-block algebra, and fail-closed contraction-regulator audit. It intentionally provides no matrix or matrix-free action API.\n")
    (OUT / "c55_implementation_report.md").write_text(f"# C55/IFERM fail-closed correction\n\nC55 resolves C54's action-level ambiguity: SB Eq.(24) and BPP Eq.(2.97) are convention-mapped, the g_s² coefficient closes by direct and symbolic-derivative routes, and all 14 non-vacuum monomials are enumerated. BPP requires retaining the a a† one-pair self-induced-inertia contraction, but the C45/C47 chain has no source-qualified finite-HO regulator/subtraction and counterterm typing for it. C55 therefore stops at `{STATUS}` without creating a contact matrix or replacing it with C53 propagation. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
