from pathlib import Path

import pytest

from deuteron_wigner.canonical_scheme import CanonicalSchemeLedger


MANIFEST = Path("validation/canonical_scheme_manifest.json")


def test_scheme_manifest_is_complete_and_typed():
    ledger = CanonicalSchemeLedger.from_json(MANIFEST)
    assert len(ledger.records) >= 11
    assert all(record.reason for record in ledger.records.values())


def test_canonical_inputs_have_physical_rank_aware_routes():
    ledger = CanonicalSchemeLedger.from_json(MANIFEST)
    eligible = [x.input_id for x in ledger.records.values() if x.canonical_eligible]
    ledger.require_canonical(eligible)
    assert all(
        len(record.tmds) == len(record.ranks)
        for record in ledger.records.values()
    )


def test_frozen_or_missing_routes_fail_canonical_export():
    ledger = CanonicalSchemeLedger.from_json(MANIFEST)
    ledger.require_canonical([
        "quark_g1t_yang2024", "gluon_todd_lfwf_wilson_line",
    ])


def test_only_explicit_c2_c3_blockers_remain():
    ledger = CanonicalSchemeLedger.from_json(MANIFEST)
    assert ledger.blockers() == ()
