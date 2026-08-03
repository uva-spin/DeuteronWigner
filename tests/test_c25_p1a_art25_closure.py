from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.process.p1a.core import ART25MemberParser, FREE_NAMES, injection_rows

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
REP = ROOT / "data/raw/c25_sources/git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep"


def test_official_member_contract_and_independent_statistics():
    ensemble, report = ART25MemberParser().parse(REP)
    assert report.declared_stochastic == report.parsed_stochastic == 642
    assert len(FREE_NAMES) == 22 and len(ensemble.central.raw_np_parameters) == 28
    assert ensemble.central.collinear.pdf == ensemble.central.collinear.pion_ff == ensemble.central.collinear.kaon_ff == 0
    assert [m.member_id.index for m in ensemble.stochastic] == list(range(1, 643))
    a = np.array([m.free_parameters for m in ensemble.stochastic])
    assert np.allclose(ensemble.statistics()["mean"], np.mean(a, axis=0), rtol=0, atol=0)
    assert report.ensemble_content_sha256 == ensemble.content_hash
    published = json.loads((DOCS / "c25_art25_parameter_reproduction.json").read_text())
    assert published["maximum_published_rounding_residual"] < 0.03


def test_parser_rejects_dropped_row(tmp_path: Path):
    lines = REP.read_text().splitlines()
    p = tmp_path / "broken.rep"
    p.write_text("\n".join(lines[:-1]) + "\n")
    with pytest.raises(ValueError, match="C25.MEMBER.ROW_COUNT"):
        ART25MemberParser().parse(p)


def test_c25_manifests_close_and_fail_closed():
    validation = json.loads((DOCS / "c25_art25_member_validation.json").read_text())
    gates = json.loads((DOCS / "c25_source_gate_report.json").read_text())
    regression = json.loads((DOCS / "c25_regression_report.json").read_text())
    assert validation["parsed_stochastic"] == 642
    assert gates["source_process_eligible"] == gates["physical_input_eligible"] == 0
    assert regression["production_registry"] == 216 and regression["all_artifacts_unchanged"]


def test_all_960_ordered_injections_detected():
    rows = injection_rows()
    assert len(rows) == 960
    assert [r["ordinal"] for r in rows] == list(range(1, 961))
    assert all(r["status"] == "PASS_DETECTED" for r in rows)
