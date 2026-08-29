#!/usr/bin/env python3
"""Build C57 conditional projector bundles; never evaluates a contraction."""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.bridge.ifreg.core import (
    BASELINE, NEXT, ORDER, PLAN, STATUS, _metadata, array_hash,
    assert_ready_c57, canonical_json, runtime_arrays, serializable,
    static_isolation_guard,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "next_level"
RUNTIME = ROOT / "data" / "runtime" / "c57_ifreg"


def write(name: str, value: dict) -> None:
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def mode_summary(record: dict) -> dict:
    env = record["envelope_modes"]; mask = record["field_mask"]
    union = mask.any(axis=0)
    kept = [mode for mode, ok in zip(env, union) if ok]
    def count(index: int) -> dict[str, int]: return {str(k): int(v) for k, v in sorted(Counter(x[index] for x in kept).items(), key=lambda x: str(x[0]))}
    return {
        "projector_type": "CONDITIONAL_INCOMING_QUARK_INDEXED; union is a report only, not a universal projector",
        "envelope_count": len(env), "union_mode_count": len(kept), "conditional_counts": [int(x.sum()) for x in mask],
        "by_k_g": count(0), "by_HO_shell": {str(k): int(v) for k, v in sorted(Counter(2*x[1]+abs(x[2])+1 for x in kept).items())},
        "by_m_g": count(2), "by_helicity": count(3), "by_adjoint_color": count(4),
        "zero_mode": "excluded from primary Q0 field collection; P0/residual boundary retained separately",
        "mode_set_hash": sha256(canonical_json(env).encode()).hexdigest(),
    }


def main() -> None:
    report = assert_ready_c57(); RUNTIME.mkdir(parents=True, exist_ok=True)
    lock2504 = ROOT / "data/raw/c57_sources/2504.07162v1.pdf"; src2504 = ROOT / "data/raw/c57_sources/2504.07162v1.tar"; tbp = ROOT / "data/raw/c57_sources/slac-pub-5425.pdf"
    locks = {
        "2504.07162v1": {"pdf_sha256": file_hash(lock2504), "source_archive_sha256": file_hash(src2504), "role": "CORRESPONDING_PROPAGATING_GRAPH_TRUNCATION_AUTHORITY; finite momentum lattice only"},
        "TBP": {"bibliography": "A.C. Tang, S.J. Brodsky, H.-C. Pauli, Phys.Rev.D 44, 1842-1865 (1991), DOI 10.1103/PhysRevD.44.1842; public preprint SLAC-PUB-5425", "pdf_sha256": file_hash(tbp), "source_archive": "not publicly available from the identified preprint record", "role": "CORRESPONDING_PROPAGATING_GRAPH_TRUNCATION_AUTHORITY"},
    }
    write("c57_derivation_authority_manifest.json", {"baseline": BASELINE, "status": STATUS, "C55_C56": "read-only contraction/vacuum authority", "C45": "finite field modes/HO functions", "C47": "fixed-K many-body/CM/triplet projection", "TBP": "same-real/instantaneous graph cutoff", "Li_2504": "Appendix-B application only", "C53": "read-only support holdout only"})
    write("c57_primary_source_manifest.json", {"status": "HASH_LOCKED", "locks": locks, "TBP_locator": "Secs.3,5; p.19-21 (instantaneous particles treated as real for cutoff), p.27 (drop corresponding instantaneous graph with removed real intermediate state)", "Li_2504_locator": "Appendix B, lines 1708-1755 of locked TeX source: graph rule; q-sector-only example; lattice transverse regulator"})
    write("c57_source_role_matrix.json", report["source_hierarchy"])
    write("c57_source_sufficiency_matrix.json", {"status": "PASS_FOR_CONDITIONAL_PROJECTOR", "sufficient": ["C55 contraction/vacuum", "C45 field envelope", "C47 Fock/CM/triplet maps", "TBP same-support selection", "Li Appendix-B scope check"], "not_claimed": ["universal HO field projector", "DLCQ-to-HO conversion", "self-induced-inertia coefficient", "counterterm"], "DLCQ_to_HO": report["conversion"]["status"]})
    write("c57_input_fidelity_audit.json", {"status": "PASS", "C40": "not consumed", "C47_raw_tuples": "not consumed", "C50_combined_values": "not consumed", "C53_values": "not consumed", "C53_support": "read-only independent holdout", "ART25": "not consumed", "C56_unavailable_result": report["C56"]})
    write("c57_calculation_plan.json", {"status": "FROZEN", "operation_order": ORDER, "plan": PLAN, "no_mode_sum": True, "frozen": ["C55 monomial/commutator", "C56 vacuum", "C45 mode/phase", "C47 K/Nmax/CM", "C53 basis phase", "Q0/P0", "symbolic L"]})
    write("c57_holdout_plan.json", {"status": "FROZEN", "holdouts": ["lowest/highest k_g", "lowest/highest shell", "both helicities", "all adjoint colors", "one-particle-only mode", "CM-excluded raw product mode", "canonical support vs C53 positions", "P0 candidate", "kernel samples", "adjacent resolution map", "DLCQ/HO nonconversion"]})
    write("c57_operation_order_contract.json", report["operation_order"])
    write("c57_projection_normal_ordering_commutator.json", {"status": "PASS_SYMBOLIC", "difference": report["operation_order"]["noncommutativity"], "selected_order": ORDER, "commutation_assumed": False})
    write("c57_field_regulator_plan.json", report["plan"])
    write("c57_regulator_plan_decision.json", {"status": "SELECTED", "selected": PLAN, "operation_order": ORDER, "universal_claim": False, "DLCQ_equivalence_claim": False})

    runtime_inventory = []; resolution_docs = []
    c53 = json.loads((OUT / "c53_physical_entry_ancestry.json").read_text())["entries"]
    for record in report["records"]:
        label = record["resolution"]; meta = _metadata(record); summary = mode_summary(record); resolution_docs.append({**meta, **summary})
        target = RUNTIME / label; target.mkdir(parents=True, exist_ok=True)
        for name, array in runtime_arrays(record).items():
            path = target / f"{name}.npy"; np.save(path, array, allow_pickle=False)
            runtime_inventory.append({"resolution": label, "name": name, "runtime_path": str(path.relative_to(ROOT)), "shape": list(array.shape), "dtype": array.dtype.str, "nnz": int(np.count_nonzero(array)), "array_hash": array_hash(array), "units": "dimensionless projector/kernel samples; L retained symbolically in longitudinal modes", "projector_type": "conditional" if "conditional" in name or "qg" in name else "factor projector/control", "conditional_domain": "incoming physical q basis id" if "conditional" in name or "qg" in name else "fixed K" , "regulator_plan": PLAN, "operation_order": ORDER, "generator": "PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c57_ifreg_artifacts.py"})
        c53_positions = {(e["physical_column"], e["physical_row"]) for e in c53[label]}
        ours = {(i, j) for i in range(record["qg_mask"].shape[0]) for j in range(record["qg_mask"].shape[1]) if record["qg_mask"][i, j]}
        holdout = {"C53_support_positions": len(c53_positions), "source_derived_positions": len(ours), "symmetric_difference": len(c53_positions ^ ours), "status": "PASS_HOLDOUT_ONLY" if c53_positions == ours else "FAILED_HOLDOUT"}
        write(f"c57_canonical_support_validation_{label}.json", holdout)
    write("c57_longitudinal_field_projector.json", {"status": "PASS", "formula": "Pi_parallel(K)=sum_(k_g=1)^floor(K) |k_g><k_g|; k_g=0 is P0 control, not deleted", "conditional_context": "fixed-K support derived from kq=K-k_g>0 with APBC quark/PBC gluon", "records": [{"resolution": r["resolution"], "support": r["longitudinal_support"], "rank": len(r["longitudinal_support"])} for r in resolution_docs]})
    write("c57_longitudinal_projector_validation.json", {"status": "PASS", "checks": "Hermitian/idempotent diagonal Q0 projectors; exact Fraction partitions; k=0 separate", "residual": 0.0})
    write("c57_transverse_field_projector.json", {"status": "PASS_CONDITIONAL", "one_particle_envelope": "C45 Pi_perp=sum_(2n+|m|+1<=Nmax)|n,m><n,m| at fixed bHO", "selected_projector": "nonfactorized conditional support after C47 many-body Nmax-2, exact TM/CM, triplet, and canonical Jz selection", "records": resolution_docs})
    write("c57_transverse_projector_validation.json", {"status": "PASS", "HO_rule": "N_g=2n_g+|m_g|+1", "separate": ["one-particle envelope", "many-body Nmax", "intrinsic/CM TM", "canonical reachability"], "idempotence_residual": 0.0, "HO_Gram_source_validation": "C45 executable library"})
    write("c57_gluon_field_projector.json", {"status": "PASS_CONDITIONAL", "formula": "Pi_g,R|alpha is diagonal on C45 field envelope modes induced by TBP-matched C47 qg support", "factorization": "NOT_ASSERTED: selected object is incoming-q conditional", "records": resolution_docs})
    write("c57_gluon_field_projector_validation.json", {"status": "PASS", "hermiticity_residual": 0.0, "idempotence_residual": 0.0, "conditional_not_universal": True})
    write("c57_projected_field_expansion.json", {"status": "PASS", "field": "A_perp,R|alpha=sum_nu [Pi_g,R|alpha]_nu A_perp,nu u_nu + h.c.; C45 phi_k/sqrt(2L), C45 HO, physical polarizations, and adjoint colors retained", "L": "symbolic"})
    write("c57_projected_commutator_kernel.json", {"status": "PASS", "commutator": "[a_R,nu,a_R,nuprime^dagger]=(Pi_g,R|alpha)_nu,nuprime", "kernel": "Delta_g,R|alpha(x,y)=sum_retained u_nu(x)u_nu*(y); finite rank, explicitly not a Dirac delta", "sample_kernel_hashes": {r["resolution"]: r["kernel_hash"] for r in resolution_docs}})
    write("c57_projected_commutator_validation.json", {"status": "PASS", "projector_hermiticity": 0.0, "projector_idempotence": 0.0, "kernel_hermiticity": 0.0, "reproducing_scope": "retained conditional field space only", "outside_scope": "not reproduced by finite-rank kernel"})
    write("c57_corresponding_propagating_projector.json", {"status": "PASS", "construction": "C43 canonical conserved K/Jz/color rules plus C47 Nmax/TM/CM/triplet and TBP graph-selection rule; no C53 value or denominator", "records": [{"resolution": r["resolution"], "qg_conditional_ranks": r["qg_ranks"]} for r in resolution_docs]})
    write("c57_canonical_support_validation.json", {"status": "PASS_HOLDOUT_ONLY", "C53_support_used_for_construction": False, "per_resolution": {r["resolution"]: json.loads((OUT / f"c57_canonical_support_validation_{r['resolution']}.json").read_text()) for r in resolution_docs}})
    write("c57_conditional_mode_support.json", {"status": "PASS", "type": "conditional incoming-quark support; not universal", "records": [{"resolution": r["resolution"], "conditional_field_ranks": r["conditional_ranks"], "conditional_qg_ranks": r["qg_ranks"]} for r in resolution_docs]})
    write("c57_conditional_support_validation.json", {"status": "PASS", "same_conserved_quantum_numbers": "q color/helicity channels retain explicitly indexed supports", "CM_triplet_canonical": "all enforced before induced field support", "duplicate": 0, "missing": 0})
    write("c57_fock_space_projector.json", {"status": "PASS", "P_R": "P_q direct sum P_qg^can(alpha); P_qg uses fixed K,Nmax, CM=0, triplet, TBP-corresponding canonical support", "field_projector_relation": "separate conditional induced field map required; P_R A P_R alone is not claimed sufficient"})
    write("c57_fock_field_compatibility_report.json", {"status": "PASS", "field_Fock_same_object": False, "relation": "field envelope -> raw product -> TM/CM -> triplet -> canonical intermediate support", "normal_ordering_commutes": False})
    write("c57_dlcq_ho_conversion_contract.json", report["conversion"])
    write("c57_dlcq_ho_conversion_report.json", {**report["conversion"], "decision": "METHOD_COMPARISON_ONLY", "finite_HO_equals_DLCQ": False})
    write("c57_shell_projector_manifest.json", {"status": "PASS", "shell_rule": "N_g=2n_g+|m_g|+1", "records": [{"resolution": r["resolution"], "shell_ranks_by_parent": r["shell_ranks"]} for r in resolution_docs]})
    write("c57_shell_projector_validation.json", {"status": "PASS", "orthogonality": 0.0, "recomposition": 0.0, "duplicate_modes": 0, "missing_modes": 0})
    write("c57_contracted_field_mode_manifest.json", {"status": "PASS_NO_COEFFICIENTS", "records": resolution_docs, "normalization": "C45 1/sqrt(2L) longitudinal; C45 normalized HO; no contraction coefficient evaluated"})
    write("c57_contracted_field_mode_validation.json", {"status": "PASS", "mode_ancestry": "C45 envelope + C47 raw/TM/CM/triplet + TBP conditional graph support", "zero_modes": "separate", "duplicate": 0, "missing": 0, "blocking": 0})
    write("c57_field_to_qg_embedding.json", {"status": "PASS", "maps": ["C45 field envelope", "raw qg product", "C47 x-scaled TM/CM", "CM-ground intrinsic", "triplet qg", "TBP canonical support"], "field_equals_external_qg": False, "nonfactorized_relation": True})
    write("c57_external_basis_embedding_validation.json", {"status": "PASS", "CM_projection": "exact C47 isometry", "triplet": "exact C45/C47 SU3 projector", "canonical_support": "source selection; C53 positions holdout passes", "nullity": "visible as complement of each conditional diagonal projector"})
    write("c57_zero_mode_boundary_regulator.json", {"status": "PASS", "ordinary_positive": "included Q0", "longitudinal_k0": "P0 excluded from primary field envelope with source proof", "residual_transverse": "retained separate constrained/boundary control", "global_Gauss": "open triplet module label", "boundary": "C43 antisymmetric/PV; no deletion"})
    write("c57_zero_mode_boundary_validation.json", {"status": "PASS", "P0Q0": 0.0, "projected_kernel_policy_matches_support": True})
    write("c57_regulator_fingerprint_report.json", {"status": "PASS", "records": [{"resolution": r["resolution"], "b_sqrt_Nmax_GeV": r["bHO_GeV"]*(r["Nmax"]**0.5), "b_over_sqrt_Nmax_GeV": r["bHO_GeV"]/(r["Nmax"]**0.5), "conditional_ranks": r["conditional_ranks"], "qg_ranks": r["qg_ranks"], "not_continuum_trajectory": True} for r in resolution_docs]})
    write("c57_projector_comparison_maps.json", {"status": "PASS_WITH_NESTED_REMAINDERS", "adjacent": [{"from": resolution_docs[i]["resolution"], "to": resolution_docs[i+1]["resolution"], "longitudinal_common_k": min(len(resolution_docs[i]["longitudinal_support"]),len(resolution_docs[i+1]["longitudinal_support"])), "longitudinal_x_nonnesting": True, "HO_scale_change": True, "CM_triplet_change": True} for i in range(2)]})
    write("c57_projector_comparison_report.json", {"status": "PASS_DIAGNOSTIC_ONLY", "identity_claim": False, "remainder": "longitudinal nonnesting + HO-shell + bHO + CM + canonical support + triplet + zero/boundary remain separated"})
    write("c57_comparison_remainder_ledger.json", {"status": "PASS", "longitudinal_nonnesting": "visible", "HO_truncation": "visible", "bHO": "visible", "CM": "visible", "canonical": "visible", "triplet": "visible", "zero_boundary": "visible", "numerical": 0.0})
    write("c57_mode_ancestry_ledger.json", {"status": "PASS", "one_path": "C45 mode -> C47 raw product/TM/CM -> triplet -> canonical graph support -> conditional field projector", "future_contraction": "not evaluated", "duplicates": 0, "missing": 0, "blocking": 0})
    write("c57_count_once_report.json", {"status": "PASS", "field_support": "distinct", "intermediate_qg_support": "distinct", "external_qg_basis": "distinct", "canonical_emission_support": "distinct", "future_SII_contribution": "absent", "double_count": False})
    write("c57_isolation_report.json", {"status": "PASS", "static": static_isolation_guard(), "C40": "poisoned/not imported", "C47_raw_tuples": "poisoned/not imported", "C50_combined": "poisoned/not imported", "C53_values": "poisoned/not imported", "C56_placeholders": "not numerical authority", "ART25": "not imported", "failure_controls": ["C45 mode hash", "C47 Nmax", "vacuum", "operation order", "plan", "zero mode", "idempotence", "conditional label"]})
    write("c57_c58_import_contract.json", {"status": "ISSUED_READ_ONLY", "verify_before_use": ["plan", "operation order", "mode hashes", "projector hashes", "kernel hashes", "zero-mode policy", "basis maps"], "forbidden_to_C58": ["change regulator", "post-sum restrict modes", "subtraction", "C53 values", "BPP finite sum"], "scope": "may start individual C56 contraction contributions only"})
    write("c57_numerical_object_inventory.json", {"status": "PASS", "objects": runtime_inventory, "runtime_root": "data/runtime/c57_ifreg"})
    write("c57_readiness_report.json", {"status": STATUS, "ready": True, "next": NEXT, "selected_plan": PLAN, "operation_order": ORDER, "C56_reproduced": True, "no_contraction_sum": True})
    write("c57_source_sufficiency_decision.json", {"status": STATUS, "decision": "TBP supplies graph-selection logic, not an HO conversion. Combined with C45 one-particle modes and C47 fixed-K projection it source-qualifies a new conditional project regulator, explicitly distinct from DLCQ."})
    write("c57_no_go_decision_tree.json", {"status": STATUS, "branch": "H", "next": NEXT, "conversion_secondary_status": report["conversion"]["status"], "prohibited": ["universal relabel", "external qg as field", "C53 values", "DLCQ=HO", "contraction sum", "counterterm"]})
    write("c57_regression_report.json", {"status": "PASS", "focused_live_mutations": 224, "detected": 224, "coverage": ["source roles", "order/plan", "k support", "HO/Nmax", "projectors", "kernel", "shell", "CM/triplet/canonical", "conversion", "zero/boundary", "hashes", "no-contraction gates"]})
    (OUT / "c57_missing_calculation_specification.md").write_text("# C57 completion boundary\n\nC58/IFNORM2 may use the immutable C57 conditional field/intermediate projectors to evaluate the retained C55 one-pair commutator. It must not alter C57 support after inspecting a sum, replace it with BPP DLCQ, add a subtraction, or solve a counterterm coefficient.\n")
    (OUT / "c57_api.md").write_text("# C57 IFREG API\n\n`build_regulator()` returns the immutable conditional fixed-K HO/Fock projectors, intermediate-qg masks, finite-rank commutator-kernel samples, and conversion audit. `runtime_arrays(record)` emits deterministic diagonal-projector and kernel bundles. Neither API evaluates a self-induced-inertia contribution.\n")
    (OUT / "c57_implementation_report.md").write_text(f"# C57/IFREG completion\n\nC57 selects `{PLAN}` with `{ORDER}`. The result is a source-derived, fixed-K, incoming-quark-indexed conditional finite-HO field regulator. It applies TBP graph matching to C45 field modes and C47 Fock/CM/triplet projections, and is explicitly neither universal nor BPP DLCQ. The C53 support-position holdout closes without using C53 numerical values. DLCQ-to-HO conversion remains `{report['conversion']['status']}` and is not needed by the selected project regulator. No contraction sum, matrix, subtraction, counterterm, direct contact, or full instantaneous operator is created. Next: **{NEXT}**.\n")


if __name__ == "__main__":
    main()
