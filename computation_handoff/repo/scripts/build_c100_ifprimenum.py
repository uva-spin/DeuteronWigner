#!/usr/bin/env python3
"""Build C100's metadata-only primitive enumeration package.

This builder is the sole C100 operation allowed to inspect C98's persisted
direct-location index.  The resulting runtime API never opens that index.
"""
from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifhistpublic2 import core as c98

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/runtime/c98_ifhistpublic2"
OUT = ROOT / "data/runtime/c100_ifprimenum"
ORDER = ("C77", "C78", "C80", "C82", "C87")

def canonical(value): return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def digest(value): return sha256(canonical(value).encode()).hexdigest()
def file_sha(path): return sha256(path.read_bytes()).hexdigest()
def write_atomic(path, value):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(canonical(value) + "\n")
    temporary.replace(path)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    c98_manifest = json.loads((SOURCE / "manifest.json").read_text())
    index = json.loads((SOURCE / "primitive_index.json").read_text())
    if digest({k: v for k, v in c98_manifest.items() if k != "root"}) != c98_manifest.get("root"):
        raise ValueError("C98 manifest authentication failure")
    if digest({"schema": index.get("schema"), "records": index.get("records")}) != index.get("root") or index["root"] != c98_manifest["primitive_index_root"]:
        raise ValueError("C98 primitive-index authentication failure")
    if tuple(item["family_id"] for item in c98_manifest["families"]) != ORDER:
        raise ValueError("C98 primitive family ordering failure")
    records = []
    families = []
    global_sequence = 0
    for expected, summary in enumerate(c98_manifest["families"]):
        family_id = summary["family_id"]
        if family_id != ORDER[expected]: raise ValueError("unexpected C98 family")
        family = c98.historical_primitive_family(family_id)
        source_rows = [row for row in index["records"] if row["family_id"] == family_id]
        if len(source_rows) != summary["records"] or len(source_rows) != len(family["records"]): raise ValueError("C98 family census mismatch")
        if [row["sequence"] for row in source_rows] != list(range(len(source_rows))): raise ValueError("C98 family sequence mismatch")
        public_rows = []
        for local, (source_row, record) in enumerate(zip(source_rows, family["records"])):
            if source_row["record_id"] != record["path"] or digest(dict(record)) != source_row["record_digest"]: raise ValueError("C98 record identity mismatch")
            row = {"family_id": family_id, "record_id": source_row["record_id"], "global_sequence": global_sequence, "family_sequence": local, "record_digest": source_row["record_digest"], "family_root": family["scientific_root"], "C98_content_location_identity": {"C98_primitive_index_root": index["root"], "sequence": local}, "inclusion": source_row["inclusion"]}
            row["identity_root"] = digest(row)
            records.append(row); public_rows.append(row); global_sequence += 1
        families.append({"family_id": family_id, "schema": family["schema"], "sequence": expected, "count": len(public_rows), "scientific_family_root": family["scientific_root"], "enumeration_root": digest(public_rows), "first_record_identity": public_rows[0]["identity_root"], "last_record_identity": public_rows[-1]["identity_root"], "C94_package_root": c98_manifest["C94_package_root"], "C98_package_root": c98_manifest["root"]})
    domain = {"schema": "C100-PRIMITIVE-ENUMERATION-V1", "family_order": list(ORDER), "families": families, "records": records, "C98_package_root": c98_manifest["root"], "C94_package_root": c98_manifest["C94_package_root"], "C90_aggregate": c98_manifest["C90_aggregate"], "C93_capsule_root": c98_manifest["C93_capsule_root"], "C97_capsule_root": c98_manifest["C97_capsule_root"], "no_scientific_content_copy": True}
    domain["enumeration_root"] = digest(domain)
    write_atomic(OUT / "domain.json", domain)
    inventory = []
    for path in (SOURCE / "manifest.json", SOURCE / "primitive_index.json"):
        inventory.append({"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": file_sha(path)})
    domain_path = OUT / "domain.json"
    manifest = {"schema": "C100-PRIMITIVE-ENUMERATION-V1", "C100_api": "ifprimenum-v1", "C98_package_root": c98_manifest["root"], "C98_primitive_index_root": index["root"], "C94_package_root": c98_manifest["C94_package_root"], "C90_aggregate": c98_manifest["C90_aggregate"], "C93_capsule_root": c98_manifest["C93_capsule_root"], "C97_capsule_root": c98_manifest["C97_capsule_root"], "enumeration_root": domain["enumeration_root"], "C100_PRIMITIVE_DOMAIN_ENUMERATION_ROOT": domain["enumeration_root"], "families": len(families), "records": len(records), "source_inventory": inventory, "runtime_inventory":[{"path":"domain.json","bytes":domain_path.stat().st_size,"sha256":file_sha(domain_path)}], "no_scientific_content_copy": True, "runtime_files": ["manifest.json", "domain.json"]}
    manifest["package_root"] = digest(manifest)
    write_atomic(OUT / "manifest.json", manifest)
    print(manifest["package_root"])

if __name__ == "__main__": main()
