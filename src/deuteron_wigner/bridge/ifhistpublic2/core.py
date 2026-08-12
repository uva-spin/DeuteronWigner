"""Public-only C98 facade over immutable C93/C94/C97 payloads."""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifequivapi2 import (
    expansion_theorem_specification as _theorem,
    historical_pair_count as _pair_count,
    historical_primitive_family as _family,
    load_verified_c93_public_authority,
    verify_factorized_expansion_equivalence,
)
from ..ifproofinput.normal_form_index import load_verified_normal_form_key_index
from ..ifproofinput.zran_runtime import open_verified_zran_reader
from ..ifproofinput.proof_input_index import Reader as ProofReader
from ..ifproofinput import verify_c90_proof_input_capsule

ROOT = Path(__file__).resolve().parents[4]
C93 = ROOT / "data/runtime/c93_ifc90payload/capsule"
C97 = ROOT / "data/runtime/c97_ifproofinput"
RUNTIME = ROOT / "data/runtime/c98_ifhistpublic2"
SCHEMA = "C98-HISTORICAL-THEOREM-INPUT-PUBLIC-V1"
COUNTS = {"K9_2_N8_b0.40": 16224, "K11_2_N10_b0.45": 43350, "K13_2_N12_b0.50": 95256}

def _plain(value: Any) -> Any:
    if isinstance(value, MappingProxyType) or hasattr(value, "items"): return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, tuple) or isinstance(value, list): return [_plain(item) for item in value]
    return value
def _canonical(value: Any) -> str: return json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def _sha(value: Any) -> str: return sha256(_canonical(value).encode()).hexdigest()
def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    return value
def _safe(path: Path, root: Path) -> Path:
    candidate = path.resolve()
    if not str(candidate).startswith(str(root.resolve()) + "/") or candidate.is_symlink() or not candidate.is_file(): raise ValueError("unsafe C98 payload path")
    return candidate

@lru_cache(maxsize=1)
def _c98_manifest() -> dict[str, Any]:
    path = _safe(RUNTIME / "manifest.json", RUNTIME)
    body = json.loads(path.read_text())
    if body.get("schema") != SCHEMA: raise ValueError("unknown C98 schema")
    if _sha({key: value for key, value in body.items() if key != "root"}) != body.get("root"): raise ValueError("C98 package root mismatch")
    return body

@lru_cache(maxsize=1)
def _pair_order() -> tuple[MappingProxyType, ...]:
    body = json.loads(_safe(RUNTIME / "pair_order.json", RUNTIME).read_text())
    if body.get("schema") != "C98-PAIR-ORDER-INDEX-V1" or _sha({"schema": body["schema"], "records": body["records"]}) != body.get("root") or body["root"] != _c98_manifest()["pair_order_root"]: raise ValueError("C98 pair-order index mismatch")
    if len(body["records"]) != 154830 or any(item["global_sequence"] != n for n, item in enumerate(body["records"])): raise ValueError("C98 pair-order census/order mismatch")
    return tuple(_freeze(item) for item in body["records"])

@lru_cache(maxsize=1)
def _normal_reader() -> Any:
    source = C93 / "normal_forms.jsonl.gz"; transport = C97 / "transport"
    return load_verified_normal_form_key_index(source, transport / "normal_forms.keyindex", open_verified_zran_reader(source, transport / "normal_forms.zran", transport / "c97_zran"))

@lru_cache(maxsize=3)
def _proof_reader(resolution: str) -> Any:
    transport = C97 / "proof_transport"; source = C97 / "capsule" / f"route_b_indexed_{resolution}.jsonl.gz"
    return ProofReader(source, transport / f"{resolution}.index", open_verified_zran_reader(source, transport / f"{resolution}.zran", transport / "c97_zran"))

@lru_cache(maxsize=1)
def load_verified_historical_theorem_input_authority() -> Any:
    public = load_verified_c93_public_authority(); c97 = verify_c90_proof_input_capsule(); c98 = _c98_manifest()
    if c98["C93_capsule_root"] != public["capsule_root"] or c98["C94_package_root"] != public["package_root"] or c98["C97_capsule_root"] != c97["capsule_root"]: raise ValueError("C98 authority-chain mismatch")
    return _freeze({"schema": SCHEMA, "C90_aggregate": public["C90_aggregate"], "C93_capsule_root": public["capsule_root"], "C94_package_root": public["package_root"], "C97_operand_root": c97["operand_root"], "C97_capsule_root": c97["capsule_root"], "C98_root": c98["root"], "pairs": public["pairs"], "pass": True})

def verify_historical_theorem_input_authority() -> Any: return load_verified_historical_theorem_input_authority()
def historical_pair_count(resolution: str | None = None) -> int: return sum(COUNTS.values()) if resolution is None else COUNTS[resolution]

def historical_pair_normal_form(pair_id: str, resolution: str) -> Any:
    authority = load_verified_historical_theorem_input_authority()
    proof = dict(_proof_reader(resolution).lookup(resolution, pair_id))
    normal_root = proof["route_b_normal_form"]["root"]
    loaded = _normal_reader().lookup_normal_form(resolution=resolution, pair_id=pair_id, normal_form_root=normal_root)
    node = dict(loaded["normal_form"])
    proof_pair = {key: value for key, value in proof["pair"].items() if key not in ("global_sequence", "resolution_sequence")}
    if node["pair"] != proof_pair or node["primitive_roots"] != proof["primitive_equivalence"]["bindings"]: raise ValueError("C98 normal-form/proof-input binding mismatch")
    body = {"schema": "C98-PUBLIC-HISTORICAL-NORMAL-FORM-V1", "pair": node["pair"], "global_sequence": loaded["global_sequence"], "resolution_sequence": proof["pair"]["resolution_sequence"], "normal_form": node, "normal_form_root": node["normal_form_root"], "transport": {"key": dict(loaded["key"]), "line_offset": loaded["line_offset"], "line_length": loaded["line_length"]}, "C90_aggregate": authority["C90_aggregate"], "C93_capsule_root": authority["C93_capsule_root"], "C94_package_root": authority["C94_package_root"], "C97_operand_root": authority["C97_operand_root"], "C97_capsule_root": authority["C97_capsule_root"], "C98_root": authority["C98_root"]}
    body["return_root"] = _sha({"normal_form_root": body["normal_form_root"], "global_sequence": body["global_sequence"], "resolution_sequence": body["resolution_sequence"], "C98_root": body["C98_root"]}); return _freeze(body)

def historical_pair_proof_inputs(pair_id: str, resolution: str) -> Any:
    authority = load_verified_historical_theorem_input_authority()
    record = dict(_proof_reader(resolution).lookup(resolution, pair_id))
    if set(record).intersection({"proof_result", "expected_status", "proof_certificate", "comparison_outcome"}): raise ValueError("result-bearing C97 input")
    body = {"schema": "C98-PUBLIC-HISTORICAL-PROOF-INPUT-V1", "proof_input": record, "C90_aggregate": authority["C90_aggregate"], "C93_capsule_root": authority["C93_capsule_root"], "C94_package_root": authority["C94_package_root"], "C97_operand_root": authority["C97_operand_root"], "C97_capsule_root": authority["C97_capsule_root"], "C98_root": authority["C98_root"]}
    body["return_root"] = _sha({"proof_input_root": record["proof_input_root"], "C97_operand_root": authority["C97_operand_root"], "C98_root": authority["C98_root"]}); return _freeze(body)

@lru_cache(maxsize=1)
def _primitive_index() -> dict[tuple[str, str], dict[str, Any]]:
    body = json.loads(_safe(RUNTIME / "primitive_index.json", RUNTIME).read_text()); result = {}
    if body.get("schema") != "C98-PRIMITIVE-DIRECT-INDEX-V1" or _sha({"schema": body.get("schema"), "records": body.get("records")}) != body.get("root") or body.get("root") != _c98_manifest()["primitive_index_root"]:
        raise ValueError("C98 primitive-index authentication mismatch")
    for entry in body["records"]:
        key = (entry["family_id"], entry["record_id"])
        if key in result: raise ValueError("duplicate C98 primitive key")
        result[key] = entry
    return result

def historical_primitive_family(family_id: str) -> Any: return _family(family_id)

def historical_primitive_record(family_id: str, record_id: str) -> Any:
    authority = load_verified_historical_theorem_input_authority(); entry = _primitive_index().get((family_id, record_id))
    if entry is None: raise KeyError(record_id)
    family = _family(family_id); record = family["records"][entry["sequence"]]
    if entry["inclusion"] != _sha({"family": family_id, "root": family["scientific_root"], "sequence": entry["sequence"], "record": entry["record_digest"]}): raise ValueError("C98 primitive inclusion mismatch")
    if _sha(record) != entry["record_digest"] or record.get("path") != record_id: raise ValueError("C98 primitive record mismatch")
    body = {"schema": "C98-PUBLIC-HISTORICAL-PRIMITIVE-V1", "family_id": family_id, "family_schema": family["schema"], "family_root": family["scientific_root"], "record_id": record_id, "sequence": entry["sequence"], "record": dict(record), "record_digest": entry["record_digest"], "inclusion": entry["inclusion"], "C90_aggregate": authority["C90_aggregate"], "C93_capsule_root": authority["C93_capsule_root"], "C94_package_root": authority["C94_package_root"], "C97_operand_root": authority["C97_operand_root"], "C97_capsule_root": authority["C97_capsule_root"], "C98_root": authority["C98_root"]}
    body["return_root"] = _sha(body); return _freeze(body)

def expansion_theorem_specification() -> Any: return _theorem()
