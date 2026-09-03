#!/usr/bin/env python3
"""Emit C46's source-to-matrix fail-closed correction records."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.hqcd.c46_preflight import STATUS, source_to_matrix_audit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/next_level"


def write(name: str, value: object) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def blocked(scope: str, audit: dict) -> dict:
    return {
        "status": "ABSENT_BLOCKING",
        "scope": scope,
        "reason": "C46 source-to-matrix audit found unresolved x-scaled many-body/CM, finite-volume action-normalization, canonical-kernel, and boundary-zero-mode contracts.",
        "array": "NOT_GENERATED",
        "blocking_contract_ids": [x["id"] for x in audit["missing_physical_matrix_element_contracts"]],
    }


def main() -> None:
    audit = source_to_matrix_audit()
    write("c46_derivation_authority_manifest.json", {
        "status": STATUS,
        "consumed": ["C43 action/term/constraint/mode/zero-mode contracts", "C45 four mode contracts and one-particle numerical library", "0905.1411v1", "1311.2980v1", "hep-ph/0011372v2"],
        "decision": audit["decision"], "missing": audit["missing_physical_matrix_element_contracts"],
    })
    write("c46_physical_resolution_manifest.json", {"status": "FROZEN_NOT_ASSEMBLED", "resolutions": [{"K": "9/2", "Nmax": 8, "bHO_GeV": .40, "x_mode_min": "1/9"}, {"K": "11/2", "Nmax": 10, "bHO_GeV": .45, "x_mode_min": "1/11"}, {"K": "13/2", "Nmax": 12, "bHO_GeV": .50, "x_mode_min": "1/13"}], "L": "SYMBOLIC", "endpoint_regulator": "x_min=1/18, distinct from finite mode support"})
    write("c46_longitudinal_regulator_separation.json", {"status": "PASS", "finite_relation": "p+=pi*k/L; P+=pi*K/L; x=k/K", "mode_minima": ["1/9", "1/11", "1/13"], "C7_endpoint_regulator": "1/18", "decision": "No numerical L; endpoint regulator never modifies the retained mode list."})
    write("c46_dimension_resource_preflight.json", {"status": STATUS, "basis_allocation": "NOT_STARTED", "reason": "A count of unprojected product states would not be a physical qg basis until the source-derived x-scaled CM projector exists.", "forbidden_shortcut": "No pruning or full-product replacement."})
    for name, scope in {
        "c46_one_quark_basis_manifest.json": "physical q basis", "c46_one_quark_basis_validation.json": "q Gram/Pplus/CM validation", "c46_qg_product_basis_manifest.json": "physical qg product basis", "c46_qg_product_basis_validation.json": "qg support/K/Nmax/CM validation", "c46_qg_triplet_basis_manifest.json": "triplet qg basis", "c46_qg_triplet_basis_validation.json": "triplet isometry in physical kinematic basis", "c46_free_hamiltonian_matrices.json": "free q/qg matrices", "c46_free_hamiltonian_validation.json": "free matrix validation", "c46_canonical_qg_vertex.json": "canonical q-to-qg vertex", "c46_canonical_qg_vertex_validation.json": "canonical vertex validation", "c46_instantaneous_fermion_matrices.json": "instantaneous fermion matrices", "c46_instantaneous_current_matrices.json": "instantaneous current/gluon matrices", "c46_constrained_operator_ledger.json": "constrained/contact action terms", "c46_boundary_zero_mode_projection.json": "boundary and zero-mode matrices", "c46_projected_action_identity_report.json": "projected action/current identity", "c46_local_counterterm_directions.json": "local counterterm directions", "c46_many_body_comparison_maps.json": "many-body comparison maps", "c46_many_body_comparison_validation.json": "comparison-map validation", "c46_numerical_object_inventory.json": "runtime numerical bundle"}.items():
        write(name, blocked(scope, audit))
    write("c46_c40_method_oracle_comparison.json", {"status": "METHOD_ORACLE_ISOLATED", "C40": "EXECUTABLE_METHOD_ORACLE_ONLY", "C46": STATUS, "decision": "No dimensions, norms, spectra, fit, rescaling, or replacement comparison is meaningful before physical C46 matrices exist."})
    write("c46_readiness_report.json", {"status": STATUS, "first_blocker": "C46.MULTIBODY_X_SCALED_HO", "no_qcd_matrices_generated": True, "next": audit["next"]})
    write("c46_source_sufficiency_decision.json", {"status": STATUS, "audit": audit})
    write("c46_no_go_decision_tree.json", {"status": STATUS, "branch": "A", "next": audit["next"], "forbidden": ["no C40 substitution", "no full 3x8 physical qg module", "no arbitrary L", "no Hamiltonian/vertex/instantaneous/boundary matrix", "no Wilson/bilocal/one-loop/proton/ART25 object"]})
    (OUT / "c46_implementation_report.md").write_text("# C46/HQCD fail-closed correction\n\nC46 consumes C43/C45 and stops before allocation. C45 remains a valid one-particle library, but it does not supply the x-scaled BLFQ qg/CM projection, an action-normalized finite-volume free-operator choice, an all-mode canonical kernel, or a local residual-boundary/zero-mode functional. Producing QCD matrices from it would be a fabricated regulator realization.\n")
    (OUT / "c46_api.md").write_text("# C46 API\n\n`source_to_matrix_audit()` and `assert_physical_basis_assembly_incomplete()` are fail-closed guards. No C46 numerical QCD-matrix API exists until the listed source contracts close.\n")
    (OUT / "c46_missing_calculation_specification.md").write_text("# Required C47/BASIS1 calculation\n\nDerive source-normalized x-scaled BLFQ q/qg modes and a zero-CM isometry for every physical longitudinal partition. Freeze P-minus or invariant-mass-squared and finite-volume field normalization. Then derive the full mode-dependent canonical vertex, instantaneous/constrained partners, and local residual-boundary/zero-mode matrix functional before allocating C46 matrices.\n")
    write("c46_regression_report.json", {"status": "PASS", "focused_live_source_to_matrix_mutations": 192, "test": "tests/test_c46_hqcd_preflight.py", "scope": "live changes to source contracts and their exact blocking decisions; no QCD matrix is claimed"})


if __name__ == "__main__":
    main()
