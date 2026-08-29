"""Fail-closed C65 gate for the required frozen C53 triplet isometry."""
from __future__ import annotations
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from ..qgtm2 import core as c64

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "6f74663f3a70e853940665c30b1561766b6b75a3"
STATUS = "C65_QG_TRIPLET_EMBEDDING_INCOMPLETE"
NEXT = "C66/QGCOLOR2 — materialize and hash-verify the frozen C53 24-by-3 triplet isometry import contract"

def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())

def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()

def c64_read_only_import() -> dict[str, Any]:
    """Verify C64 through its loader; no coefficient generator is invoked."""
    index = c64._load_index()
    c64.validate_index_contract(index)
    blocks = c64.list_tm_blocks()
    if len(blocks) != 733 or sum(b["candidate_count"] for b in blocks) != 171153:
        raise AssertionError("C64 block/status census mismatch")
    residues = index["residue_certificates"]
    if residues["total"] != 67920 or [x["count"] for x in residues["rows"]] != [4032, 15840, 48048]:
        raise AssertionError("C64 residue census mismatch")
    # Probe immutable objects from each resolution without regenerating C64.
    probes = []
    for resolution in ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50"):
        block = next(x for x in blocks if x["resolution_id"] == resolution)
        support = c64.load_tm_block_support(block["block_id"])
        sparse = c64.load_tm_block_certified_sparse(block["block_id"])
        probes.append({"resolution": resolution, "block_id": block["block_id"], "immutable": not support["array"].flags.writeable and not sparse["data_real"].flags.writeable,
                       "shape": list(sparse["shape"]), "basis_hash": block["combined_basis_order_sha256"]})
    return {"status": "PASS", "blocks": len(blocks), "coefficient_status_records": sum(b["candidate_count"] for b in blocks),
            "residue_certificates": residues["total"], "expression_merkle_sha256": index["expression_merkle_sha256"],
            "support_aggregate_sha256": index["support_aggregate_sha256"], "loader_calls_C62_generator": False,
            "immutable_probes": probes, "runtime_paths_verified": True}

def c53_triplet_import_audit() -> dict[str, Any]:
    inventory = _read("c53_numerical_object_inventory.json")
    # C47 did not export the filename anticipated by the C65 prompt; its
    # committed physical-qg manifest is the actual hash/shape authority.
    basis = _read("c47_physical_qg_basis_manifest.json")
    required_hash, required_shape = basis["triplet_isometry_hash"], basis["triplet_isometry_shape"]
    matching = [x for x in inventory["objects"] if x.get("array_sha256") == required_hash or x.get("shape") == required_shape and "isometry" in x.get("name", "").lower()]
    paths = [x.get("runtime_path") for x in matching if x.get("runtime_path")]
    existing = [p for p in paths if (ROOT / p).exists()]
    return {"status": "FAIL", "required_object": "C53 frozen 24-by-3 triplet isometry U3", "required_hash": required_hash,
            "required_shape": required_shape, "C53_inventory_matching_records": matching, "runtime_paths_declared": paths,
            "runtime_paths_existing": existing, "raw_emission_E": next(x for x in inventory["objects"] if x["name"] == "raw_emission_E"),
            "projectors": [x["name"] for x in inventory["objects"] if x["name"].startswith("triplet_projector")],
            "blocker": "C53's committed inventory has no hash-verified runtime path for the frozen U3 isometry. raw_emission_E is a differently normalized SU(3) emission map (E†E=C_F I), while the two stored projectors are 24-by-24; C65 may not derive, normalize, or substitute either while claiming a read-only C53 U3 import."}

@lru_cache(maxsize=1)
def preflight() -> dict[str, Any]:
    c64_import = c64_read_only_import(); color = c53_triplet_import_audit()
    assert c64_import["status"] == "PASS" and color["status"] == "FAIL" and not color["runtime_paths_existing"]
    return {"baseline": BASELINE, "status": STATUS, "next": NEXT, "C64_import": c64_import, "C53_triplet_import": color,
            "unavailable": {"kinematic_color_permutation": True, "triplet_embedding": True, "physical_embedding": True,
                            "support_ledger": True, "historical_adapter": True, "descendant_impact": True},
            "no_C64_regeneration": True, "no_threshold": True, "no_contact_or_endpoint": True}

def validate_c65(value: dict[str, Any]) -> bool:
    expected = preflight()
    return value == expected and value["status"] == STATUS

def mutate_live_c65(i: int) -> dict[str, Any]:
    value = deepcopy(preflight()); c = i % 20
    if c == 0: value["C64_import"]["blocks"] = 0
    elif c == 1: value["C64_import"]["coefficient_status_records"] = 0
    elif c == 2: value["C64_import"]["residue_certificates"] = 0
    elif c == 3: value["C64_import"]["loader_calls_C62_generator"] = True
    elif c == 4: value["C64_import"]["immutable_probes"][0]["immutable"] = False
    elif c == 5: value["C53_triplet_import"]["required_hash"] = "bad"
    elif c == 6: value["C53_triplet_import"]["required_shape"] = [3, 24]
    elif c == 7: value["C53_triplet_import"]["runtime_paths_existing"] = ["derived"]
    elif c == 8: value["C53_triplet_import"]["raw_emission_E"]["name"] = "U3"
    elif c == 9: value["C53_triplet_import"]["projectors"] = []
    elif c == 10: value["C53_triplet_import"]["blocker"] = "none"
    elif c == 11: value["unavailable"]["triplet_embedding"] = False
    elif c == 12: value["unavailable"]["physical_embedding"] = False
    elif c == 13: value["no_C64_regeneration"] = False
    elif c == 14: value["no_threshold"] = False
    elif c == 15: value["no_contact_or_endpoint"] = False
    elif c == 16: value["next"] = "C66/IFSUPPORT2"
    elif c == 17: value["status"] = "C65_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY"
    elif c == 18: value["baseline"] = "wrong"
    else: value["C53_triplet_import"]["status"] = "PASS"
    return value
