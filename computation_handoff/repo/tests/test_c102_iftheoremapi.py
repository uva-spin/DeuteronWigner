from __future__ import annotations

from deuteron_wigner.bridge.ifhistpublic2 import (
    historical_pair_normal_form,
    historical_primitive_record,
)
from deuteron_wigner.bridge.ifprimenum import historical_primitive_record_page
from deuteron_wigner.bridge.iftheoremapi import (
    factorized_expansion_checker_contract,
    factorized_expansion_theorem_specification,
    load_verified_factorized_semantic_theorem_authority,
    verify_factorized_expansion_equivalence,
    verify_factorized_expansion_invocation,
)
from deuteron_wigner.bridge.iftheoremapi import core
import pytest

PAIR = "C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"
RESOLUTION = "K9_2_N8_b0.40"
ORDER = "2f6268aaa6338afa0c108b2d037c6d396be31b67ca65cec10aa1f4f3d0f623a8"


def _certificates():
    page = historical_primitive_record_page(limit=2)
    rows = []
    for item in page["records"]:
        direct = historical_primitive_record(item["family_id"], item["record_id"])
        rows.append({
            "family_id": item["family_id"],
            "record_id": item["record_id"],
            "record_digest": item["record_digest"],
            "family_root": item["family_root"],
            "relation": "BYTE_IDENTICAL_SCIENTIFIC_RECORD",
            "direct_return_root": direct["return_root"],
        })
    return rows


def test_c102_delegates_once_and_returns_immutable_invocation(monkeypatch):
    historical = historical_pair_normal_form(PAIR, RESOLUTION)
    calls = []
    accepted = core._accepted_checker

    def instrumented(*args, **kwargs):
        calls.append((args, kwargs))
        return accepted(*args, **kwargs)

    monkeypatch.setattr(core, "_accepted_checker", instrumented)
    result = verify_factorized_expansion_equivalence(
        historical, historical, _certificates(),
        scientific_schema="C90-C82-SEMANTIC-IR-V1", canonical_order=ORDER,
    )
    assert len(calls) == 1
    assert result["status"] == "EXPANDED_C88_SEQUENCE_IDENTICAL_BY_FACTORIZED_SEMANTIC_PROOF"
    assert verify_factorized_expansion_invocation(result)["pass"]
    with pytest.raises(TypeError):
        result["status"] = "mutate"
    core._authority.cache_clear()


def test_c102_never_replaces_the_accepted_checker_and_negative_reaches_it(monkeypatch):
    historical = historical_pair_normal_form(PAIR, RESOLUTION)
    changed = dict(historical["normal_form"])
    changed["cardinality"] = int(changed["cardinality"]) + 1
    calls = []
    accepted = core._accepted_checker

    def instrumented(*args, **kwargs):
        calls.append(True)
        return accepted(*args, **kwargs)

    monkeypatch.setattr(core, "_accepted_checker", instrumented)
    result = verify_factorized_expansion_equivalence(
        historical, changed, _certificates(),
        scientific_schema="C90-C82-SEMANTIC-IR-V1", canonical_order=ORDER,
    )
    assert calls == [True]
    assert result["status"] == "C94_PUBLIC_CHECKER_NONPOSITIVE"
    core._authority.cache_clear()


def test_c102_public_authority_and_contract_are_bound_to_c94():
    authority = load_verified_factorized_semantic_theorem_authority()
    theorem = factorized_expansion_theorem_specification()
    contract = factorized_expansion_checker_contract()
    assert authority["theorem_root"] == theorem["theorem_root"] == contract["theorem_root"]
    assert contract["accepted_import_path"] == "deuteron_wigner.bridge.ifequivapi2.verify_factorized_expansion_equivalence"
    assert contract["no_reimplementation"]
