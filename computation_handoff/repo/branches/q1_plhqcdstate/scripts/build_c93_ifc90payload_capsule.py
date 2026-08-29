"""Build the C93 recovered-preimage capsule from exact pinned C90 extracts."""
from __future__ import annotations

import gzip
from hashlib import sha256
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
RECOVERY = ROOT / "data/runtime/c93_ifc90payload/recovery"
OUT = ROOT / "data/runtime/c93_ifc90payload/capsule"
C90 = ROOT / "data/runtime/c90_ifboundrestart/pass_one"
SOURCES = {
    "C77": ROOT / "data/runtime/c77_qgembed9", "C78": ROOT / "data/runtime/c78_ifsupport2",
    "C80": ROOT / "data/runtime/c80_ifkernel2", "C82": ROOT / "data/runtime/c82_ifagg",
    "C87": ROOT / "data/authority/c87_canonical_c72_color_authority",
}


def canonical(value): return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def sha_bytes(value: bytes) -> str: return sha256(value).hexdigest()
def sha(path: Path) -> str: return sha_bytes(path.read_bytes())


def iter_gzip(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle: yield json.loads(line)


def write_gzip(path: Path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    digest = sha256(); count = 0
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as output:
            for record in records:
                line = canonical(record).encode() + b"\n"; output.write(line); digest.update(line); count += 1
    return count, digest.hexdigest(), sha(path)


def main() -> None:
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    a1, a2, b1, b2 = (RECOVERY / name for name in ("route_a_one.jsonl.gz", "route_a_two.jsonl.gz", "route_b_one.jsonl.gz", "route_b_two.jsonl.gz"))
    if sha(a1) != sha(a2) or sha(b1) != sha(b2): raise ValueError("pinned replay determinism failure")
    ledger = (json.loads(line) for line in (C90 / "ledger.jsonl").open())
    output_normal_forms = OUT / "normal_forms.jsonl.gz"
    def recovered_forms():
        for route_a, route_b, compact in zip(iter_gzip(a1), iter_gzip(b1), ledger):
            if route_a["pair"] != route_b["pair"] or route_a["normal_form"] != route_b["normal_form"] or route_a["proof"] != route_b["proof"]:
                raise ValueError("Route-A/B recovered content mismatch")
            if route_a["normal_form_root"] != compact["normal_form_root"] or route_a["proof"] != compact["proof"]:
                raise ValueError("C90 root/proof preimage mismatch")
            yield {"pair": route_a["pair"], "normal_form_root": route_a["normal_form_root"], "normal_form": route_a["normal_form"], "proof": route_a["proof"]}
    form_count, form_logical, form_file = write_gzip(output_normal_forms, recovered_forms())
    # Copy the original compact attestations as a descendant capsule component;
    # their C90 aggregate semantics are retained rather than reissued.
    pair_count, pair_logical, pair_file = write_gzip(OUT / "pair_attestations.jsonl.gz", (json.loads(line) for line in (C90 / "ledger.jsonl").open()))
    families = []
    for family, source in SOURCES.items():
        destination = OUT / "primitives" / family
        shutil.copytree(source, destination)
        records = []
        for path in sorted(destination.rglob("*")):
            if path.is_file(): records.append({"path": str(path.relative_to(OUT)), "sha256": sha(path), "bytes": path.stat().st_size})
        families.append({"family_id": family, "schema": "COPIED_FROZEN_AUTHORITY_FILESET_V1", "record_count": len(records), "records": records,
                         "scientific_root": next((json.loads((source / name).read_text()).get("aggregate_sha256") or json.loads((source / name).read_text()).get("scientific_root") for name in ("root.json", "manifest.json") if (source / name).exists()), None)})
    (OUT / "primitive_families.json").write_text(canonical(families) + "\n")
    core = ROOT / "src/deuteron_wigner/bridge/ifboundrestart/core.py"
    theorem = {"schema": "C90-C82-SEMANTIC-IR-V1", "normal_form": "C90-NORMAL-FORM-V1", "node_types": ["ATOM_TABLE", "ORDERED_RANGE", "ORDERED_UNION", "CARTESIAN_PRODUCT", "FILTER", "PERMUTE", "MAP_RECORD", "GROUP_TEMPLATE", "ANCESTRY_TEMPLATE", "BOUND_TEMPLATE", "STATUS_TEMPLATE"],
               "statement": "Equal normalized programs, primitive roots, schemas, cardinalities, order, and typed map expressions imply identical C88 sequences.",
               "checker_source_sha256": sha(core), "checker_api": "check_proof", "no_expanded_records": True}
    (OUT / "theorem.json").write_text(canonical(theorem) + "\n")
    c90_index = json.loads((C90 / "index.json").read_text())
    inventory = []
    for path in sorted(OUT.rglob("*")):
        if path.is_file() and path.name != "manifest.json": inventory.append({"path": str(path.relative_to(OUT)), "sha256": sha(path), "bytes": path.stat().st_size})
    root_body = {"schema": "C93-C90-RECOVERED-PREIMAGE-CAPSULE-V1", "C90_commit": "ac622ab358b83f090717d7e7fa179b58f18f526d", "C90_aggregate": c90_index["aggregate"],
                 "payload_provenance": "DESCENDANT_RECOVERED_PREIMAGE_OF_C90_FROZEN_SCIENTIFIC_ROOTS", "original_c90_runtime_payload_claim": "NOT_CLAIMED",
                 "normal_forms": {"records": form_count, "logical_sha256": form_logical, "file_sha256": form_file}, "pair_attestations": {"records": pair_count, "logical_sha256": pair_logical, "file_sha256": pair_file},
                 "route_a_file_sha256": sha(a1), "route_b_file_sha256": sha(b1), "inventory": inventory}
    root_body["capsule_root"] = sha_bytes(canonical(root_body).encode())
    (OUT / "manifest.json").write_text(canonical(root_body) + "\n")
    print(json.dumps({"capsule_root": root_body["capsule_root"], "forms": form_count, "pairs": pair_count, "C90_aggregate": c90_index["aggregate"]}, sort_keys=True))


if __name__ == "__main__": main()
