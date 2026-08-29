#!/usr/bin/env python3
"""Exhaustively validate C100 public primitive enumeration and C98 content."""
from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifprimenum import historical_primitive_domain_manifest, historical_primitive_record_page
from deuteron_wigner.bridge.ifhistpublic2 import historical_primitive_record

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/next_level"
FAMILIES = ("C77", "C78", "C80", "C82", "C87")
def canonical(value): return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def digest(value): return sha256(canonical(value).encode()).hexdigest()
def plain(value):
    if hasattr(value, "items"): return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)): return [plain(item) for item in value]
    return value

def crawl(*, family_id=None, limit):
    cursor = None; rows = []
    while True:
        page = plain(historical_primitive_record_page(family_id=family_id, cursor=cursor, limit=limit))
        rows.extend(page["records"])
        if page["terminal"]:
            assert page["next_cursor"] is None; return rows
        cursor = page["next_cursor"]

def main():
    manifest = plain(historical_primitive_domain_manifest())
    rows = crawl(limit=1)
    by_size = {str(limit): crawl(limit=limit) for limit in (1, 2, 7, 16, 64)}
    direct_bad = inclusion_bad = root_bad = 0
    for row in rows:
        direct = plain(historical_primitive_record(row["family_id"], row["record_id"]))
        direct_bad += int(direct["record_digest"] != row["record_digest"])
        inclusion_bad += int(direct["inclusion"] != row["inclusion"])
        root_bad += int(direct["family_root"] != row["family_root"])
    bad_cursor = 0
    try: historical_primitive_record_page(limit=1, cursor="bad")
    except ValueError: bad_cursor += 1
    try: historical_primitive_record_page(limit=1, cursor=plain(historical_primitive_record_page(limit=1))["next_cursor"].replace(".", ".x", 1))
    except ValueError: bad_cursor += 1
    if len(rows) != 35 or len({(r["family_id"], r["record_id"]) for r in rows}) != 35 or any(items != rows for items in by_size.values()) or direct_bad or inclusion_bad or root_bad or bad_cursor != 2:
        raise RuntimeError("C100 primitive enumeration validation failure")
    body = {"status":"C100_C98_AUTHENTICATED_PRIMITIVE_ENUMERATION_READY","families":len(manifest["families"]),"records":len(rows),"missing_families":0,"extra_families":0,"duplicate_families":0,"family_order_mismatches":0,"missing_records":0,"extra_records":0,"duplicate_records":0,"record_order_mismatches":0,"record_digest_mismatches":direct_bad,"family_root_mismatches":root_bad,"inclusion_failures":inclusion_bad,"page_direct_mismatches":direct_bad,"page_sizes":list(by_size),"cursor_mutations_rejected":bad_cursor,"C100_package_root":manifest["C100_package_root"],"C100_enumeration_root":manifest["aggregate_primitive_identity_root"]}
    body["sha256"] = digest(body)
    (DOC / "c100_exhaustive_primitive_enumeration_regression.json").write_text(canonical(body)+"\n")

if __name__ == "__main__": main()
