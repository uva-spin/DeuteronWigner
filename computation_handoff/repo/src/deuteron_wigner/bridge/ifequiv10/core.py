"""Read-only compact C103 comparison ledger; it never recompiles science."""
from __future__ import annotations
import gzip
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c103_ifequiv10"
SCHEMA = "C103-IFEQUIV10-PUBLIC-EQUIVALENCE-V1"

def _plain(v: Any) -> Any:
    if hasattr(v, "items"): return {str(k): _plain(x) for k,x in v.items()}
    if isinstance(v, (tuple,list)): return [_plain(x) for x in v]
    return v
def _canonical(v: Any) -> str: return json.dumps(_plain(v), sort_keys=True, separators=(",",":"), ensure_ascii=True, allow_nan=False)
def _sha(v: Any) -> str: return sha256(_canonical(v).encode()).hexdigest()
def _freeze(v: Any) -> Any:
    if isinstance(v,dict): return MappingProxyType({k:_freeze(x) for k,x in v.items()})
    if isinstance(v,list): return tuple(_freeze(x) for x in v)
    return v
def _safe(path: Path) -> Path:
    p=path.resolve(); r=RUNTIME.resolve()
    if not str(p).startswith(str(r)+"/") or p.is_symlink() or not p.is_file(): raise ValueError("unsafe C103 runtime path")
    return p
def _manifest() -> dict[str,Any]:
    body=json.loads(_safe(RUNTIME/"manifest.json").read_text())
    if body.get("schema") != SCHEMA or _sha({k:v for k,v in body.items() if k!="C103_PACKAGE_ROOT"}) != body.get("C103_PACKAGE_ROOT"): raise ValueError("C103 package root mismatch")
    for item in body.get("runtime_inventory",[]):
        p=_safe(RUNTIME/item["path"])
        if p.stat().st_size != item["bytes"] or sha256(p.read_bytes()).hexdigest()!=item["sha256"]: raise ValueError("C103 runtime inventory mismatch")
    return body
def load_verified_historical_descendant_equivalence() -> Any: return _freeze(_manifest())
def verify_historical_descendant_equivalence_root() -> Any:
    m=_manifest()
    return _freeze({"pass":True,"C103_PACKAGE_ROOT":m["C103_PACKAGE_ROOT"],"FACTORIZED_SEMANTIC_EQUIVALENCE_CERTIFICATE_ROOT":m["C103_HISTORICAL_DESCENDANT_EQUIVALENCE_CERTIFICATE_ROOT"]})
def scientific_equivalence_decision() -> str: return str(_manifest()["scientific_decision"])
def _pairs():
    with gzip.open(_safe(RUNTIME/"pair_ledger.jsonl.gz"),"rt",encoding="utf-8") as f:
        for line in f: yield json.loads(line)
def pair_equivalence(pair_id: str,resolution: str)->Any:
    for row in _pairs():
        if row["pair"]["id"]==pair_id and row["pair"]["resolution"]==resolution: return _freeze(row)
    raise KeyError(pair_id)
def historical_pair_attestation(pair_id: str,resolution: str)->Any:
    r=_plain(pair_equivalence(pair_id,resolution)); return _freeze({"pair":r["pair"],"historical_program_root":r["historical_program_root"],"logical_count":r["logical_count"]})
def descendant_pair_attestation(pair_id: str,resolution: str)->Any:
    r=_plain(pair_equivalence(pair_id,resolution)); return _freeze({"pair":r["pair"],"descendant_program_root":r["descendant_program_root"],"summary":r["summary"]})
def pair_equivalence_proof(pair_id: str,resolution: str)->Any:
    r=_plain(pair_equivalence(pair_id,resolution)); return _freeze({"pair":r["pair"],"status":r["comparison_status"],"C103_equivalence_certificate_root":r["C103_equivalence_certificate_root"]})
def primitive_equivalence(family_id: str,record_id: str)->Any:
    body=json.loads(_safe(RUNTIME/"primitive_certificates.json").read_text())
    for row in body["records"]:
        if row["family_id"]==family_id and row["record_id"]==record_id:return _freeze(row)
    raise KeyError(record_id)
def diagnose_pair_difference(pair_id: str,resolution: str,*,max_bytes: int=4096)->Any:
    if max_bytes < 256: raise ValueError("diagnostic byte cap too small")
    r=_plain(pair_equivalence(pair_id,resolution))
    return _freeze({"pair":r["pair"],"difference":None,"classification":r["difference_classification"],"expanded_records":0,"max_bytes":max_bytes,"bounded":True})
