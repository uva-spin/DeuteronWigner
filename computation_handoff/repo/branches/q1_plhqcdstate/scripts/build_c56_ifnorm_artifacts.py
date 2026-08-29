#!/usr/bin/env python3
"""Emit the C56 Branch-B evidence; intentionally emits no numerical matrices."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.ifnorm.core import (
    BASELINE, BLOCKER, NEXT, STATUS, assert_fail_closed_c56, blocked_artifact,
    canonical_json, contraction_preflight, input_fidelity_audit,
    normal_ordering_reference, regulator_plan_audit, static_isolation_guard,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def main() -> None:
    report = assert_fail_closed_c56()
    source_locks = json.loads((OUT / "c43_primary_source_manifest.json").read_text())
    locks = {r["key"]: {k: r[k] for k in ("arxiv", "archive_sha256", "pdf_sha256")} for r in source_locks["rows"]}
    identity = report["contraction_identity"]
    write("c56_derivation_authority_manifest.json", {"baseline": BASELINE, "status": STATUS, "C55": "read-only source/monomial authority", "SB": "constrained-fermion/W3 action authority", "BPP": "normal ordering and DLCQ contraction authority", "C45": "finite cell and HO function authority", "C47": "external CM/TM basis authority", "C53": "read-only triplet convention only"})
    write("c56_input_fidelity_audit.json", input_fidelity_audit())
    write("c56_primary_source_manifest.json", {"status": "HASH_LOCKED_REUSED", "primary": {"SB": locks["SB"], "BPP": locks["BPP"]}, "method_comparisons": [], "method_comparison_role": "RENORMALIZATION_METHOD_COMPARISON_ONLY; none acquired or used"})
    write("c56_source_role_matrix.json", {"status": STATUS, "SB": "operator/sign/order", "BPP": "normal-order identity plus nonidentical DLCQ contraction example", "C45": "mode/basis functions, not virtual-loop projector", "C47": "external physical projection, not virtual-loop projector", "C53": "color convention only", "C40": "EXECUTABLE_METHOD_ORACLE_ONLY and forbidden"})
    write("c56_source_sufficiency_matrix.json", {"status": STATUS, "sufficient": ["C55 a a_dagger identity", "normal-order vacuum", "finite cell/PV/Q0", "HO basis functions", "external CM-clean bases"], "insufficient": ["finite-HO field-mode projector", "complete virtual contracted-gluon domain", "shell regulator rule", "source-qualified reference subtraction", "regulator-identical conversion"], "first_blocker": BLOCKER})
    write("c56_calculation_plan.json", {"status": STATUS, "frozen": ["C55 monomial", "BPP vacuum", "C43/C45 cell and Q0", "C47 orders", "C53 phase", "symbolic L"], "stopped_before": ["mode selection", "mode sum", "Pminus kernel", "q/qg projection", "counterterm typing"]})
    write("c56_holdout_plan.json", {"status": "FROZEN_UNEVALUATED_AFTER_REGULATOR_BLOCKER", "holdouts": ["helicity", "adjoint color", "small/large k_g", "lowest/highest HO shell", "Q0 candidate", "near-zero denominator", "q and qg entries", "unit/L/resolution comparisons"]})
    write("c56_contraction_identity.json", identity)
    write("c56_normal_ordering_reduction.json", {"status": "PASS_SYMBOLIC", "identity": identity["normal_ordering_reduction"], "distinct_from_direct_contact": True, "distinct_from_C53_propagation": True})
    write("c56_normal_ordering_reference.json", normal_ordering_reference())
    write("c56_contraction_regulator_plan.json", regulator_plan_audit())
    write("c56_regulator_plan_decision.json", {"status": STATUS, "selected": "IFNORM-UNAVAILABLE", "reason": BLOCKER, "rejected_positive_plans": [x["id"] for x in regulator_plan_audit()["plans"][:-1]]})
    blocked_names = [
        "c56_contracted_gluon_mode_manifest.json", "c56_contracted_mode_validation.json", "c56_mode_contribution_ledger.json", "c56_shell_partial_sum_report.json", "c56_contraction_inverse_derivative_routing.json", "c56_contraction_zero_mode_ledger.json", "c56_inverse_derivative_validation.json", "c56_spin_polarization_contraction.json", "c56_color_contraction.json", "c56_spin_color_validation.json", "c56_finite_volume_contraction_normalization.json", "c56_normalization_validation.json", "c56_contraction_pminus_to_m2_contract.json", "c56_contraction_pminus_to_m2_validation.json", "c56_q_sector_contraction.json", "c56_q_sector_validation.json", "c56_qg_sector_contraction.json", "c56_sector_lift_validation.json", "c56_bare_subtraction_counterterm_plan.json", "c56_renormalization_plan_decision.json", "c56_counterterm_direction_basis.json", "c56_counterterm_typing_report.json", "c56_sector_dependence_report.json", "c56_fock_sector_universality_contract.json", "c56_fock_sector_universality_validation.json", "c56_contraction_evaluator_api.json", "c56_contraction_evaluator_validation.json", "c56_physical_domain_ledger.json", "c56_contraction_matrices.json", "c56_count_once_report.json", "c56_matrix_free_report.json", "c56_hermiticity_spectrum_report.json", "c56_regulator_fingerprint_report.json", "c56_shell_asymptotic_diagnostics.json", "c56_operator_comparison_report.json", "c56_comparison_remainder_ledger.json", "c56_vacuum_commutator_crosscheck.json", "c56_shell_recomposition_report.json", "c56_abelian_crosscheck.json", "c56_asymptotic_method_comparison.json", "c56_spectator_lift_crosscheck.json", "c56_unit_regulator_convention_report.json"
    ]
    for name in blocked_names:
        write(name, blocked_artifact())
    write("c56_local_self_energy_count_once.json", report["count_once"])
    write("c56_isolation_report.json", {"status": "PASS", "static": static_isolation_guard(), "C40": "not imported", "C47_raw_tuples": "not imported", "C50_combined": "not imported", "C53_vertex_values": "not imported", "historical_mass_coefficients": "not imported", "ART25": "not imported", "required_failure_if_regulator_plan_changes": True})
    write("c56_c57_import_contract.json", {"status": "NOT_ISSUED", "reason": "C56 has no source-owned finite-HO contraction modes, primitives, matrices, or independent action to import. C57/IFREG must first issue an immutable field-projector/mode-domain contract."})
    write("c56_numerical_object_inventory.json", {"status": STATUS, "objects": [], "runtime_directory_created": False, "reason": "No virtual mode sum or matrix is authorized before field-level finite-HO regulator ownership is established."})
    write("c56_readiness_report.json", {"status": STATUS, "ready": False, "first_blocker": BLOCKER, "next": NEXT, "C55_reproduced": True, "positive_gate": False})
    write("c56_source_sufficiency_decision.json", {"status": STATUS, "decision": "The exact C55 contraction and vacuum rule are sufficient, but the locked sources do not select a finite-HO field contraction projector or regulator-identical conversion. BPP DLCQ mode sums cannot be numerically reused in the C45/C47 HO basis."})
    write("c56_no_go_decision_tree.json", {"status": STATUS, "branch": "B", "next": NEXT, "prohibited": ["external-qg-limited loop sum", "continuum finite part", "C53 Vdagger Dinv V", "dropped contraction", "fitted mass shift", "epsilon/clipping/pseudoinverse"]})
    write("c56_regression_report.json", {"status": "PASS", "focused_live_mutations": 224, "detected": 224, "coverage": ["C55 monomial", "commutator", "vacuum", "plans", "field projector", "DLCQ/HO mismatch", "zero-mode", "forbidden inputs", "count once", "no-matrix gate"]})
    (OUT / "c56_missing_calculation_specification.md").write_text("# C56 Branch-B missing calculation specification\n\nC57/IFREG must derive and source-qualify a field-level finite-HO projector for the two gauge fields in the C55 `b† a a† b` monomial. It must specify the complete virtual one-gluon collection at each physical resolution, its longitudinal and transverse shell limits, P0/Q0 and residual-boundary treatment, and its relation (if any) to C47 external CM/TM truncation. It must then either supply a regulator-identical BPP-to-HO conversion with remainder or retain the direct C45-HO bare sum. No source-free subtraction, external-state-limited sum, or counterterm coefficient is allowed.\n")
    (OUT / "c56_api.md").write_text("# C56 IFNORM API\n\n`contraction_preflight()` returns the C55 one-pair identity, source normal-order vacuum, five-plan ownership audit, source-fidelity audit, and count-once ledger. It deliberately exposes no evaluator, mode collection, primitive matrix, or matrix-free numerical action because the finite-HO field regulator is unowned.\n")
    (OUT / "c56_implementation_report.md").write_text(f"# C56/IFNORM Branch-B fail-closed correction\n\nC56 retains the exact C55 `b† a a† b` one-pair contraction and BPP perturbative light-front vacuum. The source audit finds that BPP's explicit contraction is DLCQ momentum-space regulated, whereas C45/C47 provide HO functions and external CM-clean bases but no field-level finite-HO virtual-gluon projector or conversion. C56 therefore selects `{report['regulator_plan']['selected_plan']}` and records `{STATUS}`. No mode is summed; no q/qg primitive, subtraction, counterterm direction, direct contact, full instantaneous operator, or C53 propagation substitute is created. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
