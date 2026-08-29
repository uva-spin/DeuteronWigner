#!/usr/bin/env python3
"""Emit deterministic C48 fail-closed records; never emit QCD matrices."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.hqcd2.preflight import (
    BASELINE, NEXT, STATUS, canonical_vertex_audit, input_fidelity_audit,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main() -> None:
    fidelity = input_fidelity_audit()
    audit = canonical_vertex_audit()
    dimensions = [{
        "resolution": row["resolution"], "q_dimension": 6,
        "qg_cm_triplet_dimension": dim, "canonical_tuple_count": row["tuple_count"],
        "resource_decision": "No sparse local matrix allocated: canonical M^2 normalization is blocking.",
    } for row, dim in zip(audit["canonical_resolution_records"], [1344, 2700, 4752])]
    authority = {
        "status": "SOURCE_AUDIT_COMPLETE", "baseline": BASELINE,
        "C43": "hep-ph/0011372v2 Eqs. (1),(5)-(9),(24)-(25); locked by C43",
        "C45": "source-derived modes, spinors, polarizations, triplet projector, P0/Q0",
        "C47": "1911.10762v1 and C47 executable physical-basis/functionals",
        "decision": STATUS,
    }
    write("c48_derivation_authority_manifest.json", authority)
    write("c48_input_fidelity_audit.json", fidelity)
    write("c48_dimension_resource_preflight.json", {"status": STATUS, "resolutions": dimensions, "dense_4752_square_forbidden": True})
    write("c48_physical_resolution_manifest.json", {"status": STATUS, "trajectory": ["K=9/2", "K=11/2", "K=13/2"], "finite_mode_minima": ["1/9", "1/11", "1/13"], "C7_endpoint_regulator": "1/18; distinct", "L": "symbolic; no arbitrary value selected"})
    write("c48_basis_order_manifest.json", {"status": STATUS, "q": "(K,CM0,h,color)", "qg": "(partition,xq,xg,nrel,mrel,NCM=0,MCM=0,hq,hg,triplet)", "frozen_from": "c47_c48_matrix_assembly_interface.json"})
    write("c48_canonical_qg_matrix.json", audit)
    write("c48_canonical_qg_validation.json", {"status": STATUS, "checks": "C47 tuple hashes, m-sector support, dimensional homogeneity and C43-to-M2 conversion audited", "pass": False, "reason": audit["blockers"][0]["blocking_reason"]})
    unavailable = {"status": "NOT_CONSTRUCTED_BLOCKED_BY_C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE", "reason": "A complete coupling-ordered operator requires a valid canonical M2 coefficient; no surrogate partial matrix is exported."}
    for name in [
        "c48_free_q_matrix.json", "c48_free_q_validation.json", "c48_free_qg_matrix.json", "c48_free_qg_validation.json",
        "c48_instantaneous_fermion_matrices.json", "c48_instantaneous_current_matrices.json", "c48_constrained_contact_ledger.json", "c48_boundary_zero_mode_matrices.json",
        "c48_local_operator_block_manifest.json", "c48_polynomial_action_validation.json", "c48_projected_action_identity_report.json",
        "c48_local_counterterm_directions.json", "c48_local_counterterm_rank_report.json", "c48_operator_comparison_report.json", "c48_comparison_remainder_ledger.json",
    ]:
        write(name, unavailable)
    write("c48_numerical_object_inventory.json", {"status": STATUS, "runtime_root": "data/runtime/c48_hqcd/", "objects": [], "reason": "No arrays are emitted before a source-derived canonical invariant-mass normalization exists."})
    write("c48_c40_method_oracle_comparison.json", {"status": STATUS, "C40": "EXECUTABLE_METHOD_ORACLE_ONLY", "comparison_performed": False, "reason": "No C48 physical matrix exists to compare; no C40 coefficient or array was consumed."})
    source = {"status": STATUS, "decision": "C47 input hashes and source links pass; C48 stops at the canonical M2 normalization contract.", "next": NEXT, "blockers": audit["blockers"]}
    write("c48_source_sufficiency_decision.json", source)
    write("c48_no_go_decision_tree.json", {"status": STATUS, "branch": "C", "next": NEXT, "other_branches_not_evaluated": "Downstream local terms are deliberately not used to bypass the earliest canonical failure."})
    write("c48_readiness_report.json", {"status": STATUS, "readiness": False, "next": NEXT, "input_hashes_pass": fidelity["all_required_runtime_hashes_match"], "no_local_matrices_created": True, "no_nonlocal_or_phenomenological_objects_created": True})
    write("c48_regression_report.json", {"status": STATUS, "tests": {"focused_live_mutations": 224, "scope": "numerical tuple fingerprints, accounting, m support, units, M2 conversion, and blocking proofs", "expected": "all detected"}, "deterministic": True})
    (OUT / "c48_missing_calculation_specification.md").write_text("# C48 missing calculation specification\n\nC49/VERTEX1 must derive one C43/SB finite-volume canonical q-to-qg matrix-element formula in invariant-mass-squared units. It must retain symbolic L, include the 2P+ conversion and field normalization, cover every transverse numerator sector with a common unit, and produce an independently checked exhaustive tuple table before SU(3) and the 24x3 triplet isometry are inserted. No C40 array, arbitrary L, bHO rescaling, or fitted factor may supply this conversion.\n")
    (OUT / "c48_api.md").write_text("# C48 API\n\n`deuteron_wigner.bridge.hqcd2` exports only the C48 source-sufficiency audit. It exports no QCD Hamiltonian, canonical vertex, instantaneous operator, Wilson matrix, TMD measurement, or matching result.\n")
    (OUT / "c48_implementation_report.md").write_text(f"# C48/HQCD implementation report\n\nC48 verifies C47 runtime/source fidelity and stops fail-closed at `{STATUS}`. The C47 canonical functional mixes `|mrel|=0` and `|mrel|=1` while declaring `L^(-1/2) GeV^(1+|mrel|)`, and it provides no source-derived C43 canonical-P-minus to invariant-mass-squared conversion. A numerical SU(3) insertion would therefore not be a source-derived operator. The exact next branch is **{NEXT}**. No local matrix, JMY Wilson matrix, bilocal TMD, soft subtraction, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production route was created.\n")


if __name__ == "__main__":
    main()
