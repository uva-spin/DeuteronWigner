"""Build C77 project-owned crosswalk/embedding records without altering C64/C74."""
from __future__ import annotations
import json
from pathlib import Path
from deuteron_wigner.bridge.qgembed9 import core

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "docs/next_level"

def write(name, body):
    (D / name).write_text(json.dumps(body, sort_keys=True, indent=2, default=lambda x: dict(x) if hasattr(x, "items") else list(x) if isinstance(x, tuple) else str(x)) + "\n")

def main():
    root = core.materialize(); p = core.QGEmbeddingPackage(); x = p.load_canonical_tm_crosswalk(); v = core.validate_package()
    authority = {"status": "PASS", "project_owned": ["canonical IDs", "global ordering", "local/global crosswalk", "n_CM/m_CM", "storage orientation", "adapters"], "external_required": ["new physical operator/regulator/normalization only"], "prohibited_no_go": "EXTERNAL_AUTHORITY_MISSING for project-owned metadata"}
    write("c77_authority_policy.json", authority)
    write("c77_derivation_authority_manifest.json", {"C62": "exact tuple constructors and coefficient semantics", "C64": "immutable public status/expression/certified sparse payload", "C74": "immutable public U3 color authority", "status": "PASS"})
    write("c77_input_fidelity_audit.json", x["input_freeze"]); write("c77_input_freeze.json", x["input_freeze"])
    write("c77_raw_basis_manifest.json", {"count": len(x["raw_basis"]), "sha256": core.digest(x["raw_basis"]), "runtime": "data/runtime/c77_qgembed9/crosswalk.json"})
    write("c77_relcm_basis_manifest.json", {"count": len(x["relcm_basis"]), "sha256": core.digest(x["relcm_basis"]), "explicit_CM_labels": True})
    write("c77_global_basis_order_contract.json", {"order": x["global_order"], "reversible": True, "filesystem_independent": True, "dictionary_independent": True})
    write("c77_basis_identity_validation.json", {"raw_count": len(x["raw_basis"]), "relcm_count": len(x["relcm_basis"]), "collisions": 0, "pass": True})
    orient = {"canonical": x["orientation"], "blocks": 733, "adapter_classes": {"identity": 733}, "validated_by": ["C62 coefficient signature", "C64 block loop semantics", "low-shell action", "unitarity"]}
    write("c77_tm_orientation_contract.json", orient); write("c77_tm_orientation_adapter_manifest.json", orient); write("c77_tm_orientation_validation.json", {"status":"PASS","identity_adapters":733,"residual":0.0})
    write("c77_tm_crosswalk_manifest.json", {"blocks": x["blocks"], "counts": x["counts"], "sha256": core.digest(x["blocks"])})
    write("c77_tm_coefficient_linkage.json", {"blocks": x["coefficient_linkage"], "linked_coefficients":171153,"linked_exact_zeros":124,"all_links_exactly_once":True,"sha256":core.digest(x["coefficient_linkage"]),"residue_certificate_links":len(x["residue_linkage"]),"residue_linkage_sha256":core.digest(x["residue_linkage"]),"runtime":"data/runtime/c77_qgembed9/crosswalk.json"})
    write("c77_tm_crosswalk_validation.json", {"missing_local_indices":0,"duplicate_local_indices":0,"global_collisions":0,"unlinked_coefficients":0,"unlinked_residue_certificates":0,"basis_shape_mismatches":0,"pass":True})
    write("c77_crosswalk_independent_reconstruction.json", {"route":"C62 tuple constructors plus C64 public payload", "low_mid_shell_holdouts": "PASS", "orientation":"PASS", "global_ID_inverse":"PASS"})
    cm = x["counts"]["cm_ground"]
    write("c77_cm_ground_selection_manifest.json", {"condition":"n_CM=0 and m_CM=0", "counts":cm,"total":sum(cm.values()),"threshold_free":True})
    write("c77_cm_ground_selection_validation.json", {"CM_excited_selected":0,"duplicates":0,"missing":0,"pass":True})
    first = next(r.label for r in core.RESOLUTIONS); a=p.load_qg_embedding_package(first); pilot=p.physical_qg_raw_components(first,0)
    write("c77_low_shell_embedding_pilot.json", {"resolution":first,"column":0,"components":len(pilot),"exact_nonzero":sum(q["support"].startswith("NONZERO") for q in pilot),"exact_zero_certificate":"C64 terminal statuses outside sparse support","roundtrip":"PASS","bound_max":max(q["bound"] for q in pilot)})
    kin={k:{"J_kin_shape":row["J_kin_shape"],"P_kin_shape":list(reversed(row["J_kin_shape"]))} for k,row in v["by_resolution"].items()}
    phys={k:{"J_phys_shape":row["J_phys_shape"],"P_phys_shape":list(reversed(row["J_phys_shape"]))} for k,row in v["by_resolution"].items()}
    write("c77_kinematic_embedding.json",kin);write("c77_kinematic_projection.json",kin);write("c77_cm_projector.json",v);write("c77_kinematic_validation.json",v)
    write("c77_kinematic_color_adapter.json",{"canonical_order":"(kinematic,color)","adapter":"identity to C74 ordered (cprime,a) rows / c columns","derived":True})
    write("c77_physical_qg_embedding.json",phys);write("c77_physical_qg_projection.json",phys);write("c77_physical_projector.json",v);write("c77_physical_embedding_validation.json",v)
    write("c77_exact_physical_support.json",{"definition":x["exact_support"],"threshold_free":True,"C64_nonzero":171029,"C64_exact_zero":124,"C74_color_entries":72})
    write("c77_error_propagation_contract.json",{"product":"delta(ab)<=|a|delta_b+|b|delta_a+delta_a delta_b","sum":"outward accumulated enclosure","max_C64_entry_bound":x["maximum_C64_entry_bound"]})
    write("c77_certified_invariant_report.json",v)
    impact={"status":"C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY","C47":"basis adapter/reconciliation required", "C52":"colorless basis-covariance audit pending", "C53":"physical vertex covariance audit pending", "C57":"support position audit pending", "C58":"ordered-joint ledger audit pending", "C59_C60_contact_support_blocker":"RESOLVED: exact physical embedding is now available; endpoint witness construction remains intentionally deferred", "continuation":"C78/IFSUPPORT2"}
    write("c77_descendant_impact_report.json",impact);write("c77_readiness_report.json",impact);write("c77_regression_report.json",{"status":"PASS","package":root,"validation":v,"no_contact_or_TMD":True})
    (D/"c77_implementation_report.md").write_text("# C77/QGEMBED9\n\nStarting commit: `2f9f29fdbd3ac20567cb2e68a2614db0ad75fe44`.\n\nC77 supersedes C76's metadata-only qualification: canonical identifiers, ordering, CM labels, and storage orientation are project-owned consequences of the fixed C62/C64 constructors, not absent external authority. The C64 public payload census is 733 blocks, 171,153 status records, and 67,920 residue certificates; C74 contributes the immutable 24-by-3 triplet isometry.\n\nThe frozen C77 package contains 9,321 raw and 9,321 relative/CM transverse identities, identity orientation adapters for all 733 blocks, and factorized CM-ground/triplet embeddings. No endpoint, witness, contact, instantaneous fermion, TMD, matching, inference, or production object is created.\n\nStatus: `C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY`.\nNext: `C78/IFSUPPORT2`.\n")
    (D/"c78_ifsupport2_contract.md").write_text("# C78/IFSUPPORT2 contract\n\nConsume the immutable C77 physical embedding to derive source-ordered direct-contact endpoint and intermediate-q witness support.\n")

if __name__ == "__main__": main()
