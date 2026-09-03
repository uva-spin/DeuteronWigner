from __future__ import annotations

from pathlib import Path

import pytest

from deuteron_wigner.bridge.ifequivapi2 import load_verified_c93_public_authority
from deuteron_wigner.bridge.ifproofinput.normal_form_index import (
    build_normal_form_key_index,
    load_verified_normal_form_key_index,
)
from deuteron_wigner.bridge.ifproofinput.zran_runtime import (
    build_persistent_zran_index,
    compile_adapter,
    open_verified_zran_reader,
)

SOURCE = Path("data/runtime/c93_ifc90payload/capsule/normal_forms.jsonl.gz")
FIRST = ("K9_2_N8_b0.40", "C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0", "ba5f92f8d9f0bd9cfeff0662490015089b04770e76d59528dd2d71fa14b5fd0e")

def test_c93_normal_form_key_index_and_direct_lookup(tmp_path: Path):
    if not SOURCE.exists(): pytest.skip("C93 runtime unavailable")
    adapter = tmp_path / "adapter"; compile_adapter(adapter)
    transport = build_persistent_zran_index(SOURCE, tmp_path / "transport.zran", adapter, span=1 << 20)
    authority = load_verified_c93_public_authority()
    one = build_normal_form_key_index(SOURCE, tmp_path / "one.idx", transport, c93_root=authority["capsule_root"], c94_root=authority["package_root"])
    two = build_normal_form_key_index(SOURCE, tmp_path / "two.idx", transport, c93_root=authority["capsule_root"], c94_root=authority["package_root"])
    assert (tmp_path / "one.idx").read_bytes() == (tmp_path / "two.idx").read_bytes()
    reader = load_verified_normal_form_key_index(SOURCE, tmp_path / "one.idx", open_verified_zran_reader(SOURCE, tmp_path / "transport.zran", adapter))
    record = reader.lookup_normal_form(resolution=FIRST[0], pair_id=FIRST[1], normal_form_root=FIRST[2])
    assert record["global_sequence"] == 0
    assert record["normal_form"]["normal_form_root"] == FIRST[2]
    with pytest.raises(KeyError):
        reader.lookup_normal_form(resolution=FIRST[0], pair_id="missing", normal_form_root=FIRST[2])
    reader.close()
