from deuteron_wigner.bridge.ifprimenum import historical_primitive_domain_manifest, historical_primitive_record_page
from deuteron_wigner.bridge.ifhistpublic2 import historical_primitive_record
from deuteron_wigner.bridge.ifprimenum import core
import pytest

def plain(value):
    if hasattr(value, "items"): return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)): return [plain(item) for item in value]
    return value

def test_c100_domain_and_paginated_identities_are_authenticated():
    domain = historical_primitive_domain_manifest()
    page = historical_primitive_record_page(limit=2)
    assert domain["family_order"] == ("C77", "C78", "C80", "C82", "C87")
    assert domain["record_count"] == 35
    assert len(page["records"]) == 2 and page["next_cursor"]
    item = page["records"][0]
    direct = historical_primitive_record(item["family_id"], item["record_id"])
    assert direct["record_digest"] == item["record_digest"]
    with pytest.raises(TypeError): page["records"][0]["record_id"] = "mutate"

def test_c100_cursor_is_root_bound_and_corruption_fails_closed():
    page = plain(historical_primitive_record_page(limit=1))
    with pytest.raises(ValueError): historical_primitive_record_page(limit=1, cursor=page["next_cursor"] + "x")
    with pytest.raises(ValueError): historical_primitive_record_page(limit=2, cursor=page["next_cursor"])

def test_c100_missing_runtime_fails_closed_without_c98_index_fallback(monkeypatch, tmp_path):
    original = core.RUNTIME
    core._manifest.cache_clear(); core._domain.cache_clear()
    monkeypatch.setattr(core, "RUNTIME", tmp_path)
    with pytest.raises(ValueError): historical_primitive_domain_manifest()
    monkeypatch.setattr(core, "RUNTIME", original)
    core._manifest.cache_clear(); core._domain.cache_clear()
